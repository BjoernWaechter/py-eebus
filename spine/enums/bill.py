from enum import Enum


class MessageType(bytes, Enum):
    MSG_TYPE_INIT = b'\x00'
    MSG_TYPE_CONTROL = b'\x01'
    MSG_TYPE_DATA = b'\x02'
    MSG_TYPE_END = b'\x03'


class BillTypeEnumType(str, Enum):
    chargingSummary = 'chargingSummary'


class BillPositionTypeEnumType(str, Enum):
    gridElectricEnergy = 'gridElectricEnergy'
    selfProducedElectricEnergy = 'selfProducedElectricEnergy'


class BillCostTypeEnumType(str, Enum):
    absolutePrice = 'absolutePrice'
    relativePrice = 'relativePrice'
    co2Emission = 'co2Emission'
    renewableEnergy = 'renewableEnergy'
    radioactiveWaste = 'radioactiveWaste'

