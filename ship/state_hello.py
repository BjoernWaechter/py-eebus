
from ship.message import *
from ship.states import *


class HelloState(Enum):
    NO_STATE = auto()
    SME_HELLO_STATE_READY = auto()
    SME_HELLO_STATE_PENDING = auto()


# Ship section 13.4.3 & 13.4.4.1.3
class HelloSubState(Enum):
    # CMI_STATE:
    # CMI_STATE_CLIENT_SEND = auto()
    # CMI_STATE_CLIENT_WAIT = auto()
    # CMI_STATE_CLIENT_EVALUATE = auto()

    # SME_HELLO_STATE:
    SME_HELLO_STATE_READY_INIT = auto()
    SME_HELLO_STATE_READY_LISTEN = auto()
    SME_HELLO_STATE_OK = auto()
    SME_HELLO_STATE_READY_TIMEOUT = auto()

    SME_HELLO_STATE_PENDING_INIT = auto()
    SME_HELLO_STATE_PENDING_LISTEN = auto()
    SME_HELLO_STATE_PENDING_TIMEOUT = auto()


class HandleHello:

    def __init__(self, con, partner_known: bool):
        self.con = con
        if partner_known:
            self._hello_state: HelloState = HelloState.SME_HELLO_STATE_READY
            self._hello_sub_state: HelloSubState = HelloSubState.SME_HELLO_STATE_READY_INIT
        else:
            self._hello_state: HelloState = HelloState.SME_HELLO_STATE_PENDING
            self._hello_sub_state: HelloSubState = HelloSubState.SME_HELLO_STATE_PENDING_INIT

    def set_hello_state(self, state: HelloState):
        self._hello_state = state

    def set_hello_sub_state(self, sub_state: HelloSubState):
        self._hello_sub_state = sub_state

    @property
    def hello_state(self):
        return self._hello_state

    @property
    def hello_sub_state(self):
        return self._hello_sub_state

    def handle_state(self, msg: ShipMessage) -> bool:
        print(f"handle helo state: {self.hello_state}/{self.hello_sub_state}")
        if self.hello_state == HelloState.SME_HELLO_STATE_PENDING:
            if self.hello_sub_state == HelloSubState.SME_HELLO_STATE_PENDING_INIT:

                # TODO Server mode
                return self.handle_state_sme_hello_state_pending_init(msg)

            elif self.hello_sub_state == HelloSubState.SME_HELLO_STATE_PENDING_LISTEN:

                return self.handle_state_sme_hello_state_pending_listen(msg)

            elif self.hello_sub_state == HelloSubState.SME_HELLO_STATE_OK:

                self.con.set_con_state(ConState.PROTOCOL_HANDSHAKE)
                return True

            else:
                print("Message not handled")
                return False


        else:
            return False

    def handle_state_sme_hello_state_pending_init(self, msg: ShipMessage):
        self.con.send_message(ConnectionHello(phase=ConnectionHelloPhaseType.READY))
        self.set_hello_sub_state(HelloSubState.SME_HELLO_STATE_PENDING_LISTEN)
        return False

    def handle_state_sme_hello_state_pending_listen(self, msg: ConnectionHello):
        if not isinstance(msg, ConnectionHello):
            print(f"Wrong message type expected: ConnectionHello received: {type(msg)}")
            self.con.close()
            return False
        if msg.msg().phase != ConnectionHelloPhaseType.READY:
            print(f"Wrong message value expected READY received: {msg.msg().phase}")
            self.con.close()
            return False
        if msg.msg().phase == ConnectionHelloPhaseType.READY and msg.msg().waiting is None:
            print(f"Waiting should be set in in phase pending: {msg.msg().phase}")
            self.con.close()
            return False

        # self.con.send_message(MessageProtocolHandshake(handshake_type=ProtocolHandshakeTypeType.ANNOUNCEMAX))
        self.set_hello_sub_state(HelloSubState.SME_HELLO_STATE_OK)
        return True






