from unittest.mock import patch

from ship.connection import ShipConnection
from ship.device import ShipDevice
from ship.enums import ConnectionHelloPhaseType
from ship.message import ConnectionHello
from ship.state_hello import HandleHello, HelloState, HelloSubState
from ship.states import ConState


class TestHandleHello:

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

        con.set_con_state(ConState.SME_HELLO_STATE)

        con.handle_state()

        mock_send_message.assert_called_with(ConnectionHello(phase=ConnectionHelloPhaseType.READY))
        assert con.handle_hello.hello_state == HelloState.SME_HELLO_STATE_PENDING
        assert con.handle_hello.hello_sub_state == HelloSubState.SME_HELLO_STATE_PENDING_LISTEN

        con.on_message(None, ConnectionHello(phase=ConnectionHelloPhaseType.READY).get_msg_bytes())

        assert con.handle_hello.hello_state == HelloState.SME_HELLO_STATE_PENDING
        assert con.handle_hello.hello_sub_state == HelloSubState.SME_HELLO_STATE_OK

        assert con.con_state == ConState.PROTOCOL_HANDSHAKE

        # # Step 2
        # cmi.handle_state(Cmi())
        # assert cmi.cmi_state == CmiState.CMI_STATE_DONE

