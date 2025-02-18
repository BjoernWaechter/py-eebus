import logging
import socket
import ssl
import time

import rel
import websocket
from cryptography.x509 import Certificate, Extension

from ship.device import ShipDevice
from ship.message import *
from ship.state_access_methods import HandleAccessMethods
from ship.state_cmi import HandleCMI
from ship.state_hello import HandleHello
from ship.state_pin import HandlePin
from ship.state_protocol import HandleProtocol
from ship.states import *
from ship.timer import ShipTimer

from cryptography import x509

from tools.logger import CustomFormatter, record_factory

logger = logging.getLogger(__name__)
logging.setLogRecordFactory(record_factory)
logger.setLevel(logging.DEBUG)

# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

ch.setFormatter(CustomFormatter())
logger.addHandler(ch)


class ShipConnection:

    def __init__(
            self,
            local_device: ShipDevice,
            remote_device: ShipDevice,
            client_cert: str,
            client_key: str,
            t_hello_init=60,
            partner_known: bool = False,
            client_server: ClientServer = ClientServer.CLIENT
    ):

        self._local_device = local_device
        self._remote_device = remote_device
        # Start Ship section: 13.4.3
        self.cmi_timer = ShipTimer(duration_sec=30)
        # End Ship section: 13.4.3

        # Start Ship section: 13.4.4.1.3
        self.con_state: ConState = None
        self.t_hello_init = t_hello_init
        self.t_hello_inc = self.t_hello_init
        self.t_hello_prolong_thr_inc = 30
        self.t_hello_prolong_waiting_gap = 15
        self.t_hello_prolong_min = 1

        self.wait_for_ready_timer = ShipTimer(duration_sec=self.t_hello_init)
        self.send_prolongation_request_timer = ShipTimer()
        self.prolongation_request_reply_timer = ShipTimer()
        # End Ship section: 13.4.4.1.3

        self.client_cert = client_cert
        self.client_key = client_key

        self.server_cert: Certificate = None
        self.ws = None

        self.partner_known = partner_known
        self._client_server = client_server

        self._handle_cmi = HandleCMI(con=self, client_server=self._client_server)
        self._handle_hello = HandleHello(con=self, partner_known=partner_known)
        self._handle_protocol_handshake = HandleProtocol(con=self)
        self._handle_pin = HandlePin(con=self)
        self._handle_access_methods = HandleAccessMethods(con=self)

    def set_con_state(self, con_state: ConState):
        self.con_state = con_state

    def send_message(self, msg: ShipMessage):
        logger.debug(f"SEND msg: {msg}", extra={"color": CustomFormatter.green})
        self.ws.send_bytes(msg.get_msg_bytes())

    def handle_state(self, msg: ShipMessage = None, reason="RECV"):
        print(f"{reason} handle state: {self.con_state} msg: {msg}")

        handling_ongoing = True
        while handling_ongoing:

            if self.con_state == ConState.CMI_STATE:
                self._handle_cmi.start_handler()
                handling_ongoing = self._handle_cmi.handle_state(msg=msg)
            elif self.con_state == ConState.SME_HELLO_STATE:
                self._handle_hello.start_handler()
                handling_ongoing = self._handle_hello.handle_state(msg=msg)
            elif self.con_state == ConState.PROTOCOL_HANDSHAKE:
                handling_ongoing = self._handle_protocol_handshake.handle_state(msg=msg)
            elif self.con_state == ConState.PIN_VERIFICATION:
                handling_ongoing = self._handle_pin.handle_state(msg=msg)
            elif self.con_state == ConState.DATA_AND_ACCESS_METHODS:
                if (isinstance(msg, AccessMethodsRequest) or
                        isinstance(msg, AccessMethods) or
                        self._handle_access_methods.request_send is False):
                    handling_ongoing = self._handle_access_methods.handle_state(msg=msg)

    def on_message(self, ws, message):
        #logger.debug(f"RECV raw: {message}", extra={"color": CustomFormatter.red})
        msg = ShipMessage.from_data(message)
        logger.debug(f"RECV msg: {msg}", extra={"color": CustomFormatter.red})

        self.handle_state(msg, "RECV")

    def on_error(self, ws, error):
        print(f"error: {error}")

    def on_close(self, ws, close_status_code, close_msg):
        print(f"closed: {close_status_code} / {close_msg}")

    def on_open(self, ws):
        print("Opened connection")

    def _check_server_certificate(self):
        ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
        ssl_context.check_hostname = False
        ssl_context.verify_mode = ssl.CERT_NONE
        ssl_context.load_cert_chain(
            certfile=self.client_cert,
            keyfile=self.client_key
        )

        sock = ssl_context.wrap_socket(socket.socket(), server_hostname=self._remote_device.ip_addresses[0])
        sock.connect((self._remote_device.ip_addresses[0], int(self._remote_device.port)))
        der = sock.getpeercert(binary_form=True)
        pem = ssl.DER_cert_to_PEM_cert(der)
        self.server_cert = x509.load_pem_x509_certificate(pem.encode("utf-8"))
        ski: Extension = self.server_cert.extensions.get_extension_for_oid(x509.oid.ExtensionOID.SUBJECT_KEY_IDENTIFIER)
        print(ski.value.digest.hex())

        # TODO: Save certificate to use for verification later. Prevent man in the middle e.g.
        if ski.value.digest.hex() != self._remote_device.ski:
            raise RuntimeError(
                f"Ski announced via MDNS does not match ski in server certificate: {ski.value.digest.hex()} != {self._remote_device.ski}")

    def close(self):
        self.ws.close()

    def connect(self):

        logger.debug("test", extra={"color": CustomFormatter.red})

        websocket.enableTrace(False)
        header = "Sec-WebSocket-Protocol: ship"
        self.ws = websocket.WebSocketApp(
            f"wss://{self._remote_device.ip_addresses[0]}:{self._remote_device.port}{self._remote_device.path}",
            on_open=self.on_open,
            on_message=self.on_message,
            on_error=self.on_error,
            on_close=self.on_close,
            header=[header]
        )

        self._check_server_certificate()

        ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
        ssl_context.check_hostname = False
        ssl_context.verify_mode = ssl.CERT_NONE
        ssl_context.load_cert_chain(
            certfile=self.client_cert,
            keyfile=self.client_key
        )

        self.ws.run_forever(
            dispatcher=rel,
            reconnect=5,
            sslopt={
                "context": ssl_context
            }
        )
        # b = Cmi().get_msg_bytes()
        # print(b)

        # self.wait_for_ready_timer.start()
        # self.send_prolongation_request_timer.stop()
        # self.prolongation_request_reply_timer.stop()

        # Ship section 13.4.3
        self.cmi_timer.start()
        self.con_state = ConState.CMI_STATE
        # self.send_message(Cmi())
        self.handle_state(reason="INIT")

        rel.signal(2, rel.abort)  # Keyboard Interrupt
        rel.dispatch()

        time.sleep(4)
