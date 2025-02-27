# Jinja Template message_type.py.jinja2
from spine.simple_type.powersequences import PowerSequenceIdType
from spine.base_type.powersequences import PowerSequenceAlternativesRelationDataElementsType
from spine.base_type.powersequences import PowerSequenceAlternativesRelationDataType
from spine.base_type.commondatatypes import ElementTagType
from spine.simple_type.powersequences import AlternativesIdType
from types import NoneType
from spine import array_2_dict


class SmartEnergyManagementPsPowerTimeSlotValueListType:
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


class SmartEnergyManagementPsPowerTimeSlotValueListElementsType:
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


class SmartEnergyManagementPsPowerTimeSlotType:
    def __init__(
            self,
            value_list: SmartEnergyManagementPsPowerTimeSlotValueListType = None,
    ):
        super().__init__()
        
        self.value_list = value_list

        if not isinstance(self.value_list, SmartEnergyManagementPsPowerTimeSlotValueListType | NoneType):
            raise TypeError("value_list is not of type SmartEnergyManagementPsPowerTimeSlotValueListType")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.value_list is not None:
            msg_data.append({"valueList": self.value_list.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.value_list is not None:
            result_str += f"{sep}valueList: {self.value_list}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                value_list=data_dict.get('valueList'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class SmartEnergyManagementPsPowerTimeSlotElementsType:
    def __init__(
            self,
            value_list: SmartEnergyManagementPsPowerTimeSlotValueListElementsType = None,
    ):
        super().__init__()
        
        self.value_list = value_list

        if not isinstance(self.value_list, SmartEnergyManagementPsPowerTimeSlotValueListElementsType | NoneType):
            raise TypeError("value_list is not of type SmartEnergyManagementPsPowerTimeSlotValueListElementsType")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.value_list is not None:
            msg_data.append({"valueList": self.value_list.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.value_list is not None:
            result_str += f"{sep}valueList: {self.value_list}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                value_list=data_dict.get('valueList'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class SmartEnergyManagementPsPowerSequenceType:
    def __init__(
            self,
            power_time_slot: list[SmartEnergyManagementPsPowerTimeSlotType] = None,
    ):
        super().__init__()
        
        self.power_time_slot = power_time_slot

        if not isinstance(self.power_time_slot, list | NoneType):
            raise TypeError("power_time_slot is not of type list[SmartEnergyManagementPsPowerTimeSlotType]")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.power_time_slot is not None:
            msg_data.append({"powerTimeSlot": [d.get_data() for d in self.power_time_slot]})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.power_time_slot is not None:
            result_str += f"{sep}powerTimeSlot: {self.power_time_slot}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                power_time_slot=data_dict.get('powerTimeSlot'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class SmartEnergyManagementPsAlternativesRelationType:
    def __init__(
            self,
            alternatives_id: AlternativesIdType = None,
            sequence_id: list[PowerSequenceIdType] = None,
    ):
        super().__init__()
        
        self.alternatives_id = alternatives_id
        self.sequence_id = sequence_id

        if not isinstance(self.alternatives_id, AlternativesIdType | NoneType):
            raise TypeError("alternatives_id is not of type AlternativesIdType")
        
        if not isinstance(self.sequence_id, list | NoneType):
            raise TypeError("sequence_id is not of type list[PowerSequenceIdType]")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.alternatives_id is not None:
            msg_data.append({"alternativesId": self.alternatives_id.get_data()})
        if self.sequence_id is not None:
            msg_data.append({"sequenceId": [d.get_data() for d in self.sequence_id]})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.alternatives_id is not None:
            result_str += f"{sep}alternativesId: {self.alternatives_id}"
            sep = ", "
        if self.sequence_id is not None:
            result_str += f"{sep}sequenceId: {self.sequence_id}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                alternatives_id=data_dict.get('alternativesId'),
                sequence_id=data_dict.get('sequenceId'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class SmartEnergyManagementPsPowerSequenceElementsType:
    def __init__(
            self,
            power_time_slot: SmartEnergyManagementPsPowerTimeSlotElementsType = None,
    ):
        super().__init__()
        
        self.power_time_slot = power_time_slot

        if not isinstance(self.power_time_slot, SmartEnergyManagementPsPowerTimeSlotElementsType | NoneType):
            raise TypeError("power_time_slot is not of type SmartEnergyManagementPsPowerTimeSlotElementsType")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.power_time_slot is not None:
            msg_data.append({"powerTimeSlot": self.power_time_slot.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.power_time_slot is not None:
            result_str += f"{sep}powerTimeSlot: {self.power_time_slot}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                power_time_slot=data_dict.get('powerTimeSlot'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class SmartEnergyManagementPsAlternativesRelationElementsType:
    def __init__(
            self,
            alternatives_id: ElementTagType = None,
            sequence_id: ElementTagType = None,
    ):
        super().__init__()
        
        self.alternatives_id = alternatives_id
        self.sequence_id = sequence_id

        if not isinstance(self.alternatives_id, ElementTagType | NoneType):
            raise TypeError("alternatives_id is not of type ElementTagType")
        
        if not isinstance(self.sequence_id, ElementTagType | NoneType):
            raise TypeError("sequence_id is not of type ElementTagType")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.alternatives_id is not None:
            msg_data.append({"alternativesId": self.alternatives_id.get_data()})
        if self.sequence_id is not None:
            msg_data.append({"sequenceId": self.sequence_id.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.alternatives_id is not None:
            result_str += f"{sep}alternativesId: {self.alternatives_id}"
            sep = ", "
        if self.sequence_id is not None:
            result_str += f"{sep}sequenceId: {self.sequence_id}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                alternatives_id=data_dict.get('alternativesId'),
                sequence_id=data_dict.get('sequenceId'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class SmartEnergyManagementPsAlternativesType:
    def __init__(
            self,
            relation: SmartEnergyManagementPsAlternativesRelationType = None,
            power_sequence: list[SmartEnergyManagementPsPowerSequenceType] = None,
    ):
        super().__init__()
        
        self.relation = relation
        self.power_sequence = power_sequence

        if not isinstance(self.relation, SmartEnergyManagementPsAlternativesRelationType | NoneType):
            raise TypeError("relation is not of type SmartEnergyManagementPsAlternativesRelationType")
        
        if not isinstance(self.power_sequence, list | NoneType):
            raise TypeError("power_sequence is not of type list[SmartEnergyManagementPsPowerSequenceType]")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.relation is not None:
            msg_data.append({"relation": self.relation.get_data()})
        if self.power_sequence is not None:
            msg_data.append({"powerSequence": [d.get_data() for d in self.power_sequence]})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.relation is not None:
            result_str += f"{sep}relation: {self.relation}"
            sep = ", "
        if self.power_sequence is not None:
            result_str += f"{sep}powerSequence: {self.power_sequence}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                relation=data_dict.get('relation'),
                power_sequence=data_dict.get('powerSequence'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class SmartEnergyManagementPsAlternativesElementsType:
    def __init__(
            self,
            relation: SmartEnergyManagementPsAlternativesRelationElementsType = None,
            power_sequence: SmartEnergyManagementPsPowerSequenceElementsType = None,
    ):
        super().__init__()
        
        self.relation = relation
        self.power_sequence = power_sequence

        if not isinstance(self.relation, SmartEnergyManagementPsAlternativesRelationElementsType | NoneType):
            raise TypeError("relation is not of type SmartEnergyManagementPsAlternativesRelationElementsType")
        
        if not isinstance(self.power_sequence, SmartEnergyManagementPsPowerSequenceElementsType | NoneType):
            raise TypeError("power_sequence is not of type SmartEnergyManagementPsPowerSequenceElementsType")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.relation is not None:
            msg_data.append({"relation": self.relation.get_data()})
        if self.power_sequence is not None:
            msg_data.append({"powerSequence": self.power_sequence.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.relation is not None:
            result_str += f"{sep}relation: {self.relation}"
            sep = ", "
        if self.power_sequence is not None:
            result_str += f"{sep}powerSequence: {self.power_sequence}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                relation=data_dict.get('relation'),
                power_sequence=data_dict.get('powerSequence'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class SmartEnergyManagementPsPriceDataType:
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


class SmartEnergyManagementPsPriceDataSelectorsType:
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


class SmartEnergyManagementPsPriceDataElementsType:
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


class SmartEnergyManagementPsPriceCalculationRequestCallType:
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


class SmartEnergyManagementPsPriceCalculationRequestCallElementsType:
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


class SmartEnergyManagementPsDataType:
    def __init__(
            self,
            alternatives: list[SmartEnergyManagementPsAlternativesType] = None,
    ):
        super().__init__()
        
        self.alternatives = alternatives

        if not isinstance(self.alternatives, list | NoneType):
            raise TypeError("alternatives is not of type list[SmartEnergyManagementPsAlternativesType]")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.alternatives is not None:
            msg_data.append({"alternatives": [d.get_data() for d in self.alternatives]})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.alternatives is not None:
            result_str += f"{sep}alternatives: {self.alternatives}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                alternatives=data_dict.get('alternatives'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class SmartEnergyManagementPsDataSelectorsType:
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


class SmartEnergyManagementPsDataElementsType:
    def __init__(
            self,
            alternatives: SmartEnergyManagementPsAlternativesElementsType = None,
    ):
        super().__init__()
        
        self.alternatives = alternatives

        if not isinstance(self.alternatives, SmartEnergyManagementPsAlternativesElementsType | NoneType):
            raise TypeError("alternatives is not of type SmartEnergyManagementPsAlternativesElementsType")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.alternatives is not None:
            msg_data.append({"alternatives": self.alternatives.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.alternatives is not None:
            result_str += f"{sep}alternatives: {self.alternatives}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                alternatives=data_dict.get('alternatives'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class SmartEnergyManagementPsConfigurationRequestCallType:
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


class SmartEnergyManagementPsConfigurationRequestCallElementsType:
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



