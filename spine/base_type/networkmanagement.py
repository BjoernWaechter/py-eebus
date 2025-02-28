# Jinja Template message_type.py.jinja2
from spine.base_type.commondatatypes import DeviceAddressElementsType
from spine.base_type.commondatatypes import DeviceAddressType
from spine.base_type.commondatatypes import ElementTagType
from spine.base_type.commondatatypes import EntityAddressElementsType
from spine.base_type.commondatatypes import EntityAddressType
from spine.base_type.commondatatypes import FeatureAddressElementsType
from spine.base_type.commondatatypes import FeatureAddressType
from spine.base_type.commondatatypes import FunctionPropertyElementsType
from spine.base_type.commondatatypes import FunctionPropertyType
from spine.enums.commondatatypes import RoleType
from spine.enums.networkmanagement import NetworkManagementFeatureSetType
from spine.enums.networkmanagement import NetworkManagementProcessStateStateType
from spine.enums.networkmanagement import NetworkManagementStateChangeType
from spine.simple_type.commondatatypes import DescriptionType
from spine.simple_type.commondatatypes import FeatureGroupType
from spine.simple_type.commondatatypes import LabelType
from spine.simple_type.commondatatypes import MaxResponseDelayType
from spine.simple_type.networkmanagement import NetworkManagementCandidateSetupType
from spine.simple_type.networkmanagement import NetworkManagementCommunicationsTechnologyInformationType
from spine.simple_type.networkmanagement import NetworkManagementMinimumTrustLevelType
from spine.simple_type.networkmanagement import NetworkManagementNativeSetupType
from spine.simple_type.networkmanagement import NetworkManagementProcessTimeoutType
from spine.simple_type.networkmanagement import NetworkManagementScanSetupType
from spine.simple_type.networkmanagement import NetworkManagementSetupType
from spine.simple_type.networkmanagement import NetworkManagementTechnologyAddressType
from spine.union_type.commondatatypes import DeviceTypeType
from spine.union_type.commondatatypes import EntityTypeType
from spine.union_type.commondatatypes import FeatureSpecificUsageType
from spine.union_type.commondatatypes import FeatureTypeType
from types import NoneType
from spine import array_2_dict


class NetworkManagementFeatureDescriptionDataType: # EEBus_SPINE_TS_NetworkManagement.xsd: ComplexType
    def __init__(
            self,
            feature_address: FeatureAddressType = None,
            feature_type: FeatureTypeType = None,
            specific_usage: list[FeatureSpecificUsageType] = None,
            feature_group: FeatureGroupType = None,
            role: RoleType = None,
            supported_function: list[FunctionPropertyType] = None,
            last_state_change: NetworkManagementStateChangeType = None,
            minimum_trust_level: NetworkManagementMinimumTrustLevelType = None,
            label: LabelType = None,
            description: DescriptionType = None,
            max_response_delay: MaxResponseDelayType = None,
    ):
        super().__init__()
        
        self.feature_address = feature_address
        self.feature_type = feature_type
        self.specific_usage = specific_usage
        self.feature_group = feature_group
        self.role = role
        self.supported_function = supported_function
        self.last_state_change = last_state_change
        self.minimum_trust_level = minimum_trust_level
        self.label = label
        self.description = description
        self.max_response_delay = max_response_delay

        if not isinstance(self.feature_address, FeatureAddressType | NoneType):
            raise TypeError("feature_address is not of type FeatureAddressType")
        
        if not isinstance(self.feature_type, FeatureTypeType | NoneType):
            raise TypeError("feature_type is not of type FeatureTypeType")
        
        if not isinstance(self.specific_usage, list | NoneType):
            raise TypeError("specific_usage is not of type list[FeatureSpecificUsageType]")
        
        if not isinstance(self.feature_group, FeatureGroupType | NoneType):
            raise TypeError("feature_group is not of type FeatureGroupType")
        
        if not isinstance(self.role, RoleType | NoneType):
            raise TypeError("role is not of type RoleType")
        
        if not isinstance(self.supported_function, list | NoneType):
            raise TypeError("supported_function is not of type list[FunctionPropertyType]")
        
        if not isinstance(self.last_state_change, NetworkManagementStateChangeType | NoneType):
            raise TypeError("last_state_change is not of type NetworkManagementStateChangeType")
        
        if not isinstance(self.minimum_trust_level, NetworkManagementMinimumTrustLevelType | NoneType):
            raise TypeError("minimum_trust_level is not of type NetworkManagementMinimumTrustLevelType")
        
        if not isinstance(self.label, LabelType | NoneType):
            raise TypeError("label is not of type LabelType")
        
        if not isinstance(self.description, DescriptionType | NoneType):
            raise TypeError("description is not of type DescriptionType")
        
        if not isinstance(self.max_response_delay, MaxResponseDelayType | NoneType):
            raise TypeError("max_response_delay is not of type MaxResponseDelayType")
        
    def get_data(self):

        msg_data = []
        
        if self.feature_address is not None:
            msg_data.append({"featureAddress": self.feature_address.get_data()})
        if self.feature_type is not None:
            msg_data.append({"featureType": self.feature_type.get_data()})
        if self.specific_usage is not None:
            msg_data.append({"specificUsage": [d.get_data() for d in self.specific_usage]})
        if self.feature_group is not None:
            msg_data.append({"featureGroup": self.feature_group.get_data()})
        if self.role is not None:
            msg_data.append({"role": self.role.value})
        if self.supported_function is not None:
            msg_data.append({"supportedFunction": [d.get_data() for d in self.supported_function]})
        if self.last_state_change is not None:
            msg_data.append({"lastStateChange": self.last_state_change.value})
        if self.minimum_trust_level is not None:
            msg_data.append({"minimumTrustLevel": self.minimum_trust_level.get_data()})
        if self.label is not None:
            msg_data.append({"label": self.label.get_data()})
        if self.description is not None:
            msg_data.append({"description": self.description.get_data()})
        if self.max_response_delay is not None:
            msg_data.append({"maxResponseDelay": self.max_response_delay.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.feature_address is not None:
            result_str += f"{sep}featureAddress: {self.feature_address}"
            sep = ", "
        if self.feature_type is not None:
            result_str += f"{sep}featureType: {self.feature_type}"
            sep = ", "
        if self.specific_usage is not None:
            result_str += f"{sep}specificUsage: {self.specific_usage}"
            sep = ", "
        if self.feature_group is not None:
            result_str += f"{sep}featureGroup: {self.feature_group}"
            sep = ", "
        if self.role is not None:
            result_str += f"{sep}role: {self.role}"
            sep = ", "
        if self.supported_function is not None:
            result_str += f"{sep}supportedFunction: {self.supported_function}"
            sep = ", "
        if self.last_state_change is not None:
            result_str += f"{sep}lastStateChange: {self.last_state_change}"
            sep = ", "
        if self.minimum_trust_level is not None:
            result_str += f"{sep}minimumTrustLevel: {self.minimum_trust_level}"
            sep = ", "
        if self.label is not None:
            result_str += f"{sep}label: {self.label}"
            sep = ", "
        if self.description is not None:
            result_str += f"{sep}description: {self.description}"
            sep = ", "
        if self.max_response_delay is not None:
            result_str += f"{sep}maxResponseDelay: {self.max_response_delay}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                feature_address=data_dict.get('featureAddress'),
                feature_type=data_dict.get('featureType'),
                specific_usage=data_dict.get('specificUsage'),
                feature_group=data_dict.get('featureGroup'),
                role=data_dict.get('role'),
                supported_function=data_dict.get('supportedFunction'),
                last_state_change=data_dict.get('lastStateChange'),
                minimum_trust_level=data_dict.get('minimumTrustLevel'),
                label=data_dict.get('label'),
                description=data_dict.get('description'),
                max_response_delay=data_dict.get('maxResponseDelay'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class NetworkManagementEntityDescriptionDataType: # EEBus_SPINE_TS_NetworkManagement.xsd: ComplexType
    def __init__(
            self,
            entity_address: EntityAddressType = None,
            entity_type: EntityTypeType = None,
            last_state_change: NetworkManagementStateChangeType = None,
            minimum_trust_level: NetworkManagementMinimumTrustLevelType = None,
            label: LabelType = None,
            description: DescriptionType = None,
    ):
        super().__init__()
        
        self.entity_address = entity_address
        self.entity_type = entity_type
        self.last_state_change = last_state_change
        self.minimum_trust_level = minimum_trust_level
        self.label = label
        self.description = description

        if not isinstance(self.entity_address, EntityAddressType | NoneType):
            raise TypeError("entity_address is not of type EntityAddressType")
        
        if not isinstance(self.entity_type, EntityTypeType | NoneType):
            raise TypeError("entity_type is not of type EntityTypeType")
        
        if not isinstance(self.last_state_change, NetworkManagementStateChangeType | NoneType):
            raise TypeError("last_state_change is not of type NetworkManagementStateChangeType")
        
        if not isinstance(self.minimum_trust_level, NetworkManagementMinimumTrustLevelType | NoneType):
            raise TypeError("minimum_trust_level is not of type NetworkManagementMinimumTrustLevelType")
        
        if not isinstance(self.label, LabelType | NoneType):
            raise TypeError("label is not of type LabelType")
        
        if not isinstance(self.description, DescriptionType | NoneType):
            raise TypeError("description is not of type DescriptionType")
        
    def get_data(self):

        msg_data = []
        
        if self.entity_address is not None:
            msg_data.append({"entityAddress": self.entity_address.get_data()})
        if self.entity_type is not None:
            msg_data.append({"entityType": self.entity_type.get_data()})
        if self.last_state_change is not None:
            msg_data.append({"lastStateChange": self.last_state_change.value})
        if self.minimum_trust_level is not None:
            msg_data.append({"minimumTrustLevel": self.minimum_trust_level.get_data()})
        if self.label is not None:
            msg_data.append({"label": self.label.get_data()})
        if self.description is not None:
            msg_data.append({"description": self.description.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.entity_address is not None:
            result_str += f"{sep}entityAddress: {self.entity_address}"
            sep = ", "
        if self.entity_type is not None:
            result_str += f"{sep}entityType: {self.entity_type}"
            sep = ", "
        if self.last_state_change is not None:
            result_str += f"{sep}lastStateChange: {self.last_state_change}"
            sep = ", "
        if self.minimum_trust_level is not None:
            result_str += f"{sep}minimumTrustLevel: {self.minimum_trust_level}"
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
                entity_address=data_dict.get('entityAddress'),
                entity_type=data_dict.get('entityType'),
                last_state_change=data_dict.get('lastStateChange'),
                minimum_trust_level=data_dict.get('minimumTrustLevel'),
                label=data_dict.get('label'),
                description=data_dict.get('description'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class NetworkManagementDeviceDescriptionDataType: # EEBus_SPINE_TS_NetworkManagement.xsd: ComplexType
    def __init__(
            self,
            device_address: DeviceAddressType = None,
            device_type: DeviceTypeType = None,
            network_management_responsible_address: FeatureAddressType = None,
            native_setup: NetworkManagementNativeSetupType = None,
            technology_address: NetworkManagementTechnologyAddressType = None,
            communications_technology_information: NetworkManagementCommunicationsTechnologyInformationType = None,
            network_feature_set: NetworkManagementFeatureSetType = None,
            last_state_change: NetworkManagementStateChangeType = None,
            minimum_trust_level: NetworkManagementMinimumTrustLevelType = None,
            label: LabelType = None,
            description: DescriptionType = None,
    ):
        super().__init__()
        
        self.device_address = device_address
        self.device_type = device_type
        self.network_management_responsible_address = network_management_responsible_address
        self.native_setup = native_setup
        self.technology_address = technology_address
        self.communications_technology_information = communications_technology_information
        self.network_feature_set = network_feature_set
        self.last_state_change = last_state_change
        self.minimum_trust_level = minimum_trust_level
        self.label = label
        self.description = description

        if not isinstance(self.device_address, DeviceAddressType | NoneType):
            raise TypeError("device_address is not of type DeviceAddressType")
        
        if not isinstance(self.device_type, DeviceTypeType | NoneType):
            raise TypeError("device_type is not of type DeviceTypeType")
        
        if not isinstance(self.network_management_responsible_address, FeatureAddressType | NoneType):
            raise TypeError("network_management_responsible_address is not of type FeatureAddressType")
        
        if not isinstance(self.native_setup, NetworkManagementNativeSetupType | NoneType):
            raise TypeError("native_setup is not of type NetworkManagementNativeSetupType")
        
        if not isinstance(self.technology_address, NetworkManagementTechnologyAddressType | NoneType):
            raise TypeError("technology_address is not of type NetworkManagementTechnologyAddressType")
        
        if not isinstance(self.communications_technology_information, NetworkManagementCommunicationsTechnologyInformationType | NoneType):
            raise TypeError("communications_technology_information is not of type NetworkManagementCommunicationsTechnologyInformationType")
        
        if not isinstance(self.network_feature_set, NetworkManagementFeatureSetType | NoneType):
            raise TypeError("network_feature_set is not of type NetworkManagementFeatureSetType")
        
        if not isinstance(self.last_state_change, NetworkManagementStateChangeType | NoneType):
            raise TypeError("last_state_change is not of type NetworkManagementStateChangeType")
        
        if not isinstance(self.minimum_trust_level, NetworkManagementMinimumTrustLevelType | NoneType):
            raise TypeError("minimum_trust_level is not of type NetworkManagementMinimumTrustLevelType")
        
        if not isinstance(self.label, LabelType | NoneType):
            raise TypeError("label is not of type LabelType")
        
        if not isinstance(self.description, DescriptionType | NoneType):
            raise TypeError("description is not of type DescriptionType")
        
    def get_data(self):

        msg_data = []
        
        if self.device_address is not None:
            msg_data.append({"deviceAddress": self.device_address.get_data()})
        if self.device_type is not None:
            msg_data.append({"deviceType": self.device_type.get_data()})
        if self.network_management_responsible_address is not None:
            msg_data.append({"networkManagementResponsibleAddress": self.network_management_responsible_address.get_data()})
        if self.native_setup is not None:
            msg_data.append({"nativeSetup": self.native_setup.get_data()})
        if self.technology_address is not None:
            msg_data.append({"technologyAddress": self.technology_address.get_data()})
        if self.communications_technology_information is not None:
            msg_data.append({"communicationsTechnologyInformation": self.communications_technology_information.get_data()})
        if self.network_feature_set is not None:
            msg_data.append({"networkFeatureSet": self.network_feature_set.value})
        if self.last_state_change is not None:
            msg_data.append({"lastStateChange": self.last_state_change.value})
        if self.minimum_trust_level is not None:
            msg_data.append({"minimumTrustLevel": self.minimum_trust_level.get_data()})
        if self.label is not None:
            msg_data.append({"label": self.label.get_data()})
        if self.description is not None:
            msg_data.append({"description": self.description.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.device_address is not None:
            result_str += f"{sep}deviceAddress: {self.device_address}"
            sep = ", "
        if self.device_type is not None:
            result_str += f"{sep}deviceType: {self.device_type}"
            sep = ", "
        if self.network_management_responsible_address is not None:
            result_str += f"{sep}networkManagementResponsibleAddress: {self.network_management_responsible_address}"
            sep = ", "
        if self.native_setup is not None:
            result_str += f"{sep}nativeSetup: {self.native_setup}"
            sep = ", "
        if self.technology_address is not None:
            result_str += f"{sep}technologyAddress: {self.technology_address}"
            sep = ", "
        if self.communications_technology_information is not None:
            result_str += f"{sep}communicationsTechnologyInformation: {self.communications_technology_information}"
            sep = ", "
        if self.network_feature_set is not None:
            result_str += f"{sep}networkFeatureSet: {self.network_feature_set}"
            sep = ", "
        if self.last_state_change is not None:
            result_str += f"{sep}lastStateChange: {self.last_state_change}"
            sep = ", "
        if self.minimum_trust_level is not None:
            result_str += f"{sep}minimumTrustLevel: {self.minimum_trust_level}"
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
                device_address=data_dict.get('deviceAddress'),
                device_type=data_dict.get('deviceType'),
                network_management_responsible_address=data_dict.get('networkManagementResponsibleAddress'),
                native_setup=data_dict.get('nativeSetup'),
                technology_address=data_dict.get('technologyAddress'),
                communications_technology_information=data_dict.get('communicationsTechnologyInformation'),
                network_feature_set=data_dict.get('networkFeatureSet'),
                last_state_change=data_dict.get('lastStateChange'),
                minimum_trust_level=data_dict.get('minimumTrustLevel'),
                label=data_dict.get('label'),
                description=data_dict.get('description'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class NetworkManagementFeatureDescriptionListDataType: # EEBus_SPINE_TS_NetworkManagement.xsd: ComplexType
    def __init__(
            self,
            network_management_feature_description_data: list[NetworkManagementFeatureDescriptionDataType] = None,
    ):
        super().__init__()
        
        self.network_management_feature_description_data = network_management_feature_description_data

        if not isinstance(self.network_management_feature_description_data, list | NoneType):
            raise TypeError("network_management_feature_description_data is not of type list[NetworkManagementFeatureDescriptionDataType]")
        
    def get_data(self):

        msg_data = []
        
        if self.network_management_feature_description_data is not None:
            msg_data.append({"networkManagementFeatureDescriptionData": [d.get_data() for d in self.network_management_feature_description_data]})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.network_management_feature_description_data is not None:
            result_str += f"{sep}networkManagementFeatureDescriptionData: {self.network_management_feature_description_data}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                network_management_feature_description_data=data_dict.get('networkManagementFeatureDescriptionData'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class NetworkManagementEntityDescriptionListDataType: # EEBus_SPINE_TS_NetworkManagement.xsd: ComplexType
    def __init__(
            self,
            network_management_entity_description_data: list[NetworkManagementEntityDescriptionDataType] = None,
    ):
        super().__init__()
        
        self.network_management_entity_description_data = network_management_entity_description_data

        if not isinstance(self.network_management_entity_description_data, list | NoneType):
            raise TypeError("network_management_entity_description_data is not of type list[NetworkManagementEntityDescriptionDataType]")
        
    def get_data(self):

        msg_data = []
        
        if self.network_management_entity_description_data is not None:
            msg_data.append({"networkManagementEntityDescriptionData": [d.get_data() for d in self.network_management_entity_description_data]})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.network_management_entity_description_data is not None:
            result_str += f"{sep}networkManagementEntityDescriptionData: {self.network_management_entity_description_data}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                network_management_entity_description_data=data_dict.get('networkManagementEntityDescriptionData'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class NetworkManagementDeviceDescriptionListDataType: # EEBus_SPINE_TS_NetworkManagement.xsd: ComplexType
    def __init__(
            self,
            network_management_device_description_data: list[NetworkManagementDeviceDescriptionDataType] = None,
    ):
        super().__init__()
        
        self.network_management_device_description_data = network_management_device_description_data

        if not isinstance(self.network_management_device_description_data, list | NoneType):
            raise TypeError("network_management_device_description_data is not of type list[NetworkManagementDeviceDescriptionDataType]")
        
    def get_data(self):

        msg_data = []
        
        if self.network_management_device_description_data is not None:
            msg_data.append({"networkManagementDeviceDescriptionData": [d.get_data() for d in self.network_management_device_description_data]})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.network_management_device_description_data is not None:
            result_str += f"{sep}networkManagementDeviceDescriptionData: {self.network_management_device_description_data}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                network_management_device_description_data=data_dict.get('networkManagementDeviceDescriptionData'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class NetworkManagementReportCandidateDataType: # EEBus_SPINE_TS_NetworkManagement.xsd: ComplexType
    def __init__(
            self,
            candidate_setup: NetworkManagementCandidateSetupType = None,
            setup_usable_for_add: bool = None,
            label: LabelType = None,
            description: DescriptionType = None,
    ):
        super().__init__()
        
        self.candidate_setup = candidate_setup
        self.setup_usable_for_add = setup_usable_for_add
        self.label = label
        self.description = description

        if not isinstance(self.candidate_setup, NetworkManagementCandidateSetupType | NoneType):
            raise TypeError("candidate_setup is not of type NetworkManagementCandidateSetupType")
        
        if not isinstance(self.setup_usable_for_add, bool | NoneType):
            raise TypeError("setup_usable_for_add is not of type bool")
        
        if not isinstance(self.label, LabelType | NoneType):
            raise TypeError("label is not of type LabelType")
        
        if not isinstance(self.description, DescriptionType | NoneType):
            raise TypeError("description is not of type DescriptionType")
        
    def get_data(self):

        msg_data = []
        
        if self.candidate_setup is not None:
            msg_data.append({"candidateSetup": self.candidate_setup.get_data()})
        if self.setup_usable_for_add is not None:
            msg_data.append({"setupUsableForAdd": self.setup_usable_for_add})
        if self.label is not None:
            msg_data.append({"label": self.label.get_data()})
        if self.description is not None:
            msg_data.append({"description": self.description.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.candidate_setup is not None:
            result_str += f"{sep}candidateSetup: {self.candidate_setup}"
            sep = ", "
        if self.setup_usable_for_add is not None:
            result_str += f"{sep}setupUsableForAdd: {self.setup_usable_for_add}"
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
                candidate_setup=data_dict.get('candidateSetup'),
                setup_usable_for_add=data_dict.get('setupUsableForAdd'),
                label=data_dict.get('label'),
                description=data_dict.get('description'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class NetworkManagementJoiningModeDataType: # EEBus_SPINE_TS_NetworkManagement.xsd: ComplexType
    def __init__(
            self,
            setup: NetworkManagementSetupType = None,
    ):
        super().__init__()
        
        self.setup = setup

        if not isinstance(self.setup, NetworkManagementSetupType | NoneType):
            raise TypeError("setup is not of type NetworkManagementSetupType")
        
    def get_data(self):

        msg_data = []
        
        if self.setup is not None:
            msg_data.append({"setup": self.setup.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.setup is not None:
            result_str += f"{sep}setup: {self.setup}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                setup=data_dict.get('setup'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class NetworkManagementProcessStateDataType: # EEBus_SPINE_TS_NetworkManagement.xsd: ComplexType
    def __init__(
            self,
            state: NetworkManagementProcessStateStateType = None,
            description: DescriptionType = None,
    ):
        super().__init__()
        
        self.state = state
        self.description = description

        if not isinstance(self.state, NetworkManagementProcessStateStateType | NoneType):
            raise TypeError("state is not of type NetworkManagementProcessStateStateType")
        
        if not isinstance(self.description, DescriptionType | NoneType):
            raise TypeError("description is not of type DescriptionType")
        
    def get_data(self):

        msg_data = []
        
        if self.state is not None:
            msg_data.append({"state": self.state.value})
        if self.description is not None:
            msg_data.append({"description": self.description.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.state is not None:
            result_str += f"{sep}state: {self.state}"
            sep = ", "
        if self.description is not None:
            result_str += f"{sep}description: {self.description}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                state=data_dict.get('state'),
                description=data_dict.get('description'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class NetworkManagementAbortCallType: # EEBus_SPINE_TS_NetworkManagement.xsd: ComplexType
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


class NetworkManagementDiscoverCallType: # EEBus_SPINE_TS_NetworkManagement.xsd: ComplexType
    def __init__(
            self,
            discover_address: FeatureAddressType = None,
    ):
        super().__init__()
        
        self.discover_address = discover_address

        if not isinstance(self.discover_address, FeatureAddressType | NoneType):
            raise TypeError("discover_address is not of type FeatureAddressType")
        
    def get_data(self):

        msg_data = []
        
        if self.discover_address is not None:
            msg_data.append({"discoverAddress": self.discover_address.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.discover_address is not None:
            result_str += f"{sep}discoverAddress: {self.discover_address}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                discover_address=data_dict.get('discoverAddress'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class NetworkManagementScanNetworkCallType: # EEBus_SPINE_TS_NetworkManagement.xsd: ComplexType
    def __init__(
            self,
            scan_setup: NetworkManagementScanSetupType = None,
            timeout: NetworkManagementProcessTimeoutType = None,
    ):
        super().__init__()
        
        self.scan_setup = scan_setup
        self.timeout = timeout

        if not isinstance(self.scan_setup, NetworkManagementScanSetupType | NoneType):
            raise TypeError("scan_setup is not of type NetworkManagementScanSetupType")
        
        if not isinstance(self.timeout, NetworkManagementProcessTimeoutType | NoneType):
            raise TypeError("timeout is not of type NetworkManagementProcessTimeoutType")
        
    def get_data(self):

        msg_data = []
        
        if self.scan_setup is not None:
            msg_data.append({"scanSetup": self.scan_setup.get_data()})
        if self.timeout is not None:
            msg_data.append({"timeout": self.timeout.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.scan_setup is not None:
            result_str += f"{sep}scanSetup: {self.scan_setup}"
            sep = ", "
        if self.timeout is not None:
            result_str += f"{sep}timeout: {self.timeout}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                scan_setup=data_dict.get('scanSetup'),
                timeout=data_dict.get('timeout'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class NetworkManagementModifyNodeCallType: # EEBus_SPINE_TS_NetworkManagement.xsd: ComplexType
    def __init__(
            self,
            node_address: FeatureAddressType = None,
            native_setup: NetworkManagementNativeSetupType = None,
            timeout: NetworkManagementProcessTimeoutType = None,
            label: LabelType = None,
            description: DescriptionType = None,
    ):
        super().__init__()
        
        self.node_address = node_address
        self.native_setup = native_setup
        self.timeout = timeout
        self.label = label
        self.description = description

        if not isinstance(self.node_address, FeatureAddressType | NoneType):
            raise TypeError("node_address is not of type FeatureAddressType")
        
        if not isinstance(self.native_setup, NetworkManagementNativeSetupType | NoneType):
            raise TypeError("native_setup is not of type NetworkManagementNativeSetupType")
        
        if not isinstance(self.timeout, NetworkManagementProcessTimeoutType | NoneType):
            raise TypeError("timeout is not of type NetworkManagementProcessTimeoutType")
        
        if not isinstance(self.label, LabelType | NoneType):
            raise TypeError("label is not of type LabelType")
        
        if not isinstance(self.description, DescriptionType | NoneType):
            raise TypeError("description is not of type DescriptionType")
        
    def get_data(self):

        msg_data = []
        
        if self.node_address is not None:
            msg_data.append({"nodeAddress": self.node_address.get_data()})
        if self.native_setup is not None:
            msg_data.append({"nativeSetup": self.native_setup.get_data()})
        if self.timeout is not None:
            msg_data.append({"timeout": self.timeout.get_data()})
        if self.label is not None:
            msg_data.append({"label": self.label.get_data()})
        if self.description is not None:
            msg_data.append({"description": self.description.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.node_address is not None:
            result_str += f"{sep}nodeAddress: {self.node_address}"
            sep = ", "
        if self.native_setup is not None:
            result_str += f"{sep}nativeSetup: {self.native_setup}"
            sep = ", "
        if self.timeout is not None:
            result_str += f"{sep}timeout: {self.timeout}"
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
                node_address=data_dict.get('nodeAddress'),
                native_setup=data_dict.get('nativeSetup'),
                timeout=data_dict.get('timeout'),
                label=data_dict.get('label'),
                description=data_dict.get('description'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class NetworkManagementRemoveNodeCallType: # EEBus_SPINE_TS_NetworkManagement.xsd: ComplexType
    def __init__(
            self,
            node_address: FeatureAddressType = None,
            timeout: NetworkManagementProcessTimeoutType = None,
    ):
        super().__init__()
        
        self.node_address = node_address
        self.timeout = timeout

        if not isinstance(self.node_address, FeatureAddressType | NoneType):
            raise TypeError("node_address is not of type FeatureAddressType")
        
        if not isinstance(self.timeout, NetworkManagementProcessTimeoutType | NoneType):
            raise TypeError("timeout is not of type NetworkManagementProcessTimeoutType")
        
    def get_data(self):

        msg_data = []
        
        if self.node_address is not None:
            msg_data.append({"nodeAddress": self.node_address.get_data()})
        if self.timeout is not None:
            msg_data.append({"timeout": self.timeout.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.node_address is not None:
            result_str += f"{sep}nodeAddress: {self.node_address}"
            sep = ", "
        if self.timeout is not None:
            result_str += f"{sep}timeout: {self.timeout}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                node_address=data_dict.get('nodeAddress'),
                timeout=data_dict.get('timeout'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class NetworkManagementAddNodeCallType: # EEBus_SPINE_TS_NetworkManagement.xsd: ComplexType
    def __init__(
            self,
            node_address: FeatureAddressType = None,
            native_setup: NetworkManagementNativeSetupType = None,
            timeout: NetworkManagementProcessTimeoutType = None,
            label: LabelType = None,
            description: DescriptionType = None,
    ):
        super().__init__()
        
        self.node_address = node_address
        self.native_setup = native_setup
        self.timeout = timeout
        self.label = label
        self.description = description

        if not isinstance(self.node_address, FeatureAddressType | NoneType):
            raise TypeError("node_address is not of type FeatureAddressType")
        
        if not isinstance(self.native_setup, NetworkManagementNativeSetupType | NoneType):
            raise TypeError("native_setup is not of type NetworkManagementNativeSetupType")
        
        if not isinstance(self.timeout, NetworkManagementProcessTimeoutType | NoneType):
            raise TypeError("timeout is not of type NetworkManagementProcessTimeoutType")
        
        if not isinstance(self.label, LabelType | NoneType):
            raise TypeError("label is not of type LabelType")
        
        if not isinstance(self.description, DescriptionType | NoneType):
            raise TypeError("description is not of type DescriptionType")
        
    def get_data(self):

        msg_data = []
        
        if self.node_address is not None:
            msg_data.append({"nodeAddress": self.node_address.get_data()})
        if self.native_setup is not None:
            msg_data.append({"nativeSetup": self.native_setup.get_data()})
        if self.timeout is not None:
            msg_data.append({"timeout": self.timeout.get_data()})
        if self.label is not None:
            msg_data.append({"label": self.label.get_data()})
        if self.description is not None:
            msg_data.append({"description": self.description.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.node_address is not None:
            result_str += f"{sep}nodeAddress: {self.node_address}"
            sep = ", "
        if self.native_setup is not None:
            result_str += f"{sep}nativeSetup: {self.native_setup}"
            sep = ", "
        if self.timeout is not None:
            result_str += f"{sep}timeout: {self.timeout}"
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
                node_address=data_dict.get('nodeAddress'),
                native_setup=data_dict.get('nativeSetup'),
                timeout=data_dict.get('timeout'),
                label=data_dict.get('label'),
                description=data_dict.get('description'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class NetworkManagementScanNetworkCallElementsType: # EEBus_SPINE_TS_NetworkManagement.xsd: ComplexType
    def __init__(
            self,
            scan_setup: ElementTagType = None,
            timeout: ElementTagType = None,
    ):
        super().__init__()
        
        self.scan_setup = scan_setup
        self.timeout = timeout

        if not isinstance(self.scan_setup, ElementTagType | NoneType):
            raise TypeError("scan_setup is not of type ElementTagType")
        
        if not isinstance(self.timeout, ElementTagType | NoneType):
            raise TypeError("timeout is not of type ElementTagType")
        
    def get_data(self):

        msg_data = []
        
        if self.scan_setup is not None:
            msg_data.append({"scanSetup": self.scan_setup.get_data()})
        if self.timeout is not None:
            msg_data.append({"timeout": self.timeout.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.scan_setup is not None:
            result_str += f"{sep}scanSetup: {self.scan_setup}"
            sep = ", "
        if self.timeout is not None:
            result_str += f"{sep}timeout: {self.timeout}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                scan_setup=data_dict.get('scanSetup'),
                timeout=data_dict.get('timeout'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class NetworkManagementReportCandidateDataElementsType: # EEBus_SPINE_TS_NetworkManagement.xsd: ComplexType
    def __init__(
            self,
            candidate_setup: ElementTagType = None,
            setup_usable_for_add: ElementTagType = None,
            label: ElementTagType = None,
            description: ElementTagType = None,
    ):
        super().__init__()
        
        self.candidate_setup = candidate_setup
        self.setup_usable_for_add = setup_usable_for_add
        self.label = label
        self.description = description

        if not isinstance(self.candidate_setup, ElementTagType | NoneType):
            raise TypeError("candidate_setup is not of type ElementTagType")
        
        if not isinstance(self.setup_usable_for_add, ElementTagType | NoneType):
            raise TypeError("setup_usable_for_add is not of type ElementTagType")
        
        if not isinstance(self.label, ElementTagType | NoneType):
            raise TypeError("label is not of type ElementTagType")
        
        if not isinstance(self.description, ElementTagType | NoneType):
            raise TypeError("description is not of type ElementTagType")
        
    def get_data(self):

        msg_data = []
        
        if self.candidate_setup is not None:
            msg_data.append({"candidateSetup": self.candidate_setup.get_data()})
        if self.setup_usable_for_add is not None:
            msg_data.append({"setupUsableForAdd": self.setup_usable_for_add.get_data()})
        if self.label is not None:
            msg_data.append({"label": self.label.get_data()})
        if self.description is not None:
            msg_data.append({"description": self.description.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.candidate_setup is not None:
            result_str += f"{sep}candidateSetup: {self.candidate_setup}"
            sep = ", "
        if self.setup_usable_for_add is not None:
            result_str += f"{sep}setupUsableForAdd: {self.setup_usable_for_add}"
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
                candidate_setup=data_dict.get('candidateSetup'),
                setup_usable_for_add=data_dict.get('setupUsableForAdd'),
                label=data_dict.get('label'),
                description=data_dict.get('description'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class NetworkManagementRemoveNodeCallElementsType: # EEBus_SPINE_TS_NetworkManagement.xsd: ComplexType
    def __init__(
            self,
            node_address: FeatureAddressElementsType = None,
            timeout: ElementTagType = None,
    ):
        super().__init__()
        
        self.node_address = node_address
        self.timeout = timeout

        if not isinstance(self.node_address, FeatureAddressElementsType | NoneType):
            raise TypeError("node_address is not of type FeatureAddressElementsType")
        
        if not isinstance(self.timeout, ElementTagType | NoneType):
            raise TypeError("timeout is not of type ElementTagType")
        
    def get_data(self):

        msg_data = []
        
        if self.node_address is not None:
            msg_data.append({"nodeAddress": self.node_address.get_data()})
        if self.timeout is not None:
            msg_data.append({"timeout": self.timeout.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.node_address is not None:
            result_str += f"{sep}nodeAddress: {self.node_address}"
            sep = ", "
        if self.timeout is not None:
            result_str += f"{sep}timeout: {self.timeout}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                node_address=data_dict.get('nodeAddress'),
                timeout=data_dict.get('timeout'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class NetworkManagementProcessStateDataElementsType: # EEBus_SPINE_TS_NetworkManagement.xsd: ComplexType
    def __init__(
            self,
            state: ElementTagType = None,
            description: ElementTagType = None,
    ):
        super().__init__()
        
        self.state = state
        self.description = description

        if not isinstance(self.state, ElementTagType | NoneType):
            raise TypeError("state is not of type ElementTagType")
        
        if not isinstance(self.description, ElementTagType | NoneType):
            raise TypeError("description is not of type ElementTagType")
        
    def get_data(self):

        msg_data = []
        
        if self.state is not None:
            msg_data.append({"state": self.state.get_data()})
        if self.description is not None:
            msg_data.append({"description": self.description.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.state is not None:
            result_str += f"{sep}state: {self.state}"
            sep = ", "
        if self.description is not None:
            result_str += f"{sep}description: {self.description}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                state=data_dict.get('state'),
                description=data_dict.get('description'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class NetworkManagementModifyNodeCallElementsType: # EEBus_SPINE_TS_NetworkManagement.xsd: ComplexType
    def __init__(
            self,
            node_address: FeatureAddressElementsType = None,
            native_setup: ElementTagType = None,
            timeout: ElementTagType = None,
            label: ElementTagType = None,
            description: ElementTagType = None,
    ):
        super().__init__()
        
        self.node_address = node_address
        self.native_setup = native_setup
        self.timeout = timeout
        self.label = label
        self.description = description

        if not isinstance(self.node_address, FeatureAddressElementsType | NoneType):
            raise TypeError("node_address is not of type FeatureAddressElementsType")
        
        if not isinstance(self.native_setup, ElementTagType | NoneType):
            raise TypeError("native_setup is not of type ElementTagType")
        
        if not isinstance(self.timeout, ElementTagType | NoneType):
            raise TypeError("timeout is not of type ElementTagType")
        
        if not isinstance(self.label, ElementTagType | NoneType):
            raise TypeError("label is not of type ElementTagType")
        
        if not isinstance(self.description, ElementTagType | NoneType):
            raise TypeError("description is not of type ElementTagType")
        
    def get_data(self):

        msg_data = []
        
        if self.node_address is not None:
            msg_data.append({"nodeAddress": self.node_address.get_data()})
        if self.native_setup is not None:
            msg_data.append({"nativeSetup": self.native_setup.get_data()})
        if self.timeout is not None:
            msg_data.append({"timeout": self.timeout.get_data()})
        if self.label is not None:
            msg_data.append({"label": self.label.get_data()})
        if self.description is not None:
            msg_data.append({"description": self.description.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.node_address is not None:
            result_str += f"{sep}nodeAddress: {self.node_address}"
            sep = ", "
        if self.native_setup is not None:
            result_str += f"{sep}nativeSetup: {self.native_setup}"
            sep = ", "
        if self.timeout is not None:
            result_str += f"{sep}timeout: {self.timeout}"
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
                node_address=data_dict.get('nodeAddress'),
                native_setup=data_dict.get('nativeSetup'),
                timeout=data_dict.get('timeout'),
                label=data_dict.get('label'),
                description=data_dict.get('description'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class NetworkManagementJoiningModeDataElementsType: # EEBus_SPINE_TS_NetworkManagement.xsd: ComplexType
    def __init__(
            self,
            setup: ElementTagType = None,
    ):
        super().__init__()
        
        self.setup = setup

        if not isinstance(self.setup, ElementTagType | NoneType):
            raise TypeError("setup is not of type ElementTagType")
        
    def get_data(self):

        msg_data = []
        
        if self.setup is not None:
            msg_data.append({"setup": self.setup.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.setup is not None:
            result_str += f"{sep}setup: {self.setup}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                setup=data_dict.get('setup'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class NetworkManagementFeatureDescriptionDataElementsType: # EEBus_SPINE_TS_NetworkManagement.xsd: ComplexType
    def __init__(
            self,
            feature_address: FeatureAddressElementsType = None,
            feature_type: ElementTagType = None,
            specific_usage: ElementTagType = None,
            feature_group: ElementTagType = None,
            role: ElementTagType = None,
            supported_function: FunctionPropertyElementsType = None,
            last_state_change: ElementTagType = None,
            minimum_trust_level: ElementTagType = None,
            label: ElementTagType = None,
            description: ElementTagType = None,
            max_response_delay: ElementTagType = None,
    ):
        super().__init__()
        
        self.feature_address = feature_address
        self.feature_type = feature_type
        self.specific_usage = specific_usage
        self.feature_group = feature_group
        self.role = role
        self.supported_function = supported_function
        self.last_state_change = last_state_change
        self.minimum_trust_level = minimum_trust_level
        self.label = label
        self.description = description
        self.max_response_delay = max_response_delay

        if not isinstance(self.feature_address, FeatureAddressElementsType | NoneType):
            raise TypeError("feature_address is not of type FeatureAddressElementsType")
        
        if not isinstance(self.feature_type, ElementTagType | NoneType):
            raise TypeError("feature_type is not of type ElementTagType")
        
        if not isinstance(self.specific_usage, ElementTagType | NoneType):
            raise TypeError("specific_usage is not of type ElementTagType")
        
        if not isinstance(self.feature_group, ElementTagType | NoneType):
            raise TypeError("feature_group is not of type ElementTagType")
        
        if not isinstance(self.role, ElementTagType | NoneType):
            raise TypeError("role is not of type ElementTagType")
        
        if not isinstance(self.supported_function, FunctionPropertyElementsType | NoneType):
            raise TypeError("supported_function is not of type FunctionPropertyElementsType")
        
        if not isinstance(self.last_state_change, ElementTagType | NoneType):
            raise TypeError("last_state_change is not of type ElementTagType")
        
        if not isinstance(self.minimum_trust_level, ElementTagType | NoneType):
            raise TypeError("minimum_trust_level is not of type ElementTagType")
        
        if not isinstance(self.label, ElementTagType | NoneType):
            raise TypeError("label is not of type ElementTagType")
        
        if not isinstance(self.description, ElementTagType | NoneType):
            raise TypeError("description is not of type ElementTagType")
        
        if not isinstance(self.max_response_delay, ElementTagType | NoneType):
            raise TypeError("max_response_delay is not of type ElementTagType")
        
    def get_data(self):

        msg_data = []
        
        if self.feature_address is not None:
            msg_data.append({"featureAddress": self.feature_address.get_data()})
        if self.feature_type is not None:
            msg_data.append({"featureType": self.feature_type.get_data()})
        if self.specific_usage is not None:
            msg_data.append({"specificUsage": self.specific_usage.get_data()})
        if self.feature_group is not None:
            msg_data.append({"featureGroup": self.feature_group.get_data()})
        if self.role is not None:
            msg_data.append({"role": self.role.get_data()})
        if self.supported_function is not None:
            msg_data.append({"supportedFunction": self.supported_function.get_data()})
        if self.last_state_change is not None:
            msg_data.append({"lastStateChange": self.last_state_change.get_data()})
        if self.minimum_trust_level is not None:
            msg_data.append({"minimumTrustLevel": self.minimum_trust_level.get_data()})
        if self.label is not None:
            msg_data.append({"label": self.label.get_data()})
        if self.description is not None:
            msg_data.append({"description": self.description.get_data()})
        if self.max_response_delay is not None:
            msg_data.append({"maxResponseDelay": self.max_response_delay.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.feature_address is not None:
            result_str += f"{sep}featureAddress: {self.feature_address}"
            sep = ", "
        if self.feature_type is not None:
            result_str += f"{sep}featureType: {self.feature_type}"
            sep = ", "
        if self.specific_usage is not None:
            result_str += f"{sep}specificUsage: {self.specific_usage}"
            sep = ", "
        if self.feature_group is not None:
            result_str += f"{sep}featureGroup: {self.feature_group}"
            sep = ", "
        if self.role is not None:
            result_str += f"{sep}role: {self.role}"
            sep = ", "
        if self.supported_function is not None:
            result_str += f"{sep}supportedFunction: {self.supported_function}"
            sep = ", "
        if self.last_state_change is not None:
            result_str += f"{sep}lastStateChange: {self.last_state_change}"
            sep = ", "
        if self.minimum_trust_level is not None:
            result_str += f"{sep}minimumTrustLevel: {self.minimum_trust_level}"
            sep = ", "
        if self.label is not None:
            result_str += f"{sep}label: {self.label}"
            sep = ", "
        if self.description is not None:
            result_str += f"{sep}description: {self.description}"
            sep = ", "
        if self.max_response_delay is not None:
            result_str += f"{sep}maxResponseDelay: {self.max_response_delay}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                feature_address=data_dict.get('featureAddress'),
                feature_type=data_dict.get('featureType'),
                specific_usage=data_dict.get('specificUsage'),
                feature_group=data_dict.get('featureGroup'),
                role=data_dict.get('role'),
                supported_function=data_dict.get('supportedFunction'),
                last_state_change=data_dict.get('lastStateChange'),
                minimum_trust_level=data_dict.get('minimumTrustLevel'),
                label=data_dict.get('label'),
                description=data_dict.get('description'),
                max_response_delay=data_dict.get('maxResponseDelay'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class NetworkManagementEntityDescriptionDataElementsType: # EEBus_SPINE_TS_NetworkManagement.xsd: ComplexType
    def __init__(
            self,
            entity_address: EntityAddressElementsType = None,
            entity_type: ElementTagType = None,
            last_state_change: ElementTagType = None,
            minimum_trust_level: ElementTagType = None,
            label: ElementTagType = None,
            description: ElementTagType = None,
    ):
        super().__init__()
        
        self.entity_address = entity_address
        self.entity_type = entity_type
        self.last_state_change = last_state_change
        self.minimum_trust_level = minimum_trust_level
        self.label = label
        self.description = description

        if not isinstance(self.entity_address, EntityAddressElementsType | NoneType):
            raise TypeError("entity_address is not of type EntityAddressElementsType")
        
        if not isinstance(self.entity_type, ElementTagType | NoneType):
            raise TypeError("entity_type is not of type ElementTagType")
        
        if not isinstance(self.last_state_change, ElementTagType | NoneType):
            raise TypeError("last_state_change is not of type ElementTagType")
        
        if not isinstance(self.minimum_trust_level, ElementTagType | NoneType):
            raise TypeError("minimum_trust_level is not of type ElementTagType")
        
        if not isinstance(self.label, ElementTagType | NoneType):
            raise TypeError("label is not of type ElementTagType")
        
        if not isinstance(self.description, ElementTagType | NoneType):
            raise TypeError("description is not of type ElementTagType")
        
    def get_data(self):

        msg_data = []
        
        if self.entity_address is not None:
            msg_data.append({"entityAddress": self.entity_address.get_data()})
        if self.entity_type is not None:
            msg_data.append({"entityType": self.entity_type.get_data()})
        if self.last_state_change is not None:
            msg_data.append({"lastStateChange": self.last_state_change.get_data()})
        if self.minimum_trust_level is not None:
            msg_data.append({"minimumTrustLevel": self.minimum_trust_level.get_data()})
        if self.label is not None:
            msg_data.append({"label": self.label.get_data()})
        if self.description is not None:
            msg_data.append({"description": self.description.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.entity_address is not None:
            result_str += f"{sep}entityAddress: {self.entity_address}"
            sep = ", "
        if self.entity_type is not None:
            result_str += f"{sep}entityType: {self.entity_type}"
            sep = ", "
        if self.last_state_change is not None:
            result_str += f"{sep}lastStateChange: {self.last_state_change}"
            sep = ", "
        if self.minimum_trust_level is not None:
            result_str += f"{sep}minimumTrustLevel: {self.minimum_trust_level}"
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
                entity_address=data_dict.get('entityAddress'),
                entity_type=data_dict.get('entityType'),
                last_state_change=data_dict.get('lastStateChange'),
                minimum_trust_level=data_dict.get('minimumTrustLevel'),
                label=data_dict.get('label'),
                description=data_dict.get('description'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class NetworkManagementDiscoverCallElementsType: # EEBus_SPINE_TS_NetworkManagement.xsd: ComplexType
    def __init__(
            self,
            discover_address: FeatureAddressElementsType = None,
    ):
        super().__init__()
        
        self.discover_address = discover_address

        if not isinstance(self.discover_address, FeatureAddressElementsType | NoneType):
            raise TypeError("discover_address is not of type FeatureAddressElementsType")
        
    def get_data(self):

        msg_data = []
        
        if self.discover_address is not None:
            msg_data.append({"discoverAddress": self.discover_address.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.discover_address is not None:
            result_str += f"{sep}discoverAddress: {self.discover_address}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                discover_address=data_dict.get('discoverAddress'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class NetworkManagementDeviceDescriptionDataElementsType: # EEBus_SPINE_TS_NetworkManagement.xsd: ComplexType
    def __init__(
            self,
            device_address: DeviceAddressElementsType = None,
            device_type: ElementTagType = None,
            network_management_responsible_address: ElementTagType = None,
            native_setup: ElementTagType = None,
            technology_address: ElementTagType = None,
            communications_technology_information: ElementTagType = None,
            network_feature_set: ElementTagType = None,
            last_state_change: ElementTagType = None,
            minimum_trust_level: ElementTagType = None,
            label: ElementTagType = None,
            description: ElementTagType = None,
    ):
        super().__init__()
        
        self.device_address = device_address
        self.device_type = device_type
        self.network_management_responsible_address = network_management_responsible_address
        self.native_setup = native_setup
        self.technology_address = technology_address
        self.communications_technology_information = communications_technology_information
        self.network_feature_set = network_feature_set
        self.last_state_change = last_state_change
        self.minimum_trust_level = minimum_trust_level
        self.label = label
        self.description = description

        if not isinstance(self.device_address, DeviceAddressElementsType | NoneType):
            raise TypeError("device_address is not of type DeviceAddressElementsType")
        
        if not isinstance(self.device_type, ElementTagType | NoneType):
            raise TypeError("device_type is not of type ElementTagType")
        
        if not isinstance(self.network_management_responsible_address, ElementTagType | NoneType):
            raise TypeError("network_management_responsible_address is not of type ElementTagType")
        
        if not isinstance(self.native_setup, ElementTagType | NoneType):
            raise TypeError("native_setup is not of type ElementTagType")
        
        if not isinstance(self.technology_address, ElementTagType | NoneType):
            raise TypeError("technology_address is not of type ElementTagType")
        
        if not isinstance(self.communications_technology_information, ElementTagType | NoneType):
            raise TypeError("communications_technology_information is not of type ElementTagType")
        
        if not isinstance(self.network_feature_set, ElementTagType | NoneType):
            raise TypeError("network_feature_set is not of type ElementTagType")
        
        if not isinstance(self.last_state_change, ElementTagType | NoneType):
            raise TypeError("last_state_change is not of type ElementTagType")
        
        if not isinstance(self.minimum_trust_level, ElementTagType | NoneType):
            raise TypeError("minimum_trust_level is not of type ElementTagType")
        
        if not isinstance(self.label, ElementTagType | NoneType):
            raise TypeError("label is not of type ElementTagType")
        
        if not isinstance(self.description, ElementTagType | NoneType):
            raise TypeError("description is not of type ElementTagType")
        
    def get_data(self):

        msg_data = []
        
        if self.device_address is not None:
            msg_data.append({"deviceAddress": self.device_address.get_data()})
        if self.device_type is not None:
            msg_data.append({"deviceType": self.device_type.get_data()})
        if self.network_management_responsible_address is not None:
            msg_data.append({"networkManagementResponsibleAddress": self.network_management_responsible_address.get_data()})
        if self.native_setup is not None:
            msg_data.append({"nativeSetup": self.native_setup.get_data()})
        if self.technology_address is not None:
            msg_data.append({"technologyAddress": self.technology_address.get_data()})
        if self.communications_technology_information is not None:
            msg_data.append({"communicationsTechnologyInformation": self.communications_technology_information.get_data()})
        if self.network_feature_set is not None:
            msg_data.append({"networkFeatureSet": self.network_feature_set.get_data()})
        if self.last_state_change is not None:
            msg_data.append({"lastStateChange": self.last_state_change.get_data()})
        if self.minimum_trust_level is not None:
            msg_data.append({"minimumTrustLevel": self.minimum_trust_level.get_data()})
        if self.label is not None:
            msg_data.append({"label": self.label.get_data()})
        if self.description is not None:
            msg_data.append({"description": self.description.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.device_address is not None:
            result_str += f"{sep}deviceAddress: {self.device_address}"
            sep = ", "
        if self.device_type is not None:
            result_str += f"{sep}deviceType: {self.device_type}"
            sep = ", "
        if self.network_management_responsible_address is not None:
            result_str += f"{sep}networkManagementResponsibleAddress: {self.network_management_responsible_address}"
            sep = ", "
        if self.native_setup is not None:
            result_str += f"{sep}nativeSetup: {self.native_setup}"
            sep = ", "
        if self.technology_address is not None:
            result_str += f"{sep}technologyAddress: {self.technology_address}"
            sep = ", "
        if self.communications_technology_information is not None:
            result_str += f"{sep}communicationsTechnologyInformation: {self.communications_technology_information}"
            sep = ", "
        if self.network_feature_set is not None:
            result_str += f"{sep}networkFeatureSet: {self.network_feature_set}"
            sep = ", "
        if self.last_state_change is not None:
            result_str += f"{sep}lastStateChange: {self.last_state_change}"
            sep = ", "
        if self.minimum_trust_level is not None:
            result_str += f"{sep}minimumTrustLevel: {self.minimum_trust_level}"
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
                device_address=data_dict.get('deviceAddress'),
                device_type=data_dict.get('deviceType'),
                network_management_responsible_address=data_dict.get('networkManagementResponsibleAddress'),
                native_setup=data_dict.get('nativeSetup'),
                technology_address=data_dict.get('technologyAddress'),
                communications_technology_information=data_dict.get('communicationsTechnologyInformation'),
                network_feature_set=data_dict.get('networkFeatureSet'),
                last_state_change=data_dict.get('lastStateChange'),
                minimum_trust_level=data_dict.get('minimumTrustLevel'),
                label=data_dict.get('label'),
                description=data_dict.get('description'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class NetworkManagementAddNodeCallElementsType: # EEBus_SPINE_TS_NetworkManagement.xsd: ComplexType
    def __init__(
            self,
            node_address: FeatureAddressElementsType = None,
            native_setup: ElementTagType = None,
            timeout: ElementTagType = None,
            label: ElementTagType = None,
            description: ElementTagType = None,
    ):
        super().__init__()
        
        self.node_address = node_address
        self.native_setup = native_setup
        self.timeout = timeout
        self.label = label
        self.description = description

        if not isinstance(self.node_address, FeatureAddressElementsType | NoneType):
            raise TypeError("node_address is not of type FeatureAddressElementsType")
        
        if not isinstance(self.native_setup, ElementTagType | NoneType):
            raise TypeError("native_setup is not of type ElementTagType")
        
        if not isinstance(self.timeout, ElementTagType | NoneType):
            raise TypeError("timeout is not of type ElementTagType")
        
        if not isinstance(self.label, ElementTagType | NoneType):
            raise TypeError("label is not of type ElementTagType")
        
        if not isinstance(self.description, ElementTagType | NoneType):
            raise TypeError("description is not of type ElementTagType")
        
    def get_data(self):

        msg_data = []
        
        if self.node_address is not None:
            msg_data.append({"nodeAddress": self.node_address.get_data()})
        if self.native_setup is not None:
            msg_data.append({"nativeSetup": self.native_setup.get_data()})
        if self.timeout is not None:
            msg_data.append({"timeout": self.timeout.get_data()})
        if self.label is not None:
            msg_data.append({"label": self.label.get_data()})
        if self.description is not None:
            msg_data.append({"description": self.description.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.node_address is not None:
            result_str += f"{sep}nodeAddress: {self.node_address}"
            sep = ", "
        if self.native_setup is not None:
            result_str += f"{sep}nativeSetup: {self.native_setup}"
            sep = ", "
        if self.timeout is not None:
            result_str += f"{sep}timeout: {self.timeout}"
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
                node_address=data_dict.get('nodeAddress'),
                native_setup=data_dict.get('nativeSetup'),
                timeout=data_dict.get('timeout'),
                label=data_dict.get('label'),
                description=data_dict.get('description'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class NetworkManagementAbortCallElementsType: # EEBus_SPINE_TS_NetworkManagement.xsd: ComplexType
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


class NetworkManagementFeatureDescriptionListDataSelectorsType: # EEBus_SPINE_TS_NetworkManagement.xsd: ComplexType
    def __init__(
            self,
            feature_address: FeatureAddressType = None,
            feature_type: FeatureTypeType = None,
    ):
        super().__init__()
        
        self.feature_address = feature_address
        self.feature_type = feature_type

        if not isinstance(self.feature_address, FeatureAddressType | NoneType):
            raise TypeError("feature_address is not of type FeatureAddressType")
        
        if not isinstance(self.feature_type, FeatureTypeType | NoneType):
            raise TypeError("feature_type is not of type FeatureTypeType")
        
    def get_data(self):

        msg_data = []
        
        if self.feature_address is not None:
            msg_data.append({"featureAddress": self.feature_address.get_data()})
        if self.feature_type is not None:
            msg_data.append({"featureType": self.feature_type.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.feature_address is not None:
            result_str += f"{sep}featureAddress: {self.feature_address}"
            sep = ", "
        if self.feature_type is not None:
            result_str += f"{sep}featureType: {self.feature_type}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                feature_address=data_dict.get('featureAddress'),
                feature_type=data_dict.get('featureType'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class NetworkManagementEntityDescriptionListDataSelectorsType: # EEBus_SPINE_TS_NetworkManagement.xsd: ComplexType
    def __init__(
            self,
            entity_address: EntityAddressType = None,
            entity_type: EntityTypeType = None,
    ):
        super().__init__()
        
        self.entity_address = entity_address
        self.entity_type = entity_type

        if not isinstance(self.entity_address, EntityAddressType | NoneType):
            raise TypeError("entity_address is not of type EntityAddressType")
        
        if not isinstance(self.entity_type, EntityTypeType | NoneType):
            raise TypeError("entity_type is not of type EntityTypeType")
        
    def get_data(self):

        msg_data = []
        
        if self.entity_address is not None:
            msg_data.append({"entityAddress": self.entity_address.get_data()})
        if self.entity_type is not None:
            msg_data.append({"entityType": self.entity_type.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.entity_address is not None:
            result_str += f"{sep}entityAddress: {self.entity_address}"
            sep = ", "
        if self.entity_type is not None:
            result_str += f"{sep}entityType: {self.entity_type}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                entity_address=data_dict.get('entityAddress'),
                entity_type=data_dict.get('entityType'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class NetworkManagementDeviceDescriptionListDataSelectorsType: # EEBus_SPINE_TS_NetworkManagement.xsd: ComplexType
    def __init__(
            self,
            device_address: DeviceAddressType = None,
            device_type: DeviceTypeType = None,
    ):
        super().__init__()
        
        self.device_address = device_address
        self.device_type = device_type

        if not isinstance(self.device_address, DeviceAddressType | NoneType):
            raise TypeError("device_address is not of type DeviceAddressType")
        
        if not isinstance(self.device_type, DeviceTypeType | NoneType):
            raise TypeError("device_type is not of type DeviceTypeType")
        
    def get_data(self):

        msg_data = []
        
        if self.device_address is not None:
            msg_data.append({"deviceAddress": self.device_address.get_data()})
        if self.device_type is not None:
            msg_data.append({"deviceType": self.device_type.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.device_address is not None:
            result_str += f"{sep}deviceAddress: {self.device_address}"
            sep = ", "
        if self.device_type is not None:
            result_str += f"{sep}deviceType: {self.device_type}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                device_address=data_dict.get('deviceAddress'),
                device_type=data_dict.get('deviceType'),
            )
        elif data:
            return cls(data)
        else:
            return cls()



