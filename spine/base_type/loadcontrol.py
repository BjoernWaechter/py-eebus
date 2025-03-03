# Jinja Template message_type.py.jinja2
from spine.base_type.commondatatypes import ElementTagType
from spine.base_type.commondatatypes import ScaledNumberElementsType
from spine.base_type.commondatatypes import ScaledNumberType
from spine.base_type.commondatatypes import TimePeriodElementsType
from spine.base_type.commondatatypes import TimePeriodType
from spine.base_type.commondatatypes import TimestampIntervalType
from spine.simple_type.commondatatypes import DescriptionType
from spine.simple_type.commondatatypes import LabelType
from spine.simple_type.loadcontrol import LoadControlEventIdType
from spine.simple_type.loadcontrol import LoadControlLimitIdType
from spine.simple_type.measurement import MeasurementIdType
from spine.union_type.commondatatypes import AbsoluteOrRelativeTimeType
from spine.union_type.commondatatypes import EnergyDirectionType
from spine.union_type.commondatatypes import ScopeTypeType
from spine.union_type.commondatatypes import UnitOfMeasurementType
from spine.union_type.loadcontrol import LoadControlCategoryType
from spine.union_type.loadcontrol import LoadControlEventActionType
from spine.union_type.loadcontrol import LoadControlEventStateType
from spine.union_type.loadcontrol import LoadControlLimitTypeType
from types import NoneType
from spine import array_2_dict


class LoadControlStateDataType: # EEBus_SPINE_TS_LoadControl.xsd:ns_p:LoadControlStateDataType -> ComplexType
    def __init__(
            self,
            timestamp: AbsoluteOrRelativeTimeType = None,
            event_id: LoadControlEventIdType = None,
            event_state_consume: LoadControlEventStateType = None,
            applied_event_action_consume: LoadControlEventActionType = None,
            event_state_produce: LoadControlEventStateType = None,
            applied_event_action_produce: LoadControlEventActionType = None,
    ):
        super().__init__()
        
        self.timestamp = timestamp
        self.event_id = event_id
        self.event_state_consume = event_state_consume
        self.applied_event_action_consume = applied_event_action_consume
        self.event_state_produce = event_state_produce
        self.applied_event_action_produce = applied_event_action_produce

        if not isinstance(self.timestamp, AbsoluteOrRelativeTimeType | NoneType):
            raise TypeError("timestamp is not of type AbsoluteOrRelativeTimeType")
        
        if not isinstance(self.event_id, LoadControlEventIdType | NoneType):
            raise TypeError("event_id is not of type LoadControlEventIdType")
        
        if not isinstance(self.event_state_consume, LoadControlEventStateType | NoneType):
            raise TypeError("event_state_consume is not of type LoadControlEventStateType")
        
        if not isinstance(self.applied_event_action_consume, LoadControlEventActionType | NoneType):
            raise TypeError("applied_event_action_consume is not of type LoadControlEventActionType")
        
        if not isinstance(self.event_state_produce, LoadControlEventStateType | NoneType):
            raise TypeError("event_state_produce is not of type LoadControlEventStateType")
        
        if not isinstance(self.applied_event_action_produce, LoadControlEventActionType | NoneType):
            raise TypeError("applied_event_action_produce is not of type LoadControlEventActionType")
        
    def get_data(self):

        msg_data = []
        
        if self.timestamp is not None:
            msg_data.append({"timestamp": self.timestamp.get_data()})
        if self.event_id is not None:
            msg_data.append({"eventId": self.event_id.get_data()})
        if self.event_state_consume is not None:
            msg_data.append({"eventStateConsume": self.event_state_consume.get_data()})
        if self.applied_event_action_consume is not None:
            msg_data.append({"appliedEventActionConsume": self.applied_event_action_consume.get_data()})
        if self.event_state_produce is not None:
            msg_data.append({"eventStateProduce": self.event_state_produce.get_data()})
        if self.applied_event_action_produce is not None:
            msg_data.append({"appliedEventActionProduce": self.applied_event_action_produce.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.timestamp is not None:
            result_str += f"{sep}timestamp: {self.timestamp}"
            sep = ", "
        if self.event_id is not None:
            result_str += f"{sep}eventId: {self.event_id}"
            sep = ", "
        if self.event_state_consume is not None:
            result_str += f"{sep}eventStateConsume: {self.event_state_consume}"
            sep = ", "
        if self.applied_event_action_consume is not None:
            result_str += f"{sep}appliedEventActionConsume: {self.applied_event_action_consume}"
            sep = ", "
        if self.event_state_produce is not None:
            result_str += f"{sep}eventStateProduce: {self.event_state_produce}"
            sep = ", "
        if self.applied_event_action_produce is not None:
            result_str += f"{sep}appliedEventActionProduce: {self.applied_event_action_produce}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                timestamp=data_dict.get('timestamp'),
                event_id=data_dict.get('eventId'),
                event_state_consume=data_dict.get('eventStateConsume'),
                applied_event_action_consume=data_dict.get('appliedEventActionConsume'),
                event_state_produce=data_dict.get('eventStateProduce'),
                applied_event_action_produce=data_dict.get('appliedEventActionProduce'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class LoadControlLimitDataType: # EEBus_SPINE_TS_LoadControl.xsd:ns_p:LoadControlLimitDataType -> ComplexType
    def __init__(
            self,
            limit_id: LoadControlLimitIdType = None,
            is_limit_changeable: bool = None,
            is_limit_active: bool = None,
            time_period: TimePeriodType = None,
            value: ScaledNumberType = None,
    ):
        super().__init__()
        
        self.limit_id = limit_id
        self.is_limit_changeable = is_limit_changeable
        self.is_limit_active = is_limit_active
        self.time_period = time_period
        self.value = value

        if not isinstance(self.limit_id, LoadControlLimitIdType | NoneType):
            raise TypeError("limit_id is not of type LoadControlLimitIdType")
        
        if not isinstance(self.is_limit_changeable, bool | NoneType):
            raise TypeError("is_limit_changeable is not of type bool")
        
        if not isinstance(self.is_limit_active, bool | NoneType):
            raise TypeError("is_limit_active is not of type bool")
        
        if not isinstance(self.time_period, TimePeriodType | NoneType):
            raise TypeError("time_period is not of type TimePeriodType")
        
        if not isinstance(self.value, ScaledNumberType | NoneType):
            raise TypeError("value is not of type ScaledNumberType")
        
    def get_data(self):

        msg_data = []
        
        if self.limit_id is not None:
            msg_data.append({"limitId": self.limit_id.get_data()})
        if self.is_limit_changeable is not None:
            msg_data.append({"isLimitChangeable": self.is_limit_changeable})
        if self.is_limit_active is not None:
            msg_data.append({"isLimitActive": self.is_limit_active})
        if self.time_period is not None:
            msg_data.append({"timePeriod": self.time_period.get_data()})
        if self.value is not None:
            msg_data.append({"value": self.value.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.limit_id is not None:
            result_str += f"{sep}limitId: {self.limit_id}"
            sep = ", "
        if self.is_limit_changeable is not None:
            result_str += f"{sep}isLimitChangeable: {self.is_limit_changeable}"
            sep = ", "
        if self.is_limit_active is not None:
            result_str += f"{sep}isLimitActive: {self.is_limit_active}"
            sep = ", "
        if self.time_period is not None:
            result_str += f"{sep}timePeriod: {self.time_period}"
            sep = ", "
        if self.value is not None:
            result_str += f"{sep}value: {self.value}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                limit_id=data_dict.get('limitId'),
                is_limit_changeable=data_dict.get('isLimitChangeable'),
                is_limit_active=data_dict.get('isLimitActive'),
                time_period=data_dict.get('timePeriod'),
                value=data_dict.get('value'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class LoadControlLimitDescriptionDataType: # EEBus_SPINE_TS_LoadControl.xsd:ns_p:LoadControlLimitDescriptionDataType -> ComplexType
    def __init__(
            self,
            limit_id: LoadControlLimitIdType = None,
            limit_type: LoadControlLimitTypeType = None,
            limit_category: LoadControlCategoryType = None,
            limit_direction: EnergyDirectionType = None,
            measurement_id: MeasurementIdType = None,
            unit: UnitOfMeasurementType = None,
            scope_type: ScopeTypeType = None,
            label: LabelType = None,
            description: DescriptionType = None,
    ):
        super().__init__()
        
        self.limit_id = limit_id
        self.limit_type = limit_type
        self.limit_category = limit_category
        self.limit_direction = limit_direction
        self.measurement_id = measurement_id
        self.unit = unit
        self.scope_type = scope_type
        self.label = label
        self.description = description

        if not isinstance(self.limit_id, LoadControlLimitIdType | NoneType):
            raise TypeError("limit_id is not of type LoadControlLimitIdType")
        
        if not isinstance(self.limit_type, LoadControlLimitTypeType | NoneType):
            raise TypeError("limit_type is not of type LoadControlLimitTypeType")
        
        if not isinstance(self.limit_category, LoadControlCategoryType | NoneType):
            raise TypeError("limit_category is not of type LoadControlCategoryType")
        
        if not isinstance(self.limit_direction, EnergyDirectionType | NoneType):
            raise TypeError("limit_direction is not of type EnergyDirectionType")
        
        if not isinstance(self.measurement_id, MeasurementIdType | NoneType):
            raise TypeError("measurement_id is not of type MeasurementIdType")
        
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
        
        if self.limit_id is not None:
            msg_data.append({"limitId": self.limit_id.get_data()})
        if self.limit_type is not None:
            msg_data.append({"limitType": self.limit_type.get_data()})
        if self.limit_category is not None:
            msg_data.append({"limitCategory": self.limit_category.get_data()})
        if self.limit_direction is not None:
            msg_data.append({"limitDirection": self.limit_direction.get_data()})
        if self.measurement_id is not None:
            msg_data.append({"measurementId": self.measurement_id.get_data()})
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
        if self.limit_id is not None:
            result_str += f"{sep}limitId: {self.limit_id}"
            sep = ", "
        if self.limit_type is not None:
            result_str += f"{sep}limitType: {self.limit_type}"
            sep = ", "
        if self.limit_category is not None:
            result_str += f"{sep}limitCategory: {self.limit_category}"
            sep = ", "
        if self.limit_direction is not None:
            result_str += f"{sep}limitDirection: {self.limit_direction}"
            sep = ", "
        if self.measurement_id is not None:
            result_str += f"{sep}measurementId: {self.measurement_id}"
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
                limit_id=data_dict.get('limitId'),
                limit_type=data_dict.get('limitType'),
                limit_category=data_dict.get('limitCategory'),
                limit_direction=data_dict.get('limitDirection'),
                measurement_id=data_dict.get('measurementId'),
                unit=data_dict.get('unit'),
                scope_type=data_dict.get('scopeType'),
                label=data_dict.get('label'),
                description=data_dict.get('description'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class LoadControlLimitConstraintsDataType: # EEBus_SPINE_TS_LoadControl.xsd:ns_p:LoadControlLimitConstraintsDataType -> ComplexType
    def __init__(
            self,
            limit_id: LoadControlLimitIdType = None,
            value_range_min: ScaledNumberType = None,
            value_range_max: ScaledNumberType = None,
            value_step_size: ScaledNumberType = None,
    ):
        super().__init__()
        
        self.limit_id = limit_id
        self.value_range_min = value_range_min
        self.value_range_max = value_range_max
        self.value_step_size = value_step_size

        if not isinstance(self.limit_id, LoadControlLimitIdType | NoneType):
            raise TypeError("limit_id is not of type LoadControlLimitIdType")
        
        if not isinstance(self.value_range_min, ScaledNumberType | NoneType):
            raise TypeError("value_range_min is not of type ScaledNumberType")
        
        if not isinstance(self.value_range_max, ScaledNumberType | NoneType):
            raise TypeError("value_range_max is not of type ScaledNumberType")
        
        if not isinstance(self.value_step_size, ScaledNumberType | NoneType):
            raise TypeError("value_step_size is not of type ScaledNumberType")
        
    def get_data(self):

        msg_data = []
        
        if self.limit_id is not None:
            msg_data.append({"limitId": self.limit_id.get_data()})
        if self.value_range_min is not None:
            msg_data.append({"valueRangeMin": self.value_range_min.get_data()})
        if self.value_range_max is not None:
            msg_data.append({"valueRangeMax": self.value_range_max.get_data()})
        if self.value_step_size is not None:
            msg_data.append({"valueStepSize": self.value_step_size.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.limit_id is not None:
            result_str += f"{sep}limitId: {self.limit_id}"
            sep = ", "
        if self.value_range_min is not None:
            result_str += f"{sep}valueRangeMin: {self.value_range_min}"
            sep = ", "
        if self.value_range_max is not None:
            result_str += f"{sep}valueRangeMax: {self.value_range_max}"
            sep = ", "
        if self.value_step_size is not None:
            result_str += f"{sep}valueStepSize: {self.value_step_size}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                limit_id=data_dict.get('limitId'),
                value_range_min=data_dict.get('valueRangeMin'),
                value_range_max=data_dict.get('valueRangeMax'),
                value_step_size=data_dict.get('valueStepSize'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class LoadControlEventDataType: # EEBus_SPINE_TS_LoadControl.xsd:ns_p:LoadControlEventDataType -> ComplexType
    def __init__(
            self,
            timestamp: AbsoluteOrRelativeTimeType = None,
            event_id: LoadControlEventIdType = None,
            event_action_consume: LoadControlEventActionType = None,
            event_action_produce: LoadControlEventActionType = None,
            time_period: TimePeriodType = None,
    ):
        super().__init__()
        
        self.timestamp = timestamp
        self.event_id = event_id
        self.event_action_consume = event_action_consume
        self.event_action_produce = event_action_produce
        self.time_period = time_period

        if not isinstance(self.timestamp, AbsoluteOrRelativeTimeType | NoneType):
            raise TypeError("timestamp is not of type AbsoluteOrRelativeTimeType")
        
        if not isinstance(self.event_id, LoadControlEventIdType | NoneType):
            raise TypeError("event_id is not of type LoadControlEventIdType")
        
        if not isinstance(self.event_action_consume, LoadControlEventActionType | NoneType):
            raise TypeError("event_action_consume is not of type LoadControlEventActionType")
        
        if not isinstance(self.event_action_produce, LoadControlEventActionType | NoneType):
            raise TypeError("event_action_produce is not of type LoadControlEventActionType")
        
        if not isinstance(self.time_period, TimePeriodType | NoneType):
            raise TypeError("time_period is not of type TimePeriodType")
        
    def get_data(self):

        msg_data = []
        
        if self.timestamp is not None:
            msg_data.append({"timestamp": self.timestamp.get_data()})
        if self.event_id is not None:
            msg_data.append({"eventId": self.event_id.get_data()})
        if self.event_action_consume is not None:
            msg_data.append({"eventActionConsume": self.event_action_consume.get_data()})
        if self.event_action_produce is not None:
            msg_data.append({"eventActionProduce": self.event_action_produce.get_data()})
        if self.time_period is not None:
            msg_data.append({"timePeriod": self.time_period.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.timestamp is not None:
            result_str += f"{sep}timestamp: {self.timestamp}"
            sep = ", "
        if self.event_id is not None:
            result_str += f"{sep}eventId: {self.event_id}"
            sep = ", "
        if self.event_action_consume is not None:
            result_str += f"{sep}eventActionConsume: {self.event_action_consume}"
            sep = ", "
        if self.event_action_produce is not None:
            result_str += f"{sep}eventActionProduce: {self.event_action_produce}"
            sep = ", "
        if self.time_period is not None:
            result_str += f"{sep}timePeriod: {self.time_period}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                timestamp=data_dict.get('timestamp'),
                event_id=data_dict.get('eventId'),
                event_action_consume=data_dict.get('eventActionConsume'),
                event_action_produce=data_dict.get('eventActionProduce'),
                time_period=data_dict.get('timePeriod'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class LoadControlStateListDataType: # EEBus_SPINE_TS_LoadControl.xsd:ns_p:LoadControlStateListDataType -> ComplexType
    def __init__(
            self,
            load_control_state_data: list[LoadControlStateDataType] = None,
    ):
        super().__init__()
        
        self.load_control_state_data = load_control_state_data

        if not isinstance(self.load_control_state_data, list | NoneType):
            raise TypeError("load_control_state_data is not of type list[LoadControlStateDataType]")
        
    def get_data(self):

        msg_data = []
        
        if self.load_control_state_data is not None:
            msg_data.append({"loadControlStateData": [d.get_data() for d in self.load_control_state_data]})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.load_control_state_data is not None:
            result_str += f"{sep}loadControlStateData: {self.load_control_state_data}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                load_control_state_data=data_dict.get('loadControlStateData'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class LoadControlNodeDataType: # EEBus_SPINE_TS_LoadControl.xsd:ns_p:LoadControlNodeDataType -> ComplexType
    def __init__(
            self,
            is_node_remote_controllable: bool = None,
    ):
        super().__init__()
        
        self.is_node_remote_controllable = is_node_remote_controllable

        if not isinstance(self.is_node_remote_controllable, bool | NoneType):
            raise TypeError("is_node_remote_controllable is not of type bool")
        
    def get_data(self):

        msg_data = []
        
        if self.is_node_remote_controllable is not None:
            msg_data.append({"isNodeRemoteControllable": self.is_node_remote_controllable})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.is_node_remote_controllable is not None:
            result_str += f"{sep}isNodeRemoteControllable: {self.is_node_remote_controllable}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                is_node_remote_controllable=data_dict.get('isNodeRemoteControllable'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class LoadControlLimitListDataType: # EEBus_SPINE_TS_LoadControl.xsd:ns_p:LoadControlLimitListDataType -> ComplexType
    def __init__(
            self,
            load_control_limit_data: list[LoadControlLimitDataType] = None,
    ):
        super().__init__()
        
        self.load_control_limit_data = load_control_limit_data

        if not isinstance(self.load_control_limit_data, list | NoneType):
            raise TypeError("load_control_limit_data is not of type list[LoadControlLimitDataType]")
        
    def get_data(self):

        msg_data = []
        
        if self.load_control_limit_data is not None:
            msg_data.append({"loadControlLimitData": [d.get_data() for d in self.load_control_limit_data]})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.load_control_limit_data is not None:
            result_str += f"{sep}loadControlLimitData: {self.load_control_limit_data}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                load_control_limit_data=data_dict.get('loadControlLimitData'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class LoadControlLimitDescriptionListDataType: # EEBus_SPINE_TS_LoadControl.xsd:ns_p:LoadControlLimitDescriptionListDataType -> ComplexType
    def __init__(
            self,
            load_control_limit_description_data: list[LoadControlLimitDescriptionDataType] = None,
    ):
        super().__init__()
        
        self.load_control_limit_description_data = load_control_limit_description_data

        if not isinstance(self.load_control_limit_description_data, list | NoneType):
            raise TypeError("load_control_limit_description_data is not of type list[LoadControlLimitDescriptionDataType]")
        
    def get_data(self):

        msg_data = []
        
        if self.load_control_limit_description_data is not None:
            msg_data.append({"loadControlLimitDescriptionData": [d.get_data() for d in self.load_control_limit_description_data]})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.load_control_limit_description_data is not None:
            result_str += f"{sep}loadControlLimitDescriptionData: {self.load_control_limit_description_data}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                load_control_limit_description_data=data_dict.get('loadControlLimitDescriptionData'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class LoadControlLimitConstraintsListDataType: # EEBus_SPINE_TS_LoadControl.xsd:ns_p:LoadControlLimitConstraintsListDataType -> ComplexType
    def __init__(
            self,
            load_control_limit_constraints_data: list[LoadControlLimitConstraintsDataType] = None,
    ):
        super().__init__()
        
        self.load_control_limit_constraints_data = load_control_limit_constraints_data

        if not isinstance(self.load_control_limit_constraints_data, list | NoneType):
            raise TypeError("load_control_limit_constraints_data is not of type list[LoadControlLimitConstraintsDataType]")
        
    def get_data(self):

        msg_data = []
        
        if self.load_control_limit_constraints_data is not None:
            msg_data.append({"loadControlLimitConstraintsData": [d.get_data() for d in self.load_control_limit_constraints_data]})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.load_control_limit_constraints_data is not None:
            result_str += f"{sep}loadControlLimitConstraintsData: {self.load_control_limit_constraints_data}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                load_control_limit_constraints_data=data_dict.get('loadControlLimitConstraintsData'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class LoadControlEventListDataType: # EEBus_SPINE_TS_LoadControl.xsd:ns_p:LoadControlEventListDataType -> ComplexType
    def __init__(
            self,
            load_control_event_data: list[LoadControlEventDataType] = None,
    ):
        super().__init__()
        
        self.load_control_event_data = load_control_event_data

        if not isinstance(self.load_control_event_data, list | NoneType):
            raise TypeError("load_control_event_data is not of type list[LoadControlEventDataType]")
        
    def get_data(self):

        msg_data = []
        
        if self.load_control_event_data is not None:
            msg_data.append({"loadControlEventData": [d.get_data() for d in self.load_control_event_data]})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.load_control_event_data is not None:
            result_str += f"{sep}loadControlEventData: {self.load_control_event_data}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                load_control_event_data=data_dict.get('loadControlEventData'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class LoadControlStateDataElementsType: # EEBus_SPINE_TS_LoadControl.xsd:ns_p:LoadControlStateDataElementsType -> ComplexType
    def __init__(
            self,
            timestamp: ElementTagType = None,
            event_id: ElementTagType = None,
            event_state_consume: ElementTagType = None,
            applied_event_action_consume: ElementTagType = None,
            event_state_produce: ElementTagType = None,
            applied_event_action_produce: ElementTagType = None,
    ):
        super().__init__()
        
        self.timestamp = timestamp
        self.event_id = event_id
        self.event_state_consume = event_state_consume
        self.applied_event_action_consume = applied_event_action_consume
        self.event_state_produce = event_state_produce
        self.applied_event_action_produce = applied_event_action_produce

        if not isinstance(self.timestamp, ElementTagType | NoneType):
            raise TypeError("timestamp is not of type ElementTagType")
        
        if not isinstance(self.event_id, ElementTagType | NoneType):
            raise TypeError("event_id is not of type ElementTagType")
        
        if not isinstance(self.event_state_consume, ElementTagType | NoneType):
            raise TypeError("event_state_consume is not of type ElementTagType")
        
        if not isinstance(self.applied_event_action_consume, ElementTagType | NoneType):
            raise TypeError("applied_event_action_consume is not of type ElementTagType")
        
        if not isinstance(self.event_state_produce, ElementTagType | NoneType):
            raise TypeError("event_state_produce is not of type ElementTagType")
        
        if not isinstance(self.applied_event_action_produce, ElementTagType | NoneType):
            raise TypeError("applied_event_action_produce is not of type ElementTagType")
        
    def get_data(self):

        msg_data = []
        
        if self.timestamp is not None:
            msg_data.append({"timestamp": self.timestamp.get_data()})
        if self.event_id is not None:
            msg_data.append({"eventId": self.event_id.get_data()})
        if self.event_state_consume is not None:
            msg_data.append({"eventStateConsume": self.event_state_consume.get_data()})
        if self.applied_event_action_consume is not None:
            msg_data.append({"appliedEventActionConsume": self.applied_event_action_consume.get_data()})
        if self.event_state_produce is not None:
            msg_data.append({"eventStateProduce": self.event_state_produce.get_data()})
        if self.applied_event_action_produce is not None:
            msg_data.append({"appliedEventActionProduce": self.applied_event_action_produce.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.timestamp is not None:
            result_str += f"{sep}timestamp: {self.timestamp}"
            sep = ", "
        if self.event_id is not None:
            result_str += f"{sep}eventId: {self.event_id}"
            sep = ", "
        if self.event_state_consume is not None:
            result_str += f"{sep}eventStateConsume: {self.event_state_consume}"
            sep = ", "
        if self.applied_event_action_consume is not None:
            result_str += f"{sep}appliedEventActionConsume: {self.applied_event_action_consume}"
            sep = ", "
        if self.event_state_produce is not None:
            result_str += f"{sep}eventStateProduce: {self.event_state_produce}"
            sep = ", "
        if self.applied_event_action_produce is not None:
            result_str += f"{sep}appliedEventActionProduce: {self.applied_event_action_produce}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                timestamp=data_dict.get('timestamp'),
                event_id=data_dict.get('eventId'),
                event_state_consume=data_dict.get('eventStateConsume'),
                applied_event_action_consume=data_dict.get('appliedEventActionConsume'),
                event_state_produce=data_dict.get('eventStateProduce'),
                applied_event_action_produce=data_dict.get('appliedEventActionProduce'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class LoadControlNodeDataElementsType: # EEBus_SPINE_TS_LoadControl.xsd:ns_p:LoadControlNodeDataElementsType -> ComplexType
    def __init__(
            self,
            is_node_remote_controllable: ElementTagType = None,
    ):
        super().__init__()
        
        self.is_node_remote_controllable = is_node_remote_controllable

        if not isinstance(self.is_node_remote_controllable, ElementTagType | NoneType):
            raise TypeError("is_node_remote_controllable is not of type ElementTagType")
        
    def get_data(self):

        msg_data = []
        
        if self.is_node_remote_controllable is not None:
            msg_data.append({"isNodeRemoteControllable": self.is_node_remote_controllable.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.is_node_remote_controllable is not None:
            result_str += f"{sep}isNodeRemoteControllable: {self.is_node_remote_controllable}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                is_node_remote_controllable=data_dict.get('isNodeRemoteControllable'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class LoadControlLimitDescriptionDataElementsType: # EEBus_SPINE_TS_LoadControl.xsd:ns_p:LoadControlLimitDescriptionDataElementsType -> ComplexType
    def __init__(
            self,
            limit_id: ElementTagType = None,
            limit_type: ElementTagType = None,
            limit_category: ElementTagType = None,
            limit_direction: ElementTagType = None,
            measurement_id: ElementTagType = None,
            unit: ElementTagType = None,
            scope_type: ElementTagType = None,
            label: ElementTagType = None,
            description: ElementTagType = None,
    ):
        super().__init__()
        
        self.limit_id = limit_id
        self.limit_type = limit_type
        self.limit_category = limit_category
        self.limit_direction = limit_direction
        self.measurement_id = measurement_id
        self.unit = unit
        self.scope_type = scope_type
        self.label = label
        self.description = description

        if not isinstance(self.limit_id, ElementTagType | NoneType):
            raise TypeError("limit_id is not of type ElementTagType")
        
        if not isinstance(self.limit_type, ElementTagType | NoneType):
            raise TypeError("limit_type is not of type ElementTagType")
        
        if not isinstance(self.limit_category, ElementTagType | NoneType):
            raise TypeError("limit_category is not of type ElementTagType")
        
        if not isinstance(self.limit_direction, ElementTagType | NoneType):
            raise TypeError("limit_direction is not of type ElementTagType")
        
        if not isinstance(self.measurement_id, ElementTagType | NoneType):
            raise TypeError("measurement_id is not of type ElementTagType")
        
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
        
        if self.limit_id is not None:
            msg_data.append({"limitId": self.limit_id.get_data()})
        if self.limit_type is not None:
            msg_data.append({"limitType": self.limit_type.get_data()})
        if self.limit_category is not None:
            msg_data.append({"limitCategory": self.limit_category.get_data()})
        if self.limit_direction is not None:
            msg_data.append({"limitDirection": self.limit_direction.get_data()})
        if self.measurement_id is not None:
            msg_data.append({"measurementId": self.measurement_id.get_data()})
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
        if self.limit_id is not None:
            result_str += f"{sep}limitId: {self.limit_id}"
            sep = ", "
        if self.limit_type is not None:
            result_str += f"{sep}limitType: {self.limit_type}"
            sep = ", "
        if self.limit_category is not None:
            result_str += f"{sep}limitCategory: {self.limit_category}"
            sep = ", "
        if self.limit_direction is not None:
            result_str += f"{sep}limitDirection: {self.limit_direction}"
            sep = ", "
        if self.measurement_id is not None:
            result_str += f"{sep}measurementId: {self.measurement_id}"
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
                limit_id=data_dict.get('limitId'),
                limit_type=data_dict.get('limitType'),
                limit_category=data_dict.get('limitCategory'),
                limit_direction=data_dict.get('limitDirection'),
                measurement_id=data_dict.get('measurementId'),
                unit=data_dict.get('unit'),
                scope_type=data_dict.get('scopeType'),
                label=data_dict.get('label'),
                description=data_dict.get('description'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class LoadControlLimitDataElementsType: # EEBus_SPINE_TS_LoadControl.xsd:ns_p:LoadControlLimitDataElementsType -> ComplexType
    def __init__(
            self,
            limit_id: ElementTagType = None,
            is_limit_changeable: ElementTagType = None,
            is_limit_active: ElementTagType = None,
            time_period: TimePeriodElementsType = None,
            value: ScaledNumberElementsType = None,
    ):
        super().__init__()
        
        self.limit_id = limit_id
        self.is_limit_changeable = is_limit_changeable
        self.is_limit_active = is_limit_active
        self.time_period = time_period
        self.value = value

        if not isinstance(self.limit_id, ElementTagType | NoneType):
            raise TypeError("limit_id is not of type ElementTagType")
        
        if not isinstance(self.is_limit_changeable, ElementTagType | NoneType):
            raise TypeError("is_limit_changeable is not of type ElementTagType")
        
        if not isinstance(self.is_limit_active, ElementTagType | NoneType):
            raise TypeError("is_limit_active is not of type ElementTagType")
        
        if not isinstance(self.time_period, TimePeriodElementsType | NoneType):
            raise TypeError("time_period is not of type TimePeriodElementsType")
        
        if not isinstance(self.value, ScaledNumberElementsType | NoneType):
            raise TypeError("value is not of type ScaledNumberElementsType")
        
    def get_data(self):

        msg_data = []
        
        if self.limit_id is not None:
            msg_data.append({"limitId": self.limit_id.get_data()})
        if self.is_limit_changeable is not None:
            msg_data.append({"isLimitChangeable": self.is_limit_changeable.get_data()})
        if self.is_limit_active is not None:
            msg_data.append({"isLimitActive": self.is_limit_active.get_data()})
        if self.time_period is not None:
            msg_data.append({"timePeriod": self.time_period.get_data()})
        if self.value is not None:
            msg_data.append({"value": self.value.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.limit_id is not None:
            result_str += f"{sep}limitId: {self.limit_id}"
            sep = ", "
        if self.is_limit_changeable is not None:
            result_str += f"{sep}isLimitChangeable: {self.is_limit_changeable}"
            sep = ", "
        if self.is_limit_active is not None:
            result_str += f"{sep}isLimitActive: {self.is_limit_active}"
            sep = ", "
        if self.time_period is not None:
            result_str += f"{sep}timePeriod: {self.time_period}"
            sep = ", "
        if self.value is not None:
            result_str += f"{sep}value: {self.value}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                limit_id=data_dict.get('limitId'),
                is_limit_changeable=data_dict.get('isLimitChangeable'),
                is_limit_active=data_dict.get('isLimitActive'),
                time_period=data_dict.get('timePeriod'),
                value=data_dict.get('value'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class LoadControlLimitConstraintsDataElementsType: # EEBus_SPINE_TS_LoadControl.xsd:ns_p:LoadControlLimitConstraintsDataElementsType -> ComplexType
    def __init__(
            self,
            limit_id: ElementTagType = None,
            value_range_min: ScaledNumberElementsType = None,
            value_range_max: ScaledNumberElementsType = None,
            value_step_size: ScaledNumberElementsType = None,
    ):
        super().__init__()
        
        self.limit_id = limit_id
        self.value_range_min = value_range_min
        self.value_range_max = value_range_max
        self.value_step_size = value_step_size

        if not isinstance(self.limit_id, ElementTagType | NoneType):
            raise TypeError("limit_id is not of type ElementTagType")
        
        if not isinstance(self.value_range_min, ScaledNumberElementsType | NoneType):
            raise TypeError("value_range_min is not of type ScaledNumberElementsType")
        
        if not isinstance(self.value_range_max, ScaledNumberElementsType | NoneType):
            raise TypeError("value_range_max is not of type ScaledNumberElementsType")
        
        if not isinstance(self.value_step_size, ScaledNumberElementsType | NoneType):
            raise TypeError("value_step_size is not of type ScaledNumberElementsType")
        
    def get_data(self):

        msg_data = []
        
        if self.limit_id is not None:
            msg_data.append({"limitId": self.limit_id.get_data()})
        if self.value_range_min is not None:
            msg_data.append({"valueRangeMin": self.value_range_min.get_data()})
        if self.value_range_max is not None:
            msg_data.append({"valueRangeMax": self.value_range_max.get_data()})
        if self.value_step_size is not None:
            msg_data.append({"valueStepSize": self.value_step_size.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.limit_id is not None:
            result_str += f"{sep}limitId: {self.limit_id}"
            sep = ", "
        if self.value_range_min is not None:
            result_str += f"{sep}valueRangeMin: {self.value_range_min}"
            sep = ", "
        if self.value_range_max is not None:
            result_str += f"{sep}valueRangeMax: {self.value_range_max}"
            sep = ", "
        if self.value_step_size is not None:
            result_str += f"{sep}valueStepSize: {self.value_step_size}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                limit_id=data_dict.get('limitId'),
                value_range_min=data_dict.get('valueRangeMin'),
                value_range_max=data_dict.get('valueRangeMax'),
                value_step_size=data_dict.get('valueStepSize'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class LoadControlEventDataElementsType: # EEBus_SPINE_TS_LoadControl.xsd:ns_p:LoadControlEventDataElementsType -> ComplexType
    def __init__(
            self,
            timestamp: ElementTagType = None,
            event_id: ElementTagType = None,
            event_action_consume: ElementTagType = None,
            event_action_produce: ElementTagType = None,
            time_period: TimePeriodElementsType = None,
    ):
        super().__init__()
        
        self.timestamp = timestamp
        self.event_id = event_id
        self.event_action_consume = event_action_consume
        self.event_action_produce = event_action_produce
        self.time_period = time_period

        if not isinstance(self.timestamp, ElementTagType | NoneType):
            raise TypeError("timestamp is not of type ElementTagType")
        
        if not isinstance(self.event_id, ElementTagType | NoneType):
            raise TypeError("event_id is not of type ElementTagType")
        
        if not isinstance(self.event_action_consume, ElementTagType | NoneType):
            raise TypeError("event_action_consume is not of type ElementTagType")
        
        if not isinstance(self.event_action_produce, ElementTagType | NoneType):
            raise TypeError("event_action_produce is not of type ElementTagType")
        
        if not isinstance(self.time_period, TimePeriodElementsType | NoneType):
            raise TypeError("time_period is not of type TimePeriodElementsType")
        
    def get_data(self):

        msg_data = []
        
        if self.timestamp is not None:
            msg_data.append({"timestamp": self.timestamp.get_data()})
        if self.event_id is not None:
            msg_data.append({"eventId": self.event_id.get_data()})
        if self.event_action_consume is not None:
            msg_data.append({"eventActionConsume": self.event_action_consume.get_data()})
        if self.event_action_produce is not None:
            msg_data.append({"eventActionProduce": self.event_action_produce.get_data()})
        if self.time_period is not None:
            msg_data.append({"timePeriod": self.time_period.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.timestamp is not None:
            result_str += f"{sep}timestamp: {self.timestamp}"
            sep = ", "
        if self.event_id is not None:
            result_str += f"{sep}eventId: {self.event_id}"
            sep = ", "
        if self.event_action_consume is not None:
            result_str += f"{sep}eventActionConsume: {self.event_action_consume}"
            sep = ", "
        if self.event_action_produce is not None:
            result_str += f"{sep}eventActionProduce: {self.event_action_produce}"
            sep = ", "
        if self.time_period is not None:
            result_str += f"{sep}timePeriod: {self.time_period}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                timestamp=data_dict.get('timestamp'),
                event_id=data_dict.get('eventId'),
                event_action_consume=data_dict.get('eventActionConsume'),
                event_action_produce=data_dict.get('eventActionProduce'),
                time_period=data_dict.get('timePeriod'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class LoadControlStateListDataSelectorsType: # EEBus_SPINE_TS_LoadControl.xsd:ns_p:LoadControlStateListDataSelectorsType -> ComplexType
    def __init__(
            self,
            timestamp_interval: TimestampIntervalType = None,
            event_id: LoadControlEventIdType = None,
    ):
        super().__init__()
        
        self.timestamp_interval = timestamp_interval
        self.event_id = event_id

        if not isinstance(self.timestamp_interval, TimestampIntervalType | NoneType):
            raise TypeError("timestamp_interval is not of type TimestampIntervalType")
        
        if not isinstance(self.event_id, LoadControlEventIdType | NoneType):
            raise TypeError("event_id is not of type LoadControlEventIdType")
        
    def get_data(self):

        msg_data = []
        
        if self.timestamp_interval is not None:
            msg_data.append({"timestampInterval": self.timestamp_interval.get_data()})
        if self.event_id is not None:
            msg_data.append({"eventId": self.event_id.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.timestamp_interval is not None:
            result_str += f"{sep}timestampInterval: {self.timestamp_interval}"
            sep = ", "
        if self.event_id is not None:
            result_str += f"{sep}eventId: {self.event_id}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                timestamp_interval=data_dict.get('timestampInterval'),
                event_id=data_dict.get('eventId'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class LoadControlLimitListDataSelectorsType: # EEBus_SPINE_TS_LoadControl.xsd:ns_p:LoadControlLimitListDataSelectorsType -> ComplexType
    def __init__(
            self,
            limit_id: LoadControlLimitIdType = None,
    ):
        super().__init__()
        
        self.limit_id = limit_id

        if not isinstance(self.limit_id, LoadControlLimitIdType | NoneType):
            raise TypeError("limit_id is not of type LoadControlLimitIdType")
        
    def get_data(self):

        msg_data = []
        
        if self.limit_id is not None:
            msg_data.append({"limitId": self.limit_id.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.limit_id is not None:
            result_str += f"{sep}limitId: {self.limit_id}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                limit_id=data_dict.get('limitId'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class LoadControlLimitDescriptionListDataSelectorsType: # EEBus_SPINE_TS_LoadControl.xsd:ns_p:LoadControlLimitDescriptionListDataSelectorsType -> ComplexType
    def __init__(
            self,
            limit_id: LoadControlLimitIdType = None,
            limit_type: LoadControlLimitTypeType = None,
            limit_direction: EnergyDirectionType = None,
            measurement_id: MeasurementIdType = None,
            scope_type: ScopeTypeType = None,
    ):
        super().__init__()
        
        self.limit_id = limit_id
        self.limit_type = limit_type
        self.limit_direction = limit_direction
        self.measurement_id = measurement_id
        self.scope_type = scope_type

        if not isinstance(self.limit_id, LoadControlLimitIdType | NoneType):
            raise TypeError("limit_id is not of type LoadControlLimitIdType")
        
        if not isinstance(self.limit_type, LoadControlLimitTypeType | NoneType):
            raise TypeError("limit_type is not of type LoadControlLimitTypeType")
        
        if not isinstance(self.limit_direction, EnergyDirectionType | NoneType):
            raise TypeError("limit_direction is not of type EnergyDirectionType")
        
        if not isinstance(self.measurement_id, MeasurementIdType | NoneType):
            raise TypeError("measurement_id is not of type MeasurementIdType")
        
        if not isinstance(self.scope_type, ScopeTypeType | NoneType):
            raise TypeError("scope_type is not of type ScopeTypeType")
        
    def get_data(self):

        msg_data = []
        
        if self.limit_id is not None:
            msg_data.append({"limitId": self.limit_id.get_data()})
        if self.limit_type is not None:
            msg_data.append({"limitType": self.limit_type.get_data()})
        if self.limit_direction is not None:
            msg_data.append({"limitDirection": self.limit_direction.get_data()})
        if self.measurement_id is not None:
            msg_data.append({"measurementId": self.measurement_id.get_data()})
        if self.scope_type is not None:
            msg_data.append({"scopeType": self.scope_type.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.limit_id is not None:
            result_str += f"{sep}limitId: {self.limit_id}"
            sep = ", "
        if self.limit_type is not None:
            result_str += f"{sep}limitType: {self.limit_type}"
            sep = ", "
        if self.limit_direction is not None:
            result_str += f"{sep}limitDirection: {self.limit_direction}"
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
                limit_id=data_dict.get('limitId'),
                limit_type=data_dict.get('limitType'),
                limit_direction=data_dict.get('limitDirection'),
                measurement_id=data_dict.get('measurementId'),
                scope_type=data_dict.get('scopeType'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class LoadControlLimitConstraintsListDataSelectorsType: # EEBus_SPINE_TS_LoadControl.xsd:ns_p:LoadControlLimitConstraintsListDataSelectorsType -> ComplexType
    def __init__(
            self,
            limit_id: LoadControlLimitIdType = None,
    ):
        super().__init__()
        
        self.limit_id = limit_id

        if not isinstance(self.limit_id, LoadControlLimitIdType | NoneType):
            raise TypeError("limit_id is not of type LoadControlLimitIdType")
        
    def get_data(self):

        msg_data = []
        
        if self.limit_id is not None:
            msg_data.append({"limitId": self.limit_id.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.limit_id is not None:
            result_str += f"{sep}limitId: {self.limit_id}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                limit_id=data_dict.get('limitId'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class LoadControlEventListDataSelectorsType: # EEBus_SPINE_TS_LoadControl.xsd:ns_p:LoadControlEventListDataSelectorsType -> ComplexType
    def __init__(
            self,
            timestamp_interval: TimestampIntervalType = None,
            event_id: LoadControlEventIdType = None,
    ):
        super().__init__()
        
        self.timestamp_interval = timestamp_interval
        self.event_id = event_id

        if not isinstance(self.timestamp_interval, TimestampIntervalType | NoneType):
            raise TypeError("timestamp_interval is not of type TimestampIntervalType")
        
        if not isinstance(self.event_id, LoadControlEventIdType | NoneType):
            raise TypeError("event_id is not of type LoadControlEventIdType")
        
    def get_data(self):

        msg_data = []
        
        if self.timestamp_interval is not None:
            msg_data.append({"timestampInterval": self.timestamp_interval.get_data()})
        if self.event_id is not None:
            msg_data.append({"eventId": self.event_id.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.timestamp_interval is not None:
            result_str += f"{sep}timestampInterval: {self.timestamp_interval}"
            sep = ", "
        if self.event_id is not None:
            result_str += f"{sep}eventId: {self.event_id}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                timestamp_interval=data_dict.get('timestampInterval'),
                event_id=data_dict.get('eventId'),
            )
        elif data:
            return cls(data)
        else:
            return cls()



