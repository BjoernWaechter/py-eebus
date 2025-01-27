from enum import Enum


class MessageType(bytes, Enum):
    MSG_TYPE_INIT = b'\x00'
    MSG_TYPE_CONTROL = b'\x01'
    MSG_TYPE_DATA = b'\x02'
    MSG_TYPE_END = b'\x03'


class ConnectionHelloPhaseType(str, Enum):
    PENDING = 'pending'
    READY = 'ready'
    ABORTED = 'aborted'


class ProtocolHandshakeTypeType(str, Enum):
    ANNOUNCEMAX = 'announceMax'
    SELECT = 'select'


class PinStateType(str, Enum):
    REQUIRED = 'required'
    OPTIONAL = 'optional'
    PINOK = 'pinOk'
    NONE = 'none'


class PinInputPermissionType(str, Enum):
    BUSY = 'busy'
    OK = 'ok'


class ConnectionClosePhaseType(str, Enum):
    ANNOUNCE = 'announce'
    CONFIRM = 'confirm'


class ConnectionCloseReasonType(str, Enum):
    UNSPECIFIC = 'unspecific'
    REMOVEDCONNECTION = 'removedConnection'

