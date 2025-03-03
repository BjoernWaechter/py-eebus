# Jinja Template message_type.py.jinja2
from spine.base_type.commondatatypes import AbsoluteOrRecurringTimeElementsType
from spine.base_type.commondatatypes import AbsoluteOrRecurringTimeType
from spine.base_type.commondatatypes import ElementTagType
from spine.base_type.commondatatypes import RecurrenceInformationElementsType
from spine.base_type.commondatatypes import RecurrenceInformationType
from spine.simple_type.commondatatypes import DescriptionType
from spine.simple_type.commondatatypes import LabelType
from spine.simple_type.timetable import TimeSlotCountType
from spine.simple_type.timetable import TimeSlotIdType
from spine.simple_type.timetable import TimeTableIdType
from spine.union_type.timetable import TimeSlotTimeModeType
from types import NoneType
from spine import array_2_dict


class TimeTableDataType: # EEBus_SPINE_TS_TimeTable.xsd:ns_p:TimeTableDataType -> ComplexType
    def __init__(
            self,
            time_table_id: TimeTableIdType = None,
            time_slot_id: TimeSlotIdType = None,
            recurrence_information: RecurrenceInformationType = None,
            start_time: AbsoluteOrRecurringTimeType = None,
            end_time: AbsoluteOrRecurringTimeType = None,
    ):
        super().__init__()
        
        self.time_table_id = time_table_id
        self.time_slot_id = time_slot_id
        self.recurrence_information = recurrence_information
        self.start_time = start_time
        self.end_time = end_time

        if not isinstance(self.time_table_id, TimeTableIdType | NoneType):
            raise TypeError("time_table_id is not of type TimeTableIdType")
        
        if not isinstance(self.time_slot_id, TimeSlotIdType | NoneType):
            raise TypeError("time_slot_id is not of type TimeSlotIdType")
        
        if not isinstance(self.recurrence_information, RecurrenceInformationType | NoneType):
            raise TypeError("recurrence_information is not of type RecurrenceInformationType")
        
        if not isinstance(self.start_time, AbsoluteOrRecurringTimeType | NoneType):
            raise TypeError("start_time is not of type AbsoluteOrRecurringTimeType")
        
        if not isinstance(self.end_time, AbsoluteOrRecurringTimeType | NoneType):
            raise TypeError("end_time is not of type AbsoluteOrRecurringTimeType")
        
    def get_data(self):

        msg_data = []
        
        if self.time_table_id is not None:
            msg_data.append({"timeTableId": self.time_table_id.get_data()})
        if self.time_slot_id is not None:
            msg_data.append({"timeSlotId": self.time_slot_id.get_data()})
        if self.recurrence_information is not None:
            msg_data.append({"recurrenceInformation": self.recurrence_information.get_data()})
        if self.start_time is not None:
            msg_data.append({"startTime": self.start_time.get_data()})
        if self.end_time is not None:
            msg_data.append({"endTime": self.end_time.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.time_table_id is not None:
            result_str += f"{sep}timeTableId: {self.time_table_id}"
            sep = ", "
        if self.time_slot_id is not None:
            result_str += f"{sep}timeSlotId: {self.time_slot_id}"
            sep = ", "
        if self.recurrence_information is not None:
            result_str += f"{sep}recurrenceInformation: {self.recurrence_information}"
            sep = ", "
        if self.start_time is not None:
            result_str += f"{sep}startTime: {self.start_time}"
            sep = ", "
        if self.end_time is not None:
            result_str += f"{sep}endTime: {self.end_time}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                time_table_id=data_dict.get('timeTableId'),
                time_slot_id=data_dict.get('timeSlotId'),
                recurrence_information=data_dict.get('recurrenceInformation'),
                start_time=data_dict.get('startTime'),
                end_time=data_dict.get('endTime'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class TimeTableDescriptionDataType: # EEBus_SPINE_TS_TimeTable.xsd:ns_p:TimeTableDescriptionDataType -> ComplexType
    def __init__(
            self,
            time_table_id: int = None,
            time_slot_count_changeable: bool = None,
            time_slot_times_changeable: bool = None,
            time_slot_time_mode: TimeSlotTimeModeType = None,
            label: LabelType = None,
            description: DescriptionType = None,
    ):
        super().__init__()
        
        self.time_table_id = time_table_id
        self.time_slot_count_changeable = time_slot_count_changeable
        self.time_slot_times_changeable = time_slot_times_changeable
        self.time_slot_time_mode = time_slot_time_mode
        self.label = label
        self.description = description

        if not isinstance(self.time_table_id, int | NoneType):
            raise TypeError("time_table_id is not of type int")
        
        if not isinstance(self.time_slot_count_changeable, bool | NoneType):
            raise TypeError("time_slot_count_changeable is not of type bool")
        
        if not isinstance(self.time_slot_times_changeable, bool | NoneType):
            raise TypeError("time_slot_times_changeable is not of type bool")
        
        if not isinstance(self.time_slot_time_mode, TimeSlotTimeModeType | NoneType):
            raise TypeError("time_slot_time_mode is not of type TimeSlotTimeModeType")
        
        if not isinstance(self.label, LabelType | NoneType):
            raise TypeError("label is not of type LabelType")
        
        if not isinstance(self.description, DescriptionType | NoneType):
            raise TypeError("description is not of type DescriptionType")
        
    def get_data(self):

        msg_data = []
        
        if self.time_table_id is not None:
            msg_data.append({"timeTableId": self.time_table_id})
        if self.time_slot_count_changeable is not None:
            msg_data.append({"timeSlotCountChangeable": self.time_slot_count_changeable})
        if self.time_slot_times_changeable is not None:
            msg_data.append({"timeSlotTimesChangeable": self.time_slot_times_changeable})
        if self.time_slot_time_mode is not None:
            msg_data.append({"timeSlotTimeMode": self.time_slot_time_mode.get_data()})
        if self.label is not None:
            msg_data.append({"label": self.label.get_data()})
        if self.description is not None:
            msg_data.append({"description": self.description.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.time_table_id is not None:
            result_str += f"{sep}timeTableId: {self.time_table_id}"
            sep = ", "
        if self.time_slot_count_changeable is not None:
            result_str += f"{sep}timeSlotCountChangeable: {self.time_slot_count_changeable}"
            sep = ", "
        if self.time_slot_times_changeable is not None:
            result_str += f"{sep}timeSlotTimesChangeable: {self.time_slot_times_changeable}"
            sep = ", "
        if self.time_slot_time_mode is not None:
            result_str += f"{sep}timeSlotTimeMode: {self.time_slot_time_mode}"
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
                time_table_id=data_dict.get('timeTableId'),
                time_slot_count_changeable=data_dict.get('timeSlotCountChangeable'),
                time_slot_times_changeable=data_dict.get('timeSlotTimesChangeable'),
                time_slot_time_mode=data_dict.get('timeSlotTimeMode'),
                label=data_dict.get('label'),
                description=data_dict.get('description'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class TimeTableConstraintsDataType: # EEBus_SPINE_TS_TimeTable.xsd:ns_p:TimeTableConstraintsDataType -> ComplexType
    def __init__(
            self,
            time_table_id: int = None,
            slot_count_min: TimeSlotCountType = None,
            slot_count_max: TimeSlotCountType = None,
            slot_duration_min: str = None,
            slot_duration_max: str = None,
            slot_duration_step_size: str = None,
            slot_shift_step_size: str = None,
            first_slot_begins_at: str = None,
    ):
        super().__init__()
        
        self.time_table_id = time_table_id
        self.slot_count_min = slot_count_min
        self.slot_count_max = slot_count_max
        self.slot_duration_min = slot_duration_min
        self.slot_duration_max = slot_duration_max
        self.slot_duration_step_size = slot_duration_step_size
        self.slot_shift_step_size = slot_shift_step_size
        self.first_slot_begins_at = first_slot_begins_at

        if not isinstance(self.time_table_id, int | NoneType):
            raise TypeError("time_table_id is not of type int")
        
        if not isinstance(self.slot_count_min, TimeSlotCountType | NoneType):
            raise TypeError("slot_count_min is not of type TimeSlotCountType")
        
        if not isinstance(self.slot_count_max, TimeSlotCountType | NoneType):
            raise TypeError("slot_count_max is not of type TimeSlotCountType")
        
        if not isinstance(self.slot_duration_min, str | NoneType):
            raise TypeError("slot_duration_min is not of type str")
        
        if not isinstance(self.slot_duration_max, str | NoneType):
            raise TypeError("slot_duration_max is not of type str")
        
        if not isinstance(self.slot_duration_step_size, str | NoneType):
            raise TypeError("slot_duration_step_size is not of type str")
        
        if not isinstance(self.slot_shift_step_size, str | NoneType):
            raise TypeError("slot_shift_step_size is not of type str")
        
        if not isinstance(self.first_slot_begins_at, str | NoneType):
            raise TypeError("first_slot_begins_at is not of type str")
        
    def get_data(self):

        msg_data = []
        
        if self.time_table_id is not None:
            msg_data.append({"timeTableId": self.time_table_id})
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
        if self.slot_shift_step_size is not None:
            msg_data.append({"slotShiftStepSize": self.slot_shift_step_size})
        if self.first_slot_begins_at is not None:
            msg_data.append({"firstSlotBeginsAt": self.first_slot_begins_at})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.time_table_id is not None:
            result_str += f"{sep}timeTableId: {self.time_table_id}"
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
        if self.slot_shift_step_size is not None:
            result_str += f"{sep}slotShiftStepSize: {self.slot_shift_step_size}"
            sep = ", "
        if self.first_slot_begins_at is not None:
            result_str += f"{sep}firstSlotBeginsAt: {self.first_slot_begins_at}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                time_table_id=data_dict.get('timeTableId'),
                slot_count_min=data_dict.get('slotCountMin'),
                slot_count_max=data_dict.get('slotCountMax'),
                slot_duration_min=data_dict.get('slotDurationMin'),
                slot_duration_max=data_dict.get('slotDurationMax'),
                slot_duration_step_size=data_dict.get('slotDurationStepSize'),
                slot_shift_step_size=data_dict.get('slotShiftStepSize'),
                first_slot_begins_at=data_dict.get('firstSlotBeginsAt'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class TimeTableListDataType: # EEBus_SPINE_TS_TimeTable.xsd:ns_p:TimeTableListDataType -> ComplexType
    def __init__(
            self,
            time_table_data: list[TimeTableDataType] = None,
    ):
        super().__init__()
        
        self.time_table_data = time_table_data

        if not isinstance(self.time_table_data, list | NoneType):
            raise TypeError("time_table_data is not of type list[TimeTableDataType]")
        
    def get_data(self):

        msg_data = []
        
        if self.time_table_data is not None:
            msg_data.append({"timeTableData": [d.get_data() for d in self.time_table_data]})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.time_table_data is not None:
            result_str += f"{sep}timeTableData: {self.time_table_data}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                time_table_data=data_dict.get('timeTableData'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class TimeTableDescriptionListDataType: # EEBus_SPINE_TS_TimeTable.xsd:ns_p:TimeTableDescriptionListDataType -> ComplexType
    def __init__(
            self,
            time_table_description_data: list[TimeTableDescriptionDataType] = None,
    ):
        super().__init__()
        
        self.time_table_description_data = time_table_description_data

        if not isinstance(self.time_table_description_data, list | NoneType):
            raise TypeError("time_table_description_data is not of type list[TimeTableDescriptionDataType]")
        
    def get_data(self):

        msg_data = []
        
        if self.time_table_description_data is not None:
            msg_data.append({"timeTableDescriptionData": [d.get_data() for d in self.time_table_description_data]})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.time_table_description_data is not None:
            result_str += f"{sep}timeTableDescriptionData: {self.time_table_description_data}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                time_table_description_data=data_dict.get('timeTableDescriptionData'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class TimeTableConstraintsListDataType: # EEBus_SPINE_TS_TimeTable.xsd:ns_p:TimeTableConstraintsListDataType -> ComplexType
    def __init__(
            self,
            time_table_constraints_data: list[TimeTableConstraintsDataType] = None,
    ):
        super().__init__()
        
        self.time_table_constraints_data = time_table_constraints_data

        if not isinstance(self.time_table_constraints_data, list | NoneType):
            raise TypeError("time_table_constraints_data is not of type list[TimeTableConstraintsDataType]")
        
    def get_data(self):

        msg_data = []
        
        if self.time_table_constraints_data is not None:
            msg_data.append({"timeTableConstraintsData": [d.get_data() for d in self.time_table_constraints_data]})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.time_table_constraints_data is not None:
            result_str += f"{sep}timeTableConstraintsData: {self.time_table_constraints_data}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                time_table_constraints_data=data_dict.get('timeTableConstraintsData'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class TimeTableDescriptionDataElementsType: # EEBus_SPINE_TS_TimeTable.xsd:ns_p:TimeTableDescriptionDataElementsType -> ComplexType
    def __init__(
            self,
            time_table_id: ElementTagType = None,
            time_slot_count_changeable: ElementTagType = None,
            time_slot_times_changeable: ElementTagType = None,
            time_slot_time_mode: ElementTagType = None,
            label: ElementTagType = None,
            description: ElementTagType = None,
    ):
        super().__init__()
        
        self.time_table_id = time_table_id
        self.time_slot_count_changeable = time_slot_count_changeable
        self.time_slot_times_changeable = time_slot_times_changeable
        self.time_slot_time_mode = time_slot_time_mode
        self.label = label
        self.description = description

        if not isinstance(self.time_table_id, ElementTagType | NoneType):
            raise TypeError("time_table_id is not of type ElementTagType")
        
        if not isinstance(self.time_slot_count_changeable, ElementTagType | NoneType):
            raise TypeError("time_slot_count_changeable is not of type ElementTagType")
        
        if not isinstance(self.time_slot_times_changeable, ElementTagType | NoneType):
            raise TypeError("time_slot_times_changeable is not of type ElementTagType")
        
        if not isinstance(self.time_slot_time_mode, ElementTagType | NoneType):
            raise TypeError("time_slot_time_mode is not of type ElementTagType")
        
        if not isinstance(self.label, ElementTagType | NoneType):
            raise TypeError("label is not of type ElementTagType")
        
        if not isinstance(self.description, ElementTagType | NoneType):
            raise TypeError("description is not of type ElementTagType")
        
    def get_data(self):

        msg_data = []
        
        if self.time_table_id is not None:
            msg_data.append({"timeTableId": self.time_table_id.get_data()})
        if self.time_slot_count_changeable is not None:
            msg_data.append({"timeSlotCountChangeable": self.time_slot_count_changeable.get_data()})
        if self.time_slot_times_changeable is not None:
            msg_data.append({"timeSlotTimesChangeable": self.time_slot_times_changeable.get_data()})
        if self.time_slot_time_mode is not None:
            msg_data.append({"timeSlotTimeMode": self.time_slot_time_mode.get_data()})
        if self.label is not None:
            msg_data.append({"label": self.label.get_data()})
        if self.description is not None:
            msg_data.append({"description": self.description.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.time_table_id is not None:
            result_str += f"{sep}timeTableId: {self.time_table_id}"
            sep = ", "
        if self.time_slot_count_changeable is not None:
            result_str += f"{sep}timeSlotCountChangeable: {self.time_slot_count_changeable}"
            sep = ", "
        if self.time_slot_times_changeable is not None:
            result_str += f"{sep}timeSlotTimesChangeable: {self.time_slot_times_changeable}"
            sep = ", "
        if self.time_slot_time_mode is not None:
            result_str += f"{sep}timeSlotTimeMode: {self.time_slot_time_mode}"
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
                time_table_id=data_dict.get('timeTableId'),
                time_slot_count_changeable=data_dict.get('timeSlotCountChangeable'),
                time_slot_times_changeable=data_dict.get('timeSlotTimesChangeable'),
                time_slot_time_mode=data_dict.get('timeSlotTimeMode'),
                label=data_dict.get('label'),
                description=data_dict.get('description'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class TimeTableDataElementsType: # EEBus_SPINE_TS_TimeTable.xsd:ns_p:TimeTableDataElementsType -> ComplexType
    def __init__(
            self,
            time_table_id: ElementTagType = None,
            time_slot_id: ElementTagType = None,
            recurrence_information: RecurrenceInformationElementsType = None,
            start_time: AbsoluteOrRecurringTimeElementsType = None,
            end_time: AbsoluteOrRecurringTimeElementsType = None,
    ):
        super().__init__()
        
        self.time_table_id = time_table_id
        self.time_slot_id = time_slot_id
        self.recurrence_information = recurrence_information
        self.start_time = start_time
        self.end_time = end_time

        if not isinstance(self.time_table_id, ElementTagType | NoneType):
            raise TypeError("time_table_id is not of type ElementTagType")
        
        if not isinstance(self.time_slot_id, ElementTagType | NoneType):
            raise TypeError("time_slot_id is not of type ElementTagType")
        
        if not isinstance(self.recurrence_information, RecurrenceInformationElementsType | NoneType):
            raise TypeError("recurrence_information is not of type RecurrenceInformationElementsType")
        
        if not isinstance(self.start_time, AbsoluteOrRecurringTimeElementsType | NoneType):
            raise TypeError("start_time is not of type AbsoluteOrRecurringTimeElementsType")
        
        if not isinstance(self.end_time, AbsoluteOrRecurringTimeElementsType | NoneType):
            raise TypeError("end_time is not of type AbsoluteOrRecurringTimeElementsType")
        
    def get_data(self):

        msg_data = []
        
        if self.time_table_id is not None:
            msg_data.append({"timeTableId": self.time_table_id.get_data()})
        if self.time_slot_id is not None:
            msg_data.append({"timeSlotId": self.time_slot_id.get_data()})
        if self.recurrence_information is not None:
            msg_data.append({"recurrenceInformation": self.recurrence_information.get_data()})
        if self.start_time is not None:
            msg_data.append({"startTime": self.start_time.get_data()})
        if self.end_time is not None:
            msg_data.append({"endTime": self.end_time.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.time_table_id is not None:
            result_str += f"{sep}timeTableId: {self.time_table_id}"
            sep = ", "
        if self.time_slot_id is not None:
            result_str += f"{sep}timeSlotId: {self.time_slot_id}"
            sep = ", "
        if self.recurrence_information is not None:
            result_str += f"{sep}recurrenceInformation: {self.recurrence_information}"
            sep = ", "
        if self.start_time is not None:
            result_str += f"{sep}startTime: {self.start_time}"
            sep = ", "
        if self.end_time is not None:
            result_str += f"{sep}endTime: {self.end_time}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                time_table_id=data_dict.get('timeTableId'),
                time_slot_id=data_dict.get('timeSlotId'),
                recurrence_information=data_dict.get('recurrenceInformation'),
                start_time=data_dict.get('startTime'),
                end_time=data_dict.get('endTime'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class TimeTableConstraintsDataElementsType: # EEBus_SPINE_TS_TimeTable.xsd:ns_p:TimeTableConstraintsDataElementsType -> ComplexType
    def __init__(
            self,
            time_table_id: ElementTagType = None,
            slot_count_min: ElementTagType = None,
            slot_count_max: ElementTagType = None,
            slot_duration_min: ElementTagType = None,
            slot_duration_max: ElementTagType = None,
            slot_duration_step_size: ElementTagType = None,
            slot_shift_step_size: ElementTagType = None,
            first_slot_begins_at: ElementTagType = None,
    ):
        super().__init__()
        
        self.time_table_id = time_table_id
        self.slot_count_min = slot_count_min
        self.slot_count_max = slot_count_max
        self.slot_duration_min = slot_duration_min
        self.slot_duration_max = slot_duration_max
        self.slot_duration_step_size = slot_duration_step_size
        self.slot_shift_step_size = slot_shift_step_size
        self.first_slot_begins_at = first_slot_begins_at

        if not isinstance(self.time_table_id, ElementTagType | NoneType):
            raise TypeError("time_table_id is not of type ElementTagType")
        
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
        
        if not isinstance(self.slot_shift_step_size, ElementTagType | NoneType):
            raise TypeError("slot_shift_step_size is not of type ElementTagType")
        
        if not isinstance(self.first_slot_begins_at, ElementTagType | NoneType):
            raise TypeError("first_slot_begins_at is not of type ElementTagType")
        
    def get_data(self):

        msg_data = []
        
        if self.time_table_id is not None:
            msg_data.append({"timeTableId": self.time_table_id.get_data()})
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
        if self.slot_shift_step_size is not None:
            msg_data.append({"slotShiftStepSize": self.slot_shift_step_size.get_data()})
        if self.first_slot_begins_at is not None:
            msg_data.append({"firstSlotBeginsAt": self.first_slot_begins_at.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.time_table_id is not None:
            result_str += f"{sep}timeTableId: {self.time_table_id}"
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
        if self.slot_shift_step_size is not None:
            result_str += f"{sep}slotShiftStepSize: {self.slot_shift_step_size}"
            sep = ", "
        if self.first_slot_begins_at is not None:
            result_str += f"{sep}firstSlotBeginsAt: {self.first_slot_begins_at}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                time_table_id=data_dict.get('timeTableId'),
                slot_count_min=data_dict.get('slotCountMin'),
                slot_count_max=data_dict.get('slotCountMax'),
                slot_duration_min=data_dict.get('slotDurationMin'),
                slot_duration_max=data_dict.get('slotDurationMax'),
                slot_duration_step_size=data_dict.get('slotDurationStepSize'),
                slot_shift_step_size=data_dict.get('slotShiftStepSize'),
                first_slot_begins_at=data_dict.get('firstSlotBeginsAt'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class TimeTableListDataSelectorsType: # EEBus_SPINE_TS_TimeTable.xsd:ns_p:TimeTableListDataSelectorsType -> ComplexType
    def __init__(
            self,
            time_table_id: TimeTableIdType = None,
            time_slot_id: TimeSlotIdType = None,
    ):
        super().__init__()
        
        self.time_table_id = time_table_id
        self.time_slot_id = time_slot_id

        if not isinstance(self.time_table_id, TimeTableIdType | NoneType):
            raise TypeError("time_table_id is not of type TimeTableIdType")
        
        if not isinstance(self.time_slot_id, TimeSlotIdType | NoneType):
            raise TypeError("time_slot_id is not of type TimeSlotIdType")
        
    def get_data(self):

        msg_data = []
        
        if self.time_table_id is not None:
            msg_data.append({"timeTableId": self.time_table_id.get_data()})
        if self.time_slot_id is not None:
            msg_data.append({"timeSlotId": self.time_slot_id.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.time_table_id is not None:
            result_str += f"{sep}timeTableId: {self.time_table_id}"
            sep = ", "
        if self.time_slot_id is not None:
            result_str += f"{sep}timeSlotId: {self.time_slot_id}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                time_table_id=data_dict.get('timeTableId'),
                time_slot_id=data_dict.get('timeSlotId'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class TimeTableDescriptionListDataSelectorsType: # EEBus_SPINE_TS_TimeTable.xsd:ns_p:TimeTableDescriptionListDataSelectorsType -> ComplexType
    def __init__(
            self,
            time_table_id: TimeTableIdType = None,
    ):
        super().__init__()
        
        self.time_table_id = time_table_id

        if not isinstance(self.time_table_id, TimeTableIdType | NoneType):
            raise TypeError("time_table_id is not of type TimeTableIdType")
        
    def get_data(self):

        msg_data = []
        
        if self.time_table_id is not None:
            msg_data.append({"timeTableId": self.time_table_id.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.time_table_id is not None:
            result_str += f"{sep}timeTableId: {self.time_table_id}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                time_table_id=data_dict.get('timeTableId'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class TimeTableConstraintsListDataSelectorsType: # EEBus_SPINE_TS_TimeTable.xsd:ns_p:TimeTableConstraintsListDataSelectorsType -> ComplexType
    def __init__(
            self,
            time_table_id: TimeTableIdType = None,
    ):
        super().__init__()
        
        self.time_table_id = time_table_id

        if not isinstance(self.time_table_id, TimeTableIdType | NoneType):
            raise TypeError("time_table_id is not of type TimeTableIdType")
        
    def get_data(self):

        msg_data = []
        
        if self.time_table_id is not None:
            msg_data.append({"timeTableId": self.time_table_id.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.time_table_id is not None:
            result_str += f"{sep}timeTableId: {self.time_table_id}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                time_table_id=data_dict.get('timeTableId'),
            )
        elif data:
            return cls(data)
        else:
            return cls()



