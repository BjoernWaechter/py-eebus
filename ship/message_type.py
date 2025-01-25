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
        prolongationrequest: bool=None,
    ):
        super().__init__()
        self.phase = phase
        self.waiting = waiting
        self.prolongationrequest = prolongationrequest

    def get_data(self):
        msg_data = []
        
        if self.phase:
            msg_data.append({"phase": self.phase})
        if self.waiting:
            msg_data.append({"waiting": self.waiting})
        if self.prolongationrequest:
            msg_data.append({"prolongationRequest": self.prolongationrequest})
        
        
        return msg_data


class MessageProtocolHandshakeType(ShipMessageType):
    def __init__(
        self,
        handshaketype: ProtocolHandshakeTypeType,
        version,
        formats: MessageProtocolFormatsType,
    ):
        super().__init__()
        self.handshaketype = handshaketype
        self.version = version
        self.formats = formats

    def get_data(self):
        msg_data = []
        
        if self.handshaketype:
            msg_data.append({"handshakeType": self.handshaketype})
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
        pinstate: PinStateType,
        inputpermission: PinInputPermissionType=None,
    ):
        super().__init__()
        self.pinstate = pinstate
        self.inputpermission = inputpermission

    def get_data(self):
        msg_data = []
        
        if self.pinstate:
            msg_data.append({"pinState": self.pinstate})
        if self.inputpermission:
            msg_data.append({"inputPermission": self.inputpermission})
        
        
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
        maxtime: int=None,
        reason: ConnectionCloseReasonType=None,
    ):
        super().__init__()
        self.phase = phase
        self.maxtime = maxtime
        self.reason = reason

    def get_data(self):
        msg_data = []
        
        if self.phase:
            msg_data.append({"phase": self.phase})
        if self.maxtime:
            msg_data.append({"maxTime": self.maxtime})
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
        dnssd_mdns=None,
        dns=None,
    ):
        super().__init__()
        self.id = id
        self.dnssd_mdns = dnssd_mdns
        self.dns = dns

    def get_data(self):
        msg_data = []
        
        if self.id:
            msg_data.append({"id": self.id})
        if self.dnssd_mdns:
            msg_data.append({"dnsSd_mDns": self.dnssd_mdns})
        if self.dns:
            msg_data.append({"dns": self.dns})
        
        
        return msg_data

