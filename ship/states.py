from dataclasses import dataclass
from enum import Enum, auto


# Ship section 13.4.3 & 13.4.4.1.3
class ConState(Enum):
    CMI_STATE = auto()
    SME_HELLO_STATE = auto()


# Ship section 13.4.3 & 13.4.4.1.3
class BasicState(Enum):
    NO_STATE = auto()
    SME_HELLO_STATE_READY = auto()
    SME_HELLO_STATE_PENDING = auto()


# Ship section 13.4.3 & 13.4.4.1.3
class SubState(Enum):
    # CMI_STATE:
    CMI_STATE_CLIENT_SEND = auto()
    CMI_STATE_CLIENT_WAIT = auto()
    CMI_STATE_CLIENT_EVALUATE = auto()

    # SME_HELLO_STATE:
    SME_HELLO_STATE_READY_INIT = auto()
    SME_HELLO_STATE_READY_LISTEN = auto()
    SME_HELLO_STATE_OK = auto()
    SME_HELLO_STATE_READY_TIMEOUT = auto()

    SME_HELLO_STATE_PENDING_INIT = auto()
    SME_HELLO_STATE_PENDING_LISTEN = auto()
    SME_HELLO_STATE_PENDING_TIMEOUT = auto()


@dataclass
class ShipState:
    con_state: ConState
    basic_state: BasicState
    sub_state: SubState


EXPECTED_STATES: list[ShipState] = [
    ShipState(ConState.CMI_STATE, BasicState.NO_STATE, SubState.CMI_STATE_CLIENT_SEND),
    ShipState(ConState.CMI_STATE, BasicState.NO_STATE, SubState.CMI_STATE_CLIENT_WAIT),
    ShipState(ConState.CMI_STATE, BasicState.NO_STATE, SubState.CMI_STATE_CLIENT_EVALUATE),
    ShipState(ConState.SME_HELLO_STATE, BasicState.SME_HELLO_STATE_READY, SubState.SME_HELLO_STATE_READY_INIT),
    ShipState(ConState.SME_HELLO_STATE, BasicState.SME_HELLO_STATE_READY, SubState.SME_HELLO_STATE_READY_LISTEN),
    ShipState(ConState.SME_HELLO_STATE, BasicState.SME_HELLO_STATE_READY, SubState.SME_HELLO_STATE_READY_LISTEN),
    ShipState(ConState.SME_HELLO_STATE, BasicState.SME_HELLO_STATE_READY, SubState.SME_HELLO_STATE_OK),

]