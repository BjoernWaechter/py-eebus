from dataclasses import dataclass
from ship.message_type import *
import json


def array_2_dict(arr):
    return {list(v.keys())[0]:v[list(v.keys())[0]] for v in arr}


def get_object_data(obj):
    return obj.get_data()


@dataclass()
class ShipMessage:
    def __init__(
            self
    ):
        self._root_tag = ""
        self._msg_type = b'\x00'
        self._msg: ShipMessageType = ShipMessageType()

    def get_msg_bytes(self):
        json_data = self.get_data()
        data_bytes = self._msg_type + json_data.encode('utf8')
        return data_bytes

    def get_type(self):
        return self._msg_type

    @classmethod
    def from_data(cls, bin_msg):
        first_byte = bin_msg[0:1]
        msg_type = MessageType(first_byte)
        data = json.loads(bin_msg[1:].decode("utf8"))
        root_tag = list(data.keys())[0]

        msg = ROOT_TAG_2_TYPE[root_tag].from_data(data[root_tag])

        if msg_type != msg.get_type():
            raise RuntimeError("Message type of restored message does not match the type of the parsed one.")

        return msg

    def get_data(self):
        if self._msg:
            return json.dumps({self._root_tag: self._msg.get_data()}, separators=(',', ':'), default=get_object_data)
        else:
            return ""


class Cmi(ShipMessage):
    def __init__(
            self,
    ):
        super().__init__()
        self._msg_type = MessageType.MSG_TYPE_INIT
        self._msg = None

    @classmethod
    def from_data(cls, data):
        return cls()

    def get_msg_bytes(self):
        data_bytes = self._msg_type + b'\x00'
        return data_bytes

    def get_data(self):
        return None


class ConnectionHello(ShipMessage):
    def __init__(
            self,
            phase: ConnectionHelloPhaseType,
            waiting: int = None,
            prolongationrequest: bool = None,
    ):
        super().__init__()
        
        if waiting is None:
            waiting = 60000
        self._msg_type = MessageType.MSG_TYPE_CONTROL
        self._root_tag = "connectionHello"
        self._msg = ConnectionHelloType(
            phase=phase,
            waiting=waiting,
            prolongationrequest=prolongationrequest,
        )

    @classmethod
    def from_data(cls, data):
        data_dict = array_2_dict(data)
        return cls(
            phase=data_dict['phase'], 
            waiting=data_dict['waiting'], 
            prolongationrequest=data_dict['prolongationRequest'], 
        )


class MessageProtocolHandshake(ShipMessage):
    def __init__(
            self,
            handshaketype: ProtocolHandshakeTypeType,
            version = None,
            formats: MessageProtocolFormatsType = None,
    ):
        super().__init__()
        
        if version is None:
            version = [{"major": 1}, {"minor": 0}]
        if formats is None:
            formats = [{"format": ["JSON-UTF8"]}]
        self._msg_type = MessageType.MSG_TYPE_CONTROL
        self._root_tag = "messageProtocolHandshake"
        self._msg = MessageProtocolHandshakeType(
            handshaketype=handshaketype,
            version=version,
            formats=formats,
        )

    @classmethod
    def from_data(cls, data):
        data_dict = array_2_dict(data)
        return cls(
            handshaketype=data_dict['handshakeType'], 
            version=data_dict['version'], 
            formats=data_dict['formats'], 
        )


class MessageProtocolHandshakeError(ShipMessage):
    def __init__(
            self,
            error: MessageProtocolHandshakeErrorErrorType,
    ):
        super().__init__()
        
        self._msg_type = MessageType.MSG_TYPE_CONTROL
        self._root_tag = "messageProtocolHandshakeError"
        self._msg = MessageProtocolHandshakeErrorType(
            error=error,
        )

    @classmethod
    def from_data(cls, data):
        data_dict = array_2_dict(data)
        return cls(
            error=data_dict['error'], 
        )


class ConnectionPinState(ShipMessage):
    def __init__(
            self,
            pinstate: PinStateType,
            inputpermission: PinInputPermissionType = None,
    ):
        super().__init__()
        
        self._msg_type = MessageType.MSG_TYPE_CONTROL
        self._root_tag = "connectionPinState"
        self._msg = ConnectionPinStateType(
            pinstate=pinstate,
            inputpermission=inputpermission,
        )

    @classmethod
    def from_data(cls, data):
        data_dict = array_2_dict(data)
        return cls(
            pinstate=data_dict['pinState'], 
            inputpermission=data_dict['inputPermission'], 
        )


class ConnectionPinInput(ShipMessage):
    def __init__(
            self,
            pin: PinValueType,
    ):
        super().__init__()
        
        self._msg_type = MessageType.MSG_TYPE_CONTROL
        self._root_tag = "connectionPinInput"
        self._msg = ConnectionPinInputType(
            pin=pin,
        )

    @classmethod
    def from_data(cls, data):
        data_dict = array_2_dict(data)
        return cls(
            pin=data_dict['pin'], 
        )


class ConnectionPinError(ShipMessage):
    def __init__(
            self,
            error: ConnectionPinErrorErrorType,
    ):
        super().__init__()
        
        self._msg_type = MessageType.MSG_TYPE_CONTROL
        self._root_tag = "connectionPinError"
        self._msg = ConnectionPinErrorType(
            error=error,
        )

    @classmethod
    def from_data(cls, data):
        data_dict = array_2_dict(data)
        return cls(
            error=data_dict['error'], 
        )


class Data(ShipMessage):
    def __init__(
            self,
            header: HeaderType,
            payload,
            extension: ExtensionType = None,
    ):
        super().__init__()
        
        self._msg_type = MessageType.MSG_TYPE_DATA
        self._root_tag = "data"
        self._msg = DataType(
            header=header,
            payload=payload,
            extension=extension,
        )

    @classmethod
    def from_data(cls, data):
        data_dict = array_2_dict(data)
        return cls(
            header=data_dict['header'], 
            payload=data_dict['payload'], 
            extension=data_dict['extension'], 
        )


class ConnectionClose(ShipMessage):
    def __init__(
            self,
            phase: ConnectionClosePhaseType,
            maxtime: int = None,
            reason: ConnectionCloseReasonType = None,
    ):
        super().__init__()
        
        self._msg_type = MessageType.MSG_TYPE_END
        self._root_tag = "connectionClose"
        self._msg = ConnectionCloseType(
            phase=phase,
            maxtime=maxtime,
            reason=reason,
        )

    @classmethod
    def from_data(cls, data):
        data_dict = array_2_dict(data)
        return cls(
            phase=data_dict['phase'], 
            maxtime=data_dict['maxTime'], 
            reason=data_dict['reason'], 
        )


class AccessMethodsRequest(ShipMessage):
    def __init__(
            self,
    ):
        super().__init__()
        
        self._msg_type = MessageType.MSG_TYPE_CONTROL
        self._root_tag = "accessMethodsRequest"
        self._msg = AccessMethodsRequestType(
        )

    @classmethod
    def from_data(cls, data):
        data_dict = array_2_dict(data)
        return cls(
        )


class AccessMethods(ShipMessage):
    def __init__(
            self,
            id: str,
            dnssd_mdns = None,
            dns = None,
    ):
        super().__init__()
        
        self._msg_type = MessageType.MSG_TYPE_CONTROL
        self._root_tag = "accessMethods"
        self._msg = AccessMethodsType(
            id=id,
            dnssd_mdns=dnssd_mdns,
            dns=dns,
        )

    @classmethod
    def from_data(cls, data):
        data_dict = array_2_dict(data)
        return cls(
            id=data_dict['id'], 
            dnssd_mdns=data_dict['dnsSd_mDns'], 
            dns=data_dict['dns'], 
        )


ROOT_TAG_2_TYPE = {
    "connectionHello": ConnectionHello,
    "messageProtocolHandshake": MessageProtocolHandshake,
    "messageProtocolHandshakeError": MessageProtocolHandshakeError,
    "connectionPinState": ConnectionPinState,
    "connectionPinInput": ConnectionPinInput,
    "connectionPinError": ConnectionPinError,
    "data": Data,
    "connectionClose": ConnectionClose,
    "accessMethodsRequest": AccessMethodsRequest,
    "accessMethods": AccessMethods,
}