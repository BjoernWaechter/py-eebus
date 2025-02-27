from enum import Enum


class MessageType(bytes, Enum):
    MSG_TYPE_INIT = b'\x00'
    MSG_TYPE_CONTROL = b'\x01'
    MSG_TYPE_DATA = b'\x02'
    MSG_TYPE_END = b'\x03'


class NetworkManagementStateChangeType(str, Enum):
    added = 'added'
    removed = 'removed'
    modified = 'modified'


class NetworkManagementProcessStateStateType(str, Enum):
    succeeded = 'succeeded'
    failed = 'failed'
    aborted = 'aborted'


class NetworkManagementFeatureSetType(str, Enum):
    gateway = 'gateway'
    router = 'router'
    smart = 'smart'
    simple = 'simple'

