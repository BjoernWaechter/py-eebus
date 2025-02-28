from enum import Enum


class MessageType(bytes, Enum):
    MSG_TYPE_INIT = b'\x00'
    MSG_TYPE_CONTROL = b'\x01'
    MSG_TYPE_DATA = b'\x02'
    MSG_TYPE_END = b'\x03'


class GridConditionEnumType(str, Enum):
    consumptionRed = 'consumptionRed'
    consumptionYellow = 'consumptionYellow'
    good = 'good'
    productionYellow = 'productionYellow'
    productionRed = 'productionRed'


class SupplyConditionOriginatorEnumType(str, Enum):
    externDSO = 'externDSO'
    externSupplier = 'externSupplier'
    internalLimit = 'internalLimit'
    internalService = 'internalService'
    internalUser = 'internalUser'


class SupplyConditionEventTypeEnumType(str, Enum):
    thesholdExceeded = 'thesholdExceeded'
    fallenBelowThreshold = 'fallenBelowThreshold'
    supplyInterrupt = 'supplyInterrupt'
    releaseOfLimitations = 'releaseOfLimitations'
    otherProblem = 'otherProblem'
    gridConditionUpdate = 'gridConditionUpdate'

