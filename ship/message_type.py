from ship.base_type import *
from ship.enums import *
from types import NoneType

MSG_TYPE_INIT = b'\x00\x00'
MSG_TYPE_CONTROL = b'\x01'
MSG_TYPE_DATA = b'\x02'
MSG_TYPE_END = b'\x03'


def array_2_dict(arr):
    return {list(v.keys())[0]:v[list(v.keys())[0]] for v in arr}


class ShipMessageType:
    def __init__(
        self
    ):
        pass

    def get_data(self):
        raise NotImplementedError("get_data has to be implemented")

    def __str__(self):
        pass


class ConnectionHelloType(ShipMessageType):
    def __init__(
            self,
            phase: ConnectionHelloPhaseType,
            waiting: int = None,
            prolongation_request: bool = None,
    ):
        super().__init__()
        
        if waiting is None:
            waiting = 60000
        self.phase = phase
        self.waiting = waiting
        self.prolongation_request = prolongation_request

        if type(self.phase) is not ConnectionHelloPhaseType and type(self.phase) is not NoneType:
            raise TypeError("phase is not of type ConnectionHelloPhaseType")
        
        if type(self.waiting) is not int and type(self.waiting) is not NoneType:
            raise TypeError("waiting is not of type int")
        
        if type(self.prolongation_request) is not bool and type(self.prolongation_request) is not NoneType:
            raise TypeError("prolongation_request is not of type bool")
        
    def get_data(self):
        msg_data = []
        
        if self.phase is not None:
            msg_data.append({"phase": self.phase})
        if self.waiting is not None:
            msg_data.append({"waiting": self.waiting})
        if self.prolongation_request is not None:
            msg_data.append({"prolongationRequest": self.prolongation_request})
        
        return msg_data

    def __str__(self):
        result_str = ""
        sep = ""
        if self.phase is not None:
            result_str += f"{sep}phase: {self.phase}"
            sep = ", "
        if self.waiting is not None:
            result_str += f"{sep}waiting: {self.waiting}"
            sep = ", "
        if self.prolongation_request is not None:
            result_str += f"{sep}prolongationRequest: {self.prolongation_request}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                phase=
                ConnectionHelloPhaseType(data_dict.get('phase')), 
                waiting=
                data_dict.get('waiting'), 
                prolongation_request=
                data_dict.get('prolongationRequest'), 
            )
        elif data:
            return cls(data)
        else:
            return cls()


class MessageProtocolHandshakeType(ShipMessageType):
    def __init__(
            self,
            handshake_type: ProtocolHandshakeTypeType,
            version: Version = None,
            formats: MessageProtocolFormatsType = None,
    ):
        super().__init__()
        
        if version is None:
            version = Version(major=1, minor=0)
        if formats is None:
            formats = MessageProtocolFormatsType(format=[MessageProtocolFormatType("JSON-UTF8")])
        self.handshake_type = handshake_type
        self.version = version
        self.formats = formats

        if type(self.handshake_type) is not ProtocolHandshakeTypeType and type(self.handshake_type) is not NoneType:
            raise TypeError("handshake_type is not of type ProtocolHandshakeTypeType")
        
        if type(self.version) is not Version and type(self.version) is not NoneType:
            raise TypeError("version is not of type Version")
        
        if type(self.formats) is not MessageProtocolFormatsType and type(self.formats) is not NoneType:
            raise TypeError("formats is not of type MessageProtocolFormatsType")
        
    def get_data(self):
        msg_data = []
        
        if self.handshake_type is not None:
            msg_data.append({"handshakeType": self.handshake_type})
        if self.version is not None:
            msg_data.append({"version": self.version})
        if self.formats is not None:
            msg_data.append({"formats": self.formats})
        
        return msg_data

    def __str__(self):
        result_str = ""
        sep = ""
        if self.handshake_type is not None:
            result_str += f"{sep}handshakeType: {self.handshake_type}"
            sep = ", "
        if self.version is not None:
            result_str += f"{sep}version: {self.version}"
            sep = ", "
        if self.formats is not None:
            result_str += f"{sep}formats: {self.formats}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                handshake_type=
                ProtocolHandshakeTypeType(data_dict.get('handshakeType')), 
                version=
                Version.from_data(data_dict.get('version')), 
                formats=
                MessageProtocolFormatsType.from_data(data_dict.get('formats')), 
            )
        elif data:
            return cls(data)
        else:
            return cls()


class MessageProtocolHandshakeErrorType(ShipMessageType):
    def __init__(
            self,
            error: MessageProtocolHandshakeErrorErrorType,
    ):
        super().__init__()
        
        self.error = error

        if type(self.error) is not MessageProtocolHandshakeErrorErrorType and type(self.error) is not NoneType:
            raise TypeError("error is not of type MessageProtocolHandshakeErrorErrorType")
        
    def get_data(self):
        msg_data = []
        
        if self.error is not None:
            msg_data.append({"error": self.error})
        
        return msg_data

    def __str__(self):
        result_str = ""
        sep = ""
        if self.error is not None:
            result_str += f"{sep}error: {self.error}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                error=
                MessageProtocolHandshakeErrorErrorType.from_data(data_dict.get('error')), 
            )
        elif data:
            return cls(data)
        else:
            return cls()


class ConnectionPinStateType(ShipMessageType):
    def __init__(
            self,
            pin_state: PinStateType,
            input_permission: PinInputPermissionType = None,
    ):
        super().__init__()
        
        self.pin_state = pin_state
        self.input_permission = input_permission

        if type(self.pin_state) is not PinStateType and type(self.pin_state) is not NoneType:
            raise TypeError("pin_state is not of type PinStateType")
        
        if type(self.input_permission) is not PinInputPermissionType and type(self.input_permission) is not NoneType:
            raise TypeError("input_permission is not of type PinInputPermissionType")
        
    def get_data(self):
        msg_data = []
        
        if self.pin_state is not None:
            msg_data.append({"pinState": self.pin_state})
        if self.input_permission is not None:
            msg_data.append({"inputPermission": self.input_permission})
        
        return msg_data

    def __str__(self):
        result_str = ""
        sep = ""
        if self.pin_state is not None:
            result_str += f"{sep}pinState: {self.pin_state}"
            sep = ", "
        if self.input_permission is not None:
            result_str += f"{sep}inputPermission: {self.input_permission}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                pin_state=
                PinStateType(data_dict.get('pinState')), 
                input_permission=
                PinInputPermissionType(data_dict.get('inputPermission')), 
            )
        elif data:
            return cls(data)
        else:
            return cls()


class ConnectionPinInputType(ShipMessageType):
    def __init__(
            self,
            pin: PinValueType,
    ):
        super().__init__()
        
        self.pin = pin

        if type(self.pin) is not PinValueType and type(self.pin) is not NoneType:
            raise TypeError("pin is not of type PinValueType")
        
    def get_data(self):
        msg_data = []
        
        if self.pin is not None:
            msg_data.append({"pin": self.pin})
        
        return msg_data

    def __str__(self):
        result_str = ""
        sep = ""
        if self.pin is not None:
            result_str += f"{sep}pin: {self.pin}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                pin=
                PinValueType.from_data(data_dict.get('pin')), 
            )
        elif data:
            return cls(data)
        else:
            return cls()


class ConnectionPinErrorType(ShipMessageType):
    def __init__(
            self,
            error: ConnectionPinErrorErrorType,
    ):
        super().__init__()
        
        self.error = error

        if type(self.error) is not ConnectionPinErrorErrorType and type(self.error) is not NoneType:
            raise TypeError("error is not of type ConnectionPinErrorErrorType")
        
    def get_data(self):
        msg_data = []
        
        if self.error is not None:
            msg_data.append({"error": self.error})
        
        return msg_data

    def __str__(self):
        result_str = ""
        sep = ""
        if self.error is not None:
            result_str += f"{sep}error: {self.error}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                error=
                ConnectionPinErrorErrorType.from_data(data_dict.get('error')), 
            )
        elif data:
            return cls(data)
        else:
            return cls()


class DataType(ShipMessageType):
    def __init__(
            self,
            header: HeaderType,
            payload,
            extension: ExtensionType = None,
    ):
        super().__init__()
        
        self.header = header
        self.payload = payload
        self.extension = extension

        if type(self.header) is not HeaderType and type(self.header) is not NoneType:
            raise TypeError("header is not of type HeaderType")
        
        if type(self.extension) is not ExtensionType and type(self.extension) is not NoneType:
            raise TypeError("extension is not of type ExtensionType")
        
    def get_data(self):
        msg_data = []
        
        if self.header is not None:
            msg_data.append({"header": self.header})
        if self.payload is not None:
            msg_data.append({"payload": self.payload})
        if self.extension is not None:
            msg_data.append({"extension": self.extension})
        
        return msg_data

    def __str__(self):
        result_str = ""
        sep = ""
        if self.header is not None:
            result_str += f"{sep}header: {self.header}"
            sep = ", "
        if self.payload is not None:
            result_str += f"{sep}payload: {self.payload}"
            sep = ", "
        if self.extension is not None:
            result_str += f"{sep}extension: {self.extension}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                header=
                HeaderType.from_data(data_dict.get('header')), 
                payload=
                data_dict.get('payload'), 
                extension=
                ExtensionType.from_data(data_dict.get('extension')), 
            )
        elif data:
            return cls(data)
        else:
            return cls()


class ConnectionCloseType(ShipMessageType):
    def __init__(
            self,
            phase: ConnectionClosePhaseType,
            max_time: int = None,
            reason: ConnectionCloseReasonType = None,
    ):
        super().__init__()
        
        self.phase = phase
        self.max_time = max_time
        self.reason = reason

        if type(self.phase) is not ConnectionClosePhaseType and type(self.phase) is not NoneType:
            raise TypeError("phase is not of type ConnectionClosePhaseType")
        
        if type(self.max_time) is not int and type(self.max_time) is not NoneType:
            raise TypeError("max_time is not of type int")
        
        if type(self.reason) is not ConnectionCloseReasonType and type(self.reason) is not NoneType:
            raise TypeError("reason is not of type ConnectionCloseReasonType")
        
    def get_data(self):
        msg_data = []
        
        if self.phase is not None:
            msg_data.append({"phase": self.phase})
        if self.max_time is not None:
            msg_data.append({"maxTime": self.max_time})
        if self.reason is not None:
            msg_data.append({"reason": self.reason})
        
        return msg_data

    def __str__(self):
        result_str = ""
        sep = ""
        if self.phase is not None:
            result_str += f"{sep}phase: {self.phase}"
            sep = ", "
        if self.max_time is not None:
            result_str += f"{sep}maxTime: {self.max_time}"
            sep = ", "
        if self.reason is not None:
            result_str += f"{sep}reason: {self.reason}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                phase=
                ConnectionClosePhaseType(data_dict.get('phase')), 
                max_time=
                data_dict.get('maxTime'), 
                reason=
                ConnectionCloseReasonType(data_dict.get('reason')), 
            )
        elif data:
            return cls(data)
        else:
            return cls()


class AccessMethodsRequestType(ShipMessageType):
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


class AccessMethodsType(ShipMessageType):
    def __init__(
            self,
            id: str,
            dns_sd_m_dns: DnsSd_MDns = None,
            dns: Dns = None,
    ):
        super().__init__()
        
        self.id = id
        self.dns_sd_m_dns = dns_sd_m_dns
        self.dns = dns

        if type(self.id) is not str and type(self.id) is not NoneType:
            raise TypeError("id is not of type str")
        
        if type(self.dns_sd_m_dns) is not DnsSd_MDns and type(self.dns_sd_m_dns) is not NoneType:
            raise TypeError("dns_sd_m_dns is not of type DnsSd_MDns")
        
        if type(self.dns) is not Dns and type(self.dns) is not NoneType:
            raise TypeError("dns is not of type Dns")
        
    def get_data(self):
        msg_data = []
        
        if self.id is not None:
            msg_data.append({"id": self.id})
        if self.dns_sd_m_dns is not None:
            msg_data.append({"dnsSd_mDns": self.dns_sd_m_dns})
        if self.dns is not None:
            msg_data.append({"dns": self.dns})
        
        return msg_data

    def __str__(self):
        result_str = ""
        sep = ""
        if self.id is not None:
            result_str += f"{sep}id: {self.id}"
            sep = ", "
        if self.dns_sd_m_dns is not None:
            result_str += f"{sep}dnsSd_mDns: {self.dns_sd_m_dns}"
            sep = ", "
        if self.dns is not None:
            result_str += f"{sep}dns: {self.dns}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                id=
                data_dict.get('id'), 
                dns_sd_m_dns=
                DnsSd_MDns.from_data(data_dict.get('dnsSd_mDns')), 
                dns=
                Dns.from_data(data_dict.get('dns')), 
            )
        elif data:
            return cls(data)
        else:
            return cls()



