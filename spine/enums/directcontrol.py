from enum import Enum


class MessageType(bytes, Enum):
    MSG_TYPE_INIT = b'\x00'
    MSG_TYPE_CONTROL = b'\x01'
    MSG_TYPE_DATA = b'\x02'
    MSG_TYPE_END = b'\x03'


class DirectControlActivityStateEnumType(str, Enum):
    running = 'running'
    paused = 'paused'
    inactive = 'inactive'

