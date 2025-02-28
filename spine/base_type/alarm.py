# Jinja Template message_type.py.jinja2
from spine.base_type.commondatatypes import ElementTagType
from spine.base_type.commondatatypes import ScaledNumberElementsType
from spine.base_type.commondatatypes import ScaledNumberType
from spine.base_type.commondatatypes import TimePeriodElementsType
from spine.base_type.commondatatypes import TimePeriodType
from spine.simple_type.alarm import AlarmIdType
from spine.simple_type.commondatatypes import DescriptionType
from spine.simple_type.commondatatypes import LabelType
from spine.simple_type.threshold import ThresholdIdType
from spine.union_type.alarm import AlarmTypeType
from spine.union_type.commondatatypes import AbsoluteOrRelativeTimeType
from spine.union_type.commondatatypes import ScopeTypeType
from types import NoneType
from spine import array_2_dict


class AlarmDataType: # EEBus_SPINE_TS_Alarm.xsd: ComplexType
    def __init__(
            self,
            alarm_id: AlarmIdType = None,
            threshold_id: ThresholdIdType = None,
            timestamp: AbsoluteOrRelativeTimeType = None,
            alarm_type: AlarmTypeType = None,
            measured_value: ScaledNumberType = None,
            evaluation_period: TimePeriodType = None,
            scope_type: ScopeTypeType = None,
            label: LabelType = None,
            description: DescriptionType = None,
    ):
        super().__init__()
        
        self.alarm_id = alarm_id
        self.threshold_id = threshold_id
        self.timestamp = timestamp
        self.alarm_type = alarm_type
        self.measured_value = measured_value
        self.evaluation_period = evaluation_period
        self.scope_type = scope_type
        self.label = label
        self.description = description

        if not isinstance(self.alarm_id, AlarmIdType | NoneType):
            raise TypeError("alarm_id is not of type AlarmIdType")
        
        if not isinstance(self.threshold_id, ThresholdIdType | NoneType):
            raise TypeError("threshold_id is not of type ThresholdIdType")
        
        if not isinstance(self.timestamp, AbsoluteOrRelativeTimeType | NoneType):
            raise TypeError("timestamp is not of type AbsoluteOrRelativeTimeType")
        
        if not isinstance(self.alarm_type, AlarmTypeType | NoneType):
            raise TypeError("alarm_type is not of type AlarmTypeType")
        
        if not isinstance(self.measured_value, ScaledNumberType | NoneType):
            raise TypeError("measured_value is not of type ScaledNumberType")
        
        if not isinstance(self.evaluation_period, TimePeriodType | NoneType):
            raise TypeError("evaluation_period is not of type TimePeriodType")
        
        if not isinstance(self.scope_type, ScopeTypeType | NoneType):
            raise TypeError("scope_type is not of type ScopeTypeType")
        
        if not isinstance(self.label, LabelType | NoneType):
            raise TypeError("label is not of type LabelType")
        
        if not isinstance(self.description, DescriptionType | NoneType):
            raise TypeError("description is not of type DescriptionType")
        
    def get_data(self):

        msg_data = []
        
        if self.alarm_id is not None:
            msg_data.append({"alarmId": self.alarm_id.get_data()})
        if self.threshold_id is not None:
            msg_data.append({"thresholdId": self.threshold_id.get_data()})
        if self.timestamp is not None:
            msg_data.append({"timestamp": self.timestamp.get_data()})
        if self.alarm_type is not None:
            msg_data.append({"alarmType": self.alarm_type.get_data()})
        if self.measured_value is not None:
            msg_data.append({"measuredValue": self.measured_value.get_data()})
        if self.evaluation_period is not None:
            msg_data.append({"evaluationPeriod": self.evaluation_period.get_data()})
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
        if self.alarm_id is not None:
            result_str += f"{sep}alarmId: {self.alarm_id}"
            sep = ", "
        if self.threshold_id is not None:
            result_str += f"{sep}thresholdId: {self.threshold_id}"
            sep = ", "
        if self.timestamp is not None:
            result_str += f"{sep}timestamp: {self.timestamp}"
            sep = ", "
        if self.alarm_type is not None:
            result_str += f"{sep}alarmType: {self.alarm_type}"
            sep = ", "
        if self.measured_value is not None:
            result_str += f"{sep}measuredValue: {self.measured_value}"
            sep = ", "
        if self.evaluation_period is not None:
            result_str += f"{sep}evaluationPeriod: {self.evaluation_period}"
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
                alarm_id=data_dict.get('alarmId'),
                threshold_id=data_dict.get('thresholdId'),
                timestamp=data_dict.get('timestamp'),
                alarm_type=data_dict.get('alarmType'),
                measured_value=data_dict.get('measuredValue'),
                evaluation_period=data_dict.get('evaluationPeriod'),
                scope_type=data_dict.get('scopeType'),
                label=data_dict.get('label'),
                description=data_dict.get('description'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class AlarmListDataType: # EEBus_SPINE_TS_Alarm.xsd: ComplexType
    def __init__(
            self,
            alarm_data: list[AlarmDataType] = None,
    ):
        super().__init__()
        
        self.alarm_data = alarm_data

        if not isinstance(self.alarm_data, list | NoneType):
            raise TypeError("alarm_data is not of type list[AlarmDataType]")
        
    def get_data(self):

        msg_data = []
        
        if self.alarm_data is not None:
            msg_data.append({"alarmData": [d.get_data() for d in self.alarm_data]})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.alarm_data is not None:
            result_str += f"{sep}alarmData: {self.alarm_data}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                alarm_data=data_dict.get('alarmData'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class AlarmDataElementsType: # EEBus_SPINE_TS_Alarm.xsd: ComplexType
    def __init__(
            self,
            alarm_id: ElementTagType = None,
            threshold_id: ElementTagType = None,
            timestamp: ElementTagType = None,
            alarm_type: ElementTagType = None,
            measured_value: ScaledNumberElementsType = None,
            evaluation_period: TimePeriodElementsType = None,
            scope_type: ElementTagType = None,
            label: ElementTagType = None,
            description: ElementTagType = None,
    ):
        super().__init__()
        
        self.alarm_id = alarm_id
        self.threshold_id = threshold_id
        self.timestamp = timestamp
        self.alarm_type = alarm_type
        self.measured_value = measured_value
        self.evaluation_period = evaluation_period
        self.scope_type = scope_type
        self.label = label
        self.description = description

        if not isinstance(self.alarm_id, ElementTagType | NoneType):
            raise TypeError("alarm_id is not of type ElementTagType")
        
        if not isinstance(self.threshold_id, ElementTagType | NoneType):
            raise TypeError("threshold_id is not of type ElementTagType")
        
        if not isinstance(self.timestamp, ElementTagType | NoneType):
            raise TypeError("timestamp is not of type ElementTagType")
        
        if not isinstance(self.alarm_type, ElementTagType | NoneType):
            raise TypeError("alarm_type is not of type ElementTagType")
        
        if not isinstance(self.measured_value, ScaledNumberElementsType | NoneType):
            raise TypeError("measured_value is not of type ScaledNumberElementsType")
        
        if not isinstance(self.evaluation_period, TimePeriodElementsType | NoneType):
            raise TypeError("evaluation_period is not of type TimePeriodElementsType")
        
        if not isinstance(self.scope_type, ElementTagType | NoneType):
            raise TypeError("scope_type is not of type ElementTagType")
        
        if not isinstance(self.label, ElementTagType | NoneType):
            raise TypeError("label is not of type ElementTagType")
        
        if not isinstance(self.description, ElementTagType | NoneType):
            raise TypeError("description is not of type ElementTagType")
        
    def get_data(self):

        msg_data = []
        
        if self.alarm_id is not None:
            msg_data.append({"alarmId": self.alarm_id.get_data()})
        if self.threshold_id is not None:
            msg_data.append({"thresholdId": self.threshold_id.get_data()})
        if self.timestamp is not None:
            msg_data.append({"timestamp": self.timestamp.get_data()})
        if self.alarm_type is not None:
            msg_data.append({"alarmType": self.alarm_type.get_data()})
        if self.measured_value is not None:
            msg_data.append({"measuredValue": self.measured_value.get_data()})
        if self.evaluation_period is not None:
            msg_data.append({"evaluationPeriod": self.evaluation_period.get_data()})
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
        if self.alarm_id is not None:
            result_str += f"{sep}alarmId: {self.alarm_id}"
            sep = ", "
        if self.threshold_id is not None:
            result_str += f"{sep}thresholdId: {self.threshold_id}"
            sep = ", "
        if self.timestamp is not None:
            result_str += f"{sep}timestamp: {self.timestamp}"
            sep = ", "
        if self.alarm_type is not None:
            result_str += f"{sep}alarmType: {self.alarm_type}"
            sep = ", "
        if self.measured_value is not None:
            result_str += f"{sep}measuredValue: {self.measured_value}"
            sep = ", "
        if self.evaluation_period is not None:
            result_str += f"{sep}evaluationPeriod: {self.evaluation_period}"
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
                alarm_id=data_dict.get('alarmId'),
                threshold_id=data_dict.get('thresholdId'),
                timestamp=data_dict.get('timestamp'),
                alarm_type=data_dict.get('alarmType'),
                measured_value=data_dict.get('measuredValue'),
                evaluation_period=data_dict.get('evaluationPeriod'),
                scope_type=data_dict.get('scopeType'),
                label=data_dict.get('label'),
                description=data_dict.get('description'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class AlarmListDataSelectorsType: # EEBus_SPINE_TS_Alarm.xsd: ComplexType
    def __init__(
            self,
            alarm_id: AlarmIdType = None,
            scope_type: ScopeTypeType = None,
    ):
        super().__init__()
        
        self.alarm_id = alarm_id
        self.scope_type = scope_type

        if not isinstance(self.alarm_id, AlarmIdType | NoneType):
            raise TypeError("alarm_id is not of type AlarmIdType")
        
        if not isinstance(self.scope_type, ScopeTypeType | NoneType):
            raise TypeError("scope_type is not of type ScopeTypeType")
        
    def get_data(self):

        msg_data = []
        
        if self.alarm_id is not None:
            msg_data.append({"alarmId": self.alarm_id.get_data()})
        if self.scope_type is not None:
            msg_data.append({"scopeType": self.scope_type.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.alarm_id is not None:
            result_str += f"{sep}alarmId: {self.alarm_id}"
            sep = ", "
        if self.scope_type is not None:
            result_str += f"{sep}scopeType: {self.scope_type}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                alarm_id=data_dict.get('alarmId'),
                scope_type=data_dict.get('scopeType'),
            )
        elif data:
            return cls(data)
        else:
            return cls()



