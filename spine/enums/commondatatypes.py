from enum import Enum


class MessageType(bytes, Enum):
    MSG_TYPE_INIT = b'\x00'
    MSG_TYPE_CONTROL = b'\x01'
    MSG_TYPE_DATA = b'\x02'
    MSG_TYPE_END = b'\x03'


class RoleType(str, Enum):
    client = 'client'
    server = 'server'
    special = 'special'


class MonthType(str, Enum):
    january = 'january'
    february = 'february'
    march = 'march'
    april = 'april'
    may = 'may'
    june = 'june'
    july = 'july'
    august = 'august'
    september = 'september'
    october = 'october'
    november = 'november'
    december = 'december'


class DayOfWeekType(str, Enum):
    monday = 'monday'
    tuesday = 'tuesday'
    wednesday = 'wednesday'
    thursday = 'thursday'
    friday = 'friday'
    saturday = 'saturday'
    sunday = 'sunday'

