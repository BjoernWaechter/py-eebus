# Jinja Template message_type.py.jinja2
from types import NoneType
from spine import array_2_dict


class ChannelIdType: # EEBus_SPINE_TS_DataTunneling.xsd:ns_p:ChannelIdType -> AliasType
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


class PurposeIdType: # EEBus_SPINE_TS_DataTunneling.xsd:ns_p:PurposeIdType -> AliasType
    def __init__(
            self,
            value: str,
    ):
        super().__init__()
        
        self.value = value

        if not isinstance(self.value, str):
            raise TypeError("value is not of type str")
        
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



