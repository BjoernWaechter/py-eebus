# Jinja Template message_type.py.jinja2
from spine.base_type.commondatatypes import ElementTagType
from spine.base_type.commondatatypes import ScaledNumberElementsType
from spine.base_type.commondatatypes import ScaledNumberType
from spine.base_type.commondatatypes import TimestampIntervalType
from spine.simple_type.powersequences import PowerSequenceIdType
from spine.union_type.commondatatypes import AbsoluteOrRelativeTimeType
from spine.union_type.commondatatypes import EnergyDirectionType
from spine.union_type.commondatatypes import EnergyModeType
from spine.union_type.commondatatypes import UnitOfMeasurementType
from spine.union_type.directcontrol import DirectControlActivityStateType
from types import NoneType
from spine import array_2_dict


class DirectControlActivityDataType: # EEBus_SPINE_TS_DirectControl.xsd: ComplexType
    def __init__(
            self,
            timestamp: AbsoluteOrRelativeTimeType = None,
            activity_state: DirectControlActivityStateType = None,
            is_activity_state_changeable: bool = None,
            energy_mode: EnergyModeType = None,
            is_energy_mode_changeable: bool = None,
            power: ScaledNumberType = None,
            is_power_changeable: bool = None,
            energy: ScaledNumberType = None,
            is_energy_changeable: bool = None,
            sequence_id: PowerSequenceIdType = None,
    ):
        super().__init__()
        
        self.timestamp = timestamp
        self.activity_state = activity_state
        self.is_activity_state_changeable = is_activity_state_changeable
        self.energy_mode = energy_mode
        self.is_energy_mode_changeable = is_energy_mode_changeable
        self.power = power
        self.is_power_changeable = is_power_changeable
        self.energy = energy
        self.is_energy_changeable = is_energy_changeable
        self.sequence_id = sequence_id

        if not isinstance(self.timestamp, AbsoluteOrRelativeTimeType | NoneType):
            raise TypeError("timestamp is not of type AbsoluteOrRelativeTimeType")
        
        if not isinstance(self.activity_state, DirectControlActivityStateType | NoneType):
            raise TypeError("activity_state is not of type DirectControlActivityStateType")
        
        if not isinstance(self.is_activity_state_changeable, bool | NoneType):
            raise TypeError("is_activity_state_changeable is not of type bool")
        
        if not isinstance(self.energy_mode, EnergyModeType | NoneType):
            raise TypeError("energy_mode is not of type EnergyModeType")
        
        if not isinstance(self.is_energy_mode_changeable, bool | NoneType):
            raise TypeError("is_energy_mode_changeable is not of type bool")
        
        if not isinstance(self.power, ScaledNumberType | NoneType):
            raise TypeError("power is not of type ScaledNumberType")
        
        if not isinstance(self.is_power_changeable, bool | NoneType):
            raise TypeError("is_power_changeable is not of type bool")
        
        if not isinstance(self.energy, ScaledNumberType | NoneType):
            raise TypeError("energy is not of type ScaledNumberType")
        
        if not isinstance(self.is_energy_changeable, bool | NoneType):
            raise TypeError("is_energy_changeable is not of type bool")
        
        if not isinstance(self.sequence_id, PowerSequenceIdType | NoneType):
            raise TypeError("sequence_id is not of type PowerSequenceIdType")
        
    def get_data(self):

        msg_data = []
        
        if self.timestamp is not None:
            msg_data.append({"timestamp": self.timestamp.get_data()})
        if self.activity_state is not None:
            msg_data.append({"activityState": self.activity_state.get_data()})
        if self.is_activity_state_changeable is not None:
            msg_data.append({"isActivityStateChangeable": self.is_activity_state_changeable})
        if self.energy_mode is not None:
            msg_data.append({"energyMode": self.energy_mode.get_data()})
        if self.is_energy_mode_changeable is not None:
            msg_data.append({"isEnergyModeChangeable": self.is_energy_mode_changeable})
        if self.power is not None:
            msg_data.append({"power": self.power.get_data()})
        if self.is_power_changeable is not None:
            msg_data.append({"isPowerChangeable": self.is_power_changeable})
        if self.energy is not None:
            msg_data.append({"energy": self.energy.get_data()})
        if self.is_energy_changeable is not None:
            msg_data.append({"isEnergyChangeable": self.is_energy_changeable})
        if self.sequence_id is not None:
            msg_data.append({"sequenceId": self.sequence_id.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.timestamp is not None:
            result_str += f"{sep}timestamp: {self.timestamp}"
            sep = ", "
        if self.activity_state is not None:
            result_str += f"{sep}activityState: {self.activity_state}"
            sep = ", "
        if self.is_activity_state_changeable is not None:
            result_str += f"{sep}isActivityStateChangeable: {self.is_activity_state_changeable}"
            sep = ", "
        if self.energy_mode is not None:
            result_str += f"{sep}energyMode: {self.energy_mode}"
            sep = ", "
        if self.is_energy_mode_changeable is not None:
            result_str += f"{sep}isEnergyModeChangeable: {self.is_energy_mode_changeable}"
            sep = ", "
        if self.power is not None:
            result_str += f"{sep}power: {self.power}"
            sep = ", "
        if self.is_power_changeable is not None:
            result_str += f"{sep}isPowerChangeable: {self.is_power_changeable}"
            sep = ", "
        if self.energy is not None:
            result_str += f"{sep}energy: {self.energy}"
            sep = ", "
        if self.is_energy_changeable is not None:
            result_str += f"{sep}isEnergyChangeable: {self.is_energy_changeable}"
            sep = ", "
        if self.sequence_id is not None:
            result_str += f"{sep}sequenceId: {self.sequence_id}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                timestamp=data_dict.get('timestamp'),
                activity_state=data_dict.get('activityState'),
                is_activity_state_changeable=data_dict.get('isActivityStateChangeable'),
                energy_mode=data_dict.get('energyMode'),
                is_energy_mode_changeable=data_dict.get('isEnergyModeChangeable'),
                power=data_dict.get('power'),
                is_power_changeable=data_dict.get('isPowerChangeable'),
                energy=data_dict.get('energy'),
                is_energy_changeable=data_dict.get('isEnergyChangeable'),
                sequence_id=data_dict.get('sequenceId'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class DirectControlDescriptionDataType: # EEBus_SPINE_TS_DirectControl.xsd: ComplexType
    def __init__(
            self,
            positive_energy_direction: EnergyDirectionType = None,
            power_unit: UnitOfMeasurementType = None,
            energy_unit: UnitOfMeasurementType = None,
    ):
        super().__init__()
        
        self.positive_energy_direction = positive_energy_direction
        self.power_unit = power_unit
        self.energy_unit = energy_unit

        if not isinstance(self.positive_energy_direction, EnergyDirectionType | NoneType):
            raise TypeError("positive_energy_direction is not of type EnergyDirectionType")
        
        if not isinstance(self.power_unit, UnitOfMeasurementType | NoneType):
            raise TypeError("power_unit is not of type UnitOfMeasurementType")
        
        if not isinstance(self.energy_unit, UnitOfMeasurementType | NoneType):
            raise TypeError("energy_unit is not of type UnitOfMeasurementType")
        
    def get_data(self):

        msg_data = []
        
        if self.positive_energy_direction is not None:
            msg_data.append({"positiveEnergyDirection": self.positive_energy_direction.get_data()})
        if self.power_unit is not None:
            msg_data.append({"powerUnit": self.power_unit.get_data()})
        if self.energy_unit is not None:
            msg_data.append({"energyUnit": self.energy_unit.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.positive_energy_direction is not None:
            result_str += f"{sep}positiveEnergyDirection: {self.positive_energy_direction}"
            sep = ", "
        if self.power_unit is not None:
            result_str += f"{sep}powerUnit: {self.power_unit}"
            sep = ", "
        if self.energy_unit is not None:
            result_str += f"{sep}energyUnit: {self.energy_unit}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                positive_energy_direction=data_dict.get('positiveEnergyDirection'),
                power_unit=data_dict.get('powerUnit'),
                energy_unit=data_dict.get('energyUnit'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class DirectControlActivityListDataType: # EEBus_SPINE_TS_DirectControl.xsd: ComplexType
    def __init__(
            self,
            direct_control_activity_data: list[DirectControlActivityDataType] = None,
    ):
        super().__init__()
        
        self.direct_control_activity_data = direct_control_activity_data

        if not isinstance(self.direct_control_activity_data, list | NoneType):
            raise TypeError("direct_control_activity_data is not of type list[DirectControlActivityDataType]")
        
    def get_data(self):

        msg_data = []
        
        if self.direct_control_activity_data is not None:
            msg_data.append({"directControlActivityData": [d.get_data() for d in self.direct_control_activity_data]})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.direct_control_activity_data is not None:
            result_str += f"{sep}directControlActivityData: {self.direct_control_activity_data}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                direct_control_activity_data=data_dict.get('directControlActivityData'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class DirectControlDescriptionDataElementsType: # EEBus_SPINE_TS_DirectControl.xsd: ComplexType
    def __init__(
            self,
            positive_energy_direction: ElementTagType = None,
            power_unit: ElementTagType = None,
            energy_unit: ElementTagType = None,
    ):
        super().__init__()
        
        self.positive_energy_direction = positive_energy_direction
        self.power_unit = power_unit
        self.energy_unit = energy_unit

        if not isinstance(self.positive_energy_direction, ElementTagType | NoneType):
            raise TypeError("positive_energy_direction is not of type ElementTagType")
        
        if not isinstance(self.power_unit, ElementTagType | NoneType):
            raise TypeError("power_unit is not of type ElementTagType")
        
        if not isinstance(self.energy_unit, ElementTagType | NoneType):
            raise TypeError("energy_unit is not of type ElementTagType")
        
    def get_data(self):

        msg_data = []
        
        if self.positive_energy_direction is not None:
            msg_data.append({"positiveEnergyDirection": self.positive_energy_direction.get_data()})
        if self.power_unit is not None:
            msg_data.append({"powerUnit": self.power_unit.get_data()})
        if self.energy_unit is not None:
            msg_data.append({"energyUnit": self.energy_unit.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.positive_energy_direction is not None:
            result_str += f"{sep}positiveEnergyDirection: {self.positive_energy_direction}"
            sep = ", "
        if self.power_unit is not None:
            result_str += f"{sep}powerUnit: {self.power_unit}"
            sep = ", "
        if self.energy_unit is not None:
            result_str += f"{sep}energyUnit: {self.energy_unit}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                positive_energy_direction=data_dict.get('positiveEnergyDirection'),
                power_unit=data_dict.get('powerUnit'),
                energy_unit=data_dict.get('energyUnit'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class DirectControlActivityDataElementsType: # EEBus_SPINE_TS_DirectControl.xsd: ComplexType
    def __init__(
            self,
            timestamp: ElementTagType = None,
            activity_state: ElementTagType = None,
            is_activity_state_changeable: ElementTagType = None,
            energy_mode: ElementTagType = None,
            is_energy_mode_changeable: ElementTagType = None,
            power: ScaledNumberElementsType = None,
            is_power_changeable: ElementTagType = None,
            energy: ScaledNumberElementsType = None,
            is_energy_changeable: ElementTagType = None,
            sequence_id: ElementTagType = None,
    ):
        super().__init__()
        
        self.timestamp = timestamp
        self.activity_state = activity_state
        self.is_activity_state_changeable = is_activity_state_changeable
        self.energy_mode = energy_mode
        self.is_energy_mode_changeable = is_energy_mode_changeable
        self.power = power
        self.is_power_changeable = is_power_changeable
        self.energy = energy
        self.is_energy_changeable = is_energy_changeable
        self.sequence_id = sequence_id

        if not isinstance(self.timestamp, ElementTagType | NoneType):
            raise TypeError("timestamp is not of type ElementTagType")
        
        if not isinstance(self.activity_state, ElementTagType | NoneType):
            raise TypeError("activity_state is not of type ElementTagType")
        
        if not isinstance(self.is_activity_state_changeable, ElementTagType | NoneType):
            raise TypeError("is_activity_state_changeable is not of type ElementTagType")
        
        if not isinstance(self.energy_mode, ElementTagType | NoneType):
            raise TypeError("energy_mode is not of type ElementTagType")
        
        if not isinstance(self.is_energy_mode_changeable, ElementTagType | NoneType):
            raise TypeError("is_energy_mode_changeable is not of type ElementTagType")
        
        if not isinstance(self.power, ScaledNumberElementsType | NoneType):
            raise TypeError("power is not of type ScaledNumberElementsType")
        
        if not isinstance(self.is_power_changeable, ElementTagType | NoneType):
            raise TypeError("is_power_changeable is not of type ElementTagType")
        
        if not isinstance(self.energy, ScaledNumberElementsType | NoneType):
            raise TypeError("energy is not of type ScaledNumberElementsType")
        
        if not isinstance(self.is_energy_changeable, ElementTagType | NoneType):
            raise TypeError("is_energy_changeable is not of type ElementTagType")
        
        if not isinstance(self.sequence_id, ElementTagType | NoneType):
            raise TypeError("sequence_id is not of type ElementTagType")
        
    def get_data(self):

        msg_data = []
        
        if self.timestamp is not None:
            msg_data.append({"timestamp": self.timestamp.get_data()})
        if self.activity_state is not None:
            msg_data.append({"activityState": self.activity_state.get_data()})
        if self.is_activity_state_changeable is not None:
            msg_data.append({"isActivityStateChangeable": self.is_activity_state_changeable.get_data()})
        if self.energy_mode is not None:
            msg_data.append({"energyMode": self.energy_mode.get_data()})
        if self.is_energy_mode_changeable is not None:
            msg_data.append({"isEnergyModeChangeable": self.is_energy_mode_changeable.get_data()})
        if self.power is not None:
            msg_data.append({"power": self.power.get_data()})
        if self.is_power_changeable is not None:
            msg_data.append({"isPowerChangeable": self.is_power_changeable.get_data()})
        if self.energy is not None:
            msg_data.append({"energy": self.energy.get_data()})
        if self.is_energy_changeable is not None:
            msg_data.append({"isEnergyChangeable": self.is_energy_changeable.get_data()})
        if self.sequence_id is not None:
            msg_data.append({"sequenceId": self.sequence_id.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.timestamp is not None:
            result_str += f"{sep}timestamp: {self.timestamp}"
            sep = ", "
        if self.activity_state is not None:
            result_str += f"{sep}activityState: {self.activity_state}"
            sep = ", "
        if self.is_activity_state_changeable is not None:
            result_str += f"{sep}isActivityStateChangeable: {self.is_activity_state_changeable}"
            sep = ", "
        if self.energy_mode is not None:
            result_str += f"{sep}energyMode: {self.energy_mode}"
            sep = ", "
        if self.is_energy_mode_changeable is not None:
            result_str += f"{sep}isEnergyModeChangeable: {self.is_energy_mode_changeable}"
            sep = ", "
        if self.power is not None:
            result_str += f"{sep}power: {self.power}"
            sep = ", "
        if self.is_power_changeable is not None:
            result_str += f"{sep}isPowerChangeable: {self.is_power_changeable}"
            sep = ", "
        if self.energy is not None:
            result_str += f"{sep}energy: {self.energy}"
            sep = ", "
        if self.is_energy_changeable is not None:
            result_str += f"{sep}isEnergyChangeable: {self.is_energy_changeable}"
            sep = ", "
        if self.sequence_id is not None:
            result_str += f"{sep}sequenceId: {self.sequence_id}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                timestamp=data_dict.get('timestamp'),
                activity_state=data_dict.get('activityState'),
                is_activity_state_changeable=data_dict.get('isActivityStateChangeable'),
                energy_mode=data_dict.get('energyMode'),
                is_energy_mode_changeable=data_dict.get('isEnergyModeChangeable'),
                power=data_dict.get('power'),
                is_power_changeable=data_dict.get('isPowerChangeable'),
                energy=data_dict.get('energy'),
                is_energy_changeable=data_dict.get('isEnergyChangeable'),
                sequence_id=data_dict.get('sequenceId'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class DirectControlActivityListDataSelectorsType: # EEBus_SPINE_TS_DirectControl.xsd: ComplexType
    def __init__(
            self,
            timestamp_interval: TimestampIntervalType = None,
    ):
        super().__init__()
        
        self.timestamp_interval = timestamp_interval

        if not isinstance(self.timestamp_interval, TimestampIntervalType | NoneType):
            raise TypeError("timestamp_interval is not of type TimestampIntervalType")
        
    def get_data(self):

        msg_data = []
        
        if self.timestamp_interval is not None:
            msg_data.append({"timestampInterval": self.timestamp_interval.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.timestamp_interval is not None:
            result_str += f"{sep}timestampInterval: {self.timestamp_interval}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                timestamp_interval=data_dict.get('timestampInterval'),
            )
        elif data:
            return cls(data)
        else:
            return cls()



