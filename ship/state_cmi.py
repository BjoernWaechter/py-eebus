from ship.message import *
from ship.states import *
from ship.timer import ShipTimer


# Ship section 13.4.3
class CmiState(Enum):
    CMI_STATE_CLIENT_SEND = auto()
    CMI_STATE_CLIENT_WAIT = auto()
    CMI_STATE_CLIENT_EVALUATE = auto()
    CMI_STATE_SERVER_WAIT = auto()
    CMI_STATE_SERVER_EVALUATE = auto()
    CMI_STATE_DONE = auto()


class HandleCMI:

    def __init__(
            self,
            con,
            client_server: ClientServer = ClientServer.CLIENT,
            cmi_timeout: float = 10
    ):
        self.con = con
        self._client_server = client_server
        self._cmi_timer = ShipTimer(duration_sec=cmi_timeout)

        if self._client_server == ClientServer.CLIENT:
            self._cmi_state: CmiState = CmiState.CMI_STATE_CLIENT_SEND
        else:
            self._cmi_state: CmiState = CmiState.CMI_STATE_SERVER_WAIT

        if cmi_timeout < 10 or cmi_timeout > 30:
            raise RuntimeError(f"cmi_timeout {cmi_timeout} is not in range 10 to 30")

    def set_cmi_state(self, state: CmiState):
        self._cmi_state = state

    @property
    def cmi_state(self):
        return self._cmi_state

    def start_handler(self):
        self._cmi_timer.start()

    def handle_state(self, msg: ShipMessage = None) -> bool:

        if self._cmi_timer.is_expired():
            self.con.close()
            return False

        if self.cmi_state == CmiState.CMI_STATE_CLIENT_SEND:
            return self.handle_state_cmi_state_client_send(msg)
        elif self.cmi_state == CmiState.CMI_STATE_CLIENT_WAIT:
            return self.handle_state_cmi_state_client_wait(msg)
        else:
            print("Message not handled")
            return False

    def handle_state_cmi_state_client_send(self, msg: ShipMessage):
        self.con.send_message(Cmi())
        self.set_cmi_state(CmiState.CMI_STATE_CLIENT_WAIT)
        return False

    def handle_state_cmi_state_client_wait(self, msg: ShipMessage):
        # Ship section 13.4.3
        self.set_cmi_state(CmiState.CMI_STATE_CLIENT_EVALUATE)
        # 3.2.1
        if not isinstance(msg, Cmi):
            print(f"Wrong message type expected: Cmi received: {type(msg)}")
            self.con.close()
            return False
        # 3.2.3
        if msg.msg() != b'\x00':
            print(f"Wrong message value expected \x00 received: {msg._msg}")
            self.con.close()
            return False

        self.set_cmi_state(CmiState.CMI_STATE_DONE)
        # 3.2.2
        self.con.set_con_state(ConState.SME_HELLO_STATE)
        return True
