# Jinja Template message_type.py.jinja2
from spine.simple_type.commondatatypes import SpecificationVersionType
from spine.base_type.commondatatypes import ElementTagType
from spine.simple_type.usecaseinformation import UseCaseScenarioSupportType
from spine.union_type.commondatatypes import FunctionType
from spine.base_type.commondatatypes import FeatureAddressType
from spine.base_type.commondatatypes import FeatureAddressElementsType
from types import NoneType
from spine import array_2_dict


class UseCaseSupportType:
    def __init__(
            self,
            use_case_name: FunctionType = None,
            use_case_version: SpecificationVersionType = None,
            use_case_available: bool = None,
            scenario_support: list[UseCaseScenarioSupportType] = None,
            use_case_document_sub_revision: str = None,
    ):
        super().__init__()
        
        self.use_case_name = use_case_name
        self.use_case_version = use_case_version
        self.use_case_available = use_case_available
        self.scenario_support = scenario_support
        self.use_case_document_sub_revision = use_case_document_sub_revision

        if not isinstance(self.use_case_name, FunctionType | NoneType):
            raise TypeError("use_case_name is not of type FunctionType")
        
        if not isinstance(self.use_case_version, SpecificationVersionType | NoneType):
            raise TypeError("use_case_version is not of type SpecificationVersionType")
        
        if not isinstance(self.use_case_available, bool | NoneType):
            raise TypeError("use_case_available is not of type bool")
        
        if not isinstance(self.scenario_support, list | NoneType):
            raise TypeError("scenario_support is not of type list[UseCaseScenarioSupportType]")
        
        if not isinstance(self.use_case_document_sub_revision, str | NoneType):
            raise TypeError("use_case_document_sub_revision is not of type str")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.use_case_name is not None:
            msg_data.append({"useCaseName": self.use_case_name.get_data()})
        if self.use_case_version is not None:
            msg_data.append({"useCaseVersion": self.use_case_version.get_data()})
        if self.use_case_available is not None:
            msg_data.append({"useCaseAvailable": self.use_case_available})
        if self.scenario_support is not None:
            msg_data.append({"scenarioSupport": [d.get_data() for d in self.scenario_support]})
        if self.use_case_document_sub_revision is not None:
            msg_data.append({"useCaseDocumentSubRevision": self.use_case_document_sub_revision})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.use_case_name is not None:
            result_str += f"{sep}useCaseName: {self.use_case_name}"
            sep = ", "
        if self.use_case_version is not None:
            result_str += f"{sep}useCaseVersion: {self.use_case_version}"
            sep = ", "
        if self.use_case_available is not None:
            result_str += f"{sep}useCaseAvailable: {self.use_case_available}"
            sep = ", "
        if self.scenario_support is not None:
            result_str += f"{sep}scenarioSupport: {self.scenario_support}"
            sep = ", "
        if self.use_case_document_sub_revision is not None:
            result_str += f"{sep}useCaseDocumentSubRevision: {self.use_case_document_sub_revision}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                use_case_name=data_dict.get('useCaseName'),
                use_case_version=data_dict.get('useCaseVersion'),
                use_case_available=data_dict.get('useCaseAvailable'),
                scenario_support=data_dict.get('scenarioSupport'),
                use_case_document_sub_revision=data_dict.get('useCaseDocumentSubRevision'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class UseCaseInformationDataType:
    def __init__(
            self,
            address: FeatureAddressType = None,
            actor: FunctionType = None,
            use_case_support: list[UseCaseSupportType] = None,
    ):
        super().__init__()
        
        self.address = address
        self.actor = actor
        self.use_case_support = use_case_support

        if not isinstance(self.address, FeatureAddressType | NoneType):
            raise TypeError("address is not of type FeatureAddressType")
        
        if not isinstance(self.actor, FunctionType | NoneType):
            raise TypeError("actor is not of type FunctionType")
        
        if not isinstance(self.use_case_support, list | NoneType):
            raise TypeError("use_case_support is not of type list[UseCaseSupportType]")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.address is not None:
            msg_data.append({"address": self.address.get_data()})
        if self.actor is not None:
            msg_data.append({"actor": self.actor.get_data()})
        if self.use_case_support is not None:
            msg_data.append({"useCaseSupport": [d.get_data() for d in self.use_case_support]})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.address is not None:
            result_str += f"{sep}address: {self.address}"
            sep = ", "
        if self.actor is not None:
            result_str += f"{sep}actor: {self.actor}"
            sep = ", "
        if self.use_case_support is not None:
            result_str += f"{sep}useCaseSupport: {self.use_case_support}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                address=data_dict.get('address'),
                actor=data_dict.get('actor'),
                use_case_support=data_dict.get('useCaseSupport'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class UseCaseSupportSelectorsType:
    def __init__(
            self,
            use_case_name: FunctionType = None,
            use_case_version: SpecificationVersionType = None,
            scenario_support: UseCaseScenarioSupportType = None,
    ):
        super().__init__()
        
        self.use_case_name = use_case_name
        self.use_case_version = use_case_version
        self.scenario_support = scenario_support

        if not isinstance(self.use_case_name, FunctionType | NoneType):
            raise TypeError("use_case_name is not of type FunctionType")
        
        if not isinstance(self.use_case_version, SpecificationVersionType | NoneType):
            raise TypeError("use_case_version is not of type SpecificationVersionType")
        
        if not isinstance(self.scenario_support, UseCaseScenarioSupportType | NoneType):
            raise TypeError("scenario_support is not of type UseCaseScenarioSupportType")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.use_case_name is not None:
            msg_data.append({"useCaseName": self.use_case_name.get_data()})
        if self.use_case_version is not None:
            msg_data.append({"useCaseVersion": self.use_case_version.get_data()})
        if self.scenario_support is not None:
            msg_data.append({"scenarioSupport": self.scenario_support.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.use_case_name is not None:
            result_str += f"{sep}useCaseName: {self.use_case_name}"
            sep = ", "
        if self.use_case_version is not None:
            result_str += f"{sep}useCaseVersion: {self.use_case_version}"
            sep = ", "
        if self.scenario_support is not None:
            result_str += f"{sep}scenarioSupport: {self.scenario_support}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                use_case_name=data_dict.get('useCaseName'),
                use_case_version=data_dict.get('useCaseVersion'),
                scenario_support=data_dict.get('scenarioSupport'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class UseCaseSupportElementsType:
    def __init__(
            self,
            use_case_name: ElementTagType = None,
            use_case_version: ElementTagType = None,
            use_case_available: ElementTagType = None,
            scenario_support: ElementTagType = None,
            use_case_document_sub_revision: ElementTagType = None,
    ):
        super().__init__()
        
        self.use_case_name = use_case_name
        self.use_case_version = use_case_version
        self.use_case_available = use_case_available
        self.scenario_support = scenario_support
        self.use_case_document_sub_revision = use_case_document_sub_revision

        if not isinstance(self.use_case_name, ElementTagType | NoneType):
            raise TypeError("use_case_name is not of type ElementTagType")
        
        if not isinstance(self.use_case_version, ElementTagType | NoneType):
            raise TypeError("use_case_version is not of type ElementTagType")
        
        if not isinstance(self.use_case_available, ElementTagType | NoneType):
            raise TypeError("use_case_available is not of type ElementTagType")
        
        if not isinstance(self.scenario_support, ElementTagType | NoneType):
            raise TypeError("scenario_support is not of type ElementTagType")
        
        if not isinstance(self.use_case_document_sub_revision, ElementTagType | NoneType):
            raise TypeError("use_case_document_sub_revision is not of type ElementTagType")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.use_case_name is not None:
            msg_data.append({"useCaseName": self.use_case_name.get_data()})
        if self.use_case_version is not None:
            msg_data.append({"useCaseVersion": self.use_case_version.get_data()})
        if self.use_case_available is not None:
            msg_data.append({"useCaseAvailable": self.use_case_available.get_data()})
        if self.scenario_support is not None:
            msg_data.append({"scenarioSupport": self.scenario_support.get_data()})
        if self.use_case_document_sub_revision is not None:
            msg_data.append({"useCaseDocumentSubRevision": self.use_case_document_sub_revision.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.use_case_name is not None:
            result_str += f"{sep}useCaseName: {self.use_case_name}"
            sep = ", "
        if self.use_case_version is not None:
            result_str += f"{sep}useCaseVersion: {self.use_case_version}"
            sep = ", "
        if self.use_case_available is not None:
            result_str += f"{sep}useCaseAvailable: {self.use_case_available}"
            sep = ", "
        if self.scenario_support is not None:
            result_str += f"{sep}scenarioSupport: {self.scenario_support}"
            sep = ", "
        if self.use_case_document_sub_revision is not None:
            result_str += f"{sep}useCaseDocumentSubRevision: {self.use_case_document_sub_revision}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                use_case_name=data_dict.get('useCaseName'),
                use_case_version=data_dict.get('useCaseVersion'),
                use_case_available=data_dict.get('useCaseAvailable'),
                scenario_support=data_dict.get('scenarioSupport'),
                use_case_document_sub_revision=data_dict.get('useCaseDocumentSubRevision'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class UseCaseInformationListDataType:
    def __init__(
            self,
            use_case_information_data: list[UseCaseInformationDataType] = None,
    ):
        super().__init__()
        
        self.use_case_information_data = use_case_information_data

        if not isinstance(self.use_case_information_data, list | NoneType):
            raise TypeError("use_case_information_data is not of type list[UseCaseInformationDataType]")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.use_case_information_data is not None:
            msg_data.append({"useCaseInformationData": [d.get_data() for d in self.use_case_information_data]})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.use_case_information_data is not None:
            result_str += f"{sep}useCaseInformationData: {self.use_case_information_data}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                use_case_information_data=data_dict.get('useCaseInformationData'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class UseCaseInformationListDataSelectorsType:
    def __init__(
            self,
            address: FeatureAddressType = None,
            actor: FunctionType = None,
            use_case_support: UseCaseSupportSelectorsType = None,
    ):
        super().__init__()
        
        self.address = address
        self.actor = actor
        self.use_case_support = use_case_support

        if not isinstance(self.address, FeatureAddressType | NoneType):
            raise TypeError("address is not of type FeatureAddressType")
        
        if not isinstance(self.actor, FunctionType | NoneType):
            raise TypeError("actor is not of type FunctionType")
        
        if not isinstance(self.use_case_support, UseCaseSupportSelectorsType | NoneType):
            raise TypeError("use_case_support is not of type UseCaseSupportSelectorsType")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.address is not None:
            msg_data.append({"address": self.address.get_data()})
        if self.actor is not None:
            msg_data.append({"actor": self.actor.get_data()})
        if self.use_case_support is not None:
            msg_data.append({"useCaseSupport": self.use_case_support.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.address is not None:
            result_str += f"{sep}address: {self.address}"
            sep = ", "
        if self.actor is not None:
            result_str += f"{sep}actor: {self.actor}"
            sep = ", "
        if self.use_case_support is not None:
            result_str += f"{sep}useCaseSupport: {self.use_case_support}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                address=data_dict.get('address'),
                actor=data_dict.get('actor'),
                use_case_support=data_dict.get('useCaseSupport'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class UseCaseInformationDataElementsType:
    def __init__(
            self,
            address: FeatureAddressElementsType = None,
            actor: ElementTagType = None,
            use_case_support: UseCaseSupportElementsType = None,
    ):
        super().__init__()
        
        self.address = address
        self.actor = actor
        self.use_case_support = use_case_support

        if not isinstance(self.address, FeatureAddressElementsType | NoneType):
            raise TypeError("address is not of type FeatureAddressElementsType")
        
        if not isinstance(self.actor, ElementTagType | NoneType):
            raise TypeError("actor is not of type ElementTagType")
        
        if not isinstance(self.use_case_support, UseCaseSupportElementsType | NoneType):
            raise TypeError("use_case_support is not of type UseCaseSupportElementsType")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.address is not None:
            msg_data.append({"address": self.address.get_data()})
        if self.actor is not None:
            msg_data.append({"actor": self.actor.get_data()})
        if self.use_case_support is not None:
            msg_data.append({"useCaseSupport": self.use_case_support.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.address is not None:
            result_str += f"{sep}address: {self.address}"
            sep = ", "
        if self.actor is not None:
            result_str += f"{sep}actor: {self.actor}"
            sep = ", "
        if self.use_case_support is not None:
            result_str += f"{sep}useCaseSupport: {self.use_case_support}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                address=data_dict.get('address'),
                actor=data_dict.get('actor'),
                use_case_support=data_dict.get('useCaseSupport'),
            )
        elif data:
            return cls(data)
        else:
            return cls()



