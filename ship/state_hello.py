
from ship.message import *
from ship.states import *


class HandleHello:

    def __init__(self, con):
        self.con = con

    def handle_state(self, msg: ShipMessage):
        if self.con.basic_state == BasicState.SME_HELLO_STATE_READY:
            if self.con.sub_state == SubState.SME_HELLO_STATE_READY_INIT:

                # TODO Server mode
                self.handle_state_sme_hello_state_ready_init(msg)
                self.con.set_sub_state(SubState.SME_HELLO_STATE_READY_LISTEN)

            elif self.con.sub_state == SubState.SME_HELLO_STATE_READY_LISTEN:

                self.handle_state_sme_hello_state_ready_listen(msg)

            else:
                print("Message not handled")

    def handle_state_sme_hello_state_ready_init(self, msg: ShipMessage):
        self.con.send_message(ConnectionHello(phase=ConnectionHelloPhaseType.READY))
        self.con.set_sub_state(SubState.SME_HELLO_STATE_READY_LISTEN)

    def handle_state_sme_hello_state_ready_listen(self, msg: ShipMessage):
        if not isinstance(msg, ConnectionHello):
            print(f"Wrong message type expected: ConnectionHello received: {type(msg)}")
            self.con.close()
        if msg.msg().phase != ConnectionHelloPhaseType.READY:
            print(f"Wrong message value expected READY received: {msg.msg().phase}")
            self.con.close()
        self.con.send_message(MessageProtocolHandshake(handshake_type=ProtocolHandshakeTypeType.ANNOUNCEMAX))
        self.con.set_sub_state(SubState.SME_HELLO_STATE_OK)






