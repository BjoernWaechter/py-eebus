
from ship.message import *
from ship.states import *


# Section: 13.4.4.2.3
class ProtocolState(Enum):
    NO_STATE = auto()
    SME_PROT_H_STATE_SERVER_INIT = auto()
    SME_PROT_H_STATE_CLIENT_INIT = auto()
    SME_PROT_H_STATE_SERVER_LISTEN_PROPOSAL = auto()
    SME_PROT_H_STATE_CLIENT_LISTEN_CHOICE = auto()
    SME_PROT_H_STATE_SERVER_LISTEN_CONFIRM = auto()
    SME_PROT_H_STATE_TIMEOUT = auto()
    SME_PROT_H_STATE_CLIENT_OK = auto()
    SME_PROT_H_STATE_SERVER_OK = auto()


class HandleProtocol:

    def __init__(self, con):
        self.con = con
        self._proto_state: ProtocolState = ProtocolState.SME_PROT_H_STATE_CLIENT_INIT

    def set_proto_state(self, state: ProtocolState):
        self._proto_state = state

    @property
    def proto_state(self):
        return self._proto_state

    def handle_state(self, msg: ShipMessage) -> bool:
        print(f"handle proto state: {self.proto_state}")
        if self.proto_state == ProtocolState.SME_PROT_H_STATE_CLIENT_INIT:

            return self.handle_state_sme_prot_h_state_client_init()

        elif self.proto_state == ProtocolState.SME_PROT_H_STATE_CLIENT_LISTEN_CHOICE:

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








