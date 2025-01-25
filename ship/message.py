from ship.message_type import *
import json

MSG_TYPE_INIT = b'\x00\x00'
MSG_TYPE_CONTROL = b'\x01'
MSG_TYPE_DATA = b'\x02'
MSG_TYPE_END = b'\x03'

def get_object_data(obj):
    return obj.get_data()

class ShipMessage:
    def __init__(
        self
    ):
        self.root_tag = ""
        self.msg_type = b'\x00'
        self.msg: ShipMessageType = ShipMessageType()

    def get_msg_bytes(self):
        if self.msg:
            json_data = json.dumps({self.root_tag: self.msg.get_data()}, separators=(',', ':'), default=get_object_data)
        else:
            json_data = ""
        json_bytes = self.msg_type + json_data.encode('utf8')
        return json_bytes


class ConnectionHello(ShipMessage):
    def __init__(
        self,
        phase: ConnectionHelloPhaseType,
        waiting: int=None,
        prolongationrequest: bool=None,
    ):
        super().__init__()
        
        if waiting is None:
            waiting = 60000
        
        
        self.msg_type = MSG_TYPE_CONTROL
        self.root_tag = "connectionHello"
        self.msg = ConnectionHelloType(
            phase=phase,
            waiting=waiting,
            prolongationrequest=prolongationrequest,
        )


class MessageProtocolHandshake(ShipMessage):
    def __init__(
        self,
        handshaketype: ProtocolHandshakeTypeType,
        version=None,
        formats: MessageProtocolFormatsType=None,
    ):
        super().__init__()
        
        if version is None:
            version = [{"major": 1}, {"minor": 0}]
        if formats is None:
            formats = [{"format": ["JSON-UTF8"]}]
        
        self.msg_type = MSG_TYPE_CONTROL
        self.root_tag = "messageProtocolHandshake"
        self.msg = MessageProtocolHandshakeType(
            handshaketype=handshaketype,
            version=version,
            formats=formats,
        )


class MessageProtocolHandshakeError(ShipMessage):
    def __init__(
        self,
        error: MessageProtocolHandshakeErrorErrorType,
    ):
        super().__init__()
        
        
        self.msg_type = MSG_TYPE_CONTROL
        self.root_tag = "messageProtocolHandshakeError"
        self.msg = MessageProtocolHandshakeErrorType(
            error=error,
        )


class ConnectionPinState(ShipMessage):
    def __init__(
        self,
        pinstate: PinStateType,
        inputpermission: PinInputPermissionType=None,
    ):
        super().__init__()
        
        
        
        self.msg_type = MSG_TYPE_CONTROL
        self.root_tag = "connectionPinState"
        self.msg = ConnectionPinStateType(
            pinstate=pinstate,
            inputpermission=inputpermission,
        )


class ConnectionPinInput(ShipMessage):
    def __init__(
        self,
        pin: PinValueType,
    ):
        super().__init__()
        
        
        self.msg_type = MSG_TYPE_CONTROL
        self.root_tag = "connectionPinInput"
        self.msg = ConnectionPinInputType(
            pin=pin,
        )


class ConnectionPinError(ShipMessage):
    def __init__(
        self,
        error: ConnectionPinErrorErrorType,
    ):
        super().__init__()
        
        
        self.msg_type = MSG_TYPE_CONTROL
        self.root_tag = "connectionPinError"
        self.msg = ConnectionPinErrorType(
            error=error,
        )


class Data(ShipMessage):
    def __init__(
        self,
        header: HeaderType,
        payload,
        extension: ExtensionType=None,
    ):
        super().__init__()
        
        
        
        
        self.msg_type = MSG_TYPE_DATA
        self.root_tag = "data"
        self.msg = DataType(
            header=header,
            payload=payload,
            extension=extension,
        )


class ConnectionClose(ShipMessage):
    def __init__(
        self,
        phase: ConnectionClosePhaseType,
        maxtime: int=None,
        reason: ConnectionCloseReasonType=None,
    ):
        super().__init__()
        
        
        
        
        self.msg_type = MSG_TYPE_END
        self.root_tag = "connectionClose"
        self.msg = ConnectionCloseType(
            phase=phase,
            maxtime=maxtime,
            reason=reason,
        )


class AccessMethodsRequest(ShipMessage):
    def __init__(
        self,
    ):
        super().__init__()
        
        self.msg_type = MSG_TYPE_CONTROL
        self.root_tag = "accessMethodsRequest"
        self.msg = AccessMethodsRequestType(
        )


class AccessMethods(ShipMessage):
    def __init__(
        self,
        id: str,
        dnssd_mdns=None,
        dns=None,
    ):
        super().__init__()
        
        
        
        
        self.msg_type = MSG_TYPE_CONTROL
        self.root_tag = "accessMethods"
        self.msg = AccessMethodsType(
            id=id,
            dnssd_mdns=dnssd_mdns,
            dns=dns,
        )

