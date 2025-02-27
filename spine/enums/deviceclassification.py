from enum import Enum


class MessageType(bytes, Enum):
    MSG_TYPE_INIT = b'\x00'
    MSG_TYPE_CONTROL = b'\x01'
    MSG_TYPE_DATA = b'\x02'
    MSG_TYPE_END = b'\x03'


class PowerSourceEnumType(str, Enum):
    unknown = 'unknown'
    mainsSinglePhase = 'mainsSinglePhase'
    mains3Phase = 'mains3Phase'
    battery = 'battery'
    dc = 'dc'

