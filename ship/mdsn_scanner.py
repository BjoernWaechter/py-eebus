import time

from zeroconf import ServiceBrowser, ServiceListener, Zeroconf
from typing import cast


class MdnsServiceListener(ServiceListener):

    def __init__(self):
        self._service_entries = {}

    def get_services(self):
        return self._service_entries

    def clear_services(self):
        self._service_entries = {}

    def update_service(self, zc: Zeroconf, type_: str, name: str) -> None:
        print(f"Service {name} updated")
        info = zc.get_service_info(type_, name)
        self._service_entries[name] = info

    def remove_service(self, zc: Zeroconf, type_: str, name: str) -> None:
        print(f"Service {name} removed")
        self._service_entries.pop(name, None)

    def add_service(self, zc: Zeroconf, type_: str, name: str) -> None:
        info = zc.get_service_info(type_, name)
        self._service_entries[name] = info


class MdnsScannerService:

    def __init__(self):
        self.zeroconf = Zeroconf()
        self.listener = MdnsServiceListener()

    def search_devices(self, duration_sec=15):
        self.listener.clear_services()
        browser = ServiceBrowser(self.zeroconf, "_ship._tcp.local.", self.listener)
        time.sleep(duration_sec)
        browser.cancel()
        return self.listener.get_services()


if __name__ == "__main__":
    srv = MdnsScannerService()
    srv = srv.search_devices()

    for name, info in srv.items():

        print(f"Service {name} added, service info: {info}")
        addresses = [f"{addr}:{cast(int, info.port)}" for addr in info.parsed_scoped_addresses()]
        print(f"  Name: {name}")
        print(f"  Addresses: {', '.join(addresses)}")
        print(f"  Weight: {info.weight}, priority: {info.priority}")
        print(f"  Server: {info.server}")
        if info.properties:
            print("  Properties are:")
            for key, value in info.properties.items():
                print(f"    {key!r}: {value!r}")
        else:
            print("  No properties")

