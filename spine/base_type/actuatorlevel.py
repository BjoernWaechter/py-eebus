# Jinja Template message_type.py.jinja2
from spine.base_type.commondatatypes import ElementTagType
from spine.base_type.commondatatypes import ScaledNumberElementsType
from spine.base_type.commondatatypes import ScaledNumberType
from spine.simple_type.commondatatypes import DescriptionType
from spine.simple_type.commondatatypes import LabelType
from spine.union_type.actuatorlevel import ActuatorLevelFctType
from spine.union_type.commondatatypes import UnitOfMeasurementType
from types import NoneType
from spine import array_2_dict


class ActuatorLevelDescriptionDataType: # EEBus_SPINE_TS_ActuatorLevel.xsd: ComplexType
    def __init__(
            self,
            label: LabelType = None,
            description: DescriptionType = None,
            level_default_unit: UnitOfMeasurementType = None,
    ):
        super().__init__()
        
        self.label = label
        self.description = description
        self.level_default_unit = level_default_unit

        if not isinstance(self.label, LabelType | NoneType):
            raise TypeError("label is not of type LabelType")
        
        if not isinstance(self.description, DescriptionType | NoneType):
            raise TypeError("description is not of type DescriptionType")
        
        if not isinstance(self.level_default_unit, UnitOfMeasurementType | NoneType):
            raise TypeError("level_default_unit is not of type UnitOfMeasurementType")
        
    def get_data(self):

        msg_data = []
        
        if self.label is not None:
            msg_data.append({"label": self.label.get_data()})
        if self.description is not None:
            msg_data.append({"description": self.description.get_data()})
        if self.level_default_unit is not None:
            msg_data.append({"levelDefaultUnit": self.level_default_unit.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.label is not None:
            result_str += f"{sep}label: {self.label}"
            sep = ", "
        if self.description is not None:
            result_str += f"{sep}description: {self.description}"
            sep = ", "
        if self.level_default_unit is not None:
            result_str += f"{sep}levelDefaultUnit: {self.level_default_unit}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                label=data_dict.get('label'),
                description=data_dict.get('description'),
                level_default_unit=data_dict.get('levelDefaultUnit'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class ActuatorLevelDataType: # EEBus_SPINE_TS_ActuatorLevel.xsd: ComplexType
    def __init__(
            self,
            function: ActuatorLevelFctType = None,
            value: ScaledNumberType = None,
    ):
        super().__init__()
        
        self.function = function
        self.value = value

        if not isinstance(self.function, ActuatorLevelFctType | NoneType):
            raise TypeError("function is not of type ActuatorLevelFctType")
        
        if not isinstance(self.value, ScaledNumberType | NoneType):
            raise TypeError("value is not of type ScaledNumberType")
        
    def get_data(self):

        msg_data = []
        
        if self.function is not None:
            msg_data.append({"function": self.function.get_data()})
        if self.value is not None:
            msg_data.append({"value": self.value.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.function is not None:
            result_str += f"{sep}function: {self.function}"
            sep = ", "
        if self.value is not None:
            result_str += f"{sep}value: {self.value}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                function=data_dict.get('function'),
                value=data_dict.get('value'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class ActuatorLevelDescriptionDataElementsType: # EEBus_SPINE_TS_ActuatorLevel.xsd: ComplexType
    def __init__(
            self,
            label: ElementTagType = None,
            description: ElementTagType = None,
            level_default_unit: ElementTagType = None,
    ):
        super().__init__()
        
        self.label = label
        self.description = description
        self.level_default_unit = level_default_unit

        if not isinstance(self.label, ElementTagType | NoneType):
            raise TypeError("label is not of type ElementTagType")
        
        if not isinstance(self.description, ElementTagType | NoneType):
            raise TypeError("description is not of type ElementTagType")
        
        if not isinstance(self.level_default_unit, ElementTagType | NoneType):
            raise TypeError("level_default_unit is not of type ElementTagType")
        
    def get_data(self):

        msg_data = []
        
        if self.label is not None:
            msg_data.append({"label": self.label.get_data()})
        if self.description is not None:
            msg_data.append({"description": self.description.get_data()})
        if self.level_default_unit is not None:
            msg_data.append({"levelDefaultUnit": self.level_default_unit.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.label is not None:
            result_str += f"{sep}label: {self.label}"
            sep = ", "
        if self.description is not None:
            result_str += f"{sep}description: {self.description}"
            sep = ", "
        if self.level_default_unit is not None:
            result_str += f"{sep}levelDefaultUnit: {self.level_default_unit}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                label=data_dict.get('label'),
                description=data_dict.get('description'),
                level_default_unit=data_dict.get('levelDefaultUnit'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class ActuatorLevelDataElementsType: # EEBus_SPINE_TS_ActuatorLevel.xsd: ComplexType
    def __init__(
            self,
            function: ElementTagType = None,
            value: ScaledNumberElementsType = None,
    ):
        super().__init__()
        
        self.function = function
        self.value = value

        if not isinstance(self.function, ElementTagType | NoneType):
            raise TypeError("function is not of type ElementTagType")
        
        if not isinstance(self.value, ScaledNumberElementsType | NoneType):
            raise TypeError("value is not of type ScaledNumberElementsType")
        
    def get_data(self):

        msg_data = []
        
        if self.function is not None:
            msg_data.append({"function": self.function.get_data()})
        if self.value is not None:
            msg_data.append({"value": self.value.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.function is not None:
            result_str += f"{sep}function: {self.function}"
            sep = ", "
        if self.value is not None:
            result_str += f"{sep}value: {self.value}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                function=data_dict.get('function'),
                value=data_dict.get('value'),
            )
        elif data:
            return cls(data)
        else:
            return cls()



