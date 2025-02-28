# Jinja Template message_type.py.jinja2
from spine.simple_type.commondatatypes import DescriptionType
from spine.simple_type.result import ErrorNumberType
from types import NoneType
from spine import array_2_dict


class ResultDataType: # EEBus_SPINE_TS_Result.xsd: ComplexType
    def __init__(
            self,
            error_number: ErrorNumberType = None,
            description: DescriptionType = None,
    ):
        super().__init__()
        
        self.error_number = error_number
        self.description = description

        if not isinstance(self.error_number, ErrorNumberType | NoneType):
            raise TypeError("error_number is not of type ErrorNumberType")
        
        if not isinstance(self.description, DescriptionType | NoneType):
            raise TypeError("description is not of type DescriptionType")
        
    def get_data(self):

        msg_data = []
        
        if self.error_number is not None:
            msg_data.append({"errorNumber": self.error_number.get_data()})
        if self.description is not None:
            msg_data.append({"description": self.description.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.error_number is not None:
            result_str += f"{sep}errorNumber: {self.error_number}"
            sep = ", "
        if self.description is not None:
            result_str += f"{sep}description: {self.description}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                error_number=data_dict.get('errorNumber'),
                description=data_dict.get('description'),
            )
        elif data:
            return cls(data)
        else:
            return cls()



