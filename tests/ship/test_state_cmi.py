import time
from unittest.mock import patch

import pytest

from ship.connection import ShipConnection
from ship.device import ShipDevice
from ship.enums import ConnectionHelloPhaseType
from ship.message import Cmi, ConnectionHello
from ship.state_cmi import HandleCMI, CmiState


class TestHandleCMI:

    @pytest.fixture
    def get_connection(self):
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

        return ShipConnection(device=device, client_cert="my.cert", client_key="my.key")

    @patch("ship.connection.ShipConnection.send_message")
    def test_ok_flow(self, mock_send_message, get_connection):
        mock_send_message.return_value = ""

        cmi = HandleCMI(con=get_connection)

        # Step 1
        cmi.handle_state()

        mock_send_message.assert_called_with(Cmi())
        assert cmi.cmi_state == CmiState.CMI_STATE_CLIENT_WAIT

        # Step 2
        cmi.handle_state(Cmi())
        assert cmi.cmi_state == CmiState.CMI_STATE_DONE

    @patch("ship.connection.ShipConnection.send_message")
    @patch("ship.connection.ShipConnection.close")
    def test_wrong_message_type(self, mock_close, mock_send_message, get_connection):
        mock_send_message.return_value = ""

        cmi = HandleCMI(con=get_connection)

        # Step 1
        cmi.handle_state()

        mock_send_message.assert_called_with(Cmi())
        assert cmi.cmi_state == CmiState.CMI_STATE_CLIENT_WAIT

        # Step 2
        cmi.handle_state(ConnectionHello(phase=ConnectionHelloPhaseType.READY))
        mock_close.assert_called_once()

    @patch("ship.connection.ShipConnection.send_message")
    @patch("ship.connection.ShipConnection.close")
    def test_wrong_message_data(self, mock_close, mock_send_message, get_connection):
        mock_send_message.return_value = ""

        cmi = HandleCMI(con=get_connection)

        # Step 1
        cmi.handle_state()

        mock_send_message.assert_called_with(Cmi())
        assert cmi.cmi_state == CmiState.CMI_STATE_CLIENT_WAIT

        cmi_msg = Cmi()
        cmi_msg._msg = b'\x01'
        cmi.handle_state(cmi_msg)
        mock_close.assert_called_once()

    @patch("ship.connection.ShipConnection.send_message")
    @patch("ship.connection.ShipConnection.close")
    def test_timeout(self, mock_close, mock_send_message, get_connection):
        mock_send_message.return_value = ""

        cmi = HandleCMI(con=get_connection, cmi_timeout=10)
        cmi._cmi_timer.set_duration(0.1)

        cmi.start_handler()
        cmi.handle_state()

        time.sleep(0.2)

        cmi.handle_state(Cmi())
        mock_send_message.assert_called_with(Cmi())
        mock_close.assert_called_once()

    @patch("ship.connection.ShipConnection.send_message")
    @patch("ship.connection.ShipConnection.close")
    def test_timeout_range(self, mock_close, mock_send_message, get_connection):
        mock_send_message.return_value = ""

        with pytest.raises(RuntimeError):
            HandleCMI(con=get_connection, cmi_timeout=9)

        with pytest.raises(RuntimeError):
            HandleCMI(con=get_connection, cmi_timeout=31)



