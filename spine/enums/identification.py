from enum import Enum


class MessageType(bytes, Enum):
    MSG_TYPE_INIT = b'\x00'
    MSG_TYPE_CONTROL = b'\x01'
    MSG_TYPE_DATA = b'\x02'
    MSG_TYPE_END = b'\x03'


class IdentificationTypeEnumType(str, Enum):
    eui48 = 'eui48'
    eui64 = 'eui64'
    userRfidTag = 'userRfidTag'

