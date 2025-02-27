from enum import Enum


class MessageType(bytes, Enum):
    MSG_TYPE_INIT = b'\x00'
    MSG_TYPE_CONTROL = b'\x01'
    MSG_TYPE_DATA = b'\x02'
    MSG_TYPE_END = b'\x03'


class ThresholdTypeEnumType(str, Enum):
    goodAbove = 'goodAbove'
    badAbove = 'badAbove'
    goodBelow = 'goodBelow'
    badBelow = 'badBelow'
    minValueThreshold = 'minValueThreshold'
    maxValueThreshold = 'maxValueThreshold'
    minValueThresholdExtreme = 'minValueThresholdExtreme'
    maxValueThresholdExtreme = 'maxValueThresholdExtreme'
    sagThreshold = 'sagThreshold'
    swellThreshold = 'swellThreshold'

