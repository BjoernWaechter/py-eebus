from ship.message import *
from ship.states import *


class HandleCMI:

    def __init__(self, con):
        self.con = con

    def handle_state(self, msg: ShipMessage):
        if self.con.sub_state == SubState.CMI_STATE_CLIENT_SEND:
            self.handle_state_cmi_state_client_send(msg)
        elif self.con.sub_state == SubState.CMI_STATE_CLIENT_WAIT:
            self.handle_state_cmi_state_client_wait(msg)
        else:
            print("Message not handled")

    def handle_state_cmi_state_client_send(self, msg: ShipMessage):
        self.con.send_message(Cmi())
        self.con.set_sub_state(SubState.CMI_STATE_CLIENT_WAIT)

    def handle_state_cmi_state_client_wait(self, msg: ShipMessage):
        # Ship section 13.4.3
        self.con.set_sub_state(SubState.CMI_STATE_CLIENT_EVALUATE)
        # 3.2.1
        if not isinstance(msg, Cmi):
            print(f"Wrong message type expected: Cmi received: {type(msg)}")
            self.con.close()
        # 3.2.3
        if msg.msg() != b'\x00':
            print(f"Wrong message value expected \x00 received: {str(msg.get_data())}")
            self.con.close()

        # 3.2.2
        self.con.set_state(
            ConState.SME_HELLO_STATE,
            BasicState.SME_HELLO_STATE_READY,
            SubState.SME_HELLO_STATE_READY_INIT
        )






