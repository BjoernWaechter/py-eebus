# Jinja Template message_type.py.jinja2
from spine.simple_type.commondatatypes import DayOfMonthType
from spine.simple_type.commondatatypes import CalendarWeekType
from spine.simple_type.commondatatypes import AddressDeviceType
from spine.simple_type.commondatatypes import NumberType
from spine.enums.commondatatypes import MonthType
from spine.union_type.commondatatypes import FunctionType
from spine.simple_type.commondatatypes import ScaleType
from spine.simple_type.commondatatypes import AddressFeatureType
from spine.simple_type.commondatatypes import AddressEntityType
from types import NoneType
from spine import array_2_dict


class ElementTagType:
    def __init__(
            self,
    ):
        super().__init__()
        

    def get_data(self): # ComplexType

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


class PossibleOperationsClassifierType:
    def __init__(
            self,
            partial: ElementTagType = None,
    ):
        super().__init__()
        
        self.partial = partial

        if not isinstance(self.partial, ElementTagType | NoneType):
            raise TypeError("partial is not of type ElementTagType")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.partial is not None:
            msg_data.append({"partial": self.partial.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.partial is not None:
            result_str += f"{sep}partial: {self.partial}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                partial=data_dict.get('partial'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class ScaledNumberType:
    def __init__(
            self,
            number: NumberType = None,
            scale: ScaleType = None,
    ):
        super().__init__()
        
        self.number = number
        self.scale = scale

        if not isinstance(self.number, NumberType | NoneType):
            raise TypeError("number is not of type NumberType")
        
        if not isinstance(self.scale, ScaleType | NoneType):
            raise TypeError("scale is not of type ScaleType")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.number is not None:
            msg_data.append({"number": self.number.get_data()})
        if self.scale is not None:
            msg_data.append({"scale": self.scale.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.number is not None:
            result_str += f"{sep}number: {self.number}"
            sep = ", "
        if self.scale is not None:
            result_str += f"{sep}scale: {self.scale}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                number=data_dict.get('number'),
                scale=data_dict.get('scale'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class ScaledNumberElementsType:
    def __init__(
            self,
            number: ElementTagType = None,
            scale: ElementTagType = None,
    ):
        super().__init__()
        
        self.number = number
        self.scale = scale

        if not isinstance(self.number, ElementTagType | NoneType):
            raise TypeError("number is not of type ElementTagType")
        
        if not isinstance(self.scale, ElementTagType | NoneType):
            raise TypeError("scale is not of type ElementTagType")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.number is not None:
            msg_data.append({"number": self.number.get_data()})
        if self.scale is not None:
            msg_data.append({"scale": self.scale.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.number is not None:
            result_str += f"{sep}number: {self.number}"
            sep = ", "
        if self.scale is not None:
            result_str += f"{sep}scale: {self.scale}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                number=data_dict.get('number'),
                scale=data_dict.get('scale'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class PossibleOperationsWriteType:
    def __init__(
            self,
            partial: ElementTagType = None,
    ):
        super().__init__()
        
        self.partial = partial

        if not isinstance(self.partial, ElementTagType | NoneType):
            raise TypeError("partial is not of type ElementTagType")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.partial is not None:
            msg_data.append({"partial": self.partial.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.partial is not None:
            result_str += f"{sep}partial: {self.partial}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                partial=data_dict.get('partial'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class PossibleOperationsReadType:
    def __init__(
            self,
            partial: ElementTagType = None,
    ):
        super().__init__()
        
        self.partial = partial

        if not isinstance(self.partial, ElementTagType | NoneType):
            raise TypeError("partial is not of type ElementTagType")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.partial is not None:
            msg_data.append({"partial": self.partial.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.partial is not None:
            result_str += f"{sep}partial: {self.partial}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                partial=data_dict.get('partial'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class DeviceAddressType:
    def __init__(
            self,
            device: AddressDeviceType = None,
    ):
        super().__init__()
        
        self.device = device

        if not isinstance(self.device, AddressDeviceType | NoneType):
            raise TypeError("device is not of type AddressDeviceType")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.device is not None:
            msg_data.append({"device": self.device.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.device is not None:
            result_str += f"{sep}device: {self.device}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                device=data_dict.get('device'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class DeviceAddressElementsType:
    def __init__(
            self,
            device: ElementTagType = None,
    ):
        super().__init__()
        
        self.device = device

        if not isinstance(self.device, ElementTagType | NoneType):
            raise TypeError("device is not of type ElementTagType")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.device is not None:
            msg_data.append({"device": self.device.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.device is not None:
            result_str += f"{sep}device: {self.device}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                device=data_dict.get('device'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class ScaledNumberRangeType:
    def __init__(
            self,
            min: ScaledNumberType = None,
            max: ScaledNumberType = None,
    ):
        super().__init__()
        
        self.min = min
        self.max = max

        if not isinstance(self.min, ScaledNumberType | NoneType):
            raise TypeError("min is not of type ScaledNumberType")
        
        if not isinstance(self.max, ScaledNumberType | NoneType):
            raise TypeError("max is not of type ScaledNumberType")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.min is not None:
            msg_data.append({"min": self.min.get_data()})
        if self.max is not None:
            msg_data.append({"max": self.max.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.min is not None:
            result_str += f"{sep}min: {self.min}"
            sep = ", "
        if self.max is not None:
            result_str += f"{sep}max: {self.max}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                min=data_dict.get('min'),
                max=data_dict.get('max'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class ScaledNumberRangeElementsType:
    def __init__(
            self,
            min: ScaledNumberElementsType = None,
            max: ScaledNumberElementsType = None,
    ):
        super().__init__()
        
        self.min = min
        self.max = max

        if not isinstance(self.min, ScaledNumberElementsType | NoneType):
            raise TypeError("min is not of type ScaledNumberElementsType")
        
        if not isinstance(self.max, ScaledNumberElementsType | NoneType):
            raise TypeError("max is not of type ScaledNumberElementsType")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.min is not None:
            msg_data.append({"min": self.min.get_data()})
        if self.max is not None:
            msg_data.append({"max": self.max.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.min is not None:
            result_str += f"{sep}min: {self.min}"
            sep = ", "
        if self.max is not None:
            result_str += f"{sep}max: {self.max}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                min=data_dict.get('min'),
                max=data_dict.get('max'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class PossibleOperationsType:
    def __init__(
            self,
            read: PossibleOperationsReadType = None,
            write: PossibleOperationsWriteType = None,
    ):
        super().__init__()
        
        self.read = read
        self.write = write

        if not isinstance(self.read, PossibleOperationsReadType | NoneType):
            raise TypeError("read is not of type PossibleOperationsReadType")
        
        if not isinstance(self.write, PossibleOperationsWriteType | NoneType):
            raise TypeError("write is not of type PossibleOperationsWriteType")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.read is not None:
            msg_data.append({"read": self.read.get_data()})
        if self.write is not None:
            msg_data.append({"write": self.write.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.read is not None:
            result_str += f"{sep}read: {self.read}"
            sep = ", "
        if self.write is not None:
            result_str += f"{sep}write: {self.write}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                read=data_dict.get('read'),
                write=data_dict.get('write'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class PossibleOperationsElementsType:
    def __init__(
            self,
            read: ElementTagType = None,
            write: ElementTagType = None,
    ):
        super().__init__()
        
        self.read = read
        self.write = write

        if not isinstance(self.read, ElementTagType | NoneType):
            raise TypeError("read is not of type ElementTagType")
        
        if not isinstance(self.write, ElementTagType | NoneType):
            raise TypeError("write is not of type ElementTagType")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.read is not None:
            msg_data.append({"read": self.read.get_data()})
        if self.write is not None:
            msg_data.append({"write": self.write.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.read is not None:
            result_str += f"{sep}read: {self.read}"
            sep = ", "
        if self.write is not None:
            result_str += f"{sep}write: {self.write}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                read=data_dict.get('read'),
                write=data_dict.get('write'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class EntityAddressType:
    def __init__(
            self,
            device: AddressDeviceType = None,
            entity: list[AddressEntityType] = None,
    ):
        super().__init__()
        
        self.device = device
        self.entity = entity

        if not isinstance(self.device, AddressDeviceType | NoneType):
            raise TypeError("device is not of type AddressDeviceType")
        
        if not isinstance(self.entity, list | NoneType):
            raise TypeError("entity is not of type list[AddressEntityType]")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.device is not None:
            msg_data.append({"device": self.device.get_data()})
        if self.entity is not None:
            msg_data.append({"entity": [d.get_data() for d in self.entity]})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.device is not None:
            result_str += f"{sep}device: {self.device}"
            sep = ", "
        if self.entity is not None:
            result_str += f"{sep}entity: {self.entity}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                device=data_dict.get('device'),
                entity=data_dict.get('entity'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class EntityAddressElementsType:
    def __init__(
            self,
            device: ElementTagType = None,
            entity: ElementTagType = None,
    ):
        super().__init__()
        
        self.device = device
        self.entity = entity

        if not isinstance(self.device, ElementTagType | NoneType):
            raise TypeError("device is not of type ElementTagType")
        
        if not isinstance(self.entity, ElementTagType | NoneType):
            raise TypeError("entity is not of type ElementTagType")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.device is not None:
            msg_data.append({"device": self.device.get_data()})
        if self.entity is not None:
            msg_data.append({"entity": self.entity.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.device is not None:
            result_str += f"{sep}device: {self.device}"
            sep = ", "
        if self.entity is not None:
            result_str += f"{sep}entity: {self.entity}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                device=data_dict.get('device'),
                entity=data_dict.get('entity'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class DaysOfWeekType:
    def __init__(
            self,
            monday: ElementTagType = None,
            tuesday: ElementTagType = None,
            wednesday: ElementTagType = None,
            thursday: ElementTagType = None,
            friday: ElementTagType = None,
            saturday: ElementTagType = None,
            sunday: ElementTagType = None,
    ):
        super().__init__()
        
        self.monday = monday
        self.tuesday = tuesday
        self.wednesday = wednesday
        self.thursday = thursday
        self.friday = friday
        self.saturday = saturday
        self.sunday = sunday

        if not isinstance(self.monday, ElementTagType | NoneType):
            raise TypeError("monday is not of type ElementTagType")
        
        if not isinstance(self.tuesday, ElementTagType | NoneType):
            raise TypeError("tuesday is not of type ElementTagType")
        
        if not isinstance(self.wednesday, ElementTagType | NoneType):
            raise TypeError("wednesday is not of type ElementTagType")
        
        if not isinstance(self.thursday, ElementTagType | NoneType):
            raise TypeError("thursday is not of type ElementTagType")
        
        if not isinstance(self.friday, ElementTagType | NoneType):
            raise TypeError("friday is not of type ElementTagType")
        
        if not isinstance(self.saturday, ElementTagType | NoneType):
            raise TypeError("saturday is not of type ElementTagType")
        
        if not isinstance(self.sunday, ElementTagType | NoneType):
            raise TypeError("sunday is not of type ElementTagType")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.monday is not None:
            msg_data.append({"monday": self.monday.get_data()})
        if self.tuesday is not None:
            msg_data.append({"tuesday": self.tuesday.get_data()})
        if self.wednesday is not None:
            msg_data.append({"wednesday": self.wednesday.get_data()})
        if self.thursday is not None:
            msg_data.append({"thursday": self.thursday.get_data()})
        if self.friday is not None:
            msg_data.append({"friday": self.friday.get_data()})
        if self.saturday is not None:
            msg_data.append({"saturday": self.saturday.get_data()})
        if self.sunday is not None:
            msg_data.append({"sunday": self.sunday.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.monday is not None:
            result_str += f"{sep}monday: {self.monday}"
            sep = ", "
        if self.tuesday is not None:
            result_str += f"{sep}tuesday: {self.tuesday}"
            sep = ", "
        if self.wednesday is not None:
            result_str += f"{sep}wednesday: {self.wednesday}"
            sep = ", "
        if self.thursday is not None:
            result_str += f"{sep}thursday: {self.thursday}"
            sep = ", "
        if self.friday is not None:
            result_str += f"{sep}friday: {self.friday}"
            sep = ", "
        if self.saturday is not None:
            result_str += f"{sep}saturday: {self.saturday}"
            sep = ", "
        if self.sunday is not None:
            result_str += f"{sep}sunday: {self.sunday}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                monday=data_dict.get('monday'),
                tuesday=data_dict.get('tuesday'),
                wednesday=data_dict.get('wednesday'),
                thursday=data_dict.get('thursday'),
                friday=data_dict.get('friday'),
                saturday=data_dict.get('saturday'),
                sunday=data_dict.get('sunday'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class TimestampIntervalType:
    def __init__(
            self,
            start_time: FunctionType = None,
            end_time: FunctionType = None,
    ):
        super().__init__()
        
        self.start_time = start_time
        self.end_time = end_time

        if not isinstance(self.start_time, FunctionType | NoneType):
            raise TypeError("start_time is not of type FunctionType")
        
        if not isinstance(self.end_time, FunctionType | NoneType):
            raise TypeError("end_time is not of type FunctionType")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.start_time is not None:
            msg_data.append({"startTime": self.start_time.get_data()})
        if self.end_time is not None:
            msg_data.append({"endTime": self.end_time.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
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
                start_time=data_dict.get('startTime'),
                end_time=data_dict.get('endTime'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class TimePeriodType:
    def __init__(
            self,
            start_time: FunctionType = None,
            end_time: FunctionType = None,
    ):
        super().__init__()
        
        self.start_time = start_time
        self.end_time = end_time

        if not isinstance(self.start_time, FunctionType | NoneType):
            raise TypeError("start_time is not of type FunctionType")
        
        if not isinstance(self.end_time, FunctionType | NoneType):
            raise TypeError("end_time is not of type FunctionType")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.start_time is not None:
            msg_data.append({"startTime": self.start_time.get_data()})
        if self.end_time is not None:
            msg_data.append({"endTime": self.end_time.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
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
                start_time=data_dict.get('startTime'),
                end_time=data_dict.get('endTime'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class TimePeriodElementsType:
    def __init__(
            self,
            start_time: ElementTagType = None,
            end_time: ElementTagType = None,
    ):
        super().__init__()
        
        self.start_time = start_time
        self.end_time = end_time

        if not isinstance(self.start_time, ElementTagType | NoneType):
            raise TypeError("start_time is not of type ElementTagType")
        
        if not isinstance(self.end_time, ElementTagType | NoneType):
            raise TypeError("end_time is not of type ElementTagType")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.start_time is not None:
            msg_data.append({"startTime": self.start_time.get_data()})
        if self.end_time is not None:
            msg_data.append({"endTime": self.end_time.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
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
                start_time=data_dict.get('startTime'),
                end_time=data_dict.get('endTime'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class ScaledNumberSetType:
    def __init__(
            self,
            value: list[ScaledNumberType] = None,
            range: list[ScaledNumberRangeType] = None,
    ):
        super().__init__()
        
        self.value = value
        self.range = range

        if not isinstance(self.value, list | NoneType):
            raise TypeError("value is not of type list[ScaledNumberType]")
        
        if not isinstance(self.range, list | NoneType):
            raise TypeError("range is not of type list[ScaledNumberRangeType]")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.value is not None:
            msg_data.append({"value": [d.get_data() for d in self.value]})
        if self.range is not None:
            msg_data.append({"range": [d.get_data() for d in self.range]})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.value is not None:
            result_str += f"{sep}value: {self.value}"
            sep = ", "
        if self.range is not None:
            result_str += f"{sep}range: {self.range}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                value=data_dict.get('value'),
                range=data_dict.get('range'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class ScaledNumberSetElementsType:
    def __init__(
            self,
            value: ScaledNumberElementsType = None,
            range: ScaledNumberRangeElementsType = None,
    ):
        super().__init__()
        
        self.value = value
        self.range = range

        if not isinstance(self.value, ScaledNumberElementsType | NoneType):
            raise TypeError("value is not of type ScaledNumberElementsType")
        
        if not isinstance(self.range, ScaledNumberRangeElementsType | NoneType):
            raise TypeError("range is not of type ScaledNumberRangeElementsType")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.value is not None:
            msg_data.append({"value": self.value.get_data()})
        if self.range is not None:
            msg_data.append({"range": self.range.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.value is not None:
            result_str += f"{sep}value: {self.value}"
            sep = ", "
        if self.range is not None:
            result_str += f"{sep}range: {self.range}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                value=data_dict.get('value'),
                range=data_dict.get('range'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class RecurrenceInformationType:
    def __init__(
            self,
            recurring_interval: FunctionType = None,
            recurring_interval_step: int = None,
            first_execution: str = None,
            execution_count: int = None,
            last_execution: str = None,
    ):
        super().__init__()
        
        self.recurring_interval = recurring_interval
        self.recurring_interval_step = recurring_interval_step
        self.first_execution = first_execution
        self.execution_count = execution_count
        self.last_execution = last_execution

        if not isinstance(self.recurring_interval, FunctionType | NoneType):
            raise TypeError("recurring_interval is not of type FunctionType")
        
        if not isinstance(self.recurring_interval_step, int | NoneType):
            raise TypeError("recurring_interval_step is not of type int")
        
        if not isinstance(self.first_execution, str | NoneType):
            raise TypeError("first_execution is not of type str")
        
        if not isinstance(self.execution_count, int | NoneType):
            raise TypeError("execution_count is not of type int")
        
        if not isinstance(self.last_execution, str | NoneType):
            raise TypeError("last_execution is not of type str")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.recurring_interval is not None:
            msg_data.append({"recurringInterval": self.recurring_interval.get_data()})
        if self.recurring_interval_step is not None:
            msg_data.append({"recurringIntervalStep": self.recurring_interval_step})
        if self.first_execution is not None:
            msg_data.append({"firstExecution": self.first_execution})
        if self.execution_count is not None:
            msg_data.append({"executionCount": self.execution_count})
        if self.last_execution is not None:
            msg_data.append({"lastExecution": self.last_execution})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.recurring_interval is not None:
            result_str += f"{sep}recurringInterval: {self.recurring_interval}"
            sep = ", "
        if self.recurring_interval_step is not None:
            result_str += f"{sep}recurringIntervalStep: {self.recurring_interval_step}"
            sep = ", "
        if self.first_execution is not None:
            result_str += f"{sep}firstExecution: {self.first_execution}"
            sep = ", "
        if self.execution_count is not None:
            result_str += f"{sep}executionCount: {self.execution_count}"
            sep = ", "
        if self.last_execution is not None:
            result_str += f"{sep}lastExecution: {self.last_execution}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                recurring_interval=data_dict.get('recurringInterval'),
                recurring_interval_step=data_dict.get('recurringIntervalStep'),
                first_execution=data_dict.get('firstExecution'),
                execution_count=data_dict.get('executionCount'),
                last_execution=data_dict.get('lastExecution'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class RecurrenceInformationElementsType:
    def __init__(
            self,
            recurring_interval: ElementTagType = None,
            recurring_interval_step: ElementTagType = None,
            first_execution: ElementTagType = None,
            execution_count: ElementTagType = None,
            last_execution: ElementTagType = None,
    ):
        super().__init__()
        
        self.recurring_interval = recurring_interval
        self.recurring_interval_step = recurring_interval_step
        self.first_execution = first_execution
        self.execution_count = execution_count
        self.last_execution = last_execution

        if not isinstance(self.recurring_interval, ElementTagType | NoneType):
            raise TypeError("recurring_interval is not of type ElementTagType")
        
        if not isinstance(self.recurring_interval_step, ElementTagType | NoneType):
            raise TypeError("recurring_interval_step is not of type ElementTagType")
        
        if not isinstance(self.first_execution, ElementTagType | NoneType):
            raise TypeError("first_execution is not of type ElementTagType")
        
        if not isinstance(self.execution_count, ElementTagType | NoneType):
            raise TypeError("execution_count is not of type ElementTagType")
        
        if not isinstance(self.last_execution, ElementTagType | NoneType):
            raise TypeError("last_execution is not of type ElementTagType")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.recurring_interval is not None:
            msg_data.append({"recurringInterval": self.recurring_interval.get_data()})
        if self.recurring_interval_step is not None:
            msg_data.append({"recurringIntervalStep": self.recurring_interval_step.get_data()})
        if self.first_execution is not None:
            msg_data.append({"firstExecution": self.first_execution.get_data()})
        if self.execution_count is not None:
            msg_data.append({"executionCount": self.execution_count.get_data()})
        if self.last_execution is not None:
            msg_data.append({"lastExecution": self.last_execution.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.recurring_interval is not None:
            result_str += f"{sep}recurringInterval: {self.recurring_interval}"
            sep = ", "
        if self.recurring_interval_step is not None:
            result_str += f"{sep}recurringIntervalStep: {self.recurring_interval_step}"
            sep = ", "
        if self.first_execution is not None:
            result_str += f"{sep}firstExecution: {self.first_execution}"
            sep = ", "
        if self.execution_count is not None:
            result_str += f"{sep}executionCount: {self.execution_count}"
            sep = ", "
        if self.last_execution is not None:
            result_str += f"{sep}lastExecution: {self.last_execution}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                recurring_interval=data_dict.get('recurringInterval'),
                recurring_interval_step=data_dict.get('recurringIntervalStep'),
                first_execution=data_dict.get('firstExecution'),
                execution_count=data_dict.get('executionCount'),
                last_execution=data_dict.get('lastExecution'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class FunctionPropertyType:
    def __init__(
            self,
            function: FunctionType = None,
            possible_operations: PossibleOperationsType = None,
    ):
        super().__init__()
        
        self.function = function
        self.possible_operations = possible_operations

        if not isinstance(self.function, FunctionType | NoneType):
            raise TypeError("function is not of type FunctionType")
        
        if not isinstance(self.possible_operations, PossibleOperationsType | NoneType):
            raise TypeError("possible_operations is not of type PossibleOperationsType")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.function is not None:
            msg_data.append({"function": self.function.get_data()})
        if self.possible_operations is not None:
            msg_data.append({"possibleOperations": self.possible_operations.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.function is not None:
            result_str += f"{sep}function: {self.function}"
            sep = ", "
        if self.possible_operations is not None:
            result_str += f"{sep}possibleOperations: {self.possible_operations}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                function=data_dict.get('function'),
                possible_operations=data_dict.get('possibleOperations'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class FunctionPropertyElementsType:
    def __init__(
            self,
            function: ElementTagType = None,
            possible_operations: PossibleOperationsElementsType = None,
    ):
        super().__init__()
        
        self.function = function
        self.possible_operations = possible_operations

        if not isinstance(self.function, ElementTagType | NoneType):
            raise TypeError("function is not of type ElementTagType")
        
        if not isinstance(self.possible_operations, PossibleOperationsElementsType | NoneType):
            raise TypeError("possible_operations is not of type PossibleOperationsElementsType")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.function is not None:
            msg_data.append({"function": self.function.get_data()})
        if self.possible_operations is not None:
            msg_data.append({"possibleOperations": self.possible_operations.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.function is not None:
            result_str += f"{sep}function: {self.function}"
            sep = ", "
        if self.possible_operations is not None:
            result_str += f"{sep}possibleOperations: {self.possible_operations}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                function=data_dict.get('function'),
                possible_operations=data_dict.get('possibleOperations'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class FeatureAddressType:
    def __init__(
            self,
            device: AddressDeviceType = None,
            entity: list[AddressEntityType] = None,
            feature: AddressFeatureType = None,
    ):
        super().__init__()
        
        self.device = device
        self.entity = entity
        self.feature = feature

        if not isinstance(self.device, AddressDeviceType | NoneType):
            raise TypeError("device is not of type AddressDeviceType")
        
        if not isinstance(self.entity, list | NoneType):
            raise TypeError("entity is not of type list[AddressEntityType]")
        
        if not isinstance(self.feature, AddressFeatureType | NoneType):
            raise TypeError("feature is not of type AddressFeatureType")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.device is not None:
            msg_data.append({"device": self.device.get_data()})
        if self.entity is not None:
            msg_data.append({"entity": [d.get_data() for d in self.entity]})
        if self.feature is not None:
            msg_data.append({"feature": self.feature.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.device is not None:
            result_str += f"{sep}device: {self.device}"
            sep = ", "
        if self.entity is not None:
            result_str += f"{sep}entity: {self.entity}"
            sep = ", "
        if self.feature is not None:
            result_str += f"{sep}feature: {self.feature}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                device=data_dict.get('device'),
                entity=data_dict.get('entity'),
                feature=data_dict.get('feature'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class FeatureAddressElementsType:
    def __init__(
            self,
            device: ElementTagType = None,
            entity: ElementTagType = None,
            feature: ElementTagType = None,
    ):
        super().__init__()
        
        self.device = device
        self.entity = entity
        self.feature = feature

        if not isinstance(self.device, ElementTagType | NoneType):
            raise TypeError("device is not of type ElementTagType")
        
        if not isinstance(self.entity, ElementTagType | NoneType):
            raise TypeError("entity is not of type ElementTagType")
        
        if not isinstance(self.feature, ElementTagType | NoneType):
            raise TypeError("feature is not of type ElementTagType")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.device is not None:
            msg_data.append({"device": self.device.get_data()})
        if self.entity is not None:
            msg_data.append({"entity": self.entity.get_data()})
        if self.feature is not None:
            msg_data.append({"feature": self.feature.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.device is not None:
            result_str += f"{sep}device: {self.device}"
            sep = ", "
        if self.entity is not None:
            result_str += f"{sep}entity: {self.entity}"
            sep = ", "
        if self.feature is not None:
            result_str += f"{sep}feature: {self.feature}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                device=data_dict.get('device'),
                entity=data_dict.get('entity'),
                feature=data_dict.get('feature'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class AbsoluteOrRecurringTimeType:
    def __init__(
            self,
            date_time: str = None,
            month: MonthType = None,
            day_of_month: DayOfMonthType = None,
            calendar_week: CalendarWeekType = None,
            day_of_week_occurrence: FunctionType = None,
            days_of_week: DaysOfWeekType = None,
            time: str = None,
            relative: str = None,
    ):
        super().__init__()
        
        self.date_time = date_time
        self.month = month
        self.day_of_month = day_of_month
        self.calendar_week = calendar_week
        self.day_of_week_occurrence = day_of_week_occurrence
        self.days_of_week = days_of_week
        self.time = time
        self.relative = relative

        if not isinstance(self.date_time, str | NoneType):
            raise TypeError("date_time is not of type str")
        
        if not isinstance(self.month, MonthType | NoneType):
            raise TypeError("month is not of type MonthType")
        
        if not isinstance(self.day_of_month, DayOfMonthType | NoneType):
            raise TypeError("day_of_month is not of type DayOfMonthType")
        
        if not isinstance(self.calendar_week, CalendarWeekType | NoneType):
            raise TypeError("calendar_week is not of type CalendarWeekType")
        
        if not isinstance(self.day_of_week_occurrence, FunctionType | NoneType):
            raise TypeError("day_of_week_occurrence is not of type FunctionType")
        
        if not isinstance(self.days_of_week, DaysOfWeekType | NoneType):
            raise TypeError("days_of_week is not of type DaysOfWeekType")
        
        if not isinstance(self.time, str | NoneType):
            raise TypeError("time is not of type str")
        
        if not isinstance(self.relative, str | NoneType):
            raise TypeError("relative is not of type str")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.date_time is not None:
            msg_data.append({"dateTime": self.date_time})
        if self.month is not None:
            msg_data.append({"month": self.month.value})
        if self.day_of_month is not None:
            msg_data.append({"dayOfMonth": self.day_of_month.get_data()})
        if self.calendar_week is not None:
            msg_data.append({"calendarWeek": self.calendar_week.get_data()})
        if self.day_of_week_occurrence is not None:
            msg_data.append({"dayOfWeekOccurrence": self.day_of_week_occurrence.get_data()})
        if self.days_of_week is not None:
            msg_data.append({"daysOfWeek": self.days_of_week.get_data()})
        if self.time is not None:
            msg_data.append({"time": self.time})
        if self.relative is not None:
            msg_data.append({"relative": self.relative})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.date_time is not None:
            result_str += f"{sep}dateTime: {self.date_time}"
            sep = ", "
        if self.month is not None:
            result_str += f"{sep}month: {self.month}"
            sep = ", "
        if self.day_of_month is not None:
            result_str += f"{sep}dayOfMonth: {self.day_of_month}"
            sep = ", "
        if self.calendar_week is not None:
            result_str += f"{sep}calendarWeek: {self.calendar_week}"
            sep = ", "
        if self.day_of_week_occurrence is not None:
            result_str += f"{sep}dayOfWeekOccurrence: {self.day_of_week_occurrence}"
            sep = ", "
        if self.days_of_week is not None:
            result_str += f"{sep}daysOfWeek: {self.days_of_week}"
            sep = ", "
        if self.time is not None:
            result_str += f"{sep}time: {self.time}"
            sep = ", "
        if self.relative is not None:
            result_str += f"{sep}relative: {self.relative}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                date_time=data_dict.get('dateTime'),
                month=data_dict.get('month'),
                day_of_month=data_dict.get('dayOfMonth'),
                calendar_week=data_dict.get('calendarWeek'),
                day_of_week_occurrence=data_dict.get('dayOfWeekOccurrence'),
                days_of_week=data_dict.get('daysOfWeek'),
                time=data_dict.get('time'),
                relative=data_dict.get('relative'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class AbsoluteOrRecurringTimeElementsType:
    def __init__(
            self,
            date_time: ElementTagType = None,
            month: ElementTagType = None,
            day_of_month: ElementTagType = None,
            calendar_week: ElementTagType = None,
            day_of_week_occurrence: ElementTagType = None,
            days_of_week: ElementTagType = None,
            time: ElementTagType = None,
            relative: ElementTagType = None,
    ):
        super().__init__()
        
        self.date_time = date_time
        self.month = month
        self.day_of_month = day_of_month
        self.calendar_week = calendar_week
        self.day_of_week_occurrence = day_of_week_occurrence
        self.days_of_week = days_of_week
        self.time = time
        self.relative = relative

        if not isinstance(self.date_time, ElementTagType | NoneType):
            raise TypeError("date_time is not of type ElementTagType")
        
        if not isinstance(self.month, ElementTagType | NoneType):
            raise TypeError("month is not of type ElementTagType")
        
        if not isinstance(self.day_of_month, ElementTagType | NoneType):
            raise TypeError("day_of_month is not of type ElementTagType")
        
        if not isinstance(self.calendar_week, ElementTagType | NoneType):
            raise TypeError("calendar_week is not of type ElementTagType")
        
        if not isinstance(self.day_of_week_occurrence, ElementTagType | NoneType):
            raise TypeError("day_of_week_occurrence is not of type ElementTagType")
        
        if not isinstance(self.days_of_week, ElementTagType | NoneType):
            raise TypeError("days_of_week is not of type ElementTagType")
        
        if not isinstance(self.time, ElementTagType | NoneType):
            raise TypeError("time is not of type ElementTagType")
        
        if not isinstance(self.relative, ElementTagType | NoneType):
            raise TypeError("relative is not of type ElementTagType")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.date_time is not None:
            msg_data.append({"dateTime": self.date_time.get_data()})
        if self.month is not None:
            msg_data.append({"month": self.month.get_data()})
        if self.day_of_month is not None:
            msg_data.append({"dayOfMonth": self.day_of_month.get_data()})
        if self.calendar_week is not None:
            msg_data.append({"calendarWeek": self.calendar_week.get_data()})
        if self.day_of_week_occurrence is not None:
            msg_data.append({"dayOfWeekOccurrence": self.day_of_week_occurrence.get_data()})
        if self.days_of_week is not None:
            msg_data.append({"daysOfWeek": self.days_of_week.get_data()})
        if self.time is not None:
            msg_data.append({"time": self.time.get_data()})
        if self.relative is not None:
            msg_data.append({"relative": self.relative.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.date_time is not None:
            result_str += f"{sep}dateTime: {self.date_time}"
            sep = ", "
        if self.month is not None:
            result_str += f"{sep}month: {self.month}"
            sep = ", "
        if self.day_of_month is not None:
            result_str += f"{sep}dayOfMonth: {self.day_of_month}"
            sep = ", "
        if self.calendar_week is not None:
            result_str += f"{sep}calendarWeek: {self.calendar_week}"
            sep = ", "
        if self.day_of_week_occurrence is not None:
            result_str += f"{sep}dayOfWeekOccurrence: {self.day_of_week_occurrence}"
            sep = ", "
        if self.days_of_week is not None:
            result_str += f"{sep}daysOfWeek: {self.days_of_week}"
            sep = ", "
        if self.time is not None:
            result_str += f"{sep}time: {self.time}"
            sep = ", "
        if self.relative is not None:
            result_str += f"{sep}relative: {self.relative}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                date_time=data_dict.get('dateTime'),
                month=data_dict.get('month'),
                day_of_month=data_dict.get('dayOfMonth'),
                calendar_week=data_dict.get('calendarWeek'),
                day_of_week_occurrence=data_dict.get('dayOfWeekOccurrence'),
                days_of_week=data_dict.get('daysOfWeek'),
                time=data_dict.get('time'),
                relative=data_dict.get('relative'),
            )
        elif data:
            return cls(data)
        else:
            return cls()



