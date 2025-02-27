from enum import Enum


class MessageType(bytes, Enum):
    MSG_TYPE_INIT = b'\x00'
    MSG_TYPE_CONTROL = b'\x01'
    MSG_TYPE_DATA = b'\x02'
    MSG_TYPE_END = b'\x03'


class LoadControlLimitTypeEnumType(str, Enum):
    minValueLimit = 'minValueLimit'
    maxValueLimit = 'maxValueLimit'
    signDependentAbsValueLimit = 'signDependentAbsValueLimit'


class LoadControlEventStateEnumType(str, Enum):
    eventAccepted = 'eventAccepted'
    eventStarted = 'eventStarted'
    eventStopped = 'eventStopped'
    eventRejected = 'eventRejected'
    eventCancelled = 'eventCancelled'
    eventError = 'eventError'


class LoadControlEventActionEnumType(str, Enum):
    pause = 'pause'
    resume = 'resume'
    reduce = 'reduce'
    increase = 'increase'
    emergency = 'emergency'
    normal = 'normal'


class LoadControlCategoryEnumType(str, Enum):
    obligation = 'obligation'
    recommendation = 'recommendation'
    optimization = 'optimization'

