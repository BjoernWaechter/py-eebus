# Jinja Template message_type.py.jinja2
from types import NoneType
from spine import array_2_dict


class HvacSystemFunctionIdType: # EEBus_SPINE_TS_HVAC.xsd:ns_p:HvacSystemFunctionIdType -> AliasType
    def __init__(
            self,
            value: int,
    ):
        super().__init__()
        
        self.value = value

        if not isinstance(self.value, int):
            raise TypeError("value is not of type int")
        
    def get_data(self):

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


class HvacOverrunIdType: # EEBus_SPINE_TS_HVAC.xsd:ns_p:HvacOverrunIdType -> AliasType
    def __init__(
            self,
            value: int,
    ):
        super().__init__()
        
        self.value = value

        if not isinstance(self.value, int):
            raise TypeError("value is not of type int")
        
    def get_data(self):

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


class HvacOperationModeIdType: # EEBus_SPINE_TS_HVAC.xsd:ns_p:HvacOperationModeIdType -> AliasType
    def __init__(
            self,
            value: int,
    ):
        super().__init__()
        
        self.value = value

        if not isinstance(self.value, int):
            raise TypeError("value is not of type int")
        
    def get_data(self):

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



