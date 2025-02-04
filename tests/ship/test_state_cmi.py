from unittest.mock import patch

from ship.connection import ShipConnection
from ship.device import ShipDevice
from ship.message import Cmi
from ship.state_cmi import HandleCMI, CmiState


class TestHandleCMI:

    @patch("ship.connection.ShipConnection.send_message")
    def test_ok_flow(self, mock_send_message):
        mock_send_message.return_value = ""

        device = ShipDevice(
            name="",
            ski="",
            ip_addresses=[""],
            port=5431,
            model="",
            type="",
            id="",
            path="",
        )
        con = ShipConnection(device=device, client_cert="my.cert", client_key="my.key")

        cmi = HandleCMI(con=con)

        # Step 1
        cmi.handle_state()

        mock_send_message.assert_called_with(Cmi())
        assert cmi.cmi_state == CmiState.CMI_STATE_CLIENT_WAIT

        # Step 2
        cmi.handle_state(Cmi())
        assert cmi.cmi_state == CmiState.CMI_STATE_DONE


