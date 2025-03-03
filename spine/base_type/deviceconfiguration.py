# Jinja Template message_type.py.jinja2
from spine.base_type.commondatatypes import ElementTagType
from spine.base_type.commondatatypes import ScaledNumberElementsType
from spine.base_type.commondatatypes import ScaledNumberType
from spine.enums.deviceconfiguration import DeviceConfigurationKeyValueTypeType
from spine.simple_type.commondatatypes import DescriptionType
from spine.simple_type.commondatatypes import LabelType
from spine.simple_type.deviceconfiguration import DeviceConfigurationKeyIdType
from spine.simple_type.deviceconfiguration import DeviceConfigurationKeyValueStringType
from spine.union_type.commondatatypes import UnitOfMeasurementType
from spine.union_type.deviceconfiguration import DeviceConfigurationKeyNameType
from types import NoneType
from spine import array_2_dict


class DeviceConfigurationKeyValueValueType: # EEBus_SPINE_TS_DeviceConfiguration.xsd:ns_p:DeviceConfigurationKeyValueValueType -> ComplexType
    def __init__(
            self,
            boolean: bool = None,
            date: str = None,
            date_time: str = None,
            duration: str = None,
            string: DeviceConfigurationKeyValueStringType = None,
            time: str = None,
            scaled_number: ScaledNumberType = None,
            integer: int = None,
    ):
        super().__init__()
        
        self.boolean = boolean
        self.date = date
        self.date_time = date_time
        self.duration = duration
        self.string = string
        self.time = time
        self.scaled_number = scaled_number
        self.integer = integer

        if not isinstance(self.boolean, bool | NoneType):
            raise TypeError("boolean is not of type bool")
        
        if not isinstance(self.date, str | NoneType):
            raise TypeError("date is not of type str")
        
        if not isinstance(self.date_time, str | NoneType):
            raise TypeError("date_time is not of type str")
        
        if not isinstance(self.duration, str | NoneType):
            raise TypeError("duration is not of type str")
        
        if not isinstance(self.string, DeviceConfigurationKeyValueStringType | NoneType):
            raise TypeError("string is not of type DeviceConfigurationKeyValueStringType")
        
        if not isinstance(self.time, str | NoneType):
            raise TypeError("time is not of type str")
        
        if not isinstance(self.scaled_number, ScaledNumberType | NoneType):
            raise TypeError("scaled_number is not of type ScaledNumberType")
        
        if not isinstance(self.integer, int | NoneType):
            raise TypeError("integer is not of type int")
        
    def get_data(self):

        msg_data = []
        
        if self.boolean is not None:
            msg_data.append({"boolean": self.boolean})
        if self.date is not None:
            msg_data.append({"date": self.date})
        if self.date_time is not None:
            msg_data.append({"dateTime": self.date_time})
        if self.duration is not None:
            msg_data.append({"duration": self.duration})
        if self.string is not None:
            msg_data.append({"string": self.string.get_data()})
        if self.time is not None:
            msg_data.append({"time": self.time})
        if self.scaled_number is not None:
            msg_data.append({"scaledNumber": self.scaled_number.get_data()})
        if self.integer is not None:
            msg_data.append({"integer": self.integer})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.boolean is not None:
            result_str += f"{sep}boolean: {self.boolean}"
            sep = ", "
        if self.date is not None:
            result_str += f"{sep}date: {self.date}"
            sep = ", "
        if self.date_time is not None:
            result_str += f"{sep}dateTime: {self.date_time}"
            sep = ", "
        if self.duration is not None:
            result_str += f"{sep}duration: {self.duration}"
            sep = ", "
        if self.string is not None:
            result_str += f"{sep}string: {self.string}"
            sep = ", "
        if self.time is not None:
            result_str += f"{sep}time: {self.time}"
            sep = ", "
        if self.scaled_number is not None:
            result_str += f"{sep}scaledNumber: {self.scaled_number}"
            sep = ", "
        if self.integer is not None:
            result_str += f"{sep}integer: {self.integer}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                boolean=data_dict.get('boolean'),
                date=data_dict.get('date'),
                date_time=data_dict.get('dateTime'),
                duration=data_dict.get('duration'),
                string=data_dict.get('string'),
                time=data_dict.get('time'),
                scaled_number=data_dict.get('scaledNumber'),
                integer=data_dict.get('integer'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class DeviceConfigurationKeyValueDataType: # EEBus_SPINE_TS_DeviceConfiguration.xsd:ns_p:DeviceConfigurationKeyValueDataType -> ComplexType
    def __init__(
            self,
            key_id: DeviceConfigurationKeyIdType = None,
            value: DeviceConfigurationKeyValueValueType = None,
            is_value_changeable: bool = None,
    ):
        super().__init__()
        
        self.key_id = key_id
        self.value = value
        self.is_value_changeable = is_value_changeable

        if not isinstance(self.key_id, DeviceConfigurationKeyIdType | NoneType):
            raise TypeError("key_id is not of type DeviceConfigurationKeyIdType")
        
        if not isinstance(self.value, DeviceConfigurationKeyValueValueType | NoneType):
            raise TypeError("value is not of type DeviceConfigurationKeyValueValueType")
        
        if not isinstance(self.is_value_changeable, bool | NoneType):
            raise TypeError("is_value_changeable is not of type bool")
        
    def get_data(self):

        msg_data = []
        
        if self.key_id is not None:
            msg_data.append({"keyId": self.key_id.get_data()})
        if self.value is not None:
            msg_data.append({"value": self.value.get_data()})
        if self.is_value_changeable is not None:
            msg_data.append({"isValueChangeable": self.is_value_changeable})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.key_id is not None:
            result_str += f"{sep}keyId: {self.key_id}"
            sep = ", "
        if self.value is not None:
            result_str += f"{sep}value: {self.value}"
            sep = ", "
        if self.is_value_changeable is not None:
            result_str += f"{sep}isValueChangeable: {self.is_value_changeable}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                key_id=data_dict.get('keyId'),
                value=data_dict.get('value'),
                is_value_changeable=data_dict.get('isValueChangeable'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class DeviceConfigurationKeyValueDescriptionDataType: # EEBus_SPINE_TS_DeviceConfiguration.xsd:ns_p:DeviceConfigurationKeyValueDescriptionDataType -> ComplexType
    def __init__(
            self,
            key_id: DeviceConfigurationKeyIdType = None,
            key_name: DeviceConfigurationKeyNameType = None,
            value_type: DeviceConfigurationKeyValueTypeType = None,
            unit: UnitOfMeasurementType = None,
            label: LabelType = None,
            description: DescriptionType = None,
    ):
        super().__init__()
        
        self.key_id = key_id
        self.key_name = key_name
        self.value_type = value_type
        self.unit = unit
        self.label = label
        self.description = description

        if not isinstance(self.key_id, DeviceConfigurationKeyIdType | NoneType):
            raise TypeError("key_id is not of type DeviceConfigurationKeyIdType")
        
        if not isinstance(self.key_name, DeviceConfigurationKeyNameType | NoneType):
            raise TypeError("key_name is not of type DeviceConfigurationKeyNameType")
        
        if not isinstance(self.value_type, DeviceConfigurationKeyValueTypeType | NoneType):
            raise TypeError("value_type is not of type DeviceConfigurationKeyValueTypeType")
        
        if not isinstance(self.unit, UnitOfMeasurementType | NoneType):
            raise TypeError("unit is not of type UnitOfMeasurementType")
        
        if not isinstance(self.label, LabelType | NoneType):
            raise TypeError("label is not of type LabelType")
        
        if not isinstance(self.description, DescriptionType | NoneType):
            raise TypeError("description is not of type DescriptionType")
        
    def get_data(self):

        msg_data = []
        
        if self.key_id is not None:
            msg_data.append({"keyId": self.key_id.get_data()})
        if self.key_name is not None:
            msg_data.append({"keyName": self.key_name.get_data()})
        if self.value_type is not None:
            msg_data.append({"valueType": self.value_type.value})
        if self.unit is not None:
            msg_data.append({"unit": self.unit.get_data()})
        if self.label is not None:
            msg_data.append({"label": self.label.get_data()})
        if self.description is not None:
            msg_data.append({"description": self.description.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.key_id is not None:
            result_str += f"{sep}keyId: {self.key_id}"
            sep = ", "
        if self.key_name is not None:
            result_str += f"{sep}keyName: {self.key_name}"
            sep = ", "
        if self.value_type is not None:
            result_str += f"{sep}valueType: {self.value_type}"
            sep = ", "
        if self.unit is not None:
            result_str += f"{sep}unit: {self.unit}"
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
                key_id=data_dict.get('keyId'),
                key_name=data_dict.get('keyName'),
                value_type=data_dict.get('valueType'),
                unit=data_dict.get('unit'),
                label=data_dict.get('label'),
                description=data_dict.get('description'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class DeviceConfigurationKeyValueConstraintsDataType: # EEBus_SPINE_TS_DeviceConfiguration.xsd:ns_p:DeviceConfigurationKeyValueConstraintsDataType -> ComplexType
    def __init__(
            self,
            key_id: DeviceConfigurationKeyIdType = None,
            value_range_min: DeviceConfigurationKeyValueValueType = None,
            value_range_max: DeviceConfigurationKeyValueValueType = None,
            value_step_size: DeviceConfigurationKeyValueValueType = None,
    ):
        super().__init__()
        
        self.key_id = key_id
        self.value_range_min = value_range_min
        self.value_range_max = value_range_max
        self.value_step_size = value_step_size

        if not isinstance(self.key_id, DeviceConfigurationKeyIdType | NoneType):
            raise TypeError("key_id is not of type DeviceConfigurationKeyIdType")
        
        if not isinstance(self.value_range_min, DeviceConfigurationKeyValueValueType | NoneType):
            raise TypeError("value_range_min is not of type DeviceConfigurationKeyValueValueType")
        
        if not isinstance(self.value_range_max, DeviceConfigurationKeyValueValueType | NoneType):
            raise TypeError("value_range_max is not of type DeviceConfigurationKeyValueValueType")
        
        if not isinstance(self.value_step_size, DeviceConfigurationKeyValueValueType | NoneType):
            raise TypeError("value_step_size is not of type DeviceConfigurationKeyValueValueType")
        
    def get_data(self):

        msg_data = []
        
        if self.key_id is not None:
            msg_data.append({"keyId": self.key_id.get_data()})
        if self.value_range_min is not None:
            msg_data.append({"valueRangeMin": self.value_range_min.get_data()})
        if self.value_range_max is not None:
            msg_data.append({"valueRangeMax": self.value_range_max.get_data()})
        if self.value_step_size is not None:
            msg_data.append({"valueStepSize": self.value_step_size.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.key_id is not None:
            result_str += f"{sep}keyId: {self.key_id}"
            sep = ", "
        if self.value_range_min is not None:
            result_str += f"{sep}valueRangeMin: {self.value_range_min}"
            sep = ", "
        if self.value_range_max is not None:
            result_str += f"{sep}valueRangeMax: {self.value_range_max}"
            sep = ", "
        if self.value_step_size is not None:
            result_str += f"{sep}valueStepSize: {self.value_step_size}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                key_id=data_dict.get('keyId'),
                value_range_min=data_dict.get('valueRangeMin'),
                value_range_max=data_dict.get('valueRangeMax'),
                value_step_size=data_dict.get('valueStepSize'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class DeviceConfigurationKeyValueValueElementsType: # EEBus_SPINE_TS_DeviceConfiguration.xsd:ns_p:DeviceConfigurationKeyValueValueElementsType -> ComplexType
    def __init__(
            self,
            boolean: ElementTagType = None,
            date: ElementTagType = None,
            date_time: ElementTagType = None,
            duration: ElementTagType = None,
            string: ElementTagType = None,
            time: ElementTagType = None,
            scaled_number: ScaledNumberElementsType = None,
    ):
        super().__init__()
        
        self.boolean = boolean
        self.date = date
        self.date_time = date_time
        self.duration = duration
        self.string = string
        self.time = time
        self.scaled_number = scaled_number

        if not isinstance(self.boolean, ElementTagType | NoneType):
            raise TypeError("boolean is not of type ElementTagType")
        
        if not isinstance(self.date, ElementTagType | NoneType):
            raise TypeError("date is not of type ElementTagType")
        
        if not isinstance(self.date_time, ElementTagType | NoneType):
            raise TypeError("date_time is not of type ElementTagType")
        
        if not isinstance(self.duration, ElementTagType | NoneType):
            raise TypeError("duration is not of type ElementTagType")
        
        if not isinstance(self.string, ElementTagType | NoneType):
            raise TypeError("string is not of type ElementTagType")
        
        if not isinstance(self.time, ElementTagType | NoneType):
            raise TypeError("time is not of type ElementTagType")
        
        if not isinstance(self.scaled_number, ScaledNumberElementsType | NoneType):
            raise TypeError("scaled_number is not of type ScaledNumberElementsType")
        
    def get_data(self):

        msg_data = []
        
        if self.boolean is not None:
            msg_data.append({"boolean": self.boolean.get_data()})
        if self.date is not None:
            msg_data.append({"date": self.date.get_data()})
        if self.date_time is not None:
            msg_data.append({"dateTime": self.date_time.get_data()})
        if self.duration is not None:
            msg_data.append({"duration": self.duration.get_data()})
        if self.string is not None:
            msg_data.append({"string": self.string.get_data()})
        if self.time is not None:
            msg_data.append({"time": self.time.get_data()})
        if self.scaled_number is not None:
            msg_data.append({"scaledNumber": self.scaled_number.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.boolean is not None:
            result_str += f"{sep}boolean: {self.boolean}"
            sep = ", "
        if self.date is not None:
            result_str += f"{sep}date: {self.date}"
            sep = ", "
        if self.date_time is not None:
            result_str += f"{sep}dateTime: {self.date_time}"
            sep = ", "
        if self.duration is not None:
            result_str += f"{sep}duration: {self.duration}"
            sep = ", "
        if self.string is not None:
            result_str += f"{sep}string: {self.string}"
            sep = ", "
        if self.time is not None:
            result_str += f"{sep}time: {self.time}"
            sep = ", "
        if self.scaled_number is not None:
            result_str += f"{sep}scaledNumber: {self.scaled_number}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                boolean=data_dict.get('boolean'),
                date=data_dict.get('date'),
                date_time=data_dict.get('dateTime'),
                duration=data_dict.get('duration'),
                string=data_dict.get('string'),
                time=data_dict.get('time'),
                scaled_number=data_dict.get('scaledNumber'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class DeviceConfigurationKeyValueListDataType: # EEBus_SPINE_TS_DeviceConfiguration.xsd:ns_p:DeviceConfigurationKeyValueListDataType -> ComplexType
    def __init__(
            self,
            device_configuration_key_value_data: list[DeviceConfigurationKeyValueDataType] = None,
    ):
        super().__init__()
        
        self.device_configuration_key_value_data = device_configuration_key_value_data

        if not isinstance(self.device_configuration_key_value_data, list | NoneType):
            raise TypeError("device_configuration_key_value_data is not of type list[DeviceConfigurationKeyValueDataType]")
        
    def get_data(self):

        msg_data = []
        
        if self.device_configuration_key_value_data is not None:
            msg_data.append({"deviceConfigurationKeyValueData": [d.get_data() for d in self.device_configuration_key_value_data]})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.device_configuration_key_value_data is not None:
            result_str += f"{sep}deviceConfigurationKeyValueData: {self.device_configuration_key_value_data}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                device_configuration_key_value_data=data_dict.get('deviceConfigurationKeyValueData'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class DeviceConfigurationKeyValueDescriptionListDataType: # EEBus_SPINE_TS_DeviceConfiguration.xsd:ns_p:DeviceConfigurationKeyValueDescriptionListDataType -> ComplexType
    def __init__(
            self,
            device_configuration_key_value_description_data: list[DeviceConfigurationKeyValueDescriptionDataType] = None,
    ):
        super().__init__()
        
        self.device_configuration_key_value_description_data = device_configuration_key_value_description_data

        if not isinstance(self.device_configuration_key_value_description_data, list | NoneType):
            raise TypeError("device_configuration_key_value_description_data is not of type list[DeviceConfigurationKeyValueDescriptionDataType]")
        
    def get_data(self):

        msg_data = []
        
        if self.device_configuration_key_value_description_data is not None:
            msg_data.append({"deviceConfigurationKeyValueDescriptionData": [d.get_data() for d in self.device_configuration_key_value_description_data]})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.device_configuration_key_value_description_data is not None:
            result_str += f"{sep}deviceConfigurationKeyValueDescriptionData: {self.device_configuration_key_value_description_data}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                device_configuration_key_value_description_data=data_dict.get('deviceConfigurationKeyValueDescriptionData'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class DeviceConfigurationKeyValueConstraintsListDataType: # EEBus_SPINE_TS_DeviceConfiguration.xsd:ns_p:DeviceConfigurationKeyValueConstraintsListDataType -> ComplexType
    def __init__(
            self,
            device_configuration_key_value_constraints_data: list[DeviceConfigurationKeyValueConstraintsDataType] = None,
    ):
        super().__init__()
        
        self.device_configuration_key_value_constraints_data = device_configuration_key_value_constraints_data

        if not isinstance(self.device_configuration_key_value_constraints_data, list | NoneType):
            raise TypeError("device_configuration_key_value_constraints_data is not of type list[DeviceConfigurationKeyValueConstraintsDataType]")
        
    def get_data(self):

        msg_data = []
        
        if self.device_configuration_key_value_constraints_data is not None:
            msg_data.append({"deviceConfigurationKeyValueConstraintsData": [d.get_data() for d in self.device_configuration_key_value_constraints_data]})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.device_configuration_key_value_constraints_data is not None:
            result_str += f"{sep}deviceConfigurationKeyValueConstraintsData: {self.device_configuration_key_value_constraints_data}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                device_configuration_key_value_constraints_data=data_dict.get('deviceConfigurationKeyValueConstraintsData'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class DeviceConfigurationKeyValueDescriptionDataElementsType: # EEBus_SPINE_TS_DeviceConfiguration.xsd:ns_p:DeviceConfigurationKeyValueDescriptionDataElementsType -> ComplexType
    def __init__(
            self,
            key_id: ElementTagType = None,
            key_name: ElementTagType = None,
            value_type: ElementTagType = None,
            unit: ElementTagType = None,
            label: ElementTagType = None,
            description: ElementTagType = None,
    ):
        super().__init__()
        
        self.key_id = key_id
        self.key_name = key_name
        self.value_type = value_type
        self.unit = unit
        self.label = label
        self.description = description

        if not isinstance(self.key_id, ElementTagType | NoneType):
            raise TypeError("key_id is not of type ElementTagType")
        
        if not isinstance(self.key_name, ElementTagType | NoneType):
            raise TypeError("key_name is not of type ElementTagType")
        
        if not isinstance(self.value_type, ElementTagType | NoneType):
            raise TypeError("value_type is not of type ElementTagType")
        
        if not isinstance(self.unit, ElementTagType | NoneType):
            raise TypeError("unit is not of type ElementTagType")
        
        if not isinstance(self.label, ElementTagType | NoneType):
            raise TypeError("label is not of type ElementTagType")
        
        if not isinstance(self.description, ElementTagType | NoneType):
            raise TypeError("description is not of type ElementTagType")
        
    def get_data(self):

        msg_data = []
        
        if self.key_id is not None:
            msg_data.append({"keyId": self.key_id.get_data()})
        if self.key_name is not None:
            msg_data.append({"keyName": self.key_name.get_data()})
        if self.value_type is not None:
            msg_data.append({"valueType": self.value_type.get_data()})
        if self.unit is not None:
            msg_data.append({"unit": self.unit.get_data()})
        if self.label is not None:
            msg_data.append({"label": self.label.get_data()})
        if self.description is not None:
            msg_data.append({"description": self.description.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.key_id is not None:
            result_str += f"{sep}keyId: {self.key_id}"
            sep = ", "
        if self.key_name is not None:
            result_str += f"{sep}keyName: {self.key_name}"
            sep = ", "
        if self.value_type is not None:
            result_str += f"{sep}valueType: {self.value_type}"
            sep = ", "
        if self.unit is not None:
            result_str += f"{sep}unit: {self.unit}"
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
                key_id=data_dict.get('keyId'),
                key_name=data_dict.get('keyName'),
                value_type=data_dict.get('valueType'),
                unit=data_dict.get('unit'),
                label=data_dict.get('label'),
                description=data_dict.get('description'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class DeviceConfigurationKeyValueDataElementsType: # EEBus_SPINE_TS_DeviceConfiguration.xsd:ns_p:DeviceConfigurationKeyValueDataElementsType -> ComplexType
    def __init__(
            self,
            key_id: ElementTagType = None,
            value: DeviceConfigurationKeyValueValueElementsType = None,
            is_value_changeable: ElementTagType = None,
    ):
        super().__init__()
        
        self.key_id = key_id
        self.value = value
        self.is_value_changeable = is_value_changeable

        if not isinstance(self.key_id, ElementTagType | NoneType):
            raise TypeError("key_id is not of type ElementTagType")
        
        if not isinstance(self.value, DeviceConfigurationKeyValueValueElementsType | NoneType):
            raise TypeError("value is not of type DeviceConfigurationKeyValueValueElementsType")
        
        if not isinstance(self.is_value_changeable, ElementTagType | NoneType):
            raise TypeError("is_value_changeable is not of type ElementTagType")
        
    def get_data(self):

        msg_data = []
        
        if self.key_id is not None:
            msg_data.append({"keyId": self.key_id.get_data()})
        if self.value is not None:
            msg_data.append({"value": self.value.get_data()})
        if self.is_value_changeable is not None:
            msg_data.append({"isValueChangeable": self.is_value_changeable.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.key_id is not None:
            result_str += f"{sep}keyId: {self.key_id}"
            sep = ", "
        if self.value is not None:
            result_str += f"{sep}value: {self.value}"
            sep = ", "
        if self.is_value_changeable is not None:
            result_str += f"{sep}isValueChangeable: {self.is_value_changeable}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                key_id=data_dict.get('keyId'),
                value=data_dict.get('value'),
                is_value_changeable=data_dict.get('isValueChangeable'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class DeviceConfigurationKeyValueConstraintsDataElementsType: # EEBus_SPINE_TS_DeviceConfiguration.xsd:ns_p:DeviceConfigurationKeyValueConstraintsDataElementsType -> ComplexType
    def __init__(
            self,
            key_id: ElementTagType = None,
            value_range_min: DeviceConfigurationKeyValueValueElementsType = None,
            value_range_max: DeviceConfigurationKeyValueValueElementsType = None,
            value_step_size: DeviceConfigurationKeyValueValueElementsType = None,
    ):
        super().__init__()
        
        self.key_id = key_id
        self.value_range_min = value_range_min
        self.value_range_max = value_range_max
        self.value_step_size = value_step_size

        if not isinstance(self.key_id, ElementTagType | NoneType):
            raise TypeError("key_id is not of type ElementTagType")
        
        if not isinstance(self.value_range_min, DeviceConfigurationKeyValueValueElementsType | NoneType):
            raise TypeError("value_range_min is not of type DeviceConfigurationKeyValueValueElementsType")
        
        if not isinstance(self.value_range_max, DeviceConfigurationKeyValueValueElementsType | NoneType):
            raise TypeError("value_range_max is not of type DeviceConfigurationKeyValueValueElementsType")
        
        if not isinstance(self.value_step_size, DeviceConfigurationKeyValueValueElementsType | NoneType):
            raise TypeError("value_step_size is not of type DeviceConfigurationKeyValueValueElementsType")
        
    def get_data(self):

        msg_data = []
        
        if self.key_id is not None:
            msg_data.append({"keyId": self.key_id.get_data()})
        if self.value_range_min is not None:
            msg_data.append({"valueRangeMin": self.value_range_min.get_data()})
        if self.value_range_max is not None:
            msg_data.append({"valueRangeMax": self.value_range_max.get_data()})
        if self.value_step_size is not None:
            msg_data.append({"valueStepSize": self.value_step_size.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.key_id is not None:
            result_str += f"{sep}keyId: {self.key_id}"
            sep = ", "
        if self.value_range_min is not None:
            result_str += f"{sep}valueRangeMin: {self.value_range_min}"
            sep = ", "
        if self.value_range_max is not None:
            result_str += f"{sep}valueRangeMax: {self.value_range_max}"
            sep = ", "
        if self.value_step_size is not None:
            result_str += f"{sep}valueStepSize: {self.value_step_size}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                key_id=data_dict.get('keyId'),
                value_range_min=data_dict.get('valueRangeMin'),
                value_range_max=data_dict.get('valueRangeMax'),
                value_step_size=data_dict.get('valueStepSize'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class DeviceConfigurationKeyValueListDataSelectorsType: # EEBus_SPINE_TS_DeviceConfiguration.xsd:ns_p:DeviceConfigurationKeyValueListDataSelectorsType -> ComplexType
    def __init__(
            self,
            key_id: DeviceConfigurationKeyIdType = None,
    ):
        super().__init__()
        
        self.key_id = key_id

        if not isinstance(self.key_id, DeviceConfigurationKeyIdType | NoneType):
            raise TypeError("key_id is not of type DeviceConfigurationKeyIdType")
        
    def get_data(self):

        msg_data = []
        
        if self.key_id is not None:
            msg_data.append({"keyId": self.key_id.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.key_id is not None:
            result_str += f"{sep}keyId: {self.key_id}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                key_id=data_dict.get('keyId'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class DeviceConfigurationKeyValueDescriptionListDataSelectorsType: # EEBus_SPINE_TS_DeviceConfiguration.xsd:ns_p:DeviceConfigurationKeyValueDescriptionListDataSelectorsType -> ComplexType
    def __init__(
            self,
            key_id: DeviceConfigurationKeyIdType = None,
            key_name: DeviceConfigurationKeyNameType = None,
    ):
        super().__init__()
        
        self.key_id = key_id
        self.key_name = key_name

        if not isinstance(self.key_id, DeviceConfigurationKeyIdType | NoneType):
            raise TypeError("key_id is not of type DeviceConfigurationKeyIdType")
        
        if not isinstance(self.key_name, DeviceConfigurationKeyNameType | NoneType):
            raise TypeError("key_name is not of type DeviceConfigurationKeyNameType")
        
    def get_data(self):

        msg_data = []
        
        if self.key_id is not None:
            msg_data.append({"keyId": self.key_id.get_data()})
        if self.key_name is not None:
            msg_data.append({"keyName": self.key_name.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.key_id is not None:
            result_str += f"{sep}keyId: {self.key_id}"
            sep = ", "
        if self.key_name is not None:
            result_str += f"{sep}keyName: {self.key_name}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                key_id=data_dict.get('keyId'),
                key_name=data_dict.get('keyName'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class DeviceConfigurationKeyValueConstraintsListDataSelectorsType: # EEBus_SPINE_TS_DeviceConfiguration.xsd:ns_p:DeviceConfigurationKeyValueConstraintsListDataSelectorsType -> ComplexType
    def __init__(
            self,
            key_id: DeviceConfigurationKeyIdType = None,
    ):
        super().__init__()
        
        self.key_id = key_id

        if not isinstance(self.key_id, DeviceConfigurationKeyIdType | NoneType):
            raise TypeError("key_id is not of type DeviceConfigurationKeyIdType")
        
    def get_data(self):

        msg_data = []
        
        if self.key_id is not None:
            msg_data.append({"keyId": self.key_id.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.key_id is not None:
            result_str += f"{sep}keyId: {self.key_id}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                key_id=data_dict.get('keyId'),
            )
        elif data:
            return cls(data)
        else:
            return cls()



