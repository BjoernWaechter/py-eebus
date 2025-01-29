from ship.enums import *
import json

MSG_TYPE_INIT = b'\x00\x00'
MSG_TYPE_CONTROL = b'\x01'
MSG_TYPE_DATA = b'\x02'
MSG_TYPE_END = b'\x03'




class MessageProtocolFormatType:
    def __init__(
            self,
            message_protocol_format_type: str,
    ):
        super().__init__()
        
        self.message_protocol_format_type = message_protocol_format_type

    def get_data(self):
        msg_data = self.message_protocol_format_type
        return msg_data

    def __str__(self):
        result_str = ""
        sep = ""
        if self.message_protocol_format_type:
            result_str += f"{sep}{self.message_protocol_format_type}"
        
        return result_str


class MessageProtocolHandshakeErrorErrorType:
    def __init__(
            self,
            message_protocol_handshake_error_error_type: float,
    ):
        super().__init__()
        
        self.message_protocol_handshake_error_error_type = message_protocol_handshake_error_error_type

    def get_data(self):
        msg_data = []
        
        if self.message_protocol_handshake_error_error_type:
            msg_data.append({"MessageProtocolHandshakeErrorErrorType": self.message_protocol_handshake_error_error_type})
        
        return msg_data

    def __str__(self):
        result_str = ""
        sep = ""
        if self.message_protocol_handshake_error_error_type:
            result_str += f"{sep}MessageProtocolHandshakeErrorErrorType: {self.message_protocol_handshake_error_error_type}"
        
        return result_str


class PinValueType:
    def __init__(
            self,
            pin_value_type: str,
    ):
        super().__init__()
        
        self.pin_value_type = pin_value_type

    def get_data(self):
        msg_data = []
        
        if self.pin_value_type:
            msg_data.append({"PinValueType": self.pin_value_type})
        
        return msg_data

    def __str__(self):
        result_str = ""
        sep = ""
        if self.pin_value_type:
            result_str += f"{sep}PinValueType: {self.pin_value_type}"
        
        return result_str


class ConnectionPinErrorErrorType:
    def __init__(
            self,
            connection_pin_error_error_type: float,
    ):
        super().__init__()
        
        self.connection_pin_error_error_type = connection_pin_error_error_type

    def get_data(self):
        msg_data = []
        
        if self.connection_pin_error_error_type:
            msg_data.append({"ConnectionPinErrorErrorType": self.connection_pin_error_error_type})
        
        return msg_data

    def __str__(self):
        result_str = ""
        sep = ""
        if self.connection_pin_error_error_type:
            result_str += f"{sep}ConnectionPinErrorErrorType: {self.connection_pin_error_error_type}"
        
        return result_str


class ProtocolIdType:
    def __init__(
            self,
            protocol_id_type: str = None,
    ):
        super().__init__()
        
        if protocol_id_type is None:
            protocol_id_type = 'ee1.0'
        self.protocol_id_type = protocol_id_type

    def get_data(self):
        msg_data = self.protocol_id_type
        return msg_data

    def __str__(self):
        result_str = ""
        sep = ""
        if self.protocol_id_type:
            result_str += f"{sep}{self.protocol_id_type}"
        
        return result_str


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

    def __str__(self):
        result_str = ""
        sep = ""
        if self.format:
            result_str += f"{sep}format: {', '.join([str(x) for x in self.format])}"
        
        return result_str


class HeaderType:
    def __init__(
            self,
            protocol_id: ProtocolIdType,
    ):
        super().__init__()
        
        self.protocol_id = protocol_id

    def get_data(self):
        msg_data = []
        
        if self.protocol_id:
            msg_data.append({"protocolId": self.protocol_id})
        
        return msg_data

    def __str__(self):
        result_str = ""
        sep = ""
        if self.protocol_id:
            result_str += f"{sep}protocolId: {self.protocol_id}"
        
        return result_str


class ExtensionType:
    def __init__(
            self,
            extension_id: str = None,
            binary: str = None,
            string: str = None,
    ):
        super().__init__()
        
        self.extension_id = extension_id
        self.binary = binary
        self.string = string

    def get_data(self):
        msg_data = []
        
        if self.extension_id:
            msg_data.append({"extensionId": self.extension_id})
        if self.binary:
            msg_data.append({"binary": self.binary})
        if self.string:
            msg_data.append({"string": self.string})
        
        return msg_data

    def __str__(self):
        result_str = ""
        sep = ""
        if self.extension_id:
            result_str += f"{sep}extensionId: {self.extension_id}"
            sep = ", "
        if self.binary:
            result_str += f"{sep}binary: {self.binary}"
            sep = ", "
        if self.string:
            result_str += f"{sep}string: {self.string}"
        
        return result_str



