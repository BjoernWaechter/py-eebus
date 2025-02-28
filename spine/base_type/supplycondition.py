# Jinja Template message_type.py.jinja2
from spine.base_type.commondatatypes import ElementTagType
from spine.base_type.commondatatypes import ScaledNumberElementsType
from spine.base_type.commondatatypes import ScaledNumberType
from spine.base_type.commondatatypes import TimePeriodElementsType
from spine.base_type.commondatatypes import TimePeriodType
from spine.base_type.commondatatypes import TimestampIntervalType
from spine.simple_type.commondatatypes import DescriptionType
from spine.simple_type.commondatatypes import LabelType
from spine.simple_type.supplycondition import ConditionIdType
from spine.simple_type.threshold import ThresholdIdType
from spine.union_type.commondatatypes import AbsoluteOrRelativeTimeType
from spine.union_type.commondatatypes import CommodityTypeType
from spine.union_type.commondatatypes import EnergyDirectionType
from spine.union_type.supplycondition import GridConditionType
from spine.union_type.supplycondition import SupplyConditionEventTypeType
from spine.union_type.supplycondition import SupplyConditionOriginatorType
from types import NoneType
from spine import array_2_dict


class SupplyConditionThresholdRelationDataType: # EEBus_SPINE_TS_SupplyCondition.xsd: ComplexType
    def __init__(
            self,
            condition_id: ConditionIdType = None,
            threshold_id: list[ThresholdIdType] = None,
    ):
        super().__init__()
        
        self.condition_id = condition_id
        self.threshold_id = threshold_id

        if not isinstance(self.condition_id, ConditionIdType | NoneType):
            raise TypeError("condition_id is not of type ConditionIdType")
        
        if not isinstance(self.threshold_id, list | NoneType):
            raise TypeError("threshold_id is not of type list[ThresholdIdType]")
        
    def get_data(self):

        msg_data = []
        
        if self.condition_id is not None:
            msg_data.append({"conditionId": self.condition_id.get_data()})
        if self.threshold_id is not None:
            msg_data.append({"thresholdId": [d.get_data() for d in self.threshold_id]})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.condition_id is not None:
            result_str += f"{sep}conditionId: {self.condition_id}"
            sep = ", "
        if self.threshold_id is not None:
            result_str += f"{sep}thresholdId: {self.threshold_id}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                condition_id=data_dict.get('conditionId'),
                threshold_id=data_dict.get('thresholdId'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class SupplyConditionDescriptionDataType: # EEBus_SPINE_TS_SupplyCondition.xsd: ComplexType
    def __init__(
            self,
            condition_id: ConditionIdType = None,
            commodity_type: CommodityTypeType = None,
            positive_energy_direction: EnergyDirectionType = None,
            label: LabelType = None,
            description: DescriptionType = None,
    ):
        super().__init__()
        
        self.condition_id = condition_id
        self.commodity_type = commodity_type
        self.positive_energy_direction = positive_energy_direction
        self.label = label
        self.description = description

        if not isinstance(self.condition_id, ConditionIdType | NoneType):
            raise TypeError("condition_id is not of type ConditionIdType")
        
        if not isinstance(self.commodity_type, CommodityTypeType | NoneType):
            raise TypeError("commodity_type is not of type CommodityTypeType")
        
        if not isinstance(self.positive_energy_direction, EnergyDirectionType | NoneType):
            raise TypeError("positive_energy_direction is not of type EnergyDirectionType")
        
        if not isinstance(self.label, LabelType | NoneType):
            raise TypeError("label is not of type LabelType")
        
        if not isinstance(self.description, DescriptionType | NoneType):
            raise TypeError("description is not of type DescriptionType")
        
    def get_data(self):

        msg_data = []
        
        if self.condition_id is not None:
            msg_data.append({"conditionId": self.condition_id.get_data()})
        if self.commodity_type is not None:
            msg_data.append({"commodityType": self.commodity_type.get_data()})
        if self.positive_energy_direction is not None:
            msg_data.append({"positiveEnergyDirection": self.positive_energy_direction.get_data()})
        if self.label is not None:
            msg_data.append({"label": self.label.get_data()})
        if self.description is not None:
            msg_data.append({"description": self.description.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.condition_id is not None:
            result_str += f"{sep}conditionId: {self.condition_id}"
            sep = ", "
        if self.commodity_type is not None:
            result_str += f"{sep}commodityType: {self.commodity_type}"
            sep = ", "
        if self.positive_energy_direction is not None:
            result_str += f"{sep}positiveEnergyDirection: {self.positive_energy_direction}"
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
                condition_id=data_dict.get('conditionId'),
                commodity_type=data_dict.get('commodityType'),
                positive_energy_direction=data_dict.get('positiveEnergyDirection'),
                label=data_dict.get('label'),
                description=data_dict.get('description'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class SupplyConditionDataType: # EEBus_SPINE_TS_SupplyCondition.xsd: ComplexType
    def __init__(
            self,
            condition_id: ConditionIdType = None,
            timestamp: AbsoluteOrRelativeTimeType = None,
            event_type: SupplyConditionEventTypeType = None,
            originator: SupplyConditionOriginatorType = None,
            threshold_id: ThresholdIdType = None,
            threshold_percentage: ScaledNumberType = None,
            relevant_period: TimePeriodType = None,
            description: DescriptionType = None,
            grid_condition: GridConditionType = None,
    ):
        super().__init__()
        
        self.condition_id = condition_id
        self.timestamp = timestamp
        self.event_type = event_type
        self.originator = originator
        self.threshold_id = threshold_id
        self.threshold_percentage = threshold_percentage
        self.relevant_period = relevant_period
        self.description = description
        self.grid_condition = grid_condition

        if not isinstance(self.condition_id, ConditionIdType | NoneType):
            raise TypeError("condition_id is not of type ConditionIdType")
        
        if not isinstance(self.timestamp, AbsoluteOrRelativeTimeType | NoneType):
            raise TypeError("timestamp is not of type AbsoluteOrRelativeTimeType")
        
        if not isinstance(self.event_type, SupplyConditionEventTypeType | NoneType):
            raise TypeError("event_type is not of type SupplyConditionEventTypeType")
        
        if not isinstance(self.originator, SupplyConditionOriginatorType | NoneType):
            raise TypeError("originator is not of type SupplyConditionOriginatorType")
        
        if not isinstance(self.threshold_id, ThresholdIdType | NoneType):
            raise TypeError("threshold_id is not of type ThresholdIdType")
        
        if not isinstance(self.threshold_percentage, ScaledNumberType | NoneType):
            raise TypeError("threshold_percentage is not of type ScaledNumberType")
        
        if not isinstance(self.relevant_period, TimePeriodType | NoneType):
            raise TypeError("relevant_period is not of type TimePeriodType")
        
        if not isinstance(self.description, DescriptionType | NoneType):
            raise TypeError("description is not of type DescriptionType")
        
        if not isinstance(self.grid_condition, GridConditionType | NoneType):
            raise TypeError("grid_condition is not of type GridConditionType")
        
    def get_data(self):

        msg_data = []
        
        if self.condition_id is not None:
            msg_data.append({"conditionId": self.condition_id.get_data()})
        if self.timestamp is not None:
            msg_data.append({"timestamp": self.timestamp.get_data()})
        if self.event_type is not None:
            msg_data.append({"eventType": self.event_type.get_data()})
        if self.originator is not None:
            msg_data.append({"originator": self.originator.get_data()})
        if self.threshold_id is not None:
            msg_data.append({"thresholdId": self.threshold_id.get_data()})
        if self.threshold_percentage is not None:
            msg_data.append({"thresholdPercentage": self.threshold_percentage.get_data()})
        if self.relevant_period is not None:
            msg_data.append({"relevantPeriod": self.relevant_period.get_data()})
        if self.description is not None:
            msg_data.append({"description": self.description.get_data()})
        if self.grid_condition is not None:
            msg_data.append({"gridCondition": self.grid_condition.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.condition_id is not None:
            result_str += f"{sep}conditionId: {self.condition_id}"
            sep = ", "
        if self.timestamp is not None:
            result_str += f"{sep}timestamp: {self.timestamp}"
            sep = ", "
        if self.event_type is not None:
            result_str += f"{sep}eventType: {self.event_type}"
            sep = ", "
        if self.originator is not None:
            result_str += f"{sep}originator: {self.originator}"
            sep = ", "
        if self.threshold_id is not None:
            result_str += f"{sep}thresholdId: {self.threshold_id}"
            sep = ", "
        if self.threshold_percentage is not None:
            result_str += f"{sep}thresholdPercentage: {self.threshold_percentage}"
            sep = ", "
        if self.relevant_period is not None:
            result_str += f"{sep}relevantPeriod: {self.relevant_period}"
            sep = ", "
        if self.description is not None:
            result_str += f"{sep}description: {self.description}"
            sep = ", "
        if self.grid_condition is not None:
            result_str += f"{sep}gridCondition: {self.grid_condition}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                condition_id=data_dict.get('conditionId'),
                timestamp=data_dict.get('timestamp'),
                event_type=data_dict.get('eventType'),
                originator=data_dict.get('originator'),
                threshold_id=data_dict.get('thresholdId'),
                threshold_percentage=data_dict.get('thresholdPercentage'),
                relevant_period=data_dict.get('relevantPeriod'),
                description=data_dict.get('description'),
                grid_condition=data_dict.get('gridCondition'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class SupplyConditionThresholdRelationListDataType: # EEBus_SPINE_TS_SupplyCondition.xsd: ComplexType
    def __init__(
            self,
            supply_condition_threshold_relation_data: list[SupplyConditionThresholdRelationDataType] = None,
    ):
        super().__init__()
        
        self.supply_condition_threshold_relation_data = supply_condition_threshold_relation_data

        if not isinstance(self.supply_condition_threshold_relation_data, list | NoneType):
            raise TypeError("supply_condition_threshold_relation_data is not of type list[SupplyConditionThresholdRelationDataType]")
        
    def get_data(self):

        msg_data = []
        
        if self.supply_condition_threshold_relation_data is not None:
            msg_data.append({"supplyConditionThresholdRelationData": [d.get_data() for d in self.supply_condition_threshold_relation_data]})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.supply_condition_threshold_relation_data is not None:
            result_str += f"{sep}supplyConditionThresholdRelationData: {self.supply_condition_threshold_relation_data}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                supply_condition_threshold_relation_data=data_dict.get('supplyConditionThresholdRelationData'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class SupplyConditionDescriptionListDataType: # EEBus_SPINE_TS_SupplyCondition.xsd: ComplexType
    def __init__(
            self,
            supply_condition_description_data: list[SupplyConditionDescriptionDataType] = None,
    ):
        super().__init__()
        
        self.supply_condition_description_data = supply_condition_description_data

        if not isinstance(self.supply_condition_description_data, list | NoneType):
            raise TypeError("supply_condition_description_data is not of type list[SupplyConditionDescriptionDataType]")
        
    def get_data(self):

        msg_data = []
        
        if self.supply_condition_description_data is not None:
            msg_data.append({"supplyConditionDescriptionData": [d.get_data() for d in self.supply_condition_description_data]})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.supply_condition_description_data is not None:
            result_str += f"{sep}supplyConditionDescriptionData: {self.supply_condition_description_data}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                supply_condition_description_data=data_dict.get('supplyConditionDescriptionData'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class SupplyConditionListDataType: # EEBus_SPINE_TS_SupplyCondition.xsd: ComplexType
    def __init__(
            self,
            supply_condition_data: list[SupplyConditionDataType] = None,
    ):
        super().__init__()
        
        self.supply_condition_data = supply_condition_data

        if not isinstance(self.supply_condition_data, list | NoneType):
            raise TypeError("supply_condition_data is not of type list[SupplyConditionDataType]")
        
    def get_data(self):

        msg_data = []
        
        if self.supply_condition_data is not None:
            msg_data.append({"supplyConditionData": [d.get_data() for d in self.supply_condition_data]})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.supply_condition_data is not None:
            result_str += f"{sep}supplyConditionData: {self.supply_condition_data}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                supply_condition_data=data_dict.get('supplyConditionData'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class SupplyConditionThresholdRelationDataElementsType: # EEBus_SPINE_TS_SupplyCondition.xsd: ComplexType
    def __init__(
            self,
            condition_id: ElementTagType = None,
            threshold_id: ElementTagType = None,
    ):
        super().__init__()
        
        self.condition_id = condition_id
        self.threshold_id = threshold_id

        if not isinstance(self.condition_id, ElementTagType | NoneType):
            raise TypeError("condition_id is not of type ElementTagType")
        
        if not isinstance(self.threshold_id, ElementTagType | NoneType):
            raise TypeError("threshold_id is not of type ElementTagType")
        
    def get_data(self):

        msg_data = []
        
        if self.condition_id is not None:
            msg_data.append({"conditionId": self.condition_id.get_data()})
        if self.threshold_id is not None:
            msg_data.append({"thresholdId": self.threshold_id.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.condition_id is not None:
            result_str += f"{sep}conditionId: {self.condition_id}"
            sep = ", "
        if self.threshold_id is not None:
            result_str += f"{sep}thresholdId: {self.threshold_id}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                condition_id=data_dict.get('conditionId'),
                threshold_id=data_dict.get('thresholdId'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class SupplyConditionDescriptionDataElementsType: # EEBus_SPINE_TS_SupplyCondition.xsd: ComplexType
    def __init__(
            self,
            condition_id: ElementTagType = None,
            commodity_type: ElementTagType = None,
            positive_energy_direction: ElementTagType = None,
            label: ElementTagType = None,
            description: ElementTagType = None,
    ):
        super().__init__()
        
        self.condition_id = condition_id
        self.commodity_type = commodity_type
        self.positive_energy_direction = positive_energy_direction
        self.label = label
        self.description = description

        if not isinstance(self.condition_id, ElementTagType | NoneType):
            raise TypeError("condition_id is not of type ElementTagType")
        
        if not isinstance(self.commodity_type, ElementTagType | NoneType):
            raise TypeError("commodity_type is not of type ElementTagType")
        
        if not isinstance(self.positive_energy_direction, ElementTagType | NoneType):
            raise TypeError("positive_energy_direction is not of type ElementTagType")
        
        if not isinstance(self.label, ElementTagType | NoneType):
            raise TypeError("label is not of type ElementTagType")
        
        if not isinstance(self.description, ElementTagType | NoneType):
            raise TypeError("description is not of type ElementTagType")
        
    def get_data(self):

        msg_data = []
        
        if self.condition_id is not None:
            msg_data.append({"conditionId": self.condition_id.get_data()})
        if self.commodity_type is not None:
            msg_data.append({"commodityType": self.commodity_type.get_data()})
        if self.positive_energy_direction is not None:
            msg_data.append({"positiveEnergyDirection": self.positive_energy_direction.get_data()})
        if self.label is not None:
            msg_data.append({"label": self.label.get_data()})
        if self.description is not None:
            msg_data.append({"description": self.description.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.condition_id is not None:
            result_str += f"{sep}conditionId: {self.condition_id}"
            sep = ", "
        if self.commodity_type is not None:
            result_str += f"{sep}commodityType: {self.commodity_type}"
            sep = ", "
        if self.positive_energy_direction is not None:
            result_str += f"{sep}positiveEnergyDirection: {self.positive_energy_direction}"
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
                condition_id=data_dict.get('conditionId'),
                commodity_type=data_dict.get('commodityType'),
                positive_energy_direction=data_dict.get('positiveEnergyDirection'),
                label=data_dict.get('label'),
                description=data_dict.get('description'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class SupplyConditionDataElementsType: # EEBus_SPINE_TS_SupplyCondition.xsd: ComplexType
    def __init__(
            self,
            condition_id: ElementTagType = None,
            timestamp: ElementTagType = None,
            event_type: ElementTagType = None,
            originator: ElementTagType = None,
            threshold_id: ElementTagType = None,
            threshold_percentage: ScaledNumberElementsType = None,
            relevant_period: TimePeriodElementsType = None,
            description: ElementTagType = None,
            grid_condition: ElementTagType = None,
    ):
        super().__init__()
        
        self.condition_id = condition_id
        self.timestamp = timestamp
        self.event_type = event_type
        self.originator = originator
        self.threshold_id = threshold_id
        self.threshold_percentage = threshold_percentage
        self.relevant_period = relevant_period
        self.description = description
        self.grid_condition = grid_condition

        if not isinstance(self.condition_id, ElementTagType | NoneType):
            raise TypeError("condition_id is not of type ElementTagType")
        
        if not isinstance(self.timestamp, ElementTagType | NoneType):
            raise TypeError("timestamp is not of type ElementTagType")
        
        if not isinstance(self.event_type, ElementTagType | NoneType):
            raise TypeError("event_type is not of type ElementTagType")
        
        if not isinstance(self.originator, ElementTagType | NoneType):
            raise TypeError("originator is not of type ElementTagType")
        
        if not isinstance(self.threshold_id, ElementTagType | NoneType):
            raise TypeError("threshold_id is not of type ElementTagType")
        
        if not isinstance(self.threshold_percentage, ScaledNumberElementsType | NoneType):
            raise TypeError("threshold_percentage is not of type ScaledNumberElementsType")
        
        if not isinstance(self.relevant_period, TimePeriodElementsType | NoneType):
            raise TypeError("relevant_period is not of type TimePeriodElementsType")
        
        if not isinstance(self.description, ElementTagType | NoneType):
            raise TypeError("description is not of type ElementTagType")
        
        if not isinstance(self.grid_condition, ElementTagType | NoneType):
            raise TypeError("grid_condition is not of type ElementTagType")
        
    def get_data(self):

        msg_data = []
        
        if self.condition_id is not None:
            msg_data.append({"conditionId": self.condition_id.get_data()})
        if self.timestamp is not None:
            msg_data.append({"timestamp": self.timestamp.get_data()})
        if self.event_type is not None:
            msg_data.append({"eventType": self.event_type.get_data()})
        if self.originator is not None:
            msg_data.append({"originator": self.originator.get_data()})
        if self.threshold_id is not None:
            msg_data.append({"thresholdId": self.threshold_id.get_data()})
        if self.threshold_percentage is not None:
            msg_data.append({"thresholdPercentage": self.threshold_percentage.get_data()})
        if self.relevant_period is not None:
            msg_data.append({"relevantPeriod": self.relevant_period.get_data()})
        if self.description is not None:
            msg_data.append({"description": self.description.get_data()})
        if self.grid_condition is not None:
            msg_data.append({"gridCondition": self.grid_condition.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.condition_id is not None:
            result_str += f"{sep}conditionId: {self.condition_id}"
            sep = ", "
        if self.timestamp is not None:
            result_str += f"{sep}timestamp: {self.timestamp}"
            sep = ", "
        if self.event_type is not None:
            result_str += f"{sep}eventType: {self.event_type}"
            sep = ", "
        if self.originator is not None:
            result_str += f"{sep}originator: {self.originator}"
            sep = ", "
        if self.threshold_id is not None:
            result_str += f"{sep}thresholdId: {self.threshold_id}"
            sep = ", "
        if self.threshold_percentage is not None:
            result_str += f"{sep}thresholdPercentage: {self.threshold_percentage}"
            sep = ", "
        if self.relevant_period is not None:
            result_str += f"{sep}relevantPeriod: {self.relevant_period}"
            sep = ", "
        if self.description is not None:
            result_str += f"{sep}description: {self.description}"
            sep = ", "
        if self.grid_condition is not None:
            result_str += f"{sep}gridCondition: {self.grid_condition}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                condition_id=data_dict.get('conditionId'),
                timestamp=data_dict.get('timestamp'),
                event_type=data_dict.get('eventType'),
                originator=data_dict.get('originator'),
                threshold_id=data_dict.get('thresholdId'),
                threshold_percentage=data_dict.get('thresholdPercentage'),
                relevant_period=data_dict.get('relevantPeriod'),
                description=data_dict.get('description'),
                grid_condition=data_dict.get('gridCondition'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class SupplyConditionThresholdRelationListDataSelectorsType: # EEBus_SPINE_TS_SupplyCondition.xsd: ComplexType
    def __init__(
            self,
            condition_id: ConditionIdType = None,
            threshold_id: ThresholdIdType = None,
    ):
        super().__init__()
        
        self.condition_id = condition_id
        self.threshold_id = threshold_id

        if not isinstance(self.condition_id, ConditionIdType | NoneType):
            raise TypeError("condition_id is not of type ConditionIdType")
        
        if not isinstance(self.threshold_id, ThresholdIdType | NoneType):
            raise TypeError("threshold_id is not of type ThresholdIdType")
        
    def get_data(self):

        msg_data = []
        
        if self.condition_id is not None:
            msg_data.append({"conditionId": self.condition_id.get_data()})
        if self.threshold_id is not None:
            msg_data.append({"thresholdId": self.threshold_id.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.condition_id is not None:
            result_str += f"{sep}conditionId: {self.condition_id}"
            sep = ", "
        if self.threshold_id is not None:
            result_str += f"{sep}thresholdId: {self.threshold_id}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                condition_id=data_dict.get('conditionId'),
                threshold_id=data_dict.get('thresholdId'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class SupplyConditionListDataSelectorsType: # EEBus_SPINE_TS_SupplyCondition.xsd: ComplexType
    def __init__(
            self,
            condition_id: ConditionIdType = None,
            timestamp_interval: TimestampIntervalType = None,
            event_type: SupplyConditionEventTypeType = None,
            originator: SupplyConditionOriginatorType = None,
    ):
        super().__init__()
        
        self.condition_id = condition_id
        self.timestamp_interval = timestamp_interval
        self.event_type = event_type
        self.originator = originator

        if not isinstance(self.condition_id, ConditionIdType | NoneType):
            raise TypeError("condition_id is not of type ConditionIdType")
        
        if not isinstance(self.timestamp_interval, TimestampIntervalType | NoneType):
            raise TypeError("timestamp_interval is not of type TimestampIntervalType")
        
        if not isinstance(self.event_type, SupplyConditionEventTypeType | NoneType):
            raise TypeError("event_type is not of type SupplyConditionEventTypeType")
        
        if not isinstance(self.originator, SupplyConditionOriginatorType | NoneType):
            raise TypeError("originator is not of type SupplyConditionOriginatorType")
        
    def get_data(self):

        msg_data = []
        
        if self.condition_id is not None:
            msg_data.append({"conditionId": self.condition_id.get_data()})
        if self.timestamp_interval is not None:
            msg_data.append({"timestampInterval": self.timestamp_interval.get_data()})
        if self.event_type is not None:
            msg_data.append({"eventType": self.event_type.get_data()})
        if self.originator is not None:
            msg_data.append({"originator": self.originator.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.condition_id is not None:
            result_str += f"{sep}conditionId: {self.condition_id}"
            sep = ", "
        if self.timestamp_interval is not None:
            result_str += f"{sep}timestampInterval: {self.timestamp_interval}"
            sep = ", "
        if self.event_type is not None:
            result_str += f"{sep}eventType: {self.event_type}"
            sep = ", "
        if self.originator is not None:
            result_str += f"{sep}originator: {self.originator}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                condition_id=data_dict.get('conditionId'),
                timestamp_interval=data_dict.get('timestampInterval'),
                event_type=data_dict.get('eventType'),
                originator=data_dict.get('originator'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class SupplyConditionDescriptionListDataSelectorsType: # EEBus_SPINE_TS_SupplyCondition.xsd: ComplexType
    def __init__(
            self,
            condition_id: ConditionIdType = None,
    ):
        super().__init__()
        
        self.condition_id = condition_id

        if not isinstance(self.condition_id, ConditionIdType | NoneType):
            raise TypeError("condition_id is not of type ConditionIdType")
        
    def get_data(self):

        msg_data = []
        
        if self.condition_id is not None:
            msg_data.append({"conditionId": self.condition_id.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.condition_id is not None:
            result_str += f"{sep}conditionId: {self.condition_id}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                condition_id=data_dict.get('conditionId'),
            )
        elif data:
            return cls(data)
        else:
            return cls()



