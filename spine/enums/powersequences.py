from enum import Enum


class MessageType(bytes, Enum):
    MSG_TYPE_INIT = b'\x00'
    MSG_TYPE_CONTROL = b'\x01'
    MSG_TYPE_DATA = b'\x02'
    MSG_TYPE_END = b'\x03'


class PowerSequenceStateEnumType(str, Enum):
    running = 'running'
    paused = 'paused'
    scheduled = 'scheduled'
    scheduledPaused = 'scheduledPaused'
    pending = 'pending'
    inactive = 'inactive'
    completed = 'completed'
    invalid = 'invalid'


class PowerSequenceScopeEnumType(str, Enum):
    forecast = 'forecast'
    measurement = 'measurement'
    recommendation = 'recommendation'


class PowerTimeSlotValueTypeEnumType(str, Enum):
    power = 'power'
    powerMin = 'powerMin'
    powerMax = 'powerMax'
    powerExpectedValue = 'powerExpectedValue'
    powerStandardDeviation = 'powerStandardDeviation'
    powerSkewness = 'powerSkewness'
    energy = 'energy'
    energyMin = 'energyMin'
    energyMax = 'energyMax'
    energyExpectedValue = 'energyExpectedValue'
    energyStandardDeviation = 'energyStandardDeviation'
    energySkewness = 'energySkewness'

