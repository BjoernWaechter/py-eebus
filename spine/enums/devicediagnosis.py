from enum import Enum


class MessageType(bytes, Enum):
    MSG_TYPE_INIT = b'\x00'
    MSG_TYPE_CONTROL = b'\x01'
    MSG_TYPE_DATA = b'\x02'
    MSG_TYPE_END = b'\x03'


class PowerSupplyConditionEnumType(str, Enum):
    good = 'good'
    low = 'low'
    critical = 'critical'
    unknown = 'unknown'
    error = 'error'


class DeviceDiagnosisOperatingStateEnumType(str, Enum):
    normalOperation = 'normalOperation'
    standby = 'standby'
    failure = 'failure'
    serviceNeeded = 'serviceNeeded'
    overrideDetected = 'overrideDetected'
    inAlarm = 'inAlarm'
    notReachable = 'notReachable'
    finished = 'finished'
    temporarilyNotReady = 'temporarilyNotReady'
    off = 'off'

