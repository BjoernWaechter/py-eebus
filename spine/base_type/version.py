# Jinja Template message_type.py.jinja2
from spine.simple_type.commondatatypes import SpecificationVersionType
from types import NoneType
from spine import array_2_dict


class SpecificationVersionDataType:
    def __init__(
            self,
            value: str,
    ):
        super().__init__()
        
        self.value = value

        if not isinstance(self.value, str):
            raise TypeError("value is not of type str")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.value is not None:
            msg_data.append({"value": self.value})
        
        return msg_data


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


class SpecificationVersionListDataType:
    def __init__(
            self,
            specification_version_data: list[SpecificationVersionDataType] = None,
    ):
        super().__init__()
        
        self.specification_version_data = specification_version_data

        if not isinstance(self.specification_version_data, list | NoneType):
            raise TypeError("specification_version_data is not of type list[SpecificationVersionDataType]")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.specification_version_data is not None:
            msg_data.append({"specificationVersionData": [d.get_data() for d in self.specification_version_data]})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.specification_version_data is not None:
            result_str += f"{sep}specificationVersionData: {self.specification_version_data}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                specification_version_data=data_dict.get('specificationVersionData'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class SpecificationVersionListDataSelectorsType:
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


class SpecificationVersionDataElementsType:
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



