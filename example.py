import time
from pathlib import Path
from typing import cast

import inquirer

from ship.mdns_announce import MdnsAnnounceService
from ship.mdsn_scanner import MdnsScannerService

if __name__ == "__main__":

    try:
        file_path = Path('key.cert')
        pem_data = file_path.read_bytes()

        #print(pem_data)

        runner = MdnsAnnounceService(
            device_id="TESTBRAND11314235241414",
            tls_cert=pem_data,
            interfaces=["WLAN", ""]
        )

        runner.start()

        srv = MdnsScannerService()
        srv = srv.search_devices(5)
        devices = ["-- Query again --"]
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

            devices.append((f"{name}-{info.properties.get('ski')}",info))

        questions = [
            inquirer.List('device',
                          message="Which device do you want to connect with?",
                          choices=devices
                          ),
        ]
        answers = inquirer.prompt(questions)

        addresses = [f"{addr}:{cast(int, info.port)}" for addr in answers['device'].parsed_scoped_addresses()]
        print(f"you have selected: {answers['device'].name} ski: {answers['device'].properties.get(b'ski')} Adresses: {', '.join(addresses)}")
        #print(f"you have selected: {srv.items()[answers]}")


    finally:
        runner.stop()
