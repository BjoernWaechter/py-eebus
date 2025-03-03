# Jinja Template message_type.py.jinja2
from spine.base_type.commondatatypes import ElementTagType
from spine.simple_type.commondatatypes import DescriptionType
from spine.simple_type.commondatatypes import LabelType
from spine.union_type.actuatorswitch import ActuatorSwitchFctType
from types import NoneType
from spine import array_2_dict


class ActuatorSwitchDescriptionDataType: # EEBus_SPINE_TS_ActuatorSwitch.xsd:ns_p:ActuatorSwitchDescriptionDataType -> ComplexType
    def __init__(
            self,
            label: LabelType = None,
            description: DescriptionType = None,
    ):
        super().__init__()
        
        self.label = label
        self.description = description

        if not isinstance(self.label, LabelType | NoneType):
            raise TypeError("label is not of type LabelType")
        
        if not isinstance(self.description, DescriptionType | NoneType):
            raise TypeError("description is not of type DescriptionType")
        
    def get_data(self):

        msg_data = []
        
        if self.label is not None:
            msg_data.append({"label": self.label.get_data()})
        if self.description is not None:
            msg_data.append({"description": self.description.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
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
                label=data_dict.get('label'),
                description=data_dict.get('description'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class ActuatorSwitchDataType: # EEBus_SPINE_TS_ActuatorSwitch.xsd:ns_p:ActuatorSwitchDataType -> ComplexType
    def __init__(
            self,
            function: ActuatorSwitchFctType = None,
    ):
        super().__init__()
        
        self.function = function

        if not isinstance(self.function, ActuatorSwitchFctType | NoneType):
            raise TypeError("function is not of type ActuatorSwitchFctType")
        
    def get_data(self):

        msg_data = []
        
        if self.function is not None:
            msg_data.append({"function": self.function.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.function is not None:
            result_str += f"{sep}function: {self.function}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                function=data_dict.get('function'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class ActuatorSwitchDescriptionDataElementsType: # EEBus_SPINE_TS_ActuatorSwitch.xsd:ns_p:ActuatorSwitchDescriptionDataElementsType -> ComplexType
    def __init__(
            self,
            label: ElementTagType = None,
            description: ElementTagType = None,
    ):
        super().__init__()
        
        self.label = label
        self.description = description

        if not isinstance(self.label, ElementTagType | NoneType):
            raise TypeError("label is not of type ElementTagType")
        
        if not isinstance(self.description, ElementTagType | NoneType):
            raise TypeError("description is not of type ElementTagType")
        
    def get_data(self):

        msg_data = []
        
        if self.label is not None:
            msg_data.append({"label": self.label.get_data()})
        if self.description is not None:
            msg_data.append({"description": self.description.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
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
                label=data_dict.get('label'),
                description=data_dict.get('description'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class ActuatorSwitchDataElementsType: # EEBus_SPINE_TS_ActuatorSwitch.xsd:ns_p:ActuatorSwitchDataElementsType -> ComplexType
    def __init__(
            self,
            function: ElementTagType = None,
    ):
        super().__init__()
        
        self.function = function

        if not isinstance(self.function, ElementTagType | NoneType):
            raise TypeError("function is not of type ElementTagType")
        
    def get_data(self):

        msg_data = []
        
        if self.function is not None:
            msg_data.append({"function": self.function.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.function is not None:
            result_str += f"{sep}function: {self.function}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                function=data_dict.get('function'),
            )
        elif data:
            return cls(data)
        else:
            return cls()



