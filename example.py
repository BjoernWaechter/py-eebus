import time
from pathlib import Path
from pprint import pprint
from typing import cast

import inquirer

from ship.connection import ShipConnection
from ship.mdns_announce import MdnsAnnounceService
from ship.mdsn_scanner import MdnsScannerService

if __name__ == "__main__":

    try:
        file_path = Path('key.cert')
        pem_data = file_path.read_bytes()

        #print(pem_data)

        runner = MdnsAnnounceService(
            device_id="MY_TEST_DEVICE_123",
            tls_cert=pem_data,
            interfaces=["WLAN", ""]
        )

        runner.start()

        srv = MdnsScannerService()
        devices = srv.search_devices(5)
        select_devices = ["-- Query again --"]
        for device in devices:

            select_devices.append((device.name, device))

        questions = [
            inquirer.List('device',
                          message="Which device do you want to connect with?",
                          choices=select_devices
                          ),
        ]
        answer = inquirer.prompt(questions)

        pprint(answer)

        con = ShipConnection(device=answer["device"], client_key="key.priv", client_cert="key.cert")
        # time.sleep(20)
        # con = ShipConnection(device=devices[0], client_key="key.priv", client_cert="key.cert")

        con.connect()


    finally:
        con.close()
        runner.stop()
