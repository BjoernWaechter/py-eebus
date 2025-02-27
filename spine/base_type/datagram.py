# Jinja Template message_type.py.jinja2
from spine.simple_type.commondatatypes import SpecificationVersionType
from spine.enums.commandframe import CmdClassifierType
from spine.union_type.actuatorlevel import ActuatorLevelFctType
from spine.base_type.commandframe import CmdType
from spine.simple_type.commandframe import MsgCounterType
from spine.base_type.commondatatypes import FeatureAddressType
from types import NoneType
from spine import array_2_dict


class PayloadType:
    def __init__(
            self,
            cmd: list[CmdType] = None,
    ):
        super().__init__()
        
        self.cmd = cmd

        if not isinstance(self.cmd, list | NoneType):
            raise TypeError("cmd is not of type list[CmdType]")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.cmd is not None:
            msg_data.append({"cmd": [d.get_data() for d in self.cmd]})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.cmd is not None:
            result_str += f"{sep}cmd: {self.cmd}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                cmd=data_dict.get('cmd'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class HeaderType:
    def __init__(
            self,
            specification_version: SpecificationVersionType = None,
            address_source: FeatureAddressType = None,
            address_destination: FeatureAddressType = None,
            address_originator: FeatureAddressType = None,
            msg_counter: MsgCounterType = None,
            msg_counter_reference: MsgCounterType = None,
            cmd_classifier: CmdClassifierType = None,
            ack_request: bool = None,
            timestamp: ActuatorLevelFctType = None,
    ):
        super().__init__()
        
        self.specification_version = specification_version
        self.address_source = address_source
        self.address_destination = address_destination
        self.address_originator = address_originator
        self.msg_counter = msg_counter
        self.msg_counter_reference = msg_counter_reference
        self.cmd_classifier = cmd_classifier
        self.ack_request = ack_request
        self.timestamp = timestamp

        if not isinstance(self.specification_version, SpecificationVersionType | NoneType):
            raise TypeError("specification_version is not of type SpecificationVersionType")
        
        if not isinstance(self.address_source, FeatureAddressType | NoneType):
            raise TypeError("address_source is not of type FeatureAddressType")
        
        if not isinstance(self.address_destination, FeatureAddressType | NoneType):
            raise TypeError("address_destination is not of type FeatureAddressType")
        
        if not isinstance(self.address_originator, FeatureAddressType | NoneType):
            raise TypeError("address_originator is not of type FeatureAddressType")
        
        if not isinstance(self.msg_counter, MsgCounterType | NoneType):
            raise TypeError("msg_counter is not of type MsgCounterType")
        
        if not isinstance(self.msg_counter_reference, MsgCounterType | NoneType):
            raise TypeError("msg_counter_reference is not of type MsgCounterType")
        
        if not isinstance(self.cmd_classifier, CmdClassifierType | NoneType):
            raise TypeError("cmd_classifier is not of type CmdClassifierType")
        
        if not isinstance(self.ack_request, bool | NoneType):
            raise TypeError("ack_request is not of type bool")
        
        if not isinstance(self.timestamp, ActuatorLevelFctType | NoneType):
            raise TypeError("timestamp is not of type ActuatorLevelFctType")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.specification_version is not None:
            msg_data.append({"specificationVersion": self.specification_version.get_data()})
        if self.address_source is not None:
            msg_data.append({"addressSource": self.address_source.get_data()})
        if self.address_destination is not None:
            msg_data.append({"addressDestination": self.address_destination.get_data()})
        if self.address_originator is not None:
            msg_data.append({"addressOriginator": self.address_originator.get_data()})
        if self.msg_counter is not None:
            msg_data.append({"msgCounter": self.msg_counter.get_data()})
        if self.msg_counter_reference is not None:
            msg_data.append({"msgCounterReference": self.msg_counter_reference.get_data()})
        if self.cmd_classifier is not None:
            msg_data.append({"cmdClassifier": self.cmd_classifier.value})
        if self.ack_request is not None:
            msg_data.append({"ackRequest": self.ack_request})
        if self.timestamp is not None:
            msg_data.append({"timestamp": self.timestamp.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.specification_version is not None:
            result_str += f"{sep}specificationVersion: {self.specification_version}"
            sep = ", "
        if self.address_source is not None:
            result_str += f"{sep}addressSource: {self.address_source}"
            sep = ", "
        if self.address_destination is not None:
            result_str += f"{sep}addressDestination: {self.address_destination}"
            sep = ", "
        if self.address_originator is not None:
            result_str += f"{sep}addressOriginator: {self.address_originator}"
            sep = ", "
        if self.msg_counter is not None:
            result_str += f"{sep}msgCounter: {self.msg_counter}"
            sep = ", "
        if self.msg_counter_reference is not None:
            result_str += f"{sep}msgCounterReference: {self.msg_counter_reference}"
            sep = ", "
        if self.cmd_classifier is not None:
            result_str += f"{sep}cmdClassifier: {self.cmd_classifier}"
            sep = ", "
        if self.ack_request is not None:
            result_str += f"{sep}ackRequest: {self.ack_request}"
            sep = ", "
        if self.timestamp is not None:
            result_str += f"{sep}timestamp: {self.timestamp}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                specification_version=data_dict.get('specificationVersion'),
                address_source=data_dict.get('addressSource'),
                address_destination=data_dict.get('addressDestination'),
                address_originator=data_dict.get('addressOriginator'),
                msg_counter=data_dict.get('msgCounter'),
                msg_counter_reference=data_dict.get('msgCounterReference'),
                cmd_classifier=data_dict.get('cmdClassifier'),
                ack_request=data_dict.get('ackRequest'),
                timestamp=data_dict.get('timestamp'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class DatagramType:
    def __init__(
            self,
            header: HeaderType,
            payload: PayloadType,
    ):
        super().__init__()
        
        self.header = header
        self.payload = payload

        if not isinstance(self.header, HeaderType):
            raise TypeError("header is not of type HeaderType")
        
        if not isinstance(self.payload, PayloadType):
            raise TypeError("payload is not of type PayloadType")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.header is not None:
            msg_data.append({"header": self.header.get_data()})
        if self.payload is not None:
            msg_data.append({"payload": self.payload.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.header is not None:
            result_str += f"{sep}header: {self.header}"
            sep = ", "
        if self.payload is not None:
            result_str += f"{sep}payload: {self.payload}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                header=data_dict.get('header'),
                payload=data_dict.get('payload'),
            )
        elif data:
            return cls(data)
        else:
            return cls()



