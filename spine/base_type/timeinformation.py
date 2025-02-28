# Jinja Template message_type.py.jinja2
from spine.base_type.commondatatypes import ElementTagType
from spine.enums.commondatatypes import DayOfWeekType
from spine.simple_type.commondatatypes import CalendarWeekType
from types import NoneType
from spine import array_2_dict


class TimeDistributorEnquiryCallType: # EEBus_SPINE_TS_TimeInformation.xsd: ComplexType
    def __init__(
            self,
    ):
        super().__init__()
        

    def get_data(self):

        msg_data = []
        
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
            )
        elif data:
            return cls(data)
        else:
            return cls()


class TimePrecisionDataType: # EEBus_SPINE_TS_TimeInformation.xsd: ComplexType
    def __init__(
            self,
            is_synchronised: bool = None,
            last_sync_at: str = None,
            clock_drift: int = None,
    ):
        super().__init__()
        
        self.is_synchronised = is_synchronised
        self.last_sync_at = last_sync_at
        self.clock_drift = clock_drift

        if not isinstance(self.is_synchronised, bool | NoneType):
            raise TypeError("is_synchronised is not of type bool")
        
        if not isinstance(self.last_sync_at, str | NoneType):
            raise TypeError("last_sync_at is not of type str")
        
        if not isinstance(self.clock_drift, int | NoneType):
            raise TypeError("clock_drift is not of type int")
        
    def get_data(self):

        msg_data = []
        
        if self.is_synchronised is not None:
            msg_data.append({"isSynchronised": self.is_synchronised})
        if self.last_sync_at is not None:
            msg_data.append({"lastSyncAt": self.last_sync_at})
        if self.clock_drift is not None:
            msg_data.append({"clockDrift": self.clock_drift})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.is_synchronised is not None:
            result_str += f"{sep}isSynchronised: {self.is_synchronised}"
            sep = ", "
        if self.last_sync_at is not None:
            result_str += f"{sep}lastSyncAt: {self.last_sync_at}"
            sep = ", "
        if self.clock_drift is not None:
            result_str += f"{sep}clockDrift: {self.clock_drift}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                is_synchronised=data_dict.get('isSynchronised'),
                last_sync_at=data_dict.get('lastSyncAt'),
                clock_drift=data_dict.get('clockDrift'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class TimeDistributorDataType: # EEBus_SPINE_TS_TimeInformation.xsd: ComplexType
    def __init__(
            self,
            is_time_distributor: bool = None,
            distributor_priority: int = None,
    ):
        super().__init__()
        
        self.is_time_distributor = is_time_distributor
        self.distributor_priority = distributor_priority

        if not isinstance(self.is_time_distributor, bool | NoneType):
            raise TypeError("is_time_distributor is not of type bool")
        
        if not isinstance(self.distributor_priority, int | NoneType):
            raise TypeError("distributor_priority is not of type int")
        
    def get_data(self):

        msg_data = []
        
        if self.is_time_distributor is not None:
            msg_data.append({"isTimeDistributor": self.is_time_distributor})
        if self.distributor_priority is not None:
            msg_data.append({"distributorPriority": self.distributor_priority})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.is_time_distributor is not None:
            result_str += f"{sep}isTimeDistributor: {self.is_time_distributor}"
            sep = ", "
        if self.distributor_priority is not None:
            result_str += f"{sep}distributorPriority: {self.distributor_priority}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                is_time_distributor=data_dict.get('isTimeDistributor'),
                distributor_priority=data_dict.get('distributorPriority'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class TimeInformationDataType: # EEBus_SPINE_TS_TimeInformation.xsd: ComplexType
    def __init__(
            self,
            utc: str = None,
            utc_offset: str = None,
            day_of_week: DayOfWeekType = None,
            calendar_week: CalendarWeekType = None,
    ):
        super().__init__()
        
        self.utc = utc
        self.utc_offset = utc_offset
        self.day_of_week = day_of_week
        self.calendar_week = calendar_week

        if not isinstance(self.utc, str | NoneType):
            raise TypeError("utc is not of type str")
        
        if not isinstance(self.utc_offset, str | NoneType):
            raise TypeError("utc_offset is not of type str")
        
        if not isinstance(self.day_of_week, DayOfWeekType | NoneType):
            raise TypeError("day_of_week is not of type DayOfWeekType")
        
        if not isinstance(self.calendar_week, CalendarWeekType | NoneType):
            raise TypeError("calendar_week is not of type CalendarWeekType")
        
    def get_data(self):

        msg_data = []
        
        if self.utc is not None:
            msg_data.append({"utc": self.utc})
        if self.utc_offset is not None:
            msg_data.append({"utcOffset": self.utc_offset})
        if self.day_of_week is not None:
            msg_data.append({"dayOfWeek": self.day_of_week.value})
        if self.calendar_week is not None:
            msg_data.append({"calendarWeek": self.calendar_week.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.utc is not None:
            result_str += f"{sep}utc: {self.utc}"
            sep = ", "
        if self.utc_offset is not None:
            result_str += f"{sep}utcOffset: {self.utc_offset}"
            sep = ", "
        if self.day_of_week is not None:
            result_str += f"{sep}dayOfWeek: {self.day_of_week}"
            sep = ", "
        if self.calendar_week is not None:
            result_str += f"{sep}calendarWeek: {self.calendar_week}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                utc=data_dict.get('utc'),
                utc_offset=data_dict.get('utcOffset'),
                day_of_week=data_dict.get('dayOfWeek'),
                calendar_week=data_dict.get('calendarWeek'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class TimePrecisionDataElementsType: # EEBus_SPINE_TS_TimeInformation.xsd: ComplexType
    def __init__(
            self,
            is_synchronised: ElementTagType = None,
            last_sync_at: ElementTagType = None,
            clock_drift: ElementTagType = None,
    ):
        super().__init__()
        
        self.is_synchronised = is_synchronised
        self.last_sync_at = last_sync_at
        self.clock_drift = clock_drift

        if not isinstance(self.is_synchronised, ElementTagType | NoneType):
            raise TypeError("is_synchronised is not of type ElementTagType")
        
        if not isinstance(self.last_sync_at, ElementTagType | NoneType):
            raise TypeError("last_sync_at is not of type ElementTagType")
        
        if not isinstance(self.clock_drift, ElementTagType | NoneType):
            raise TypeError("clock_drift is not of type ElementTagType")
        
    def get_data(self):

        msg_data = []
        
        if self.is_synchronised is not None:
            msg_data.append({"isSynchronised": self.is_synchronised.get_data()})
        if self.last_sync_at is not None:
            msg_data.append({"lastSyncAt": self.last_sync_at.get_data()})
        if self.clock_drift is not None:
            msg_data.append({"clockDrift": self.clock_drift.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.is_synchronised is not None:
            result_str += f"{sep}isSynchronised: {self.is_synchronised}"
            sep = ", "
        if self.last_sync_at is not None:
            result_str += f"{sep}lastSyncAt: {self.last_sync_at}"
            sep = ", "
        if self.clock_drift is not None:
            result_str += f"{sep}clockDrift: {self.clock_drift}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                is_synchronised=data_dict.get('isSynchronised'),
                last_sync_at=data_dict.get('lastSyncAt'),
                clock_drift=data_dict.get('clockDrift'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class TimeInformationDataElementsType: # EEBus_SPINE_TS_TimeInformation.xsd: ComplexType
    def __init__(
            self,
            utc: ElementTagType = None,
            utc_offset: ElementTagType = None,
            day_of_week: ElementTagType = None,
            calendar_week: ElementTagType = None,
    ):
        super().__init__()
        
        self.utc = utc
        self.utc_offset = utc_offset
        self.day_of_week = day_of_week
        self.calendar_week = calendar_week

        if not isinstance(self.utc, ElementTagType | NoneType):
            raise TypeError("utc is not of type ElementTagType")
        
        if not isinstance(self.utc_offset, ElementTagType | NoneType):
            raise TypeError("utc_offset is not of type ElementTagType")
        
        if not isinstance(self.day_of_week, ElementTagType | NoneType):
            raise TypeError("day_of_week is not of type ElementTagType")
        
        if not isinstance(self.calendar_week, ElementTagType | NoneType):
            raise TypeError("calendar_week is not of type ElementTagType")
        
    def get_data(self):

        msg_data = []
        
        if self.utc is not None:
            msg_data.append({"utc": self.utc.get_data()})
        if self.utc_offset is not None:
            msg_data.append({"utcOffset": self.utc_offset.get_data()})
        if self.day_of_week is not None:
            msg_data.append({"dayOfWeek": self.day_of_week.get_data()})
        if self.calendar_week is not None:
            msg_data.append({"calendarWeek": self.calendar_week.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.utc is not None:
            result_str += f"{sep}utc: {self.utc}"
            sep = ", "
        if self.utc_offset is not None:
            result_str += f"{sep}utcOffset: {self.utc_offset}"
            sep = ", "
        if self.day_of_week is not None:
            result_str += f"{sep}dayOfWeek: {self.day_of_week}"
            sep = ", "
        if self.calendar_week is not None:
            result_str += f"{sep}calendarWeek: {self.calendar_week}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                utc=data_dict.get('utc'),
                utc_offset=data_dict.get('utcOffset'),
                day_of_week=data_dict.get('dayOfWeek'),
                calendar_week=data_dict.get('calendarWeek'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class TimeDistributorEnquiryCallElementsType: # EEBus_SPINE_TS_TimeInformation.xsd: ComplexType
    def __init__(
            self,
    ):
        super().__init__()
        

    def get_data(self):

        msg_data = []
        
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
            )
        elif data:
            return cls(data)
        else:
            return cls()


class TimeDistributorDataElementsType: # EEBus_SPINE_TS_TimeInformation.xsd: ComplexType
    def __init__(
            self,
            is_time_distributor: ElementTagType = None,
            distributor_priority: ElementTagType = None,
    ):
        super().__init__()
        
        self.is_time_distributor = is_time_distributor
        self.distributor_priority = distributor_priority

        if not isinstance(self.is_time_distributor, ElementTagType | NoneType):
            raise TypeError("is_time_distributor is not of type ElementTagType")
        
        if not isinstance(self.distributor_priority, ElementTagType | NoneType):
            raise TypeError("distributor_priority is not of type ElementTagType")
        
    def get_data(self):

        msg_data = []
        
        if self.is_time_distributor is not None:
            msg_data.append({"isTimeDistributor": self.is_time_distributor.get_data()})
        if self.distributor_priority is not None:
            msg_data.append({"distributorPriority": self.distributor_priority.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.is_time_distributor is not None:
            result_str += f"{sep}isTimeDistributor: {self.is_time_distributor}"
            sep = ", "
        if self.distributor_priority is not None:
            result_str += f"{sep}distributorPriority: {self.distributor_priority}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                is_time_distributor=data_dict.get('isTimeDistributor'),
                distributor_priority=data_dict.get('distributorPriority'),
            )
        elif data:
            return cls(data)
        else:
            return cls()



