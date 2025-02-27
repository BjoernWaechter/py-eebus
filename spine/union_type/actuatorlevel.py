# Jinja Template message_type.py.jinja2
from types import NoneType
from spine import array_2_dict


class ActuatorLevelFctType:
    def __init__(
            self,
    ):
        super().__init__()
        

    def get_data(self): # UnionType

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



