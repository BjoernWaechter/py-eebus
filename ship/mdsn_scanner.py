import time
from ipaddress import ip_address
from pprint import pprint

from zeroconf import ServiceBrowser, ServiceListener, Zeroconf, ServiceInfo, IPVersion

from ship.device import ShipDevice

ZEROCONF_2_IPADDRESS_TYPE = {
    IPVersion.V4Only: 4,
    IPVersion.V6Only: 6
}


class MdnsServiceListener(ServiceListener):

    def __init__(self):
        self._service_entries = {}

    def get_services(self) -> dict[str, ServiceInfo]:
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
        print(f"Service {name} added")
        info = zc.get_service_info(type_, name)
        self._service_entries[name] = info


class MdnsScannerService:

    def __init__(self):
        self.zeroconf = Zeroconf()
        self.listener = MdnsServiceListener()

    def search_devices(self, duration_sec=10, ip_version=IPVersion.V4Only) -> list[ShipDevice]:
        self.listener.clear_services()
        browser = ServiceBrowser(self.zeroconf, "_ship._tcp.local.", self.listener)
        time.sleep(duration_sec)
        browser.cancel()


        result_devices = []
        for name, srv_info in self.listener.get_services().items():
            print(srv_info)
            result_devices.append(ShipDevice(
                name=srv_info.name,
                ski=srv_info.properties.get(b'ski').decode("utf8"),
                ip_addresses=[
                    addr for addr in srv_info.parsed_scoped_addresses()
                    if ip_version == IPVersion.All or ip_address(addr).version == ZEROCONF_2_IPADDRESS_TYPE[ip_version]
                ],
                port=srv_info.port,
                model=srv_info.properties.get(b'model').decode("utf8"),
                type=srv_info.properties.get(b'type').decode("utf8"),
                id=srv_info.properties.get(b'id').decode("utf8"),
                path=srv_info.properties.get(b'path', b'/ship/').decode("utf8"),
            ))

        return result_devices


if __name__ == "__main__":
    srv = MdnsScannerService()
    srv = srv.search_devices(ip_version=IPVersion.V4Only)

    for device in srv:

        pprint(device)

