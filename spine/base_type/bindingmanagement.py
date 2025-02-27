# Jinja Template message_type.py.jinja2
from spine.simple_type.bindingmanagement import BindingIdType
from spine.simple_type.commondatatypes import LabelType
from spine.simple_type.commondatatypes import DescriptionType
from spine.base_type.commondatatypes import ElementTagType
from spine.union_type.commondatatypes import FunctionType
from spine.base_type.commondatatypes import FeatureAddressType
from spine.base_type.commondatatypes import FeatureAddressElementsType
from types import NoneType
from spine import array_2_dict


class BindingManagementEntryDataType:
    def __init__(
            self,
            binding_id: BindingIdType = None,
            client_address: FeatureAddressType = None,
            server_address: FeatureAddressType = None,
            label: LabelType = None,
            description: DescriptionType = None,
    ):
        super().__init__()
        
        self.binding_id = binding_id
        self.client_address = client_address
        self.server_address = server_address
        self.label = label
        self.description = description

        if not isinstance(self.binding_id, BindingIdType | NoneType):
            raise TypeError("binding_id is not of type BindingIdType")
        
        if not isinstance(self.client_address, FeatureAddressType | NoneType):
            raise TypeError("client_address is not of type FeatureAddressType")
        
        if not isinstance(self.server_address, FeatureAddressType | NoneType):
            raise TypeError("server_address is not of type FeatureAddressType")
        
        if not isinstance(self.label, LabelType | NoneType):
            raise TypeError("label is not of type LabelType")
        
        if not isinstance(self.description, DescriptionType | NoneType):
            raise TypeError("description is not of type DescriptionType")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.binding_id is not None:
            msg_data.append({"bindingId": self.binding_id.get_data()})
        if self.client_address is not None:
            msg_data.append({"clientAddress": self.client_address.get_data()})
        if self.server_address is not None:
            msg_data.append({"serverAddress": self.server_address.get_data()})
        if self.label is not None:
            msg_data.append({"label": self.label.get_data()})
        if self.description is not None:
            msg_data.append({"description": self.description.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.binding_id is not None:
            result_str += f"{sep}bindingId: {self.binding_id}"
            sep = ", "
        if self.client_address is not None:
            result_str += f"{sep}clientAddress: {self.client_address}"
            sep = ", "
        if self.server_address is not None:
            result_str += f"{sep}serverAddress: {self.server_address}"
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
                binding_id=data_dict.get('bindingId'),
                client_address=data_dict.get('clientAddress'),
                server_address=data_dict.get('serverAddress'),
                label=data_dict.get('label'),
                description=data_dict.get('description'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class BindingManagementRequestCallType:
    def __init__(
            self,
            client_address: FeatureAddressType = None,
            server_address: FeatureAddressType = None,
            server_feature_type: FunctionType = None,
    ):
        super().__init__()
        
        self.client_address = client_address
        self.server_address = server_address
        self.server_feature_type = server_feature_type

        if not isinstance(self.client_address, FeatureAddressType | NoneType):
            raise TypeError("client_address is not of type FeatureAddressType")
        
        if not isinstance(self.server_address, FeatureAddressType | NoneType):
            raise TypeError("server_address is not of type FeatureAddressType")
        
        if not isinstance(self.server_feature_type, FunctionType | NoneType):
            raise TypeError("server_feature_type is not of type FunctionType")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.client_address is not None:
            msg_data.append({"clientAddress": self.client_address.get_data()})
        if self.server_address is not None:
            msg_data.append({"serverAddress": self.server_address.get_data()})
        if self.server_feature_type is not None:
            msg_data.append({"serverFeatureType": self.server_feature_type.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.client_address is not None:
            result_str += f"{sep}clientAddress: {self.client_address}"
            sep = ", "
        if self.server_address is not None:
            result_str += f"{sep}serverAddress: {self.server_address}"
            sep = ", "
        if self.server_feature_type is not None:
            result_str += f"{sep}serverFeatureType: {self.server_feature_type}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                client_address=data_dict.get('clientAddress'),
                server_address=data_dict.get('serverAddress'),
                server_feature_type=data_dict.get('serverFeatureType'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class BindingManagementRequestCallElementsType:
    def __init__(
            self,
            client_address: FeatureAddressElementsType = None,
            server_address: FeatureAddressElementsType = None,
            server_feature_type: ElementTagType = None,
    ):
        super().__init__()
        
        self.client_address = client_address
        self.server_address = server_address
        self.server_feature_type = server_feature_type

        if not isinstance(self.client_address, FeatureAddressElementsType | NoneType):
            raise TypeError("client_address is not of type FeatureAddressElementsType")
        
        if not isinstance(self.server_address, FeatureAddressElementsType | NoneType):
            raise TypeError("server_address is not of type FeatureAddressElementsType")
        
        if not isinstance(self.server_feature_type, ElementTagType | NoneType):
            raise TypeError("server_feature_type is not of type ElementTagType")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.client_address is not None:
            msg_data.append({"clientAddress": self.client_address.get_data()})
        if self.server_address is not None:
            msg_data.append({"serverAddress": self.server_address.get_data()})
        if self.server_feature_type is not None:
            msg_data.append({"serverFeatureType": self.server_feature_type.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.client_address is not None:
            result_str += f"{sep}clientAddress: {self.client_address}"
            sep = ", "
        if self.server_address is not None:
            result_str += f"{sep}serverAddress: {self.server_address}"
            sep = ", "
        if self.server_feature_type is not None:
            result_str += f"{sep}serverFeatureType: {self.server_feature_type}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                client_address=data_dict.get('clientAddress'),
                server_address=data_dict.get('serverAddress'),
                server_feature_type=data_dict.get('serverFeatureType'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class BindingManagementEntryListDataType:
    def __init__(
            self,
            binding_management_entry_data: list[BindingManagementEntryDataType] = None,
    ):
        super().__init__()
        
        self.binding_management_entry_data = binding_management_entry_data

        if not isinstance(self.binding_management_entry_data, list | NoneType):
            raise TypeError("binding_management_entry_data is not of type list[BindingManagementEntryDataType]")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.binding_management_entry_data is not None:
            msg_data.append({"bindingManagementEntryData": [d.get_data() for d in self.binding_management_entry_data]})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.binding_management_entry_data is not None:
            result_str += f"{sep}bindingManagementEntryData: {self.binding_management_entry_data}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                binding_management_entry_data=data_dict.get('bindingManagementEntryData'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class BindingManagementEntryListDataSelectorsType:
    def __init__(
            self,
            binding_id: BindingIdType = None,
            client_address: FeatureAddressType = None,
            server_address: FeatureAddressType = None,
    ):
        super().__init__()
        
        self.binding_id = binding_id
        self.client_address = client_address
        self.server_address = server_address

        if not isinstance(self.binding_id, BindingIdType | NoneType):
            raise TypeError("binding_id is not of type BindingIdType")
        
        if not isinstance(self.client_address, FeatureAddressType | NoneType):
            raise TypeError("client_address is not of type FeatureAddressType")
        
        if not isinstance(self.server_address, FeatureAddressType | NoneType):
            raise TypeError("server_address is not of type FeatureAddressType")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.binding_id is not None:
            msg_data.append({"bindingId": self.binding_id.get_data()})
        if self.client_address is not None:
            msg_data.append({"clientAddress": self.client_address.get_data()})
        if self.server_address is not None:
            msg_data.append({"serverAddress": self.server_address.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.binding_id is not None:
            result_str += f"{sep}bindingId: {self.binding_id}"
            sep = ", "
        if self.client_address is not None:
            result_str += f"{sep}clientAddress: {self.client_address}"
            sep = ", "
        if self.server_address is not None:
            result_str += f"{sep}serverAddress: {self.server_address}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                binding_id=data_dict.get('bindingId'),
                client_address=data_dict.get('clientAddress'),
                server_address=data_dict.get('serverAddress'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class BindingManagementEntryDataElementsType:
    def __init__(
            self,
            binding_id: ElementTagType = None,
            client_address: FeatureAddressElementsType = None,
            server_address: FeatureAddressElementsType = None,
            label: ElementTagType = None,
            description: ElementTagType = None,
    ):
        super().__init__()
        
        self.binding_id = binding_id
        self.client_address = client_address
        self.server_address = server_address
        self.label = label
        self.description = description

        if not isinstance(self.binding_id, ElementTagType | NoneType):
            raise TypeError("binding_id is not of type ElementTagType")
        
        if not isinstance(self.client_address, FeatureAddressElementsType | NoneType):
            raise TypeError("client_address is not of type FeatureAddressElementsType")
        
        if not isinstance(self.server_address, FeatureAddressElementsType | NoneType):
            raise TypeError("server_address is not of type FeatureAddressElementsType")
        
        if not isinstance(self.label, ElementTagType | NoneType):
            raise TypeError("label is not of type ElementTagType")
        
        if not isinstance(self.description, ElementTagType | NoneType):
            raise TypeError("description is not of type ElementTagType")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.binding_id is not None:
            msg_data.append({"bindingId": self.binding_id.get_data()})
        if self.client_address is not None:
            msg_data.append({"clientAddress": self.client_address.get_data()})
        if self.server_address is not None:
            msg_data.append({"serverAddress": self.server_address.get_data()})
        if self.label is not None:
            msg_data.append({"label": self.label.get_data()})
        if self.description is not None:
            msg_data.append({"description": self.description.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.binding_id is not None:
            result_str += f"{sep}bindingId: {self.binding_id}"
            sep = ", "
        if self.client_address is not None:
            result_str += f"{sep}clientAddress: {self.client_address}"
            sep = ", "
        if self.server_address is not None:
            result_str += f"{sep}serverAddress: {self.server_address}"
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
                binding_id=data_dict.get('bindingId'),
                client_address=data_dict.get('clientAddress'),
                server_address=data_dict.get('serverAddress'),
                label=data_dict.get('label'),
                description=data_dict.get('description'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class BindingManagementDeleteCallType:
    def __init__(
            self,
            binding_id: BindingIdType = None,
            client_address: FeatureAddressType = None,
            server_address: FeatureAddressType = None,
    ):
        super().__init__()
        
        self.binding_id = binding_id
        self.client_address = client_address
        self.server_address = server_address

        if not isinstance(self.binding_id, BindingIdType | NoneType):
            raise TypeError("binding_id is not of type BindingIdType")
        
        if not isinstance(self.client_address, FeatureAddressType | NoneType):
            raise TypeError("client_address is not of type FeatureAddressType")
        
        if not isinstance(self.server_address, FeatureAddressType | NoneType):
            raise TypeError("server_address is not of type FeatureAddressType")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.binding_id is not None:
            msg_data.append({"bindingId": self.binding_id.get_data()})
        if self.client_address is not None:
            msg_data.append({"clientAddress": self.client_address.get_data()})
        if self.server_address is not None:
            msg_data.append({"serverAddress": self.server_address.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.binding_id is not None:
            result_str += f"{sep}bindingId: {self.binding_id}"
            sep = ", "
        if self.client_address is not None:
            result_str += f"{sep}clientAddress: {self.client_address}"
            sep = ", "
        if self.server_address is not None:
            result_str += f"{sep}serverAddress: {self.server_address}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                binding_id=data_dict.get('bindingId'),
                client_address=data_dict.get('clientAddress'),
                server_address=data_dict.get('serverAddress'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class BindingManagementDeleteCallElementsType:
    def __init__(
            self,
            binding_id: ElementTagType = None,
            client_address: FeatureAddressElementsType = None,
            server_address: FeatureAddressElementsType = None,
    ):
        super().__init__()
        
        self.binding_id = binding_id
        self.client_address = client_address
        self.server_address = server_address

        if not isinstance(self.binding_id, ElementTagType | NoneType):
            raise TypeError("binding_id is not of type ElementTagType")
        
        if not isinstance(self.client_address, FeatureAddressElementsType | NoneType):
            raise TypeError("client_address is not of type FeatureAddressElementsType")
        
        if not isinstance(self.server_address, FeatureAddressElementsType | NoneType):
            raise TypeError("server_address is not of type FeatureAddressElementsType")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.binding_id is not None:
            msg_data.append({"bindingId": self.binding_id.get_data()})
        if self.client_address is not None:
            msg_data.append({"clientAddress": self.client_address.get_data()})
        if self.server_address is not None:
            msg_data.append({"serverAddress": self.server_address.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.binding_id is not None:
            result_str += f"{sep}bindingId: {self.binding_id}"
            sep = ", "
        if self.client_address is not None:
            result_str += f"{sep}clientAddress: {self.client_address}"
            sep = ", "
        if self.server_address is not None:
            result_str += f"{sep}serverAddress: {self.server_address}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                binding_id=data_dict.get('bindingId'),
                client_address=data_dict.get('clientAddress'),
                server_address=data_dict.get('serverAddress'),
            )
        elif data:
            return cls(data)
        else:
            return cls()



