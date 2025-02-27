# Jinja Template message_type.py.jinja2
from spine.simple_type.commondatatypes import LabelType
from spine.base_type.commondatatypes import TimePeriodElementsType
from spine.base_type.commondatatypes import TimestampIntervalType
from spine.simple_type.commondatatypes import DescriptionType
from spine.base_type.commondatatypes import ScaledNumberElementsType
from spine.base_type.commondatatypes import ElementTagType
from spine.simple_type.measurement import MeasurementIdType
from spine.union_type.commondatatypes import FunctionType
from spine.base_type.commondatatypes import ScaledNumberType
from spine.simple_type.threshold import ThresholdIdType
from spine.base_type.commondatatypes import TimePeriodType
from types import NoneType
from spine import array_2_dict


class MeasurementThresholdRelationDataType:
    def __init__(
            self,
            measurement_id: MeasurementIdType = None,
            threshold_id: list[ThresholdIdType] = None,
    ):
        super().__init__()
        
        self.measurement_id = measurement_id
        self.threshold_id = threshold_id

        if not isinstance(self.measurement_id, MeasurementIdType | NoneType):
            raise TypeError("measurement_id is not of type MeasurementIdType")
        
        if not isinstance(self.threshold_id, list | NoneType):
            raise TypeError("threshold_id is not of type list[ThresholdIdType]")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.measurement_id is not None:
            msg_data.append({"measurementId": self.measurement_id.get_data()})
        if self.threshold_id is not None:
            msg_data.append({"thresholdId": [d.get_data() for d in self.threshold_id]})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.measurement_id is not None:
            result_str += f"{sep}measurementId: {self.measurement_id}"
            sep = ", "
        if self.threshold_id is not None:
            result_str += f"{sep}thresholdId: {self.threshold_id}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                measurement_id=data_dict.get('measurementId'),
                threshold_id=data_dict.get('thresholdId'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class MeasurementSeriesDataType:
    def __init__(
            self,
            measurement_id: MeasurementIdType = None,
            value_type: FunctionType = None,
            timestamp: FunctionType = None,
            value: ScaledNumberType = None,
            evaluation_period: TimePeriodType = None,
            value_source: FunctionType = None,
            value_tendency: FunctionType = None,
            value_state: FunctionType = None,
    ):
        super().__init__()
        
        self.measurement_id = measurement_id
        self.value_type = value_type
        self.timestamp = timestamp
        self.value = value
        self.evaluation_period = evaluation_period
        self.value_source = value_source
        self.value_tendency = value_tendency
        self.value_state = value_state

        if not isinstance(self.measurement_id, MeasurementIdType | NoneType):
            raise TypeError("measurement_id is not of type MeasurementIdType")
        
        if not isinstance(self.value_type, FunctionType | NoneType):
            raise TypeError("value_type is not of type FunctionType")
        
        if not isinstance(self.timestamp, FunctionType | NoneType):
            raise TypeError("timestamp is not of type FunctionType")
        
        if not isinstance(self.value, ScaledNumberType | NoneType):
            raise TypeError("value is not of type ScaledNumberType")
        
        if not isinstance(self.evaluation_period, TimePeriodType | NoneType):
            raise TypeError("evaluation_period is not of type TimePeriodType")
        
        if not isinstance(self.value_source, FunctionType | NoneType):
            raise TypeError("value_source is not of type FunctionType")
        
        if not isinstance(self.value_tendency, FunctionType | NoneType):
            raise TypeError("value_tendency is not of type FunctionType")
        
        if not isinstance(self.value_state, FunctionType | NoneType):
            raise TypeError("value_state is not of type FunctionType")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.measurement_id is not None:
            msg_data.append({"measurementId": self.measurement_id.get_data()})
        if self.value_type is not None:
            msg_data.append({"valueType": self.value_type.get_data()})
        if self.timestamp is not None:
            msg_data.append({"timestamp": self.timestamp.get_data()})
        if self.value is not None:
            msg_data.append({"value": self.value.get_data()})
        if self.evaluation_period is not None:
            msg_data.append({"evaluationPeriod": self.evaluation_period.get_data()})
        if self.value_source is not None:
            msg_data.append({"valueSource": self.value_source.get_data()})
        if self.value_tendency is not None:
            msg_data.append({"valueTendency": self.value_tendency.get_data()})
        if self.value_state is not None:
            msg_data.append({"valueState": self.value_state.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.measurement_id is not None:
            result_str += f"{sep}measurementId: {self.measurement_id}"
            sep = ", "
        if self.value_type is not None:
            result_str += f"{sep}valueType: {self.value_type}"
            sep = ", "
        if self.timestamp is not None:
            result_str += f"{sep}timestamp: {self.timestamp}"
            sep = ", "
        if self.value is not None:
            result_str += f"{sep}value: {self.value}"
            sep = ", "
        if self.evaluation_period is not None:
            result_str += f"{sep}evaluationPeriod: {self.evaluation_period}"
            sep = ", "
        if self.value_source is not None:
            result_str += f"{sep}valueSource: {self.value_source}"
            sep = ", "
        if self.value_tendency is not None:
            result_str += f"{sep}valueTendency: {self.value_tendency}"
            sep = ", "
        if self.value_state is not None:
            result_str += f"{sep}valueState: {self.value_state}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                measurement_id=data_dict.get('measurementId'),
                value_type=data_dict.get('valueType'),
                timestamp=data_dict.get('timestamp'),
                value=data_dict.get('value'),
                evaluation_period=data_dict.get('evaluationPeriod'),
                value_source=data_dict.get('valueSource'),
                value_tendency=data_dict.get('valueTendency'),
                value_state=data_dict.get('valueState'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class MeasurementDataType:
    def __init__(
            self,
            measurement_id: MeasurementIdType = None,
            value_type: FunctionType = None,
            timestamp: FunctionType = None,
            value: ScaledNumberType = None,
            evaluation_period: TimePeriodType = None,
            value_source: FunctionType = None,
            value_tendency: FunctionType = None,
            value_state: FunctionType = None,
    ):
        super().__init__()
        
        self.measurement_id = measurement_id
        self.value_type = value_type
        self.timestamp = timestamp
        self.value = value
        self.evaluation_period = evaluation_period
        self.value_source = value_source
        self.value_tendency = value_tendency
        self.value_state = value_state

        if not isinstance(self.measurement_id, MeasurementIdType | NoneType):
            raise TypeError("measurement_id is not of type MeasurementIdType")
        
        if not isinstance(self.value_type, FunctionType | NoneType):
            raise TypeError("value_type is not of type FunctionType")
        
        if not isinstance(self.timestamp, FunctionType | NoneType):
            raise TypeError("timestamp is not of type FunctionType")
        
        if not isinstance(self.value, ScaledNumberType | NoneType):
            raise TypeError("value is not of type ScaledNumberType")
        
        if not isinstance(self.evaluation_period, TimePeriodType | NoneType):
            raise TypeError("evaluation_period is not of type TimePeriodType")
        
        if not isinstance(self.value_source, FunctionType | NoneType):
            raise TypeError("value_source is not of type FunctionType")
        
        if not isinstance(self.value_tendency, FunctionType | NoneType):
            raise TypeError("value_tendency is not of type FunctionType")
        
        if not isinstance(self.value_state, FunctionType | NoneType):
            raise TypeError("value_state is not of type FunctionType")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.measurement_id is not None:
            msg_data.append({"measurementId": self.measurement_id.get_data()})
        if self.value_type is not None:
            msg_data.append({"valueType": self.value_type.get_data()})
        if self.timestamp is not None:
            msg_data.append({"timestamp": self.timestamp.get_data()})
        if self.value is not None:
            msg_data.append({"value": self.value.get_data()})
        if self.evaluation_period is not None:
            msg_data.append({"evaluationPeriod": self.evaluation_period.get_data()})
        if self.value_source is not None:
            msg_data.append({"valueSource": self.value_source.get_data()})
        if self.value_tendency is not None:
            msg_data.append({"valueTendency": self.value_tendency.get_data()})
        if self.value_state is not None:
            msg_data.append({"valueState": self.value_state.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.measurement_id is not None:
            result_str += f"{sep}measurementId: {self.measurement_id}"
            sep = ", "
        if self.value_type is not None:
            result_str += f"{sep}valueType: {self.value_type}"
            sep = ", "
        if self.timestamp is not None:
            result_str += f"{sep}timestamp: {self.timestamp}"
            sep = ", "
        if self.value is not None:
            result_str += f"{sep}value: {self.value}"
            sep = ", "
        if self.evaluation_period is not None:
            result_str += f"{sep}evaluationPeriod: {self.evaluation_period}"
            sep = ", "
        if self.value_source is not None:
            result_str += f"{sep}valueSource: {self.value_source}"
            sep = ", "
        if self.value_tendency is not None:
            result_str += f"{sep}valueTendency: {self.value_tendency}"
            sep = ", "
        if self.value_state is not None:
            result_str += f"{sep}valueState: {self.value_state}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                measurement_id=data_dict.get('measurementId'),
                value_type=data_dict.get('valueType'),
                timestamp=data_dict.get('timestamp'),
                value=data_dict.get('value'),
                evaluation_period=data_dict.get('evaluationPeriod'),
                value_source=data_dict.get('valueSource'),
                value_tendency=data_dict.get('valueTendency'),
                value_state=data_dict.get('valueState'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class MeasurementDescriptionDataType:
    def __init__(
            self,
            measurement_id: MeasurementIdType = None,
            measurement_type: FunctionType = None,
            commodity_type: FunctionType = None,
            unit: FunctionType = None,
            calibration_value: ScaledNumberType = None,
            scope_type: FunctionType = None,
            label: LabelType = None,
            description: DescriptionType = None,
    ):
        super().__init__()
        
        self.measurement_id = measurement_id
        self.measurement_type = measurement_type
        self.commodity_type = commodity_type
        self.unit = unit
        self.calibration_value = calibration_value
        self.scope_type = scope_type
        self.label = label
        self.description = description

        if not isinstance(self.measurement_id, MeasurementIdType | NoneType):
            raise TypeError("measurement_id is not of type MeasurementIdType")
        
        if not isinstance(self.measurement_type, FunctionType | NoneType):
            raise TypeError("measurement_type is not of type FunctionType")
        
        if not isinstance(self.commodity_type, FunctionType | NoneType):
            raise TypeError("commodity_type is not of type FunctionType")
        
        if not isinstance(self.unit, FunctionType | NoneType):
            raise TypeError("unit is not of type FunctionType")
        
        if not isinstance(self.calibration_value, ScaledNumberType | NoneType):
            raise TypeError("calibration_value is not of type ScaledNumberType")
        
        if not isinstance(self.scope_type, FunctionType | NoneType):
            raise TypeError("scope_type is not of type FunctionType")
        
        if not isinstance(self.label, LabelType | NoneType):
            raise TypeError("label is not of type LabelType")
        
        if not isinstance(self.description, DescriptionType | NoneType):
            raise TypeError("description is not of type DescriptionType")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.measurement_id is not None:
            msg_data.append({"measurementId": self.measurement_id.get_data()})
        if self.measurement_type is not None:
            msg_data.append({"measurementType": self.measurement_type.get_data()})
        if self.commodity_type is not None:
            msg_data.append({"commodityType": self.commodity_type.get_data()})
        if self.unit is not None:
            msg_data.append({"unit": self.unit.get_data()})
        if self.calibration_value is not None:
            msg_data.append({"calibrationValue": self.calibration_value.get_data()})
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
        if self.measurement_id is not None:
            result_str += f"{sep}measurementId: {self.measurement_id}"
            sep = ", "
        if self.measurement_type is not None:
            result_str += f"{sep}measurementType: {self.measurement_type}"
            sep = ", "
        if self.commodity_type is not None:
            result_str += f"{sep}commodityType: {self.commodity_type}"
            sep = ", "
        if self.unit is not None:
            result_str += f"{sep}unit: {self.unit}"
            sep = ", "
        if self.calibration_value is not None:
            result_str += f"{sep}calibrationValue: {self.calibration_value}"
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
                measurement_id=data_dict.get('measurementId'),
                measurement_type=data_dict.get('measurementType'),
                commodity_type=data_dict.get('commodityType'),
                unit=data_dict.get('unit'),
                calibration_value=data_dict.get('calibrationValue'),
                scope_type=data_dict.get('scopeType'),
                label=data_dict.get('label'),
                description=data_dict.get('description'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class MeasurementConstraintsDataType:
    def __init__(
            self,
            measurement_id: MeasurementIdType = None,
            value_range_min: ScaledNumberType = None,
            value_range_max: ScaledNumberType = None,
            value_step_size: ScaledNumberType = None,
    ):
        super().__init__()
        
        self.measurement_id = measurement_id
        self.value_range_min = value_range_min
        self.value_range_max = value_range_max
        self.value_step_size = value_step_size

        if not isinstance(self.measurement_id, MeasurementIdType | NoneType):
            raise TypeError("measurement_id is not of type MeasurementIdType")
        
        if not isinstance(self.value_range_min, ScaledNumberType | NoneType):
            raise TypeError("value_range_min is not of type ScaledNumberType")
        
        if not isinstance(self.value_range_max, ScaledNumberType | NoneType):
            raise TypeError("value_range_max is not of type ScaledNumberType")
        
        if not isinstance(self.value_step_size, ScaledNumberType | NoneType):
            raise TypeError("value_step_size is not of type ScaledNumberType")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.measurement_id is not None:
            msg_data.append({"measurementId": self.measurement_id.get_data()})
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
        if self.measurement_id is not None:
            result_str += f"{sep}measurementId: {self.measurement_id}"
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
                measurement_id=data_dict.get('measurementId'),
                value_range_min=data_dict.get('valueRangeMin'),
                value_range_max=data_dict.get('valueRangeMax'),
                value_step_size=data_dict.get('valueStepSize'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class MeasurementThresholdRelationListDataType:
    def __init__(
            self,
            measurement_threshold_relation_data: list[MeasurementThresholdRelationDataType] = None,
    ):
        super().__init__()
        
        self.measurement_threshold_relation_data = measurement_threshold_relation_data

        if not isinstance(self.measurement_threshold_relation_data, list | NoneType):
            raise TypeError("measurement_threshold_relation_data is not of type list[MeasurementThresholdRelationDataType]")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.measurement_threshold_relation_data is not None:
            msg_data.append({"measurementThresholdRelationData": [d.get_data() for d in self.measurement_threshold_relation_data]})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.measurement_threshold_relation_data is not None:
            result_str += f"{sep}measurementThresholdRelationData: {self.measurement_threshold_relation_data}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                measurement_threshold_relation_data=data_dict.get('measurementThresholdRelationData'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class MeasurementThresholdRelationListDataSelectorsType:
    def __init__(
            self,
            measurement_id: MeasurementIdType = None,
            threshold_id: ThresholdIdType = None,
    ):
        super().__init__()
        
        self.measurement_id = measurement_id
        self.threshold_id = threshold_id

        if not isinstance(self.measurement_id, MeasurementIdType | NoneType):
            raise TypeError("measurement_id is not of type MeasurementIdType")
        
        if not isinstance(self.threshold_id, ThresholdIdType | NoneType):
            raise TypeError("threshold_id is not of type ThresholdIdType")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.measurement_id is not None:
            msg_data.append({"measurementId": self.measurement_id.get_data()})
        if self.threshold_id is not None:
            msg_data.append({"thresholdId": self.threshold_id.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.measurement_id is not None:
            result_str += f"{sep}measurementId: {self.measurement_id}"
            sep = ", "
        if self.threshold_id is not None:
            result_str += f"{sep}thresholdId: {self.threshold_id}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                measurement_id=data_dict.get('measurementId'),
                threshold_id=data_dict.get('thresholdId'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class MeasurementThresholdRelationDataElementsType:
    def __init__(
            self,
            measurement_id: ElementTagType = None,
            threshold_id: ElementTagType = None,
    ):
        super().__init__()
        
        self.measurement_id = measurement_id
        self.threshold_id = threshold_id

        if not isinstance(self.measurement_id, ElementTagType | NoneType):
            raise TypeError("measurement_id is not of type ElementTagType")
        
        if not isinstance(self.threshold_id, ElementTagType | NoneType):
            raise TypeError("threshold_id is not of type ElementTagType")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.measurement_id is not None:
            msg_data.append({"measurementId": self.measurement_id.get_data()})
        if self.threshold_id is not None:
            msg_data.append({"thresholdId": self.threshold_id.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.measurement_id is not None:
            result_str += f"{sep}measurementId: {self.measurement_id}"
            sep = ", "
        if self.threshold_id is not None:
            result_str += f"{sep}thresholdId: {self.threshold_id}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                measurement_id=data_dict.get('measurementId'),
                threshold_id=data_dict.get('thresholdId'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class MeasurementSeriesListDataType:
    def __init__(
            self,
            measurement_series_data: list[MeasurementSeriesDataType] = None,
    ):
        super().__init__()
        
        self.measurement_series_data = measurement_series_data

        if not isinstance(self.measurement_series_data, list | NoneType):
            raise TypeError("measurement_series_data is not of type list[MeasurementSeriesDataType]")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.measurement_series_data is not None:
            msg_data.append({"measurementSeriesData": [d.get_data() for d in self.measurement_series_data]})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.measurement_series_data is not None:
            result_str += f"{sep}measurementSeriesData: {self.measurement_series_data}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                measurement_series_data=data_dict.get('measurementSeriesData'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class MeasurementSeriesListDataSelectorsType:
    def __init__(
            self,
            measurement_id: MeasurementIdType = None,
            value_type: FunctionType = None,
            timestamp_interval: TimestampIntervalType = None,
    ):
        super().__init__()
        
        self.measurement_id = measurement_id
        self.value_type = value_type
        self.timestamp_interval = timestamp_interval

        if not isinstance(self.measurement_id, MeasurementIdType | NoneType):
            raise TypeError("measurement_id is not of type MeasurementIdType")
        
        if not isinstance(self.value_type, FunctionType | NoneType):
            raise TypeError("value_type is not of type FunctionType")
        
        if not isinstance(self.timestamp_interval, TimestampIntervalType | NoneType):
            raise TypeError("timestamp_interval is not of type TimestampIntervalType")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.measurement_id is not None:
            msg_data.append({"measurementId": self.measurement_id.get_data()})
        if self.value_type is not None:
            msg_data.append({"valueType": self.value_type.get_data()})
        if self.timestamp_interval is not None:
            msg_data.append({"timestampInterval": self.timestamp_interval.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.measurement_id is not None:
            result_str += f"{sep}measurementId: {self.measurement_id}"
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
                measurement_id=data_dict.get('measurementId'),
                value_type=data_dict.get('valueType'),
                timestamp_interval=data_dict.get('timestampInterval'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class MeasurementSeriesDataElementsType:
    def __init__(
            self,
            measurement_id: ElementTagType = None,
            value_type: ElementTagType = None,
            timestamp: ElementTagType = None,
            value: ScaledNumberElementsType = None,
            evaluation_period: TimePeriodElementsType = None,
            value_source: ElementTagType = None,
            value_tendency: ElementTagType = None,
            value_state: ElementTagType = None,
    ):
        super().__init__()
        
        self.measurement_id = measurement_id
        self.value_type = value_type
        self.timestamp = timestamp
        self.value = value
        self.evaluation_period = evaluation_period
        self.value_source = value_source
        self.value_tendency = value_tendency
        self.value_state = value_state

        if not isinstance(self.measurement_id, ElementTagType | NoneType):
            raise TypeError("measurement_id is not of type ElementTagType")
        
        if not isinstance(self.value_type, ElementTagType | NoneType):
            raise TypeError("value_type is not of type ElementTagType")
        
        if not isinstance(self.timestamp, ElementTagType | NoneType):
            raise TypeError("timestamp is not of type ElementTagType")
        
        if not isinstance(self.value, ScaledNumberElementsType | NoneType):
            raise TypeError("value is not of type ScaledNumberElementsType")
        
        if not isinstance(self.evaluation_period, TimePeriodElementsType | NoneType):
            raise TypeError("evaluation_period is not of type TimePeriodElementsType")
        
        if not isinstance(self.value_source, ElementTagType | NoneType):
            raise TypeError("value_source is not of type ElementTagType")
        
        if not isinstance(self.value_tendency, ElementTagType | NoneType):
            raise TypeError("value_tendency is not of type ElementTagType")
        
        if not isinstance(self.value_state, ElementTagType | NoneType):
            raise TypeError("value_state is not of type ElementTagType")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.measurement_id is not None:
            msg_data.append({"measurementId": self.measurement_id.get_data()})
        if self.value_type is not None:
            msg_data.append({"valueType": self.value_type.get_data()})
        if self.timestamp is not None:
            msg_data.append({"timestamp": self.timestamp.get_data()})
        if self.value is not None:
            msg_data.append({"value": self.value.get_data()})
        if self.evaluation_period is not None:
            msg_data.append({"evaluationPeriod": self.evaluation_period.get_data()})
        if self.value_source is not None:
            msg_data.append({"valueSource": self.value_source.get_data()})
        if self.value_tendency is not None:
            msg_data.append({"valueTendency": self.value_tendency.get_data()})
        if self.value_state is not None:
            msg_data.append({"valueState": self.value_state.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.measurement_id is not None:
            result_str += f"{sep}measurementId: {self.measurement_id}"
            sep = ", "
        if self.value_type is not None:
            result_str += f"{sep}valueType: {self.value_type}"
            sep = ", "
        if self.timestamp is not None:
            result_str += f"{sep}timestamp: {self.timestamp}"
            sep = ", "
        if self.value is not None:
            result_str += f"{sep}value: {self.value}"
            sep = ", "
        if self.evaluation_period is not None:
            result_str += f"{sep}evaluationPeriod: {self.evaluation_period}"
            sep = ", "
        if self.value_source is not None:
            result_str += f"{sep}valueSource: {self.value_source}"
            sep = ", "
        if self.value_tendency is not None:
            result_str += f"{sep}valueTendency: {self.value_tendency}"
            sep = ", "
        if self.value_state is not None:
            result_str += f"{sep}valueState: {self.value_state}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                measurement_id=data_dict.get('measurementId'),
                value_type=data_dict.get('valueType'),
                timestamp=data_dict.get('timestamp'),
                value=data_dict.get('value'),
                evaluation_period=data_dict.get('evaluationPeriod'),
                value_source=data_dict.get('valueSource'),
                value_tendency=data_dict.get('valueTendency'),
                value_state=data_dict.get('valueState'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class MeasurementListDataType:
    def __init__(
            self,
            measurement_data: list[MeasurementDataType] = None,
    ):
        super().__init__()
        
        self.measurement_data = measurement_data

        if not isinstance(self.measurement_data, list | NoneType):
            raise TypeError("measurement_data is not of type list[MeasurementDataType]")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.measurement_data is not None:
            msg_data.append({"measurementData": [d.get_data() for d in self.measurement_data]})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.measurement_data is not None:
            result_str += f"{sep}measurementData: {self.measurement_data}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                measurement_data=data_dict.get('measurementData'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class MeasurementListDataSelectorsType:
    def __init__(
            self,
            measurement_id: MeasurementIdType = None,
            value_type: FunctionType = None,
            timestamp_interval: TimestampIntervalType = None,
    ):
        super().__init__()
        
        self.measurement_id = measurement_id
        self.value_type = value_type
        self.timestamp_interval = timestamp_interval

        if not isinstance(self.measurement_id, MeasurementIdType | NoneType):
            raise TypeError("measurement_id is not of type MeasurementIdType")
        
        if not isinstance(self.value_type, FunctionType | NoneType):
            raise TypeError("value_type is not of type FunctionType")
        
        if not isinstance(self.timestamp_interval, TimestampIntervalType | NoneType):
            raise TypeError("timestamp_interval is not of type TimestampIntervalType")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.measurement_id is not None:
            msg_data.append({"measurementId": self.measurement_id.get_data()})
        if self.value_type is not None:
            msg_data.append({"valueType": self.value_type.get_data()})
        if self.timestamp_interval is not None:
            msg_data.append({"timestampInterval": self.timestamp_interval.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.measurement_id is not None:
            result_str += f"{sep}measurementId: {self.measurement_id}"
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
                measurement_id=data_dict.get('measurementId'),
                value_type=data_dict.get('valueType'),
                timestamp_interval=data_dict.get('timestampInterval'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class MeasurementDescriptionListDataType:
    def __init__(
            self,
            measurement_description_data: list[MeasurementDescriptionDataType] = None,
    ):
        super().__init__()
        
        self.measurement_description_data = measurement_description_data

        if not isinstance(self.measurement_description_data, list | NoneType):
            raise TypeError("measurement_description_data is not of type list[MeasurementDescriptionDataType]")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.measurement_description_data is not None:
            msg_data.append({"measurementDescriptionData": [d.get_data() for d in self.measurement_description_data]})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.measurement_description_data is not None:
            result_str += f"{sep}measurementDescriptionData: {self.measurement_description_data}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                measurement_description_data=data_dict.get('measurementDescriptionData'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class MeasurementDescriptionListDataSelectorsType:
    def __init__(
            self,
            measurement_id: MeasurementIdType = None,
            measurement_type: FunctionType = None,
            commodity_type: FunctionType = None,
            scope_type: FunctionType = None,
    ):
        super().__init__()
        
        self.measurement_id = measurement_id
        self.measurement_type = measurement_type
        self.commodity_type = commodity_type
        self.scope_type = scope_type

        if not isinstance(self.measurement_id, MeasurementIdType | NoneType):
            raise TypeError("measurement_id is not of type MeasurementIdType")
        
        if not isinstance(self.measurement_type, FunctionType | NoneType):
            raise TypeError("measurement_type is not of type FunctionType")
        
        if not isinstance(self.commodity_type, FunctionType | NoneType):
            raise TypeError("commodity_type is not of type FunctionType")
        
        if not isinstance(self.scope_type, FunctionType | NoneType):
            raise TypeError("scope_type is not of type FunctionType")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.measurement_id is not None:
            msg_data.append({"measurementId": self.measurement_id.get_data()})
        if self.measurement_type is not None:
            msg_data.append({"measurementType": self.measurement_type.get_data()})
        if self.commodity_type is not None:
            msg_data.append({"commodityType": self.commodity_type.get_data()})
        if self.scope_type is not None:
            msg_data.append({"scopeType": self.scope_type.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.measurement_id is not None:
            result_str += f"{sep}measurementId: {self.measurement_id}"
            sep = ", "
        if self.measurement_type is not None:
            result_str += f"{sep}measurementType: {self.measurement_type}"
            sep = ", "
        if self.commodity_type is not None:
            result_str += f"{sep}commodityType: {self.commodity_type}"
            sep = ", "
        if self.scope_type is not None:
            result_str += f"{sep}scopeType: {self.scope_type}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                measurement_id=data_dict.get('measurementId'),
                measurement_type=data_dict.get('measurementType'),
                commodity_type=data_dict.get('commodityType'),
                scope_type=data_dict.get('scopeType'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class MeasurementDescriptionDataElementsType:
    def __init__(
            self,
            measurement_id: ElementTagType = None,
            measurement_type: ElementTagType = None,
            commodity_type: ElementTagType = None,
            unit: ElementTagType = None,
            calibration_value: ScaledNumberElementsType = None,
            scope_type: ElementTagType = None,
            label: ElementTagType = None,
            description: ElementTagType = None,
    ):
        super().__init__()
        
        self.measurement_id = measurement_id
        self.measurement_type = measurement_type
        self.commodity_type = commodity_type
        self.unit = unit
        self.calibration_value = calibration_value
        self.scope_type = scope_type
        self.label = label
        self.description = description

        if not isinstance(self.measurement_id, ElementTagType | NoneType):
            raise TypeError("measurement_id is not of type ElementTagType")
        
        if not isinstance(self.measurement_type, ElementTagType | NoneType):
            raise TypeError("measurement_type is not of type ElementTagType")
        
        if not isinstance(self.commodity_type, ElementTagType | NoneType):
            raise TypeError("commodity_type is not of type ElementTagType")
        
        if not isinstance(self.unit, ElementTagType | NoneType):
            raise TypeError("unit is not of type ElementTagType")
        
        if not isinstance(self.calibration_value, ScaledNumberElementsType | NoneType):
            raise TypeError("calibration_value is not of type ScaledNumberElementsType")
        
        if not isinstance(self.scope_type, ElementTagType | NoneType):
            raise TypeError("scope_type is not of type ElementTagType")
        
        if not isinstance(self.label, ElementTagType | NoneType):
            raise TypeError("label is not of type ElementTagType")
        
        if not isinstance(self.description, ElementTagType | NoneType):
            raise TypeError("description is not of type ElementTagType")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.measurement_id is not None:
            msg_data.append({"measurementId": self.measurement_id.get_data()})
        if self.measurement_type is not None:
            msg_data.append({"measurementType": self.measurement_type.get_data()})
        if self.commodity_type is not None:
            msg_data.append({"commodityType": self.commodity_type.get_data()})
        if self.unit is not None:
            msg_data.append({"unit": self.unit.get_data()})
        if self.calibration_value is not None:
            msg_data.append({"calibrationValue": self.calibration_value.get_data()})
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
        if self.measurement_id is not None:
            result_str += f"{sep}measurementId: {self.measurement_id}"
            sep = ", "
        if self.measurement_type is not None:
            result_str += f"{sep}measurementType: {self.measurement_type}"
            sep = ", "
        if self.commodity_type is not None:
            result_str += f"{sep}commodityType: {self.commodity_type}"
            sep = ", "
        if self.unit is not None:
            result_str += f"{sep}unit: {self.unit}"
            sep = ", "
        if self.calibration_value is not None:
            result_str += f"{sep}calibrationValue: {self.calibration_value}"
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
                measurement_id=data_dict.get('measurementId'),
                measurement_type=data_dict.get('measurementType'),
                commodity_type=data_dict.get('commodityType'),
                unit=data_dict.get('unit'),
                calibration_value=data_dict.get('calibrationValue'),
                scope_type=data_dict.get('scopeType'),
                label=data_dict.get('label'),
                description=data_dict.get('description'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class MeasurementDataElementsType:
    def __init__(
            self,
            measurement_id: ElementTagType = None,
            value_type: ElementTagType = None,
            timestamp: ElementTagType = None,
            value: ScaledNumberElementsType = None,
            evaluation_period: TimePeriodElementsType = None,
            value_source: ElementTagType = None,
            value_tendency: ElementTagType = None,
            value_state: ElementTagType = None,
    ):
        super().__init__()
        
        self.measurement_id = measurement_id
        self.value_type = value_type
        self.timestamp = timestamp
        self.value = value
        self.evaluation_period = evaluation_period
        self.value_source = value_source
        self.value_tendency = value_tendency
        self.value_state = value_state

        if not isinstance(self.measurement_id, ElementTagType | NoneType):
            raise TypeError("measurement_id is not of type ElementTagType")
        
        if not isinstance(self.value_type, ElementTagType | NoneType):
            raise TypeError("value_type is not of type ElementTagType")
        
        if not isinstance(self.timestamp, ElementTagType | NoneType):
            raise TypeError("timestamp is not of type ElementTagType")
        
        if not isinstance(self.value, ScaledNumberElementsType | NoneType):
            raise TypeError("value is not of type ScaledNumberElementsType")
        
        if not isinstance(self.evaluation_period, TimePeriodElementsType | NoneType):
            raise TypeError("evaluation_period is not of type TimePeriodElementsType")
        
        if not isinstance(self.value_source, ElementTagType | NoneType):
            raise TypeError("value_source is not of type ElementTagType")
        
        if not isinstance(self.value_tendency, ElementTagType | NoneType):
            raise TypeError("value_tendency is not of type ElementTagType")
        
        if not isinstance(self.value_state, ElementTagType | NoneType):
            raise TypeError("value_state is not of type ElementTagType")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.measurement_id is not None:
            msg_data.append({"measurementId": self.measurement_id.get_data()})
        if self.value_type is not None:
            msg_data.append({"valueType": self.value_type.get_data()})
        if self.timestamp is not None:
            msg_data.append({"timestamp": self.timestamp.get_data()})
        if self.value is not None:
            msg_data.append({"value": self.value.get_data()})
        if self.evaluation_period is not None:
            msg_data.append({"evaluationPeriod": self.evaluation_period.get_data()})
        if self.value_source is not None:
            msg_data.append({"valueSource": self.value_source.get_data()})
        if self.value_tendency is not None:
            msg_data.append({"valueTendency": self.value_tendency.get_data()})
        if self.value_state is not None:
            msg_data.append({"valueState": self.value_state.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.measurement_id is not None:
            result_str += f"{sep}measurementId: {self.measurement_id}"
            sep = ", "
        if self.value_type is not None:
            result_str += f"{sep}valueType: {self.value_type}"
            sep = ", "
        if self.timestamp is not None:
            result_str += f"{sep}timestamp: {self.timestamp}"
            sep = ", "
        if self.value is not None:
            result_str += f"{sep}value: {self.value}"
            sep = ", "
        if self.evaluation_period is not None:
            result_str += f"{sep}evaluationPeriod: {self.evaluation_period}"
            sep = ", "
        if self.value_source is not None:
            result_str += f"{sep}valueSource: {self.value_source}"
            sep = ", "
        if self.value_tendency is not None:
            result_str += f"{sep}valueTendency: {self.value_tendency}"
            sep = ", "
        if self.value_state is not None:
            result_str += f"{sep}valueState: {self.value_state}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                measurement_id=data_dict.get('measurementId'),
                value_type=data_dict.get('valueType'),
                timestamp=data_dict.get('timestamp'),
                value=data_dict.get('value'),
                evaluation_period=data_dict.get('evaluationPeriod'),
                value_source=data_dict.get('valueSource'),
                value_tendency=data_dict.get('valueTendency'),
                value_state=data_dict.get('valueState'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class MeasurementConstraintsListDataType:
    def __init__(
            self,
            measurement_constraints_data: list[MeasurementConstraintsDataType] = None,
    ):
        super().__init__()
        
        self.measurement_constraints_data = measurement_constraints_data

        if not isinstance(self.measurement_constraints_data, list | NoneType):
            raise TypeError("measurement_constraints_data is not of type list[MeasurementConstraintsDataType]")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.measurement_constraints_data is not None:
            msg_data.append({"measurementConstraintsData": [d.get_data() for d in self.measurement_constraints_data]})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.measurement_constraints_data is not None:
            result_str += f"{sep}measurementConstraintsData: {self.measurement_constraints_data}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                measurement_constraints_data=data_dict.get('measurementConstraintsData'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class MeasurementConstraintsListDataSelectorsType:
    def __init__(
            self,
            measurement_id: MeasurementIdType = None,
    ):
        super().__init__()
        
        self.measurement_id = measurement_id

        if not isinstance(self.measurement_id, MeasurementIdType | NoneType):
            raise TypeError("measurement_id is not of type MeasurementIdType")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.measurement_id is not None:
            msg_data.append({"measurementId": self.measurement_id.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.measurement_id is not None:
            result_str += f"{sep}measurementId: {self.measurement_id}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                measurement_id=data_dict.get('measurementId'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class MeasurementConstraintsDataElementsType:
    def __init__(
            self,
            measurement_id: ElementTagType = None,
            value_range_min: ScaledNumberElementsType = None,
            value_range_max: ScaledNumberElementsType = None,
            value_step_size: ScaledNumberElementsType = None,
    ):
        super().__init__()
        
        self.measurement_id = measurement_id
        self.value_range_min = value_range_min
        self.value_range_max = value_range_max
        self.value_step_size = value_step_size

        if not isinstance(self.measurement_id, ElementTagType | NoneType):
            raise TypeError("measurement_id is not of type ElementTagType")
        
        if not isinstance(self.value_range_min, ScaledNumberElementsType | NoneType):
            raise TypeError("value_range_min is not of type ScaledNumberElementsType")
        
        if not isinstance(self.value_range_max, ScaledNumberElementsType | NoneType):
            raise TypeError("value_range_max is not of type ScaledNumberElementsType")
        
        if not isinstance(self.value_step_size, ScaledNumberElementsType | NoneType):
            raise TypeError("value_step_size is not of type ScaledNumberElementsType")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.measurement_id is not None:
            msg_data.append({"measurementId": self.measurement_id.get_data()})
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
        if self.measurement_id is not None:
            result_str += f"{sep}measurementId: {self.measurement_id}"
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
                measurement_id=data_dict.get('measurementId'),
                value_range_min=data_dict.get('valueRangeMin'),
                value_range_max=data_dict.get('valueRangeMax'),
                value_step_size=data_dict.get('valueStepSize'),
            )
        elif data:
            return cls(data)
        else:
            return cls()



