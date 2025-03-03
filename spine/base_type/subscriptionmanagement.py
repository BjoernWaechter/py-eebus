# Jinja Template message_type.py.jinja2
from spine.base_type.commondatatypes import ElementTagType
from spine.base_type.commondatatypes import FeatureAddressElementsType
from spine.base_type.commondatatypes import FeatureAddressType
from spine.simple_type.commondatatypes import DescriptionType
from spine.simple_type.commondatatypes import LabelType
from spine.simple_type.subscriptionmanagement import SubscriptionIdType
from spine.union_type.commondatatypes import FeatureTypeType
from types import NoneType
from spine import array_2_dict


class SubscriptionManagementEntryDataType: # EEBus_SPINE_TS_SubscriptionManagement.xsd:ns_p:SubscriptionManagementEntryDataType -> ComplexType
    def __init__(
            self,
            subscription_id: SubscriptionIdType = None,
            client_address: FeatureAddressType = None,
            server_address: FeatureAddressType = None,
            label: LabelType = None,
            description: DescriptionType = None,
    ):
        super().__init__()
        
        self.subscription_id = subscription_id
        self.client_address = client_address
        self.server_address = server_address
        self.label = label
        self.description = description

        if not isinstance(self.subscription_id, SubscriptionIdType | NoneType):
            raise TypeError("subscription_id is not of type SubscriptionIdType")
        
        if not isinstance(self.client_address, FeatureAddressType | NoneType):
            raise TypeError("client_address is not of type FeatureAddressType")
        
        if not isinstance(self.server_address, FeatureAddressType | NoneType):
            raise TypeError("server_address is not of type FeatureAddressType")
        
        if not isinstance(self.label, LabelType | NoneType):
            raise TypeError("label is not of type LabelType")
        
        if not isinstance(self.description, DescriptionType | NoneType):
            raise TypeError("description is not of type DescriptionType")
        
    def get_data(self):

        msg_data = []
        
        if self.subscription_id is not None:
            msg_data.append({"subscriptionId": self.subscription_id.get_data()})
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
        if self.subscription_id is not None:
            result_str += f"{sep}subscriptionId: {self.subscription_id}"
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
                subscription_id=data_dict.get('subscriptionId'),
                client_address=data_dict.get('clientAddress'),
                server_address=data_dict.get('serverAddress'),
                label=data_dict.get('label'),
                description=data_dict.get('description'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class SubscriptionManagementRequestCallType: # EEBus_SPINE_TS_SubscriptionManagement.xsd:ns_p:SubscriptionManagementRequestCallType -> ComplexType
    def __init__(
            self,
            client_address: FeatureAddressType = None,
            server_address: FeatureAddressType = None,
            server_feature_type: FeatureTypeType = None,
    ):
        super().__init__()
        
        self.client_address = client_address
        self.server_address = server_address
        self.server_feature_type = server_feature_type

        if not isinstance(self.client_address, FeatureAddressType | NoneType):
            raise TypeError("client_address is not of type FeatureAddressType")
        
        if not isinstance(self.server_address, FeatureAddressType | NoneType):
            raise TypeError("server_address is not of type FeatureAddressType")
        
        if not isinstance(self.server_feature_type, FeatureTypeType | NoneType):
            raise TypeError("server_feature_type is not of type FeatureTypeType")
        
    def get_data(self):

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


class SubscriptionManagementEntryListDataType: # EEBus_SPINE_TS_SubscriptionManagement.xsd:ns_p:SubscriptionManagementEntryListDataType -> ComplexType
    def __init__(
            self,
            subscription_management_entry_data: list[SubscriptionManagementEntryDataType] = None,
    ):
        super().__init__()
        
        self.subscription_management_entry_data = subscription_management_entry_data

        if not isinstance(self.subscription_management_entry_data, list | NoneType):
            raise TypeError("subscription_management_entry_data is not of type list[SubscriptionManagementEntryDataType]")
        
    def get_data(self):

        msg_data = []
        
        if self.subscription_management_entry_data is not None:
            msg_data.append({"subscriptionManagementEntryData": [d.get_data() for d in self.subscription_management_entry_data]})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.subscription_management_entry_data is not None:
            result_str += f"{sep}subscriptionManagementEntryData: {self.subscription_management_entry_data}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                subscription_management_entry_data=data_dict.get('subscriptionManagementEntryData'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class SubscriptionManagementDeleteCallType: # EEBus_SPINE_TS_SubscriptionManagement.xsd:ns_p:SubscriptionManagementDeleteCallType -> ComplexType
    def __init__(
            self,
            subscription_id: SubscriptionIdType = None,
            client_address: FeatureAddressType = None,
            server_address: FeatureAddressType = None,
    ):
        super().__init__()
        
        self.subscription_id = subscription_id
        self.client_address = client_address
        self.server_address = server_address

        if not isinstance(self.subscription_id, SubscriptionIdType | NoneType):
            raise TypeError("subscription_id is not of type SubscriptionIdType")
        
        if not isinstance(self.client_address, FeatureAddressType | NoneType):
            raise TypeError("client_address is not of type FeatureAddressType")
        
        if not isinstance(self.server_address, FeatureAddressType | NoneType):
            raise TypeError("server_address is not of type FeatureAddressType")
        
    def get_data(self):

        msg_data = []
        
        if self.subscription_id is not None:
            msg_data.append({"subscriptionId": self.subscription_id.get_data()})
        if self.client_address is not None:
            msg_data.append({"clientAddress": self.client_address.get_data()})
        if self.server_address is not None:
            msg_data.append({"serverAddress": self.server_address.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.subscription_id is not None:
            result_str += f"{sep}subscriptionId: {self.subscription_id}"
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
                subscription_id=data_dict.get('subscriptionId'),
                client_address=data_dict.get('clientAddress'),
                server_address=data_dict.get('serverAddress'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class SubscriptionManagementRequestCallElementsType: # EEBus_SPINE_TS_SubscriptionManagement.xsd:ns_p:SubscriptionManagementRequestCallElementsType -> ComplexType
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
        
    def get_data(self):

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


class SubscriptionManagementEntryDataElementsType: # EEBus_SPINE_TS_SubscriptionManagement.xsd:ns_p:SubscriptionManagementEntryDataElementsType -> ComplexType
    def __init__(
            self,
            subscription_id: ElementTagType = None,
            client_address: FeatureAddressElementsType = None,
            server_address: FeatureAddressElementsType = None,
            label: ElementTagType = None,
            description: ElementTagType = None,
    ):
        super().__init__()
        
        self.subscription_id = subscription_id
        self.client_address = client_address
        self.server_address = server_address
        self.label = label
        self.description = description

        if not isinstance(self.subscription_id, ElementTagType | NoneType):
            raise TypeError("subscription_id is not of type ElementTagType")
        
        if not isinstance(self.client_address, FeatureAddressElementsType | NoneType):
            raise TypeError("client_address is not of type FeatureAddressElementsType")
        
        if not isinstance(self.server_address, FeatureAddressElementsType | NoneType):
            raise TypeError("server_address is not of type FeatureAddressElementsType")
        
        if not isinstance(self.label, ElementTagType | NoneType):
            raise TypeError("label is not of type ElementTagType")
        
        if not isinstance(self.description, ElementTagType | NoneType):
            raise TypeError("description is not of type ElementTagType")
        
    def get_data(self):

        msg_data = []
        
        if self.subscription_id is not None:
            msg_data.append({"subscriptionId": self.subscription_id.get_data()})
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
        if self.subscription_id is not None:
            result_str += f"{sep}subscriptionId: {self.subscription_id}"
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
                subscription_id=data_dict.get('subscriptionId'),
                client_address=data_dict.get('clientAddress'),
                server_address=data_dict.get('serverAddress'),
                label=data_dict.get('label'),
                description=data_dict.get('description'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class SubscriptionManagementDeleteCallElementsType: # EEBus_SPINE_TS_SubscriptionManagement.xsd:ns_p:SubscriptionManagementDeleteCallElementsType -> ComplexType
    def __init__(
            self,
            subscription_id: ElementTagType = None,
            client_address: FeatureAddressElementsType = None,
            server_address: FeatureAddressElementsType = None,
    ):
        super().__init__()
        
        self.subscription_id = subscription_id
        self.client_address = client_address
        self.server_address = server_address

        if not isinstance(self.subscription_id, ElementTagType | NoneType):
            raise TypeError("subscription_id is not of type ElementTagType")
        
        if not isinstance(self.client_address, FeatureAddressElementsType | NoneType):
            raise TypeError("client_address is not of type FeatureAddressElementsType")
        
        if not isinstance(self.server_address, FeatureAddressElementsType | NoneType):
            raise TypeError("server_address is not of type FeatureAddressElementsType")
        
    def get_data(self):

        msg_data = []
        
        if self.subscription_id is not None:
            msg_data.append({"subscriptionId": self.subscription_id.get_data()})
        if self.client_address is not None:
            msg_data.append({"clientAddress": self.client_address.get_data()})
        if self.server_address is not None:
            msg_data.append({"serverAddress": self.server_address.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.subscription_id is not None:
            result_str += f"{sep}subscriptionId: {self.subscription_id}"
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
                subscription_id=data_dict.get('subscriptionId'),
                client_address=data_dict.get('clientAddress'),
                server_address=data_dict.get('serverAddress'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class SubscriptionManagementEntryListDataSelectorsType: # EEBus_SPINE_TS_SubscriptionManagement.xsd:ns_p:SubscriptionManagementEntryListDataSelectorsType -> ComplexType
    def __init__(
            self,
            subscription_id: SubscriptionIdType = None,
            client_address: FeatureAddressType = None,
            server_address: FeatureAddressType = None,
    ):
        super().__init__()
        
        self.subscription_id = subscription_id
        self.client_address = client_address
        self.server_address = server_address

        if not isinstance(self.subscription_id, SubscriptionIdType | NoneType):
            raise TypeError("subscription_id is not of type SubscriptionIdType")
        
        if not isinstance(self.client_address, FeatureAddressType | NoneType):
            raise TypeError("client_address is not of type FeatureAddressType")
        
        if not isinstance(self.server_address, FeatureAddressType | NoneType):
            raise TypeError("server_address is not of type FeatureAddressType")
        
    def get_data(self):

        msg_data = []
        
        if self.subscription_id is not None:
            msg_data.append({"subscriptionId": self.subscription_id.get_data()})
        if self.client_address is not None:
            msg_data.append({"clientAddress": self.client_address.get_data()})
        if self.server_address is not None:
            msg_data.append({"serverAddress": self.server_address.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.subscription_id is not None:
            result_str += f"{sep}subscriptionId: {self.subscription_id}"
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
                subscription_id=data_dict.get('subscriptionId'),
                client_address=data_dict.get('clientAddress'),
                server_address=data_dict.get('serverAddress'),
            )
        elif data:
            return cls(data)
        else:
            return cls()



