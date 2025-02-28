from enum import Enum


class MessageType(bytes, Enum):
    MSG_TYPE_INIT = b'\x00'
    MSG_TYPE_CONTROL = b'\x01'
    MSG_TYPE_DATA = b'\x02'
    MSG_TYPE_END = b'\x03'


class ElectricalConnectionCharacteristicTypeEnumType(str, Enum):
    powerConsumptionMin = 'powerConsumptionMin'
    powerConsumptionMax = 'powerConsumptionMax'
    powerConsumptionNominalMin = 'powerConsumptionNominalMin'
    powerConsumptionNominalMax = 'powerConsumptionNominalMax'
    powerProductionMin = 'powerProductionMin'
    powerProductionMax = 'powerProductionMax'
    powerProductionNominalMin = 'powerProductionNominalMin'
    powerProductionNominalMax = 'powerProductionNominalMax'
    energyCapacityNominalMax = 'energyCapacityNominalMax'
    contractualConsumptionNominalMax = 'contractualConsumptionNominalMax'
    contractualProductionNominalMax = 'contractualProductionNominalMax'
    apparentPowerProductionNominalMax = 'apparentPowerProductionNominalMax'
    apparentPowerConsumptionNominalMax = 'apparentPowerConsumptionNominalMax'


class ElectricalConnectionCharacteristicContextEnumType(str, Enum):
    device = 'device'
    entity = 'entity'
    inverter = 'inverter'
    pvString = 'pvString'
    battery = 'battery'


class ElectricalConnectionConnectionPointType(str, Enum):
    grid = 'grid'
    home = 'home'
    pv = 'pv'
    sd = 'sd'
    other = 'other'


class ElectricalConnectionPhaseNameEnumType(str, Enum):
    a = 'a'
    b = 'b'
    c = 'c'
    ab = 'ab'
    bc = 'bc'
    ac = 'ac'
    abc = 'abc'
    neutral = 'neutral'
    ground = 'ground'
    none = 'none'


class ElectricalConnectionAcMeasurementTypeEnumType(str, Enum):
    real = 'real'
    reactive = 'reactive'
    apparent = 'apparent'
    phase = 'phase'


class ElectricalConnectionVoltageTypeEnumType(str, Enum):
    ac = 'ac'
    dc = 'dc'


class ElectricalConnectionMeasurandVariantEnumType(str, Enum):
    amplitude = 'amplitude'
    rms = 'rms'
    instantaneous = 'instantaneous'
    angle = 'angle'
    cosPhi = 'cosPhi'

