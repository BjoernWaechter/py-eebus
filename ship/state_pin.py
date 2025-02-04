
from ship.message import *
from ship.states import *


# Section: 13.4.4.2.3
class PinState(Enum):
    SME_PIN_STATE_CHECK_INIT = auto()
    SME_PIN_STATE_CHECK_LISTEN = auto()
    SME_PIN_STATE_CHECK_ERROR = auto()
    SME_PIN_STATE_CHECK_BUSY_INIT = auto()
    SME_PIN_STATE_CHECK_BUSY_WAIT = auto()
    SME_PIN_STATE_CHECK_OK = auto()
    SME_PIN_STATE_ASK_INIT = auto()
    SME_PIN_STATE_ASK_PROCESS = auto()
    SME_PIN_STATE_ASK_RESTRICTED_OK = auto()
    SME_PIN_STATE_ASK_OK = auto()


class HandlePin:

    def __init__(self, con):
        self.con = con
        self._pin_state: PinState = PinState.SME_PIN_STATE_CHECK_INIT

    def set_pin_state(self, state: PinState):
        self._pin_state = state

    @property
    def pin_state(self):
        return self._pin_state

    def handle_state(self, msg: ShipMessage) -> bool:
        print(f"handle pin state: {self.pin_state}")
        if self.pin_state == ProtocolState.SME_PROT_H_STATE_CLIENT_INIT:

            return self.handle_state_sme_prot_h_state_client_init()

        elif self.pin_state == ProtocolState.SME_PROT_H_STATE_CLIENT_LISTEN_CHOICE:

            return self.handle_state_sme_prot_h_state_client_listen_choice(msg)

        else:
            return False

    def handle_state_sme_prot_h_state_client_init(self):

        self.con.send_message(MessageProtocolHandshake(handshake_type=ProtocolHandshakeTypeType.ANNOUNCEMAX))
        # TODO: init wait timer

        self.set_proto_state(ProtocolState.SME_PROT_H_STATE_CLIENT_LISTEN_CHOICE)
        return False

    def handle_state_sme_prot_h_state_client_listen_choice(self, msg: MessageProtocolHandshake):
        # TODO: deactivate timer
        if not isinstance(msg, MessageProtocolHandshake):
            print(f"Wrong message type expected: ConnectionHello received: {type(msg)}")
            self.con.close()
            return False
        if msg.msg().handshake_type != ProtocolHandshakeTypeType.SELECT:
            print(f"Wrong message value expected READY received: {msg.msg().phase}")
            self.con.close()
            return False
        # TODO: check version
        # TODO: check formats
        self.con.send_message(msg)
        self.set_proto_state(ProtocolState.SME_PROT_H_STATE_CLIENT_OK)








