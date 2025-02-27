from enum import Enum


class MessageType(bytes, Enum):
    MSG_TYPE_INIT = b'\x00'
    MSG_TYPE_CONTROL = b'\x01'
    MSG_TYPE_DATA = b'\x02'
    MSG_TYPE_END = b'\x03'


class HvacSystemFunctionTypeEnumType(str, Enum):
    heating = 'heating'
    cooling = 'cooling'
    ventilation = 'ventilation'
    dhw = 'dhw'


class HvacOverrunTypeEnumType(str, Enum):
    oneTimeDhw = 'oneTimeDhw'
    party = 'party'
    sgReadyCondition1 = 'sgReadyCondition1'
    sgReadyCondition3 = 'sgReadyCondition3'
    sgReadyCondition4 = 'sgReadyCondition4'
    oneDayAway = 'oneDayAway'
    oneDayAtHome = 'oneDayAtHome'
    oneTimeVentilation = 'oneTimeVentilation'
    hvacSystemOff = 'hvacSystemOff'
    valveKick = 'valveKick'


class HvacOverrunStatusEnumType(str, Enum):
    active = 'active'
    running = 'running'
    finished = 'finished'
    inactive = 'inactive'


class HvacOperationModeTypeEnumType(str, Enum):
    auto = 'auto'
    on = 'on'
    off = 'off'
    eco = 'eco'

