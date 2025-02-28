from enum import Enum


class MessageType(bytes, Enum):
    MSG_TYPE_INIT = b'\x00'
    MSG_TYPE_CONTROL = b'\x01'
    MSG_TYPE_DATA = b'\x02'
    MSG_TYPE_END = b'\x03'


class StateInformationCategoryEnumType(str, Enum):
    functionality = 'functionality'
    failure = 'failure'


class StateInformationFailureEnumType(str, Enum):
    inverterDefective = 'inverterDefective'
    batteryOvercurrentProtection = 'batteryOvercurrentProtection'
    pvStringOvercurrentProtection = 'pvStringOvercurrentProtection'
    gridFault = 'gridFault'
    groundFault = 'groundFault'
    acDisconnected = 'acDisconnected'
    dcDisconnected = 'dcDisconnected'
    cabinetOpen = 'cabinetOpen'
    overTemperature = 'overTemperature'
    underTemperature = 'underTemperature'
    frequencyAboveLimit = 'frequencyAboveLimit'
    frequencyBelowLimit = 'frequencyBelowLimit'
    acVoltageAboveLimit = 'acVoltageAboveLimit'
    acVoltageBelowLimit = 'acVoltageBelowLimit'
    dcVoltageAboveLimit = 'dcVoltageAboveLimit'
    dcVoltageBelowLimit = 'dcVoltageBelowLimit'
    hardwareTestFailure = 'hardwareTestFailure'
    genericInternalError = 'genericInternalError'


class StateInformationFunctionalityEnumType(str, Enum):
    externalOverrideFromGrid = 'externalOverrideFromGrid'
    autonomousGridSupport = 'autonomousGridSupport'
    islandingMode = 'islandingMode'
    balancing = 'balancing'
    trickleCharging = 'trickleCharging'
    calibration = 'calibration'
    commissioningMissing = 'commissioningMissing'
    sleeping = 'sleeping'
    starting = 'starting'
    mppt = 'mppt'
    throttled = 'throttled'
    shuttingDown = 'shuttingDown'
    manualShutdown = 'manualShutdown'

