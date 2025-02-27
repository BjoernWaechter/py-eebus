# Jinja Template message_type.py.jinja2
from spine.base_type.version import SpecificationVersionDataType
from types import NoneType
from spine import array_2_dict


class NodeManagementDetailedDiscoveryFeatureInformationType:
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


class NodeManagementDetailedDiscoveryEntityInformationType:
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


class NodeManagementDetailedDiscoveryDeviceInformationType:
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


class NodeManagementSpecificationVersionListType:
    def __init__(
            self,
            specification_version: list[SpecificationVersionDataType] = None,
    ):
        super().__init__()
        
        self.specification_version = specification_version

        if not isinstance(self.specification_version, list | NoneType):
            raise TypeError("specification_version is not of type list[SpecificationVersionDataType]")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.specification_version is not None:
            msg_data.append({"specificationVersion": [d.get_data() for d in self.specification_version]})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.specification_version is not None:
            result_str += f"{sep}specificationVersion: {self.specification_version}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                specification_version=data_dict.get('specificationVersion'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class NodeManagementDetailedDiscoveryFeatureInformationElementsType:
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


class NodeManagementDetailedDiscoveryEntityInformationElementsType:
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


class NodeManagementDetailedDiscoveryDeviceInformationElementsType:
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


class NodeManagementSpecificationVersionListElementsType:
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


class NodeManagementDestinationDataType:
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


class NodeManagementUseCaseDataType:
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


class NodeManagementUseCaseDataSelectorsType:
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


class NodeManagementUseCaseDataElementsType:
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


class NodeManagementSubscriptionRequestCallType:
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


class NodeManagementSubscriptionRequestCallElementsType:
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


class NodeManagementSubscriptionDeleteCallType:
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


class NodeManagementSubscriptionDeleteCallElementsType:
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


class NodeManagementSubscriptionDataType:
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


class NodeManagementSubscriptionDataSelectorsType:
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


class NodeManagementSubscriptionDataElementsType:
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


class NodeManagementDetailedDiscoveryDataType:
    def __init__(
            self,
            specification_version_list: NodeManagementSpecificationVersionListType = None,
            device_information: NodeManagementDetailedDiscoveryDeviceInformationType = None,
            entity_information: list[NodeManagementDetailedDiscoveryEntityInformationType] = None,
            feature_information: list[NodeManagementDetailedDiscoveryFeatureInformationType] = None,
    ):
        super().__init__()
        
        self.specification_version_list = specification_version_list
        self.device_information = device_information
        self.entity_information = entity_information
        self.feature_information = feature_information

        if not isinstance(self.specification_version_list, NodeManagementSpecificationVersionListType | NoneType):
            raise TypeError("specification_version_list is not of type NodeManagementSpecificationVersionListType")
        
        if not isinstance(self.device_information, NodeManagementDetailedDiscoveryDeviceInformationType | NoneType):
            raise TypeError("device_information is not of type NodeManagementDetailedDiscoveryDeviceInformationType")
        
        if not isinstance(self.entity_information, list | NoneType):
            raise TypeError("entity_information is not of type list[NodeManagementDetailedDiscoveryEntityInformationType]")
        
        if not isinstance(self.feature_information, list | NoneType):
            raise TypeError("feature_information is not of type list[NodeManagementDetailedDiscoveryFeatureInformationType]")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.specification_version_list is not None:
            msg_data.append({"specificationVersionList": self.specification_version_list.get_data()})
        if self.device_information is not None:
            msg_data.append({"deviceInformation": self.device_information.get_data()})
        if self.entity_information is not None:
            msg_data.append({"entityInformation": [d.get_data() for d in self.entity_information]})
        if self.feature_information is not None:
            msg_data.append({"featureInformation": [d.get_data() for d in self.feature_information]})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.specification_version_list is not None:
            result_str += f"{sep}specificationVersionList: {self.specification_version_list}"
            sep = ", "
        if self.device_information is not None:
            result_str += f"{sep}deviceInformation: {self.device_information}"
            sep = ", "
        if self.entity_information is not None:
            result_str += f"{sep}entityInformation: {self.entity_information}"
            sep = ", "
        if self.feature_information is not None:
            result_str += f"{sep}featureInformation: {self.feature_information}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                specification_version_list=data_dict.get('specificationVersionList'),
                device_information=data_dict.get('deviceInformation'),
                entity_information=data_dict.get('entityInformation'),
                feature_information=data_dict.get('featureInformation'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class NodeManagementDetailedDiscoveryDataSelectorsType:
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


class NodeManagementDetailedDiscoveryDataElementsType:
    def __init__(
            self,
            specification_version_list: NodeManagementSpecificationVersionListElementsType = None,
            device_information: NodeManagementDetailedDiscoveryDeviceInformationElementsType = None,
            entity_information: NodeManagementDetailedDiscoveryEntityInformationElementsType = None,
            feature_information: NodeManagementDetailedDiscoveryFeatureInformationElementsType = None,
    ):
        super().__init__()
        
        self.specification_version_list = specification_version_list
        self.device_information = device_information
        self.entity_information = entity_information
        self.feature_information = feature_information

        if not isinstance(self.specification_version_list, NodeManagementSpecificationVersionListElementsType | NoneType):
            raise TypeError("specification_version_list is not of type NodeManagementSpecificationVersionListElementsType")
        
        if not isinstance(self.device_information, NodeManagementDetailedDiscoveryDeviceInformationElementsType | NoneType):
            raise TypeError("device_information is not of type NodeManagementDetailedDiscoveryDeviceInformationElementsType")
        
        if not isinstance(self.entity_information, NodeManagementDetailedDiscoveryEntityInformationElementsType | NoneType):
            raise TypeError("entity_information is not of type NodeManagementDetailedDiscoveryEntityInformationElementsType")
        
        if not isinstance(self.feature_information, NodeManagementDetailedDiscoveryFeatureInformationElementsType | NoneType):
            raise TypeError("feature_information is not of type NodeManagementDetailedDiscoveryFeatureInformationElementsType")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.specification_version_list is not None:
            msg_data.append({"specificationVersionList": self.specification_version_list.get_data()})
        if self.device_information is not None:
            msg_data.append({"deviceInformation": self.device_information.get_data()})
        if self.entity_information is not None:
            msg_data.append({"entityInformation": self.entity_information.get_data()})
        if self.feature_information is not None:
            msg_data.append({"featureInformation": self.feature_information.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.specification_version_list is not None:
            result_str += f"{sep}specificationVersionList: {self.specification_version_list}"
            sep = ", "
        if self.device_information is not None:
            result_str += f"{sep}deviceInformation: {self.device_information}"
            sep = ", "
        if self.entity_information is not None:
            result_str += f"{sep}entityInformation: {self.entity_information}"
            sep = ", "
        if self.feature_information is not None:
            result_str += f"{sep}featureInformation: {self.feature_information}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                specification_version_list=data_dict.get('specificationVersionList'),
                device_information=data_dict.get('deviceInformation'),
                entity_information=data_dict.get('entityInformation'),
                feature_information=data_dict.get('featureInformation'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class NodeManagementDestinationListDataType:
    def __init__(
            self,
            node_management_destination_data: list[NodeManagementDestinationDataType] = None,
    ):
        super().__init__()
        
        self.node_management_destination_data = node_management_destination_data

        if not isinstance(self.node_management_destination_data, list | NoneType):
            raise TypeError("node_management_destination_data is not of type list[NodeManagementDestinationDataType]")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.node_management_destination_data is not None:
            msg_data.append({"nodeManagementDestinationData": [d.get_data() for d in self.node_management_destination_data]})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.node_management_destination_data is not None:
            result_str += f"{sep}nodeManagementDestinationData: {self.node_management_destination_data}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                node_management_destination_data=data_dict.get('nodeManagementDestinationData'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class NodeManagementDestinationListDataSelectorsType:
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


class NodeManagementDestinationDataElementsType:
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


class NodeManagementBindingRequestCallType:
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


class NodeManagementBindingRequestCallElementsType:
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


class NodeManagementBindingDeleteCallType:
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


class NodeManagementBindingDeleteCallElementsType:
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


class NodeManagementBindingDataType:
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


class NodeManagementBindingDataSelectorsType:
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


class NodeManagementBindingDataElementsType:
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



