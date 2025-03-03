# Jinja Template message_type.py.jinja2
from spine.base_type.commondatatypes import ElementTagType
from spine.base_type.commondatatypes import ScaledNumberElementsType
from spine.base_type.commondatatypes import ScaledNumberType
from spine.simple_type.commondatatypes import DescriptionType
from spine.simple_type.commondatatypes import LabelType
from spine.simple_type.threshold import ThresholdIdType
from spine.union_type.commondatatypes import ScopeTypeType
from spine.union_type.commondatatypes import UnitOfMeasurementType
from spine.union_type.threshold import ThresholdTypeType
from types import NoneType
from spine import array_2_dict


class ThresholdDataType: # EEBus_SPINE_TS_Threshold.xsd:ns_p:ThresholdDataType -> ComplexType
    def __init__(
            self,
            threshold_id: ThresholdIdType = None,
            threshold_value: ScaledNumberType = None,
    ):
        super().__init__()
        
        self.threshold_id = threshold_id
        self.threshold_value = threshold_value

        if not isinstance(self.threshold_id, ThresholdIdType | NoneType):
            raise TypeError("threshold_id is not of type ThresholdIdType")
        
        if not isinstance(self.threshold_value, ScaledNumberType | NoneType):
            raise TypeError("threshold_value is not of type ScaledNumberType")
        
    def get_data(self):

        msg_data = []
        
        if self.threshold_id is not None:
            msg_data.append({"thresholdId": self.threshold_id.get_data()})
        if self.threshold_value is not None:
            msg_data.append({"thresholdValue": self.threshold_value.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.threshold_id is not None:
            result_str += f"{sep}thresholdId: {self.threshold_id}"
            sep = ", "
        if self.threshold_value is not None:
            result_str += f"{sep}thresholdValue: {self.threshold_value}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                threshold_id=data_dict.get('thresholdId'),
                threshold_value=data_dict.get('thresholdValue'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class ThresholdDescriptionDataType: # EEBus_SPINE_TS_Threshold.xsd:ns_p:ThresholdDescriptionDataType -> ComplexType
    def __init__(
            self,
            threshold_id: ThresholdIdType = None,
            threshold_type: ThresholdTypeType = None,
            unit: UnitOfMeasurementType = None,
            scope_type: ScopeTypeType = None,
            label: LabelType = None,
            description: DescriptionType = None,
    ):
        super().__init__()
        
        self.threshold_id = threshold_id
        self.threshold_type = threshold_type
        self.unit = unit
        self.scope_type = scope_type
        self.label = label
        self.description = description

        if not isinstance(self.threshold_id, ThresholdIdType | NoneType):
            raise TypeError("threshold_id is not of type ThresholdIdType")
        
        if not isinstance(self.threshold_type, ThresholdTypeType | NoneType):
            raise TypeError("threshold_type is not of type ThresholdTypeType")
        
        if not isinstance(self.unit, UnitOfMeasurementType | NoneType):
            raise TypeError("unit is not of type UnitOfMeasurementType")
        
        if not isinstance(self.scope_type, ScopeTypeType | NoneType):
            raise TypeError("scope_type is not of type ScopeTypeType")
        
        if not isinstance(self.label, LabelType | NoneType):
            raise TypeError("label is not of type LabelType")
        
        if not isinstance(self.description, DescriptionType | NoneType):
            raise TypeError("description is not of type DescriptionType")
        
    def get_data(self):

        msg_data = []
        
        if self.threshold_id is not None:
            msg_data.append({"thresholdId": self.threshold_id.get_data()})
        if self.threshold_type is not None:
            msg_data.append({"thresholdType": self.threshold_type.get_data()})
        if self.unit is not None:
            msg_data.append({"unit": self.unit.get_data()})
        if self.scope_type is not None:
            msg_data.append({"scopeType": self.scope_type.get_data()})
        if self.label is not None:
            msg_data.append({"label": self.label.get_data()})
        if self.description is not None:
            msg_data.append({"description": self.description.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.threshold_id is not None:
            result_str += f"{sep}thresholdId: {self.threshold_id}"
            sep = ", "
        if self.threshold_type is not None:
            result_str += f"{sep}thresholdType: {self.threshold_type}"
            sep = ", "
        if self.unit is not None:
            result_str += f"{sep}unit: {self.unit}"
            sep = ", "
        if self.scope_type is not None:
            result_str += f"{sep}scopeType: {self.scope_type}"
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
                threshold_id=data_dict.get('thresholdId'),
                threshold_type=data_dict.get('thresholdType'),
                unit=data_dict.get('unit'),
                scope_type=data_dict.get('scopeType'),
                label=data_dict.get('label'),
                description=data_dict.get('description'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class ThresholdConstraintsDataType: # EEBus_SPINE_TS_Threshold.xsd:ns_p:ThresholdConstraintsDataType -> ComplexType
    def __init__(
            self,
            threshold_id: ThresholdIdType = None,
            threshold_range_min: ScaledNumberType = None,
            threshold_range_max: ScaledNumberType = None,
            threshold_step_size: ScaledNumberType = None,
    ):
        super().__init__()
        
        self.threshold_id = threshold_id
        self.threshold_range_min = threshold_range_min
        self.threshold_range_max = threshold_range_max
        self.threshold_step_size = threshold_step_size

        if not isinstance(self.threshold_id, ThresholdIdType | NoneType):
            raise TypeError("threshold_id is not of type ThresholdIdType")
        
        if not isinstance(self.threshold_range_min, ScaledNumberType | NoneType):
            raise TypeError("threshold_range_min is not of type ScaledNumberType")
        
        if not isinstance(self.threshold_range_max, ScaledNumberType | NoneType):
            raise TypeError("threshold_range_max is not of type ScaledNumberType")
        
        if not isinstance(self.threshold_step_size, ScaledNumberType | NoneType):
            raise TypeError("threshold_step_size is not of type ScaledNumberType")
        
    def get_data(self):

        msg_data = []
        
        if self.threshold_id is not None:
            msg_data.append({"thresholdId": self.threshold_id.get_data()})
        if self.threshold_range_min is not None:
            msg_data.append({"thresholdRangeMin": self.threshold_range_min.get_data()})
        if self.threshold_range_max is not None:
            msg_data.append({"thresholdRangeMax": self.threshold_range_max.get_data()})
        if self.threshold_step_size is not None:
            msg_data.append({"thresholdStepSize": self.threshold_step_size.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.threshold_id is not None:
            result_str += f"{sep}thresholdId: {self.threshold_id}"
            sep = ", "
        if self.threshold_range_min is not None:
            result_str += f"{sep}thresholdRangeMin: {self.threshold_range_min}"
            sep = ", "
        if self.threshold_range_max is not None:
            result_str += f"{sep}thresholdRangeMax: {self.threshold_range_max}"
            sep = ", "
        if self.threshold_step_size is not None:
            result_str += f"{sep}thresholdStepSize: {self.threshold_step_size}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                threshold_id=data_dict.get('thresholdId'),
                threshold_range_min=data_dict.get('thresholdRangeMin'),
                threshold_range_max=data_dict.get('thresholdRangeMax'),
                threshold_step_size=data_dict.get('thresholdStepSize'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class ThresholdListDataType: # EEBus_SPINE_TS_Threshold.xsd:ns_p:ThresholdListDataType -> ComplexType
    def __init__(
            self,
            threshold_data: list[ThresholdDataType] = None,
    ):
        super().__init__()
        
        self.threshold_data = threshold_data

        if not isinstance(self.threshold_data, list | NoneType):
            raise TypeError("threshold_data is not of type list[ThresholdDataType]")
        
    def get_data(self):

        msg_data = []
        
        if self.threshold_data is not None:
            msg_data.append({"thresholdData": [d.get_data() for d in self.threshold_data]})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.threshold_data is not None:
            result_str += f"{sep}thresholdData: {self.threshold_data}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                threshold_data=data_dict.get('thresholdData'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class ThresholdDescriptionListDataType: # EEBus_SPINE_TS_Threshold.xsd:ns_p:ThresholdDescriptionListDataType -> ComplexType
    def __init__(
            self,
            threshold_description_data: list[ThresholdDescriptionDataType] = None,
    ):
        super().__init__()
        
        self.threshold_description_data = threshold_description_data

        if not isinstance(self.threshold_description_data, list | NoneType):
            raise TypeError("threshold_description_data is not of type list[ThresholdDescriptionDataType]")
        
    def get_data(self):

        msg_data = []
        
        if self.threshold_description_data is not None:
            msg_data.append({"thresholdDescriptionData": [d.get_data() for d in self.threshold_description_data]})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.threshold_description_data is not None:
            result_str += f"{sep}thresholdDescriptionData: {self.threshold_description_data}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                threshold_description_data=data_dict.get('thresholdDescriptionData'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class ThresholdConstraintsListDataType: # EEBus_SPINE_TS_Threshold.xsd:ns_p:ThresholdConstraintsListDataType -> ComplexType
    def __init__(
            self,
            threshold_constraints_data: list[ThresholdConstraintsDataType] = None,
    ):
        super().__init__()
        
        self.threshold_constraints_data = threshold_constraints_data

        if not isinstance(self.threshold_constraints_data, list | NoneType):
            raise TypeError("threshold_constraints_data is not of type list[ThresholdConstraintsDataType]")
        
    def get_data(self):

        msg_data = []
        
        if self.threshold_constraints_data is not None:
            msg_data.append({"thresholdConstraintsData": [d.get_data() for d in self.threshold_constraints_data]})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.threshold_constraints_data is not None:
            result_str += f"{sep}thresholdConstraintsData: {self.threshold_constraints_data}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                threshold_constraints_data=data_dict.get('thresholdConstraintsData'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class ThresholdDescriptionDataElementsType: # EEBus_SPINE_TS_Threshold.xsd:ns_p:ThresholdDescriptionDataElementsType -> ComplexType
    def __init__(
            self,
            threshold_id: ElementTagType = None,
            threshold_type: ElementTagType = None,
            unit: ElementTagType = None,
            scope_type: ElementTagType = None,
            label: ElementTagType = None,
            description: ElementTagType = None,
    ):
        super().__init__()
        
        self.threshold_id = threshold_id
        self.threshold_type = threshold_type
        self.unit = unit
        self.scope_type = scope_type
        self.label = label
        self.description = description

        if not isinstance(self.threshold_id, ElementTagType | NoneType):
            raise TypeError("threshold_id is not of type ElementTagType")
        
        if not isinstance(self.threshold_type, ElementTagType | NoneType):
            raise TypeError("threshold_type is not of type ElementTagType")
        
        if not isinstance(self.unit, ElementTagType | NoneType):
            raise TypeError("unit is not of type ElementTagType")
        
        if not isinstance(self.scope_type, ElementTagType | NoneType):
            raise TypeError("scope_type is not of type ElementTagType")
        
        if not isinstance(self.label, ElementTagType | NoneType):
            raise TypeError("label is not of type ElementTagType")
        
        if not isinstance(self.description, ElementTagType | NoneType):
            raise TypeError("description is not of type ElementTagType")
        
    def get_data(self):

        msg_data = []
        
        if self.threshold_id is not None:
            msg_data.append({"thresholdId": self.threshold_id.get_data()})
        if self.threshold_type is not None:
            msg_data.append({"thresholdType": self.threshold_type.get_data()})
        if self.unit is not None:
            msg_data.append({"unit": self.unit.get_data()})
        if self.scope_type is not None:
            msg_data.append({"scopeType": self.scope_type.get_data()})
        if self.label is not None:
            msg_data.append({"label": self.label.get_data()})
        if self.description is not None:
            msg_data.append({"description": self.description.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.threshold_id is not None:
            result_str += f"{sep}thresholdId: {self.threshold_id}"
            sep = ", "
        if self.threshold_type is not None:
            result_str += f"{sep}thresholdType: {self.threshold_type}"
            sep = ", "
        if self.unit is not None:
            result_str += f"{sep}unit: {self.unit}"
            sep = ", "
        if self.scope_type is not None:
            result_str += f"{sep}scopeType: {self.scope_type}"
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
                threshold_id=data_dict.get('thresholdId'),
                threshold_type=data_dict.get('thresholdType'),
                unit=data_dict.get('unit'),
                scope_type=data_dict.get('scopeType'),
                label=data_dict.get('label'),
                description=data_dict.get('description'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class ThresholdDataElementsType: # EEBus_SPINE_TS_Threshold.xsd:ns_p:ThresholdDataElementsType -> ComplexType
    def __init__(
            self,
            threshold_id: ElementTagType = None,
            threshold_value: ScaledNumberElementsType = None,
    ):
        super().__init__()
        
        self.threshold_id = threshold_id
        self.threshold_value = threshold_value

        if not isinstance(self.threshold_id, ElementTagType | NoneType):
            raise TypeError("threshold_id is not of type ElementTagType")
        
        if not isinstance(self.threshold_value, ScaledNumberElementsType | NoneType):
            raise TypeError("threshold_value is not of type ScaledNumberElementsType")
        
    def get_data(self):

        msg_data = []
        
        if self.threshold_id is not None:
            msg_data.append({"thresholdId": self.threshold_id.get_data()})
        if self.threshold_value is not None:
            msg_data.append({"thresholdValue": self.threshold_value.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.threshold_id is not None:
            result_str += f"{sep}thresholdId: {self.threshold_id}"
            sep = ", "
        if self.threshold_value is not None:
            result_str += f"{sep}thresholdValue: {self.threshold_value}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                threshold_id=data_dict.get('thresholdId'),
                threshold_value=data_dict.get('thresholdValue'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class ThresholdConstraintsDataElementsType: # EEBus_SPINE_TS_Threshold.xsd:ns_p:ThresholdConstraintsDataElementsType -> ComplexType
    def __init__(
            self,
            threshold_id: ElementTagType = None,
            threshold_range_min: ScaledNumberElementsType = None,
            threshold_range_max: ScaledNumberElementsType = None,
            threshold_step_size: ScaledNumberElementsType = None,
    ):
        super().__init__()
        
        self.threshold_id = threshold_id
        self.threshold_range_min = threshold_range_min
        self.threshold_range_max = threshold_range_max
        self.threshold_step_size = threshold_step_size

        if not isinstance(self.threshold_id, ElementTagType | NoneType):
            raise TypeError("threshold_id is not of type ElementTagType")
        
        if not isinstance(self.threshold_range_min, ScaledNumberElementsType | NoneType):
            raise TypeError("threshold_range_min is not of type ScaledNumberElementsType")
        
        if not isinstance(self.threshold_range_max, ScaledNumberElementsType | NoneType):
            raise TypeError("threshold_range_max is not of type ScaledNumberElementsType")
        
        if not isinstance(self.threshold_step_size, ScaledNumberElementsType | NoneType):
            raise TypeError("threshold_step_size is not of type ScaledNumberElementsType")
        
    def get_data(self):

        msg_data = []
        
        if self.threshold_id is not None:
            msg_data.append({"thresholdId": self.threshold_id.get_data()})
        if self.threshold_range_min is not None:
            msg_data.append({"thresholdRangeMin": self.threshold_range_min.get_data()})
        if self.threshold_range_max is not None:
            msg_data.append({"thresholdRangeMax": self.threshold_range_max.get_data()})
        if self.threshold_step_size is not None:
            msg_data.append({"thresholdStepSize": self.threshold_step_size.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.threshold_id is not None:
            result_str += f"{sep}thresholdId: {self.threshold_id}"
            sep = ", "
        if self.threshold_range_min is not None:
            result_str += f"{sep}thresholdRangeMin: {self.threshold_range_min}"
            sep = ", "
        if self.threshold_range_max is not None:
            result_str += f"{sep}thresholdRangeMax: {self.threshold_range_max}"
            sep = ", "
        if self.threshold_step_size is not None:
            result_str += f"{sep}thresholdStepSize: {self.threshold_step_size}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                threshold_id=data_dict.get('thresholdId'),
                threshold_range_min=data_dict.get('thresholdRangeMin'),
                threshold_range_max=data_dict.get('thresholdRangeMax'),
                threshold_step_size=data_dict.get('thresholdStepSize'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class ThresholdListDataSelectorsType: # EEBus_SPINE_TS_Threshold.xsd:ns_p:ThresholdListDataSelectorsType -> ComplexType
    def __init__(
            self,
            threshold_id: ThresholdIdType = None,
    ):
        super().__init__()
        
        self.threshold_id = threshold_id

        if not isinstance(self.threshold_id, ThresholdIdType | NoneType):
            raise TypeError("threshold_id is not of type ThresholdIdType")
        
    def get_data(self):

        msg_data = []
        
        if self.threshold_id is not None:
            msg_data.append({"thresholdId": self.threshold_id.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.threshold_id is not None:
            result_str += f"{sep}thresholdId: {self.threshold_id}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                threshold_id=data_dict.get('thresholdId'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class ThresholdDescriptionListDataSelectorsType: # EEBus_SPINE_TS_Threshold.xsd:ns_p:ThresholdDescriptionListDataSelectorsType -> ComplexType
    def __init__(
            self,
            threshold_id: ThresholdIdType = None,
            scope_type: ScopeTypeType = None,
    ):
        super().__init__()
        
        self.threshold_id = threshold_id
        self.scope_type = scope_type

        if not isinstance(self.threshold_id, ThresholdIdType | NoneType):
            raise TypeError("threshold_id is not of type ThresholdIdType")
        
        if not isinstance(self.scope_type, ScopeTypeType | NoneType):
            raise TypeError("scope_type is not of type ScopeTypeType")
        
    def get_data(self):

        msg_data = []
        
        if self.threshold_id is not None:
            msg_data.append({"thresholdId": self.threshold_id.get_data()})
        if self.scope_type is not None:
            msg_data.append({"scopeType": self.scope_type.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.threshold_id is not None:
            result_str += f"{sep}thresholdId: {self.threshold_id}"
            sep = ", "
        if self.scope_type is not None:
            result_str += f"{sep}scopeType: {self.scope_type}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                threshold_id=data_dict.get('thresholdId'),
                scope_type=data_dict.get('scopeType'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class ThresholdConstraintsListDataSelectorsType: # EEBus_SPINE_TS_Threshold.xsd:ns_p:ThresholdConstraintsListDataSelectorsType -> ComplexType
    def __init__(
            self,
            threshold_id: ThresholdIdType = None,
    ):
        super().__init__()
        
        self.threshold_id = threshold_id

        if not isinstance(self.threshold_id, ThresholdIdType | NoneType):
            raise TypeError("threshold_id is not of type ThresholdIdType")
        
    def get_data(self):

        msg_data = []
        
        if self.threshold_id is not None:
            msg_data.append({"thresholdId": self.threshold_id.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.threshold_id is not None:
            result_str += f"{sep}thresholdId: {self.threshold_id}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                threshold_id=data_dict.get('thresholdId'),
            )
        elif data:
            return cls(data)
        else:
            return cls()



