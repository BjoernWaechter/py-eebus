# Jinja Template message_type.py.jinja2
from types import NoneType
from spine import array_2_dict


class SpecificationVersionType:
    def __init__(
            self,
            value: str,
    ):
        super().__init__()
        
        self.value = value

        if not isinstance(self.value, str):
            raise TypeError("value is not of type str")
        
    def get_data(self): # AliasType

        return self.value


    def __str__(self):
        result_str = ""
        sep = ""
        if self.value is not None:
            result_str += f"{sep}value: {self.value}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                value=data_dict.get('value'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class ScaleType:
    def __init__(
            self,
            value: int,
    ):
        super().__init__()
        
        self.value = value

        if not isinstance(self.value, int):
            raise TypeError("value is not of type int")
        
    def get_data(self): # AliasType

        return self.value


    def __str__(self):
        result_str = ""
        sep = ""
        if self.value is not None:
            result_str += f"{sep}value: {self.value}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                value=data_dict.get('value'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class NumberType:
    def __init__(
            self,
            value: int,
    ):
        super().__init__()
        
        self.value = value

        if not isinstance(self.value, int):
            raise TypeError("value is not of type int")
        
    def get_data(self): # AliasType

        return self.value


    def __str__(self):
        result_str = ""
        sep = ""
        if self.value is not None:
            result_str += f"{sep}value: {self.value}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                value=data_dict.get('value'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class MaxResponseDelayType:
    def __init__(
            self,
            value: str,
    ):
        super().__init__()
        
        self.value = value

        if not isinstance(self.value, str):
            raise TypeError("value is not of type str")
        
    def get_data(self): # AliasType

        return self.value


    def __str__(self):
        result_str = ""
        sep = ""
        if self.value is not None:
            result_str += f"{sep}value: {self.value}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                value=data_dict.get('value'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class LabelType:
    def __init__(
            self,
            value: str,
    ):
        super().__init__()
        
        self.value = value

        if not isinstance(self.value, str):
            raise TypeError("value is not of type str")
        
    def get_data(self): # AliasType

        return self.value


    def __str__(self):
        result_str = ""
        sep = ""
        if self.value is not None:
            result_str += f"{sep}value: {self.value}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                value=data_dict.get('value'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class FeatureGroupType:
    def __init__(
            self,
            value: str,
    ):
        super().__init__()
        
        self.value = value

        if not isinstance(self.value, str):
            raise TypeError("value is not of type str")
        
    def get_data(self): # AliasType

        return self.value


    def __str__(self):
        result_str = ""
        sep = ""
        if self.value is not None:
            result_str += f"{sep}value: {self.value}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                value=data_dict.get('value'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class DescriptionType:
    def __init__(
            self,
            value: str,
    ):
        super().__init__()
        
        self.value = value

        if not isinstance(self.value, str):
            raise TypeError("value is not of type str")
        
    def get_data(self): # AliasType

        return self.value


    def __str__(self):
        result_str = ""
        sep = ""
        if self.value is not None:
            result_str += f"{sep}value: {self.value}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                value=data_dict.get('value'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class DayOfMonthType:
    def __init__(
            self,
            value: int,
    ):
        super().__init__()
        
        self.value = value

        if not isinstance(self.value, int):
            raise TypeError("value is not of type int")
        
    def get_data(self): # AliasType

        return self.value


    def __str__(self):
        result_str = ""
        sep = ""
        if self.value is not None:
            result_str += f"{sep}value: {self.value}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                value=data_dict.get('value'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class CalendarWeekType:
    def __init__(
            self,
            value: int,
    ):
        super().__init__()
        
        self.value = value

        if not isinstance(self.value, int):
            raise TypeError("value is not of type int")
        
    def get_data(self): # AliasType

        return self.value


    def __str__(self):
        result_str = ""
        sep = ""
        if self.value is not None:
            result_str += f"{sep}value: {self.value}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                value=data_dict.get('value'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class AddressFeatureType:
    def __init__(
            self,
            value: int,
    ):
        super().__init__()
        
        self.value = value

        if not isinstance(self.value, int):
            raise TypeError("value is not of type int")
        
    def get_data(self): # AliasType

        return self.value


    def __str__(self):
        result_str = ""
        sep = ""
        if self.value is not None:
            result_str += f"{sep}value: {self.value}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                value=data_dict.get('value'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class AddressEntityType:
    def __init__(
            self,
            value: int,
    ):
        super().__init__()
        
        self.value = value

        if not isinstance(self.value, int):
            raise TypeError("value is not of type int")
        
    def get_data(self): # AliasType

        return self.value


    def __str__(self):
        result_str = ""
        sep = ""
        if self.value is not None:
            result_str += f"{sep}value: {self.value}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                value=data_dict.get('value'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class AddressDeviceType:
    def __init__(
            self,
            value: str,
    ):
        super().__init__()
        
        self.value = value

        if not isinstance(self.value, str):
            raise TypeError("value is not of type str")
        
    def get_data(self): # AliasType

        return self.value


    def __str__(self):
        result_str = ""
        sep = ""
        if self.value is not None:
            result_str += f"{sep}value: {self.value}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                value=data_dict.get('value'),
            )
        elif data:
            return cls(data)
        else:
            return cls()



