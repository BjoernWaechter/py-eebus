# Jinja Template message_type.py.jinja2
from spine.simple_type.powersequences import PowerSequenceIdType
from spine.simple_type.commondatatypes import DescriptionType
from spine.base_type.commondatatypes import ScaledNumberElementsType
from spine.base_type.commondatatypes import ElementTagType
from spine.union_type.commondatatypes import FunctionType
from spine.base_type.commondatatypes import ScaledNumberType
from types import NoneType
from spine import array_2_dict


class OperatingConstraintsResumeImplicationDataType:
    def __init__(
            self,
            sequence_id: PowerSequenceIdType = None,
            resume_energy_estimated: ScaledNumberType = None,
            energy_unit: FunctionType = None,
            resume_cost_estimated: ScaledNumberType = None,
            currency: FunctionType = None,
    ):
        super().__init__()
        
        self.sequence_id = sequence_id
        self.resume_energy_estimated = resume_energy_estimated
        self.energy_unit = energy_unit
        self.resume_cost_estimated = resume_cost_estimated
        self.currency = currency

        if not isinstance(self.sequence_id, PowerSequenceIdType | NoneType):
            raise TypeError("sequence_id is not of type PowerSequenceIdType")
        
        if not isinstance(self.resume_energy_estimated, ScaledNumberType | NoneType):
            raise TypeError("resume_energy_estimated is not of type ScaledNumberType")
        
        if not isinstance(self.energy_unit, FunctionType | NoneType):
            raise TypeError("energy_unit is not of type FunctionType")
        
        if not isinstance(self.resume_cost_estimated, ScaledNumberType | NoneType):
            raise TypeError("resume_cost_estimated is not of type ScaledNumberType")
        
        if not isinstance(self.currency, FunctionType | NoneType):
            raise TypeError("currency is not of type FunctionType")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.sequence_id is not None:
            msg_data.append({"sequenceId": self.sequence_id.get_data()})
        if self.resume_energy_estimated is not None:
            msg_data.append({"resumeEnergyEstimated": self.resume_energy_estimated.get_data()})
        if self.energy_unit is not None:
            msg_data.append({"energyUnit": self.energy_unit.get_data()})
        if self.resume_cost_estimated is not None:
            msg_data.append({"resumeCostEstimated": self.resume_cost_estimated.get_data()})
        if self.currency is not None:
            msg_data.append({"currency": self.currency.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.sequence_id is not None:
            result_str += f"{sep}sequenceId: {self.sequence_id}"
            sep = ", "
        if self.resume_energy_estimated is not None:
            result_str += f"{sep}resumeEnergyEstimated: {self.resume_energy_estimated}"
            sep = ", "
        if self.energy_unit is not None:
            result_str += f"{sep}energyUnit: {self.energy_unit}"
            sep = ", "
        if self.resume_cost_estimated is not None:
            result_str += f"{sep}resumeCostEstimated: {self.resume_cost_estimated}"
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
                resume_energy_estimated=data_dict.get('resumeEnergyEstimated'),
                energy_unit=data_dict.get('energyUnit'),
                resume_cost_estimated=data_dict.get('resumeCostEstimated'),
                currency=data_dict.get('currency'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class OperatingConstraintsPowerRangeDataType:
    def __init__(
            self,
            sequence_id: PowerSequenceIdType = None,
            power_min: ScaledNumberType = None,
            power_max: ScaledNumberType = None,
            energy_min: ScaledNumberType = None,
            energy_max: ScaledNumberType = None,
    ):
        super().__init__()
        
        self.sequence_id = sequence_id
        self.power_min = power_min
        self.power_max = power_max
        self.energy_min = energy_min
        self.energy_max = energy_max

        if not isinstance(self.sequence_id, PowerSequenceIdType | NoneType):
            raise TypeError("sequence_id is not of type PowerSequenceIdType")
        
        if not isinstance(self.power_min, ScaledNumberType | NoneType):
            raise TypeError("power_min is not of type ScaledNumberType")
        
        if not isinstance(self.power_max, ScaledNumberType | NoneType):
            raise TypeError("power_max is not of type ScaledNumberType")
        
        if not isinstance(self.energy_min, ScaledNumberType | NoneType):
            raise TypeError("energy_min is not of type ScaledNumberType")
        
        if not isinstance(self.energy_max, ScaledNumberType | NoneType):
            raise TypeError("energy_max is not of type ScaledNumberType")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.sequence_id is not None:
            msg_data.append({"sequenceId": self.sequence_id.get_data()})
        if self.power_min is not None:
            msg_data.append({"powerMin": self.power_min.get_data()})
        if self.power_max is not None:
            msg_data.append({"powerMax": self.power_max.get_data()})
        if self.energy_min is not None:
            msg_data.append({"energyMin": self.energy_min.get_data()})
        if self.energy_max is not None:
            msg_data.append({"energyMax": self.energy_max.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.sequence_id is not None:
            result_str += f"{sep}sequenceId: {self.sequence_id}"
            sep = ", "
        if self.power_min is not None:
            result_str += f"{sep}powerMin: {self.power_min}"
            sep = ", "
        if self.power_max is not None:
            result_str += f"{sep}powerMax: {self.power_max}"
            sep = ", "
        if self.energy_min is not None:
            result_str += f"{sep}energyMin: {self.energy_min}"
            sep = ", "
        if self.energy_max is not None:
            result_str += f"{sep}energyMax: {self.energy_max}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                sequence_id=data_dict.get('sequenceId'),
                power_min=data_dict.get('powerMin'),
                power_max=data_dict.get('powerMax'),
                energy_min=data_dict.get('energyMin'),
                energy_max=data_dict.get('energyMax'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class OperatingConstraintsPowerLevelDataType:
    def __init__(
            self,
            sequence_id: PowerSequenceIdType = None,
            power: list[ScaledNumberType] = None,
    ):
        super().__init__()
        
        self.sequence_id = sequence_id
        self.power = power

        if not isinstance(self.sequence_id, PowerSequenceIdType | NoneType):
            raise TypeError("sequence_id is not of type PowerSequenceIdType")
        
        if not isinstance(self.power, list | NoneType):
            raise TypeError("power is not of type list[ScaledNumberType]")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.sequence_id is not None:
            msg_data.append({"sequenceId": self.sequence_id.get_data()})
        if self.power is not None:
            msg_data.append({"power": [d.get_data() for d in self.power]})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.sequence_id is not None:
            result_str += f"{sep}sequenceId: {self.sequence_id}"
            sep = ", "
        if self.power is not None:
            result_str += f"{sep}power: {self.power}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                sequence_id=data_dict.get('sequenceId'),
                power=data_dict.get('power'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class OperatingConstraintsPowerDescriptionDataType:
    def __init__(
            self,
            sequence_id: PowerSequenceIdType = None,
            positive_energy_direction: FunctionType = None,
            power_unit: FunctionType = None,
            energy_unit: FunctionType = None,
            description: DescriptionType = None,
    ):
        super().__init__()
        
        self.sequence_id = sequence_id
        self.positive_energy_direction = positive_energy_direction
        self.power_unit = power_unit
        self.energy_unit = energy_unit
        self.description = description

        if not isinstance(self.sequence_id, PowerSequenceIdType | NoneType):
            raise TypeError("sequence_id is not of type PowerSequenceIdType")
        
        if not isinstance(self.positive_energy_direction, FunctionType | NoneType):
            raise TypeError("positive_energy_direction is not of type FunctionType")
        
        if not isinstance(self.power_unit, FunctionType | NoneType):
            raise TypeError("power_unit is not of type FunctionType")
        
        if not isinstance(self.energy_unit, FunctionType | NoneType):
            raise TypeError("energy_unit is not of type FunctionType")
        
        if not isinstance(self.description, DescriptionType | NoneType):
            raise TypeError("description is not of type DescriptionType")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.sequence_id is not None:
            msg_data.append({"sequenceId": self.sequence_id.get_data()})
        if self.positive_energy_direction is not None:
            msg_data.append({"positiveEnergyDirection": self.positive_energy_direction.get_data()})
        if self.power_unit is not None:
            msg_data.append({"powerUnit": self.power_unit.get_data()})
        if self.energy_unit is not None:
            msg_data.append({"energyUnit": self.energy_unit.get_data()})
        if self.description is not None:
            msg_data.append({"description": self.description.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.sequence_id is not None:
            result_str += f"{sep}sequenceId: {self.sequence_id}"
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
        if self.description is not None:
            result_str += f"{sep}description: {self.description}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                sequence_id=data_dict.get('sequenceId'),
                positive_energy_direction=data_dict.get('positiveEnergyDirection'),
                power_unit=data_dict.get('powerUnit'),
                energy_unit=data_dict.get('energyUnit'),
                description=data_dict.get('description'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class OperatingConstraintsInterruptDataType:
    def __init__(
            self,
            sequence_id: PowerSequenceIdType = None,
            is_pausable: bool = None,
            is_stoppable: bool = None,
            not_interruptible_at_high_power: bool = None,
            max_cycles_per_day: int = None,
    ):
        super().__init__()
        
        self.sequence_id = sequence_id
        self.is_pausable = is_pausable
        self.is_stoppable = is_stoppable
        self.not_interruptible_at_high_power = not_interruptible_at_high_power
        self.max_cycles_per_day = max_cycles_per_day

        if not isinstance(self.sequence_id, PowerSequenceIdType | NoneType):
            raise TypeError("sequence_id is not of type PowerSequenceIdType")
        
        if not isinstance(self.is_pausable, bool | NoneType):
            raise TypeError("is_pausable is not of type bool")
        
        if not isinstance(self.is_stoppable, bool | NoneType):
            raise TypeError("is_stoppable is not of type bool")
        
        if not isinstance(self.not_interruptible_at_high_power, bool | NoneType):
            raise TypeError("not_interruptible_at_high_power is not of type bool")
        
        if not isinstance(self.max_cycles_per_day, int | NoneType):
            raise TypeError("max_cycles_per_day is not of type int")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.sequence_id is not None:
            msg_data.append({"sequenceId": self.sequence_id.get_data()})
        if self.is_pausable is not None:
            msg_data.append({"isPausable": self.is_pausable})
        if self.is_stoppable is not None:
            msg_data.append({"isStoppable": self.is_stoppable})
        if self.not_interruptible_at_high_power is not None:
            msg_data.append({"notInterruptibleAtHighPower": self.not_interruptible_at_high_power})
        if self.max_cycles_per_day is not None:
            msg_data.append({"maxCyclesPerDay": self.max_cycles_per_day})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.sequence_id is not None:
            result_str += f"{sep}sequenceId: {self.sequence_id}"
            sep = ", "
        if self.is_pausable is not None:
            result_str += f"{sep}isPausable: {self.is_pausable}"
            sep = ", "
        if self.is_stoppable is not None:
            result_str += f"{sep}isStoppable: {self.is_stoppable}"
            sep = ", "
        if self.not_interruptible_at_high_power is not None:
            result_str += f"{sep}notInterruptibleAtHighPower: {self.not_interruptible_at_high_power}"
            sep = ", "
        if self.max_cycles_per_day is not None:
            result_str += f"{sep}maxCyclesPerDay: {self.max_cycles_per_day}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                sequence_id=data_dict.get('sequenceId'),
                is_pausable=data_dict.get('isPausable'),
                is_stoppable=data_dict.get('isStoppable'),
                not_interruptible_at_high_power=data_dict.get('notInterruptibleAtHighPower'),
                max_cycles_per_day=data_dict.get('maxCyclesPerDay'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class OperatingConstraintsDurationDataType:
    def __init__(
            self,
            sequence_id: PowerSequenceIdType = None,
            active_duration_min: str = None,
            active_duration_max: str = None,
            pause_duration_min: str = None,
            pause_duration_max: str = None,
            active_duration_sum_min: str = None,
            active_duration_sum_max: str = None,
    ):
        super().__init__()
        
        self.sequence_id = sequence_id
        self.active_duration_min = active_duration_min
        self.active_duration_max = active_duration_max
        self.pause_duration_min = pause_duration_min
        self.pause_duration_max = pause_duration_max
        self.active_duration_sum_min = active_duration_sum_min
        self.active_duration_sum_max = active_duration_sum_max

        if not isinstance(self.sequence_id, PowerSequenceIdType | NoneType):
            raise TypeError("sequence_id is not of type PowerSequenceIdType")
        
        if not isinstance(self.active_duration_min, str | NoneType):
            raise TypeError("active_duration_min is not of type str")
        
        if not isinstance(self.active_duration_max, str | NoneType):
            raise TypeError("active_duration_max is not of type str")
        
        if not isinstance(self.pause_duration_min, str | NoneType):
            raise TypeError("pause_duration_min is not of type str")
        
        if not isinstance(self.pause_duration_max, str | NoneType):
            raise TypeError("pause_duration_max is not of type str")
        
        if not isinstance(self.active_duration_sum_min, str | NoneType):
            raise TypeError("active_duration_sum_min is not of type str")
        
        if not isinstance(self.active_duration_sum_max, str | NoneType):
            raise TypeError("active_duration_sum_max is not of type str")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.sequence_id is not None:
            msg_data.append({"sequenceId": self.sequence_id.get_data()})
        if self.active_duration_min is not None:
            msg_data.append({"activeDurationMin": self.active_duration_min})
        if self.active_duration_max is not None:
            msg_data.append({"activeDurationMax": self.active_duration_max})
        if self.pause_duration_min is not None:
            msg_data.append({"pauseDurationMin": self.pause_duration_min})
        if self.pause_duration_max is not None:
            msg_data.append({"pauseDurationMax": self.pause_duration_max})
        if self.active_duration_sum_min is not None:
            msg_data.append({"activeDurationSumMin": self.active_duration_sum_min})
        if self.active_duration_sum_max is not None:
            msg_data.append({"activeDurationSumMax": self.active_duration_sum_max})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.sequence_id is not None:
            result_str += f"{sep}sequenceId: {self.sequence_id}"
            sep = ", "
        if self.active_duration_min is not None:
            result_str += f"{sep}activeDurationMin: {self.active_duration_min}"
            sep = ", "
        if self.active_duration_max is not None:
            result_str += f"{sep}activeDurationMax: {self.active_duration_max}"
            sep = ", "
        if self.pause_duration_min is not None:
            result_str += f"{sep}pauseDurationMin: {self.pause_duration_min}"
            sep = ", "
        if self.pause_duration_max is not None:
            result_str += f"{sep}pauseDurationMax: {self.pause_duration_max}"
            sep = ", "
        if self.active_duration_sum_min is not None:
            result_str += f"{sep}activeDurationSumMin: {self.active_duration_sum_min}"
            sep = ", "
        if self.active_duration_sum_max is not None:
            result_str += f"{sep}activeDurationSumMax: {self.active_duration_sum_max}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                sequence_id=data_dict.get('sequenceId'),
                active_duration_min=data_dict.get('activeDurationMin'),
                active_duration_max=data_dict.get('activeDurationMax'),
                pause_duration_min=data_dict.get('pauseDurationMin'),
                pause_duration_max=data_dict.get('pauseDurationMax'),
                active_duration_sum_min=data_dict.get('activeDurationSumMin'),
                active_duration_sum_max=data_dict.get('activeDurationSumMax'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class OperatingConstraintsResumeImplicationListDataType:
    def __init__(
            self,
            operating_constraints_resume_implication_data: list[OperatingConstraintsResumeImplicationDataType] = None,
    ):
        super().__init__()
        
        self.operating_constraints_resume_implication_data = operating_constraints_resume_implication_data

        if not isinstance(self.operating_constraints_resume_implication_data, list | NoneType):
            raise TypeError("operating_constraints_resume_implication_data is not of type list[OperatingConstraintsResumeImplicationDataType]")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.operating_constraints_resume_implication_data is not None:
            msg_data.append({"operatingConstraintsResumeImplicationData": [d.get_data() for d in self.operating_constraints_resume_implication_data]})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.operating_constraints_resume_implication_data is not None:
            result_str += f"{sep}operatingConstraintsResumeImplicationData: {self.operating_constraints_resume_implication_data}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                operating_constraints_resume_implication_data=data_dict.get('operatingConstraintsResumeImplicationData'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class OperatingConstraintsResumeImplicationListDataSelectorsType:
    def __init__(
            self,
            sequence_id: PowerSequenceIdType = None,
    ):
        super().__init__()
        
        self.sequence_id = sequence_id

        if not isinstance(self.sequence_id, PowerSequenceIdType | NoneType):
            raise TypeError("sequence_id is not of type PowerSequenceIdType")
        
    def get_data(self): # ComplexType

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


class OperatingConstraintsResumeImplicationDataElementsType:
    def __init__(
            self,
            sequence_id: ElementTagType = None,
            resume_energy_estimated: ScaledNumberElementsType = None,
            energy_unit: ElementTagType = None,
            resume_cost_estimated: ScaledNumberElementsType = None,
            currency: ElementTagType = None,
    ):
        super().__init__()
        
        self.sequence_id = sequence_id
        self.resume_energy_estimated = resume_energy_estimated
        self.energy_unit = energy_unit
        self.resume_cost_estimated = resume_cost_estimated
        self.currency = currency

        if not isinstance(self.sequence_id, ElementTagType | NoneType):
            raise TypeError("sequence_id is not of type ElementTagType")
        
        if not isinstance(self.resume_energy_estimated, ScaledNumberElementsType | NoneType):
            raise TypeError("resume_energy_estimated is not of type ScaledNumberElementsType")
        
        if not isinstance(self.energy_unit, ElementTagType | NoneType):
            raise TypeError("energy_unit is not of type ElementTagType")
        
        if not isinstance(self.resume_cost_estimated, ScaledNumberElementsType | NoneType):
            raise TypeError("resume_cost_estimated is not of type ScaledNumberElementsType")
        
        if not isinstance(self.currency, ElementTagType | NoneType):
            raise TypeError("currency is not of type ElementTagType")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.sequence_id is not None:
            msg_data.append({"sequenceId": self.sequence_id.get_data()})
        if self.resume_energy_estimated is not None:
            msg_data.append({"resumeEnergyEstimated": self.resume_energy_estimated.get_data()})
        if self.energy_unit is not None:
            msg_data.append({"energyUnit": self.energy_unit.get_data()})
        if self.resume_cost_estimated is not None:
            msg_data.append({"resumeCostEstimated": self.resume_cost_estimated.get_data()})
        if self.currency is not None:
            msg_data.append({"currency": self.currency.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.sequence_id is not None:
            result_str += f"{sep}sequenceId: {self.sequence_id}"
            sep = ", "
        if self.resume_energy_estimated is not None:
            result_str += f"{sep}resumeEnergyEstimated: {self.resume_energy_estimated}"
            sep = ", "
        if self.energy_unit is not None:
            result_str += f"{sep}energyUnit: {self.energy_unit}"
            sep = ", "
        if self.resume_cost_estimated is not None:
            result_str += f"{sep}resumeCostEstimated: {self.resume_cost_estimated}"
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
                resume_energy_estimated=data_dict.get('resumeEnergyEstimated'),
                energy_unit=data_dict.get('energyUnit'),
                resume_cost_estimated=data_dict.get('resumeCostEstimated'),
                currency=data_dict.get('currency'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class OperatingConstraintsPowerRangeListDataType:
    def __init__(
            self,
            operating_constraints_power_range_data: list[OperatingConstraintsPowerRangeDataType] = None,
    ):
        super().__init__()
        
        self.operating_constraints_power_range_data = operating_constraints_power_range_data

        if not isinstance(self.operating_constraints_power_range_data, list | NoneType):
            raise TypeError("operating_constraints_power_range_data is not of type list[OperatingConstraintsPowerRangeDataType]")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.operating_constraints_power_range_data is not None:
            msg_data.append({"operatingConstraintsPowerRangeData": [d.get_data() for d in self.operating_constraints_power_range_data]})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.operating_constraints_power_range_data is not None:
            result_str += f"{sep}operatingConstraintsPowerRangeData: {self.operating_constraints_power_range_data}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                operating_constraints_power_range_data=data_dict.get('operatingConstraintsPowerRangeData'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class OperatingConstraintsPowerRangeListDataSelectorsType:
    def __init__(
            self,
            sequence_id: PowerSequenceIdType = None,
    ):
        super().__init__()
        
        self.sequence_id = sequence_id

        if not isinstance(self.sequence_id, PowerSequenceIdType | NoneType):
            raise TypeError("sequence_id is not of type PowerSequenceIdType")
        
    def get_data(self): # ComplexType

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


class OperatingConstraintsPowerRangeDataElementsType:
    def __init__(
            self,
            sequence_id: ElementTagType = None,
            power_min: ScaledNumberElementsType = None,
            power_max: ScaledNumberElementsType = None,
            energy_min: ScaledNumberElementsType = None,
            energy_max: ScaledNumberElementsType = None,
    ):
        super().__init__()
        
        self.sequence_id = sequence_id
        self.power_min = power_min
        self.power_max = power_max
        self.energy_min = energy_min
        self.energy_max = energy_max

        if not isinstance(self.sequence_id, ElementTagType | NoneType):
            raise TypeError("sequence_id is not of type ElementTagType")
        
        if not isinstance(self.power_min, ScaledNumberElementsType | NoneType):
            raise TypeError("power_min is not of type ScaledNumberElementsType")
        
        if not isinstance(self.power_max, ScaledNumberElementsType | NoneType):
            raise TypeError("power_max is not of type ScaledNumberElementsType")
        
        if not isinstance(self.energy_min, ScaledNumberElementsType | NoneType):
            raise TypeError("energy_min is not of type ScaledNumberElementsType")
        
        if not isinstance(self.energy_max, ScaledNumberElementsType | NoneType):
            raise TypeError("energy_max is not of type ScaledNumberElementsType")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.sequence_id is not None:
            msg_data.append({"sequenceId": self.sequence_id.get_data()})
        if self.power_min is not None:
            msg_data.append({"powerMin": self.power_min.get_data()})
        if self.power_max is not None:
            msg_data.append({"powerMax": self.power_max.get_data()})
        if self.energy_min is not None:
            msg_data.append({"energyMin": self.energy_min.get_data()})
        if self.energy_max is not None:
            msg_data.append({"energyMax": self.energy_max.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.sequence_id is not None:
            result_str += f"{sep}sequenceId: {self.sequence_id}"
            sep = ", "
        if self.power_min is not None:
            result_str += f"{sep}powerMin: {self.power_min}"
            sep = ", "
        if self.power_max is not None:
            result_str += f"{sep}powerMax: {self.power_max}"
            sep = ", "
        if self.energy_min is not None:
            result_str += f"{sep}energyMin: {self.energy_min}"
            sep = ", "
        if self.energy_max is not None:
            result_str += f"{sep}energyMax: {self.energy_max}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                sequence_id=data_dict.get('sequenceId'),
                power_min=data_dict.get('powerMin'),
                power_max=data_dict.get('powerMax'),
                energy_min=data_dict.get('energyMin'),
                energy_max=data_dict.get('energyMax'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class OperatingConstraintsPowerLevelListDataType:
    def __init__(
            self,
            operating_constraints_power_level_data: list[OperatingConstraintsPowerLevelDataType] = None,
    ):
        super().__init__()
        
        self.operating_constraints_power_level_data = operating_constraints_power_level_data

        if not isinstance(self.operating_constraints_power_level_data, list | NoneType):
            raise TypeError("operating_constraints_power_level_data is not of type list[OperatingConstraintsPowerLevelDataType]")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.operating_constraints_power_level_data is not None:
            msg_data.append({"operatingConstraintsPowerLevelData": [d.get_data() for d in self.operating_constraints_power_level_data]})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.operating_constraints_power_level_data is not None:
            result_str += f"{sep}operatingConstraintsPowerLevelData: {self.operating_constraints_power_level_data}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                operating_constraints_power_level_data=data_dict.get('operatingConstraintsPowerLevelData'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class OperatingConstraintsPowerLevelListDataSelectorsType:
    def __init__(
            self,
            sequence_id: PowerSequenceIdType = None,
    ):
        super().__init__()
        
        self.sequence_id = sequence_id

        if not isinstance(self.sequence_id, PowerSequenceIdType | NoneType):
            raise TypeError("sequence_id is not of type PowerSequenceIdType")
        
    def get_data(self): # ComplexType

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


class OperatingConstraintsPowerLevelDataElementsType:
    def __init__(
            self,
            sequence_id: ElementTagType = None,
            power: ScaledNumberElementsType = None,
    ):
        super().__init__()
        
        self.sequence_id = sequence_id
        self.power = power

        if not isinstance(self.sequence_id, ElementTagType | NoneType):
            raise TypeError("sequence_id is not of type ElementTagType")
        
        if not isinstance(self.power, ScaledNumberElementsType | NoneType):
            raise TypeError("power is not of type ScaledNumberElementsType")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.sequence_id is not None:
            msg_data.append({"sequenceId": self.sequence_id.get_data()})
        if self.power is not None:
            msg_data.append({"power": self.power.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.sequence_id is not None:
            result_str += f"{sep}sequenceId: {self.sequence_id}"
            sep = ", "
        if self.power is not None:
            result_str += f"{sep}power: {self.power}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                sequence_id=data_dict.get('sequenceId'),
                power=data_dict.get('power'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class OperatingConstraintsPowerDescriptionListDataType:
    def __init__(
            self,
            operating_constraints_power_description_data: list[OperatingConstraintsPowerDescriptionDataType] = None,
    ):
        super().__init__()
        
        self.operating_constraints_power_description_data = operating_constraints_power_description_data

        if not isinstance(self.operating_constraints_power_description_data, list | NoneType):
            raise TypeError("operating_constraints_power_description_data is not of type list[OperatingConstraintsPowerDescriptionDataType]")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.operating_constraints_power_description_data is not None:
            msg_data.append({"operatingConstraintsPowerDescriptionData": [d.get_data() for d in self.operating_constraints_power_description_data]})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.operating_constraints_power_description_data is not None:
            result_str += f"{sep}operatingConstraintsPowerDescriptionData: {self.operating_constraints_power_description_data}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                operating_constraints_power_description_data=data_dict.get('operatingConstraintsPowerDescriptionData'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class OperatingConstraintsPowerDescriptionListDataSelectorsType:
    def __init__(
            self,
            sequence_id: PowerSequenceIdType = None,
    ):
        super().__init__()
        
        self.sequence_id = sequence_id

        if not isinstance(self.sequence_id, PowerSequenceIdType | NoneType):
            raise TypeError("sequence_id is not of type PowerSequenceIdType")
        
    def get_data(self): # ComplexType

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


class OperatingConstraintsPowerDescriptionDataElementsType:
    def __init__(
            self,
            sequence_id: ElementTagType = None,
            positive_energy_direction: ElementTagType = None,
            power_unit: ElementTagType = None,
            energy_unit: ElementTagType = None,
            description: ElementTagType = None,
    ):
        super().__init__()
        
        self.sequence_id = sequence_id
        self.positive_energy_direction = positive_energy_direction
        self.power_unit = power_unit
        self.energy_unit = energy_unit
        self.description = description

        if not isinstance(self.sequence_id, ElementTagType | NoneType):
            raise TypeError("sequence_id is not of type ElementTagType")
        
        if not isinstance(self.positive_energy_direction, ElementTagType | NoneType):
            raise TypeError("positive_energy_direction is not of type ElementTagType")
        
        if not isinstance(self.power_unit, ElementTagType | NoneType):
            raise TypeError("power_unit is not of type ElementTagType")
        
        if not isinstance(self.energy_unit, ElementTagType | NoneType):
            raise TypeError("energy_unit is not of type ElementTagType")
        
        if not isinstance(self.description, ElementTagType | NoneType):
            raise TypeError("description is not of type ElementTagType")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.sequence_id is not None:
            msg_data.append({"sequenceId": self.sequence_id.get_data()})
        if self.positive_energy_direction is not None:
            msg_data.append({"positiveEnergyDirection": self.positive_energy_direction.get_data()})
        if self.power_unit is not None:
            msg_data.append({"powerUnit": self.power_unit.get_data()})
        if self.energy_unit is not None:
            msg_data.append({"energyUnit": self.energy_unit.get_data()})
        if self.description is not None:
            msg_data.append({"description": self.description.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.sequence_id is not None:
            result_str += f"{sep}sequenceId: {self.sequence_id}"
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
        if self.description is not None:
            result_str += f"{sep}description: {self.description}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                sequence_id=data_dict.get('sequenceId'),
                positive_energy_direction=data_dict.get('positiveEnergyDirection'),
                power_unit=data_dict.get('powerUnit'),
                energy_unit=data_dict.get('energyUnit'),
                description=data_dict.get('description'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class OperatingConstraintsInterruptListDataType:
    def __init__(
            self,
            operating_constraints_interrupt_data: list[OperatingConstraintsInterruptDataType] = None,
    ):
        super().__init__()
        
        self.operating_constraints_interrupt_data = operating_constraints_interrupt_data

        if not isinstance(self.operating_constraints_interrupt_data, list | NoneType):
            raise TypeError("operating_constraints_interrupt_data is not of type list[OperatingConstraintsInterruptDataType]")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.operating_constraints_interrupt_data is not None:
            msg_data.append({"operatingConstraintsInterruptData": [d.get_data() for d in self.operating_constraints_interrupt_data]})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.operating_constraints_interrupt_data is not None:
            result_str += f"{sep}operatingConstraintsInterruptData: {self.operating_constraints_interrupt_data}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                operating_constraints_interrupt_data=data_dict.get('operatingConstraintsInterruptData'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class OperatingConstraintsInterruptListDataSelectorsType:
    def __init__(
            self,
            sequence_id: PowerSequenceIdType = None,
    ):
        super().__init__()
        
        self.sequence_id = sequence_id

        if not isinstance(self.sequence_id, PowerSequenceIdType | NoneType):
            raise TypeError("sequence_id is not of type PowerSequenceIdType")
        
    def get_data(self): # ComplexType

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


class OperatingConstraintsInterruptDataElementsType:
    def __init__(
            self,
            sequence_id: ElementTagType = None,
            is_pausable: ElementTagType = None,
            is_stoppable: ElementTagType = None,
            not_interruptible_at_high_power: ElementTagType = None,
            max_cycles_per_day: ElementTagType = None,
    ):
        super().__init__()
        
        self.sequence_id = sequence_id
        self.is_pausable = is_pausable
        self.is_stoppable = is_stoppable
        self.not_interruptible_at_high_power = not_interruptible_at_high_power
        self.max_cycles_per_day = max_cycles_per_day

        if not isinstance(self.sequence_id, ElementTagType | NoneType):
            raise TypeError("sequence_id is not of type ElementTagType")
        
        if not isinstance(self.is_pausable, ElementTagType | NoneType):
            raise TypeError("is_pausable is not of type ElementTagType")
        
        if not isinstance(self.is_stoppable, ElementTagType | NoneType):
            raise TypeError("is_stoppable is not of type ElementTagType")
        
        if not isinstance(self.not_interruptible_at_high_power, ElementTagType | NoneType):
            raise TypeError("not_interruptible_at_high_power is not of type ElementTagType")
        
        if not isinstance(self.max_cycles_per_day, ElementTagType | NoneType):
            raise TypeError("max_cycles_per_day is not of type ElementTagType")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.sequence_id is not None:
            msg_data.append({"sequenceId": self.sequence_id.get_data()})
        if self.is_pausable is not None:
            msg_data.append({"isPausable": self.is_pausable.get_data()})
        if self.is_stoppable is not None:
            msg_data.append({"isStoppable": self.is_stoppable.get_data()})
        if self.not_interruptible_at_high_power is not None:
            msg_data.append({"notInterruptibleAtHighPower": self.not_interruptible_at_high_power.get_data()})
        if self.max_cycles_per_day is not None:
            msg_data.append({"maxCyclesPerDay": self.max_cycles_per_day.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.sequence_id is not None:
            result_str += f"{sep}sequenceId: {self.sequence_id}"
            sep = ", "
        if self.is_pausable is not None:
            result_str += f"{sep}isPausable: {self.is_pausable}"
            sep = ", "
        if self.is_stoppable is not None:
            result_str += f"{sep}isStoppable: {self.is_stoppable}"
            sep = ", "
        if self.not_interruptible_at_high_power is not None:
            result_str += f"{sep}notInterruptibleAtHighPower: {self.not_interruptible_at_high_power}"
            sep = ", "
        if self.max_cycles_per_day is not None:
            result_str += f"{sep}maxCyclesPerDay: {self.max_cycles_per_day}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                sequence_id=data_dict.get('sequenceId'),
                is_pausable=data_dict.get('isPausable'),
                is_stoppable=data_dict.get('isStoppable'),
                not_interruptible_at_high_power=data_dict.get('notInterruptibleAtHighPower'),
                max_cycles_per_day=data_dict.get('maxCyclesPerDay'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class OperatingConstraintsDurationListDataType:
    def __init__(
            self,
            operating_constraints_duration_data: list[OperatingConstraintsDurationDataType] = None,
    ):
        super().__init__()
        
        self.operating_constraints_duration_data = operating_constraints_duration_data

        if not isinstance(self.operating_constraints_duration_data, list | NoneType):
            raise TypeError("operating_constraints_duration_data is not of type list[OperatingConstraintsDurationDataType]")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.operating_constraints_duration_data is not None:
            msg_data.append({"operatingConstraintsDurationData": [d.get_data() for d in self.operating_constraints_duration_data]})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.operating_constraints_duration_data is not None:
            result_str += f"{sep}operatingConstraintsDurationData: {self.operating_constraints_duration_data}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                operating_constraints_duration_data=data_dict.get('operatingConstraintsDurationData'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class OperatingConstraintsDurationListDataSelectorsType:
    def __init__(
            self,
            sequence_id: PowerSequenceIdType = None,
    ):
        super().__init__()
        
        self.sequence_id = sequence_id

        if not isinstance(self.sequence_id, PowerSequenceIdType | NoneType):
            raise TypeError("sequence_id is not of type PowerSequenceIdType")
        
    def get_data(self): # ComplexType

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


class OperatingConstraintsDurationDataElementsType:
    def __init__(
            self,
            sequence_id: ElementTagType = None,
            active_duration_min: ElementTagType = None,
            active_duration_max: ElementTagType = None,
            pause_duration_min: ElementTagType = None,
            pause_duration_max: ElementTagType = None,
            active_duration_sum_min: ElementTagType = None,
            active_duration_sum_max: ElementTagType = None,
    ):
        super().__init__()
        
        self.sequence_id = sequence_id
        self.active_duration_min = active_duration_min
        self.active_duration_max = active_duration_max
        self.pause_duration_min = pause_duration_min
        self.pause_duration_max = pause_duration_max
        self.active_duration_sum_min = active_duration_sum_min
        self.active_duration_sum_max = active_duration_sum_max

        if not isinstance(self.sequence_id, ElementTagType | NoneType):
            raise TypeError("sequence_id is not of type ElementTagType")
        
        if not isinstance(self.active_duration_min, ElementTagType | NoneType):
            raise TypeError("active_duration_min is not of type ElementTagType")
        
        if not isinstance(self.active_duration_max, ElementTagType | NoneType):
            raise TypeError("active_duration_max is not of type ElementTagType")
        
        if not isinstance(self.pause_duration_min, ElementTagType | NoneType):
            raise TypeError("pause_duration_min is not of type ElementTagType")
        
        if not isinstance(self.pause_duration_max, ElementTagType | NoneType):
            raise TypeError("pause_duration_max is not of type ElementTagType")
        
        if not isinstance(self.active_duration_sum_min, ElementTagType | NoneType):
            raise TypeError("active_duration_sum_min is not of type ElementTagType")
        
        if not isinstance(self.active_duration_sum_max, ElementTagType | NoneType):
            raise TypeError("active_duration_sum_max is not of type ElementTagType")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.sequence_id is not None:
            msg_data.append({"sequenceId": self.sequence_id.get_data()})
        if self.active_duration_min is not None:
            msg_data.append({"activeDurationMin": self.active_duration_min.get_data()})
        if self.active_duration_max is not None:
            msg_data.append({"activeDurationMax": self.active_duration_max.get_data()})
        if self.pause_duration_min is not None:
            msg_data.append({"pauseDurationMin": self.pause_duration_min.get_data()})
        if self.pause_duration_max is not None:
            msg_data.append({"pauseDurationMax": self.pause_duration_max.get_data()})
        if self.active_duration_sum_min is not None:
            msg_data.append({"activeDurationSumMin": self.active_duration_sum_min.get_data()})
        if self.active_duration_sum_max is not None:
            msg_data.append({"activeDurationSumMax": self.active_duration_sum_max.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.sequence_id is not None:
            result_str += f"{sep}sequenceId: {self.sequence_id}"
            sep = ", "
        if self.active_duration_min is not None:
            result_str += f"{sep}activeDurationMin: {self.active_duration_min}"
            sep = ", "
        if self.active_duration_max is not None:
            result_str += f"{sep}activeDurationMax: {self.active_duration_max}"
            sep = ", "
        if self.pause_duration_min is not None:
            result_str += f"{sep}pauseDurationMin: {self.pause_duration_min}"
            sep = ", "
        if self.pause_duration_max is not None:
            result_str += f"{sep}pauseDurationMax: {self.pause_duration_max}"
            sep = ", "
        if self.active_duration_sum_min is not None:
            result_str += f"{sep}activeDurationSumMin: {self.active_duration_sum_min}"
            sep = ", "
        if self.active_duration_sum_max is not None:
            result_str += f"{sep}activeDurationSumMax: {self.active_duration_sum_max}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                sequence_id=data_dict.get('sequenceId'),
                active_duration_min=data_dict.get('activeDurationMin'),
                active_duration_max=data_dict.get('activeDurationMax'),
                pause_duration_min=data_dict.get('pauseDurationMin'),
                pause_duration_max=data_dict.get('pauseDurationMax'),
                active_duration_sum_min=data_dict.get('activeDurationSumMin'),
                active_duration_sum_max=data_dict.get('activeDurationSumMax'),
            )
        elif data:
            return cls(data)
        else:
            return cls()



