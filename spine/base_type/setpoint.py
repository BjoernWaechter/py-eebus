# Jinja Template message_type.py.jinja2
from spine.simple_type.commondatatypes import LabelType
from spine.base_type.commondatatypes import TimePeriodElementsType
from spine.simple_type.setpoint import SetpointIdType
from spine.base_type.commondatatypes import ScaledNumberElementsType
from spine.simple_type.commondatatypes import DescriptionType
from spine.simple_type.timetable import TimeTableIdType
from spine.base_type.commondatatypes import ElementTagType
from spine.simple_type.measurement import MeasurementIdType
from spine.union_type.commondatatypes import FunctionType
from spine.base_type.commondatatypes import ScaledNumberType
from spine.base_type.commondatatypes import TimePeriodType
from types import NoneType
from spine import array_2_dict


class SetpointDataType:
    def __init__(
            self,
            setpoint_id: SetpointIdType = None,
            value: ScaledNumberType = None,
            value_min: ScaledNumberType = None,
            value_max: ScaledNumberType = None,
            value_tolerance_absolute: ScaledNumberType = None,
            value_tolerance_percentage: ScaledNumberType = None,
            is_setpoint_changeable: bool = None,
            is_setpoint_active: bool = None,
            time_period: TimePeriodType = None,
    ):
        super().__init__()
        
        self.setpoint_id = setpoint_id
        self.value = value
        self.value_min = value_min
        self.value_max = value_max
        self.value_tolerance_absolute = value_tolerance_absolute
        self.value_tolerance_percentage = value_tolerance_percentage
        self.is_setpoint_changeable = is_setpoint_changeable
        self.is_setpoint_active = is_setpoint_active
        self.time_period = time_period

        if not isinstance(self.setpoint_id, SetpointIdType | NoneType):
            raise TypeError("setpoint_id is not of type SetpointIdType")
        
        if not isinstance(self.value, ScaledNumberType | NoneType):
            raise TypeError("value is not of type ScaledNumberType")
        
        if not isinstance(self.value_min, ScaledNumberType | NoneType):
            raise TypeError("value_min is not of type ScaledNumberType")
        
        if not isinstance(self.value_max, ScaledNumberType | NoneType):
            raise TypeError("value_max is not of type ScaledNumberType")
        
        if not isinstance(self.value_tolerance_absolute, ScaledNumberType | NoneType):
            raise TypeError("value_tolerance_absolute is not of type ScaledNumberType")
        
        if not isinstance(self.value_tolerance_percentage, ScaledNumberType | NoneType):
            raise TypeError("value_tolerance_percentage is not of type ScaledNumberType")
        
        if not isinstance(self.is_setpoint_changeable, bool | NoneType):
            raise TypeError("is_setpoint_changeable is not of type bool")
        
        if not isinstance(self.is_setpoint_active, bool | NoneType):
            raise TypeError("is_setpoint_active is not of type bool")
        
        if not isinstance(self.time_period, TimePeriodType | NoneType):
            raise TypeError("time_period is not of type TimePeriodType")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.setpoint_id is not None:
            msg_data.append({"setpointId": self.setpoint_id.get_data()})
        if self.value is not None:
            msg_data.append({"value": self.value.get_data()})
        if self.value_min is not None:
            msg_data.append({"valueMin": self.value_min.get_data()})
        if self.value_max is not None:
            msg_data.append({"valueMax": self.value_max.get_data()})
        if self.value_tolerance_absolute is not None:
            msg_data.append({"valueToleranceAbsolute": self.value_tolerance_absolute.get_data()})
        if self.value_tolerance_percentage is not None:
            msg_data.append({"valueTolerancePercentage": self.value_tolerance_percentage.get_data()})
        if self.is_setpoint_changeable is not None:
            msg_data.append({"isSetpointChangeable": self.is_setpoint_changeable})
        if self.is_setpoint_active is not None:
            msg_data.append({"isSetpointActive": self.is_setpoint_active})
        if self.time_period is not None:
            msg_data.append({"timePeriod": self.time_period.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.setpoint_id is not None:
            result_str += f"{sep}setpointId: {self.setpoint_id}"
            sep = ", "
        if self.value is not None:
            result_str += f"{sep}value: {self.value}"
            sep = ", "
        if self.value_min is not None:
            result_str += f"{sep}valueMin: {self.value_min}"
            sep = ", "
        if self.value_max is not None:
            result_str += f"{sep}valueMax: {self.value_max}"
            sep = ", "
        if self.value_tolerance_absolute is not None:
            result_str += f"{sep}valueToleranceAbsolute: {self.value_tolerance_absolute}"
            sep = ", "
        if self.value_tolerance_percentage is not None:
            result_str += f"{sep}valueTolerancePercentage: {self.value_tolerance_percentage}"
            sep = ", "
        if self.is_setpoint_changeable is not None:
            result_str += f"{sep}isSetpointChangeable: {self.is_setpoint_changeable}"
            sep = ", "
        if self.is_setpoint_active is not None:
            result_str += f"{sep}isSetpointActive: {self.is_setpoint_active}"
            sep = ", "
        if self.time_period is not None:
            result_str += f"{sep}timePeriod: {self.time_period}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                setpoint_id=data_dict.get('setpointId'),
                value=data_dict.get('value'),
                value_min=data_dict.get('valueMin'),
                value_max=data_dict.get('valueMax'),
                value_tolerance_absolute=data_dict.get('valueToleranceAbsolute'),
                value_tolerance_percentage=data_dict.get('valueTolerancePercentage'),
                is_setpoint_changeable=data_dict.get('isSetpointChangeable'),
                is_setpoint_active=data_dict.get('isSetpointActive'),
                time_period=data_dict.get('timePeriod'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class SetpointDescriptionDataType:
    def __init__(
            self,
            setpoint_id: SetpointIdType = None,
            measurement_id: MeasurementIdType = None,
            time_table_id: TimeTableIdType = None,
            setpoint_type: FunctionType = None,
            unit: FunctionType = None,
            scope_type: FunctionType = None,
            label: LabelType = None,
            description: DescriptionType = None,
    ):
        super().__init__()
        
        self.setpoint_id = setpoint_id
        self.measurement_id = measurement_id
        self.time_table_id = time_table_id
        self.setpoint_type = setpoint_type
        self.unit = unit
        self.scope_type = scope_type
        self.label = label
        self.description = description

        if not isinstance(self.setpoint_id, SetpointIdType | NoneType):
            raise TypeError("setpoint_id is not of type SetpointIdType")
        
        if not isinstance(self.measurement_id, MeasurementIdType | NoneType):
            raise TypeError("measurement_id is not of type MeasurementIdType")
        
        if not isinstance(self.time_table_id, TimeTableIdType | NoneType):
            raise TypeError("time_table_id is not of type TimeTableIdType")
        
        if not isinstance(self.setpoint_type, FunctionType | NoneType):
            raise TypeError("setpoint_type is not of type FunctionType")
        
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
        
        if self.setpoint_id is not None:
            msg_data.append({"setpointId": self.setpoint_id.get_data()})
        if self.measurement_id is not None:
            msg_data.append({"measurementId": self.measurement_id.get_data()})
        if self.time_table_id is not None:
            msg_data.append({"timeTableId": self.time_table_id.get_data()})
        if self.setpoint_type is not None:
            msg_data.append({"setpointType": self.setpoint_type.get_data()})
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
        if self.setpoint_id is not None:
            result_str += f"{sep}setpointId: {self.setpoint_id}"
            sep = ", "
        if self.measurement_id is not None:
            result_str += f"{sep}measurementId: {self.measurement_id}"
            sep = ", "
        if self.time_table_id is not None:
            result_str += f"{sep}timeTableId: {self.time_table_id}"
            sep = ", "
        if self.setpoint_type is not None:
            result_str += f"{sep}setpointType: {self.setpoint_type}"
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
                setpoint_id=data_dict.get('setpointId'),
                measurement_id=data_dict.get('measurementId'),
                time_table_id=data_dict.get('timeTableId'),
                setpoint_type=data_dict.get('setpointType'),
                unit=data_dict.get('unit'),
                scope_type=data_dict.get('scopeType'),
                label=data_dict.get('label'),
                description=data_dict.get('description'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class SetpointConstraintsDataType:
    def __init__(
            self,
            setpoint_id: SetpointIdType = None,
            setpoint_range_min: ScaledNumberType = None,
            setpoint_range_max: ScaledNumberType = None,
            setpoint_step_size: ScaledNumberType = None,
    ):
        super().__init__()
        
        self.setpoint_id = setpoint_id
        self.setpoint_range_min = setpoint_range_min
        self.setpoint_range_max = setpoint_range_max
        self.setpoint_step_size = setpoint_step_size

        if not isinstance(self.setpoint_id, SetpointIdType | NoneType):
            raise TypeError("setpoint_id is not of type SetpointIdType")
        
        if not isinstance(self.setpoint_range_min, ScaledNumberType | NoneType):
            raise TypeError("setpoint_range_min is not of type ScaledNumberType")
        
        if not isinstance(self.setpoint_range_max, ScaledNumberType | NoneType):
            raise TypeError("setpoint_range_max is not of type ScaledNumberType")
        
        if not isinstance(self.setpoint_step_size, ScaledNumberType | NoneType):
            raise TypeError("setpoint_step_size is not of type ScaledNumberType")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.setpoint_id is not None:
            msg_data.append({"setpointId": self.setpoint_id.get_data()})
        if self.setpoint_range_min is not None:
            msg_data.append({"setpointRangeMin": self.setpoint_range_min.get_data()})
        if self.setpoint_range_max is not None:
            msg_data.append({"setpointRangeMax": self.setpoint_range_max.get_data()})
        if self.setpoint_step_size is not None:
            msg_data.append({"setpointStepSize": self.setpoint_step_size.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.setpoint_id is not None:
            result_str += f"{sep}setpointId: {self.setpoint_id}"
            sep = ", "
        if self.setpoint_range_min is not None:
            result_str += f"{sep}setpointRangeMin: {self.setpoint_range_min}"
            sep = ", "
        if self.setpoint_range_max is not None:
            result_str += f"{sep}setpointRangeMax: {self.setpoint_range_max}"
            sep = ", "
        if self.setpoint_step_size is not None:
            result_str += f"{sep}setpointStepSize: {self.setpoint_step_size}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                setpoint_id=data_dict.get('setpointId'),
                setpoint_range_min=data_dict.get('setpointRangeMin'),
                setpoint_range_max=data_dict.get('setpointRangeMax'),
                setpoint_step_size=data_dict.get('setpointStepSize'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class SetpointListDataType:
    def __init__(
            self,
            setpoint_data: list[SetpointDataType] = None,
    ):
        super().__init__()
        
        self.setpoint_data = setpoint_data

        if not isinstance(self.setpoint_data, list | NoneType):
            raise TypeError("setpoint_data is not of type list[SetpointDataType]")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.setpoint_data is not None:
            msg_data.append({"setpointData": [d.get_data() for d in self.setpoint_data]})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.setpoint_data is not None:
            result_str += f"{sep}setpointData: {self.setpoint_data}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                setpoint_data=data_dict.get('setpointData'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class SetpointListDataSelectorsType:
    def __init__(
            self,
            setpoint_id: SetpointIdType = None,
    ):
        super().__init__()
        
        self.setpoint_id = setpoint_id

        if not isinstance(self.setpoint_id, SetpointIdType | NoneType):
            raise TypeError("setpoint_id is not of type SetpointIdType")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.setpoint_id is not None:
            msg_data.append({"setpointId": self.setpoint_id.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.setpoint_id is not None:
            result_str += f"{sep}setpointId: {self.setpoint_id}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                setpoint_id=data_dict.get('setpointId'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class SetpointDescriptionListDataType:
    def __init__(
            self,
            setpoint_description_data: list[SetpointDescriptionDataType] = None,
    ):
        super().__init__()
        
        self.setpoint_description_data = setpoint_description_data

        if not isinstance(self.setpoint_description_data, list | NoneType):
            raise TypeError("setpoint_description_data is not of type list[SetpointDescriptionDataType]")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.setpoint_description_data is not None:
            msg_data.append({"setpointDescriptionData": [d.get_data() for d in self.setpoint_description_data]})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.setpoint_description_data is not None:
            result_str += f"{sep}setpointDescriptionData: {self.setpoint_description_data}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                setpoint_description_data=data_dict.get('setpointDescriptionData'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class SetpointDescriptionListDataSelectorsType:
    def __init__(
            self,
            setpoint_id: SetpointIdType = None,
            measurement_id: MeasurementIdType = None,
            time_table_id: TimeTableIdType = None,
            setpoint_type: FunctionType = None,
            scope_type: FunctionType = None,
    ):
        super().__init__()
        
        self.setpoint_id = setpoint_id
        self.measurement_id = measurement_id
        self.time_table_id = time_table_id
        self.setpoint_type = setpoint_type
        self.scope_type = scope_type

        if not isinstance(self.setpoint_id, SetpointIdType | NoneType):
            raise TypeError("setpoint_id is not of type SetpointIdType")
        
        if not isinstance(self.measurement_id, MeasurementIdType | NoneType):
            raise TypeError("measurement_id is not of type MeasurementIdType")
        
        if not isinstance(self.time_table_id, TimeTableIdType | NoneType):
            raise TypeError("time_table_id is not of type TimeTableIdType")
        
        if not isinstance(self.setpoint_type, FunctionType | NoneType):
            raise TypeError("setpoint_type is not of type FunctionType")
        
        if not isinstance(self.scope_type, FunctionType | NoneType):
            raise TypeError("scope_type is not of type FunctionType")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.setpoint_id is not None:
            msg_data.append({"setpointId": self.setpoint_id.get_data()})
        if self.measurement_id is not None:
            msg_data.append({"measurementId": self.measurement_id.get_data()})
        if self.time_table_id is not None:
            msg_data.append({"timeTableId": self.time_table_id.get_data()})
        if self.setpoint_type is not None:
            msg_data.append({"setpointType": self.setpoint_type.get_data()})
        if self.scope_type is not None:
            msg_data.append({"scopeType": self.scope_type.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.setpoint_id is not None:
            result_str += f"{sep}setpointId: {self.setpoint_id}"
            sep = ", "
        if self.measurement_id is not None:
            result_str += f"{sep}measurementId: {self.measurement_id}"
            sep = ", "
        if self.time_table_id is not None:
            result_str += f"{sep}timeTableId: {self.time_table_id}"
            sep = ", "
        if self.setpoint_type is not None:
            result_str += f"{sep}setpointType: {self.setpoint_type}"
            sep = ", "
        if self.scope_type is not None:
            result_str += f"{sep}scopeType: {self.scope_type}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                setpoint_id=data_dict.get('setpointId'),
                measurement_id=data_dict.get('measurementId'),
                time_table_id=data_dict.get('timeTableId'),
                setpoint_type=data_dict.get('setpointType'),
                scope_type=data_dict.get('scopeType'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class SetpointDescriptionDataElementsType:
    def __init__(
            self,
            setpoint_id: ElementTagType = None,
            measurement_id: ElementTagType = None,
            time_table_id: ElementTagType = None,
            setpoint_type: ElementTagType = None,
            unit: ElementTagType = None,
            scope_type: ElementTagType = None,
            label: ElementTagType = None,
            description: ElementTagType = None,
    ):
        super().__init__()
        
        self.setpoint_id = setpoint_id
        self.measurement_id = measurement_id
        self.time_table_id = time_table_id
        self.setpoint_type = setpoint_type
        self.unit = unit
        self.scope_type = scope_type
        self.label = label
        self.description = description

        if not isinstance(self.setpoint_id, ElementTagType | NoneType):
            raise TypeError("setpoint_id is not of type ElementTagType")
        
        if not isinstance(self.measurement_id, ElementTagType | NoneType):
            raise TypeError("measurement_id is not of type ElementTagType")
        
        if not isinstance(self.time_table_id, ElementTagType | NoneType):
            raise TypeError("time_table_id is not of type ElementTagType")
        
        if not isinstance(self.setpoint_type, ElementTagType | NoneType):
            raise TypeError("setpoint_type is not of type ElementTagType")
        
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
        
        if self.setpoint_id is not None:
            msg_data.append({"setpointId": self.setpoint_id.get_data()})
        if self.measurement_id is not None:
            msg_data.append({"measurementId": self.measurement_id.get_data()})
        if self.time_table_id is not None:
            msg_data.append({"timeTableId": self.time_table_id.get_data()})
        if self.setpoint_type is not None:
            msg_data.append({"setpointType": self.setpoint_type.get_data()})
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
        if self.setpoint_id is not None:
            result_str += f"{sep}setpointId: {self.setpoint_id}"
            sep = ", "
        if self.measurement_id is not None:
            result_str += f"{sep}measurementId: {self.measurement_id}"
            sep = ", "
        if self.time_table_id is not None:
            result_str += f"{sep}timeTableId: {self.time_table_id}"
            sep = ", "
        if self.setpoint_type is not None:
            result_str += f"{sep}setpointType: {self.setpoint_type}"
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
                setpoint_id=data_dict.get('setpointId'),
                measurement_id=data_dict.get('measurementId'),
                time_table_id=data_dict.get('timeTableId'),
                setpoint_type=data_dict.get('setpointType'),
                unit=data_dict.get('unit'),
                scope_type=data_dict.get('scopeType'),
                label=data_dict.get('label'),
                description=data_dict.get('description'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class SetpointDataElementsType:
    def __init__(
            self,
            setpoint_id: ElementTagType = None,
            value: ScaledNumberElementsType = None,
            value_min: ScaledNumberElementsType = None,
            value_max: ScaledNumberElementsType = None,
            value_tolerance_absolute: ScaledNumberElementsType = None,
            value_tolerance_percentage: ScaledNumberElementsType = None,
            is_setpoint_changeable: ElementTagType = None,
            is_setpoint_active: ElementTagType = None,
            time_period: TimePeriodElementsType = None,
    ):
        super().__init__()
        
        self.setpoint_id = setpoint_id
        self.value = value
        self.value_min = value_min
        self.value_max = value_max
        self.value_tolerance_absolute = value_tolerance_absolute
        self.value_tolerance_percentage = value_tolerance_percentage
        self.is_setpoint_changeable = is_setpoint_changeable
        self.is_setpoint_active = is_setpoint_active
        self.time_period = time_period

        if not isinstance(self.setpoint_id, ElementTagType | NoneType):
            raise TypeError("setpoint_id is not of type ElementTagType")
        
        if not isinstance(self.value, ScaledNumberElementsType | NoneType):
            raise TypeError("value is not of type ScaledNumberElementsType")
        
        if not isinstance(self.value_min, ScaledNumberElementsType | NoneType):
            raise TypeError("value_min is not of type ScaledNumberElementsType")
        
        if not isinstance(self.value_max, ScaledNumberElementsType | NoneType):
            raise TypeError("value_max is not of type ScaledNumberElementsType")
        
        if not isinstance(self.value_tolerance_absolute, ScaledNumberElementsType | NoneType):
            raise TypeError("value_tolerance_absolute is not of type ScaledNumberElementsType")
        
        if not isinstance(self.value_tolerance_percentage, ScaledNumberElementsType | NoneType):
            raise TypeError("value_tolerance_percentage is not of type ScaledNumberElementsType")
        
        if not isinstance(self.is_setpoint_changeable, ElementTagType | NoneType):
            raise TypeError("is_setpoint_changeable is not of type ElementTagType")
        
        if not isinstance(self.is_setpoint_active, ElementTagType | NoneType):
            raise TypeError("is_setpoint_active is not of type ElementTagType")
        
        if not isinstance(self.time_period, TimePeriodElementsType | NoneType):
            raise TypeError("time_period is not of type TimePeriodElementsType")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.setpoint_id is not None:
            msg_data.append({"setpointId": self.setpoint_id.get_data()})
        if self.value is not None:
            msg_data.append({"value": self.value.get_data()})
        if self.value_min is not None:
            msg_data.append({"valueMin": self.value_min.get_data()})
        if self.value_max is not None:
            msg_data.append({"valueMax": self.value_max.get_data()})
        if self.value_tolerance_absolute is not None:
            msg_data.append({"valueToleranceAbsolute": self.value_tolerance_absolute.get_data()})
        if self.value_tolerance_percentage is not None:
            msg_data.append({"valueTolerancePercentage": self.value_tolerance_percentage.get_data()})
        if self.is_setpoint_changeable is not None:
            msg_data.append({"isSetpointChangeable": self.is_setpoint_changeable.get_data()})
        if self.is_setpoint_active is not None:
            msg_data.append({"isSetpointActive": self.is_setpoint_active.get_data()})
        if self.time_period is not None:
            msg_data.append({"timePeriod": self.time_period.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.setpoint_id is not None:
            result_str += f"{sep}setpointId: {self.setpoint_id}"
            sep = ", "
        if self.value is not None:
            result_str += f"{sep}value: {self.value}"
            sep = ", "
        if self.value_min is not None:
            result_str += f"{sep}valueMin: {self.value_min}"
            sep = ", "
        if self.value_max is not None:
            result_str += f"{sep}valueMax: {self.value_max}"
            sep = ", "
        if self.value_tolerance_absolute is not None:
            result_str += f"{sep}valueToleranceAbsolute: {self.value_tolerance_absolute}"
            sep = ", "
        if self.value_tolerance_percentage is not None:
            result_str += f"{sep}valueTolerancePercentage: {self.value_tolerance_percentage}"
            sep = ", "
        if self.is_setpoint_changeable is not None:
            result_str += f"{sep}isSetpointChangeable: {self.is_setpoint_changeable}"
            sep = ", "
        if self.is_setpoint_active is not None:
            result_str += f"{sep}isSetpointActive: {self.is_setpoint_active}"
            sep = ", "
        if self.time_period is not None:
            result_str += f"{sep}timePeriod: {self.time_period}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                setpoint_id=data_dict.get('setpointId'),
                value=data_dict.get('value'),
                value_min=data_dict.get('valueMin'),
                value_max=data_dict.get('valueMax'),
                value_tolerance_absolute=data_dict.get('valueToleranceAbsolute'),
                value_tolerance_percentage=data_dict.get('valueTolerancePercentage'),
                is_setpoint_changeable=data_dict.get('isSetpointChangeable'),
                is_setpoint_active=data_dict.get('isSetpointActive'),
                time_period=data_dict.get('timePeriod'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class SetpointConstraintsListDataType:
    def __init__(
            self,
            setpoint_constraints_data: list[SetpointConstraintsDataType] = None,
    ):
        super().__init__()
        
        self.setpoint_constraints_data = setpoint_constraints_data

        if not isinstance(self.setpoint_constraints_data, list | NoneType):
            raise TypeError("setpoint_constraints_data is not of type list[SetpointConstraintsDataType]")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.setpoint_constraints_data is not None:
            msg_data.append({"setpointConstraintsData": [d.get_data() for d in self.setpoint_constraints_data]})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.setpoint_constraints_data is not None:
            result_str += f"{sep}setpointConstraintsData: {self.setpoint_constraints_data}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                setpoint_constraints_data=data_dict.get('setpointConstraintsData'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class SetpointConstraintsListDataSelectorsType:
    def __init__(
            self,
            setpoint_id: SetpointIdType = None,
    ):
        super().__init__()
        
        self.setpoint_id = setpoint_id

        if not isinstance(self.setpoint_id, SetpointIdType | NoneType):
            raise TypeError("setpoint_id is not of type SetpointIdType")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.setpoint_id is not None:
            msg_data.append({"setpointId": self.setpoint_id.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.setpoint_id is not None:
            result_str += f"{sep}setpointId: {self.setpoint_id}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                setpoint_id=data_dict.get('setpointId'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class SetpointConstraintsDataElementsType:
    def __init__(
            self,
            setpoint_id: ElementTagType = None,
            setpoint_range_min: ScaledNumberElementsType = None,
            setpoint_range_max: ScaledNumberElementsType = None,
            setpoint_step_size: ScaledNumberElementsType = None,
    ):
        super().__init__()
        
        self.setpoint_id = setpoint_id
        self.setpoint_range_min = setpoint_range_min
        self.setpoint_range_max = setpoint_range_max
        self.setpoint_step_size = setpoint_step_size

        if not isinstance(self.setpoint_id, ElementTagType | NoneType):
            raise TypeError("setpoint_id is not of type ElementTagType")
        
        if not isinstance(self.setpoint_range_min, ScaledNumberElementsType | NoneType):
            raise TypeError("setpoint_range_min is not of type ScaledNumberElementsType")
        
        if not isinstance(self.setpoint_range_max, ScaledNumberElementsType | NoneType):
            raise TypeError("setpoint_range_max is not of type ScaledNumberElementsType")
        
        if not isinstance(self.setpoint_step_size, ScaledNumberElementsType | NoneType):
            raise TypeError("setpoint_step_size is not of type ScaledNumberElementsType")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.setpoint_id is not None:
            msg_data.append({"setpointId": self.setpoint_id.get_data()})
        if self.setpoint_range_min is not None:
            msg_data.append({"setpointRangeMin": self.setpoint_range_min.get_data()})
        if self.setpoint_range_max is not None:
            msg_data.append({"setpointRangeMax": self.setpoint_range_max.get_data()})
        if self.setpoint_step_size is not None:
            msg_data.append({"setpointStepSize": self.setpoint_step_size.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.setpoint_id is not None:
            result_str += f"{sep}setpointId: {self.setpoint_id}"
            sep = ", "
        if self.setpoint_range_min is not None:
            result_str += f"{sep}setpointRangeMin: {self.setpoint_range_min}"
            sep = ", "
        if self.setpoint_range_max is not None:
            result_str += f"{sep}setpointRangeMax: {self.setpoint_range_max}"
            sep = ", "
        if self.setpoint_step_size is not None:
            result_str += f"{sep}setpointStepSize: {self.setpoint_step_size}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                setpoint_id=data_dict.get('setpointId'),
                setpoint_range_min=data_dict.get('setpointRangeMin'),
                setpoint_range_max=data_dict.get('setpointRangeMax'),
                setpoint_step_size=data_dict.get('setpointStepSize'),
            )
        elif data:
            return cls(data)
        else:
            return cls()



