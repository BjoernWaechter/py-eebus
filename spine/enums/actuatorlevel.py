from enum import Enum


class MessageType(bytes, Enum):
    MSG_TYPE_INIT = b'\x00'
    MSG_TYPE_CONTROL = b'\x01'
    MSG_TYPE_DATA = b'\x02'
    MSG_TYPE_END = b'\x03'


class ActuatorLevelFctEnumType(str, Enum):
    start = 'start'
    up = 'up'
    down = 'down'
    stop = 'stop'
    percentageAbsolute = 'percentageAbsolute'
    percentageRelative = 'percentageRelative'
    absolute = 'absolute'
    relative = 'relative'

