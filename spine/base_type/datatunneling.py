# Jinja Template message_type.py.jinja2
from spine.simple_type.datatunneling import PurposeIdType
from spine.simple_type.datatunneling import ChannelIdType
from spine.base_type.commondatatypes import ElementTagType
from types import NoneType
from spine import array_2_dict


class DataTunnelingHeaderType:
    def __init__(
            self,
            purpose_id: PurposeIdType = None,
            channel_id: ChannelIdType = None,
            sequence_id: int = None,
    ):
        super().__init__()
        
        self.purpose_id = purpose_id
        self.channel_id = channel_id
        self.sequence_id = sequence_id

        if not isinstance(self.purpose_id, PurposeIdType | NoneType):
            raise TypeError("purpose_id is not of type PurposeIdType")
        
        if not isinstance(self.channel_id, ChannelIdType | NoneType):
            raise TypeError("channel_id is not of type ChannelIdType")
        
        if not isinstance(self.sequence_id, int | NoneType):
            raise TypeError("sequence_id is not of type int")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.purpose_id is not None:
            msg_data.append({"purposeId": self.purpose_id.get_data()})
        if self.channel_id is not None:
            msg_data.append({"channelId": self.channel_id.get_data()})
        if self.sequence_id is not None:
            msg_data.append({"sequenceId": self.sequence_id})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.purpose_id is not None:
            result_str += f"{sep}purposeId: {self.purpose_id}"
            sep = ", "
        if self.channel_id is not None:
            result_str += f"{sep}channelId: {self.channel_id}"
            sep = ", "
        if self.sequence_id is not None:
            result_str += f"{sep}sequenceId: {self.sequence_id}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                purpose_id=data_dict.get('purposeId'),
                channel_id=data_dict.get('channelId'),
                sequence_id=data_dict.get('sequenceId'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class DataTunnelingHeaderElementsType:
    def __init__(
            self,
            purpose_id: ElementTagType = None,
            channel_id: ElementTagType = None,
            sequence_id: ElementTagType = None,
    ):
        super().__init__()
        
        self.purpose_id = purpose_id
        self.channel_id = channel_id
        self.sequence_id = sequence_id

        if not isinstance(self.purpose_id, ElementTagType | NoneType):
            raise TypeError("purpose_id is not of type ElementTagType")
        
        if not isinstance(self.channel_id, ElementTagType | NoneType):
            raise TypeError("channel_id is not of type ElementTagType")
        
        if not isinstance(self.sequence_id, ElementTagType | NoneType):
            raise TypeError("sequence_id is not of type ElementTagType")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.purpose_id is not None:
            msg_data.append({"purposeId": self.purpose_id.get_data()})
        if self.channel_id is not None:
            msg_data.append({"channelId": self.channel_id.get_data()})
        if self.sequence_id is not None:
            msg_data.append({"sequenceId": self.sequence_id.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.purpose_id is not None:
            result_str += f"{sep}purposeId: {self.purpose_id}"
            sep = ", "
        if self.channel_id is not None:
            result_str += f"{sep}channelId: {self.channel_id}"
            sep = ", "
        if self.sequence_id is not None:
            result_str += f"{sep}sequenceId: {self.sequence_id}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                purpose_id=data_dict.get('purposeId'),
                channel_id=data_dict.get('channelId'),
                sequence_id=data_dict.get('sequenceId'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class DataTunnelingCallType:
    def __init__(
            self,
            header: DataTunnelingHeaderType = None,
            payload: str = None,
    ):
        super().__init__()
        
        self.header = header
        self.payload = payload

        if not isinstance(self.header, DataTunnelingHeaderType | NoneType):
            raise TypeError("header is not of type DataTunnelingHeaderType")
        
        if not isinstance(self.payload, str | NoneType):
            raise TypeError("payload is not of type str")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.header is not None:
            msg_data.append({"header": self.header.get_data()})
        if self.payload is not None:
            msg_data.append({"payload": self.payload})
        
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


class DataTunnelingCallElementsType:
    def __init__(
            self,
            header: DataTunnelingHeaderElementsType = None,
            payload: ElementTagType = None,
    ):
        super().__init__()
        
        self.header = header
        self.payload = payload

        if not isinstance(self.header, DataTunnelingHeaderElementsType | NoneType):
            raise TypeError("header is not of type DataTunnelingHeaderElementsType")
        
        if not isinstance(self.payload, ElementTagType | NoneType):
            raise TypeError("payload is not of type ElementTagType")
        
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



