from ship.message import *
from ship.states import *


# Section: 13.4.4.3.5.2
class PinState(Enum):
    SME_PIN_STATE_CHECK = auto()
    SME_PIN_STATE_ASK = auto()


# Section: 13.4.4.3.5.2
class PinSubState(Enum):
    # SME_PIN_STATE_CHECK
    SME_PIN_STATE_CHECK_INIT = auto()
    SME_PIN_STATE_CHECK_LISTEN = auto()
    SME_PIN_STATE_CHECK_ERROR = auto()
    SME_PIN_STATE_CHECK_BUSY_INIT = auto()
    SME_PIN_STATE_CHECK_BUSY_WAIT = auto()
    SME_PIN_STATE_CHECK_OK = auto()
    # SME_PIN_STATE_ASK
    SME_PIN_STATE_ASK_INIT = auto()
    SME_PIN_STATE_ASK_PROCESS = auto()
    SME_PIN_STATE_ASK_RESTRICTED_OK = auto()
    SME_PIN_STATE_ASK_OK = auto()


class HandlePin:

    def __init__(self, con):
        self._con = con
        self._pin_state: PinState = PinState.SME_PIN_STATE_ASK
        self._pin_sub_state: PinSubState = PinSubState.SME_PIN_STATE_ASK_INIT

    def set_pin_sub_state(self, state: PinSubState):
        self._pin_sub_state = state

    @property
    def pin_state(self):
        return self._pin_state

    @property
    def pin_sub_state(self):
        return self._pin_sub_state

    def handle_state(self, msg: ShipMessage) -> bool:
        print(f"handle pin state: {self.pin_state}/{self.pin_sub_state}")
        if self.pin_state == PinState.SME_PIN_STATE_ASK:
            if self.pin_sub_state == PinSubState.SME_PIN_STATE_ASK_INIT:
                return self.handle_state_sme_pin_state_ask_init()
            elif self.pin_sub_state == PinSubState.SME_PIN_STATE_ASK_PROCESS:
                return self.handle_state_sme_pin_state_ask_process(msg)
            elif self.pin_sub_state == PinSubState.SME_PIN_STATE_ASK_OK:
                # End of handler
                self._con.set_con_state(ConState.DATA_AND_ACCESS_METHODS)
                return True
            else:
                return False
        else:
            return False

    def handle_state_sme_pin_state_ask_init(self):
        self._con.send_message(ConnectionPinState(pin_state=PinStateType.NONE))
        self.set_pin_sub_state(PinSubState.SME_PIN_STATE_ASK_PROCESS)

        return False

    def handle_state_sme_pin_state_ask_process(self, msg: ShipMessage):
        if not isinstance(msg, ConnectionPinState):
            print(f"Wrong message type expected: ConnectionPinState received: {type(msg)}")
            self._con.close()
            return False
        if msg.msg().pin_state != PinStateType.NONE:
            print(f"Wrong message value expected NONE received: {msg.msg().pin_state}")
            self._con.close()
            return False
        self.set_pin_sub_state(PinSubState.SME_PIN_STATE_ASK_OK)
        return True









