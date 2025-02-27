# Jinja Template message_type.py.jinja2
from spine.simple_type.commondatatypes import LabelType
from spine.base_type.commondatatypes import TimestampIntervalType
from spine.simple_type.commondatatypes import DescriptionType
from spine.base_type.commondatatypes import ScaledNumberElementsType
from spine.base_type.commondatatypes import ElementTagType
from spine.union_type.commondatatypes import FunctionType
from spine.base_type.commondatatypes import ScaledNumberType
from types import NoneType
from spine import array_2_dict


class SensingDataType:
    def __init__(
            self,
            timestamp: FunctionType = None,
            state: FunctionType = None,
            value: ScaledNumberType = None,
    ):
        super().__init__()
        
        self.timestamp = timestamp
        self.state = state
        self.value = value

        if not isinstance(self.timestamp, FunctionType | NoneType):
            raise TypeError("timestamp is not of type FunctionType")
        
        if not isinstance(self.state, FunctionType | NoneType):
            raise TypeError("state is not of type FunctionType")
        
        if not isinstance(self.value, ScaledNumberType | NoneType):
            raise TypeError("value is not of type ScaledNumberType")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.timestamp is not None:
            msg_data.append({"timestamp": self.timestamp.get_data()})
        if self.state is not None:
            msg_data.append({"state": self.state.get_data()})
        if self.value is not None:
            msg_data.append({"value": self.value.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.timestamp is not None:
            result_str += f"{sep}timestamp: {self.timestamp}"
            sep = ", "
        if self.state is not None:
            result_str += f"{sep}state: {self.state}"
            sep = ", "
        if self.value is not None:
            result_str += f"{sep}value: {self.value}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                timestamp=data_dict.get('timestamp'),
                state=data_dict.get('state'),
                value=data_dict.get('value'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class SensingListDataType:
    def __init__(
            self,
            sensing_data: list[SensingDataType] = None,
    ):
        super().__init__()
        
        self.sensing_data = sensing_data

        if not isinstance(self.sensing_data, list | NoneType):
            raise TypeError("sensing_data is not of type list[SensingDataType]")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.sensing_data is not None:
            msg_data.append({"sensingData": [d.get_data() for d in self.sensing_data]})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.sensing_data is not None:
            result_str += f"{sep}sensingData: {self.sensing_data}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                sensing_data=data_dict.get('sensingData'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class SensingListDataSelectorsType:
    def __init__(
            self,
            timestamp_interval: TimestampIntervalType = None,
    ):
        super().__init__()
        
        self.timestamp_interval = timestamp_interval

        if not isinstance(self.timestamp_interval, TimestampIntervalType | NoneType):
            raise TypeError("timestamp_interval is not of type TimestampIntervalType")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.timestamp_interval is not None:
            msg_data.append({"timestampInterval": self.timestamp_interval.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.timestamp_interval is not None:
            result_str += f"{sep}timestampInterval: {self.timestamp_interval}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                timestamp_interval=data_dict.get('timestampInterval'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class SensingDescriptionDataType:
    def __init__(
            self,
            sensing_type: FunctionType = None,
            unit: FunctionType = None,
            scope_type: FunctionType = None,
            label: LabelType = None,
            description: DescriptionType = None,
    ):
        super().__init__()
        
        self.sensing_type = sensing_type
        self.unit = unit
        self.scope_type = scope_type
        self.label = label
        self.description = description

        if not isinstance(self.sensing_type, FunctionType | NoneType):
            raise TypeError("sensing_type is not of type FunctionType")
        
        if not isinstance(self.unit, FunctionType | NoneType):
            raise TypeError("unit is not of type FunctionType")
        
        if not isinstance(self.scope_type, FunctionType | NoneType):
            raise TypeError("scope_type is not of type FunctionType")
        
        if not isinstance(self.label, LabelType | NoneType):
            raise TypeError("label is not of type LabelType")
        
        if not isinstance(self.description, DescriptionType | NoneType):
            raise TypeError("description is not of type DescriptionType")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.sensing_type is not None:
            msg_data.append({"sensingType": self.sensing_type.get_data()})
        if self.unit is not None:
            msg_data.append({"unit": self.unit.get_data()})
        if self.scope_type is not None:
            msg_data.append({"scopeType": self.scope_type.get_data()})
        if self.label is not None:
            msg_data.append({"label": self.label.get_data()})
        if self.description is not None:
            msg_data.append({"description": self.description.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.sensing_type is not None:
            result_str += f"{sep}sensingType: {self.sensing_type}"
            sep = ", "
        if self.unit is not None:
            result_str += f"{sep}unit: {self.unit}"
            sep = ", "
        if self.scope_type is not None:
            result_str += f"{sep}scopeType: {self.scope_type}"
            sep = ", "
        if self.label is not None:
            result_str += f"{sep}label: {self.label}"
            sep = ", "
        if self.description is not None:
            result_str += f"{sep}description: {self.description}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                sensing_type=data_dict.get('sensingType'),
                unit=data_dict.get('unit'),
                scope_type=data_dict.get('scopeType'),
                label=data_dict.get('label'),
                description=data_dict.get('description'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class SensingDescriptionDataElementsType:
    def __init__(
            self,
            sensing_type: ElementTagType = None,
            unit: ElementTagType = None,
            scope_type: ElementTagType = None,
            label: ElementTagType = None,
            description: ElementTagType = None,
    ):
        super().__init__()
        
        self.sensing_type = sensing_type
        self.unit = unit
        self.scope_type = scope_type
        self.label = label
        self.description = description

        if not isinstance(self.sensing_type, ElementTagType | NoneType):
            raise TypeError("sensing_type is not of type ElementTagType")
        
        if not isinstance(self.unit, ElementTagType | NoneType):
            raise TypeError("unit is not of type ElementTagType")
        
        if not isinstance(self.scope_type, ElementTagType | NoneType):
            raise TypeError("scope_type is not of type ElementTagType")
        
        if not isinstance(self.label, ElementTagType | NoneType):
            raise TypeError("label is not of type ElementTagType")
        
        if not isinstance(self.description, ElementTagType | NoneType):
            raise TypeError("description is not of type ElementTagType")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.sensing_type is not None:
            msg_data.append({"sensingType": self.sensing_type.get_data()})
        if self.unit is not None:
            msg_data.append({"unit": self.unit.get_data()})
        if self.scope_type is not None:
            msg_data.append({"scopeType": self.scope_type.get_data()})
        if self.label is not None:
            msg_data.append({"label": self.label.get_data()})
        if self.description is not None:
            msg_data.append({"description": self.description.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.sensing_type is not None:
            result_str += f"{sep}sensingType: {self.sensing_type}"
            sep = ", "
        if self.unit is not None:
            result_str += f"{sep}unit: {self.unit}"
            sep = ", "
        if self.scope_type is not None:
            result_str += f"{sep}scopeType: {self.scope_type}"
            sep = ", "
        if self.label is not None:
            result_str += f"{sep}label: {self.label}"
            sep = ", "
        if self.description is not None:
            result_str += f"{sep}description: {self.description}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                sensing_type=data_dict.get('sensingType'),
                unit=data_dict.get('unit'),
                scope_type=data_dict.get('scopeType'),
                label=data_dict.get('label'),
                description=data_dict.get('description'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class SensingDataElementsType:
    def __init__(
            self,
            timestamp: ElementTagType = None,
            state: ElementTagType = None,
            value: ScaledNumberElementsType = None,
    ):
        super().__init__()
        
        self.timestamp = timestamp
        self.state = state
        self.value = value

        if not isinstance(self.timestamp, ElementTagType | NoneType):
            raise TypeError("timestamp is not of type ElementTagType")
        
        if not isinstance(self.state, ElementTagType | NoneType):
            raise TypeError("state is not of type ElementTagType")
        
        if not isinstance(self.value, ScaledNumberElementsType | NoneType):
            raise TypeError("value is not of type ScaledNumberElementsType")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.timestamp is not None:
            msg_data.append({"timestamp": self.timestamp.get_data()})
        if self.state is not None:
            msg_data.append({"state": self.state.get_data()})
        if self.value is not None:
            msg_data.append({"value": self.value.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.timestamp is not None:
            result_str += f"{sep}timestamp: {self.timestamp}"
            sep = ", "
        if self.state is not None:
            result_str += f"{sep}state: {self.state}"
            sep = ", "
        if self.value is not None:
            result_str += f"{sep}value: {self.value}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                timestamp=data_dict.get('timestamp'),
                state=data_dict.get('state'),
                value=data_dict.get('value'),
            )
        elif data:
            return cls(data)
        else:
            return cls()



