from enum import Enum


class MessageType(bytes, Enum):
    MSG_TYPE_INIT = b'\x00'
    MSG_TYPE_CONTROL = b'\x01'
    MSG_TYPE_DATA = b'\x02'
    MSG_TYPE_END = b'\x03'


class CmdClassifierType(str, Enum):
    read = 'read'
    reply = 'reply'
    notify = 'notify'
    write = 'write'
    call = 'call'
    result = 'result'

