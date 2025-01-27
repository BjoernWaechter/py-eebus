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
        self.root_tag = ""
        self.msg_type = b'\x00'

    def get_data(self):
        raise NotImplementedError("get_data has to be implemented")


class ConnectionHelloType(ShipMessageType):
    def __init__(
        self,
        phase: ConnectionHelloPhaseType,
        waiting: int=None,
        prolongation_request: bool=None,
    ):
        super().__init__()
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


class MessageProtocolHandshakeType(ShipMessageType):
    def __init__(
        self,
        handshake_type: ProtocolHandshakeTypeType,
        version,
        formats: MessageProtocolFormatsType,
    ):
        super().__init__()
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


class ConnectionPinStateType(ShipMessageType):
    def __init__(
        self,
        pin_state: PinStateType,
        input_permission: PinInputPermissionType=None,
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


class DataType(ShipMessageType):
    def __init__(
        self,
        header: HeaderType,
        payload,
        extension: ExtensionType=None,
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


class ConnectionCloseType(ShipMessageType):
    def __init__(
        self,
        phase: ConnectionClosePhaseType,
        max_time: int=None,
        reason: ConnectionCloseReasonType=None,
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


class AccessMethodsRequestType(ShipMessageType):
    def __init__(
        self,
    ):
        super().__init__()

    def get_data(self):
        msg_data = []
        
        
        
        return msg_data


class AccessMethodsType(ShipMessageType):
    def __init__(
        self,
        id: str,
        dns_sd_m_dns=None,
        dns=None,
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

