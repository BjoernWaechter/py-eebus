from enum import Enum


class MessageType(bytes, Enum):
    MSG_TYPE_INIT = b'\x00'
    MSG_TYPE_CONTROL = b'\x01'
    MSG_TYPE_DATA = b'\x02'
    MSG_TYPE_END = b'\x03'


class IncentiveValueTypeEnumType(str, Enum):
    value = 'value'
    averageValue = 'averageValue'
    minValue = 'minValue'
    maxValue = 'maxValue'


class IncentiveTypeEnumType(str, Enum):
    absoluteCost = 'absoluteCost'
    relativeCost = 'relativeCost'
    renewableEnergyPercentage = 'renewableEnergyPercentage'
    co2Emission = 'co2Emission'


class TierTypeEnumType(str, Enum):
    fixedCost = 'fixedCost'
    dynamicCost = 'dynamicCost'


class TierBoundaryTypeEnumType(str, Enum):
    powerBoundary = 'powerBoundary'
    energyBoundary = 'energyBoundary'
    countBoundary = 'countBoundary'

