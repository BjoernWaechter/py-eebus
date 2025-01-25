from ship.enums import *
import json

MSG_TYPE_INIT = b'\x00\x00'
MSG_TYPE_CONTROL = b'\x01'
MSG_TYPE_DATA = b'\x02'
MSG_TYPE_END = b'\x03'


class MessageProtocolFormatType:
    def __init__(
        self,
        messageprotocolformattype: str,
    ):
        super().__init__()
        
        
        self.messageprotocolformattype = messageprotocolformattype

    def get_data(self):
        msg_data = self.messageprotocolformattype
        return msg_data


class MessageProtocolHandshakeErrorErrorType:
    def __init__(
        self,
        messageprotocolhandshakeerrorerrortype: float,
    ):
        super().__init__()
        
        
        self.messageprotocolhandshakeerrorerrortype = messageprotocolhandshakeerrorerrortype

    def get_data(self):
        msg_data = []
        
        if self.messageprotocolhandshakeerrorerrortype:
            msg_data.append({"MessageProtocolHandshakeErrorErrorType": self.messageprotocolhandshakeerrorerrortype})
        
        return msg_data


class PinValueType:
    def __init__(
        self,
        pinvaluetype: str,
    ):
        super().__init__()
        
        
        self.pinvaluetype = pinvaluetype

    def get_data(self):
        msg_data = []
        
        if self.pinvaluetype:
            msg_data.append({"PinValueType": self.pinvaluetype})
        
        return msg_data


class ConnectionPinErrorErrorType:
    def __init__(
        self,
        connectionpinerrorerrortype: float,
    ):
        super().__init__()
        
        
        self.connectionpinerrorerrortype = connectionpinerrorerrortype

    def get_data(self):
        msg_data = []
        
        if self.connectionpinerrorerrortype:
            msg_data.append({"ConnectionPinErrorErrorType": self.connectionpinerrorerrortype})
        
        return msg_data


class ProtocolIdType:
    def __init__(
        self,
        protocolidtype: str=None,
    ):
        super().__init__()
        if protocolidtype is None:
            protocolidtype = 'ee1.0'
        
        self.protocolidtype = protocolidtype

    def get_data(self):
        msg_data = self.protocolidtype
        return msg_data


class MessageProtocolFormatsType:
    def __init__(
        self,
        format: list[MessageProtocolFormatType],
    ):
        super().__init__()
        
        
        self.format = format

    def get_data(self):
        msg_data = []
        
        if self.format:
            msg_data.append({"format": self.format})
        
        return msg_data


class HeaderType:
    def __init__(
        self,
        protocolid: ProtocolIdType,
    ):
        super().__init__()
        
        
        self.protocolid = protocolid

    def get_data(self):
        msg_data = []
        
        if self.protocolid:
            msg_data.append({"protocolId": self.protocolid})
        
        return msg_data


class ExtensionType:
    def __init__(
        self,
        extensionid: str=None,
        binary: str=None,
        string: str=None,
    ):
        super().__init__()
        
        
        
        
        self.extensionid = extensionid
        self.binary = binary
        self.string = string

    def get_data(self):
        msg_data = []
        
        if self.extensionid:
            msg_data.append({"extensionId": self.extensionid})
        if self.binary:
            msg_data.append({"binary": self.binary})
        if self.string:
            msg_data.append({"string": self.string})
        
        return msg_data

