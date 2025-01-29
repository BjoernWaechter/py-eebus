from types import NoneType

MSG_TYPE_INIT = b'\x00\x00'
MSG_TYPE_CONTROL = b'\x01'
MSG_TYPE_DATA = b'\x02'
MSG_TYPE_END = b'\x03'


def array_2_dict(arr):
    return {list(v.keys())[0]:v[list(v.keys())[0]] for v in arr}



class MessageProtocolFormatType:
    def __init__(
            self,
            message_protocol_format_type: str,
    ):
        super().__init__()
        
        self.message_protocol_format_type = message_protocol_format_type

        if type(self.message_protocol_format_type) is not str and type(self.message_protocol_format_type) is not NoneType:
            raise TypeError("message_protocol_format_type is not of type str")
        
    def get_data(self):
        msg_data = self.message_protocol_format_type
        return msg_data

    def __str__(self):
        result_str = ""
        sep = ""
        if self.message_protocol_format_type is not None:
            result_str += f"{sep}{self.message_protocol_format_type}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                message_protocol_format_type=
                data_dict.get('MessageProtocolFormatType'), 
            )
        elif data:
            return cls(data)
        else:
            return cls()


class MessageProtocolHandshakeErrorErrorType:
    def __init__(
            self,
            message_protocol_handshake_error_error_type: float,
    ):
        super().__init__()
        
        self.message_protocol_handshake_error_error_type = message_protocol_handshake_error_error_type

        if type(self.message_protocol_handshake_error_error_type) is not float and type(self.message_protocol_handshake_error_error_type) is not NoneType:
            raise TypeError("message_protocol_handshake_error_error_type is not of type float")
        
    def get_data(self):
        msg_data = []
        
        if self.message_protocol_handshake_error_error_type is not None:
            msg_data.append({"MessageProtocolHandshakeErrorErrorType": self.message_protocol_handshake_error_error_type})
        
        return msg_data

    def __str__(self):
        result_str = ""
        sep = ""
        if self.message_protocol_handshake_error_error_type is not None:
            result_str += f"{sep}MessageProtocolHandshakeErrorErrorType: {self.message_protocol_handshake_error_error_type}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                message_protocol_handshake_error_error_type=
                data_dict.get('MessageProtocolHandshakeErrorErrorType'), 
            )
        elif data:
            return cls(data)
        else:
            return cls()


class PinValueType:
    def __init__(
            self,
            pin_value_type: str,
    ):
        super().__init__()
        
        self.pin_value_type = pin_value_type

        if type(self.pin_value_type) is not str and type(self.pin_value_type) is not NoneType:
            raise TypeError("pin_value_type is not of type str")
        
    def get_data(self):
        msg_data = []
        
        if self.pin_value_type is not None:
            msg_data.append({"PinValueType": self.pin_value_type})
        
        return msg_data

    def __str__(self):
        result_str = ""
        sep = ""
        if self.pin_value_type is not None:
            result_str += f"{sep}PinValueType: {self.pin_value_type}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                pin_value_type=
                data_dict.get('PinValueType'), 
            )
        elif data:
            return cls(data)
        else:
            return cls()


class ConnectionPinErrorErrorType:
    def __init__(
            self,
            connection_pin_error_error_type: float,
    ):
        super().__init__()
        
        self.connection_pin_error_error_type = connection_pin_error_error_type

        if type(self.connection_pin_error_error_type) is not float and type(self.connection_pin_error_error_type) is not NoneType:
            raise TypeError("connection_pin_error_error_type is not of type float")
        
    def get_data(self):
        msg_data = []
        
        if self.connection_pin_error_error_type is not None:
            msg_data.append({"ConnectionPinErrorErrorType": self.connection_pin_error_error_type})
        
        return msg_data

    def __str__(self):
        result_str = ""
        sep = ""
        if self.connection_pin_error_error_type is not None:
            result_str += f"{sep}ConnectionPinErrorErrorType: {self.connection_pin_error_error_type}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                connection_pin_error_error_type=
                data_dict.get('ConnectionPinErrorErrorType'), 
            )
        elif data:
            return cls(data)
        else:
            return cls()


class ProtocolIdType:
    def __init__(
            self,
            protocol_id_type: str = None,
    ):
        super().__init__()
        
        if protocol_id_type is None:
            protocol_id_type = 'ee1.0'
        self.protocol_id_type = protocol_id_type

        if type(self.protocol_id_type) is not str and type(self.protocol_id_type) is not NoneType:
            raise TypeError("protocol_id_type is not of type str")
        
    def get_data(self):
        msg_data = self.protocol_id_type
        return msg_data

    def __str__(self):
        result_str = ""
        sep = ""
        if self.protocol_id_type is not None:
            result_str += f"{sep}{self.protocol_id_type}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                protocol_id_type=
                data_dict.get('ProtocolIdType'), 
            )
        elif data:
            return cls(data)
        else:
            return cls()


class MessageProtocolFormatsType:
    def __init__(
            self,
            format: list[MessageProtocolFormatType],
    ):
        super().__init__()
        
        self.format = format

        if type(self.format) is not list:
            raise TypeError("format is not of type MessageProtocolFormatType")
        
    def get_data(self):
        msg_data = []
        
        if self.format is not None:
            msg_data.append({"format": self.format})
        
        return msg_data

    def __str__(self):
        result_str = ""
        sep = ""
        if self.format is not None:
            result_str += f"{sep}format: {', '.join([str(x) for x in self.format])}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                format=[MessageProtocolFormatType.from_data(x) for x in data_dict.get('format')]
            )
        elif data:
            return cls(data)
        else:
            return cls()


class Version:
    def __init__(
            self,
            major: int,
            minor: int,
    ):
        super().__init__()
        
        self.major = major
        self.minor = minor

        if type(self.major) is not int and type(self.major) is not NoneType:
            raise TypeError("major is not of type int")
        
        if type(self.minor) is not int and type(self.minor) is not NoneType:
            raise TypeError("minor is not of type int")
        
    def get_data(self):
        msg_data = []
        
        if self.major is not None:
            msg_data.append({"major": self.major})
        if self.minor is not None:
            msg_data.append({"minor": self.minor})
        
        return msg_data

    def __str__(self):
        result_str = ""
        sep = ""
        if self.major is not None:
            result_str += f"{sep}major: {self.major}"
            sep = ", "
        if self.minor is not None:
            result_str += f"{sep}minor: {self.minor}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                major=
                data_dict.get('major'), 
                minor=
                data_dict.get('minor'), 
            )
        elif data:
            return cls(data)
        else:
            return cls()


class HeaderType:
    def __init__(
            self,
            protocol_id: ProtocolIdType,
    ):
        super().__init__()
        
        self.protocol_id = protocol_id

        if type(self.protocol_id) is not ProtocolIdType and type(self.protocol_id) is not NoneType:
            raise TypeError("protocol_id is not of type ProtocolIdType")
        
    def get_data(self):
        msg_data = []
        
        if self.protocol_id is not None:
            msg_data.append({"protocolId": self.protocol_id})
        
        return msg_data

    def __str__(self):
        result_str = ""
        sep = ""
        if self.protocol_id is not None:
            result_str += f"{sep}protocolId: {self.protocol_id}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                protocol_id=
                ProtocolIdType.from_data(data_dict.get('protocolId')), 
            )
        elif data:
            return cls(data)
        else:
            return cls()


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

        if type(self.extension_id) is not str and type(self.extension_id) is not NoneType:
            raise TypeError("extension_id is not of type str")
        
        if type(self.binary) is not str and type(self.binary) is not NoneType:
            raise TypeError("binary is not of type str")
        
        if type(self.string) is not str and type(self.string) is not NoneType:
            raise TypeError("string is not of type str")
        
    def get_data(self):
        msg_data = []
        
        if self.extension_id is not None:
            msg_data.append({"extensionId": self.extension_id})
        if self.binary is not None:
            msg_data.append({"binary": self.binary})
        if self.string is not None:
            msg_data.append({"string": self.string})
        
        return msg_data

    def __str__(self):
        result_str = ""
        sep = ""
        if self.extension_id is not None:
            result_str += f"{sep}extensionId: {self.extension_id}"
            sep = ", "
        if self.binary is not None:
            result_str += f"{sep}binary: {self.binary}"
            sep = ", "
        if self.string is not None:
            result_str += f"{sep}string: {self.string}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                extension_id=
                data_dict.get('extensionId'), 
                binary=
                data_dict.get('binary'), 
                string=
                data_dict.get('string'), 
            )
        elif data:
            return cls(data)
        else:
            return cls()


class DnsSd_MDns:
    def __init__(
            self,
    ):
        super().__init__()
        

    def get_data(self):
        msg_data = []
        
        
        return msg_data

    def __str__(self):
        result_str = ""
        sep = ""
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
            )
        elif data:
            return cls(data)
        else:
            return cls()


class Dns:
    def __init__(
            self,
            uri: str,
    ):
        super().__init__()
        
        self.uri = uri

        if type(self.uri) is not str and type(self.uri) is not NoneType:
            raise TypeError("uri is not of type str")
        
    def get_data(self):
        msg_data = []
        
        if self.uri is not None:
            msg_data.append({"uri": self.uri})
        
        return msg_data

    def __str__(self):
        result_str = ""
        sep = ""
        if self.uri is not None:
            result_str += f"{sep}uri: {self.uri}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                uri=
                data_dict.get('uri'), 
            )
        elif data:
            return cls(data)
        else:
            return cls()



