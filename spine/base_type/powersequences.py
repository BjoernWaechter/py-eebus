# Jinja Template message_type.py.jinja2
from spine.base_type.commondatatypes import ElementTagType
from spine.base_type.commondatatypes import ScaledNumberElementsType
from spine.base_type.commondatatypes import ScaledNumberType
from spine.base_type.commondatatypes import TimePeriodElementsType
from spine.base_type.commondatatypes import TimePeriodType
from spine.base_type.commondatatypes import TimestampIntervalType
from spine.simple_type.commondatatypes import DescriptionType
from spine.simple_type.powersequences import AlternativesIdType
from spine.simple_type.powersequences import PowerSequenceIdType
from spine.simple_type.powersequences import PowerTimeSlotNumberType
from spine.union_type.commondatatypes import AbsoluteOrRelativeTimeType
from spine.union_type.commondatatypes import CurrencyType
from spine.union_type.commondatatypes import EnergyDirectionType
from spine.union_type.commondatatypes import UnitOfMeasurementType
from spine.union_type.measurement import MeasurementValueSourceType
from spine.union_type.powersequences import PowerSequenceScopeType
from spine.union_type.powersequences import PowerSequenceStateType
from spine.union_type.powersequences import PowerTimeSlotValueTypeType
from types import NoneType
from spine import array_2_dict


class PowerTimeSlotValueDataType: # EEBus_SPINE_TS_PowerSequences.xsd:ns_p:PowerTimeSlotValueDataType -> ComplexType
    def __init__(
            self,
            sequence_id: PowerSequenceIdType = None,
            slot_number: PowerTimeSlotNumberType = None,
            value_type: PowerTimeSlotValueTypeType = None,
            value: ScaledNumberType = None,
    ):
        super().__init__()
        
        self.sequence_id = sequence_id
        self.slot_number = slot_number
        self.value_type = value_type
        self.value = value

        if not isinstance(self.sequence_id, PowerSequenceIdType | NoneType):
            raise TypeError("sequence_id is not of type PowerSequenceIdType")
        
        if not isinstance(self.slot_number, PowerTimeSlotNumberType | NoneType):
            raise TypeError("slot_number is not of type PowerTimeSlotNumberType")
        
        if not isinstance(self.value_type, PowerTimeSlotValueTypeType | NoneType):
            raise TypeError("value_type is not of type PowerTimeSlotValueTypeType")
        
        if not isinstance(self.value, ScaledNumberType | NoneType):
            raise TypeError("value is not of type ScaledNumberType")
        
    def get_data(self):

        msg_data = []
        
        if self.sequence_id is not None:
            msg_data.append({"sequenceId": self.sequence_id.get_data()})
        if self.slot_number is not None:
            msg_data.append({"slotNumber": self.slot_number.get_data()})
        if self.value_type is not None:
            msg_data.append({"valueType": self.value_type.get_data()})
        if self.value is not None:
            msg_data.append({"value": self.value.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.sequence_id is not None:
            result_str += f"{sep}sequenceId: {self.sequence_id}"
            sep = ", "
        if self.slot_number is not None:
            result_str += f"{sep}slotNumber: {self.slot_number}"
            sep = ", "
        if self.value_type is not None:
            result_str += f"{sep}valueType: {self.value_type}"
            sep = ", "
        if self.value is not None:
            result_str += f"{sep}value: {self.value}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                sequence_id=data_dict.get('sequenceId'),
                slot_number=data_dict.get('slotNumber'),
                value_type=data_dict.get('valueType'),
                value=data_dict.get('value'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class PowerTimeSlotScheduleDataType: # EEBus_SPINE_TS_PowerSequences.xsd:ns_p:PowerTimeSlotScheduleDataType -> ComplexType
    def __init__(
            self,
            sequence_id: PowerSequenceIdType = None,
            slot_number: PowerTimeSlotNumberType = None,
            time_period: TimePeriodType = None,
            default_duration: str = None,
            duration_uncertainty: str = None,
            slot_activated: bool = None,
            description: DescriptionType = None,
    ):
        super().__init__()
        
        self.sequence_id = sequence_id
        self.slot_number = slot_number
        self.time_period = time_period
        self.default_duration = default_duration
        self.duration_uncertainty = duration_uncertainty
        self.slot_activated = slot_activated
        self.description = description

        if not isinstance(self.sequence_id, PowerSequenceIdType | NoneType):
            raise TypeError("sequence_id is not of type PowerSequenceIdType")
        
        if not isinstance(self.slot_number, PowerTimeSlotNumberType | NoneType):
            raise TypeError("slot_number is not of type PowerTimeSlotNumberType")
        
        if not isinstance(self.time_period, TimePeriodType | NoneType):
            raise TypeError("time_period is not of type TimePeriodType")
        
        if not isinstance(self.default_duration, str | NoneType):
            raise TypeError("default_duration is not of type str")
        
        if not isinstance(self.duration_uncertainty, str | NoneType):
            raise TypeError("duration_uncertainty is not of type str")
        
        if not isinstance(self.slot_activated, bool | NoneType):
            raise TypeError("slot_activated is not of type bool")
        
        if not isinstance(self.description, DescriptionType | NoneType):
            raise TypeError("description is not of type DescriptionType")
        
    def get_data(self):

        msg_data = []
        
        if self.sequence_id is not None:
            msg_data.append({"sequenceId": self.sequence_id.get_data()})
        if self.slot_number is not None:
            msg_data.append({"slotNumber": self.slot_number.get_data()})
        if self.time_period is not None:
            msg_data.append({"timePeriod": self.time_period.get_data()})
        if self.default_duration is not None:
            msg_data.append({"defaultDuration": self.default_duration})
        if self.duration_uncertainty is not None:
            msg_data.append({"durationUncertainty": self.duration_uncertainty})
        if self.slot_activated is not None:
            msg_data.append({"slotActivated": self.slot_activated})
        if self.description is not None:
            msg_data.append({"description": self.description.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.sequence_id is not None:
            result_str += f"{sep}sequenceId: {self.sequence_id}"
            sep = ", "
        if self.slot_number is not None:
            result_str += f"{sep}slotNumber: {self.slot_number}"
            sep = ", "
        if self.time_period is not None:
            result_str += f"{sep}timePeriod: {self.time_period}"
            sep = ", "
        if self.default_duration is not None:
            result_str += f"{sep}defaultDuration: {self.default_duration}"
            sep = ", "
        if self.duration_uncertainty is not None:
            result_str += f"{sep}durationUncertainty: {self.duration_uncertainty}"
            sep = ", "
        if self.slot_activated is not None:
            result_str += f"{sep}slotActivated: {self.slot_activated}"
            sep = ", "
        if self.description is not None:
            result_str += f"{sep}description: {self.description}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                sequence_id=data_dict.get('sequenceId'),
                slot_number=data_dict.get('slotNumber'),
                time_period=data_dict.get('timePeriod'),
                default_duration=data_dict.get('defaultDuration'),
                duration_uncertainty=data_dict.get('durationUncertainty'),
                slot_activated=data_dict.get('slotActivated'),
                description=data_dict.get('description'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class PowerTimeSlotScheduleConstraintsDataType: # EEBus_SPINE_TS_PowerSequences.xsd:ns_p:PowerTimeSlotScheduleConstraintsDataType -> ComplexType
    def __init__(
            self,
            sequence_id: PowerSequenceIdType = None,
            slot_number: PowerTimeSlotNumberType = None,
            earliest_start_time: AbsoluteOrRelativeTimeType = None,
            latest_end_time: AbsoluteOrRelativeTimeType = None,
            min_duration: str = None,
            max_duration: str = None,
            optional_slot: bool = None,
    ):
        super().__init__()
        
        self.sequence_id = sequence_id
        self.slot_number = slot_number
        self.earliest_start_time = earliest_start_time
        self.latest_end_time = latest_end_time
        self.min_duration = min_duration
        self.max_duration = max_duration
        self.optional_slot = optional_slot

        if not isinstance(self.sequence_id, PowerSequenceIdType | NoneType):
            raise TypeError("sequence_id is not of type PowerSequenceIdType")
        
        if not isinstance(self.slot_number, PowerTimeSlotNumberType | NoneType):
            raise TypeError("slot_number is not of type PowerTimeSlotNumberType")
        
        if not isinstance(self.earliest_start_time, AbsoluteOrRelativeTimeType | NoneType):
            raise TypeError("earliest_start_time is not of type AbsoluteOrRelativeTimeType")
        
        if not isinstance(self.latest_end_time, AbsoluteOrRelativeTimeType | NoneType):
            raise TypeError("latest_end_time is not of type AbsoluteOrRelativeTimeType")
        
        if not isinstance(self.min_duration, str | NoneType):
            raise TypeError("min_duration is not of type str")
        
        if not isinstance(self.max_duration, str | NoneType):
            raise TypeError("max_duration is not of type str")
        
        if not isinstance(self.optional_slot, bool | NoneType):
            raise TypeError("optional_slot is not of type bool")
        
    def get_data(self):

        msg_data = []
        
        if self.sequence_id is not None:
            msg_data.append({"sequenceId": self.sequence_id.get_data()})
        if self.slot_number is not None:
            msg_data.append({"slotNumber": self.slot_number.get_data()})
        if self.earliest_start_time is not None:
            msg_data.append({"earliestStartTime": self.earliest_start_time.get_data()})
        if self.latest_end_time is not None:
            msg_data.append({"latestEndTime": self.latest_end_time.get_data()})
        if self.min_duration is not None:
            msg_data.append({"minDuration": self.min_duration})
        if self.max_duration is not None:
            msg_data.append({"maxDuration": self.max_duration})
        if self.optional_slot is not None:
            msg_data.append({"optionalSlot": self.optional_slot})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.sequence_id is not None:
            result_str += f"{sep}sequenceId: {self.sequence_id}"
            sep = ", "
        if self.slot_number is not None:
            result_str += f"{sep}slotNumber: {self.slot_number}"
            sep = ", "
        if self.earliest_start_time is not None:
            result_str += f"{sep}earliestStartTime: {self.earliest_start_time}"
            sep = ", "
        if self.latest_end_time is not None:
            result_str += f"{sep}latestEndTime: {self.latest_end_time}"
            sep = ", "
        if self.min_duration is not None:
            result_str += f"{sep}minDuration: {self.min_duration}"
            sep = ", "
        if self.max_duration is not None:
            result_str += f"{sep}maxDuration: {self.max_duration}"
            sep = ", "
        if self.optional_slot is not None:
            result_str += f"{sep}optionalSlot: {self.optional_slot}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                sequence_id=data_dict.get('sequenceId'),
                slot_number=data_dict.get('slotNumber'),
                earliest_start_time=data_dict.get('earliestStartTime'),
                latest_end_time=data_dict.get('latestEndTime'),
                min_duration=data_dict.get('minDuration'),
                max_duration=data_dict.get('maxDuration'),
                optional_slot=data_dict.get('optionalSlot'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class PowerSequenceStateDataType: # EEBus_SPINE_TS_PowerSequences.xsd:ns_p:PowerSequenceStateDataType -> ComplexType
    def __init__(
            self,
            sequence_id: PowerSequenceIdType = None,
            state: PowerSequenceStateType = None,
            active_slot_number: PowerTimeSlotNumberType = None,
            elapsed_slot_time: str = None,
            remaining_slot_time: str = None,
            sequence_remote_controllable: bool = None,
            active_repetition_number: int = None,
            remaining_pause_time: str = None,
    ):
        super().__init__()
        
        self.sequence_id = sequence_id
        self.state = state
        self.active_slot_number = active_slot_number
        self.elapsed_slot_time = elapsed_slot_time
        self.remaining_slot_time = remaining_slot_time
        self.sequence_remote_controllable = sequence_remote_controllable
        self.active_repetition_number = active_repetition_number
        self.remaining_pause_time = remaining_pause_time

        if not isinstance(self.sequence_id, PowerSequenceIdType | NoneType):
            raise TypeError("sequence_id is not of type PowerSequenceIdType")
        
        if not isinstance(self.state, PowerSequenceStateType | NoneType):
            raise TypeError("state is not of type PowerSequenceStateType")
        
        if not isinstance(self.active_slot_number, PowerTimeSlotNumberType | NoneType):
            raise TypeError("active_slot_number is not of type PowerTimeSlotNumberType")
        
        if not isinstance(self.elapsed_slot_time, str | NoneType):
            raise TypeError("elapsed_slot_time is not of type str")
        
        if not isinstance(self.remaining_slot_time, str | NoneType):
            raise TypeError("remaining_slot_time is not of type str")
        
        if not isinstance(self.sequence_remote_controllable, bool | NoneType):
            raise TypeError("sequence_remote_controllable is not of type bool")
        
        if not isinstance(self.active_repetition_number, int | NoneType):
            raise TypeError("active_repetition_number is not of type int")
        
        if not isinstance(self.remaining_pause_time, str | NoneType):
            raise TypeError("remaining_pause_time is not of type str")
        
    def get_data(self):

        msg_data = []
        
        if self.sequence_id is not None:
            msg_data.append({"sequenceId": self.sequence_id.get_data()})
        if self.state is not None:
            msg_data.append({"state": self.state.get_data()})
        if self.active_slot_number is not None:
            msg_data.append({"activeSlotNumber": self.active_slot_number.get_data()})
        if self.elapsed_slot_time is not None:
            msg_data.append({"elapsedSlotTime": self.elapsed_slot_time})
        if self.remaining_slot_time is not None:
            msg_data.append({"remainingSlotTime": self.remaining_slot_time})
        if self.sequence_remote_controllable is not None:
            msg_data.append({"sequenceRemoteControllable": self.sequence_remote_controllable})
        if self.active_repetition_number is not None:
            msg_data.append({"activeRepetitionNumber": self.active_repetition_number})
        if self.remaining_pause_time is not None:
            msg_data.append({"remainingPauseTime": self.remaining_pause_time})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.sequence_id is not None:
            result_str += f"{sep}sequenceId: {self.sequence_id}"
            sep = ", "
        if self.state is not None:
            result_str += f"{sep}state: {self.state}"
            sep = ", "
        if self.active_slot_number is not None:
            result_str += f"{sep}activeSlotNumber: {self.active_slot_number}"
            sep = ", "
        if self.elapsed_slot_time is not None:
            result_str += f"{sep}elapsedSlotTime: {self.elapsed_slot_time}"
            sep = ", "
        if self.remaining_slot_time is not None:
            result_str += f"{sep}remainingSlotTime: {self.remaining_slot_time}"
            sep = ", "
        if self.sequence_remote_controllable is not None:
            result_str += f"{sep}sequenceRemoteControllable: {self.sequence_remote_controllable}"
            sep = ", "
        if self.active_repetition_number is not None:
            result_str += f"{sep}activeRepetitionNumber: {self.active_repetition_number}"
            sep = ", "
        if self.remaining_pause_time is not None:
            result_str += f"{sep}remainingPauseTime: {self.remaining_pause_time}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                sequence_id=data_dict.get('sequenceId'),
                state=data_dict.get('state'),
                active_slot_number=data_dict.get('activeSlotNumber'),
                elapsed_slot_time=data_dict.get('elapsedSlotTime'),
                remaining_slot_time=data_dict.get('remainingSlotTime'),
                sequence_remote_controllable=data_dict.get('sequenceRemoteControllable'),
                active_repetition_number=data_dict.get('activeRepetitionNumber'),
                remaining_pause_time=data_dict.get('remainingPauseTime'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class PowerSequenceSchedulePreferenceDataType: # EEBus_SPINE_TS_PowerSequences.xsd:ns_p:PowerSequenceSchedulePreferenceDataType -> ComplexType
    def __init__(
            self,
            sequence_id: PowerSequenceIdType = None,
            greenest: bool = None,
            cheapest: bool = None,
    ):
        super().__init__()
        
        self.sequence_id = sequence_id
        self.greenest = greenest
        self.cheapest = cheapest

        if not isinstance(self.sequence_id, PowerSequenceIdType | NoneType):
            raise TypeError("sequence_id is not of type PowerSequenceIdType")
        
        if not isinstance(self.greenest, bool | NoneType):
            raise TypeError("greenest is not of type bool")
        
        if not isinstance(self.cheapest, bool | NoneType):
            raise TypeError("cheapest is not of type bool")
        
    def get_data(self):

        msg_data = []
        
        if self.sequence_id is not None:
            msg_data.append({"sequenceId": self.sequence_id.get_data()})
        if self.greenest is not None:
            msg_data.append({"greenest": self.greenest})
        if self.cheapest is not None:
            msg_data.append({"cheapest": self.cheapest})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.sequence_id is not None:
            result_str += f"{sep}sequenceId: {self.sequence_id}"
            sep = ", "
        if self.greenest is not None:
            result_str += f"{sep}greenest: {self.greenest}"
            sep = ", "
        if self.cheapest is not None:
            result_str += f"{sep}cheapest: {self.cheapest}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                sequence_id=data_dict.get('sequenceId'),
                greenest=data_dict.get('greenest'),
                cheapest=data_dict.get('cheapest'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class PowerSequenceScheduleDataType: # EEBus_SPINE_TS_PowerSequences.xsd:ns_p:PowerSequenceScheduleDataType -> ComplexType
    def __init__(
            self,
            sequence_id: PowerSequenceIdType = None,
            start_time: AbsoluteOrRelativeTimeType = None,
            end_time: AbsoluteOrRelativeTimeType = None,
    ):
        super().__init__()
        
        self.sequence_id = sequence_id
        self.start_time = start_time
        self.end_time = end_time

        if not isinstance(self.sequence_id, PowerSequenceIdType | NoneType):
            raise TypeError("sequence_id is not of type PowerSequenceIdType")
        
        if not isinstance(self.start_time, AbsoluteOrRelativeTimeType | NoneType):
            raise TypeError("start_time is not of type AbsoluteOrRelativeTimeType")
        
        if not isinstance(self.end_time, AbsoluteOrRelativeTimeType | NoneType):
            raise TypeError("end_time is not of type AbsoluteOrRelativeTimeType")
        
    def get_data(self):

        msg_data = []
        
        if self.sequence_id is not None:
            msg_data.append({"sequenceId": self.sequence_id.get_data()})
        if self.start_time is not None:
            msg_data.append({"startTime": self.start_time.get_data()})
        if self.end_time is not None:
            msg_data.append({"endTime": self.end_time.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.sequence_id is not None:
            result_str += f"{sep}sequenceId: {self.sequence_id}"
            sep = ", "
        if self.start_time is not None:
            result_str += f"{sep}startTime: {self.start_time}"
            sep = ", "
        if self.end_time is not None:
            result_str += f"{sep}endTime: {self.end_time}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                sequence_id=data_dict.get('sequenceId'),
                start_time=data_dict.get('startTime'),
                end_time=data_dict.get('endTime'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class PowerSequenceScheduleConstraintsDataType: # EEBus_SPINE_TS_PowerSequences.xsd:ns_p:PowerSequenceScheduleConstraintsDataType -> ComplexType
    def __init__(
            self,
            sequence_id: PowerSequenceIdType = None,
            earliest_start_time: AbsoluteOrRelativeTimeType = None,
            latest_start_time: AbsoluteOrRelativeTimeType = None,
            earliest_end_time: AbsoluteOrRelativeTimeType = None,
            latest_end_time: AbsoluteOrRelativeTimeType = None,
            optional_sequence: bool = None,
    ):
        super().__init__()
        
        self.sequence_id = sequence_id
        self.earliest_start_time = earliest_start_time
        self.latest_start_time = latest_start_time
        self.earliest_end_time = earliest_end_time
        self.latest_end_time = latest_end_time
        self.optional_sequence = optional_sequence

        if not isinstance(self.sequence_id, PowerSequenceIdType | NoneType):
            raise TypeError("sequence_id is not of type PowerSequenceIdType")
        
        if not isinstance(self.earliest_start_time, AbsoluteOrRelativeTimeType | NoneType):
            raise TypeError("earliest_start_time is not of type AbsoluteOrRelativeTimeType")
        
        if not isinstance(self.latest_start_time, AbsoluteOrRelativeTimeType | NoneType):
            raise TypeError("latest_start_time is not of type AbsoluteOrRelativeTimeType")
        
        if not isinstance(self.earliest_end_time, AbsoluteOrRelativeTimeType | NoneType):
            raise TypeError("earliest_end_time is not of type AbsoluteOrRelativeTimeType")
        
        if not isinstance(self.latest_end_time, AbsoluteOrRelativeTimeType | NoneType):
            raise TypeError("latest_end_time is not of type AbsoluteOrRelativeTimeType")
        
        if not isinstance(self.optional_sequence, bool | NoneType):
            raise TypeError("optional_sequence is not of type bool")
        
    def get_data(self):

        msg_data = []
        
        if self.sequence_id is not None:
            msg_data.append({"sequenceId": self.sequence_id.get_data()})
        if self.earliest_start_time is not None:
            msg_data.append({"earliestStartTime": self.earliest_start_time.get_data()})
        if self.latest_start_time is not None:
            msg_data.append({"latestStartTime": self.latest_start_time.get_data()})
        if self.earliest_end_time is not None:
            msg_data.append({"earliestEndTime": self.earliest_end_time.get_data()})
        if self.latest_end_time is not None:
            msg_data.append({"latestEndTime": self.latest_end_time.get_data()})
        if self.optional_sequence is not None:
            msg_data.append({"optionalSequence": self.optional_sequence})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.sequence_id is not None:
            result_str += f"{sep}sequenceId: {self.sequence_id}"
            sep = ", "
        if self.earliest_start_time is not None:
            result_str += f"{sep}earliestStartTime: {self.earliest_start_time}"
            sep = ", "
        if self.latest_start_time is not None:
            result_str += f"{sep}latestStartTime: {self.latest_start_time}"
            sep = ", "
        if self.earliest_end_time is not None:
            result_str += f"{sep}earliestEndTime: {self.earliest_end_time}"
            sep = ", "
        if self.latest_end_time is not None:
            result_str += f"{sep}latestEndTime: {self.latest_end_time}"
            sep = ", "
        if self.optional_sequence is not None:
            result_str += f"{sep}optionalSequence: {self.optional_sequence}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                sequence_id=data_dict.get('sequenceId'),
                earliest_start_time=data_dict.get('earliestStartTime'),
                latest_start_time=data_dict.get('latestStartTime'),
                earliest_end_time=data_dict.get('earliestEndTime'),
                latest_end_time=data_dict.get('latestEndTime'),
                optional_sequence=data_dict.get('optionalSequence'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class PowerSequencePriceDataType: # EEBus_SPINE_TS_PowerSequences.xsd:ns_p:PowerSequencePriceDataType -> ComplexType
    def __init__(
            self,
            sequence_id: PowerSequenceIdType = None,
            potential_start_time: AbsoluteOrRelativeTimeType = None,
            price: ScaledNumberType = None,
            currency: CurrencyType = None,
    ):
        super().__init__()
        
        self.sequence_id = sequence_id
        self.potential_start_time = potential_start_time
        self.price = price
        self.currency = currency

        if not isinstance(self.sequence_id, PowerSequenceIdType | NoneType):
            raise TypeError("sequence_id is not of type PowerSequenceIdType")
        
        if not isinstance(self.potential_start_time, AbsoluteOrRelativeTimeType | NoneType):
            raise TypeError("potential_start_time is not of type AbsoluteOrRelativeTimeType")
        
        if not isinstance(self.price, ScaledNumberType | NoneType):
            raise TypeError("price is not of type ScaledNumberType")
        
        if not isinstance(self.currency, CurrencyType | NoneType):
            raise TypeError("currency is not of type CurrencyType")
        
    def get_data(self):

        msg_data = []
        
        if self.sequence_id is not None:
            msg_data.append({"sequenceId": self.sequence_id.get_data()})
        if self.potential_start_time is not None:
            msg_data.append({"potentialStartTime": self.potential_start_time.get_data()})
        if self.price is not None:
            msg_data.append({"price": self.price.get_data()})
        if self.currency is not None:
            msg_data.append({"currency": self.currency.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.sequence_id is not None:
            result_str += f"{sep}sequenceId: {self.sequence_id}"
            sep = ", "
        if self.potential_start_time is not None:
            result_str += f"{sep}potentialStartTime: {self.potential_start_time}"
            sep = ", "
        if self.price is not None:
            result_str += f"{sep}price: {self.price}"
            sep = ", "
        if self.currency is not None:
            result_str += f"{sep}currency: {self.currency}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                sequence_id=data_dict.get('sequenceId'),
                potential_start_time=data_dict.get('potentialStartTime'),
                price=data_dict.get('price'),
                currency=data_dict.get('currency'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class PowerSequenceDescriptionDataType: # EEBus_SPINE_TS_PowerSequences.xsd:ns_p:PowerSequenceDescriptionDataType -> ComplexType
    def __init__(
            self,
            sequence_id: PowerSequenceIdType = None,
            description: DescriptionType = None,
            positive_energy_direction: EnergyDirectionType = None,
            power_unit: UnitOfMeasurementType = None,
            energy_unit: UnitOfMeasurementType = None,
            value_source: MeasurementValueSourceType = None,
            scope: PowerSequenceScopeType = None,
            task_identifier: int = None,
            repetitions_total: int = None,
    ):
        super().__init__()
        
        self.sequence_id = sequence_id
        self.description = description
        self.positive_energy_direction = positive_energy_direction
        self.power_unit = power_unit
        self.energy_unit = energy_unit
        self.value_source = value_source
        self.scope = scope
        self.task_identifier = task_identifier
        self.repetitions_total = repetitions_total

        if not isinstance(self.sequence_id, PowerSequenceIdType | NoneType):
            raise TypeError("sequence_id is not of type PowerSequenceIdType")
        
        if not isinstance(self.description, DescriptionType | NoneType):
            raise TypeError("description is not of type DescriptionType")
        
        if not isinstance(self.positive_energy_direction, EnergyDirectionType | NoneType):
            raise TypeError("positive_energy_direction is not of type EnergyDirectionType")
        
        if not isinstance(self.power_unit, UnitOfMeasurementType | NoneType):
            raise TypeError("power_unit is not of type UnitOfMeasurementType")
        
        if not isinstance(self.energy_unit, UnitOfMeasurementType | NoneType):
            raise TypeError("energy_unit is not of type UnitOfMeasurementType")
        
        if not isinstance(self.value_source, MeasurementValueSourceType | NoneType):
            raise TypeError("value_source is not of type MeasurementValueSourceType")
        
        if not isinstance(self.scope, PowerSequenceScopeType | NoneType):
            raise TypeError("scope is not of type PowerSequenceScopeType")
        
        if not isinstance(self.task_identifier, int | NoneType):
            raise TypeError("task_identifier is not of type int")
        
        if not isinstance(self.repetitions_total, int | NoneType):
            raise TypeError("repetitions_total is not of type int")
        
    def get_data(self):

        msg_data = []
        
        if self.sequence_id is not None:
            msg_data.append({"sequenceId": self.sequence_id.get_data()})
        if self.description is not None:
            msg_data.append({"description": self.description.get_data()})
        if self.positive_energy_direction is not None:
            msg_data.append({"positiveEnergyDirection": self.positive_energy_direction.get_data()})
        if self.power_unit is not None:
            msg_data.append({"powerUnit": self.power_unit.get_data()})
        if self.energy_unit is not None:
            msg_data.append({"energyUnit": self.energy_unit.get_data()})
        if self.value_source is not None:
            msg_data.append({"valueSource": self.value_source.get_data()})
        if self.scope is not None:
            msg_data.append({"scope": self.scope.get_data()})
        if self.task_identifier is not None:
            msg_data.append({"taskIdentifier": self.task_identifier})
        if self.repetitions_total is not None:
            msg_data.append({"repetitionsTotal": self.repetitions_total})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.sequence_id is not None:
            result_str += f"{sep}sequenceId: {self.sequence_id}"
            sep = ", "
        if self.description is not None:
            result_str += f"{sep}description: {self.description}"
            sep = ", "
        if self.positive_energy_direction is not None:
            result_str += f"{sep}positiveEnergyDirection: {self.positive_energy_direction}"
            sep = ", "
        if self.power_unit is not None:
            result_str += f"{sep}powerUnit: {self.power_unit}"
            sep = ", "
        if self.energy_unit is not None:
            result_str += f"{sep}energyUnit: {self.energy_unit}"
            sep = ", "
        if self.value_source is not None:
            result_str += f"{sep}valueSource: {self.value_source}"
            sep = ", "
        if self.scope is not None:
            result_str += f"{sep}scope: {self.scope}"
            sep = ", "
        if self.task_identifier is not None:
            result_str += f"{sep}taskIdentifier: {self.task_identifier}"
            sep = ", "
        if self.repetitions_total is not None:
            result_str += f"{sep}repetitionsTotal: {self.repetitions_total}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                sequence_id=data_dict.get('sequenceId'),
                description=data_dict.get('description'),
                positive_energy_direction=data_dict.get('positiveEnergyDirection'),
                power_unit=data_dict.get('powerUnit'),
                energy_unit=data_dict.get('energyUnit'),
                value_source=data_dict.get('valueSource'),
                scope=data_dict.get('scope'),
                task_identifier=data_dict.get('taskIdentifier'),
                repetitions_total=data_dict.get('repetitionsTotal'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class PowerSequenceAlternativesRelationDataType: # EEBus_SPINE_TS_PowerSequences.xsd:ns_p:PowerSequenceAlternativesRelationDataType -> ComplexType
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
        
    def get_data(self):

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


class PowerTimeSlotValueListDataType: # EEBus_SPINE_TS_PowerSequences.xsd:ns_p:PowerTimeSlotValueListDataType -> ComplexType
    def __init__(
            self,
            power_time_slot_value_data: list[PowerTimeSlotValueDataType] = None,
    ):
        super().__init__()
        
        self.power_time_slot_value_data = power_time_slot_value_data

        if not isinstance(self.power_time_slot_value_data, list | NoneType):
            raise TypeError("power_time_slot_value_data is not of type list[PowerTimeSlotValueDataType]")
        
    def get_data(self):

        msg_data = []
        
        if self.power_time_slot_value_data is not None:
            msg_data.append({"powerTimeSlotValueData": [d.get_data() for d in self.power_time_slot_value_data]})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.power_time_slot_value_data is not None:
            result_str += f"{sep}powerTimeSlotValueData: {self.power_time_slot_value_data}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                power_time_slot_value_data=data_dict.get('powerTimeSlotValueData'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class PowerTimeSlotScheduleListDataType: # EEBus_SPINE_TS_PowerSequences.xsd:ns_p:PowerTimeSlotScheduleListDataType -> ComplexType
    def __init__(
            self,
            power_time_slot_schedule_data: list[PowerTimeSlotScheduleDataType] = None,
    ):
        super().__init__()
        
        self.power_time_slot_schedule_data = power_time_slot_schedule_data

        if not isinstance(self.power_time_slot_schedule_data, list | NoneType):
            raise TypeError("power_time_slot_schedule_data is not of type list[PowerTimeSlotScheduleDataType]")
        
    def get_data(self):

        msg_data = []
        
        if self.power_time_slot_schedule_data is not None:
            msg_data.append({"powerTimeSlotScheduleData": [d.get_data() for d in self.power_time_slot_schedule_data]})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.power_time_slot_schedule_data is not None:
            result_str += f"{sep}powerTimeSlotScheduleData: {self.power_time_slot_schedule_data}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                power_time_slot_schedule_data=data_dict.get('powerTimeSlotScheduleData'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class PowerTimeSlotScheduleConstraintsListDataType: # EEBus_SPINE_TS_PowerSequences.xsd:ns_p:PowerTimeSlotScheduleConstraintsListDataType -> ComplexType
    def __init__(
            self,
            power_time_slot_schedule_constraints_data: list[PowerTimeSlotScheduleConstraintsDataType] = None,
    ):
        super().__init__()
        
        self.power_time_slot_schedule_constraints_data = power_time_slot_schedule_constraints_data

        if not isinstance(self.power_time_slot_schedule_constraints_data, list | NoneType):
            raise TypeError("power_time_slot_schedule_constraints_data is not of type list[PowerTimeSlotScheduleConstraintsDataType]")
        
    def get_data(self):

        msg_data = []
        
        if self.power_time_slot_schedule_constraints_data is not None:
            msg_data.append({"powerTimeSlotScheduleConstraintsData": [d.get_data() for d in self.power_time_slot_schedule_constraints_data]})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.power_time_slot_schedule_constraints_data is not None:
            result_str += f"{sep}powerTimeSlotScheduleConstraintsData: {self.power_time_slot_schedule_constraints_data}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                power_time_slot_schedule_constraints_data=data_dict.get('powerTimeSlotScheduleConstraintsData'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class PowerSequenceStateListDataType: # EEBus_SPINE_TS_PowerSequences.xsd:ns_p:PowerSequenceStateListDataType -> ComplexType
    def __init__(
            self,
            power_sequence_state_data: list[PowerSequenceStateDataType] = None,
    ):
        super().__init__()
        
        self.power_sequence_state_data = power_sequence_state_data

        if not isinstance(self.power_sequence_state_data, list | NoneType):
            raise TypeError("power_sequence_state_data is not of type list[PowerSequenceStateDataType]")
        
    def get_data(self):

        msg_data = []
        
        if self.power_sequence_state_data is not None:
            msg_data.append({"powerSequenceStateData": [d.get_data() for d in self.power_sequence_state_data]})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.power_sequence_state_data is not None:
            result_str += f"{sep}powerSequenceStateData: {self.power_sequence_state_data}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                power_sequence_state_data=data_dict.get('powerSequenceStateData'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class PowerSequenceSchedulePreferenceListDataType: # EEBus_SPINE_TS_PowerSequences.xsd:ns_p:PowerSequenceSchedulePreferenceListDataType -> ComplexType
    def __init__(
            self,
            power_sequence_schedule_preference_data: list[PowerSequenceSchedulePreferenceDataType] = None,
    ):
        super().__init__()
        
        self.power_sequence_schedule_preference_data = power_sequence_schedule_preference_data

        if not isinstance(self.power_sequence_schedule_preference_data, list | NoneType):
            raise TypeError("power_sequence_schedule_preference_data is not of type list[PowerSequenceSchedulePreferenceDataType]")
        
    def get_data(self):

        msg_data = []
        
        if self.power_sequence_schedule_preference_data is not None:
            msg_data.append({"powerSequenceSchedulePreferenceData": [d.get_data() for d in self.power_sequence_schedule_preference_data]})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.power_sequence_schedule_preference_data is not None:
            result_str += f"{sep}powerSequenceSchedulePreferenceData: {self.power_sequence_schedule_preference_data}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                power_sequence_schedule_preference_data=data_dict.get('powerSequenceSchedulePreferenceData'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class PowerSequenceScheduleListDataType: # EEBus_SPINE_TS_PowerSequences.xsd:ns_p:PowerSequenceScheduleListDataType -> ComplexType
    def __init__(
            self,
            power_sequence_schedule_data: list[PowerSequenceScheduleDataType] = None,
    ):
        super().__init__()
        
        self.power_sequence_schedule_data = power_sequence_schedule_data

        if not isinstance(self.power_sequence_schedule_data, list | NoneType):
            raise TypeError("power_sequence_schedule_data is not of type list[PowerSequenceScheduleDataType]")
        
    def get_data(self):

        msg_data = []
        
        if self.power_sequence_schedule_data is not None:
            msg_data.append({"powerSequenceScheduleData": [d.get_data() for d in self.power_sequence_schedule_data]})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.power_sequence_schedule_data is not None:
            result_str += f"{sep}powerSequenceScheduleData: {self.power_sequence_schedule_data}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                power_sequence_schedule_data=data_dict.get('powerSequenceScheduleData'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class PowerSequenceScheduleConstraintsListDataType: # EEBus_SPINE_TS_PowerSequences.xsd:ns_p:PowerSequenceScheduleConstraintsListDataType -> ComplexType
    def __init__(
            self,
            power_sequence_schedule_constraints_data: list[PowerSequenceScheduleConstraintsDataType] = None,
    ):
        super().__init__()
        
        self.power_sequence_schedule_constraints_data = power_sequence_schedule_constraints_data

        if not isinstance(self.power_sequence_schedule_constraints_data, list | NoneType):
            raise TypeError("power_sequence_schedule_constraints_data is not of type list[PowerSequenceScheduleConstraintsDataType]")
        
    def get_data(self):

        msg_data = []
        
        if self.power_sequence_schedule_constraints_data is not None:
            msg_data.append({"powerSequenceScheduleConstraintsData": [d.get_data() for d in self.power_sequence_schedule_constraints_data]})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.power_sequence_schedule_constraints_data is not None:
            result_str += f"{sep}powerSequenceScheduleConstraintsData: {self.power_sequence_schedule_constraints_data}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                power_sequence_schedule_constraints_data=data_dict.get('powerSequenceScheduleConstraintsData'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class PowerSequenceScheduleConfigurationRequestCallType: # EEBus_SPINE_TS_PowerSequences.xsd:ns_p:PowerSequenceScheduleConfigurationRequestCallType -> ComplexType
    def __init__(
            self,
            sequence_id: PowerSequenceIdType = None,
    ):
        super().__init__()
        
        self.sequence_id = sequence_id

        if not isinstance(self.sequence_id, PowerSequenceIdType | NoneType):
            raise TypeError("sequence_id is not of type PowerSequenceIdType")
        
    def get_data(self):

        msg_data = []
        
        if self.sequence_id is not None:
            msg_data.append({"sequenceId": self.sequence_id.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.sequence_id is not None:
            result_str += f"{sep}sequenceId: {self.sequence_id}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                sequence_id=data_dict.get('sequenceId'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class PowerSequencePriceListDataType: # EEBus_SPINE_TS_PowerSequences.xsd:ns_p:PowerSequencePriceListDataType -> ComplexType
    def __init__(
            self,
            power_sequence_price_data: list[PowerSequencePriceDataType] = None,
    ):
        super().__init__()
        
        self.power_sequence_price_data = power_sequence_price_data

        if not isinstance(self.power_sequence_price_data, list | NoneType):
            raise TypeError("power_sequence_price_data is not of type list[PowerSequencePriceDataType]")
        
    def get_data(self):

        msg_data = []
        
        if self.power_sequence_price_data is not None:
            msg_data.append({"powerSequencePriceData": [d.get_data() for d in self.power_sequence_price_data]})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.power_sequence_price_data is not None:
            result_str += f"{sep}powerSequencePriceData: {self.power_sequence_price_data}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                power_sequence_price_data=data_dict.get('powerSequencePriceData'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class PowerSequencePriceCalculationRequestCallType: # EEBus_SPINE_TS_PowerSequences.xsd:ns_p:PowerSequencePriceCalculationRequestCallType -> ComplexType
    def __init__(
            self,
            sequence_id: PowerSequenceIdType = None,
            potential_start_time: AbsoluteOrRelativeTimeType = None,
    ):
        super().__init__()
        
        self.sequence_id = sequence_id
        self.potential_start_time = potential_start_time

        if not isinstance(self.sequence_id, PowerSequenceIdType | NoneType):
            raise TypeError("sequence_id is not of type PowerSequenceIdType")
        
        if not isinstance(self.potential_start_time, AbsoluteOrRelativeTimeType | NoneType):
            raise TypeError("potential_start_time is not of type AbsoluteOrRelativeTimeType")
        
    def get_data(self):

        msg_data = []
        
        if self.sequence_id is not None:
            msg_data.append({"sequenceId": self.sequence_id.get_data()})
        if self.potential_start_time is not None:
            msg_data.append({"potentialStartTime": self.potential_start_time.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.sequence_id is not None:
            result_str += f"{sep}sequenceId: {self.sequence_id}"
            sep = ", "
        if self.potential_start_time is not None:
            result_str += f"{sep}potentialStartTime: {self.potential_start_time}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                sequence_id=data_dict.get('sequenceId'),
                potential_start_time=data_dict.get('potentialStartTime'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class PowerSequenceNodeScheduleInformationDataType: # EEBus_SPINE_TS_PowerSequences.xsd:ns_p:PowerSequenceNodeScheduleInformationDataType -> ComplexType
    def __init__(
            self,
            node_remote_controllable: bool = None,
            supports_single_slot_scheduling_only: bool = None,
            alternatives_count: int = None,
            total_sequences_count_max: int = None,
            supports_reselection: bool = None,
    ):
        super().__init__()
        
        self.node_remote_controllable = node_remote_controllable
        self.supports_single_slot_scheduling_only = supports_single_slot_scheduling_only
        self.alternatives_count = alternatives_count
        self.total_sequences_count_max = total_sequences_count_max
        self.supports_reselection = supports_reselection

        if not isinstance(self.node_remote_controllable, bool | NoneType):
            raise TypeError("node_remote_controllable is not of type bool")
        
        if not isinstance(self.supports_single_slot_scheduling_only, bool | NoneType):
            raise TypeError("supports_single_slot_scheduling_only is not of type bool")
        
        if not isinstance(self.alternatives_count, int | NoneType):
            raise TypeError("alternatives_count is not of type int")
        
        if not isinstance(self.total_sequences_count_max, int | NoneType):
            raise TypeError("total_sequences_count_max is not of type int")
        
        if not isinstance(self.supports_reselection, bool | NoneType):
            raise TypeError("supports_reselection is not of type bool")
        
    def get_data(self):

        msg_data = []
        
        if self.node_remote_controllable is not None:
            msg_data.append({"nodeRemoteControllable": self.node_remote_controllable})
        if self.supports_single_slot_scheduling_only is not None:
            msg_data.append({"supportsSingleSlotSchedulingOnly": self.supports_single_slot_scheduling_only})
        if self.alternatives_count is not None:
            msg_data.append({"alternativesCount": self.alternatives_count})
        if self.total_sequences_count_max is not None:
            msg_data.append({"totalSequencesCountMax": self.total_sequences_count_max})
        if self.supports_reselection is not None:
            msg_data.append({"supportsReselection": self.supports_reselection})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.node_remote_controllable is not None:
            result_str += f"{sep}nodeRemoteControllable: {self.node_remote_controllable}"
            sep = ", "
        if self.supports_single_slot_scheduling_only is not None:
            result_str += f"{sep}supportsSingleSlotSchedulingOnly: {self.supports_single_slot_scheduling_only}"
            sep = ", "
        if self.alternatives_count is not None:
            result_str += f"{sep}alternativesCount: {self.alternatives_count}"
            sep = ", "
        if self.total_sequences_count_max is not None:
            result_str += f"{sep}totalSequencesCountMax: {self.total_sequences_count_max}"
            sep = ", "
        if self.supports_reselection is not None:
            result_str += f"{sep}supportsReselection: {self.supports_reselection}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                node_remote_controllable=data_dict.get('nodeRemoteControllable'),
                supports_single_slot_scheduling_only=data_dict.get('supportsSingleSlotSchedulingOnly'),
                alternatives_count=data_dict.get('alternativesCount'),
                total_sequences_count_max=data_dict.get('totalSequencesCountMax'),
                supports_reselection=data_dict.get('supportsReselection'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class PowerSequenceDescriptionListDataType: # EEBus_SPINE_TS_PowerSequences.xsd:ns_p:PowerSequenceDescriptionListDataType -> ComplexType
    def __init__(
            self,
            power_sequence_description_data: list[PowerSequenceDescriptionDataType] = None,
    ):
        super().__init__()
        
        self.power_sequence_description_data = power_sequence_description_data

        if not isinstance(self.power_sequence_description_data, list | NoneType):
            raise TypeError("power_sequence_description_data is not of type list[PowerSequenceDescriptionDataType]")
        
    def get_data(self):

        msg_data = []
        
        if self.power_sequence_description_data is not None:
            msg_data.append({"powerSequenceDescriptionData": [d.get_data() for d in self.power_sequence_description_data]})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.power_sequence_description_data is not None:
            result_str += f"{sep}powerSequenceDescriptionData: {self.power_sequence_description_data}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                power_sequence_description_data=data_dict.get('powerSequenceDescriptionData'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class PowerSequenceAlternativesRelationListDataType: # EEBus_SPINE_TS_PowerSequences.xsd:ns_p:PowerSequenceAlternativesRelationListDataType -> ComplexType
    def __init__(
            self,
            power_sequence_alternatives_relation_data: list[PowerSequenceAlternativesRelationDataType] = None,
    ):
        super().__init__()
        
        self.power_sequence_alternatives_relation_data = power_sequence_alternatives_relation_data

        if not isinstance(self.power_sequence_alternatives_relation_data, list | NoneType):
            raise TypeError("power_sequence_alternatives_relation_data is not of type list[PowerSequenceAlternativesRelationDataType]")
        
    def get_data(self):

        msg_data = []
        
        if self.power_sequence_alternatives_relation_data is not None:
            msg_data.append({"powerSequenceAlternativesRelationData": [d.get_data() for d in self.power_sequence_alternatives_relation_data]})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.power_sequence_alternatives_relation_data is not None:
            result_str += f"{sep}powerSequenceAlternativesRelationData: {self.power_sequence_alternatives_relation_data}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                power_sequence_alternatives_relation_data=data_dict.get('powerSequenceAlternativesRelationData'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class PowerTimeSlotValueDataElementsType: # EEBus_SPINE_TS_PowerSequences.xsd:ns_p:PowerTimeSlotValueDataElementsType -> ComplexType
    def __init__(
            self,
            sequence_id: ElementTagType = None,
            slot_number: ElementTagType = None,
            value_type: ElementTagType = None,
            value: ScaledNumberElementsType = None,
    ):
        super().__init__()
        
        self.sequence_id = sequence_id
        self.slot_number = slot_number
        self.value_type = value_type
        self.value = value

        if not isinstance(self.sequence_id, ElementTagType | NoneType):
            raise TypeError("sequence_id is not of type ElementTagType")
        
        if not isinstance(self.slot_number, ElementTagType | NoneType):
            raise TypeError("slot_number is not of type ElementTagType")
        
        if not isinstance(self.value_type, ElementTagType | NoneType):
            raise TypeError("value_type is not of type ElementTagType")
        
        if not isinstance(self.value, ScaledNumberElementsType | NoneType):
            raise TypeError("value is not of type ScaledNumberElementsType")
        
    def get_data(self):

        msg_data = []
        
        if self.sequence_id is not None:
            msg_data.append({"sequenceId": self.sequence_id.get_data()})
        if self.slot_number is not None:
            msg_data.append({"slotNumber": self.slot_number.get_data()})
        if self.value_type is not None:
            msg_data.append({"valueType": self.value_type.get_data()})
        if self.value is not None:
            msg_data.append({"value": self.value.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.sequence_id is not None:
            result_str += f"{sep}sequenceId: {self.sequence_id}"
            sep = ", "
        if self.slot_number is not None:
            result_str += f"{sep}slotNumber: {self.slot_number}"
            sep = ", "
        if self.value_type is not None:
            result_str += f"{sep}valueType: {self.value_type}"
            sep = ", "
        if self.value is not None:
            result_str += f"{sep}value: {self.value}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                sequence_id=data_dict.get('sequenceId'),
                slot_number=data_dict.get('slotNumber'),
                value_type=data_dict.get('valueType'),
                value=data_dict.get('value'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class PowerTimeSlotScheduleDataElementsType: # EEBus_SPINE_TS_PowerSequences.xsd:ns_p:PowerTimeSlotScheduleDataElementsType -> ComplexType
    def __init__(
            self,
            sequence_id: ElementTagType = None,
            slot_number: ElementTagType = None,
            time_period: TimePeriodElementsType = None,
            default_duration: ElementTagType = None,
            duration_uncertainty: ElementTagType = None,
            slot_activated: ElementTagType = None,
            description: ElementTagType = None,
    ):
        super().__init__()
        
        self.sequence_id = sequence_id
        self.slot_number = slot_number
        self.time_period = time_period
        self.default_duration = default_duration
        self.duration_uncertainty = duration_uncertainty
        self.slot_activated = slot_activated
        self.description = description

        if not isinstance(self.sequence_id, ElementTagType | NoneType):
            raise TypeError("sequence_id is not of type ElementTagType")
        
        if not isinstance(self.slot_number, ElementTagType | NoneType):
            raise TypeError("slot_number is not of type ElementTagType")
        
        if not isinstance(self.time_period, TimePeriodElementsType | NoneType):
            raise TypeError("time_period is not of type TimePeriodElementsType")
        
        if not isinstance(self.default_duration, ElementTagType | NoneType):
            raise TypeError("default_duration is not of type ElementTagType")
        
        if not isinstance(self.duration_uncertainty, ElementTagType | NoneType):
            raise TypeError("duration_uncertainty is not of type ElementTagType")
        
        if not isinstance(self.slot_activated, ElementTagType | NoneType):
            raise TypeError("slot_activated is not of type ElementTagType")
        
        if not isinstance(self.description, ElementTagType | NoneType):
            raise TypeError("description is not of type ElementTagType")
        
    def get_data(self):

        msg_data = []
        
        if self.sequence_id is not None:
            msg_data.append({"sequenceId": self.sequence_id.get_data()})
        if self.slot_number is not None:
            msg_data.append({"slotNumber": self.slot_number.get_data()})
        if self.time_period is not None:
            msg_data.append({"timePeriod": self.time_period.get_data()})
        if self.default_duration is not None:
            msg_data.append({"defaultDuration": self.default_duration.get_data()})
        if self.duration_uncertainty is not None:
            msg_data.append({"durationUncertainty": self.duration_uncertainty.get_data()})
        if self.slot_activated is not None:
            msg_data.append({"slotActivated": self.slot_activated.get_data()})
        if self.description is not None:
            msg_data.append({"description": self.description.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.sequence_id is not None:
            result_str += f"{sep}sequenceId: {self.sequence_id}"
            sep = ", "
        if self.slot_number is not None:
            result_str += f"{sep}slotNumber: {self.slot_number}"
            sep = ", "
        if self.time_period is not None:
            result_str += f"{sep}timePeriod: {self.time_period}"
            sep = ", "
        if self.default_duration is not None:
            result_str += f"{sep}defaultDuration: {self.default_duration}"
            sep = ", "
        if self.duration_uncertainty is not None:
            result_str += f"{sep}durationUncertainty: {self.duration_uncertainty}"
            sep = ", "
        if self.slot_activated is not None:
            result_str += f"{sep}slotActivated: {self.slot_activated}"
            sep = ", "
        if self.description is not None:
            result_str += f"{sep}description: {self.description}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                sequence_id=data_dict.get('sequenceId'),
                slot_number=data_dict.get('slotNumber'),
                time_period=data_dict.get('timePeriod'),
                default_duration=data_dict.get('defaultDuration'),
                duration_uncertainty=data_dict.get('durationUncertainty'),
                slot_activated=data_dict.get('slotActivated'),
                description=data_dict.get('description'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class PowerTimeSlotScheduleConstraintsDataElementsType: # EEBus_SPINE_TS_PowerSequences.xsd:ns_p:PowerTimeSlotScheduleConstraintsDataElementsType -> ComplexType
    def __init__(
            self,
            sequence_id: ElementTagType = None,
            slot_number: ElementTagType = None,
            earliest_start_time: ElementTagType = None,
            latest_end_time: ElementTagType = None,
            min_duration: ElementTagType = None,
            max_duration: ElementTagType = None,
            optional_slot: ElementTagType = None,
    ):
        super().__init__()
        
        self.sequence_id = sequence_id
        self.slot_number = slot_number
        self.earliest_start_time = earliest_start_time
        self.latest_end_time = latest_end_time
        self.min_duration = min_duration
        self.max_duration = max_duration
        self.optional_slot = optional_slot

        if not isinstance(self.sequence_id, ElementTagType | NoneType):
            raise TypeError("sequence_id is not of type ElementTagType")
        
        if not isinstance(self.slot_number, ElementTagType | NoneType):
            raise TypeError("slot_number is not of type ElementTagType")
        
        if not isinstance(self.earliest_start_time, ElementTagType | NoneType):
            raise TypeError("earliest_start_time is not of type ElementTagType")
        
        if not isinstance(self.latest_end_time, ElementTagType | NoneType):
            raise TypeError("latest_end_time is not of type ElementTagType")
        
        if not isinstance(self.min_duration, ElementTagType | NoneType):
            raise TypeError("min_duration is not of type ElementTagType")
        
        if not isinstance(self.max_duration, ElementTagType | NoneType):
            raise TypeError("max_duration is not of type ElementTagType")
        
        if not isinstance(self.optional_slot, ElementTagType | NoneType):
            raise TypeError("optional_slot is not of type ElementTagType")
        
    def get_data(self):

        msg_data = []
        
        if self.sequence_id is not None:
            msg_data.append({"sequenceId": self.sequence_id.get_data()})
        if self.slot_number is not None:
            msg_data.append({"slotNumber": self.slot_number.get_data()})
        if self.earliest_start_time is not None:
            msg_data.append({"earliestStartTime": self.earliest_start_time.get_data()})
        if self.latest_end_time is not None:
            msg_data.append({"latestEndTime": self.latest_end_time.get_data()})
        if self.min_duration is not None:
            msg_data.append({"minDuration": self.min_duration.get_data()})
        if self.max_duration is not None:
            msg_data.append({"maxDuration": self.max_duration.get_data()})
        if self.optional_slot is not None:
            msg_data.append({"optionalSlot": self.optional_slot.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.sequence_id is not None:
            result_str += f"{sep}sequenceId: {self.sequence_id}"
            sep = ", "
        if self.slot_number is not None:
            result_str += f"{sep}slotNumber: {self.slot_number}"
            sep = ", "
        if self.earliest_start_time is not None:
            result_str += f"{sep}earliestStartTime: {self.earliest_start_time}"
            sep = ", "
        if self.latest_end_time is not None:
            result_str += f"{sep}latestEndTime: {self.latest_end_time}"
            sep = ", "
        if self.min_duration is not None:
            result_str += f"{sep}minDuration: {self.min_duration}"
            sep = ", "
        if self.max_duration is not None:
            result_str += f"{sep}maxDuration: {self.max_duration}"
            sep = ", "
        if self.optional_slot is not None:
            result_str += f"{sep}optionalSlot: {self.optional_slot}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                sequence_id=data_dict.get('sequenceId'),
                slot_number=data_dict.get('slotNumber'),
                earliest_start_time=data_dict.get('earliestStartTime'),
                latest_end_time=data_dict.get('latestEndTime'),
                min_duration=data_dict.get('minDuration'),
                max_duration=data_dict.get('maxDuration'),
                optional_slot=data_dict.get('optionalSlot'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class PowerSequenceStateDataElementsType: # EEBus_SPINE_TS_PowerSequences.xsd:ns_p:PowerSequenceStateDataElementsType -> ComplexType
    def __init__(
            self,
            sequence_id: ElementTagType = None,
            state: ElementTagType = None,
            active_slot_number: ElementTagType = None,
            elapsed_slot_time: ElementTagType = None,
            remaining_slot_time: ElementTagType = None,
            sequence_remote_controllable: ElementTagType = None,
            active_repetition_number: ElementTagType = None,
            remaining_pause_time: ElementTagType = None,
    ):
        super().__init__()
        
        self.sequence_id = sequence_id
        self.state = state
        self.active_slot_number = active_slot_number
        self.elapsed_slot_time = elapsed_slot_time
        self.remaining_slot_time = remaining_slot_time
        self.sequence_remote_controllable = sequence_remote_controllable
        self.active_repetition_number = active_repetition_number
        self.remaining_pause_time = remaining_pause_time

        if not isinstance(self.sequence_id, ElementTagType | NoneType):
            raise TypeError("sequence_id is not of type ElementTagType")
        
        if not isinstance(self.state, ElementTagType | NoneType):
            raise TypeError("state is not of type ElementTagType")
        
        if not isinstance(self.active_slot_number, ElementTagType | NoneType):
            raise TypeError("active_slot_number is not of type ElementTagType")
        
        if not isinstance(self.elapsed_slot_time, ElementTagType | NoneType):
            raise TypeError("elapsed_slot_time is not of type ElementTagType")
        
        if not isinstance(self.remaining_slot_time, ElementTagType | NoneType):
            raise TypeError("remaining_slot_time is not of type ElementTagType")
        
        if not isinstance(self.sequence_remote_controllable, ElementTagType | NoneType):
            raise TypeError("sequence_remote_controllable is not of type ElementTagType")
        
        if not isinstance(self.active_repetition_number, ElementTagType | NoneType):
            raise TypeError("active_repetition_number is not of type ElementTagType")
        
        if not isinstance(self.remaining_pause_time, ElementTagType | NoneType):
            raise TypeError("remaining_pause_time is not of type ElementTagType")
        
    def get_data(self):

        msg_data = []
        
        if self.sequence_id is not None:
            msg_data.append({"sequenceId": self.sequence_id.get_data()})
        if self.state is not None:
            msg_data.append({"state": self.state.get_data()})
        if self.active_slot_number is not None:
            msg_data.append({"activeSlotNumber": self.active_slot_number.get_data()})
        if self.elapsed_slot_time is not None:
            msg_data.append({"elapsedSlotTime": self.elapsed_slot_time.get_data()})
        if self.remaining_slot_time is not None:
            msg_data.append({"remainingSlotTime": self.remaining_slot_time.get_data()})
        if self.sequence_remote_controllable is not None:
            msg_data.append({"sequenceRemoteControllable": self.sequence_remote_controllable.get_data()})
        if self.active_repetition_number is not None:
            msg_data.append({"activeRepetitionNumber": self.active_repetition_number.get_data()})
        if self.remaining_pause_time is not None:
            msg_data.append({"remainingPauseTime": self.remaining_pause_time.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.sequence_id is not None:
            result_str += f"{sep}sequenceId: {self.sequence_id}"
            sep = ", "
        if self.state is not None:
            result_str += f"{sep}state: {self.state}"
            sep = ", "
        if self.active_slot_number is not None:
            result_str += f"{sep}activeSlotNumber: {self.active_slot_number}"
            sep = ", "
        if self.elapsed_slot_time is not None:
            result_str += f"{sep}elapsedSlotTime: {self.elapsed_slot_time}"
            sep = ", "
        if self.remaining_slot_time is not None:
            result_str += f"{sep}remainingSlotTime: {self.remaining_slot_time}"
            sep = ", "
        if self.sequence_remote_controllable is not None:
            result_str += f"{sep}sequenceRemoteControllable: {self.sequence_remote_controllable}"
            sep = ", "
        if self.active_repetition_number is not None:
            result_str += f"{sep}activeRepetitionNumber: {self.active_repetition_number}"
            sep = ", "
        if self.remaining_pause_time is not None:
            result_str += f"{sep}remainingPauseTime: {self.remaining_pause_time}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                sequence_id=data_dict.get('sequenceId'),
                state=data_dict.get('state'),
                active_slot_number=data_dict.get('activeSlotNumber'),
                elapsed_slot_time=data_dict.get('elapsedSlotTime'),
                remaining_slot_time=data_dict.get('remainingSlotTime'),
                sequence_remote_controllable=data_dict.get('sequenceRemoteControllable'),
                active_repetition_number=data_dict.get('activeRepetitionNumber'),
                remaining_pause_time=data_dict.get('remainingPauseTime'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class PowerSequenceSchedulePreferenceDataElementsType: # EEBus_SPINE_TS_PowerSequences.xsd:ns_p:PowerSequenceSchedulePreferenceDataElementsType -> ComplexType
    def __init__(
            self,
            sequence_id: ElementTagType = None,
            greenest: ElementTagType = None,
            cheapest: ElementTagType = None,
    ):
        super().__init__()
        
        self.sequence_id = sequence_id
        self.greenest = greenest
        self.cheapest = cheapest

        if not isinstance(self.sequence_id, ElementTagType | NoneType):
            raise TypeError("sequence_id is not of type ElementTagType")
        
        if not isinstance(self.greenest, ElementTagType | NoneType):
            raise TypeError("greenest is not of type ElementTagType")
        
        if not isinstance(self.cheapest, ElementTagType | NoneType):
            raise TypeError("cheapest is not of type ElementTagType")
        
    def get_data(self):

        msg_data = []
        
        if self.sequence_id is not None:
            msg_data.append({"sequenceId": self.sequence_id.get_data()})
        if self.greenest is not None:
            msg_data.append({"greenest": self.greenest.get_data()})
        if self.cheapest is not None:
            msg_data.append({"cheapest": self.cheapest.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.sequence_id is not None:
            result_str += f"{sep}sequenceId: {self.sequence_id}"
            sep = ", "
        if self.greenest is not None:
            result_str += f"{sep}greenest: {self.greenest}"
            sep = ", "
        if self.cheapest is not None:
            result_str += f"{sep}cheapest: {self.cheapest}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                sequence_id=data_dict.get('sequenceId'),
                greenest=data_dict.get('greenest'),
                cheapest=data_dict.get('cheapest'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class PowerSequenceScheduleDataElementsType: # EEBus_SPINE_TS_PowerSequences.xsd:ns_p:PowerSequenceScheduleDataElementsType -> ComplexType
    def __init__(
            self,
            sequence_id: ElementTagType = None,
            start_time: ElementTagType = None,
            end_time: ElementTagType = None,
    ):
        super().__init__()
        
        self.sequence_id = sequence_id
        self.start_time = start_time
        self.end_time = end_time

        if not isinstance(self.sequence_id, ElementTagType | NoneType):
            raise TypeError("sequence_id is not of type ElementTagType")
        
        if not isinstance(self.start_time, ElementTagType | NoneType):
            raise TypeError("start_time is not of type ElementTagType")
        
        if not isinstance(self.end_time, ElementTagType | NoneType):
            raise TypeError("end_time is not of type ElementTagType")
        
    def get_data(self):

        msg_data = []
        
        if self.sequence_id is not None:
            msg_data.append({"sequenceId": self.sequence_id.get_data()})
        if self.start_time is not None:
            msg_data.append({"startTime": self.start_time.get_data()})
        if self.end_time is not None:
            msg_data.append({"endTime": self.end_time.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.sequence_id is not None:
            result_str += f"{sep}sequenceId: {self.sequence_id}"
            sep = ", "
        if self.start_time is not None:
            result_str += f"{sep}startTime: {self.start_time}"
            sep = ", "
        if self.end_time is not None:
            result_str += f"{sep}endTime: {self.end_time}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                sequence_id=data_dict.get('sequenceId'),
                start_time=data_dict.get('startTime'),
                end_time=data_dict.get('endTime'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class PowerSequenceScheduleConstraintsDataElementsType: # EEBus_SPINE_TS_PowerSequences.xsd:ns_p:PowerSequenceScheduleConstraintsDataElementsType -> ComplexType
    def __init__(
            self,
            sequence_id: ElementTagType = None,
            earliest_start_time: ElementTagType = None,
            latest_start_time: ElementTagType = None,
            earliest_end_time: ElementTagType = None,
            latest_end_time: ElementTagType = None,
            optional_sequence: ElementTagType = None,
    ):
        super().__init__()
        
        self.sequence_id = sequence_id
        self.earliest_start_time = earliest_start_time
        self.latest_start_time = latest_start_time
        self.earliest_end_time = earliest_end_time
        self.latest_end_time = latest_end_time
        self.optional_sequence = optional_sequence

        if not isinstance(self.sequence_id, ElementTagType | NoneType):
            raise TypeError("sequence_id is not of type ElementTagType")
        
        if not isinstance(self.earliest_start_time, ElementTagType | NoneType):
            raise TypeError("earliest_start_time is not of type ElementTagType")
        
        if not isinstance(self.latest_start_time, ElementTagType | NoneType):
            raise TypeError("latest_start_time is not of type ElementTagType")
        
        if not isinstance(self.earliest_end_time, ElementTagType | NoneType):
            raise TypeError("earliest_end_time is not of type ElementTagType")
        
        if not isinstance(self.latest_end_time, ElementTagType | NoneType):
            raise TypeError("latest_end_time is not of type ElementTagType")
        
        if not isinstance(self.optional_sequence, ElementTagType | NoneType):
            raise TypeError("optional_sequence is not of type ElementTagType")
        
    def get_data(self):

        msg_data = []
        
        if self.sequence_id is not None:
            msg_data.append({"sequenceId": self.sequence_id.get_data()})
        if self.earliest_start_time is not None:
            msg_data.append({"earliestStartTime": self.earliest_start_time.get_data()})
        if self.latest_start_time is not None:
            msg_data.append({"latestStartTime": self.latest_start_time.get_data()})
        if self.earliest_end_time is not None:
            msg_data.append({"earliestEndTime": self.earliest_end_time.get_data()})
        if self.latest_end_time is not None:
            msg_data.append({"latestEndTime": self.latest_end_time.get_data()})
        if self.optional_sequence is not None:
            msg_data.append({"optionalSequence": self.optional_sequence.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.sequence_id is not None:
            result_str += f"{sep}sequenceId: {self.sequence_id}"
            sep = ", "
        if self.earliest_start_time is not None:
            result_str += f"{sep}earliestStartTime: {self.earliest_start_time}"
            sep = ", "
        if self.latest_start_time is not None:
            result_str += f"{sep}latestStartTime: {self.latest_start_time}"
            sep = ", "
        if self.earliest_end_time is not None:
            result_str += f"{sep}earliestEndTime: {self.earliest_end_time}"
            sep = ", "
        if self.latest_end_time is not None:
            result_str += f"{sep}latestEndTime: {self.latest_end_time}"
            sep = ", "
        if self.optional_sequence is not None:
            result_str += f"{sep}optionalSequence: {self.optional_sequence}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                sequence_id=data_dict.get('sequenceId'),
                earliest_start_time=data_dict.get('earliestStartTime'),
                latest_start_time=data_dict.get('latestStartTime'),
                earliest_end_time=data_dict.get('earliestEndTime'),
                latest_end_time=data_dict.get('latestEndTime'),
                optional_sequence=data_dict.get('optionalSequence'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class PowerSequenceScheduleConfigurationRequestCallElementsType: # EEBus_SPINE_TS_PowerSequences.xsd:ns_p:PowerSequenceScheduleConfigurationRequestCallElementsType -> ComplexType
    def __init__(
            self,
            sequence_id: ElementTagType = None,
    ):
        super().__init__()
        
        self.sequence_id = sequence_id

        if not isinstance(self.sequence_id, ElementTagType | NoneType):
            raise TypeError("sequence_id is not of type ElementTagType")
        
    def get_data(self):

        msg_data = []
        
        if self.sequence_id is not None:
            msg_data.append({"sequenceId": self.sequence_id.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.sequence_id is not None:
            result_str += f"{sep}sequenceId: {self.sequence_id}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                sequence_id=data_dict.get('sequenceId'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class PowerSequencePriceDataElementsType: # EEBus_SPINE_TS_PowerSequences.xsd:ns_p:PowerSequencePriceDataElementsType -> ComplexType
    def __init__(
            self,
            sequence_id: ElementTagType = None,
            potential_start_time: ElementTagType = None,
            price: ScaledNumberElementsType = None,
            currency: ElementTagType = None,
    ):
        super().__init__()
        
        self.sequence_id = sequence_id
        self.potential_start_time = potential_start_time
        self.price = price
        self.currency = currency

        if not isinstance(self.sequence_id, ElementTagType | NoneType):
            raise TypeError("sequence_id is not of type ElementTagType")
        
        if not isinstance(self.potential_start_time, ElementTagType | NoneType):
            raise TypeError("potential_start_time is not of type ElementTagType")
        
        if not isinstance(self.price, ScaledNumberElementsType | NoneType):
            raise TypeError("price is not of type ScaledNumberElementsType")
        
        if not isinstance(self.currency, ElementTagType | NoneType):
            raise TypeError("currency is not of type ElementTagType")
        
    def get_data(self):

        msg_data = []
        
        if self.sequence_id is not None:
            msg_data.append({"sequenceId": self.sequence_id.get_data()})
        if self.potential_start_time is not None:
            msg_data.append({"potentialStartTime": self.potential_start_time.get_data()})
        if self.price is not None:
            msg_data.append({"price": self.price.get_data()})
        if self.currency is not None:
            msg_data.append({"currency": self.currency.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.sequence_id is not None:
            result_str += f"{sep}sequenceId: {self.sequence_id}"
            sep = ", "
        if self.potential_start_time is not None:
            result_str += f"{sep}potentialStartTime: {self.potential_start_time}"
            sep = ", "
        if self.price is not None:
            result_str += f"{sep}price: {self.price}"
            sep = ", "
        if self.currency is not None:
            result_str += f"{sep}currency: {self.currency}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                sequence_id=data_dict.get('sequenceId'),
                potential_start_time=data_dict.get('potentialStartTime'),
                price=data_dict.get('price'),
                currency=data_dict.get('currency'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class PowerSequencePriceCalculationRequestCallElementsType: # EEBus_SPINE_TS_PowerSequences.xsd:ns_p:PowerSequencePriceCalculationRequestCallElementsType -> ComplexType
    def __init__(
            self,
            sequence_id: ElementTagType = None,
            potential_start_time: ElementTagType = None,
    ):
        super().__init__()
        
        self.sequence_id = sequence_id
        self.potential_start_time = potential_start_time

        if not isinstance(self.sequence_id, ElementTagType | NoneType):
            raise TypeError("sequence_id is not of type ElementTagType")
        
        if not isinstance(self.potential_start_time, ElementTagType | NoneType):
            raise TypeError("potential_start_time is not of type ElementTagType")
        
    def get_data(self):

        msg_data = []
        
        if self.sequence_id is not None:
            msg_data.append({"sequenceId": self.sequence_id.get_data()})
        if self.potential_start_time is not None:
            msg_data.append({"potentialStartTime": self.potential_start_time.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.sequence_id is not None:
            result_str += f"{sep}sequenceId: {self.sequence_id}"
            sep = ", "
        if self.potential_start_time is not None:
            result_str += f"{sep}potentialStartTime: {self.potential_start_time}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                sequence_id=data_dict.get('sequenceId'),
                potential_start_time=data_dict.get('potentialStartTime'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class PowerSequenceNodeScheduleInformationDataElementsType: # EEBus_SPINE_TS_PowerSequences.xsd:ns_p:PowerSequenceNodeScheduleInformationDataElementsType -> ComplexType
    def __init__(
            self,
            node_remote_controllable: ElementTagType = None,
            supports_single_slot_scheduling_only: ElementTagType = None,
            alternatives_count: ElementTagType = None,
            total_sequences_count_max: ElementTagType = None,
            supports_reselection: ElementTagType = None,
    ):
        super().__init__()
        
        self.node_remote_controllable = node_remote_controllable
        self.supports_single_slot_scheduling_only = supports_single_slot_scheduling_only
        self.alternatives_count = alternatives_count
        self.total_sequences_count_max = total_sequences_count_max
        self.supports_reselection = supports_reselection

        if not isinstance(self.node_remote_controllable, ElementTagType | NoneType):
            raise TypeError("node_remote_controllable is not of type ElementTagType")
        
        if not isinstance(self.supports_single_slot_scheduling_only, ElementTagType | NoneType):
            raise TypeError("supports_single_slot_scheduling_only is not of type ElementTagType")
        
        if not isinstance(self.alternatives_count, ElementTagType | NoneType):
            raise TypeError("alternatives_count is not of type ElementTagType")
        
        if not isinstance(self.total_sequences_count_max, ElementTagType | NoneType):
            raise TypeError("total_sequences_count_max is not of type ElementTagType")
        
        if not isinstance(self.supports_reselection, ElementTagType | NoneType):
            raise TypeError("supports_reselection is not of type ElementTagType")
        
    def get_data(self):

        msg_data = []
        
        if self.node_remote_controllable is not None:
            msg_data.append({"nodeRemoteControllable": self.node_remote_controllable.get_data()})
        if self.supports_single_slot_scheduling_only is not None:
            msg_data.append({"supportsSingleSlotSchedulingOnly": self.supports_single_slot_scheduling_only.get_data()})
        if self.alternatives_count is not None:
            msg_data.append({"alternativesCount": self.alternatives_count.get_data()})
        if self.total_sequences_count_max is not None:
            msg_data.append({"totalSequencesCountMax": self.total_sequences_count_max.get_data()})
        if self.supports_reselection is not None:
            msg_data.append({"supportsReselection": self.supports_reselection.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.node_remote_controllable is not None:
            result_str += f"{sep}nodeRemoteControllable: {self.node_remote_controllable}"
            sep = ", "
        if self.supports_single_slot_scheduling_only is not None:
            result_str += f"{sep}supportsSingleSlotSchedulingOnly: {self.supports_single_slot_scheduling_only}"
            sep = ", "
        if self.alternatives_count is not None:
            result_str += f"{sep}alternativesCount: {self.alternatives_count}"
            sep = ", "
        if self.total_sequences_count_max is not None:
            result_str += f"{sep}totalSequencesCountMax: {self.total_sequences_count_max}"
            sep = ", "
        if self.supports_reselection is not None:
            result_str += f"{sep}supportsReselection: {self.supports_reselection}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                node_remote_controllable=data_dict.get('nodeRemoteControllable'),
                supports_single_slot_scheduling_only=data_dict.get('supportsSingleSlotSchedulingOnly'),
                alternatives_count=data_dict.get('alternativesCount'),
                total_sequences_count_max=data_dict.get('totalSequencesCountMax'),
                supports_reselection=data_dict.get('supportsReselection'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class PowerSequenceDescriptionDataElementsType: # EEBus_SPINE_TS_PowerSequences.xsd:ns_p:PowerSequenceDescriptionDataElementsType -> ComplexType
    def __init__(
            self,
            sequence_id: ElementTagType = None,
            description: ElementTagType = None,
            positive_energy_direction: ElementTagType = None,
            power_unit: ElementTagType = None,
            energy_unit: ElementTagType = None,
            value_source: ElementTagType = None,
            scope: ElementTagType = None,
            task_identifier: ElementTagType = None,
            repetitions_total: ElementTagType = None,
    ):
        super().__init__()
        
        self.sequence_id = sequence_id
        self.description = description
        self.positive_energy_direction = positive_energy_direction
        self.power_unit = power_unit
        self.energy_unit = energy_unit
        self.value_source = value_source
        self.scope = scope
        self.task_identifier = task_identifier
        self.repetitions_total = repetitions_total

        if not isinstance(self.sequence_id, ElementTagType | NoneType):
            raise TypeError("sequence_id is not of type ElementTagType")
        
        if not isinstance(self.description, ElementTagType | NoneType):
            raise TypeError("description is not of type ElementTagType")
        
        if not isinstance(self.positive_energy_direction, ElementTagType | NoneType):
            raise TypeError("positive_energy_direction is not of type ElementTagType")
        
        if not isinstance(self.power_unit, ElementTagType | NoneType):
            raise TypeError("power_unit is not of type ElementTagType")
        
        if not isinstance(self.energy_unit, ElementTagType | NoneType):
            raise TypeError("energy_unit is not of type ElementTagType")
        
        if not isinstance(self.value_source, ElementTagType | NoneType):
            raise TypeError("value_source is not of type ElementTagType")
        
        if not isinstance(self.scope, ElementTagType | NoneType):
            raise TypeError("scope is not of type ElementTagType")
        
        if not isinstance(self.task_identifier, ElementTagType | NoneType):
            raise TypeError("task_identifier is not of type ElementTagType")
        
        if not isinstance(self.repetitions_total, ElementTagType | NoneType):
            raise TypeError("repetitions_total is not of type ElementTagType")
        
    def get_data(self):

        msg_data = []
        
        if self.sequence_id is not None:
            msg_data.append({"sequenceId": self.sequence_id.get_data()})
        if self.description is not None:
            msg_data.append({"description": self.description.get_data()})
        if self.positive_energy_direction is not None:
            msg_data.append({"positiveEnergyDirection": self.positive_energy_direction.get_data()})
        if self.power_unit is not None:
            msg_data.append({"powerUnit": self.power_unit.get_data()})
        if self.energy_unit is not None:
            msg_data.append({"energyUnit": self.energy_unit.get_data()})
        if self.value_source is not None:
            msg_data.append({"valueSource": self.value_source.get_data()})
        if self.scope is not None:
            msg_data.append({"scope": self.scope.get_data()})
        if self.task_identifier is not None:
            msg_data.append({"taskIdentifier": self.task_identifier.get_data()})
        if self.repetitions_total is not None:
            msg_data.append({"repetitionsTotal": self.repetitions_total.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.sequence_id is not None:
            result_str += f"{sep}sequenceId: {self.sequence_id}"
            sep = ", "
        if self.description is not None:
            result_str += f"{sep}description: {self.description}"
            sep = ", "
        if self.positive_energy_direction is not None:
            result_str += f"{sep}positiveEnergyDirection: {self.positive_energy_direction}"
            sep = ", "
        if self.power_unit is not None:
            result_str += f"{sep}powerUnit: {self.power_unit}"
            sep = ", "
        if self.energy_unit is not None:
            result_str += f"{sep}energyUnit: {self.energy_unit}"
            sep = ", "
        if self.value_source is not None:
            result_str += f"{sep}valueSource: {self.value_source}"
            sep = ", "
        if self.scope is not None:
            result_str += f"{sep}scope: {self.scope}"
            sep = ", "
        if self.task_identifier is not None:
            result_str += f"{sep}taskIdentifier: {self.task_identifier}"
            sep = ", "
        if self.repetitions_total is not None:
            result_str += f"{sep}repetitionsTotal: {self.repetitions_total}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                sequence_id=data_dict.get('sequenceId'),
                description=data_dict.get('description'),
                positive_energy_direction=data_dict.get('positiveEnergyDirection'),
                power_unit=data_dict.get('powerUnit'),
                energy_unit=data_dict.get('energyUnit'),
                value_source=data_dict.get('valueSource'),
                scope=data_dict.get('scope'),
                task_identifier=data_dict.get('taskIdentifier'),
                repetitions_total=data_dict.get('repetitionsTotal'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class PowerSequenceAlternativesRelationDataElementsType: # EEBus_SPINE_TS_PowerSequences.xsd:ns_p:PowerSequenceAlternativesRelationDataElementsType -> ComplexType
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
        
    def get_data(self):

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


class PowerTimeSlotValueListDataSelectorsType: # EEBus_SPINE_TS_PowerSequences.xsd:ns_p:PowerTimeSlotValueListDataSelectorsType -> ComplexType
    def __init__(
            self,
            sequence_id: PowerSequenceIdType = None,
            slot_number: PowerTimeSlotNumberType = None,
            value_type: PowerTimeSlotValueTypeType = None,
    ):
        super().__init__()
        
        self.sequence_id = sequence_id
        self.slot_number = slot_number
        self.value_type = value_type

        if not isinstance(self.sequence_id, PowerSequenceIdType | NoneType):
            raise TypeError("sequence_id is not of type PowerSequenceIdType")
        
        if not isinstance(self.slot_number, PowerTimeSlotNumberType | NoneType):
            raise TypeError("slot_number is not of type PowerTimeSlotNumberType")
        
        if not isinstance(self.value_type, PowerTimeSlotValueTypeType | NoneType):
            raise TypeError("value_type is not of type PowerTimeSlotValueTypeType")
        
    def get_data(self):

        msg_data = []
        
        if self.sequence_id is not None:
            msg_data.append({"sequenceId": self.sequence_id.get_data()})
        if self.slot_number is not None:
            msg_data.append({"slotNumber": self.slot_number.get_data()})
        if self.value_type is not None:
            msg_data.append({"valueType": self.value_type.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.sequence_id is not None:
            result_str += f"{sep}sequenceId: {self.sequence_id}"
            sep = ", "
        if self.slot_number is not None:
            result_str += f"{sep}slotNumber: {self.slot_number}"
            sep = ", "
        if self.value_type is not None:
            result_str += f"{sep}valueType: {self.value_type}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                sequence_id=data_dict.get('sequenceId'),
                slot_number=data_dict.get('slotNumber'),
                value_type=data_dict.get('valueType'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class PowerTimeSlotScheduleListDataSelectorsType: # EEBus_SPINE_TS_PowerSequences.xsd:ns_p:PowerTimeSlotScheduleListDataSelectorsType -> ComplexType
    def __init__(
            self,
            sequence_id: PowerSequenceIdType = None,
            slot_number: PowerTimeSlotNumberType = None,
    ):
        super().__init__()
        
        self.sequence_id = sequence_id
        self.slot_number = slot_number

        if not isinstance(self.sequence_id, PowerSequenceIdType | NoneType):
            raise TypeError("sequence_id is not of type PowerSequenceIdType")
        
        if not isinstance(self.slot_number, PowerTimeSlotNumberType | NoneType):
            raise TypeError("slot_number is not of type PowerTimeSlotNumberType")
        
    def get_data(self):

        msg_data = []
        
        if self.sequence_id is not None:
            msg_data.append({"sequenceId": self.sequence_id.get_data()})
        if self.slot_number is not None:
            msg_data.append({"slotNumber": self.slot_number.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.sequence_id is not None:
            result_str += f"{sep}sequenceId: {self.sequence_id}"
            sep = ", "
        if self.slot_number is not None:
            result_str += f"{sep}slotNumber: {self.slot_number}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                sequence_id=data_dict.get('sequenceId'),
                slot_number=data_dict.get('slotNumber'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class PowerTimeSlotScheduleConstraintsListDataSelectorsType: # EEBus_SPINE_TS_PowerSequences.xsd:ns_p:PowerTimeSlotScheduleConstraintsListDataSelectorsType -> ComplexType
    def __init__(
            self,
            sequence_id: PowerSequenceIdType = None,
            slot_number: PowerTimeSlotNumberType = None,
    ):
        super().__init__()
        
        self.sequence_id = sequence_id
        self.slot_number = slot_number

        if not isinstance(self.sequence_id, PowerSequenceIdType | NoneType):
            raise TypeError("sequence_id is not of type PowerSequenceIdType")
        
        if not isinstance(self.slot_number, PowerTimeSlotNumberType | NoneType):
            raise TypeError("slot_number is not of type PowerTimeSlotNumberType")
        
    def get_data(self):

        msg_data = []
        
        if self.sequence_id is not None:
            msg_data.append({"sequenceId": self.sequence_id.get_data()})
        if self.slot_number is not None:
            msg_data.append({"slotNumber": self.slot_number.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.sequence_id is not None:
            result_str += f"{sep}sequenceId: {self.sequence_id}"
            sep = ", "
        if self.slot_number is not None:
            result_str += f"{sep}slotNumber: {self.slot_number}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                sequence_id=data_dict.get('sequenceId'),
                slot_number=data_dict.get('slotNumber'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class PowerSequenceStateListDataSelectorsType: # EEBus_SPINE_TS_PowerSequences.xsd:ns_p:PowerSequenceStateListDataSelectorsType -> ComplexType
    def __init__(
            self,
            sequence_id: PowerSequenceIdType = None,
    ):
        super().__init__()
        
        self.sequence_id = sequence_id

        if not isinstance(self.sequence_id, PowerSequenceIdType | NoneType):
            raise TypeError("sequence_id is not of type PowerSequenceIdType")
        
    def get_data(self):

        msg_data = []
        
        if self.sequence_id is not None:
            msg_data.append({"sequenceId": self.sequence_id.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.sequence_id is not None:
            result_str += f"{sep}sequenceId: {self.sequence_id}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                sequence_id=data_dict.get('sequenceId'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class PowerSequenceSchedulePreferenceListDataSelectorsType: # EEBus_SPINE_TS_PowerSequences.xsd:ns_p:PowerSequenceSchedulePreferenceListDataSelectorsType -> ComplexType
    def __init__(
            self,
            sequence_id: PowerSequenceIdType = None,
    ):
        super().__init__()
        
        self.sequence_id = sequence_id

        if not isinstance(self.sequence_id, PowerSequenceIdType | NoneType):
            raise TypeError("sequence_id is not of type PowerSequenceIdType")
        
    def get_data(self):

        msg_data = []
        
        if self.sequence_id is not None:
            msg_data.append({"sequenceId": self.sequence_id.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.sequence_id is not None:
            result_str += f"{sep}sequenceId: {self.sequence_id}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                sequence_id=data_dict.get('sequenceId'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class PowerSequenceScheduleListDataSelectorsType: # EEBus_SPINE_TS_PowerSequences.xsd:ns_p:PowerSequenceScheduleListDataSelectorsType -> ComplexType
    def __init__(
            self,
            sequence_id: PowerSequenceIdType = None,
    ):
        super().__init__()
        
        self.sequence_id = sequence_id

        if not isinstance(self.sequence_id, PowerSequenceIdType | NoneType):
            raise TypeError("sequence_id is not of type PowerSequenceIdType")
        
    def get_data(self):

        msg_data = []
        
        if self.sequence_id is not None:
            msg_data.append({"sequenceId": self.sequence_id.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.sequence_id is not None:
            result_str += f"{sep}sequenceId: {self.sequence_id}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                sequence_id=data_dict.get('sequenceId'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class PowerSequenceScheduleConstraintsListDataSelectorsType: # EEBus_SPINE_TS_PowerSequences.xsd:ns_p:PowerSequenceScheduleConstraintsListDataSelectorsType -> ComplexType
    def __init__(
            self,
            sequence_id: PowerSequenceIdType = None,
    ):
        super().__init__()
        
        self.sequence_id = sequence_id

        if not isinstance(self.sequence_id, PowerSequenceIdType | NoneType):
            raise TypeError("sequence_id is not of type PowerSequenceIdType")
        
    def get_data(self):

        msg_data = []
        
        if self.sequence_id is not None:
            msg_data.append({"sequenceId": self.sequence_id.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.sequence_id is not None:
            result_str += f"{sep}sequenceId: {self.sequence_id}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                sequence_id=data_dict.get('sequenceId'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class PowerSequencePriceListDataSelectorsType: # EEBus_SPINE_TS_PowerSequences.xsd:ns_p:PowerSequencePriceListDataSelectorsType -> ComplexType
    def __init__(
            self,
            sequence_id: PowerSequenceIdType = None,
            potential_start_time_interval: TimestampIntervalType = None,
    ):
        super().__init__()
        
        self.sequence_id = sequence_id
        self.potential_start_time_interval = potential_start_time_interval

        if not isinstance(self.sequence_id, PowerSequenceIdType | NoneType):
            raise TypeError("sequence_id is not of type PowerSequenceIdType")
        
        if not isinstance(self.potential_start_time_interval, TimestampIntervalType | NoneType):
            raise TypeError("potential_start_time_interval is not of type TimestampIntervalType")
        
    def get_data(self):

        msg_data = []
        
        if self.sequence_id is not None:
            msg_data.append({"sequenceId": self.sequence_id.get_data()})
        if self.potential_start_time_interval is not None:
            msg_data.append({"potentialStartTimeInterval": self.potential_start_time_interval.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.sequence_id is not None:
            result_str += f"{sep}sequenceId: {self.sequence_id}"
            sep = ", "
        if self.potential_start_time_interval is not None:
            result_str += f"{sep}potentialStartTimeInterval: {self.potential_start_time_interval}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                sequence_id=data_dict.get('sequenceId'),
                potential_start_time_interval=data_dict.get('potentialStartTimeInterval'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class PowerSequenceDescriptionListDataSelectorsType: # EEBus_SPINE_TS_PowerSequences.xsd:ns_p:PowerSequenceDescriptionListDataSelectorsType -> ComplexType
    def __init__(
            self,
            sequence_id: PowerSequenceIdType = None,
    ):
        super().__init__()
        
        self.sequence_id = sequence_id

        if not isinstance(self.sequence_id, PowerSequenceIdType | NoneType):
            raise TypeError("sequence_id is not of type PowerSequenceIdType")
        
    def get_data(self):

        msg_data = []
        
        if self.sequence_id is not None:
            msg_data.append({"sequenceId": self.sequence_id.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.sequence_id is not None:
            result_str += f"{sep}sequenceId: {self.sequence_id}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                sequence_id=data_dict.get('sequenceId'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class PowerSequenceAlternativesRelationListDataSelectorsType: # EEBus_SPINE_TS_PowerSequences.xsd:ns_p:PowerSequenceAlternativesRelationListDataSelectorsType -> ComplexType
    def __init__(
            self,
            alternatives_id: AlternativesIdType = None,
            sequence_id: PowerSequenceIdType = None,
    ):
        super().__init__()
        
        self.alternatives_id = alternatives_id
        self.sequence_id = sequence_id

        if not isinstance(self.alternatives_id, AlternativesIdType | NoneType):
            raise TypeError("alternatives_id is not of type AlternativesIdType")
        
        if not isinstance(self.sequence_id, PowerSequenceIdType | NoneType):
            raise TypeError("sequence_id is not of type PowerSequenceIdType")
        
    def get_data(self):

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



