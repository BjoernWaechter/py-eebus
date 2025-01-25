from enum import Enum


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

