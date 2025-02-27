# Jinja Template message_type.py.jinja2
from spine.simple_type.timeseries import TimeSeriesSlotIdType
from spine.simple_type.commondatatypes import LabelType
from spine.base_type.commondatatypes import TimePeriodElementsType
from spine.simple_type.commondatatypes import DescriptionType
from spine.base_type.commondatatypes import ScaledNumberElementsType
from spine.base_type.commondatatypes import AbsoluteOrRecurringTimeType
from spine.base_type.commondatatypes import ElementTagType
from spine.simple_type.timeseries import TimeSeriesSlotCountType
from spine.simple_type.measurement import MeasurementIdType
from spine.simple_type.timeseries import TimeSeriesIdType
from spine.union_type.commondatatypes import FunctionType
from spine.base_type.commondatatypes import ScaledNumberType
from spine.base_type.commondatatypes import AbsoluteOrRecurringTimeElementsType
from spine.base_type.commondatatypes import TimePeriodType
from types import NoneType
from spine import array_2_dict


class TimeSeriesSlotType:
    def __init__(
            self,
            time_series_slot_id: TimeSeriesSlotIdType = None,
            time_period: TimePeriodType = None,
            duration: str = None,
            recurrence_information: AbsoluteOrRecurringTimeType = None,
            value: ScaledNumberType = None,
            min_value: ScaledNumberType = None,
            max_value: ScaledNumberType = None,
    ):
        super().__init__()
        
        self.time_series_slot_id = time_series_slot_id
        self.time_period = time_period
        self.duration = duration
        self.recurrence_information = recurrence_information
        self.value = value
        self.min_value = min_value
        self.max_value = max_value

        if not isinstance(self.time_series_slot_id, TimeSeriesSlotIdType | NoneType):
            raise TypeError("time_series_slot_id is not of type TimeSeriesSlotIdType")
        
        if not isinstance(self.time_period, TimePeriodType | NoneType):
            raise TypeError("time_period is not of type TimePeriodType")
        
        if not isinstance(self.duration, str | NoneType):
            raise TypeError("duration is not of type str")
        
        if not isinstance(self.recurrence_information, AbsoluteOrRecurringTimeType | NoneType):
            raise TypeError("recurrence_information is not of type AbsoluteOrRecurringTimeType")
        
        if not isinstance(self.value, ScaledNumberType | NoneType):
            raise TypeError("value is not of type ScaledNumberType")
        
        if not isinstance(self.min_value, ScaledNumberType | NoneType):
            raise TypeError("min_value is not of type ScaledNumberType")
        
        if not isinstance(self.max_value, ScaledNumberType | NoneType):
            raise TypeError("max_value is not of type ScaledNumberType")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.time_series_slot_id is not None:
            msg_data.append({"timeSeriesSlotId": self.time_series_slot_id.get_data()})
        if self.time_period is not None:
            msg_data.append({"timePeriod": self.time_period.get_data()})
        if self.duration is not None:
            msg_data.append({"duration": self.duration})
        if self.recurrence_information is not None:
            msg_data.append({"recurrenceInformation": self.recurrence_information.get_data()})
        if self.value is not None:
            msg_data.append({"value": self.value.get_data()})
        if self.min_value is not None:
            msg_data.append({"minValue": self.min_value.get_data()})
        if self.max_value is not None:
            msg_data.append({"maxValue": self.max_value.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.time_series_slot_id is not None:
            result_str += f"{sep}timeSeriesSlotId: {self.time_series_slot_id}"
            sep = ", "
        if self.time_period is not None:
            result_str += f"{sep}timePeriod: {self.time_period}"
            sep = ", "
        if self.duration is not None:
            result_str += f"{sep}duration: {self.duration}"
            sep = ", "
        if self.recurrence_information is not None:
            result_str += f"{sep}recurrenceInformation: {self.recurrence_information}"
            sep = ", "
        if self.value is not None:
            result_str += f"{sep}value: {self.value}"
            sep = ", "
        if self.min_value is not None:
            result_str += f"{sep}minValue: {self.min_value}"
            sep = ", "
        if self.max_value is not None:
            result_str += f"{sep}maxValue: {self.max_value}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                time_series_slot_id=data_dict.get('timeSeriesSlotId'),
                time_period=data_dict.get('timePeriod'),
                duration=data_dict.get('duration'),
                recurrence_information=data_dict.get('recurrenceInformation'),
                value=data_dict.get('value'),
                min_value=data_dict.get('minValue'),
                max_value=data_dict.get('maxValue'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class TimeSeriesDataType:
    def __init__(
            self,
            time_series_id: TimeSeriesIdType = None,
            time_period: TimePeriodType = None,
            time_series_slot: list[TimeSeriesSlotType] = None,
    ):
        super().__init__()
        
        self.time_series_id = time_series_id
        self.time_period = time_period
        self.time_series_slot = time_series_slot

        if not isinstance(self.time_series_id, TimeSeriesIdType | NoneType):
            raise TypeError("time_series_id is not of type TimeSeriesIdType")
        
        if not isinstance(self.time_period, TimePeriodType | NoneType):
            raise TypeError("time_period is not of type TimePeriodType")
        
        if not isinstance(self.time_series_slot, list | NoneType):
            raise TypeError("time_series_slot is not of type list[TimeSeriesSlotType]")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.time_series_id is not None:
            msg_data.append({"timeSeriesId": self.time_series_id.get_data()})
        if self.time_period is not None:
            msg_data.append({"timePeriod": self.time_period.get_data()})
        if self.time_series_slot is not None:
            msg_data.append({"timeSeriesSlot": [d.get_data() for d in self.time_series_slot]})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.time_series_id is not None:
            result_str += f"{sep}timeSeriesId: {self.time_series_id}"
            sep = ", "
        if self.time_period is not None:
            result_str += f"{sep}timePeriod: {self.time_period}"
            sep = ", "
        if self.time_series_slot is not None:
            result_str += f"{sep}timeSeriesSlot: {self.time_series_slot}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                time_series_id=data_dict.get('timeSeriesId'),
                time_period=data_dict.get('timePeriod'),
                time_series_slot=data_dict.get('timeSeriesSlot'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class TimeSeriesDescriptionDataType:
    def __init__(
            self,
            time_series_id: TimeSeriesIdType = None,
            time_series_type: FunctionType = None,
            time_series_writeable: bool = None,
            update_required: bool = None,
            measurement_id: MeasurementIdType = None,
            currency: FunctionType = None,
            unit: FunctionType = None,
            label: LabelType = None,
            description: DescriptionType = None,
            scope_type: FunctionType = None,
    ):
        super().__init__()
        
        self.time_series_id = time_series_id
        self.time_series_type = time_series_type
        self.time_series_writeable = time_series_writeable
        self.update_required = update_required
        self.measurement_id = measurement_id
        self.currency = currency
        self.unit = unit
        self.label = label
        self.description = description
        self.scope_type = scope_type

        if not isinstance(self.time_series_id, TimeSeriesIdType | NoneType):
            raise TypeError("time_series_id is not of type TimeSeriesIdType")
        
        if not isinstance(self.time_series_type, FunctionType | NoneType):
            raise TypeError("time_series_type is not of type FunctionType")
        
        if not isinstance(self.time_series_writeable, bool | NoneType):
            raise TypeError("time_series_writeable is not of type bool")
        
        if not isinstance(self.update_required, bool | NoneType):
            raise TypeError("update_required is not of type bool")
        
        if not isinstance(self.measurement_id, MeasurementIdType | NoneType):
            raise TypeError("measurement_id is not of type MeasurementIdType")
        
        if not isinstance(self.currency, FunctionType | NoneType):
            raise TypeError("currency is not of type FunctionType")
        
        if not isinstance(self.unit, FunctionType | NoneType):
            raise TypeError("unit is not of type FunctionType")
        
        if not isinstance(self.label, LabelType | NoneType):
            raise TypeError("label is not of type LabelType")
        
        if not isinstance(self.description, DescriptionType | NoneType):
            raise TypeError("description is not of type DescriptionType")
        
        if not isinstance(self.scope_type, FunctionType | NoneType):
            raise TypeError("scope_type is not of type FunctionType")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.time_series_id is not None:
            msg_data.append({"timeSeriesId": self.time_series_id.get_data()})
        if self.time_series_type is not None:
            msg_data.append({"timeSeriesType": self.time_series_type.get_data()})
        if self.time_series_writeable is not None:
            msg_data.append({"timeSeriesWriteable": self.time_series_writeable})
        if self.update_required is not None:
            msg_data.append({"updateRequired": self.update_required})
        if self.measurement_id is not None:
            msg_data.append({"measurementId": self.measurement_id.get_data()})
        if self.currency is not None:
            msg_data.append({"currency": self.currency.get_data()})
        if self.unit is not None:
            msg_data.append({"unit": self.unit.get_data()})
        if self.label is not None:
            msg_data.append({"label": self.label.get_data()})
        if self.description is not None:
            msg_data.append({"description": self.description.get_data()})
        if self.scope_type is not None:
            msg_data.append({"scopeType": self.scope_type.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.time_series_id is not None:
            result_str += f"{sep}timeSeriesId: {self.time_series_id}"
            sep = ", "
        if self.time_series_type is not None:
            result_str += f"{sep}timeSeriesType: {self.time_series_type}"
            sep = ", "
        if self.time_series_writeable is not None:
            result_str += f"{sep}timeSeriesWriteable: {self.time_series_writeable}"
            sep = ", "
        if self.update_required is not None:
            result_str += f"{sep}updateRequired: {self.update_required}"
            sep = ", "
        if self.measurement_id is not None:
            result_str += f"{sep}measurementId: {self.measurement_id}"
            sep = ", "
        if self.currency is not None:
            result_str += f"{sep}currency: {self.currency}"
            sep = ", "
        if self.unit is not None:
            result_str += f"{sep}unit: {self.unit}"
            sep = ", "
        if self.label is not None:
            result_str += f"{sep}label: {self.label}"
            sep = ", "
        if self.description is not None:
            result_str += f"{sep}description: {self.description}"
            sep = ", "
        if self.scope_type is not None:
            result_str += f"{sep}scopeType: {self.scope_type}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                time_series_id=data_dict.get('timeSeriesId'),
                time_series_type=data_dict.get('timeSeriesType'),
                time_series_writeable=data_dict.get('timeSeriesWriteable'),
                update_required=data_dict.get('updateRequired'),
                measurement_id=data_dict.get('measurementId'),
                currency=data_dict.get('currency'),
                unit=data_dict.get('unit'),
                label=data_dict.get('label'),
                description=data_dict.get('description'),
                scope_type=data_dict.get('scopeType'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class TimeSeriesSlotElementsType:
    def __init__(
            self,
            time_series_slot_id: ElementTagType = None,
            time_period: TimePeriodElementsType = None,
            duration: ElementTagType = None,
            recurrence_information: AbsoluteOrRecurringTimeElementsType = None,
            value: ElementTagType = None,
            min_value: ElementTagType = None,
            max_value: ElementTagType = None,
    ):
        super().__init__()
        
        self.time_series_slot_id = time_series_slot_id
        self.time_period = time_period
        self.duration = duration
        self.recurrence_information = recurrence_information
        self.value = value
        self.min_value = min_value
        self.max_value = max_value

        if not isinstance(self.time_series_slot_id, ElementTagType | NoneType):
            raise TypeError("time_series_slot_id is not of type ElementTagType")
        
        if not isinstance(self.time_period, TimePeriodElementsType | NoneType):
            raise TypeError("time_period is not of type TimePeriodElementsType")
        
        if not isinstance(self.duration, ElementTagType | NoneType):
            raise TypeError("duration is not of type ElementTagType")
        
        if not isinstance(self.recurrence_information, AbsoluteOrRecurringTimeElementsType | NoneType):
            raise TypeError("recurrence_information is not of type AbsoluteOrRecurringTimeElementsType")
        
        if not isinstance(self.value, ElementTagType | NoneType):
            raise TypeError("value is not of type ElementTagType")
        
        if not isinstance(self.min_value, ElementTagType | NoneType):
            raise TypeError("min_value is not of type ElementTagType")
        
        if not isinstance(self.max_value, ElementTagType | NoneType):
            raise TypeError("max_value is not of type ElementTagType")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.time_series_slot_id is not None:
            msg_data.append({"timeSeriesSlotId": self.time_series_slot_id.get_data()})
        if self.time_period is not None:
            msg_data.append({"timePeriod": self.time_period.get_data()})
        if self.duration is not None:
            msg_data.append({"duration": self.duration.get_data()})
        if self.recurrence_information is not None:
            msg_data.append({"recurrenceInformation": self.recurrence_information.get_data()})
        if self.value is not None:
            msg_data.append({"value": self.value.get_data()})
        if self.min_value is not None:
            msg_data.append({"minValue": self.min_value.get_data()})
        if self.max_value is not None:
            msg_data.append({"maxValue": self.max_value.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.time_series_slot_id is not None:
            result_str += f"{sep}timeSeriesSlotId: {self.time_series_slot_id}"
            sep = ", "
        if self.time_period is not None:
            result_str += f"{sep}timePeriod: {self.time_period}"
            sep = ", "
        if self.duration is not None:
            result_str += f"{sep}duration: {self.duration}"
            sep = ", "
        if self.recurrence_information is not None:
            result_str += f"{sep}recurrenceInformation: {self.recurrence_information}"
            sep = ", "
        if self.value is not None:
            result_str += f"{sep}value: {self.value}"
            sep = ", "
        if self.min_value is not None:
            result_str += f"{sep}minValue: {self.min_value}"
            sep = ", "
        if self.max_value is not None:
            result_str += f"{sep}maxValue: {self.max_value}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                time_series_slot_id=data_dict.get('timeSeriesSlotId'),
                time_period=data_dict.get('timePeriod'),
                duration=data_dict.get('duration'),
                recurrence_information=data_dict.get('recurrenceInformation'),
                value=data_dict.get('value'),
                min_value=data_dict.get('minValue'),
                max_value=data_dict.get('maxValue'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class TimeSeriesConstraintsDataType:
    def __init__(
            self,
            time_series_id: TimeSeriesIdType = None,
            slot_count_min: TimeSeriesSlotCountType = None,
            slot_count_max: TimeSeriesSlotCountType = None,
            slot_duration_min: str = None,
            slot_duration_max: str = None,
            slot_duration_step_size: str = None,
            earliest_time_series_start_time: FunctionType = None,
            latest_time_series_end_time: FunctionType = None,
            slot_value_min: ScaledNumberType = None,
            slot_value_max: ScaledNumberType = None,
            slot_value_step_size: ScaledNumberType = None,
    ):
        super().__init__()
        
        self.time_series_id = time_series_id
        self.slot_count_min = slot_count_min
        self.slot_count_max = slot_count_max
        self.slot_duration_min = slot_duration_min
        self.slot_duration_max = slot_duration_max
        self.slot_duration_step_size = slot_duration_step_size
        self.earliest_time_series_start_time = earliest_time_series_start_time
        self.latest_time_series_end_time = latest_time_series_end_time
        self.slot_value_min = slot_value_min
        self.slot_value_max = slot_value_max
        self.slot_value_step_size = slot_value_step_size

        if not isinstance(self.time_series_id, TimeSeriesIdType | NoneType):
            raise TypeError("time_series_id is not of type TimeSeriesIdType")
        
        if not isinstance(self.slot_count_min, TimeSeriesSlotCountType | NoneType):
            raise TypeError("slot_count_min is not of type TimeSeriesSlotCountType")
        
        if not isinstance(self.slot_count_max, TimeSeriesSlotCountType | NoneType):
            raise TypeError("slot_count_max is not of type TimeSeriesSlotCountType")
        
        if not isinstance(self.slot_duration_min, str | NoneType):
            raise TypeError("slot_duration_min is not of type str")
        
        if not isinstance(self.slot_duration_max, str | NoneType):
            raise TypeError("slot_duration_max is not of type str")
        
        if not isinstance(self.slot_duration_step_size, str | NoneType):
            raise TypeError("slot_duration_step_size is not of type str")
        
        if not isinstance(self.earliest_time_series_start_time, FunctionType | NoneType):
            raise TypeError("earliest_time_series_start_time is not of type FunctionType")
        
        if not isinstance(self.latest_time_series_end_time, FunctionType | NoneType):
            raise TypeError("latest_time_series_end_time is not of type FunctionType")
        
        if not isinstance(self.slot_value_min, ScaledNumberType | NoneType):
            raise TypeError("slot_value_min is not of type ScaledNumberType")
        
        if not isinstance(self.slot_value_max, ScaledNumberType | NoneType):
            raise TypeError("slot_value_max is not of type ScaledNumberType")
        
        if not isinstance(self.slot_value_step_size, ScaledNumberType | NoneType):
            raise TypeError("slot_value_step_size is not of type ScaledNumberType")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.time_series_id is not None:
            msg_data.append({"timeSeriesId": self.time_series_id.get_data()})
        if self.slot_count_min is not None:
            msg_data.append({"slotCountMin": self.slot_count_min.get_data()})
        if self.slot_count_max is not None:
            msg_data.append({"slotCountMax": self.slot_count_max.get_data()})
        if self.slot_duration_min is not None:
            msg_data.append({"slotDurationMin": self.slot_duration_min})
        if self.slot_duration_max is not None:
            msg_data.append({"slotDurationMax": self.slot_duration_max})
        if self.slot_duration_step_size is not None:
            msg_data.append({"slotDurationStepSize": self.slot_duration_step_size})
        if self.earliest_time_series_start_time is not None:
            msg_data.append({"earliestTimeSeriesStartTime": self.earliest_time_series_start_time.get_data()})
        if self.latest_time_series_end_time is not None:
            msg_data.append({"latestTimeSeriesEndTime": self.latest_time_series_end_time.get_data()})
        if self.slot_value_min is not None:
            msg_data.append({"slotValueMin": self.slot_value_min.get_data()})
        if self.slot_value_max is not None:
            msg_data.append({"slotValueMax": self.slot_value_max.get_data()})
        if self.slot_value_step_size is not None:
            msg_data.append({"slotValueStepSize": self.slot_value_step_size.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.time_series_id is not None:
            result_str += f"{sep}timeSeriesId: {self.time_series_id}"
            sep = ", "
        if self.slot_count_min is not None:
            result_str += f"{sep}slotCountMin: {self.slot_count_min}"
            sep = ", "
        if self.slot_count_max is not None:
            result_str += f"{sep}slotCountMax: {self.slot_count_max}"
            sep = ", "
        if self.slot_duration_min is not None:
            result_str += f"{sep}slotDurationMin: {self.slot_duration_min}"
            sep = ", "
        if self.slot_duration_max is not None:
            result_str += f"{sep}slotDurationMax: {self.slot_duration_max}"
            sep = ", "
        if self.slot_duration_step_size is not None:
            result_str += f"{sep}slotDurationStepSize: {self.slot_duration_step_size}"
            sep = ", "
        if self.earliest_time_series_start_time is not None:
            result_str += f"{sep}earliestTimeSeriesStartTime: {self.earliest_time_series_start_time}"
            sep = ", "
        if self.latest_time_series_end_time is not None:
            result_str += f"{sep}latestTimeSeriesEndTime: {self.latest_time_series_end_time}"
            sep = ", "
        if self.slot_value_min is not None:
            result_str += f"{sep}slotValueMin: {self.slot_value_min}"
            sep = ", "
        if self.slot_value_max is not None:
            result_str += f"{sep}slotValueMax: {self.slot_value_max}"
            sep = ", "
        if self.slot_value_step_size is not None:
            result_str += f"{sep}slotValueStepSize: {self.slot_value_step_size}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                time_series_id=data_dict.get('timeSeriesId'),
                slot_count_min=data_dict.get('slotCountMin'),
                slot_count_max=data_dict.get('slotCountMax'),
                slot_duration_min=data_dict.get('slotDurationMin'),
                slot_duration_max=data_dict.get('slotDurationMax'),
                slot_duration_step_size=data_dict.get('slotDurationStepSize'),
                earliest_time_series_start_time=data_dict.get('earliestTimeSeriesStartTime'),
                latest_time_series_end_time=data_dict.get('latestTimeSeriesEndTime'),
                slot_value_min=data_dict.get('slotValueMin'),
                slot_value_max=data_dict.get('slotValueMax'),
                slot_value_step_size=data_dict.get('slotValueStepSize'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class TimeSeriesListDataType:
    def __init__(
            self,
            time_series_data: list[TimeSeriesDataType] = None,
    ):
        super().__init__()
        
        self.time_series_data = time_series_data

        if not isinstance(self.time_series_data, list | NoneType):
            raise TypeError("time_series_data is not of type list[TimeSeriesDataType]")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.time_series_data is not None:
            msg_data.append({"timeSeriesData": [d.get_data() for d in self.time_series_data]})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.time_series_data is not None:
            result_str += f"{sep}timeSeriesData: {self.time_series_data}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                time_series_data=data_dict.get('timeSeriesData'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class TimeSeriesListDataSelectorsType:
    def __init__(
            self,
            time_series_id: TimeSeriesIdType = None,
            time_series_slot_id: TimeSeriesSlotIdType = None,
    ):
        super().__init__()
        
        self.time_series_id = time_series_id
        self.time_series_slot_id = time_series_slot_id

        if not isinstance(self.time_series_id, TimeSeriesIdType | NoneType):
            raise TypeError("time_series_id is not of type TimeSeriesIdType")
        
        if not isinstance(self.time_series_slot_id, TimeSeriesSlotIdType | NoneType):
            raise TypeError("time_series_slot_id is not of type TimeSeriesSlotIdType")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.time_series_id is not None:
            msg_data.append({"timeSeriesId": self.time_series_id.get_data()})
        if self.time_series_slot_id is not None:
            msg_data.append({"timeSeriesSlotId": self.time_series_slot_id.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.time_series_id is not None:
            result_str += f"{sep}timeSeriesId: {self.time_series_id}"
            sep = ", "
        if self.time_series_slot_id is not None:
            result_str += f"{sep}timeSeriesSlotId: {self.time_series_slot_id}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                time_series_id=data_dict.get('timeSeriesId'),
                time_series_slot_id=data_dict.get('timeSeriesSlotId'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class TimeSeriesDescriptionListDataType:
    def __init__(
            self,
            time_series_description_data: list[TimeSeriesDescriptionDataType] = None,
    ):
        super().__init__()
        
        self.time_series_description_data = time_series_description_data

        if not isinstance(self.time_series_description_data, list | NoneType):
            raise TypeError("time_series_description_data is not of type list[TimeSeriesDescriptionDataType]")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.time_series_description_data is not None:
            msg_data.append({"timeSeriesDescriptionData": [d.get_data() for d in self.time_series_description_data]})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.time_series_description_data is not None:
            result_str += f"{sep}timeSeriesDescriptionData: {self.time_series_description_data}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                time_series_description_data=data_dict.get('timeSeriesDescriptionData'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class TimeSeriesDescriptionListDataSelectorsType:
    def __init__(
            self,
            time_series_id: TimeSeriesIdType = None,
            time_series_type: FunctionType = None,
            measurement_id: MeasurementIdType = None,
            scope_type: FunctionType = None,
    ):
        super().__init__()
        
        self.time_series_id = time_series_id
        self.time_series_type = time_series_type
        self.measurement_id = measurement_id
        self.scope_type = scope_type

        if not isinstance(self.time_series_id, TimeSeriesIdType | NoneType):
            raise TypeError("time_series_id is not of type TimeSeriesIdType")
        
        if not isinstance(self.time_series_type, FunctionType | NoneType):
            raise TypeError("time_series_type is not of type FunctionType")
        
        if not isinstance(self.measurement_id, MeasurementIdType | NoneType):
            raise TypeError("measurement_id is not of type MeasurementIdType")
        
        if not isinstance(self.scope_type, FunctionType | NoneType):
            raise TypeError("scope_type is not of type FunctionType")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.time_series_id is not None:
            msg_data.append({"timeSeriesId": self.time_series_id.get_data()})
        if self.time_series_type is not None:
            msg_data.append({"timeSeriesType": self.time_series_type.get_data()})
        if self.measurement_id is not None:
            msg_data.append({"measurementId": self.measurement_id.get_data()})
        if self.scope_type is not None:
            msg_data.append({"scopeType": self.scope_type.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.time_series_id is not None:
            result_str += f"{sep}timeSeriesId: {self.time_series_id}"
            sep = ", "
        if self.time_series_type is not None:
            result_str += f"{sep}timeSeriesType: {self.time_series_type}"
            sep = ", "
        if self.measurement_id is not None:
            result_str += f"{sep}measurementId: {self.measurement_id}"
            sep = ", "
        if self.scope_type is not None:
            result_str += f"{sep}scopeType: {self.scope_type}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                time_series_id=data_dict.get('timeSeriesId'),
                time_series_type=data_dict.get('timeSeriesType'),
                measurement_id=data_dict.get('measurementId'),
                scope_type=data_dict.get('scopeType'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class TimeSeriesDescriptionDataElementsType:
    def __init__(
            self,
            time_series_id: ElementTagType = None,
            time_series_type: ElementTagType = None,
            time_series_writeable: ElementTagType = None,
            update_required: ElementTagType = None,
            measurement_id: ElementTagType = None,
            currency: ElementTagType = None,
            unit: ElementTagType = None,
            label: ElementTagType = None,
            description: ElementTagType = None,
            scope_type: ElementTagType = None,
    ):
        super().__init__()
        
        self.time_series_id = time_series_id
        self.time_series_type = time_series_type
        self.time_series_writeable = time_series_writeable
        self.update_required = update_required
        self.measurement_id = measurement_id
        self.currency = currency
        self.unit = unit
        self.label = label
        self.description = description
        self.scope_type = scope_type

        if not isinstance(self.time_series_id, ElementTagType | NoneType):
            raise TypeError("time_series_id is not of type ElementTagType")
        
        if not isinstance(self.time_series_type, ElementTagType | NoneType):
            raise TypeError("time_series_type is not of type ElementTagType")
        
        if not isinstance(self.time_series_writeable, ElementTagType | NoneType):
            raise TypeError("time_series_writeable is not of type ElementTagType")
        
        if not isinstance(self.update_required, ElementTagType | NoneType):
            raise TypeError("update_required is not of type ElementTagType")
        
        if not isinstance(self.measurement_id, ElementTagType | NoneType):
            raise TypeError("measurement_id is not of type ElementTagType")
        
        if not isinstance(self.currency, ElementTagType | NoneType):
            raise TypeError("currency is not of type ElementTagType")
        
        if not isinstance(self.unit, ElementTagType | NoneType):
            raise TypeError("unit is not of type ElementTagType")
        
        if not isinstance(self.label, ElementTagType | NoneType):
            raise TypeError("label is not of type ElementTagType")
        
        if not isinstance(self.description, ElementTagType | NoneType):
            raise TypeError("description is not of type ElementTagType")
        
        if not isinstance(self.scope_type, ElementTagType | NoneType):
            raise TypeError("scope_type is not of type ElementTagType")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.time_series_id is not None:
            msg_data.append({"timeSeriesId": self.time_series_id.get_data()})
        if self.time_series_type is not None:
            msg_data.append({"timeSeriesType": self.time_series_type.get_data()})
        if self.time_series_writeable is not None:
            msg_data.append({"timeSeriesWriteable": self.time_series_writeable.get_data()})
        if self.update_required is not None:
            msg_data.append({"updateRequired": self.update_required.get_data()})
        if self.measurement_id is not None:
            msg_data.append({"measurementId": self.measurement_id.get_data()})
        if self.currency is not None:
            msg_data.append({"currency": self.currency.get_data()})
        if self.unit is not None:
            msg_data.append({"unit": self.unit.get_data()})
        if self.label is not None:
            msg_data.append({"label": self.label.get_data()})
        if self.description is not None:
            msg_data.append({"description": self.description.get_data()})
        if self.scope_type is not None:
            msg_data.append({"scopeType": self.scope_type.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.time_series_id is not None:
            result_str += f"{sep}timeSeriesId: {self.time_series_id}"
            sep = ", "
        if self.time_series_type is not None:
            result_str += f"{sep}timeSeriesType: {self.time_series_type}"
            sep = ", "
        if self.time_series_writeable is not None:
            result_str += f"{sep}timeSeriesWriteable: {self.time_series_writeable}"
            sep = ", "
        if self.update_required is not None:
            result_str += f"{sep}updateRequired: {self.update_required}"
            sep = ", "
        if self.measurement_id is not None:
            result_str += f"{sep}measurementId: {self.measurement_id}"
            sep = ", "
        if self.currency is not None:
            result_str += f"{sep}currency: {self.currency}"
            sep = ", "
        if self.unit is not None:
            result_str += f"{sep}unit: {self.unit}"
            sep = ", "
        if self.label is not None:
            result_str += f"{sep}label: {self.label}"
            sep = ", "
        if self.description is not None:
            result_str += f"{sep}description: {self.description}"
            sep = ", "
        if self.scope_type is not None:
            result_str += f"{sep}scopeType: {self.scope_type}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                time_series_id=data_dict.get('timeSeriesId'),
                time_series_type=data_dict.get('timeSeriesType'),
                time_series_writeable=data_dict.get('timeSeriesWriteable'),
                update_required=data_dict.get('updateRequired'),
                measurement_id=data_dict.get('measurementId'),
                currency=data_dict.get('currency'),
                unit=data_dict.get('unit'),
                label=data_dict.get('label'),
                description=data_dict.get('description'),
                scope_type=data_dict.get('scopeType'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class TimeSeriesDataElementsType:
    def __init__(
            self,
            time_series_id: ElementTagType = None,
            time_period: TimePeriodElementsType = None,
            time_series_slot: TimeSeriesSlotElementsType = None,
    ):
        super().__init__()
        
        self.time_series_id = time_series_id
        self.time_period = time_period
        self.time_series_slot = time_series_slot

        if not isinstance(self.time_series_id, ElementTagType | NoneType):
            raise TypeError("time_series_id is not of type ElementTagType")
        
        if not isinstance(self.time_period, TimePeriodElementsType | NoneType):
            raise TypeError("time_period is not of type TimePeriodElementsType")
        
        if not isinstance(self.time_series_slot, TimeSeriesSlotElementsType | NoneType):
            raise TypeError("time_series_slot is not of type TimeSeriesSlotElementsType")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.time_series_id is not None:
            msg_data.append({"timeSeriesId": self.time_series_id.get_data()})
        if self.time_period is not None:
            msg_data.append({"timePeriod": self.time_period.get_data()})
        if self.time_series_slot is not None:
            msg_data.append({"timeSeriesSlot": self.time_series_slot.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.time_series_id is not None:
            result_str += f"{sep}timeSeriesId: {self.time_series_id}"
            sep = ", "
        if self.time_period is not None:
            result_str += f"{sep}timePeriod: {self.time_period}"
            sep = ", "
        if self.time_series_slot is not None:
            result_str += f"{sep}timeSeriesSlot: {self.time_series_slot}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                time_series_id=data_dict.get('timeSeriesId'),
                time_period=data_dict.get('timePeriod'),
                time_series_slot=data_dict.get('timeSeriesSlot'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class TimeSeriesConstraintsListDataType:
    def __init__(
            self,
            time_series_constraints_data: list[TimeSeriesConstraintsDataType] = None,
    ):
        super().__init__()
        
        self.time_series_constraints_data = time_series_constraints_data

        if not isinstance(self.time_series_constraints_data, list | NoneType):
            raise TypeError("time_series_constraints_data is not of type list[TimeSeriesConstraintsDataType]")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.time_series_constraints_data is not None:
            msg_data.append({"timeSeriesConstraintsData": [d.get_data() for d in self.time_series_constraints_data]})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.time_series_constraints_data is not None:
            result_str += f"{sep}timeSeriesConstraintsData: {self.time_series_constraints_data}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                time_series_constraints_data=data_dict.get('timeSeriesConstraintsData'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class TimeSeriesConstraintsListDataSelectorsType:
    def __init__(
            self,
            time_series_id: TimeSeriesIdType = None,
    ):
        super().__init__()
        
        self.time_series_id = time_series_id

        if not isinstance(self.time_series_id, TimeSeriesIdType | NoneType):
            raise TypeError("time_series_id is not of type TimeSeriesIdType")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.time_series_id is not None:
            msg_data.append({"timeSeriesId": self.time_series_id.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.time_series_id is not None:
            result_str += f"{sep}timeSeriesId: {self.time_series_id}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                time_series_id=data_dict.get('timeSeriesId'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class TimeSeriesConstraintsDataElementsType:
    def __init__(
            self,
            time_series_id: ElementTagType = None,
            slot_count_min: ElementTagType = None,
            slot_count_max: ElementTagType = None,
            slot_duration_min: ElementTagType = None,
            slot_duration_max: ElementTagType = None,
            slot_duration_step_size: ElementTagType = None,
            earliest_time_series_start_time: ElementTagType = None,
            latest_time_series_end_time: ElementTagType = None,
            slot_value_min: ScaledNumberElementsType = None,
            slot_value_max: ScaledNumberElementsType = None,
            slot_value_step_size: ScaledNumberElementsType = None,
    ):
        super().__init__()
        
        self.time_series_id = time_series_id
        self.slot_count_min = slot_count_min
        self.slot_count_max = slot_count_max
        self.slot_duration_min = slot_duration_min
        self.slot_duration_max = slot_duration_max
        self.slot_duration_step_size = slot_duration_step_size
        self.earliest_time_series_start_time = earliest_time_series_start_time
        self.latest_time_series_end_time = latest_time_series_end_time
        self.slot_value_min = slot_value_min
        self.slot_value_max = slot_value_max
        self.slot_value_step_size = slot_value_step_size

        if not isinstance(self.time_series_id, ElementTagType | NoneType):
            raise TypeError("time_series_id is not of type ElementTagType")
        
        if not isinstance(self.slot_count_min, ElementTagType | NoneType):
            raise TypeError("slot_count_min is not of type ElementTagType")
        
        if not isinstance(self.slot_count_max, ElementTagType | NoneType):
            raise TypeError("slot_count_max is not of type ElementTagType")
        
        if not isinstance(self.slot_duration_min, ElementTagType | NoneType):
            raise TypeError("slot_duration_min is not of type ElementTagType")
        
        if not isinstance(self.slot_duration_max, ElementTagType | NoneType):
            raise TypeError("slot_duration_max is not of type ElementTagType")
        
        if not isinstance(self.slot_duration_step_size, ElementTagType | NoneType):
            raise TypeError("slot_duration_step_size is not of type ElementTagType")
        
        if not isinstance(self.earliest_time_series_start_time, ElementTagType | NoneType):
            raise TypeError("earliest_time_series_start_time is not of type ElementTagType")
        
        if not isinstance(self.latest_time_series_end_time, ElementTagType | NoneType):
            raise TypeError("latest_time_series_end_time is not of type ElementTagType")
        
        if not isinstance(self.slot_value_min, ScaledNumberElementsType | NoneType):
            raise TypeError("slot_value_min is not of type ScaledNumberElementsType")
        
        if not isinstance(self.slot_value_max, ScaledNumberElementsType | NoneType):
            raise TypeError("slot_value_max is not of type ScaledNumberElementsType")
        
        if not isinstance(self.slot_value_step_size, ScaledNumberElementsType | NoneType):
            raise TypeError("slot_value_step_size is not of type ScaledNumberElementsType")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.time_series_id is not None:
            msg_data.append({"timeSeriesId": self.time_series_id.get_data()})
        if self.slot_count_min is not None:
            msg_data.append({"slotCountMin": self.slot_count_min.get_data()})
        if self.slot_count_max is not None:
            msg_data.append({"slotCountMax": self.slot_count_max.get_data()})
        if self.slot_duration_min is not None:
            msg_data.append({"slotDurationMin": self.slot_duration_min.get_data()})
        if self.slot_duration_max is not None:
            msg_data.append({"slotDurationMax": self.slot_duration_max.get_data()})
        if self.slot_duration_step_size is not None:
            msg_data.append({"slotDurationStepSize": self.slot_duration_step_size.get_data()})
        if self.earliest_time_series_start_time is not None:
            msg_data.append({"earliestTimeSeriesStartTime": self.earliest_time_series_start_time.get_data()})
        if self.latest_time_series_end_time is not None:
            msg_data.append({"latestTimeSeriesEndTime": self.latest_time_series_end_time.get_data()})
        if self.slot_value_min is not None:
            msg_data.append({"slotValueMin": self.slot_value_min.get_data()})
        if self.slot_value_max is not None:
            msg_data.append({"slotValueMax": self.slot_value_max.get_data()})
        if self.slot_value_step_size is not None:
            msg_data.append({"slotValueStepSize": self.slot_value_step_size.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.time_series_id is not None:
            result_str += f"{sep}timeSeriesId: {self.time_series_id}"
            sep = ", "
        if self.slot_count_min is not None:
            result_str += f"{sep}slotCountMin: {self.slot_count_min}"
            sep = ", "
        if self.slot_count_max is not None:
            result_str += f"{sep}slotCountMax: {self.slot_count_max}"
            sep = ", "
        if self.slot_duration_min is not None:
            result_str += f"{sep}slotDurationMin: {self.slot_duration_min}"
            sep = ", "
        if self.slot_duration_max is not None:
            result_str += f"{sep}slotDurationMax: {self.slot_duration_max}"
            sep = ", "
        if self.slot_duration_step_size is not None:
            result_str += f"{sep}slotDurationStepSize: {self.slot_duration_step_size}"
            sep = ", "
        if self.earliest_time_series_start_time is not None:
            result_str += f"{sep}earliestTimeSeriesStartTime: {self.earliest_time_series_start_time}"
            sep = ", "
        if self.latest_time_series_end_time is not None:
            result_str += f"{sep}latestTimeSeriesEndTime: {self.latest_time_series_end_time}"
            sep = ", "
        if self.slot_value_min is not None:
            result_str += f"{sep}slotValueMin: {self.slot_value_min}"
            sep = ", "
        if self.slot_value_max is not None:
            result_str += f"{sep}slotValueMax: {self.slot_value_max}"
            sep = ", "
        if self.slot_value_step_size is not None:
            result_str += f"{sep}slotValueStepSize: {self.slot_value_step_size}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                time_series_id=data_dict.get('timeSeriesId'),
                slot_count_min=data_dict.get('slotCountMin'),
                slot_count_max=data_dict.get('slotCountMax'),
                slot_duration_min=data_dict.get('slotDurationMin'),
                slot_duration_max=data_dict.get('slotDurationMax'),
                slot_duration_step_size=data_dict.get('slotDurationStepSize'),
                earliest_time_series_start_time=data_dict.get('earliestTimeSeriesStartTime'),
                latest_time_series_end_time=data_dict.get('latestTimeSeriesEndTime'),
                slot_value_min=data_dict.get('slotValueMin'),
                slot_value_max=data_dict.get('slotValueMax'),
                slot_value_step_size=data_dict.get('slotValueStepSize'),
            )
        elif data:
            return cls(data)
        else:
            return cls()



