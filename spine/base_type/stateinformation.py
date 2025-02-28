# Jinja Template message_type.py.jinja2
from spine.base_type.commondatatypes import ElementTagType
from spine.simple_type.stateinformation import stateInformationIdType
from spine.union_type.commondatatypes import AbsoluteOrRelativeTimeType
from spine.union_type.stateinformation import StateInformationCategoryType
from spine.union_type.stateinformation import StateInformationType
from types import NoneType
from spine import array_2_dict


class StateInformationDataType: # EEBus_SPINE_TS_StateInformation.xsd: ComplexType
    def __init__(
            self,
            state_information_id: stateInformationIdType = None,
            state_information: StateInformationType = None,
            is_active: bool = None,
            category: StateInformationCategoryType = None,
            time_of_last_change: AbsoluteOrRelativeTimeType = None,
    ):
        super().__init__()
        
        self.state_information_id = state_information_id
        self.state_information = state_information
        self.is_active = is_active
        self.category = category
        self.time_of_last_change = time_of_last_change

        if not isinstance(self.state_information_id, stateInformationIdType | NoneType):
            raise TypeError("state_information_id is not of type stateInformationIdType")
        
        if not isinstance(self.state_information, StateInformationType | NoneType):
            raise TypeError("state_information is not of type StateInformationType")
        
        if not isinstance(self.is_active, bool | NoneType):
            raise TypeError("is_active is not of type bool")
        
        if not isinstance(self.category, StateInformationCategoryType | NoneType):
            raise TypeError("category is not of type StateInformationCategoryType")
        
        if not isinstance(self.time_of_last_change, AbsoluteOrRelativeTimeType | NoneType):
            raise TypeError("time_of_last_change is not of type AbsoluteOrRelativeTimeType")
        
    def get_data(self):

        msg_data = []
        
        if self.state_information_id is not None:
            msg_data.append({"stateInformationId": self.state_information_id.get_data()})
        if self.state_information is not None:
            msg_data.append({"stateInformation": self.state_information.get_data()})
        if self.is_active is not None:
            msg_data.append({"isActive": self.is_active})
        if self.category is not None:
            msg_data.append({"category": self.category.get_data()})
        if self.time_of_last_change is not None:
            msg_data.append({"timeOfLastChange": self.time_of_last_change.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.state_information_id is not None:
            result_str += f"{sep}stateInformationId: {self.state_information_id}"
            sep = ", "
        if self.state_information is not None:
            result_str += f"{sep}stateInformation: {self.state_information}"
            sep = ", "
        if self.is_active is not None:
            result_str += f"{sep}isActive: {self.is_active}"
            sep = ", "
        if self.category is not None:
            result_str += f"{sep}category: {self.category}"
            sep = ", "
        if self.time_of_last_change is not None:
            result_str += f"{sep}timeOfLastChange: {self.time_of_last_change}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                state_information_id=data_dict.get('stateInformationId'),
                state_information=data_dict.get('stateInformation'),
                is_active=data_dict.get('isActive'),
                category=data_dict.get('category'),
                time_of_last_change=data_dict.get('timeOfLastChange'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class StateInformationListDataType: # EEBus_SPINE_TS_StateInformation.xsd: ComplexType
    def __init__(
            self,
            state_information_data: list[StateInformationDataType] = None,
    ):
        super().__init__()
        
        self.state_information_data = state_information_data

        if not isinstance(self.state_information_data, list | NoneType):
            raise TypeError("state_information_data is not of type list[StateInformationDataType]")
        
    def get_data(self):

        msg_data = []
        
        if self.state_information_data is not None:
            msg_data.append({"stateInformationData": [d.get_data() for d in self.state_information_data]})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.state_information_data is not None:
            result_str += f"{sep}stateInformationData: {self.state_information_data}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                state_information_data=data_dict.get('stateInformationData'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class StateInformationDataElementsType: # EEBus_SPINE_TS_StateInformation.xsd: ComplexType
    def __init__(
            self,
            state_information_id: ElementTagType = None,
            state_information: ElementTagType = None,
            is_active: ElementTagType = None,
            category: ElementTagType = None,
            time_of_last_change: ElementTagType = None,
    ):
        super().__init__()
        
        self.state_information_id = state_information_id
        self.state_information = state_information
        self.is_active = is_active
        self.category = category
        self.time_of_last_change = time_of_last_change

        if not isinstance(self.state_information_id, ElementTagType | NoneType):
            raise TypeError("state_information_id is not of type ElementTagType")
        
        if not isinstance(self.state_information, ElementTagType | NoneType):
            raise TypeError("state_information is not of type ElementTagType")
        
        if not isinstance(self.is_active, ElementTagType | NoneType):
            raise TypeError("is_active is not of type ElementTagType")
        
        if not isinstance(self.category, ElementTagType | NoneType):
            raise TypeError("category is not of type ElementTagType")
        
        if not isinstance(self.time_of_last_change, ElementTagType | NoneType):
            raise TypeError("time_of_last_change is not of type ElementTagType")
        
    def get_data(self):

        msg_data = []
        
        if self.state_information_id is not None:
            msg_data.append({"stateInformationId": self.state_information_id.get_data()})
        if self.state_information is not None:
            msg_data.append({"stateInformation": self.state_information.get_data()})
        if self.is_active is not None:
            msg_data.append({"isActive": self.is_active.get_data()})
        if self.category is not None:
            msg_data.append({"category": self.category.get_data()})
        if self.time_of_last_change is not None:
            msg_data.append({"timeOfLastChange": self.time_of_last_change.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.state_information_id is not None:
            result_str += f"{sep}stateInformationId: {self.state_information_id}"
            sep = ", "
        if self.state_information is not None:
            result_str += f"{sep}stateInformation: {self.state_information}"
            sep = ", "
        if self.is_active is not None:
            result_str += f"{sep}isActive: {self.is_active}"
            sep = ", "
        if self.category is not None:
            result_str += f"{sep}category: {self.category}"
            sep = ", "
        if self.time_of_last_change is not None:
            result_str += f"{sep}timeOfLastChange: {self.time_of_last_change}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                state_information_id=data_dict.get('stateInformationId'),
                state_information=data_dict.get('stateInformation'),
                is_active=data_dict.get('isActive'),
                category=data_dict.get('category'),
                time_of_last_change=data_dict.get('timeOfLastChange'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class StateInformationListDataSelectorsType: # EEBus_SPINE_TS_StateInformation.xsd: ComplexType
    def __init__(
            self,
            state_information_id: stateInformationIdType = None,
            state_information: StateInformationType = None,
            is_active: bool = None,
            category: StateInformationCategoryType = None,
    ):
        super().__init__()
        
        self.state_information_id = state_information_id
        self.state_information = state_information
        self.is_active = is_active
        self.category = category

        if not isinstance(self.state_information_id, stateInformationIdType | NoneType):
            raise TypeError("state_information_id is not of type stateInformationIdType")
        
        if not isinstance(self.state_information, StateInformationType | NoneType):
            raise TypeError("state_information is not of type StateInformationType")
        
        if not isinstance(self.is_active, bool | NoneType):
            raise TypeError("is_active is not of type bool")
        
        if not isinstance(self.category, StateInformationCategoryType | NoneType):
            raise TypeError("category is not of type StateInformationCategoryType")
        
    def get_data(self):

        msg_data = []
        
        if self.state_information_id is not None:
            msg_data.append({"stateInformationId": self.state_information_id.get_data()})
        if self.state_information is not None:
            msg_data.append({"stateInformation": self.state_information.get_data()})
        if self.is_active is not None:
            msg_data.append({"isActive": self.is_active})
        if self.category is not None:
            msg_data.append({"category": self.category.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.state_information_id is not None:
            result_str += f"{sep}stateInformationId: {self.state_information_id}"
            sep = ", "
        if self.state_information is not None:
            result_str += f"{sep}stateInformation: {self.state_information}"
            sep = ", "
        if self.is_active is not None:
            result_str += f"{sep}isActive: {self.is_active}"
            sep = ", "
        if self.category is not None:
            result_str += f"{sep}category: {self.category}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                state_information_id=data_dict.get('stateInformationId'),
                state_information=data_dict.get('stateInformation'),
                is_active=data_dict.get('isActive'),
                category=data_dict.get('category'),
            )
        elif data:
            return cls(data)
        else:
            return cls()



