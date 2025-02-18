import time
from pathlib import Path
from pprint import pprint
from typing import cast

import inquirer

from ship.connection import ShipConnection
from ship.device import ShipDevice
from ship.mdns_announce import MdnsAnnounceService
from ship.mdsn_scanner import MdnsScannerService

if __name__ == "__main__":

    cert_path = 'f90d886eb34325082f7513bbdcc03ae2609a7625.cert'
    key_path = 'f90d886eb34325082f7513bbdcc03ae2609a7625.priv'

    try:
        #file_path = Path('f90d886eb34325082f7513bbdcc03ae2609a7625.cert')
        file_path = Path(cert_path)
        pem_data = file_path.read_bytes()

        local_device_name = "Bjoerns_Dev"

        runner = MdnsAnnounceService(
            device_id=local_device_name,
            tls_cert=pem_data,
            interfaces=["WLAN"]
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

        con = ShipConnection(
            local_device=ShipDevice(
                name=local_device_name,
                ski="",
                ip_addresses=[],
                port=None,
                model=None,
                type=None,
                id=None,
                path=None
            ),
            remote_device=answer["device"],
            client_key=key_path,
            client_cert=cert_path,
            partner_known=True
        )
        # time.sleep(20)
        # con = ShipConnection(device=devices[0], client_key="key.priv", client_cert="key.cert")

        con.connect()

    finally:
        con.close()
        runner.stop()
