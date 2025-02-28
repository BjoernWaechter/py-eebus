# Jinja Template message_type.py.jinja2
from spine.base_type.commondatatypes import ElementTagType
from spine.base_type.commondatatypes import ScaledNumberElementsType
from spine.base_type.commondatatypes import ScaledNumberType
from spine.base_type.commondatatypes import TimePeriodElementsType
from spine.base_type.commondatatypes import TimePeriodType
from spine.base_type.commondatatypes import TimestampIntervalType
from spine.simple_type.commondatatypes import DescriptionType
from spine.simple_type.commondatatypes import LabelType
from spine.simple_type.measurement import MeasurementIdType
from spine.simple_type.tariffinformation import CommodityIdType
from spine.simple_type.tariffinformation import IncentiveCountType
from spine.simple_type.tariffinformation import IncentiveIdType
from spine.simple_type.tariffinformation import IncentivePriorityType
from spine.simple_type.tariffinformation import TariffCountType
from spine.simple_type.tariffinformation import TariffIdType
from spine.simple_type.tariffinformation import TierBoundaryCountType
from spine.simple_type.tariffinformation import TierBoundaryIdType
from spine.simple_type.tariffinformation import TierCountType
from spine.simple_type.tariffinformation import TierIdType
from spine.simple_type.timetable import TimeTableIdType
from spine.union_type.commondatatypes import AbsoluteOrRelativeTimeType
from spine.union_type.commondatatypes import CommodityTypeType
from spine.union_type.commondatatypes import CurrencyType
from spine.union_type.commondatatypes import EnergyDirectionType
from spine.union_type.commondatatypes import ScopeTypeType
from spine.union_type.commondatatypes import UnitOfMeasurementType
from spine.union_type.tariffinformation import IncentiveTypeType
from spine.union_type.tariffinformation import IncentiveValueTypeType
from spine.union_type.tariffinformation import TierBoundaryTypeType
from spine.union_type.tariffinformation import TierTypeType
from types import NoneType
from spine import array_2_dict


class IncentiveDescriptionDataType: # EEBus_SPINE_TS_TariffInformation.xsd: ComplexType
    def __init__(
            self,
            incentive_id: IncentiveIdType = None,
            incentive_type: IncentiveTypeType = None,
            incentive_priority: IncentivePriorityType = None,
            currency: CurrencyType = None,
            unit: UnitOfMeasurementType = None,
            label: LabelType = None,
            description: DescriptionType = None,
    ):
        super().__init__()
        
        self.incentive_id = incentive_id
        self.incentive_type = incentive_type
        self.incentive_priority = incentive_priority
        self.currency = currency
        self.unit = unit
        self.label = label
        self.description = description

        if not isinstance(self.incentive_id, IncentiveIdType | NoneType):
            raise TypeError("incentive_id is not of type IncentiveIdType")
        
        if not isinstance(self.incentive_type, IncentiveTypeType | NoneType):
            raise TypeError("incentive_type is not of type IncentiveTypeType")
        
        if not isinstance(self.incentive_priority, IncentivePriorityType | NoneType):
            raise TypeError("incentive_priority is not of type IncentivePriorityType")
        
        if not isinstance(self.currency, CurrencyType | NoneType):
            raise TypeError("currency is not of type CurrencyType")
        
        if not isinstance(self.unit, UnitOfMeasurementType | NoneType):
            raise TypeError("unit is not of type UnitOfMeasurementType")
        
        if not isinstance(self.label, LabelType | NoneType):
            raise TypeError("label is not of type LabelType")
        
        if not isinstance(self.description, DescriptionType | NoneType):
            raise TypeError("description is not of type DescriptionType")
        
    def get_data(self):

        msg_data = []
        
        if self.incentive_id is not None:
            msg_data.append({"incentiveId": self.incentive_id.get_data()})
        if self.incentive_type is not None:
            msg_data.append({"incentiveType": self.incentive_type.get_data()})
        if self.incentive_priority is not None:
            msg_data.append({"incentivePriority": self.incentive_priority.get_data()})
        if self.currency is not None:
            msg_data.append({"currency": self.currency.get_data()})
        if self.unit is not None:
            msg_data.append({"unit": self.unit.get_data()})
        if self.label is not None:
            msg_data.append({"label": self.label.get_data()})
        if self.description is not None:
            msg_data.append({"description": self.description.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.incentive_id is not None:
            result_str += f"{sep}incentiveId: {self.incentive_id}"
            sep = ", "
        if self.incentive_type is not None:
            result_str += f"{sep}incentiveType: {self.incentive_type}"
            sep = ", "
        if self.incentive_priority is not None:
            result_str += f"{sep}incentivePriority: {self.incentive_priority}"
            sep = ", "
        if self.currency is not None:
            result_str += f"{sep}currency: {self.currency}"
            sep = ", "
        if self.unit is not None:
            result_str += f"{sep}unit: {self.unit}"
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
                incentive_id=data_dict.get('incentiveId'),
                incentive_type=data_dict.get('incentiveType'),
                incentive_priority=data_dict.get('incentivePriority'),
                currency=data_dict.get('currency'),
                unit=data_dict.get('unit'),
                label=data_dict.get('label'),
                description=data_dict.get('description'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class IncentiveDataType: # EEBus_SPINE_TS_TariffInformation.xsd: ComplexType
    def __init__(
            self,
            incentive_id: IncentiveIdType = None,
            value_type: IncentiveValueTypeType = None,
            timestamp: AbsoluteOrRelativeTimeType = None,
            time_period: TimePeriodType = None,
            time_table_id: TimeTableIdType = None,
            value: ScaledNumberType = None,
    ):
        super().__init__()
        
        self.incentive_id = incentive_id
        self.value_type = value_type
        self.timestamp = timestamp
        self.time_period = time_period
        self.time_table_id = time_table_id
        self.value = value

        if not isinstance(self.incentive_id, IncentiveIdType | NoneType):
            raise TypeError("incentive_id is not of type IncentiveIdType")
        
        if not isinstance(self.value_type, IncentiveValueTypeType | NoneType):
            raise TypeError("value_type is not of type IncentiveValueTypeType")
        
        if not isinstance(self.timestamp, AbsoluteOrRelativeTimeType | NoneType):
            raise TypeError("timestamp is not of type AbsoluteOrRelativeTimeType")
        
        if not isinstance(self.time_period, TimePeriodType | NoneType):
            raise TypeError("time_period is not of type TimePeriodType")
        
        if not isinstance(self.time_table_id, TimeTableIdType | NoneType):
            raise TypeError("time_table_id is not of type TimeTableIdType")
        
        if not isinstance(self.value, ScaledNumberType | NoneType):
            raise TypeError("value is not of type ScaledNumberType")
        
    def get_data(self):

        msg_data = []
        
        if self.incentive_id is not None:
            msg_data.append({"incentiveId": self.incentive_id.get_data()})
        if self.value_type is not None:
            msg_data.append({"valueType": self.value_type.get_data()})
        if self.timestamp is not None:
            msg_data.append({"timestamp": self.timestamp.get_data()})
        if self.time_period is not None:
            msg_data.append({"timePeriod": self.time_period.get_data()})
        if self.time_table_id is not None:
            msg_data.append({"timeTableId": self.time_table_id.get_data()})
        if self.value is not None:
            msg_data.append({"value": self.value.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.incentive_id is not None:
            result_str += f"{sep}incentiveId: {self.incentive_id}"
            sep = ", "
        if self.value_type is not None:
            result_str += f"{sep}valueType: {self.value_type}"
            sep = ", "
        if self.timestamp is not None:
            result_str += f"{sep}timestamp: {self.timestamp}"
            sep = ", "
        if self.time_period is not None:
            result_str += f"{sep}timePeriod: {self.time_period}"
            sep = ", "
        if self.time_table_id is not None:
            result_str += f"{sep}timeTableId: {self.time_table_id}"
            sep = ", "
        if self.value is not None:
            result_str += f"{sep}value: {self.value}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                incentive_id=data_dict.get('incentiveId'),
                value_type=data_dict.get('valueType'),
                timestamp=data_dict.get('timestamp'),
                time_period=data_dict.get('timePeriod'),
                time_table_id=data_dict.get('timeTableId'),
                value=data_dict.get('value'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class TierDescriptionDataType: # EEBus_SPINE_TS_TariffInformation.xsd: ComplexType
    def __init__(
            self,
            tier_id: TierIdType = None,
            tier_type: TierTypeType = None,
            label: LabelType = None,
            description: DescriptionType = None,
    ):
        super().__init__()
        
        self.tier_id = tier_id
        self.tier_type = tier_type
        self.label = label
        self.description = description

        if not isinstance(self.tier_id, TierIdType | NoneType):
            raise TypeError("tier_id is not of type TierIdType")
        
        if not isinstance(self.tier_type, TierTypeType | NoneType):
            raise TypeError("tier_type is not of type TierTypeType")
        
        if not isinstance(self.label, LabelType | NoneType):
            raise TypeError("label is not of type LabelType")
        
        if not isinstance(self.description, DescriptionType | NoneType):
            raise TypeError("description is not of type DescriptionType")
        
    def get_data(self):

        msg_data = []
        
        if self.tier_id is not None:
            msg_data.append({"tierId": self.tier_id.get_data()})
        if self.tier_type is not None:
            msg_data.append({"tierType": self.tier_type.get_data()})
        if self.label is not None:
            msg_data.append({"label": self.label.get_data()})
        if self.description is not None:
            msg_data.append({"description": self.description.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.tier_id is not None:
            result_str += f"{sep}tierId: {self.tier_id}"
            sep = ", "
        if self.tier_type is not None:
            result_str += f"{sep}tierType: {self.tier_type}"
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
                tier_id=data_dict.get('tierId'),
                tier_type=data_dict.get('tierType'),
                label=data_dict.get('label'),
                description=data_dict.get('description'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class TierIncentiveRelationDataType: # EEBus_SPINE_TS_TariffInformation.xsd: ComplexType
    def __init__(
            self,
            tier_id: TierIdType = None,
            incentive_id: list[IncentiveIdType] = None,
    ):
        super().__init__()
        
        self.tier_id = tier_id
        self.incentive_id = incentive_id

        if not isinstance(self.tier_id, TierIdType | NoneType):
            raise TypeError("tier_id is not of type TierIdType")
        
        if not isinstance(self.incentive_id, list | NoneType):
            raise TypeError("incentive_id is not of type list[IncentiveIdType]")
        
    def get_data(self):

        msg_data = []
        
        if self.tier_id is not None:
            msg_data.append({"tierId": self.tier_id.get_data()})
        if self.incentive_id is not None:
            msg_data.append({"incentiveId": [d.get_data() for d in self.incentive_id]})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.tier_id is not None:
            result_str += f"{sep}tierId: {self.tier_id}"
            sep = ", "
        if self.incentive_id is not None:
            result_str += f"{sep}incentiveId: {self.incentive_id}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                tier_id=data_dict.get('tierId'),
                incentive_id=data_dict.get('incentiveId'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class TierDataType: # EEBus_SPINE_TS_TariffInformation.xsd: ComplexType
    def __init__(
            self,
            tier_id: TierIdType = None,
            time_period: TimePeriodType = None,
            time_table_id: TimeTableIdType = None,
            active_incentive_id: list[IncentiveIdType] = None,
    ):
        super().__init__()
        
        self.tier_id = tier_id
        self.time_period = time_period
        self.time_table_id = time_table_id
        self.active_incentive_id = active_incentive_id

        if not isinstance(self.tier_id, TierIdType | NoneType):
            raise TypeError("tier_id is not of type TierIdType")
        
        if not isinstance(self.time_period, TimePeriodType | NoneType):
            raise TypeError("time_period is not of type TimePeriodType")
        
        if not isinstance(self.time_table_id, TimeTableIdType | NoneType):
            raise TypeError("time_table_id is not of type TimeTableIdType")
        
        if not isinstance(self.active_incentive_id, list | NoneType):
            raise TypeError("active_incentive_id is not of type list[IncentiveIdType]")
        
    def get_data(self):

        msg_data = []
        
        if self.tier_id is not None:
            msg_data.append({"tierId": self.tier_id.get_data()})
        if self.time_period is not None:
            msg_data.append({"timePeriod": self.time_period.get_data()})
        if self.time_table_id is not None:
            msg_data.append({"timeTableId": self.time_table_id.get_data()})
        if self.active_incentive_id is not None:
            msg_data.append({"activeIncentiveId": [d.get_data() for d in self.active_incentive_id]})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.tier_id is not None:
            result_str += f"{sep}tierId: {self.tier_id}"
            sep = ", "
        if self.time_period is not None:
            result_str += f"{sep}timePeriod: {self.time_period}"
            sep = ", "
        if self.time_table_id is not None:
            result_str += f"{sep}timeTableId: {self.time_table_id}"
            sep = ", "
        if self.active_incentive_id is not None:
            result_str += f"{sep}activeIncentiveId: {self.active_incentive_id}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                tier_id=data_dict.get('tierId'),
                time_period=data_dict.get('timePeriod'),
                time_table_id=data_dict.get('timeTableId'),
                active_incentive_id=data_dict.get('activeIncentiveId'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class CommodityDataType: # EEBus_SPINE_TS_TariffInformation.xsd: ComplexType
    def __init__(
            self,
            commodity_id: CommodityIdType = None,
            commodity_type: CommodityTypeType = None,
            positive_energy_direction: EnergyDirectionType = None,
            label: LabelType = None,
            description: DescriptionType = None,
    ):
        super().__init__()
        
        self.commodity_id = commodity_id
        self.commodity_type = commodity_type
        self.positive_energy_direction = positive_energy_direction
        self.label = label
        self.description = description

        if not isinstance(self.commodity_id, CommodityIdType | NoneType):
            raise TypeError("commodity_id is not of type CommodityIdType")
        
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
        
        if self.commodity_id is not None:
            msg_data.append({"commodityId": self.commodity_id.get_data()})
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
        if self.commodity_id is not None:
            result_str += f"{sep}commodityId: {self.commodity_id}"
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
                commodity_id=data_dict.get('commodityId'),
                commodity_type=data_dict.get('commodityType'),
                positive_energy_direction=data_dict.get('positiveEnergyDirection'),
                label=data_dict.get('label'),
                description=data_dict.get('description'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class TierBoundaryDescriptionDataType: # EEBus_SPINE_TS_TariffInformation.xsd: ComplexType
    def __init__(
            self,
            boundary_id: TierBoundaryIdType = None,
            boundary_type: TierBoundaryTypeType = None,
            valid_for_tier_id: TierIdType = None,
            switch_to_tier_id_when_lower: TierIdType = None,
            switch_to_tier_id_when_higher: TierIdType = None,
            boundary_unit: UnitOfMeasurementType = None,
            label: LabelType = None,
            description: DescriptionType = None,
    ):
        super().__init__()
        
        self.boundary_id = boundary_id
        self.boundary_type = boundary_type
        self.valid_for_tier_id = valid_for_tier_id
        self.switch_to_tier_id_when_lower = switch_to_tier_id_when_lower
        self.switch_to_tier_id_when_higher = switch_to_tier_id_when_higher
        self.boundary_unit = boundary_unit
        self.label = label
        self.description = description

        if not isinstance(self.boundary_id, TierBoundaryIdType | NoneType):
            raise TypeError("boundary_id is not of type TierBoundaryIdType")
        
        if not isinstance(self.boundary_type, TierBoundaryTypeType | NoneType):
            raise TypeError("boundary_type is not of type TierBoundaryTypeType")
        
        if not isinstance(self.valid_for_tier_id, TierIdType | NoneType):
            raise TypeError("valid_for_tier_id is not of type TierIdType")
        
        if not isinstance(self.switch_to_tier_id_when_lower, TierIdType | NoneType):
            raise TypeError("switch_to_tier_id_when_lower is not of type TierIdType")
        
        if not isinstance(self.switch_to_tier_id_when_higher, TierIdType | NoneType):
            raise TypeError("switch_to_tier_id_when_higher is not of type TierIdType")
        
        if not isinstance(self.boundary_unit, UnitOfMeasurementType | NoneType):
            raise TypeError("boundary_unit is not of type UnitOfMeasurementType")
        
        if not isinstance(self.label, LabelType | NoneType):
            raise TypeError("label is not of type LabelType")
        
        if not isinstance(self.description, DescriptionType | NoneType):
            raise TypeError("description is not of type DescriptionType")
        
    def get_data(self):

        msg_data = []
        
        if self.boundary_id is not None:
            msg_data.append({"boundaryId": self.boundary_id.get_data()})
        if self.boundary_type is not None:
            msg_data.append({"boundaryType": self.boundary_type.get_data()})
        if self.valid_for_tier_id is not None:
            msg_data.append({"validForTierId": self.valid_for_tier_id.get_data()})
        if self.switch_to_tier_id_when_lower is not None:
            msg_data.append({"switchToTierIdWhenLower": self.switch_to_tier_id_when_lower.get_data()})
        if self.switch_to_tier_id_when_higher is not None:
            msg_data.append({"switchToTierIdWhenHigher": self.switch_to_tier_id_when_higher.get_data()})
        if self.boundary_unit is not None:
            msg_data.append({"boundaryUnit": self.boundary_unit.get_data()})
        if self.label is not None:
            msg_data.append({"label": self.label.get_data()})
        if self.description is not None:
            msg_data.append({"description": self.description.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.boundary_id is not None:
            result_str += f"{sep}boundaryId: {self.boundary_id}"
            sep = ", "
        if self.boundary_type is not None:
            result_str += f"{sep}boundaryType: {self.boundary_type}"
            sep = ", "
        if self.valid_for_tier_id is not None:
            result_str += f"{sep}validForTierId: {self.valid_for_tier_id}"
            sep = ", "
        if self.switch_to_tier_id_when_lower is not None:
            result_str += f"{sep}switchToTierIdWhenLower: {self.switch_to_tier_id_when_lower}"
            sep = ", "
        if self.switch_to_tier_id_when_higher is not None:
            result_str += f"{sep}switchToTierIdWhenHigher: {self.switch_to_tier_id_when_higher}"
            sep = ", "
        if self.boundary_unit is not None:
            result_str += f"{sep}boundaryUnit: {self.boundary_unit}"
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
                boundary_id=data_dict.get('boundaryId'),
                boundary_type=data_dict.get('boundaryType'),
                valid_for_tier_id=data_dict.get('validForTierId'),
                switch_to_tier_id_when_lower=data_dict.get('switchToTierIdWhenLower'),
                switch_to_tier_id_when_higher=data_dict.get('switchToTierIdWhenHigher'),
                boundary_unit=data_dict.get('boundaryUnit'),
                label=data_dict.get('label'),
                description=data_dict.get('description'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class TierBoundaryDataType: # EEBus_SPINE_TS_TariffInformation.xsd: ComplexType
    def __init__(
            self,
            boundary_id: TierBoundaryIdType = None,
            time_period: TimePeriodType = None,
            time_table_id: TimeTableIdType = None,
            lower_boundary_value: ScaledNumberType = None,
            upper_boundary_value: ScaledNumberType = None,
    ):
        super().__init__()
        
        self.boundary_id = boundary_id
        self.time_period = time_period
        self.time_table_id = time_table_id
        self.lower_boundary_value = lower_boundary_value
        self.upper_boundary_value = upper_boundary_value

        if not isinstance(self.boundary_id, TierBoundaryIdType | NoneType):
            raise TypeError("boundary_id is not of type TierBoundaryIdType")
        
        if not isinstance(self.time_period, TimePeriodType | NoneType):
            raise TypeError("time_period is not of type TimePeriodType")
        
        if not isinstance(self.time_table_id, TimeTableIdType | NoneType):
            raise TypeError("time_table_id is not of type TimeTableIdType")
        
        if not isinstance(self.lower_boundary_value, ScaledNumberType | NoneType):
            raise TypeError("lower_boundary_value is not of type ScaledNumberType")
        
        if not isinstance(self.upper_boundary_value, ScaledNumberType | NoneType):
            raise TypeError("upper_boundary_value is not of type ScaledNumberType")
        
    def get_data(self):

        msg_data = []
        
        if self.boundary_id is not None:
            msg_data.append({"boundaryId": self.boundary_id.get_data()})
        if self.time_period is not None:
            msg_data.append({"timePeriod": self.time_period.get_data()})
        if self.time_table_id is not None:
            msg_data.append({"timeTableId": self.time_table_id.get_data()})
        if self.lower_boundary_value is not None:
            msg_data.append({"lowerBoundaryValue": self.lower_boundary_value.get_data()})
        if self.upper_boundary_value is not None:
            msg_data.append({"upperBoundaryValue": self.upper_boundary_value.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.boundary_id is not None:
            result_str += f"{sep}boundaryId: {self.boundary_id}"
            sep = ", "
        if self.time_period is not None:
            result_str += f"{sep}timePeriod: {self.time_period}"
            sep = ", "
        if self.time_table_id is not None:
            result_str += f"{sep}timeTableId: {self.time_table_id}"
            sep = ", "
        if self.lower_boundary_value is not None:
            result_str += f"{sep}lowerBoundaryValue: {self.lower_boundary_value}"
            sep = ", "
        if self.upper_boundary_value is not None:
            result_str += f"{sep}upperBoundaryValue: {self.upper_boundary_value}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                boundary_id=data_dict.get('boundaryId'),
                time_period=data_dict.get('timePeriod'),
                time_table_id=data_dict.get('timeTableId'),
                lower_boundary_value=data_dict.get('lowerBoundaryValue'),
                upper_boundary_value=data_dict.get('upperBoundaryValue'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class TariffDescriptionDataType: # EEBus_SPINE_TS_TariffInformation.xsd: ComplexType
    def __init__(
            self,
            tariff_id: TariffIdType = None,
            commodity_id: CommodityIdType = None,
            measurement_id: MeasurementIdType = None,
            tariff_writeable: bool = None,
            update_required: bool = None,
            scope_type: ScopeTypeType = None,
            label: LabelType = None,
            description: DescriptionType = None,
            slot_id_support: bool = None,
    ):
        super().__init__()
        
        self.tariff_id = tariff_id
        self.commodity_id = commodity_id
        self.measurement_id = measurement_id
        self.tariff_writeable = tariff_writeable
        self.update_required = update_required
        self.scope_type = scope_type
        self.label = label
        self.description = description
        self.slot_id_support = slot_id_support

        if not isinstance(self.tariff_id, TariffIdType | NoneType):
            raise TypeError("tariff_id is not of type TariffIdType")
        
        if not isinstance(self.commodity_id, CommodityIdType | NoneType):
            raise TypeError("commodity_id is not of type CommodityIdType")
        
        if not isinstance(self.measurement_id, MeasurementIdType | NoneType):
            raise TypeError("measurement_id is not of type MeasurementIdType")
        
        if not isinstance(self.tariff_writeable, bool | NoneType):
            raise TypeError("tariff_writeable is not of type bool")
        
        if not isinstance(self.update_required, bool | NoneType):
            raise TypeError("update_required is not of type bool")
        
        if not isinstance(self.scope_type, ScopeTypeType | NoneType):
            raise TypeError("scope_type is not of type ScopeTypeType")
        
        if not isinstance(self.label, LabelType | NoneType):
            raise TypeError("label is not of type LabelType")
        
        if not isinstance(self.description, DescriptionType | NoneType):
            raise TypeError("description is not of type DescriptionType")
        
        if not isinstance(self.slot_id_support, bool | NoneType):
            raise TypeError("slot_id_support is not of type bool")
        
    def get_data(self):

        msg_data = []
        
        if self.tariff_id is not None:
            msg_data.append({"tariffId": self.tariff_id.get_data()})
        if self.commodity_id is not None:
            msg_data.append({"commodityId": self.commodity_id.get_data()})
        if self.measurement_id is not None:
            msg_data.append({"measurementId": self.measurement_id.get_data()})
        if self.tariff_writeable is not None:
            msg_data.append({"tariffWriteable": self.tariff_writeable})
        if self.update_required is not None:
            msg_data.append({"updateRequired": self.update_required})
        if self.scope_type is not None:
            msg_data.append({"scopeType": self.scope_type.get_data()})
        if self.label is not None:
            msg_data.append({"label": self.label.get_data()})
        if self.description is not None:
            msg_data.append({"description": self.description.get_data()})
        if self.slot_id_support is not None:
            msg_data.append({"slotIdSupport": self.slot_id_support})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.tariff_id is not None:
            result_str += f"{sep}tariffId: {self.tariff_id}"
            sep = ", "
        if self.commodity_id is not None:
            result_str += f"{sep}commodityId: {self.commodity_id}"
            sep = ", "
        if self.measurement_id is not None:
            result_str += f"{sep}measurementId: {self.measurement_id}"
            sep = ", "
        if self.tariff_writeable is not None:
            result_str += f"{sep}tariffWriteable: {self.tariff_writeable}"
            sep = ", "
        if self.update_required is not None:
            result_str += f"{sep}updateRequired: {self.update_required}"
            sep = ", "
        if self.scope_type is not None:
            result_str += f"{sep}scopeType: {self.scope_type}"
            sep = ", "
        if self.label is not None:
            result_str += f"{sep}label: {self.label}"
            sep = ", "
        if self.description is not None:
            result_str += f"{sep}description: {self.description}"
            sep = ", "
        if self.slot_id_support is not None:
            result_str += f"{sep}slotIdSupport: {self.slot_id_support}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                tariff_id=data_dict.get('tariffId'),
                commodity_id=data_dict.get('commodityId'),
                measurement_id=data_dict.get('measurementId'),
                tariff_writeable=data_dict.get('tariffWriteable'),
                update_required=data_dict.get('updateRequired'),
                scope_type=data_dict.get('scopeType'),
                label=data_dict.get('label'),
                description=data_dict.get('description'),
                slot_id_support=data_dict.get('slotIdSupport'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class TariffBoundaryRelationDataType: # EEBus_SPINE_TS_TariffInformation.xsd: ComplexType
    def __init__(
            self,
            tariff_id: TariffIdType = None,
            boundary_id: list[TierBoundaryIdType] = None,
    ):
        super().__init__()
        
        self.tariff_id = tariff_id
        self.boundary_id = boundary_id

        if not isinstance(self.tariff_id, TariffIdType | NoneType):
            raise TypeError("tariff_id is not of type TariffIdType")
        
        if not isinstance(self.boundary_id, list | NoneType):
            raise TypeError("boundary_id is not of type list[TierBoundaryIdType]")
        
    def get_data(self):

        msg_data = []
        
        if self.tariff_id is not None:
            msg_data.append({"tariffId": self.tariff_id.get_data()})
        if self.boundary_id is not None:
            msg_data.append({"boundaryId": [d.get_data() for d in self.boundary_id]})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.tariff_id is not None:
            result_str += f"{sep}tariffId: {self.tariff_id}"
            sep = ", "
        if self.boundary_id is not None:
            result_str += f"{sep}boundaryId: {self.boundary_id}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                tariff_id=data_dict.get('tariffId'),
                boundary_id=data_dict.get('boundaryId'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class TariffTierRelationDataType: # EEBus_SPINE_TS_TariffInformation.xsd: ComplexType
    def __init__(
            self,
            tariff_id: TariffIdType = None,
            tier_id: list[TierIdType] = None,
    ):
        super().__init__()
        
        self.tariff_id = tariff_id
        self.tier_id = tier_id

        if not isinstance(self.tariff_id, TariffIdType | NoneType):
            raise TypeError("tariff_id is not of type TariffIdType")
        
        if not isinstance(self.tier_id, list | NoneType):
            raise TypeError("tier_id is not of type list[TierIdType]")
        
    def get_data(self):

        msg_data = []
        
        if self.tariff_id is not None:
            msg_data.append({"tariffId": self.tariff_id.get_data()})
        if self.tier_id is not None:
            msg_data.append({"tierId": [d.get_data() for d in self.tier_id]})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.tariff_id is not None:
            result_str += f"{sep}tariffId: {self.tariff_id}"
            sep = ", "
        if self.tier_id is not None:
            result_str += f"{sep}tierId: {self.tier_id}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                tariff_id=data_dict.get('tariffId'),
                tier_id=data_dict.get('tierId'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class TariffDataType: # EEBus_SPINE_TS_TariffInformation.xsd: ComplexType
    def __init__(
            self,
            tariff_id: TariffIdType = None,
            active_tier_id: list[TierIdType] = None,
    ):
        super().__init__()
        
        self.tariff_id = tariff_id
        self.active_tier_id = active_tier_id

        if not isinstance(self.tariff_id, TariffIdType | NoneType):
            raise TypeError("tariff_id is not of type TariffIdType")
        
        if not isinstance(self.active_tier_id, list | NoneType):
            raise TypeError("active_tier_id is not of type list[TierIdType]")
        
    def get_data(self):

        msg_data = []
        
        if self.tariff_id is not None:
            msg_data.append({"tariffId": self.tariff_id.get_data()})
        if self.active_tier_id is not None:
            msg_data.append({"activeTierId": [d.get_data() for d in self.active_tier_id]})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.tariff_id is not None:
            result_str += f"{sep}tariffId: {self.tariff_id}"
            sep = ", "
        if self.active_tier_id is not None:
            result_str += f"{sep}activeTierId: {self.active_tier_id}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                tariff_id=data_dict.get('tariffId'),
                active_tier_id=data_dict.get('activeTierId'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class IncentiveDescriptionListDataType: # EEBus_SPINE_TS_TariffInformation.xsd: ComplexType
    def __init__(
            self,
            incentive_description_data: list[IncentiveDescriptionDataType] = None,
    ):
        super().__init__()
        
        self.incentive_description_data = incentive_description_data

        if not isinstance(self.incentive_description_data, list | NoneType):
            raise TypeError("incentive_description_data is not of type list[IncentiveDescriptionDataType]")
        
    def get_data(self):

        msg_data = []
        
        if self.incentive_description_data is not None:
            msg_data.append({"incentiveDescriptionData": [d.get_data() for d in self.incentive_description_data]})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.incentive_description_data is not None:
            result_str += f"{sep}incentiveDescriptionData: {self.incentive_description_data}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                incentive_description_data=data_dict.get('incentiveDescriptionData'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class IncentiveListDataType: # EEBus_SPINE_TS_TariffInformation.xsd: ComplexType
    def __init__(
            self,
            incentive_data: list[IncentiveDataType] = None,
    ):
        super().__init__()
        
        self.incentive_data = incentive_data

        if not isinstance(self.incentive_data, list | NoneType):
            raise TypeError("incentive_data is not of type list[IncentiveDataType]")
        
    def get_data(self):

        msg_data = []
        
        if self.incentive_data is not None:
            msg_data.append({"incentiveData": [d.get_data() for d in self.incentive_data]})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.incentive_data is not None:
            result_str += f"{sep}incentiveData: {self.incentive_data}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                incentive_data=data_dict.get('incentiveData'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class TierDescriptionListDataType: # EEBus_SPINE_TS_TariffInformation.xsd: ComplexType
    def __init__(
            self,
            tier_description_data: list[TierDescriptionDataType] = None,
    ):
        super().__init__()
        
        self.tier_description_data = tier_description_data

        if not isinstance(self.tier_description_data, list | NoneType):
            raise TypeError("tier_description_data is not of type list[TierDescriptionDataType]")
        
    def get_data(self):

        msg_data = []
        
        if self.tier_description_data is not None:
            msg_data.append({"tierDescriptionData": [d.get_data() for d in self.tier_description_data]})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.tier_description_data is not None:
            result_str += f"{sep}tierDescriptionData: {self.tier_description_data}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                tier_description_data=data_dict.get('tierDescriptionData'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class TierIncentiveRelationListDataType: # EEBus_SPINE_TS_TariffInformation.xsd: ComplexType
    def __init__(
            self,
            tier_incentive_relation_data: list[TierIncentiveRelationDataType] = None,
    ):
        super().__init__()
        
        self.tier_incentive_relation_data = tier_incentive_relation_data

        if not isinstance(self.tier_incentive_relation_data, list | NoneType):
            raise TypeError("tier_incentive_relation_data is not of type list[TierIncentiveRelationDataType]")
        
    def get_data(self):

        msg_data = []
        
        if self.tier_incentive_relation_data is not None:
            msg_data.append({"tierIncentiveRelationData": [d.get_data() for d in self.tier_incentive_relation_data]})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.tier_incentive_relation_data is not None:
            result_str += f"{sep}tierIncentiveRelationData: {self.tier_incentive_relation_data}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                tier_incentive_relation_data=data_dict.get('tierIncentiveRelationData'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class TierListDataType: # EEBus_SPINE_TS_TariffInformation.xsd: ComplexType
    def __init__(
            self,
            tier_data: list[TierDataType] = None,
    ):
        super().__init__()
        
        self.tier_data = tier_data

        if not isinstance(self.tier_data, list | NoneType):
            raise TypeError("tier_data is not of type list[TierDataType]")
        
    def get_data(self):

        msg_data = []
        
        if self.tier_data is not None:
            msg_data.append({"tierData": [d.get_data() for d in self.tier_data]})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.tier_data is not None:
            result_str += f"{sep}tierData: {self.tier_data}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                tier_data=data_dict.get('tierData'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class CommodityListDataType: # EEBus_SPINE_TS_TariffInformation.xsd: ComplexType
    def __init__(
            self,
            commodity_data: list[CommodityDataType] = None,
    ):
        super().__init__()
        
        self.commodity_data = commodity_data

        if not isinstance(self.commodity_data, list | NoneType):
            raise TypeError("commodity_data is not of type list[CommodityDataType]")
        
    def get_data(self):

        msg_data = []
        
        if self.commodity_data is not None:
            msg_data.append({"commodityData": [d.get_data() for d in self.commodity_data]})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.commodity_data is not None:
            result_str += f"{sep}commodityData: {self.commodity_data}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                commodity_data=data_dict.get('commodityData'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class TierBoundaryDescriptionListDataType: # EEBus_SPINE_TS_TariffInformation.xsd: ComplexType
    def __init__(
            self,
            tier_boundary_description_data: list[TierBoundaryDescriptionDataType] = None,
    ):
        super().__init__()
        
        self.tier_boundary_description_data = tier_boundary_description_data

        if not isinstance(self.tier_boundary_description_data, list | NoneType):
            raise TypeError("tier_boundary_description_data is not of type list[TierBoundaryDescriptionDataType]")
        
    def get_data(self):

        msg_data = []
        
        if self.tier_boundary_description_data is not None:
            msg_data.append({"tierBoundaryDescriptionData": [d.get_data() for d in self.tier_boundary_description_data]})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.tier_boundary_description_data is not None:
            result_str += f"{sep}tierBoundaryDescriptionData: {self.tier_boundary_description_data}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                tier_boundary_description_data=data_dict.get('tierBoundaryDescriptionData'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class TierBoundaryListDataType: # EEBus_SPINE_TS_TariffInformation.xsd: ComplexType
    def __init__(
            self,
            tier_boundary_data: list[TierBoundaryDataType] = None,
    ):
        super().__init__()
        
        self.tier_boundary_data = tier_boundary_data

        if not isinstance(self.tier_boundary_data, list | NoneType):
            raise TypeError("tier_boundary_data is not of type list[TierBoundaryDataType]")
        
    def get_data(self):

        msg_data = []
        
        if self.tier_boundary_data is not None:
            msg_data.append({"tierBoundaryData": [d.get_data() for d in self.tier_boundary_data]})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.tier_boundary_data is not None:
            result_str += f"{sep}tierBoundaryData: {self.tier_boundary_data}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                tier_boundary_data=data_dict.get('tierBoundaryData'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class TariffDescriptionListDataType: # EEBus_SPINE_TS_TariffInformation.xsd: ComplexType
    def __init__(
            self,
            tariff_description_data: list[TariffDescriptionDataType] = None,
    ):
        super().__init__()
        
        self.tariff_description_data = tariff_description_data

        if not isinstance(self.tariff_description_data, list | NoneType):
            raise TypeError("tariff_description_data is not of type list[TariffDescriptionDataType]")
        
    def get_data(self):

        msg_data = []
        
        if self.tariff_description_data is not None:
            msg_data.append({"tariffDescriptionData": [d.get_data() for d in self.tariff_description_data]})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.tariff_description_data is not None:
            result_str += f"{sep}tariffDescriptionData: {self.tariff_description_data}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                tariff_description_data=data_dict.get('tariffDescriptionData'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class TariffBoundaryRelationListDataType: # EEBus_SPINE_TS_TariffInformation.xsd: ComplexType
    def __init__(
            self,
            tariff_boundary_relation_data: list[TariffBoundaryRelationDataType] = None,
    ):
        super().__init__()
        
        self.tariff_boundary_relation_data = tariff_boundary_relation_data

        if not isinstance(self.tariff_boundary_relation_data, list | NoneType):
            raise TypeError("tariff_boundary_relation_data is not of type list[TariffBoundaryRelationDataType]")
        
    def get_data(self):

        msg_data = []
        
        if self.tariff_boundary_relation_data is not None:
            msg_data.append({"tariffBoundaryRelationData": [d.get_data() for d in self.tariff_boundary_relation_data]})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.tariff_boundary_relation_data is not None:
            result_str += f"{sep}tariffBoundaryRelationData: {self.tariff_boundary_relation_data}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                tariff_boundary_relation_data=data_dict.get('tariffBoundaryRelationData'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class TariffTierRelationListDataType: # EEBus_SPINE_TS_TariffInformation.xsd: ComplexType
    def __init__(
            self,
            tariff_tier_relation_data: list[TariffTierRelationDataType] = None,
    ):
        super().__init__()
        
        self.tariff_tier_relation_data = tariff_tier_relation_data

        if not isinstance(self.tariff_tier_relation_data, list | NoneType):
            raise TypeError("tariff_tier_relation_data is not of type list[TariffTierRelationDataType]")
        
    def get_data(self):

        msg_data = []
        
        if self.tariff_tier_relation_data is not None:
            msg_data.append({"tariffTierRelationData": [d.get_data() for d in self.tariff_tier_relation_data]})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.tariff_tier_relation_data is not None:
            result_str += f"{sep}tariffTierRelationData: {self.tariff_tier_relation_data}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                tariff_tier_relation_data=data_dict.get('tariffTierRelationData'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class TariffListDataType: # EEBus_SPINE_TS_TariffInformation.xsd: ComplexType
    def __init__(
            self,
            tariff_data: list[TariffDataType] = None,
    ):
        super().__init__()
        
        self.tariff_data = tariff_data

        if not isinstance(self.tariff_data, list | NoneType):
            raise TypeError("tariff_data is not of type list[TariffDataType]")
        
    def get_data(self):

        msg_data = []
        
        if self.tariff_data is not None:
            msg_data.append({"tariffData": [d.get_data() for d in self.tariff_data]})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.tariff_data is not None:
            result_str += f"{sep}tariffData: {self.tariff_data}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                tariff_data=data_dict.get('tariffData'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class TariffOverallConstraintsDataType: # EEBus_SPINE_TS_TariffInformation.xsd: ComplexType
    def __init__(
            self,
            max_tariff_count: TariffCountType = None,
            max_boundary_count: TierBoundaryCountType = None,
            max_tier_count: TierCountType = None,
            max_incentive_count: IncentiveCountType = None,
            max_boundaries_per_tariff: TierBoundaryCountType = None,
            max_tiers_per_tariff: TierCountType = None,
            max_boundaries_per_tier: TierBoundaryCountType = None,
            max_incentives_per_tier: IncentiveCountType = None,
    ):
        super().__init__()
        
        self.max_tariff_count = max_tariff_count
        self.max_boundary_count = max_boundary_count
        self.max_tier_count = max_tier_count
        self.max_incentive_count = max_incentive_count
        self.max_boundaries_per_tariff = max_boundaries_per_tariff
        self.max_tiers_per_tariff = max_tiers_per_tariff
        self.max_boundaries_per_tier = max_boundaries_per_tier
        self.max_incentives_per_tier = max_incentives_per_tier

        if not isinstance(self.max_tariff_count, TariffCountType | NoneType):
            raise TypeError("max_tariff_count is not of type TariffCountType")
        
        if not isinstance(self.max_boundary_count, TierBoundaryCountType | NoneType):
            raise TypeError("max_boundary_count is not of type TierBoundaryCountType")
        
        if not isinstance(self.max_tier_count, TierCountType | NoneType):
            raise TypeError("max_tier_count is not of type TierCountType")
        
        if not isinstance(self.max_incentive_count, IncentiveCountType | NoneType):
            raise TypeError("max_incentive_count is not of type IncentiveCountType")
        
        if not isinstance(self.max_boundaries_per_tariff, TierBoundaryCountType | NoneType):
            raise TypeError("max_boundaries_per_tariff is not of type TierBoundaryCountType")
        
        if not isinstance(self.max_tiers_per_tariff, TierCountType | NoneType):
            raise TypeError("max_tiers_per_tariff is not of type TierCountType")
        
        if not isinstance(self.max_boundaries_per_tier, TierBoundaryCountType | NoneType):
            raise TypeError("max_boundaries_per_tier is not of type TierBoundaryCountType")
        
        if not isinstance(self.max_incentives_per_tier, IncentiveCountType | NoneType):
            raise TypeError("max_incentives_per_tier is not of type IncentiveCountType")
        
    def get_data(self):

        msg_data = []
        
        if self.max_tariff_count is not None:
            msg_data.append({"maxTariffCount": self.max_tariff_count.get_data()})
        if self.max_boundary_count is not None:
            msg_data.append({"maxBoundaryCount": self.max_boundary_count.get_data()})
        if self.max_tier_count is not None:
            msg_data.append({"maxTierCount": self.max_tier_count.get_data()})
        if self.max_incentive_count is not None:
            msg_data.append({"maxIncentiveCount": self.max_incentive_count.get_data()})
        if self.max_boundaries_per_tariff is not None:
            msg_data.append({"maxBoundariesPerTariff": self.max_boundaries_per_tariff.get_data()})
        if self.max_tiers_per_tariff is not None:
            msg_data.append({"maxTiersPerTariff": self.max_tiers_per_tariff.get_data()})
        if self.max_boundaries_per_tier is not None:
            msg_data.append({"maxBoundariesPerTier": self.max_boundaries_per_tier.get_data()})
        if self.max_incentives_per_tier is not None:
            msg_data.append({"maxIncentivesPerTier": self.max_incentives_per_tier.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.max_tariff_count is not None:
            result_str += f"{sep}maxTariffCount: {self.max_tariff_count}"
            sep = ", "
        if self.max_boundary_count is not None:
            result_str += f"{sep}maxBoundaryCount: {self.max_boundary_count}"
            sep = ", "
        if self.max_tier_count is not None:
            result_str += f"{sep}maxTierCount: {self.max_tier_count}"
            sep = ", "
        if self.max_incentive_count is not None:
            result_str += f"{sep}maxIncentiveCount: {self.max_incentive_count}"
            sep = ", "
        if self.max_boundaries_per_tariff is not None:
            result_str += f"{sep}maxBoundariesPerTariff: {self.max_boundaries_per_tariff}"
            sep = ", "
        if self.max_tiers_per_tariff is not None:
            result_str += f"{sep}maxTiersPerTariff: {self.max_tiers_per_tariff}"
            sep = ", "
        if self.max_boundaries_per_tier is not None:
            result_str += f"{sep}maxBoundariesPerTier: {self.max_boundaries_per_tier}"
            sep = ", "
        if self.max_incentives_per_tier is not None:
            result_str += f"{sep}maxIncentivesPerTier: {self.max_incentives_per_tier}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                max_tariff_count=data_dict.get('maxTariffCount'),
                max_boundary_count=data_dict.get('maxBoundaryCount'),
                max_tier_count=data_dict.get('maxTierCount'),
                max_incentive_count=data_dict.get('maxIncentiveCount'),
                max_boundaries_per_tariff=data_dict.get('maxBoundariesPerTariff'),
                max_tiers_per_tariff=data_dict.get('maxTiersPerTariff'),
                max_boundaries_per_tier=data_dict.get('maxBoundariesPerTier'),
                max_incentives_per_tier=data_dict.get('maxIncentivesPerTier'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class TierIncentiveRelationDataElementsType: # EEBus_SPINE_TS_TariffInformation.xsd: ComplexType
    def __init__(
            self,
            tier_id: ElementTagType = None,
            incentive_id: ElementTagType = None,
    ):
        super().__init__()
        
        self.tier_id = tier_id
        self.incentive_id = incentive_id

        if not isinstance(self.tier_id, ElementTagType | NoneType):
            raise TypeError("tier_id is not of type ElementTagType")
        
        if not isinstance(self.incentive_id, ElementTagType | NoneType):
            raise TypeError("incentive_id is not of type ElementTagType")
        
    def get_data(self):

        msg_data = []
        
        if self.tier_id is not None:
            msg_data.append({"tierId": self.tier_id.get_data()})
        if self.incentive_id is not None:
            msg_data.append({"incentiveId": self.incentive_id.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.tier_id is not None:
            result_str += f"{sep}tierId: {self.tier_id}"
            sep = ", "
        if self.incentive_id is not None:
            result_str += f"{sep}incentiveId: {self.incentive_id}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                tier_id=data_dict.get('tierId'),
                incentive_id=data_dict.get('incentiveId'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class TierDescriptionDataElementsType: # EEBus_SPINE_TS_TariffInformation.xsd: ComplexType
    def __init__(
            self,
            tier_id: ElementTagType = None,
            tier_type: ElementTagType = None,
            label: ElementTagType = None,
            description: ElementTagType = None,
    ):
        super().__init__()
        
        self.tier_id = tier_id
        self.tier_type = tier_type
        self.label = label
        self.description = description

        if not isinstance(self.tier_id, ElementTagType | NoneType):
            raise TypeError("tier_id is not of type ElementTagType")
        
        if not isinstance(self.tier_type, ElementTagType | NoneType):
            raise TypeError("tier_type is not of type ElementTagType")
        
        if not isinstance(self.label, ElementTagType | NoneType):
            raise TypeError("label is not of type ElementTagType")
        
        if not isinstance(self.description, ElementTagType | NoneType):
            raise TypeError("description is not of type ElementTagType")
        
    def get_data(self):

        msg_data = []
        
        if self.tier_id is not None:
            msg_data.append({"tierId": self.tier_id.get_data()})
        if self.tier_type is not None:
            msg_data.append({"tierType": self.tier_type.get_data()})
        if self.label is not None:
            msg_data.append({"label": self.label.get_data()})
        if self.description is not None:
            msg_data.append({"description": self.description.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.tier_id is not None:
            result_str += f"{sep}tierId: {self.tier_id}"
            sep = ", "
        if self.tier_type is not None:
            result_str += f"{sep}tierType: {self.tier_type}"
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
                tier_id=data_dict.get('tierId'),
                tier_type=data_dict.get('tierType'),
                label=data_dict.get('label'),
                description=data_dict.get('description'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class TierDataElementsType: # EEBus_SPINE_TS_TariffInformation.xsd: ComplexType
    def __init__(
            self,
            tier_id: ElementTagType = None,
            time_period: TimePeriodElementsType = None,
            time_table_id: ElementTagType = None,
            active_incentive_id: ElementTagType = None,
    ):
        super().__init__()
        
        self.tier_id = tier_id
        self.time_period = time_period
        self.time_table_id = time_table_id
        self.active_incentive_id = active_incentive_id

        if not isinstance(self.tier_id, ElementTagType | NoneType):
            raise TypeError("tier_id is not of type ElementTagType")
        
        if not isinstance(self.time_period, TimePeriodElementsType | NoneType):
            raise TypeError("time_period is not of type TimePeriodElementsType")
        
        if not isinstance(self.time_table_id, ElementTagType | NoneType):
            raise TypeError("time_table_id is not of type ElementTagType")
        
        if not isinstance(self.active_incentive_id, ElementTagType | NoneType):
            raise TypeError("active_incentive_id is not of type ElementTagType")
        
    def get_data(self):

        msg_data = []
        
        if self.tier_id is not None:
            msg_data.append({"tierId": self.tier_id.get_data()})
        if self.time_period is not None:
            msg_data.append({"timePeriod": self.time_period.get_data()})
        if self.time_table_id is not None:
            msg_data.append({"timeTableId": self.time_table_id.get_data()})
        if self.active_incentive_id is not None:
            msg_data.append({"activeIncentiveId": self.active_incentive_id.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.tier_id is not None:
            result_str += f"{sep}tierId: {self.tier_id}"
            sep = ", "
        if self.time_period is not None:
            result_str += f"{sep}timePeriod: {self.time_period}"
            sep = ", "
        if self.time_table_id is not None:
            result_str += f"{sep}timeTableId: {self.time_table_id}"
            sep = ", "
        if self.active_incentive_id is not None:
            result_str += f"{sep}activeIncentiveId: {self.active_incentive_id}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                tier_id=data_dict.get('tierId'),
                time_period=data_dict.get('timePeriod'),
                time_table_id=data_dict.get('timeTableId'),
                active_incentive_id=data_dict.get('activeIncentiveId'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class TierBoundaryDescriptionDataElementsType: # EEBus_SPINE_TS_TariffInformation.xsd: ComplexType
    def __init__(
            self,
            boundary_id: ElementTagType = None,
            boundary_type: ElementTagType = None,
            valid_for_tier_id: ElementTagType = None,
            switch_to_tier_id_when_lower: ElementTagType = None,
            switch_to_tier_id_when_higher: ElementTagType = None,
            boundary_unit: ElementTagType = None,
            label: ElementTagType = None,
            description: ElementTagType = None,
    ):
        super().__init__()
        
        self.boundary_id = boundary_id
        self.boundary_type = boundary_type
        self.valid_for_tier_id = valid_for_tier_id
        self.switch_to_tier_id_when_lower = switch_to_tier_id_when_lower
        self.switch_to_tier_id_when_higher = switch_to_tier_id_when_higher
        self.boundary_unit = boundary_unit
        self.label = label
        self.description = description

        if not isinstance(self.boundary_id, ElementTagType | NoneType):
            raise TypeError("boundary_id is not of type ElementTagType")
        
        if not isinstance(self.boundary_type, ElementTagType | NoneType):
            raise TypeError("boundary_type is not of type ElementTagType")
        
        if not isinstance(self.valid_for_tier_id, ElementTagType | NoneType):
            raise TypeError("valid_for_tier_id is not of type ElementTagType")
        
        if not isinstance(self.switch_to_tier_id_when_lower, ElementTagType | NoneType):
            raise TypeError("switch_to_tier_id_when_lower is not of type ElementTagType")
        
        if not isinstance(self.switch_to_tier_id_when_higher, ElementTagType | NoneType):
            raise TypeError("switch_to_tier_id_when_higher is not of type ElementTagType")
        
        if not isinstance(self.boundary_unit, ElementTagType | NoneType):
            raise TypeError("boundary_unit is not of type ElementTagType")
        
        if not isinstance(self.label, ElementTagType | NoneType):
            raise TypeError("label is not of type ElementTagType")
        
        if not isinstance(self.description, ElementTagType | NoneType):
            raise TypeError("description is not of type ElementTagType")
        
    def get_data(self):

        msg_data = []
        
        if self.boundary_id is not None:
            msg_data.append({"boundaryId": self.boundary_id.get_data()})
        if self.boundary_type is not None:
            msg_data.append({"boundaryType": self.boundary_type.get_data()})
        if self.valid_for_tier_id is not None:
            msg_data.append({"validForTierId": self.valid_for_tier_id.get_data()})
        if self.switch_to_tier_id_when_lower is not None:
            msg_data.append({"switchToTierIdWhenLower": self.switch_to_tier_id_when_lower.get_data()})
        if self.switch_to_tier_id_when_higher is not None:
            msg_data.append({"switchToTierIdWhenHigher": self.switch_to_tier_id_when_higher.get_data()})
        if self.boundary_unit is not None:
            msg_data.append({"boundaryUnit": self.boundary_unit.get_data()})
        if self.label is not None:
            msg_data.append({"label": self.label.get_data()})
        if self.description is not None:
            msg_data.append({"description": self.description.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.boundary_id is not None:
            result_str += f"{sep}boundaryId: {self.boundary_id}"
            sep = ", "
        if self.boundary_type is not None:
            result_str += f"{sep}boundaryType: {self.boundary_type}"
            sep = ", "
        if self.valid_for_tier_id is not None:
            result_str += f"{sep}validForTierId: {self.valid_for_tier_id}"
            sep = ", "
        if self.switch_to_tier_id_when_lower is not None:
            result_str += f"{sep}switchToTierIdWhenLower: {self.switch_to_tier_id_when_lower}"
            sep = ", "
        if self.switch_to_tier_id_when_higher is not None:
            result_str += f"{sep}switchToTierIdWhenHigher: {self.switch_to_tier_id_when_higher}"
            sep = ", "
        if self.boundary_unit is not None:
            result_str += f"{sep}boundaryUnit: {self.boundary_unit}"
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
                boundary_id=data_dict.get('boundaryId'),
                boundary_type=data_dict.get('boundaryType'),
                valid_for_tier_id=data_dict.get('validForTierId'),
                switch_to_tier_id_when_lower=data_dict.get('switchToTierIdWhenLower'),
                switch_to_tier_id_when_higher=data_dict.get('switchToTierIdWhenHigher'),
                boundary_unit=data_dict.get('boundaryUnit'),
                label=data_dict.get('label'),
                description=data_dict.get('description'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class TierBoundaryDataElementsType: # EEBus_SPINE_TS_TariffInformation.xsd: ComplexType
    def __init__(
            self,
            boundary_id: ElementTagType = None,
            time_period: TimePeriodElementsType = None,
            time_table_id: ElementTagType = None,
            lower_boundary_value: ScaledNumberElementsType = None,
            upper_boundary_value: ScaledNumberElementsType = None,
    ):
        super().__init__()
        
        self.boundary_id = boundary_id
        self.time_period = time_period
        self.time_table_id = time_table_id
        self.lower_boundary_value = lower_boundary_value
        self.upper_boundary_value = upper_boundary_value

        if not isinstance(self.boundary_id, ElementTagType | NoneType):
            raise TypeError("boundary_id is not of type ElementTagType")
        
        if not isinstance(self.time_period, TimePeriodElementsType | NoneType):
            raise TypeError("time_period is not of type TimePeriodElementsType")
        
        if not isinstance(self.time_table_id, ElementTagType | NoneType):
            raise TypeError("time_table_id is not of type ElementTagType")
        
        if not isinstance(self.lower_boundary_value, ScaledNumberElementsType | NoneType):
            raise TypeError("lower_boundary_value is not of type ScaledNumberElementsType")
        
        if not isinstance(self.upper_boundary_value, ScaledNumberElementsType | NoneType):
            raise TypeError("upper_boundary_value is not of type ScaledNumberElementsType")
        
    def get_data(self):

        msg_data = []
        
        if self.boundary_id is not None:
            msg_data.append({"boundaryId": self.boundary_id.get_data()})
        if self.time_period is not None:
            msg_data.append({"timePeriod": self.time_period.get_data()})
        if self.time_table_id is not None:
            msg_data.append({"timeTableId": self.time_table_id.get_data()})
        if self.lower_boundary_value is not None:
            msg_data.append({"lowerBoundaryValue": self.lower_boundary_value.get_data()})
        if self.upper_boundary_value is not None:
            msg_data.append({"upperBoundaryValue": self.upper_boundary_value.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.boundary_id is not None:
            result_str += f"{sep}boundaryId: {self.boundary_id}"
            sep = ", "
        if self.time_period is not None:
            result_str += f"{sep}timePeriod: {self.time_period}"
            sep = ", "
        if self.time_table_id is not None:
            result_str += f"{sep}timeTableId: {self.time_table_id}"
            sep = ", "
        if self.lower_boundary_value is not None:
            result_str += f"{sep}lowerBoundaryValue: {self.lower_boundary_value}"
            sep = ", "
        if self.upper_boundary_value is not None:
            result_str += f"{sep}upperBoundaryValue: {self.upper_boundary_value}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                boundary_id=data_dict.get('boundaryId'),
                time_period=data_dict.get('timePeriod'),
                time_table_id=data_dict.get('timeTableId'),
                lower_boundary_value=data_dict.get('lowerBoundaryValue'),
                upper_boundary_value=data_dict.get('upperBoundaryValue'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class TariffTierRelationDataElementsType: # EEBus_SPINE_TS_TariffInformation.xsd: ComplexType
    def __init__(
            self,
            tariff_id: ElementTagType = None,
            tier_id: ElementTagType = None,
    ):
        super().__init__()
        
        self.tariff_id = tariff_id
        self.tier_id = tier_id

        if not isinstance(self.tariff_id, ElementTagType | NoneType):
            raise TypeError("tariff_id is not of type ElementTagType")
        
        if not isinstance(self.tier_id, ElementTagType | NoneType):
            raise TypeError("tier_id is not of type ElementTagType")
        
    def get_data(self):

        msg_data = []
        
        if self.tariff_id is not None:
            msg_data.append({"tariffId": self.tariff_id.get_data()})
        if self.tier_id is not None:
            msg_data.append({"tierId": self.tier_id.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.tariff_id is not None:
            result_str += f"{sep}tariffId: {self.tariff_id}"
            sep = ", "
        if self.tier_id is not None:
            result_str += f"{sep}tierId: {self.tier_id}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                tariff_id=data_dict.get('tariffId'),
                tier_id=data_dict.get('tierId'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class TariffOverallConstraintsDataElementsType: # EEBus_SPINE_TS_TariffInformation.xsd: ComplexType
    def __init__(
            self,
            max_tariff_count: ElementTagType = None,
            max_boundary_count: ElementTagType = None,
            max_tier_count: ElementTagType = None,
            max_incentive_count: ElementTagType = None,
            max_boundaries_per_tariff: ElementTagType = None,
            max_tiers_per_tariff: ElementTagType = None,
            max_boundaries_per_tier: ElementTagType = None,
            max_incentives_per_tier: ElementTagType = None,
    ):
        super().__init__()
        
        self.max_tariff_count = max_tariff_count
        self.max_boundary_count = max_boundary_count
        self.max_tier_count = max_tier_count
        self.max_incentive_count = max_incentive_count
        self.max_boundaries_per_tariff = max_boundaries_per_tariff
        self.max_tiers_per_tariff = max_tiers_per_tariff
        self.max_boundaries_per_tier = max_boundaries_per_tier
        self.max_incentives_per_tier = max_incentives_per_tier

        if not isinstance(self.max_tariff_count, ElementTagType | NoneType):
            raise TypeError("max_tariff_count is not of type ElementTagType")
        
        if not isinstance(self.max_boundary_count, ElementTagType | NoneType):
            raise TypeError("max_boundary_count is not of type ElementTagType")
        
        if not isinstance(self.max_tier_count, ElementTagType | NoneType):
            raise TypeError("max_tier_count is not of type ElementTagType")
        
        if not isinstance(self.max_incentive_count, ElementTagType | NoneType):
            raise TypeError("max_incentive_count is not of type ElementTagType")
        
        if not isinstance(self.max_boundaries_per_tariff, ElementTagType | NoneType):
            raise TypeError("max_boundaries_per_tariff is not of type ElementTagType")
        
        if not isinstance(self.max_tiers_per_tariff, ElementTagType | NoneType):
            raise TypeError("max_tiers_per_tariff is not of type ElementTagType")
        
        if not isinstance(self.max_boundaries_per_tier, ElementTagType | NoneType):
            raise TypeError("max_boundaries_per_tier is not of type ElementTagType")
        
        if not isinstance(self.max_incentives_per_tier, ElementTagType | NoneType):
            raise TypeError("max_incentives_per_tier is not of type ElementTagType")
        
    def get_data(self):

        msg_data = []
        
        if self.max_tariff_count is not None:
            msg_data.append({"maxTariffCount": self.max_tariff_count.get_data()})
        if self.max_boundary_count is not None:
            msg_data.append({"maxBoundaryCount": self.max_boundary_count.get_data()})
        if self.max_tier_count is not None:
            msg_data.append({"maxTierCount": self.max_tier_count.get_data()})
        if self.max_incentive_count is not None:
            msg_data.append({"maxIncentiveCount": self.max_incentive_count.get_data()})
        if self.max_boundaries_per_tariff is not None:
            msg_data.append({"maxBoundariesPerTariff": self.max_boundaries_per_tariff.get_data()})
        if self.max_tiers_per_tariff is not None:
            msg_data.append({"maxTiersPerTariff": self.max_tiers_per_tariff.get_data()})
        if self.max_boundaries_per_tier is not None:
            msg_data.append({"maxBoundariesPerTier": self.max_boundaries_per_tier.get_data()})
        if self.max_incentives_per_tier is not None:
            msg_data.append({"maxIncentivesPerTier": self.max_incentives_per_tier.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.max_tariff_count is not None:
            result_str += f"{sep}maxTariffCount: {self.max_tariff_count}"
            sep = ", "
        if self.max_boundary_count is not None:
            result_str += f"{sep}maxBoundaryCount: {self.max_boundary_count}"
            sep = ", "
        if self.max_tier_count is not None:
            result_str += f"{sep}maxTierCount: {self.max_tier_count}"
            sep = ", "
        if self.max_incentive_count is not None:
            result_str += f"{sep}maxIncentiveCount: {self.max_incentive_count}"
            sep = ", "
        if self.max_boundaries_per_tariff is not None:
            result_str += f"{sep}maxBoundariesPerTariff: {self.max_boundaries_per_tariff}"
            sep = ", "
        if self.max_tiers_per_tariff is not None:
            result_str += f"{sep}maxTiersPerTariff: {self.max_tiers_per_tariff}"
            sep = ", "
        if self.max_boundaries_per_tier is not None:
            result_str += f"{sep}maxBoundariesPerTier: {self.max_boundaries_per_tier}"
            sep = ", "
        if self.max_incentives_per_tier is not None:
            result_str += f"{sep}maxIncentivesPerTier: {self.max_incentives_per_tier}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                max_tariff_count=data_dict.get('maxTariffCount'),
                max_boundary_count=data_dict.get('maxBoundaryCount'),
                max_tier_count=data_dict.get('maxTierCount'),
                max_incentive_count=data_dict.get('maxIncentiveCount'),
                max_boundaries_per_tariff=data_dict.get('maxBoundariesPerTariff'),
                max_tiers_per_tariff=data_dict.get('maxTiersPerTariff'),
                max_boundaries_per_tier=data_dict.get('maxBoundariesPerTier'),
                max_incentives_per_tier=data_dict.get('maxIncentivesPerTier'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class TariffDescriptionDataElementsType: # EEBus_SPINE_TS_TariffInformation.xsd: ComplexType
    def __init__(
            self,
            tariff_id: ElementTagType = None,
            commodity_id: ElementTagType = None,
            measurement_id: ElementTagType = None,
            tariff_writeable: ElementTagType = None,
            update_required: ElementTagType = None,
            scope_type: ElementTagType = None,
            label: ElementTagType = None,
            description: ElementTagType = None,
            slot_id_support: ElementTagType = None,
    ):
        super().__init__()
        
        self.tariff_id = tariff_id
        self.commodity_id = commodity_id
        self.measurement_id = measurement_id
        self.tariff_writeable = tariff_writeable
        self.update_required = update_required
        self.scope_type = scope_type
        self.label = label
        self.description = description
        self.slot_id_support = slot_id_support

        if not isinstance(self.tariff_id, ElementTagType | NoneType):
            raise TypeError("tariff_id is not of type ElementTagType")
        
        if not isinstance(self.commodity_id, ElementTagType | NoneType):
            raise TypeError("commodity_id is not of type ElementTagType")
        
        if not isinstance(self.measurement_id, ElementTagType | NoneType):
            raise TypeError("measurement_id is not of type ElementTagType")
        
        if not isinstance(self.tariff_writeable, ElementTagType | NoneType):
            raise TypeError("tariff_writeable is not of type ElementTagType")
        
        if not isinstance(self.update_required, ElementTagType | NoneType):
            raise TypeError("update_required is not of type ElementTagType")
        
        if not isinstance(self.scope_type, ElementTagType | NoneType):
            raise TypeError("scope_type is not of type ElementTagType")
        
        if not isinstance(self.label, ElementTagType | NoneType):
            raise TypeError("label is not of type ElementTagType")
        
        if not isinstance(self.description, ElementTagType | NoneType):
            raise TypeError("description is not of type ElementTagType")
        
        if not isinstance(self.slot_id_support, ElementTagType | NoneType):
            raise TypeError("slot_id_support is not of type ElementTagType")
        
    def get_data(self):

        msg_data = []
        
        if self.tariff_id is not None:
            msg_data.append({"tariffId": self.tariff_id.get_data()})
        if self.commodity_id is not None:
            msg_data.append({"commodityId": self.commodity_id.get_data()})
        if self.measurement_id is not None:
            msg_data.append({"measurementId": self.measurement_id.get_data()})
        if self.tariff_writeable is not None:
            msg_data.append({"tariffWriteable": self.tariff_writeable.get_data()})
        if self.update_required is not None:
            msg_data.append({"updateRequired": self.update_required.get_data()})
        if self.scope_type is not None:
            msg_data.append({"scopeType": self.scope_type.get_data()})
        if self.label is not None:
            msg_data.append({"label": self.label.get_data()})
        if self.description is not None:
            msg_data.append({"description": self.description.get_data()})
        if self.slot_id_support is not None:
            msg_data.append({"slotIdSupport": self.slot_id_support.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.tariff_id is not None:
            result_str += f"{sep}tariffId: {self.tariff_id}"
            sep = ", "
        if self.commodity_id is not None:
            result_str += f"{sep}commodityId: {self.commodity_id}"
            sep = ", "
        if self.measurement_id is not None:
            result_str += f"{sep}measurementId: {self.measurement_id}"
            sep = ", "
        if self.tariff_writeable is not None:
            result_str += f"{sep}tariffWriteable: {self.tariff_writeable}"
            sep = ", "
        if self.update_required is not None:
            result_str += f"{sep}updateRequired: {self.update_required}"
            sep = ", "
        if self.scope_type is not None:
            result_str += f"{sep}scopeType: {self.scope_type}"
            sep = ", "
        if self.label is not None:
            result_str += f"{sep}label: {self.label}"
            sep = ", "
        if self.description is not None:
            result_str += f"{sep}description: {self.description}"
            sep = ", "
        if self.slot_id_support is not None:
            result_str += f"{sep}slotIdSupport: {self.slot_id_support}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                tariff_id=data_dict.get('tariffId'),
                commodity_id=data_dict.get('commodityId'),
                measurement_id=data_dict.get('measurementId'),
                tariff_writeable=data_dict.get('tariffWriteable'),
                update_required=data_dict.get('updateRequired'),
                scope_type=data_dict.get('scopeType'),
                label=data_dict.get('label'),
                description=data_dict.get('description'),
                slot_id_support=data_dict.get('slotIdSupport'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class TariffDataElementsType: # EEBus_SPINE_TS_TariffInformation.xsd: ComplexType
    def __init__(
            self,
            tariff_id: ElementTagType = None,
            active_tier_id: ElementTagType = None,
    ):
        super().__init__()
        
        self.tariff_id = tariff_id
        self.active_tier_id = active_tier_id

        if not isinstance(self.tariff_id, ElementTagType | NoneType):
            raise TypeError("tariff_id is not of type ElementTagType")
        
        if not isinstance(self.active_tier_id, ElementTagType | NoneType):
            raise TypeError("active_tier_id is not of type ElementTagType")
        
    def get_data(self):

        msg_data = []
        
        if self.tariff_id is not None:
            msg_data.append({"tariffId": self.tariff_id.get_data()})
        if self.active_tier_id is not None:
            msg_data.append({"activeTierId": self.active_tier_id.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.tariff_id is not None:
            result_str += f"{sep}tariffId: {self.tariff_id}"
            sep = ", "
        if self.active_tier_id is not None:
            result_str += f"{sep}activeTierId: {self.active_tier_id}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                tariff_id=data_dict.get('tariffId'),
                active_tier_id=data_dict.get('activeTierId'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class TariffBoundaryRelationDataElementsType: # EEBus_SPINE_TS_TariffInformation.xsd: ComplexType
    def __init__(
            self,
            tariff_id: ElementTagType = None,
            boundary_id: ElementTagType = None,
    ):
        super().__init__()
        
        self.tariff_id = tariff_id
        self.boundary_id = boundary_id

        if not isinstance(self.tariff_id, ElementTagType | NoneType):
            raise TypeError("tariff_id is not of type ElementTagType")
        
        if not isinstance(self.boundary_id, ElementTagType | NoneType):
            raise TypeError("boundary_id is not of type ElementTagType")
        
    def get_data(self):

        msg_data = []
        
        if self.tariff_id is not None:
            msg_data.append({"tariffId": self.tariff_id.get_data()})
        if self.boundary_id is not None:
            msg_data.append({"boundaryId": self.boundary_id.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.tariff_id is not None:
            result_str += f"{sep}tariffId: {self.tariff_id}"
            sep = ", "
        if self.boundary_id is not None:
            result_str += f"{sep}boundaryId: {self.boundary_id}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                tariff_id=data_dict.get('tariffId'),
                boundary_id=data_dict.get('boundaryId'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class IncentiveDescriptionDataElementsType: # EEBus_SPINE_TS_TariffInformation.xsd: ComplexType
    def __init__(
            self,
            incentive_id: ElementTagType = None,
            incentive_type: ElementTagType = None,
            incentive_priority: ElementTagType = None,
            currency: ElementTagType = None,
            unit: ElementTagType = None,
            label: ElementTagType = None,
            description: ElementTagType = None,
    ):
        super().__init__()
        
        self.incentive_id = incentive_id
        self.incentive_type = incentive_type
        self.incentive_priority = incentive_priority
        self.currency = currency
        self.unit = unit
        self.label = label
        self.description = description

        if not isinstance(self.incentive_id, ElementTagType | NoneType):
            raise TypeError("incentive_id is not of type ElementTagType")
        
        if not isinstance(self.incentive_type, ElementTagType | NoneType):
            raise TypeError("incentive_type is not of type ElementTagType")
        
        if not isinstance(self.incentive_priority, ElementTagType | NoneType):
            raise TypeError("incentive_priority is not of type ElementTagType")
        
        if not isinstance(self.currency, ElementTagType | NoneType):
            raise TypeError("currency is not of type ElementTagType")
        
        if not isinstance(self.unit, ElementTagType | NoneType):
            raise TypeError("unit is not of type ElementTagType")
        
        if not isinstance(self.label, ElementTagType | NoneType):
            raise TypeError("label is not of type ElementTagType")
        
        if not isinstance(self.description, ElementTagType | NoneType):
            raise TypeError("description is not of type ElementTagType")
        
    def get_data(self):

        msg_data = []
        
        if self.incentive_id is not None:
            msg_data.append({"incentiveId": self.incentive_id.get_data()})
        if self.incentive_type is not None:
            msg_data.append({"incentiveType": self.incentive_type.get_data()})
        if self.incentive_priority is not None:
            msg_data.append({"incentivePriority": self.incentive_priority.get_data()})
        if self.currency is not None:
            msg_data.append({"currency": self.currency.get_data()})
        if self.unit is not None:
            msg_data.append({"unit": self.unit.get_data()})
        if self.label is not None:
            msg_data.append({"label": self.label.get_data()})
        if self.description is not None:
            msg_data.append({"description": self.description.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.incentive_id is not None:
            result_str += f"{sep}incentiveId: {self.incentive_id}"
            sep = ", "
        if self.incentive_type is not None:
            result_str += f"{sep}incentiveType: {self.incentive_type}"
            sep = ", "
        if self.incentive_priority is not None:
            result_str += f"{sep}incentivePriority: {self.incentive_priority}"
            sep = ", "
        if self.currency is not None:
            result_str += f"{sep}currency: {self.currency}"
            sep = ", "
        if self.unit is not None:
            result_str += f"{sep}unit: {self.unit}"
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
                incentive_id=data_dict.get('incentiveId'),
                incentive_type=data_dict.get('incentiveType'),
                incentive_priority=data_dict.get('incentivePriority'),
                currency=data_dict.get('currency'),
                unit=data_dict.get('unit'),
                label=data_dict.get('label'),
                description=data_dict.get('description'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class IncentiveDataElementsType: # EEBus_SPINE_TS_TariffInformation.xsd: ComplexType
    def __init__(
            self,
            incentive_id: ElementTagType = None,
            value_type: ElementTagType = None,
            timestamp: ElementTagType = None,
            time_period: TimePeriodElementsType = None,
            time_table_id: ElementTagType = None,
            value: ElementTagType = None,
    ):
        super().__init__()
        
        self.incentive_id = incentive_id
        self.value_type = value_type
        self.timestamp = timestamp
        self.time_period = time_period
        self.time_table_id = time_table_id
        self.value = value

        if not isinstance(self.incentive_id, ElementTagType | NoneType):
            raise TypeError("incentive_id is not of type ElementTagType")
        
        if not isinstance(self.value_type, ElementTagType | NoneType):
            raise TypeError("value_type is not of type ElementTagType")
        
        if not isinstance(self.timestamp, ElementTagType | NoneType):
            raise TypeError("timestamp is not of type ElementTagType")
        
        if not isinstance(self.time_period, TimePeriodElementsType | NoneType):
            raise TypeError("time_period is not of type TimePeriodElementsType")
        
        if not isinstance(self.time_table_id, ElementTagType | NoneType):
            raise TypeError("time_table_id is not of type ElementTagType")
        
        if not isinstance(self.value, ElementTagType | NoneType):
            raise TypeError("value is not of type ElementTagType")
        
    def get_data(self):

        msg_data = []
        
        if self.incentive_id is not None:
            msg_data.append({"incentiveId": self.incentive_id.get_data()})
        if self.value_type is not None:
            msg_data.append({"valueType": self.value_type.get_data()})
        if self.timestamp is not None:
            msg_data.append({"timestamp": self.timestamp.get_data()})
        if self.time_period is not None:
            msg_data.append({"timePeriod": self.time_period.get_data()})
        if self.time_table_id is not None:
            msg_data.append({"timeTableId": self.time_table_id.get_data()})
        if self.value is not None:
            msg_data.append({"value": self.value.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.incentive_id is not None:
            result_str += f"{sep}incentiveId: {self.incentive_id}"
            sep = ", "
        if self.value_type is not None:
            result_str += f"{sep}valueType: {self.value_type}"
            sep = ", "
        if self.timestamp is not None:
            result_str += f"{sep}timestamp: {self.timestamp}"
            sep = ", "
        if self.time_period is not None:
            result_str += f"{sep}timePeriod: {self.time_period}"
            sep = ", "
        if self.time_table_id is not None:
            result_str += f"{sep}timeTableId: {self.time_table_id}"
            sep = ", "
        if self.value is not None:
            result_str += f"{sep}value: {self.value}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                incentive_id=data_dict.get('incentiveId'),
                value_type=data_dict.get('valueType'),
                timestamp=data_dict.get('timestamp'),
                time_period=data_dict.get('timePeriod'),
                time_table_id=data_dict.get('timeTableId'),
                value=data_dict.get('value'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class CommodityDataElementsType: # EEBus_SPINE_TS_TariffInformation.xsd: ComplexType
    def __init__(
            self,
            commodity_id: ElementTagType = None,
            commodity_type: ElementTagType = None,
            positive_energy_direction: ElementTagType = None,
            label: ElementTagType = None,
            description: ElementTagType = None,
    ):
        super().__init__()
        
        self.commodity_id = commodity_id
        self.commodity_type = commodity_type
        self.positive_energy_direction = positive_energy_direction
        self.label = label
        self.description = description

        if not isinstance(self.commodity_id, ElementTagType | NoneType):
            raise TypeError("commodity_id is not of type ElementTagType")
        
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
        
        if self.commodity_id is not None:
            msg_data.append({"commodityId": self.commodity_id.get_data()})
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
        if self.commodity_id is not None:
            result_str += f"{sep}commodityId: {self.commodity_id}"
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
                commodity_id=data_dict.get('commodityId'),
                commodity_type=data_dict.get('commodityType'),
                positive_energy_direction=data_dict.get('positiveEnergyDirection'),
                label=data_dict.get('label'),
                description=data_dict.get('description'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class TierListDataSelectorsType: # EEBus_SPINE_TS_TariffInformation.xsd: ComplexType
    def __init__(
            self,
            tier_id: TierIdType = None,
            active_incentive_id: IncentiveIdType = None,
    ):
        super().__init__()
        
        self.tier_id = tier_id
        self.active_incentive_id = active_incentive_id

        if not isinstance(self.tier_id, TierIdType | NoneType):
            raise TypeError("tier_id is not of type TierIdType")
        
        if not isinstance(self.active_incentive_id, IncentiveIdType | NoneType):
            raise TypeError("active_incentive_id is not of type IncentiveIdType")
        
    def get_data(self):

        msg_data = []
        
        if self.tier_id is not None:
            msg_data.append({"tierId": self.tier_id.get_data()})
        if self.active_incentive_id is not None:
            msg_data.append({"activeIncentiveId": self.active_incentive_id.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.tier_id is not None:
            result_str += f"{sep}tierId: {self.tier_id}"
            sep = ", "
        if self.active_incentive_id is not None:
            result_str += f"{sep}activeIncentiveId: {self.active_incentive_id}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                tier_id=data_dict.get('tierId'),
                active_incentive_id=data_dict.get('activeIncentiveId'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class TierIncentiveRelationListDataSelectorsType: # EEBus_SPINE_TS_TariffInformation.xsd: ComplexType
    def __init__(
            self,
            tier_id: TierIdType = None,
            incentive_id: IncentiveIdType = None,
    ):
        super().__init__()
        
        self.tier_id = tier_id
        self.incentive_id = incentive_id

        if not isinstance(self.tier_id, TierIdType | NoneType):
            raise TypeError("tier_id is not of type TierIdType")
        
        if not isinstance(self.incentive_id, IncentiveIdType | NoneType):
            raise TypeError("incentive_id is not of type IncentiveIdType")
        
    def get_data(self):

        msg_data = []
        
        if self.tier_id is not None:
            msg_data.append({"tierId": self.tier_id.get_data()})
        if self.incentive_id is not None:
            msg_data.append({"incentiveId": self.incentive_id.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.tier_id is not None:
            result_str += f"{sep}tierId: {self.tier_id}"
            sep = ", "
        if self.incentive_id is not None:
            result_str += f"{sep}incentiveId: {self.incentive_id}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                tier_id=data_dict.get('tierId'),
                incentive_id=data_dict.get('incentiveId'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class TierDescriptionListDataSelectorsType: # EEBus_SPINE_TS_TariffInformation.xsd: ComplexType
    def __init__(
            self,
            tier_id: TierIdType = None,
            tier_type: TierTypeType = None,
    ):
        super().__init__()
        
        self.tier_id = tier_id
        self.tier_type = tier_type

        if not isinstance(self.tier_id, TierIdType | NoneType):
            raise TypeError("tier_id is not of type TierIdType")
        
        if not isinstance(self.tier_type, TierTypeType | NoneType):
            raise TypeError("tier_type is not of type TierTypeType")
        
    def get_data(self):

        msg_data = []
        
        if self.tier_id is not None:
            msg_data.append({"tierId": self.tier_id.get_data()})
        if self.tier_type is not None:
            msg_data.append({"tierType": self.tier_type.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.tier_id is not None:
            result_str += f"{sep}tierId: {self.tier_id}"
            sep = ", "
        if self.tier_type is not None:
            result_str += f"{sep}tierType: {self.tier_type}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                tier_id=data_dict.get('tierId'),
                tier_type=data_dict.get('tierType'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class TierBoundaryListDataSelectorsType: # EEBus_SPINE_TS_TariffInformation.xsd: ComplexType
    def __init__(
            self,
            boundary_id: TierBoundaryIdType = None,
    ):
        super().__init__()
        
        self.boundary_id = boundary_id

        if not isinstance(self.boundary_id, TierBoundaryIdType | NoneType):
            raise TypeError("boundary_id is not of type TierBoundaryIdType")
        
    def get_data(self):

        msg_data = []
        
        if self.boundary_id is not None:
            msg_data.append({"boundaryId": self.boundary_id.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.boundary_id is not None:
            result_str += f"{sep}boundaryId: {self.boundary_id}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                boundary_id=data_dict.get('boundaryId'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class TierBoundaryDescriptionListDataSelectorsType: # EEBus_SPINE_TS_TariffInformation.xsd: ComplexType
    def __init__(
            self,
            boundary_id: TierBoundaryIdType = None,
            boundary_type: TierBoundaryTypeType = None,
    ):
        super().__init__()
        
        self.boundary_id = boundary_id
        self.boundary_type = boundary_type

        if not isinstance(self.boundary_id, TierBoundaryIdType | NoneType):
            raise TypeError("boundary_id is not of type TierBoundaryIdType")
        
        if not isinstance(self.boundary_type, TierBoundaryTypeType | NoneType):
            raise TypeError("boundary_type is not of type TierBoundaryTypeType")
        
    def get_data(self):

        msg_data = []
        
        if self.boundary_id is not None:
            msg_data.append({"boundaryId": self.boundary_id.get_data()})
        if self.boundary_type is not None:
            msg_data.append({"boundaryType": self.boundary_type.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.boundary_id is not None:
            result_str += f"{sep}boundaryId: {self.boundary_id}"
            sep = ", "
        if self.boundary_type is not None:
            result_str += f"{sep}boundaryType: {self.boundary_type}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                boundary_id=data_dict.get('boundaryId'),
                boundary_type=data_dict.get('boundaryType'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class TariffTierRelationListDataSelectorsType: # EEBus_SPINE_TS_TariffInformation.xsd: ComplexType
    def __init__(
            self,
            tariff_id: TariffIdType = None,
            tier_id: TierIdType = None,
    ):
        super().__init__()
        
        self.tariff_id = tariff_id
        self.tier_id = tier_id

        if not isinstance(self.tariff_id, TariffIdType | NoneType):
            raise TypeError("tariff_id is not of type TariffIdType")
        
        if not isinstance(self.tier_id, TierIdType | NoneType):
            raise TypeError("tier_id is not of type TierIdType")
        
    def get_data(self):

        msg_data = []
        
        if self.tariff_id is not None:
            msg_data.append({"tariffId": self.tariff_id.get_data()})
        if self.tier_id is not None:
            msg_data.append({"tierId": self.tier_id.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.tariff_id is not None:
            result_str += f"{sep}tariffId: {self.tariff_id}"
            sep = ", "
        if self.tier_id is not None:
            result_str += f"{sep}tierId: {self.tier_id}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                tariff_id=data_dict.get('tariffId'),
                tier_id=data_dict.get('tierId'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class TariffListDataSelectorsType: # EEBus_SPINE_TS_TariffInformation.xsd: ComplexType
    def __init__(
            self,
            tariff_id: TariffIdType = None,
            active_tier_id: TierIdType = None,
    ):
        super().__init__()
        
        self.tariff_id = tariff_id
        self.active_tier_id = active_tier_id

        if not isinstance(self.tariff_id, TariffIdType | NoneType):
            raise TypeError("tariff_id is not of type TariffIdType")
        
        if not isinstance(self.active_tier_id, TierIdType | NoneType):
            raise TypeError("active_tier_id is not of type TierIdType")
        
    def get_data(self):

        msg_data = []
        
        if self.tariff_id is not None:
            msg_data.append({"tariffId": self.tariff_id.get_data()})
        if self.active_tier_id is not None:
            msg_data.append({"activeTierId": self.active_tier_id.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.tariff_id is not None:
            result_str += f"{sep}tariffId: {self.tariff_id}"
            sep = ", "
        if self.active_tier_id is not None:
            result_str += f"{sep}activeTierId: {self.active_tier_id}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                tariff_id=data_dict.get('tariffId'),
                active_tier_id=data_dict.get('activeTierId'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class TariffDescriptionListDataSelectorsType: # EEBus_SPINE_TS_TariffInformation.xsd: ComplexType
    def __init__(
            self,
            tariff_id: TariffIdType = None,
            commodity_id: CommodityIdType = None,
            measurement_id: MeasurementIdType = None,
            scope_type: ScopeTypeType = None,
    ):
        super().__init__()
        
        self.tariff_id = tariff_id
        self.commodity_id = commodity_id
        self.measurement_id = measurement_id
        self.scope_type = scope_type

        if not isinstance(self.tariff_id, TariffIdType | NoneType):
            raise TypeError("tariff_id is not of type TariffIdType")
        
        if not isinstance(self.commodity_id, CommodityIdType | NoneType):
            raise TypeError("commodity_id is not of type CommodityIdType")
        
        if not isinstance(self.measurement_id, MeasurementIdType | NoneType):
            raise TypeError("measurement_id is not of type MeasurementIdType")
        
        if not isinstance(self.scope_type, ScopeTypeType | NoneType):
            raise TypeError("scope_type is not of type ScopeTypeType")
        
    def get_data(self):

        msg_data = []
        
        if self.tariff_id is not None:
            msg_data.append({"tariffId": self.tariff_id.get_data()})
        if self.commodity_id is not None:
            msg_data.append({"commodityId": self.commodity_id.get_data()})
        if self.measurement_id is not None:
            msg_data.append({"measurementId": self.measurement_id.get_data()})
        if self.scope_type is not None:
            msg_data.append({"scopeType": self.scope_type.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.tariff_id is not None:
            result_str += f"{sep}tariffId: {self.tariff_id}"
            sep = ", "
        if self.commodity_id is not None:
            result_str += f"{sep}commodityId: {self.commodity_id}"
            sep = ", "
        if self.measurement_id is not None:
            result_str += f"{sep}measurementId: {self.measurement_id}"
            sep = ", "
        if self.scope_type is not None:
            result_str += f"{sep}scopeType: {self.scope_type}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                tariff_id=data_dict.get('tariffId'),
                commodity_id=data_dict.get('commodityId'),
                measurement_id=data_dict.get('measurementId'),
                scope_type=data_dict.get('scopeType'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class TariffBoundaryRelationListDataSelectorsType: # EEBus_SPINE_TS_TariffInformation.xsd: ComplexType
    def __init__(
            self,
            tariff_id: TariffIdType = None,
            boundary_id: TierBoundaryIdType = None,
    ):
        super().__init__()
        
        self.tariff_id = tariff_id
        self.boundary_id = boundary_id

        if not isinstance(self.tariff_id, TariffIdType | NoneType):
            raise TypeError("tariff_id is not of type TariffIdType")
        
        if not isinstance(self.boundary_id, TierBoundaryIdType | NoneType):
            raise TypeError("boundary_id is not of type TierBoundaryIdType")
        
    def get_data(self):

        msg_data = []
        
        if self.tariff_id is not None:
            msg_data.append({"tariffId": self.tariff_id.get_data()})
        if self.boundary_id is not None:
            msg_data.append({"boundaryId": self.boundary_id.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.tariff_id is not None:
            result_str += f"{sep}tariffId: {self.tariff_id}"
            sep = ", "
        if self.boundary_id is not None:
            result_str += f"{sep}boundaryId: {self.boundary_id}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                tariff_id=data_dict.get('tariffId'),
                boundary_id=data_dict.get('boundaryId'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class IncentiveListDataSelectorsType: # EEBus_SPINE_TS_TariffInformation.xsd: ComplexType
    def __init__(
            self,
            incentive_id: IncentiveIdType = None,
            value_type: IncentiveValueTypeType = None,
            timestamp_interval: TimestampIntervalType = None,
    ):
        super().__init__()
        
        self.incentive_id = incentive_id
        self.value_type = value_type
        self.timestamp_interval = timestamp_interval

        if not isinstance(self.incentive_id, IncentiveIdType | NoneType):
            raise TypeError("incentive_id is not of type IncentiveIdType")
        
        if not isinstance(self.value_type, IncentiveValueTypeType | NoneType):
            raise TypeError("value_type is not of type IncentiveValueTypeType")
        
        if not isinstance(self.timestamp_interval, TimestampIntervalType | NoneType):
            raise TypeError("timestamp_interval is not of type TimestampIntervalType")
        
    def get_data(self):

        msg_data = []
        
        if self.incentive_id is not None:
            msg_data.append({"incentiveId": self.incentive_id.get_data()})
        if self.value_type is not None:
            msg_data.append({"valueType": self.value_type.get_data()})
        if self.timestamp_interval is not None:
            msg_data.append({"timestampInterval": self.timestamp_interval.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.incentive_id is not None:
            result_str += f"{sep}incentiveId: {self.incentive_id}"
            sep = ", "
        if self.value_type is not None:
            result_str += f"{sep}valueType: {self.value_type}"
            sep = ", "
        if self.timestamp_interval is not None:
            result_str += f"{sep}timestampInterval: {self.timestamp_interval}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                incentive_id=data_dict.get('incentiveId'),
                value_type=data_dict.get('valueType'),
                timestamp_interval=data_dict.get('timestampInterval'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class IncentiveDescriptionListDataSelectorsType: # EEBus_SPINE_TS_TariffInformation.xsd: ComplexType
    def __init__(
            self,
            incentive_id: IncentiveIdType = None,
            incentive_type: IncentiveTypeType = None,
    ):
        super().__init__()
        
        self.incentive_id = incentive_id
        self.incentive_type = incentive_type

        if not isinstance(self.incentive_id, IncentiveIdType | NoneType):
            raise TypeError("incentive_id is not of type IncentiveIdType")
        
        if not isinstance(self.incentive_type, IncentiveTypeType | NoneType):
            raise TypeError("incentive_type is not of type IncentiveTypeType")
        
    def get_data(self):

        msg_data = []
        
        if self.incentive_id is not None:
            msg_data.append({"incentiveId": self.incentive_id.get_data()})
        if self.incentive_type is not None:
            msg_data.append({"incentiveType": self.incentive_type.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.incentive_id is not None:
            result_str += f"{sep}incentiveId: {self.incentive_id}"
            sep = ", "
        if self.incentive_type is not None:
            result_str += f"{sep}incentiveType: {self.incentive_type}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                incentive_id=data_dict.get('incentiveId'),
                incentive_type=data_dict.get('incentiveType'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class CommodityListDataSelectorsType: # EEBus_SPINE_TS_TariffInformation.xsd: ComplexType
    def __init__(
            self,
            commodity_id: CommodityIdType = None,
            commodity_type: CommodityTypeType = None,
    ):
        super().__init__()
        
        self.commodity_id = commodity_id
        self.commodity_type = commodity_type

        if not isinstance(self.commodity_id, CommodityIdType | NoneType):
            raise TypeError("commodity_id is not of type CommodityIdType")
        
        if not isinstance(self.commodity_type, CommodityTypeType | NoneType):
            raise TypeError("commodity_type is not of type CommodityTypeType")
        
    def get_data(self):

        msg_data = []
        
        if self.commodity_id is not None:
            msg_data.append({"commodityId": self.commodity_id.get_data()})
        if self.commodity_type is not None:
            msg_data.append({"commodityType": self.commodity_type.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.commodity_id is not None:
            result_str += f"{sep}commodityId: {self.commodity_id}"
            sep = ", "
        if self.commodity_type is not None:
            result_str += f"{sep}commodityType: {self.commodity_type}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                commodity_id=data_dict.get('commodityId'),
                commodity_type=data_dict.get('commodityType'),
            )
        elif data:
            return cls(data)
        else:
            return cls()



