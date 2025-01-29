from __future__ import annotations

import asyncio
from pathlib import Path

from zeroconf import IPVersion, ServiceInfo
from zeroconf.asyncio import AsyncZeroconf
from cryptography import x509
from cryptography.hazmat.backends import default_backend

import socket
import psutil
import time


def get_ip_addresses(family: socket.AddressFamily, interfaces=None):
    for iface, snics in psutil.net_if_addrs().items():
        if interfaces is None or iface in interfaces:
            for snic in snics:
                if snic.family == family:
                    yield snic.address


class MdnsAnnounceService:

    def __init__(
            self,
            device_id: str,
            tls_cert,
            device_brand: str = None,
            device_type: str = None,
            device_model: str = None,
            ip_version: IPVersion = IPVersion.All,
            interfaces: list[str] = None
    ):
        self.ip_version = ip_version
        ipv4s = []
        ipv6s = []
        if self.ip_version in [IPVersion.All, IPVersion.V4Only]:
            ipv4s = list(get_ip_addresses(socket.AF_INET, interfaces))
        if self.ip_version in [IPVersion.All, IPVersion.V6Only]:
            ipv6s = list(get_ip_addresses(socket.AF_INET6, interfaces))

        cert = x509.load_pem_x509_certificate(tls_cert, default_backend())
        ski: x509.extensions.Extension = cert.extensions.get_extension_for_oid(x509.oid.ExtensionOID.SUBJECT_KEY_IDENTIFIER)

        ski_str = ski.value.digest.hex()

        mdns_properties = {
            "txtvers": "1",
            "id": device_id,
            "path": "/ship/",
            "ski": ski_str,
            "register": "true"
        }

        if device_brand:
            mdns_properties["brand"] = device_brand
        if device_type:
            mdns_properties["type"] = device_type
        if device_model:
            mdns_properties["model"] = device_model

        self.name = f"{device_id}._ship._tcp.local."

        self.mdsn_info = ServiceInfo(
            type_="_ship._tcp.local.",
            name=self.name,
            parsed_addresses=ipv4s+ipv6s,
            port=47051,
            properties=mdns_properties,
            server=f"eebus.local."
        )

        self.aiozc = AsyncZeroconf(ip_version=self.ip_version)

        self.loop = asyncio.new_event_loop()

    def start(self):
        self.loop.run_until_complete(self._register_services())

    def stop(self):
        self.loop.run_until_complete(self._unregister_services())

    async def _register_services(self) -> None:
        self.aiozc = AsyncZeroconf(ip_version=self.ip_version)
        tasks = [self.aiozc.async_register_service(self.mdsn_info) ]
        background_tasks = await asyncio.gather(*tasks)
        await asyncio.gather(*background_tasks)

    async def _unregister_services(self) -> None:
        assert self.aiozc is not None
        tasks = [self.aiozc.async_unregister_service(self.mdsn_info)]
        background_tasks = await asyncio.gather(*tasks)
        await asyncio.gather(*background_tasks)
        await self.aiozc.async_close()


if __name__ == "__main__":
    file_path = Path('../key.cert')
    pem_data = file_path.read_bytes()

    print(pem_data)

    runner = MdnsAnnounceService(
        device_id="TESTBRAND11314235241414",
        tls_cert=pem_data,
        interfaces=["WLAN", ""]
    )

    runner.start()
    time.sleep(30)
    runner.stop()



