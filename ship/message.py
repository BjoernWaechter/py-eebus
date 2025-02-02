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
        if msg_type != MessageType.MSG_TYPE_INIT:
            data = json.loads(bin_msg[1:].decode("utf8"))
            root_tag = list(data.keys())[0]
            msg = ROOT_TAG_2_TYPE[root_tag].from_data(data[root_tag])
        else:
            msg = Cmi()

        if msg_type != msg.get_type():
            raise RuntimeError("Message type of restored message does not match the type of the parsed one.")

        return msg

    def get_data(self):
        if self._msg:
            return json.dumps({self._root_tag: self._msg.get_data()}, separators=(',', ':'), default=get_object_data)
        else:
            return ""

    def __str__(self):
        return f"{self.__class__.__name__}({int.from_bytes(self._msg_type, 'big')}, {self._msg})"

    def msg(self):
        return self._msg


class Cmi(ShipMessage):
    def __init__(
            self,
            data = None
    ):
        super().__init__()
        self._msg_type = MessageType.MSG_TYPE_INIT
        if data is None:
            data = b'\x00'
        self._msg = data

    @classmethod
    def from_data(cls, data):
        return cls(data[1:2])

    def get_msg_bytes(self):
        data_bytes = self._msg_type + self._msg
        return data_bytes



class ConnectionHello(ShipMessage):
    def __init__(
            self,
            phase: ConnectionHelloPhaseType,
            waiting: int = None,
            prolongation_request: bool = None,
    ):
        super().__init__()
        
        if waiting is None:
            waiting = 60000
        self._msg_type = MessageType.MSG_TYPE_CONTROL
        self._root_tag = "connectionHello"
        self._msg = ConnectionHelloType(
            phase=phase,
            waiting=waiting,
            prolongation_request=prolongation_request,
        )

    @classmethod
    def from_data(cls, data):
        data_dict = array_2_dict(data)
        return cls(
            phase=ConnectionHelloPhaseType(data_dict.get('phase')) if 'phase' in data_dict else None, 
            waiting=data_dict.get('waiting'), 
            prolongation_request=data_dict.get('prolongationRequest'), 
        )


class MessageProtocolHandshake(ShipMessage):
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
        self._msg_type = MessageType.MSG_TYPE_CONTROL
        self._root_tag = "messageProtocolHandshake"
        self._msg = MessageProtocolHandshakeType(
            handshake_type=handshake_type,
            version=version,
            formats=formats,
        )

    @classmethod
    def from_data(cls, data):
        data_dict = array_2_dict(data)
        return cls(
            handshake_type=ProtocolHandshakeTypeType(data_dict.get('handshakeType')) if 'handshakeType' in data_dict else None, 
            version=Version.from_data(data_dict.get('version')) if 'version' in data_dict else None, 
            formats=MessageProtocolFormatsType.from_data(data_dict.get('formats')) if 'formats' in data_dict else None, 
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
            error=MessageProtocolHandshakeErrorErrorType.from_data(data_dict.get('error')) if 'error' in data_dict else None, 
        )


class ConnectionPinState(ShipMessage):
    def __init__(
            self,
            pin_state: PinStateType,
            input_permission: PinInputPermissionType = None,
    ):
        super().__init__()
        
        self._msg_type = MessageType.MSG_TYPE_CONTROL
        self._root_tag = "connectionPinState"
        self._msg = ConnectionPinStateType(
            pin_state=pin_state,
            input_permission=input_permission,
        )

    @classmethod
    def from_data(cls, data):
        data_dict = array_2_dict(data)
        return cls(
            pin_state=PinStateType(data_dict.get('pinState')) if 'pinState' in data_dict else None, 
            input_permission=PinInputPermissionType(data_dict.get('inputPermission')) if 'inputPermission' in data_dict else None, 
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
            pin=PinValueType.from_data(data_dict.get('pin')) if 'pin' in data_dict else None, 
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
            error=ConnectionPinErrorErrorType.from_data(data_dict.get('error')) if 'error' in data_dict else None, 
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
            header=HeaderType.from_data(data_dict.get('header')) if 'header' in data_dict else None, 
            payload=data_dict.get('payload'), 
            extension=ExtensionType.from_data(data_dict.get('extension')) if 'extension' in data_dict else None, 
        )


class ConnectionClose(ShipMessage):
    def __init__(
            self,
            phase: ConnectionClosePhaseType,
            max_time: int = None,
            reason: ConnectionCloseReasonType = None,
    ):
        super().__init__()
        
        self._msg_type = MessageType.MSG_TYPE_END
        self._root_tag = "connectionClose"
        self._msg = ConnectionCloseType(
            phase=phase,
            max_time=max_time,
            reason=reason,
        )

    @classmethod
    def from_data(cls, data):
        data_dict = array_2_dict(data)
        return cls(
            phase=ConnectionClosePhaseType(data_dict.get('phase')) if 'phase' in data_dict else None, 
            max_time=data_dict.get('maxTime'), 
            reason=ConnectionCloseReasonType(data_dict.get('reason')) if 'reason' in data_dict else None, 
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
            dns_sd_m_dns: DnsSd_MDns = None,
            dns: Dns = None,
    ):
        super().__init__()
        
        self._msg_type = MessageType.MSG_TYPE_CONTROL
        self._root_tag = "accessMethods"
        self._msg = AccessMethodsType(
            id=id,
            dns_sd_m_dns=dns_sd_m_dns,
            dns=dns,
        )

    @classmethod
    def from_data(cls, data):
        data_dict = array_2_dict(data)
        return cls(
            id=data_dict.get('id'), 
            dns_sd_m_dns=DnsSd_MDns.from_data(data_dict.get('dnsSd_mDns')) if 'dnsSd_mDns' in data_dict else None, 
            dns=Dns.from_data(data_dict.get('dns')) if 'dns' in data_dict else None, 
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