from dataclasses import dataclass
from enum import Enum, auto


class ConState(Enum):
    CMI_STATE = auto()
    SME_HELLO_STATE = auto()
    PROTOCOL_HANDSHAKE = auto()
    PIN_VERIFICATION = auto()
    DATA_AND_ACCESS_METHODS = auto()

class ClientServer(Enum):
    CLIENT = auto()
    SERVER = auto()