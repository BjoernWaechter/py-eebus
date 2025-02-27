# Jinja Template message_type.py.jinja2
from spine.base_type.commondatatypes import TimestampIntervalType
from spine.simple_type.messaging import MessagingNumberType
from spine.base_type.commondatatypes import ElementTagType
from spine.simple_type.messaging import MessagingDataTextType
from spine.union_type.commondatatypes import FunctionType
from types import NoneType
from spine import array_2_dict


class MessagingDataType:
    def __init__(
            self,
            timestamp: FunctionType = None,
            messaging_number: MessagingNumberType = None,
            type: FunctionType = None,
            text: MessagingDataTextType = None,
    ):
        super().__init__()
        
        self.timestamp = timestamp
        self.messaging_number = messaging_number
        self.type = type
        self.text = text

        if not isinstance(self.timestamp, FunctionType | NoneType):
            raise TypeError("timestamp is not of type FunctionType")
        
        if not isinstance(self.messaging_number, MessagingNumberType | NoneType):
            raise TypeError("messaging_number is not of type MessagingNumberType")
        
        if not isinstance(self.type, FunctionType | NoneType):
            raise TypeError("type is not of type FunctionType")
        
        if not isinstance(self.text, MessagingDataTextType | NoneType):
            raise TypeError("text is not of type MessagingDataTextType")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.timestamp is not None:
            msg_data.append({"timestamp": self.timestamp.get_data()})
        if self.messaging_number is not None:
            msg_data.append({"messagingNumber": self.messaging_number.get_data()})
        if self.type is not None:
            msg_data.append({"type": self.type.get_data()})
        if self.text is not None:
            msg_data.append({"text": self.text.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.timestamp is not None:
            result_str += f"{sep}timestamp: {self.timestamp}"
            sep = ", "
        if self.messaging_number is not None:
            result_str += f"{sep}messagingNumber: {self.messaging_number}"
            sep = ", "
        if self.type is not None:
            result_str += f"{sep}type: {self.type}"
            sep = ", "
        if self.text is not None:
            result_str += f"{sep}text: {self.text}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                timestamp=data_dict.get('timestamp'),
                messaging_number=data_dict.get('messagingNumber'),
                type=data_dict.get('type'),
                text=data_dict.get('text'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class MessagingListDataType:
    def __init__(
            self,
            messaging_data: list[MessagingDataType] = None,
    ):
        super().__init__()
        
        self.messaging_data = messaging_data

        if not isinstance(self.messaging_data, list | NoneType):
            raise TypeError("messaging_data is not of type list[MessagingDataType]")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.messaging_data is not None:
            msg_data.append({"messagingData": [d.get_data() for d in self.messaging_data]})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.messaging_data is not None:
            result_str += f"{sep}messagingData: {self.messaging_data}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                messaging_data=data_dict.get('messagingData'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class MessagingListDataSelectorsType:
    def __init__(
            self,
            timestamp_interval: TimestampIntervalType = None,
            messaging_number: MessagingNumberType = None,
    ):
        super().__init__()
        
        self.timestamp_interval = timestamp_interval
        self.messaging_number = messaging_number

        if not isinstance(self.timestamp_interval, TimestampIntervalType | NoneType):
            raise TypeError("timestamp_interval is not of type TimestampIntervalType")
        
        if not isinstance(self.messaging_number, MessagingNumberType | NoneType):
            raise TypeError("messaging_number is not of type MessagingNumberType")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.timestamp_interval is not None:
            msg_data.append({"timestampInterval": self.timestamp_interval.get_data()})
        if self.messaging_number is not None:
            msg_data.append({"messagingNumber": self.messaging_number.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.timestamp_interval is not None:
            result_str += f"{sep}timestampInterval: {self.timestamp_interval}"
            sep = ", "
        if self.messaging_number is not None:
            result_str += f"{sep}messagingNumber: {self.messaging_number}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                timestamp_interval=data_dict.get('timestampInterval'),
                messaging_number=data_dict.get('messagingNumber'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class MessagingDataElementsType:
    def __init__(
            self,
            timestamp: ElementTagType = None,
            messaging_number: ElementTagType = None,
            type: ElementTagType = None,
            text: ElementTagType = None,
    ):
        super().__init__()
        
        self.timestamp = timestamp
        self.messaging_number = messaging_number
        self.type = type
        self.text = text

        if not isinstance(self.timestamp, ElementTagType | NoneType):
            raise TypeError("timestamp is not of type ElementTagType")
        
        if not isinstance(self.messaging_number, ElementTagType | NoneType):
            raise TypeError("messaging_number is not of type ElementTagType")
        
        if not isinstance(self.type, ElementTagType | NoneType):
            raise TypeError("type is not of type ElementTagType")
        
        if not isinstance(self.text, ElementTagType | NoneType):
            raise TypeError("text is not of type ElementTagType")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.timestamp is not None:
            msg_data.append({"timestamp": self.timestamp.get_data()})
        if self.messaging_number is not None:
            msg_data.append({"messagingNumber": self.messaging_number.get_data()})
        if self.type is not None:
            msg_data.append({"type": self.type.get_data()})
        if self.text is not None:
            msg_data.append({"text": self.text.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.timestamp is not None:
            result_str += f"{sep}timestamp: {self.timestamp}"
            sep = ", "
        if self.messaging_number is not None:
            result_str += f"{sep}messagingNumber: {self.messaging_number}"
            sep = ", "
        if self.type is not None:
            result_str += f"{sep}type: {self.type}"
            sep = ", "
        if self.text is not None:
            result_str += f"{sep}text: {self.text}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                timestamp=data_dict.get('timestamp'),
                messaging_number=data_dict.get('messagingNumber'),
                type=data_dict.get('type'),
                text=data_dict.get('text'),
            )
        elif data:
            return cls(data)
        else:
            return cls()



