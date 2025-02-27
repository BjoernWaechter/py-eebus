from enum import Enum


class MessageType(bytes, Enum):
    MSG_TYPE_INIT = b'\x00'
    MSG_TYPE_CONTROL = b'\x01'
    MSG_TYPE_DATA = b'\x02'
    MSG_TYPE_END = b'\x03'


class MeasurementValueTypeEnumType(str, Enum):
    value = 'value'
    averageValue = 'averageValue'
    minValue = 'minValue'
    maxValue = 'maxValue'
    standardDeviation = 'standardDeviation'


class MeasurementValueTendencyEnumType(str, Enum):
    rising = 'rising'
    stable = 'stable'
    falling = 'falling'


class MeasurementValueStateEnumType(str, Enum):
    normal = 'normal'
    outOfRange = 'outOfRange'
    error = 'error'


class MeasurementValueSourceEnumType(str, Enum):
    measuredValue = 'measuredValue'
    calculatedValue = 'calculatedValue'
    empiricalValue = 'empiricalValue'


class MeasurementTypeEnumType(str, Enum):
    acceleration = 'acceleration'
    angle = 'angle'
    angularVelocity = 'angularVelocity'
    area = 'area'
    atmosphericPressure = 'atmosphericPressure'
    capacity = 'capacity'
    concentration = 'concentration'
    count = 'count'
    current = 'current'
    density = 'density'
    distance = 'distance'
    electricField = 'electricField'
    energy = 'energy'
    force = 'force'
    frequency = 'frequency'
    harmonicDistortion = 'harmonicDistortion'
    heat = 'heat'
    heatFlux = 'heatFlux'
    illuminance = 'illuminance'
    impulse = 'impulse'
    level = 'level'
    magneticField = 'magneticField'
    mass = 'mass'
    massFlow = 'massFlow'
    particles = 'particles'
    percentage = 'percentage'
    power = 'power'
    powerFactor = 'powerFactor'
    pressure = 'pressure'
    radonActivity = 'radonActivity'
    relativeHumidity = 'relativeHumidity'
    resistance = 'resistance'
    solarRadiation = 'solarRadiation'
    speed = 'speed'
    temperature = 'temperature'
    time = 'time'
    torque = 'torque'
    unknown = 'unknown'
    velocity = 'velocity'
    voltage = 'voltage'
    volume = 'volume'
    volumetricFlow = 'volumetricFlow'

