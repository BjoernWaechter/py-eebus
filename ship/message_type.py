from ship.base_type import *
from ship.enums import *
import json

MSG_TYPE_INIT = b'\x00\x00'
MSG_TYPE_CONTROL = b'\x01'
MSG_TYPE_DATA = b'\x02'
MSG_TYPE_END = b'\x03'


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

    def get_data(self):
        msg_data = []
        
        if self.phase:
            msg_data.append({"phase": self.phase})
        if self.waiting:
            msg_data.append({"waiting": self.waiting})
        if self.prolongation_request:
            msg_data.append({"prolongationRequest": self.prolongation_request})
        
        return msg_data

    def __str__(self):
        result_str = ""
        sep = ""
        if self.phase:
            result_str += f"{sep}phase: {self.phase}"
            sep = ", "
        if self.waiting:
            result_str += f"{sep}waiting: {self.waiting}"
            sep = ", "
        if self.prolongation_request:
            result_str += f"{sep}prolongationRequest: {self.prolongation_request}"
        
        return result_str


class MessageProtocolHandshakeType(ShipMessageType):
    def __init__(
            self,
            handshake_type: ProtocolHandshakeTypeType,
            version = None,
            formats: MessageProtocolFormatsType = None,
    ):
        super().__init__()
        
        if version is None:
            version = [{"major": 1}, {"minor": 0}]
        if formats is None:
            formats = MessageProtocolFormatsType(format=[MessageProtocolFormatType("JSON-UTF8")])
        self.handshake_type = handshake_type
        self.version = version
        self.formats = formats

    def get_data(self):
        msg_data = []
        
        if self.handshake_type:
            msg_data.append({"handshakeType": self.handshake_type})
        if self.version:
            msg_data.append({"version": self.version})
        if self.formats:
            msg_data.append({"formats": self.formats})
        
        return msg_data

    def __str__(self):
        result_str = ""
        sep = ""
        if self.handshake_type:
            result_str += f"{sep}handshakeType: {self.handshake_type}"
            sep = ", "
        if self.version:
            result_str += f"{sep}version: {self.version}"
            sep = ", "
        if self.formats:
            result_str += f"{sep}formats: {self.formats}"
        
        return result_str


class MessageProtocolHandshakeErrorType(ShipMessageType):
    def __init__(
            self,
            error: MessageProtocolHandshakeErrorErrorType,
    ):
        super().__init__()
        
        self.error = error

    def get_data(self):
        msg_data = []
        
        if self.error:
            msg_data.append({"error": self.error})
        
        return msg_data

    def __str__(self):
        result_str = ""
        sep = ""
        if self.error:
            result_str += f"{sep}error: {self.error}"
        
        return result_str


class ConnectionPinStateType(ShipMessageType):
    def __init__(
            self,
            pin_state: PinStateType,
            input_permission: PinInputPermissionType = None,
    ):
        super().__init__()
        
        self.pin_state = pin_state
        self.input_permission = input_permission

    def get_data(self):
        msg_data = []
        
        if self.pin_state:
            msg_data.append({"pinState": self.pin_state})
        if self.input_permission:
            msg_data.append({"inputPermission": self.input_permission})
        
        return msg_data

    def __str__(self):
        result_str = ""
        sep = ""
        if self.pin_state:
            result_str += f"{sep}pinState: {self.pin_state}"
            sep = ", "
        if self.input_permission:
            result_str += f"{sep}inputPermission: {self.input_permission}"
        
        return result_str


class ConnectionPinInputType(ShipMessageType):
    def __init__(
            self,
            pin: PinValueType,
    ):
        super().__init__()
        
        self.pin = pin

    def get_data(self):
        msg_data = []
        
        if self.pin:
            msg_data.append({"pin": self.pin})
        
        return msg_data

    def __str__(self):
        result_str = ""
        sep = ""
        if self.pin:
            result_str += f"{sep}pin: {self.pin}"
        
        return result_str


class ConnectionPinErrorType(ShipMessageType):
    def __init__(
            self,
            error: ConnectionPinErrorErrorType,
    ):
        super().__init__()
        
        self.error = error

    def get_data(self):
        msg_data = []
        
        if self.error:
            msg_data.append({"error": self.error})
        
        return msg_data

    def __str__(self):
        result_str = ""
        sep = ""
        if self.error:
            result_str += f"{sep}error: {self.error}"
        
        return result_str


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

    def get_data(self):
        msg_data = []
        
        if self.header:
            msg_data.append({"header": self.header})
        if self.payload:
            msg_data.append({"payload": self.payload})
        if self.extension:
            msg_data.append({"extension": self.extension})
        
        return msg_data

    def __str__(self):
        result_str = ""
        sep = ""
        if self.header:
            result_str += f"{sep}header: {self.header}"
            sep = ", "
        if self.payload:
            result_str += f"{sep}payload: {self.payload}"
            sep = ", "
        if self.extension:
            result_str += f"{sep}extension: {self.extension}"
        
        return result_str


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

    def get_data(self):
        msg_data = []
        
        if self.phase:
            msg_data.append({"phase": self.phase})
        if self.max_time:
            msg_data.append({"maxTime": self.max_time})
        if self.reason:
            msg_data.append({"reason": self.reason})
        
        return msg_data

    def __str__(self):
        result_str = ""
        sep = ""
        if self.phase:
            result_str += f"{sep}phase: {self.phase}"
            sep = ", "
        if self.max_time:
            result_str += f"{sep}maxTime: {self.max_time}"
            sep = ", "
        if self.reason:
            result_str += f"{sep}reason: {self.reason}"
        
        return result_str


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


class AccessMethodsType(ShipMessageType):
    def __init__(
            self,
            id: str,
            dns_sd_m_dns = None,
            dns = None,
    ):
        super().__init__()
        
        self.id = id
        self.dns_sd_m_dns = dns_sd_m_dns
        self.dns = dns

    def get_data(self):
        msg_data = []
        
        if self.id:
            msg_data.append({"id": self.id})
        if self.dns_sd_m_dns:
            msg_data.append({"dnsSd_mDns": self.dns_sd_m_dns})
        if self.dns:
            msg_data.append({"dns": self.dns})
        
        return msg_data

    def __str__(self):
        result_str = ""
        sep = ""
        if self.id:
            result_str += f"{sep}id: {self.id}"
            sep = ", "
        if self.dns_sd_m_dns:
            result_str += f"{sep}dnsSd_mDns: {self.dns_sd_m_dns}"
            sep = ", "
        if self.dns:
            result_str += f"{sep}dns: {self.dns}"
        
        return result_str



