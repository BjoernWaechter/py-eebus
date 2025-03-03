# Jinja Template message_type.py.jinja2
from spine.base_type.version import SpecificationVersionDataType
from types import NoneType
from spine import array_2_dict


class NodeManagementDetailedDiscoveryFeatureInformationType: # EEBus_SPINE_TS_NodeManagement.xsd:ns_p:NodeManagementDetailedDiscoveryFeatureInformationType -> ComplexType
    def __init__(
            self,
    ):
        super().__init__()
        

    def get_data(self):

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


class NodeManagementDetailedDiscoveryEntityInformationType: # EEBus_SPINE_TS_NodeManagement.xsd:ns_p:NodeManagementDetailedDiscoveryEntityInformationType -> ComplexType
    def __init__(
            self,
    ):
        super().__init__()
        

    def get_data(self):

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


class NodeManagementDetailedDiscoveryDeviceInformationType: # EEBus_SPINE_TS_NodeManagement.xsd:ns_p:NodeManagementDetailedDiscoveryDeviceInformationType -> ComplexType
    def __init__(
            self,
    ):
        super().__init__()
        

    def get_data(self):

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


class NodeManagementSpecificationVersionListType: # EEBus_SPINE_TS_NodeManagement.xsd:ns_p:NodeManagementSpecificationVersionListType -> ComplexType
    def __init__(
            self,
            specification_version: list[SpecificationVersionDataType] = None,
    ):
        super().__init__()
        
        self.specification_version = specification_version

        if not isinstance(self.specification_version, list | NoneType):
            raise TypeError("specification_version is not of type list[SpecificationVersionDataType]")
        
    def get_data(self):

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


class NodeManagementDestinationDataType: # EEBus_SPINE_TS_NodeManagement.xsd:ns_p:NodeManagementDestinationDataType -> ComplexType
    def __init__(
            self,
    ):
        super().__init__()
        

    def get_data(self):

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


class NodeManagementDetailedDiscoveryFeatureInformationElementsType: # EEBus_SPINE_TS_NodeManagement.xsd:ns_p:NodeManagementDetailedDiscoveryFeatureInformationElementsType -> ComplexType
    def __init__(
            self,
    ):
        super().__init__()
        

    def get_data(self):

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


class NodeManagementDetailedDiscoveryEntityInformationElementsType: # EEBus_SPINE_TS_NodeManagement.xsd:ns_p:NodeManagementDetailedDiscoveryEntityInformationElementsType -> ComplexType
    def __init__(
            self,
    ):
        super().__init__()
        

    def get_data(self):

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


class NodeManagementDetailedDiscoveryDeviceInformationElementsType: # EEBus_SPINE_TS_NodeManagement.xsd:ns_p:NodeManagementDetailedDiscoveryDeviceInformationElementsType -> ComplexType
    def __init__(
            self,
    ):
        super().__init__()
        

    def get_data(self):

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


class NodeManagementSpecificationVersionListElementsType: # EEBus_SPINE_TS_NodeManagement.xsd:ns_p:NodeManagementSpecificationVersionListElementsType -> ComplexType
    def __init__(
            self,
    ):
        super().__init__()
        

    def get_data(self):

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


class NodeManagementUseCaseDataType: # EEBus_SPINE_TS_NodeManagement.xsd:ns_p:NodeManagementUseCaseDataType -> ComplexType
    def __init__(
            self,
    ):
        super().__init__()
        

    def get_data(self):

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


class NodeManagementSubscriptionRequestCallType: # EEBus_SPINE_TS_NodeManagement.xsd:ns_p:NodeManagementSubscriptionRequestCallType -> ComplexType
    def __init__(
            self,
    ):
        super().__init__()
        

    def get_data(self):

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


class NodeManagementSubscriptionDeleteCallType: # EEBus_SPINE_TS_NodeManagement.xsd:ns_p:NodeManagementSubscriptionDeleteCallType -> ComplexType
    def __init__(
            self,
    ):
        super().__init__()
        

    def get_data(self):

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


class NodeManagementSubscriptionDataType: # EEBus_SPINE_TS_NodeManagement.xsd:ns_p:NodeManagementSubscriptionDataType -> ComplexType
    def __init__(
            self,
    ):
        super().__init__()
        

    def get_data(self):

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


class NodeManagementDetailedDiscoveryDataType: # EEBus_SPINE_TS_NodeManagement.xsd:ns_p:NodeManagementDetailedDiscoveryDataType -> ComplexType
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
        
    def get_data(self):

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


class NodeManagementDestinationListDataType: # EEBus_SPINE_TS_NodeManagement.xsd:ns_p:NodeManagementDestinationListDataType -> ComplexType
    def __init__(
            self,
            node_management_destination_data: list[NodeManagementDestinationDataType] = None,
    ):
        super().__init__()
        
        self.node_management_destination_data = node_management_destination_data

        if not isinstance(self.node_management_destination_data, list | NoneType):
            raise TypeError("node_management_destination_data is not of type list[NodeManagementDestinationDataType]")
        
    def get_data(self):

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


class NodeManagementBindingRequestCallType: # EEBus_SPINE_TS_NodeManagement.xsd:ns_p:NodeManagementBindingRequestCallType -> ComplexType
    def __init__(
            self,
    ):
        super().__init__()
        

    def get_data(self):

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


class NodeManagementBindingDeleteCallType: # EEBus_SPINE_TS_NodeManagement.xsd:ns_p:NodeManagementBindingDeleteCallType -> ComplexType
    def __init__(
            self,
    ):
        super().__init__()
        

    def get_data(self):

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


class NodeManagementBindingDataType: # EEBus_SPINE_TS_NodeManagement.xsd:ns_p:NodeManagementBindingDataType -> ComplexType
    def __init__(
            self,
    ):
        super().__init__()
        

    def get_data(self):

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


class NodeManagementUseCaseDataElementsType: # EEBus_SPINE_TS_NodeManagement.xsd:ns_p:NodeManagementUseCaseDataElementsType -> ComplexType
    def __init__(
            self,
    ):
        super().__init__()
        

    def get_data(self):

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


class NodeManagementSubscriptionRequestCallElementsType: # EEBus_SPINE_TS_NodeManagement.xsd:ns_p:NodeManagementSubscriptionRequestCallElementsType -> ComplexType
    def __init__(
            self,
    ):
        super().__init__()
        

    def get_data(self):

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


class NodeManagementSubscriptionDeleteCallElementsType: # EEBus_SPINE_TS_NodeManagement.xsd:ns_p:NodeManagementSubscriptionDeleteCallElementsType -> ComplexType
    def __init__(
            self,
    ):
        super().__init__()
        

    def get_data(self):

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


class NodeManagementSubscriptionDataElementsType: # EEBus_SPINE_TS_NodeManagement.xsd:ns_p:NodeManagementSubscriptionDataElementsType -> ComplexType
    def __init__(
            self,
    ):
        super().__init__()
        

    def get_data(self):

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


class NodeManagementDetailedDiscoveryDataElementsType: # EEBus_SPINE_TS_NodeManagement.xsd:ns_p:NodeManagementDetailedDiscoveryDataElementsType -> ComplexType
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
        
    def get_data(self):

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


class NodeManagementDestinationDataElementsType: # EEBus_SPINE_TS_NodeManagement.xsd:ns_p:NodeManagementDestinationDataElementsType -> ComplexType
    def __init__(
            self,
    ):
        super().__init__()
        

    def get_data(self):

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


class NodeManagementBindingRequestCallElementsType: # EEBus_SPINE_TS_NodeManagement.xsd:ns_p:NodeManagementBindingRequestCallElementsType -> ComplexType
    def __init__(
            self,
    ):
        super().__init__()
        

    def get_data(self):

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


class NodeManagementBindingDeleteCallElementsType: # EEBus_SPINE_TS_NodeManagement.xsd:ns_p:NodeManagementBindingDeleteCallElementsType -> ComplexType
    def __init__(
            self,
    ):
        super().__init__()
        

    def get_data(self):

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


class NodeManagementBindingDataElementsType: # EEBus_SPINE_TS_NodeManagement.xsd:ns_p:NodeManagementBindingDataElementsType -> ComplexType
    def __init__(
            self,
    ):
        super().__init__()
        

    def get_data(self):

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


class NodeManagementUseCaseDataSelectorsType: # EEBus_SPINE_TS_NodeManagement.xsd:ns_p:NodeManagementUseCaseDataSelectorsType -> ComplexType
    def __init__(
            self,
    ):
        super().__init__()
        

    def get_data(self):

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


class NodeManagementSubscriptionDataSelectorsType: # EEBus_SPINE_TS_NodeManagement.xsd:ns_p:NodeManagementSubscriptionDataSelectorsType -> ComplexType
    def __init__(
            self,
    ):
        super().__init__()
        

    def get_data(self):

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


class NodeManagementDetailedDiscoveryDataSelectorsType: # EEBus_SPINE_TS_NodeManagement.xsd:ns_p:NodeManagementDetailedDiscoveryDataSelectorsType -> ComplexType
    def __init__(
            self,
    ):
        super().__init__()
        

    def get_data(self):

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


class NodeManagementDestinationListDataSelectorsType: # EEBus_SPINE_TS_NodeManagement.xsd:ns_p:NodeManagementDestinationListDataSelectorsType -> ComplexType
    def __init__(
            self,
    ):
        super().__init__()
        

    def get_data(self):

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


class NodeManagementBindingDataSelectorsType: # EEBus_SPINE_TS_NodeManagement.xsd:ns_p:NodeManagementBindingDataSelectorsType -> ComplexType
    def __init__(
            self,
    ):
        super().__init__()
        

    def get_data(self):

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



