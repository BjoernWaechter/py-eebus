# Jinja Template message_type.py.jinja2
from spine.base_type.commondatatypes import ElementTagType
from spine.base_type.commondatatypes import ScaledNumberElementsType
from spine.base_type.commondatatypes import ScaledNumberSetElementsType
from spine.base_type.commondatatypes import ScaledNumberSetType
from spine.base_type.commondatatypes import ScaledNumberType
from spine.simple_type.commondatatypes import DescriptionType
from spine.simple_type.commondatatypes import LabelType
from spine.simple_type.electricalconnection import ElectricalConnectionCharacteristicIdType
from spine.simple_type.electricalconnection import ElectricalConnectionIdType
from spine.simple_type.electricalconnection import ElectricalConnectionParameterIdType
from spine.simple_type.measurement import MeasurementIdType
from spine.union_type.commondatatypes import AbsoluteOrRelativeTimeType
from spine.union_type.commondatatypes import EnergyDirectionType
from spine.union_type.commondatatypes import EnergyModeType
from spine.union_type.commondatatypes import ScopeTypeType
from spine.union_type.commondatatypes import UnitOfMeasurementType
from spine.union_type.electricalconnection import ElectricalConnectionAcMeasurementTypeType
from spine.union_type.electricalconnection import ElectricalConnectionCharacteristicContextType
from spine.union_type.electricalconnection import ElectricalConnectionCharacteristicTypeType
from spine.union_type.electricalconnection import ElectricalConnectionMeasurandVariantType
from spine.union_type.electricalconnection import ElectricalConnectionPhaseNameType
from spine.union_type.electricalconnection import ElectricalConnectionVoltageTypeType
from types import NoneType
from spine import array_2_dict


class ElectricalConnectionStateDataType: # EEBus_SPINE_TS_ElectricalConnection.xsd:ns_p:ElectricalConnectionStateDataType -> ComplexType
    def __init__(
            self,
            electrical_connection_id: ElectricalConnectionIdType = None,
            timestamp: AbsoluteOrRelativeTimeType = None,
            current_energy_mode: EnergyModeType = None,
            consumption_time: str = None,
            production_time: str = None,
            total_consumption_time: str = None,
            total_production_time: str = None,
    ):
        super().__init__()
        
        self.electrical_connection_id = electrical_connection_id
        self.timestamp = timestamp
        self.current_energy_mode = current_energy_mode
        self.consumption_time = consumption_time
        self.production_time = production_time
        self.total_consumption_time = total_consumption_time
        self.total_production_time = total_production_time

        if not isinstance(self.electrical_connection_id, ElectricalConnectionIdType | NoneType):
            raise TypeError("electrical_connection_id is not of type ElectricalConnectionIdType")
        
        if not isinstance(self.timestamp, AbsoluteOrRelativeTimeType | NoneType):
            raise TypeError("timestamp is not of type AbsoluteOrRelativeTimeType")
        
        if not isinstance(self.current_energy_mode, EnergyModeType | NoneType):
            raise TypeError("current_energy_mode is not of type EnergyModeType")
        
        if not isinstance(self.consumption_time, str | NoneType):
            raise TypeError("consumption_time is not of type str")
        
        if not isinstance(self.production_time, str | NoneType):
            raise TypeError("production_time is not of type str")
        
        if not isinstance(self.total_consumption_time, str | NoneType):
            raise TypeError("total_consumption_time is not of type str")
        
        if not isinstance(self.total_production_time, str | NoneType):
            raise TypeError("total_production_time is not of type str")
        
    def get_data(self):

        msg_data = []
        
        if self.electrical_connection_id is not None:
            msg_data.append({"electricalConnectionId": self.electrical_connection_id.get_data()})
        if self.timestamp is not None:
            msg_data.append({"timestamp": self.timestamp.get_data()})
        if self.current_energy_mode is not None:
            msg_data.append({"currentEnergyMode": self.current_energy_mode.get_data()})
        if self.consumption_time is not None:
            msg_data.append({"consumptionTime": self.consumption_time})
        if self.production_time is not None:
            msg_data.append({"productionTime": self.production_time})
        if self.total_consumption_time is not None:
            msg_data.append({"totalConsumptionTime": self.total_consumption_time})
        if self.total_production_time is not None:
            msg_data.append({"totalProductionTime": self.total_production_time})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.electrical_connection_id is not None:
            result_str += f"{sep}electricalConnectionId: {self.electrical_connection_id}"
            sep = ", "
        if self.timestamp is not None:
            result_str += f"{sep}timestamp: {self.timestamp}"
            sep = ", "
        if self.current_energy_mode is not None:
            result_str += f"{sep}currentEnergyMode: {self.current_energy_mode}"
            sep = ", "
        if self.consumption_time is not None:
            result_str += f"{sep}consumptionTime: {self.consumption_time}"
            sep = ", "
        if self.production_time is not None:
            result_str += f"{sep}productionTime: {self.production_time}"
            sep = ", "
        if self.total_consumption_time is not None:
            result_str += f"{sep}totalConsumptionTime: {self.total_consumption_time}"
            sep = ", "
        if self.total_production_time is not None:
            result_str += f"{sep}totalProductionTime: {self.total_production_time}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                electrical_connection_id=data_dict.get('electricalConnectionId'),
                timestamp=data_dict.get('timestamp'),
                current_energy_mode=data_dict.get('currentEnergyMode'),
                consumption_time=data_dict.get('consumptionTime'),
                production_time=data_dict.get('productionTime'),
                total_consumption_time=data_dict.get('totalConsumptionTime'),
                total_production_time=data_dict.get('totalProductionTime'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class ElectricalConnectionPermittedValueSetDataType: # EEBus_SPINE_TS_ElectricalConnection.xsd:ns_p:ElectricalConnectionPermittedValueSetDataType -> ComplexType
    def __init__(
            self,
            electrical_connection_id: ElectricalConnectionIdType = None,
            parameter_id: ElectricalConnectionParameterIdType = None,
            permitted_value_set: list[ScaledNumberSetType] = None,
    ):
        super().__init__()
        
        self.electrical_connection_id = electrical_connection_id
        self.parameter_id = parameter_id
        self.permitted_value_set = permitted_value_set

        if not isinstance(self.electrical_connection_id, ElectricalConnectionIdType | NoneType):
            raise TypeError("electrical_connection_id is not of type ElectricalConnectionIdType")
        
        if not isinstance(self.parameter_id, ElectricalConnectionParameterIdType | NoneType):
            raise TypeError("parameter_id is not of type ElectricalConnectionParameterIdType")
        
        if not isinstance(self.permitted_value_set, list | NoneType):
            raise TypeError("permitted_value_set is not of type list[ScaledNumberSetType]")
        
    def get_data(self):

        msg_data = []
        
        if self.electrical_connection_id is not None:
            msg_data.append({"electricalConnectionId": self.electrical_connection_id.get_data()})
        if self.parameter_id is not None:
            msg_data.append({"parameterId": self.parameter_id.get_data()})
        if self.permitted_value_set is not None:
            msg_data.append({"permittedValueSet": [d.get_data() for d in self.permitted_value_set]})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.electrical_connection_id is not None:
            result_str += f"{sep}electricalConnectionId: {self.electrical_connection_id}"
            sep = ", "
        if self.parameter_id is not None:
            result_str += f"{sep}parameterId: {self.parameter_id}"
            sep = ", "
        if self.permitted_value_set is not None:
            result_str += f"{sep}permittedValueSet: {self.permitted_value_set}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                electrical_connection_id=data_dict.get('electricalConnectionId'),
                parameter_id=data_dict.get('parameterId'),
                permitted_value_set=data_dict.get('permittedValueSet'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class ElectricalConnectionParameterDescriptionDataType: # EEBus_SPINE_TS_ElectricalConnection.xsd:ns_p:ElectricalConnectionParameterDescriptionDataType -> ComplexType
    def __init__(
            self,
            electrical_connection_id: ElectricalConnectionIdType = None,
            parameter_id: ElectricalConnectionParameterIdType = None,
            measurement_id: MeasurementIdType = None,
            voltage_type: ElectricalConnectionVoltageTypeType = None,
            ac_measured_phases: ElectricalConnectionPhaseNameType = None,
            ac_measured_in_reference_to: ElectricalConnectionPhaseNameType = None,
            ac_measurement_type: ElectricalConnectionAcMeasurementTypeType = None,
            ac_measurement_variant: ElectricalConnectionMeasurandVariantType = None,
            ac_measured_harmonic: int = None,
            scope_type: ScopeTypeType = None,
            label: LabelType = None,
            description: DescriptionType = None,
    ):
        super().__init__()
        
        self.electrical_connection_id = electrical_connection_id
        self.parameter_id = parameter_id
        self.measurement_id = measurement_id
        self.voltage_type = voltage_type
        self.ac_measured_phases = ac_measured_phases
        self.ac_measured_in_reference_to = ac_measured_in_reference_to
        self.ac_measurement_type = ac_measurement_type
        self.ac_measurement_variant = ac_measurement_variant
        self.ac_measured_harmonic = ac_measured_harmonic
        self.scope_type = scope_type
        self.label = label
        self.description = description

        if not isinstance(self.electrical_connection_id, ElectricalConnectionIdType | NoneType):
            raise TypeError("electrical_connection_id is not of type ElectricalConnectionIdType")
        
        if not isinstance(self.parameter_id, ElectricalConnectionParameterIdType | NoneType):
            raise TypeError("parameter_id is not of type ElectricalConnectionParameterIdType")
        
        if not isinstance(self.measurement_id, MeasurementIdType | NoneType):
            raise TypeError("measurement_id is not of type MeasurementIdType")
        
        if not isinstance(self.voltage_type, ElectricalConnectionVoltageTypeType | NoneType):
            raise TypeError("voltage_type is not of type ElectricalConnectionVoltageTypeType")
        
        if not isinstance(self.ac_measured_phases, ElectricalConnectionPhaseNameType | NoneType):
            raise TypeError("ac_measured_phases is not of type ElectricalConnectionPhaseNameType")
        
        if not isinstance(self.ac_measured_in_reference_to, ElectricalConnectionPhaseNameType | NoneType):
            raise TypeError("ac_measured_in_reference_to is not of type ElectricalConnectionPhaseNameType")
        
        if not isinstance(self.ac_measurement_type, ElectricalConnectionAcMeasurementTypeType | NoneType):
            raise TypeError("ac_measurement_type is not of type ElectricalConnectionAcMeasurementTypeType")
        
        if not isinstance(self.ac_measurement_variant, ElectricalConnectionMeasurandVariantType | NoneType):
            raise TypeError("ac_measurement_variant is not of type ElectricalConnectionMeasurandVariantType")
        
        if not isinstance(self.ac_measured_harmonic, int | NoneType):
            raise TypeError("ac_measured_harmonic is not of type int")
        
        if not isinstance(self.scope_type, ScopeTypeType | NoneType):
            raise TypeError("scope_type is not of type ScopeTypeType")
        
        if not isinstance(self.label, LabelType | NoneType):
            raise TypeError("label is not of type LabelType")
        
        if not isinstance(self.description, DescriptionType | NoneType):
            raise TypeError("description is not of type DescriptionType")
        
    def get_data(self):

        msg_data = []
        
        if self.electrical_connection_id is not None:
            msg_data.append({"electricalConnectionId": self.electrical_connection_id.get_data()})
        if self.parameter_id is not None:
            msg_data.append({"parameterId": self.parameter_id.get_data()})
        if self.measurement_id is not None:
            msg_data.append({"measurementId": self.measurement_id.get_data()})
        if self.voltage_type is not None:
            msg_data.append({"voltageType": self.voltage_type.get_data()})
        if self.ac_measured_phases is not None:
            msg_data.append({"acMeasuredPhases": self.ac_measured_phases.get_data()})
        if self.ac_measured_in_reference_to is not None:
            msg_data.append({"acMeasuredInReferenceTo": self.ac_measured_in_reference_to.get_data()})
        if self.ac_measurement_type is not None:
            msg_data.append({"acMeasurementType": self.ac_measurement_type.get_data()})
        if self.ac_measurement_variant is not None:
            msg_data.append({"acMeasurementVariant": self.ac_measurement_variant.get_data()})
        if self.ac_measured_harmonic is not None:
            msg_data.append({"acMeasuredHarmonic": self.ac_measured_harmonic})
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
        if self.electrical_connection_id is not None:
            result_str += f"{sep}electricalConnectionId: {self.electrical_connection_id}"
            sep = ", "
        if self.parameter_id is not None:
            result_str += f"{sep}parameterId: {self.parameter_id}"
            sep = ", "
        if self.measurement_id is not None:
            result_str += f"{sep}measurementId: {self.measurement_id}"
            sep = ", "
        if self.voltage_type is not None:
            result_str += f"{sep}voltageType: {self.voltage_type}"
            sep = ", "
        if self.ac_measured_phases is not None:
            result_str += f"{sep}acMeasuredPhases: {self.ac_measured_phases}"
            sep = ", "
        if self.ac_measured_in_reference_to is not None:
            result_str += f"{sep}acMeasuredInReferenceTo: {self.ac_measured_in_reference_to}"
            sep = ", "
        if self.ac_measurement_type is not None:
            result_str += f"{sep}acMeasurementType: {self.ac_measurement_type}"
            sep = ", "
        if self.ac_measurement_variant is not None:
            result_str += f"{sep}acMeasurementVariant: {self.ac_measurement_variant}"
            sep = ", "
        if self.ac_measured_harmonic is not None:
            result_str += f"{sep}acMeasuredHarmonic: {self.ac_measured_harmonic}"
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
                electrical_connection_id=data_dict.get('electricalConnectionId'),
                parameter_id=data_dict.get('parameterId'),
                measurement_id=data_dict.get('measurementId'),
                voltage_type=data_dict.get('voltageType'),
                ac_measured_phases=data_dict.get('acMeasuredPhases'),
                ac_measured_in_reference_to=data_dict.get('acMeasuredInReferenceTo'),
                ac_measurement_type=data_dict.get('acMeasurementType'),
                ac_measurement_variant=data_dict.get('acMeasurementVariant'),
                ac_measured_harmonic=data_dict.get('acMeasuredHarmonic'),
                scope_type=data_dict.get('scopeType'),
                label=data_dict.get('label'),
                description=data_dict.get('description'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class ElectricalConnectionDescriptionDataType: # EEBus_SPINE_TS_ElectricalConnection.xsd:ns_p:ElectricalConnectionDescriptionDataType -> ComplexType
    def __init__(
            self,
            electrical_connection_id: ElectricalConnectionIdType = None,
            power_supply_type: ElectricalConnectionVoltageTypeType = None,
            ac_connected_phases: int = None,
            ac_rms_period_duration: str = None,
            positive_energy_direction: EnergyDirectionType = None,
            scope_type: ScopeTypeType = None,
            label: LabelType = None,
            description: DescriptionType = None,
    ):
        super().__init__()
        
        self.electrical_connection_id = electrical_connection_id
        self.power_supply_type = power_supply_type
        self.ac_connected_phases = ac_connected_phases
        self.ac_rms_period_duration = ac_rms_period_duration
        self.positive_energy_direction = positive_energy_direction
        self.scope_type = scope_type
        self.label = label
        self.description = description

        if not isinstance(self.electrical_connection_id, ElectricalConnectionIdType | NoneType):
            raise TypeError("electrical_connection_id is not of type ElectricalConnectionIdType")
        
        if not isinstance(self.power_supply_type, ElectricalConnectionVoltageTypeType | NoneType):
            raise TypeError("power_supply_type is not of type ElectricalConnectionVoltageTypeType")
        
        if not isinstance(self.ac_connected_phases, int | NoneType):
            raise TypeError("ac_connected_phases is not of type int")
        
        if not isinstance(self.ac_rms_period_duration, str | NoneType):
            raise TypeError("ac_rms_period_duration is not of type str")
        
        if not isinstance(self.positive_energy_direction, EnergyDirectionType | NoneType):
            raise TypeError("positive_energy_direction is not of type EnergyDirectionType")
        
        if not isinstance(self.scope_type, ScopeTypeType | NoneType):
            raise TypeError("scope_type is not of type ScopeTypeType")
        
        if not isinstance(self.label, LabelType | NoneType):
            raise TypeError("label is not of type LabelType")
        
        if not isinstance(self.description, DescriptionType | NoneType):
            raise TypeError("description is not of type DescriptionType")
        
    def get_data(self):

        msg_data = []
        
        if self.electrical_connection_id is not None:
            msg_data.append({"electricalConnectionId": self.electrical_connection_id.get_data()})
        if self.power_supply_type is not None:
            msg_data.append({"powerSupplyType": self.power_supply_type.get_data()})
        if self.ac_connected_phases is not None:
            msg_data.append({"acConnectedPhases": self.ac_connected_phases})
        if self.ac_rms_period_duration is not None:
            msg_data.append({"acRmsPeriodDuration": self.ac_rms_period_duration})
        if self.positive_energy_direction is not None:
            msg_data.append({"positiveEnergyDirection": self.positive_energy_direction.get_data()})
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
        if self.electrical_connection_id is not None:
            result_str += f"{sep}electricalConnectionId: {self.electrical_connection_id}"
            sep = ", "
        if self.power_supply_type is not None:
            result_str += f"{sep}powerSupplyType: {self.power_supply_type}"
            sep = ", "
        if self.ac_connected_phases is not None:
            result_str += f"{sep}acConnectedPhases: {self.ac_connected_phases}"
            sep = ", "
        if self.ac_rms_period_duration is not None:
            result_str += f"{sep}acRmsPeriodDuration: {self.ac_rms_period_duration}"
            sep = ", "
        if self.positive_energy_direction is not None:
            result_str += f"{sep}positiveEnergyDirection: {self.positive_energy_direction}"
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
                electrical_connection_id=data_dict.get('electricalConnectionId'),
                power_supply_type=data_dict.get('powerSupplyType'),
                ac_connected_phases=data_dict.get('acConnectedPhases'),
                ac_rms_period_duration=data_dict.get('acRmsPeriodDuration'),
                positive_energy_direction=data_dict.get('positiveEnergyDirection'),
                scope_type=data_dict.get('scopeType'),
                label=data_dict.get('label'),
                description=data_dict.get('description'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class ElectricalConnectionCharacteristicDataType: # EEBus_SPINE_TS_ElectricalConnection.xsd:ns_p:ElectricalConnectionCharacteristicDataType -> ComplexType
    def __init__(
            self,
            electrical_connection_id: ElectricalConnectionIdType = None,
            parameter_id: ElectricalConnectionParameterIdType = None,
            characteristic_id: ElectricalConnectionCharacteristicIdType = None,
            characteristic_context: ElectricalConnectionCharacteristicContextType = None,
            characteristic_type: ElectricalConnectionCharacteristicTypeType = None,
            value: ScaledNumberType = None,
            unit: UnitOfMeasurementType = None,
    ):
        super().__init__()
        
        self.electrical_connection_id = electrical_connection_id
        self.parameter_id = parameter_id
        self.characteristic_id = characteristic_id
        self.characteristic_context = characteristic_context
        self.characteristic_type = characteristic_type
        self.value = value
        self.unit = unit

        if not isinstance(self.electrical_connection_id, ElectricalConnectionIdType | NoneType):
            raise TypeError("electrical_connection_id is not of type ElectricalConnectionIdType")
        
        if not isinstance(self.parameter_id, ElectricalConnectionParameterIdType | NoneType):
            raise TypeError("parameter_id is not of type ElectricalConnectionParameterIdType")
        
        if not isinstance(self.characteristic_id, ElectricalConnectionCharacteristicIdType | NoneType):
            raise TypeError("characteristic_id is not of type ElectricalConnectionCharacteristicIdType")
        
        if not isinstance(self.characteristic_context, ElectricalConnectionCharacteristicContextType | NoneType):
            raise TypeError("characteristic_context is not of type ElectricalConnectionCharacteristicContextType")
        
        if not isinstance(self.characteristic_type, ElectricalConnectionCharacteristicTypeType | NoneType):
            raise TypeError("characteristic_type is not of type ElectricalConnectionCharacteristicTypeType")
        
        if not isinstance(self.value, ScaledNumberType | NoneType):
            raise TypeError("value is not of type ScaledNumberType")
        
        if not isinstance(self.unit, UnitOfMeasurementType | NoneType):
            raise TypeError("unit is not of type UnitOfMeasurementType")
        
    def get_data(self):

        msg_data = []
        
        if self.electrical_connection_id is not None:
            msg_data.append({"electricalConnectionId": self.electrical_connection_id.get_data()})
        if self.parameter_id is not None:
            msg_data.append({"parameterId": self.parameter_id.get_data()})
        if self.characteristic_id is not None:
            msg_data.append({"characteristicId": self.characteristic_id.get_data()})
        if self.characteristic_context is not None:
            msg_data.append({"characteristicContext": self.characteristic_context.get_data()})
        if self.characteristic_type is not None:
            msg_data.append({"characteristicType": self.characteristic_type.get_data()})
        if self.value is not None:
            msg_data.append({"value": self.value.get_data()})
        if self.unit is not None:
            msg_data.append({"unit": self.unit.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.electrical_connection_id is not None:
            result_str += f"{sep}electricalConnectionId: {self.electrical_connection_id}"
            sep = ", "
        if self.parameter_id is not None:
            result_str += f"{sep}parameterId: {self.parameter_id}"
            sep = ", "
        if self.characteristic_id is not None:
            result_str += f"{sep}characteristicId: {self.characteristic_id}"
            sep = ", "
        if self.characteristic_context is not None:
            result_str += f"{sep}characteristicContext: {self.characteristic_context}"
            sep = ", "
        if self.characteristic_type is not None:
            result_str += f"{sep}characteristicType: {self.characteristic_type}"
            sep = ", "
        if self.value is not None:
            result_str += f"{sep}value: {self.value}"
            sep = ", "
        if self.unit is not None:
            result_str += f"{sep}unit: {self.unit}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                electrical_connection_id=data_dict.get('electricalConnectionId'),
                parameter_id=data_dict.get('parameterId'),
                characteristic_id=data_dict.get('characteristicId'),
                characteristic_context=data_dict.get('characteristicContext'),
                characteristic_type=data_dict.get('characteristicType'),
                value=data_dict.get('value'),
                unit=data_dict.get('unit'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class ElectricalConnectionStateListDataType: # EEBus_SPINE_TS_ElectricalConnection.xsd:ns_p:ElectricalConnectionStateListDataType -> ComplexType
    def __init__(
            self,
            electrical_connection_state_data: list[ElectricalConnectionStateDataType] = None,
    ):
        super().__init__()
        
        self.electrical_connection_state_data = electrical_connection_state_data

        if not isinstance(self.electrical_connection_state_data, list | NoneType):
            raise TypeError("electrical_connection_state_data is not of type list[ElectricalConnectionStateDataType]")
        
    def get_data(self):

        msg_data = []
        
        if self.electrical_connection_state_data is not None:
            msg_data.append({"electricalConnectionStateData": [d.get_data() for d in self.electrical_connection_state_data]})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.electrical_connection_state_data is not None:
            result_str += f"{sep}electricalConnectionStateData: {self.electrical_connection_state_data}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                electrical_connection_state_data=data_dict.get('electricalConnectionStateData'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class ElectricalConnectionPermittedValueSetListDataType: # EEBus_SPINE_TS_ElectricalConnection.xsd:ns_p:ElectricalConnectionPermittedValueSetListDataType -> ComplexType
    def __init__(
            self,
            electrical_connection_permitted_value_set_data: list[ElectricalConnectionPermittedValueSetDataType] = None,
    ):
        super().__init__()
        
        self.electrical_connection_permitted_value_set_data = electrical_connection_permitted_value_set_data

        if not isinstance(self.electrical_connection_permitted_value_set_data, list | NoneType):
            raise TypeError("electrical_connection_permitted_value_set_data is not of type list[ElectricalConnectionPermittedValueSetDataType]")
        
    def get_data(self):

        msg_data = []
        
        if self.electrical_connection_permitted_value_set_data is not None:
            msg_data.append({"electricalConnectionPermittedValueSetData": [d.get_data() for d in self.electrical_connection_permitted_value_set_data]})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.electrical_connection_permitted_value_set_data is not None:
            result_str += f"{sep}electricalConnectionPermittedValueSetData: {self.electrical_connection_permitted_value_set_data}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                electrical_connection_permitted_value_set_data=data_dict.get('electricalConnectionPermittedValueSetData'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class ElectricalConnectionParameterDescriptionListDataType: # EEBus_SPINE_TS_ElectricalConnection.xsd:ns_p:ElectricalConnectionParameterDescriptionListDataType -> ComplexType
    def __init__(
            self,
            electrical_connection_parameter_description_data: list[ElectricalConnectionParameterDescriptionDataType] = None,
    ):
        super().__init__()
        
        self.electrical_connection_parameter_description_data = electrical_connection_parameter_description_data

        if not isinstance(self.electrical_connection_parameter_description_data, list | NoneType):
            raise TypeError("electrical_connection_parameter_description_data is not of type list[ElectricalConnectionParameterDescriptionDataType]")
        
    def get_data(self):

        msg_data = []
        
        if self.electrical_connection_parameter_description_data is not None:
            msg_data.append({"electricalConnectionParameterDescriptionData": [d.get_data() for d in self.electrical_connection_parameter_description_data]})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.electrical_connection_parameter_description_data is not None:
            result_str += f"{sep}electricalConnectionParameterDescriptionData: {self.electrical_connection_parameter_description_data}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                electrical_connection_parameter_description_data=data_dict.get('electricalConnectionParameterDescriptionData'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class ElectricalConnectionDescriptionListDataType: # EEBus_SPINE_TS_ElectricalConnection.xsd:ns_p:ElectricalConnectionDescriptionListDataType -> ComplexType
    def __init__(
            self,
            electrical_connection_description_data: list[ElectricalConnectionDescriptionDataType] = None,
    ):
        super().__init__()
        
        self.electrical_connection_description_data = electrical_connection_description_data

        if not isinstance(self.electrical_connection_description_data, list | NoneType):
            raise TypeError("electrical_connection_description_data is not of type list[ElectricalConnectionDescriptionDataType]")
        
    def get_data(self):

        msg_data = []
        
        if self.electrical_connection_description_data is not None:
            msg_data.append({"electricalConnectionDescriptionData": [d.get_data() for d in self.electrical_connection_description_data]})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.electrical_connection_description_data is not None:
            result_str += f"{sep}electricalConnectionDescriptionData: {self.electrical_connection_description_data}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                electrical_connection_description_data=data_dict.get('electricalConnectionDescriptionData'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class ElectricalConnectionCharacteristicListDataType: # EEBus_SPINE_TS_ElectricalConnection.xsd:ns_p:ElectricalConnectionCharacteristicListDataType -> ComplexType
    def __init__(
            self,
            electrical_connection_characteristic_data: list[ElectricalConnectionCharacteristicDataType] = None,
    ):
        super().__init__()
        
        self.electrical_connection_characteristic_data = electrical_connection_characteristic_data

        if not isinstance(self.electrical_connection_characteristic_data, list | NoneType):
            raise TypeError("electrical_connection_characteristic_data is not of type list[ElectricalConnectionCharacteristicDataType]")
        
    def get_data(self):

        msg_data = []
        
        if self.electrical_connection_characteristic_data is not None:
            msg_data.append({"electricalConnectionCharacteristicData": [d.get_data() for d in self.electrical_connection_characteristic_data]})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.electrical_connection_characteristic_data is not None:
            result_str += f"{sep}electricalConnectionCharacteristicData: {self.electrical_connection_characteristic_data}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                electrical_connection_characteristic_data=data_dict.get('electricalConnectionCharacteristicData'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class ElectricalConnectionStateDataElementsType: # EEBus_SPINE_TS_ElectricalConnection.xsd:ns_p:ElectricalConnectionStateDataElementsType -> ComplexType
    def __init__(
            self,
            electrical_connection_id: ElementTagType = None,
            timestamp: ElementTagType = None,
            current_energy_mode: ElementTagType = None,
            consumption_time: ElementTagType = None,
            production_time: ElementTagType = None,
            total_consumption_time: ElementTagType = None,
            total_production_time: ElementTagType = None,
    ):
        super().__init__()
        
        self.electrical_connection_id = electrical_connection_id
        self.timestamp = timestamp
        self.current_energy_mode = current_energy_mode
        self.consumption_time = consumption_time
        self.production_time = production_time
        self.total_consumption_time = total_consumption_time
        self.total_production_time = total_production_time

        if not isinstance(self.electrical_connection_id, ElementTagType | NoneType):
            raise TypeError("electrical_connection_id is not of type ElementTagType")
        
        if not isinstance(self.timestamp, ElementTagType | NoneType):
            raise TypeError("timestamp is not of type ElementTagType")
        
        if not isinstance(self.current_energy_mode, ElementTagType | NoneType):
            raise TypeError("current_energy_mode is not of type ElementTagType")
        
        if not isinstance(self.consumption_time, ElementTagType | NoneType):
            raise TypeError("consumption_time is not of type ElementTagType")
        
        if not isinstance(self.production_time, ElementTagType | NoneType):
            raise TypeError("production_time is not of type ElementTagType")
        
        if not isinstance(self.total_consumption_time, ElementTagType | NoneType):
            raise TypeError("total_consumption_time is not of type ElementTagType")
        
        if not isinstance(self.total_production_time, ElementTagType | NoneType):
            raise TypeError("total_production_time is not of type ElementTagType")
        
    def get_data(self):

        msg_data = []
        
        if self.electrical_connection_id is not None:
            msg_data.append({"electricalConnectionId": self.electrical_connection_id.get_data()})
        if self.timestamp is not None:
            msg_data.append({"timestamp": self.timestamp.get_data()})
        if self.current_energy_mode is not None:
            msg_data.append({"currentEnergyMode": self.current_energy_mode.get_data()})
        if self.consumption_time is not None:
            msg_data.append({"consumptionTime": self.consumption_time.get_data()})
        if self.production_time is not None:
            msg_data.append({"productionTime": self.production_time.get_data()})
        if self.total_consumption_time is not None:
            msg_data.append({"totalConsumptionTime": self.total_consumption_time.get_data()})
        if self.total_production_time is not None:
            msg_data.append({"totalProductionTime": self.total_production_time.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.electrical_connection_id is not None:
            result_str += f"{sep}electricalConnectionId: {self.electrical_connection_id}"
            sep = ", "
        if self.timestamp is not None:
            result_str += f"{sep}timestamp: {self.timestamp}"
            sep = ", "
        if self.current_energy_mode is not None:
            result_str += f"{sep}currentEnergyMode: {self.current_energy_mode}"
            sep = ", "
        if self.consumption_time is not None:
            result_str += f"{sep}consumptionTime: {self.consumption_time}"
            sep = ", "
        if self.production_time is not None:
            result_str += f"{sep}productionTime: {self.production_time}"
            sep = ", "
        if self.total_consumption_time is not None:
            result_str += f"{sep}totalConsumptionTime: {self.total_consumption_time}"
            sep = ", "
        if self.total_production_time is not None:
            result_str += f"{sep}totalProductionTime: {self.total_production_time}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                electrical_connection_id=data_dict.get('electricalConnectionId'),
                timestamp=data_dict.get('timestamp'),
                current_energy_mode=data_dict.get('currentEnergyMode'),
                consumption_time=data_dict.get('consumptionTime'),
                production_time=data_dict.get('productionTime'),
                total_consumption_time=data_dict.get('totalConsumptionTime'),
                total_production_time=data_dict.get('totalProductionTime'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class ElectricalConnectionPermittedValueSetDataElementsType: # EEBus_SPINE_TS_ElectricalConnection.xsd:ns_p:ElectricalConnectionPermittedValueSetDataElementsType -> ComplexType
    def __init__(
            self,
            electrical_connection_id: ElementTagType = None,
            parameter_id: ElementTagType = None,
            permitted_value_set: ScaledNumberSetElementsType = None,
    ):
        super().__init__()
        
        self.electrical_connection_id = electrical_connection_id
        self.parameter_id = parameter_id
        self.permitted_value_set = permitted_value_set

        if not isinstance(self.electrical_connection_id, ElementTagType | NoneType):
            raise TypeError("electrical_connection_id is not of type ElementTagType")
        
        if not isinstance(self.parameter_id, ElementTagType | NoneType):
            raise TypeError("parameter_id is not of type ElementTagType")
        
        if not isinstance(self.permitted_value_set, ScaledNumberSetElementsType | NoneType):
            raise TypeError("permitted_value_set is not of type ScaledNumberSetElementsType")
        
    def get_data(self):

        msg_data = []
        
        if self.electrical_connection_id is not None:
            msg_data.append({"electricalConnectionId": self.electrical_connection_id.get_data()})
        if self.parameter_id is not None:
            msg_data.append({"parameterId": self.parameter_id.get_data()})
        if self.permitted_value_set is not None:
            msg_data.append({"permittedValueSet": self.permitted_value_set.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.electrical_connection_id is not None:
            result_str += f"{sep}electricalConnectionId: {self.electrical_connection_id}"
            sep = ", "
        if self.parameter_id is not None:
            result_str += f"{sep}parameterId: {self.parameter_id}"
            sep = ", "
        if self.permitted_value_set is not None:
            result_str += f"{sep}permittedValueSet: {self.permitted_value_set}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                electrical_connection_id=data_dict.get('electricalConnectionId'),
                parameter_id=data_dict.get('parameterId'),
                permitted_value_set=data_dict.get('permittedValueSet'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class ElectricalConnectionParameterDescriptionDataElementsType: # EEBus_SPINE_TS_ElectricalConnection.xsd:ns_p:ElectricalConnectionParameterDescriptionDataElementsType -> ComplexType
    def __init__(
            self,
            electrical_connection_id: ElementTagType = None,
            parameter_id: ElementTagType = None,
            measurement_id: ElementTagType = None,
            voltage_type: ElementTagType = None,
            ac_measured_phases: ElementTagType = None,
            ac_measured_in_reference_to: ElementTagType = None,
            ac_measurement_type: ElementTagType = None,
            ac_measurement_variant: ElementTagType = None,
            ac_measured_harmonic: ElementTagType = None,
            scope_type: ElementTagType = None,
            label: ElementTagType = None,
            description: ElementTagType = None,
    ):
        super().__init__()
        
        self.electrical_connection_id = electrical_connection_id
        self.parameter_id = parameter_id
        self.measurement_id = measurement_id
        self.voltage_type = voltage_type
        self.ac_measured_phases = ac_measured_phases
        self.ac_measured_in_reference_to = ac_measured_in_reference_to
        self.ac_measurement_type = ac_measurement_type
        self.ac_measurement_variant = ac_measurement_variant
        self.ac_measured_harmonic = ac_measured_harmonic
        self.scope_type = scope_type
        self.label = label
        self.description = description

        if not isinstance(self.electrical_connection_id, ElementTagType | NoneType):
            raise TypeError("electrical_connection_id is not of type ElementTagType")
        
        if not isinstance(self.parameter_id, ElementTagType | NoneType):
            raise TypeError("parameter_id is not of type ElementTagType")
        
        if not isinstance(self.measurement_id, ElementTagType | NoneType):
            raise TypeError("measurement_id is not of type ElementTagType")
        
        if not isinstance(self.voltage_type, ElementTagType | NoneType):
            raise TypeError("voltage_type is not of type ElementTagType")
        
        if not isinstance(self.ac_measured_phases, ElementTagType | NoneType):
            raise TypeError("ac_measured_phases is not of type ElementTagType")
        
        if not isinstance(self.ac_measured_in_reference_to, ElementTagType | NoneType):
            raise TypeError("ac_measured_in_reference_to is not of type ElementTagType")
        
        if not isinstance(self.ac_measurement_type, ElementTagType | NoneType):
            raise TypeError("ac_measurement_type is not of type ElementTagType")
        
        if not isinstance(self.ac_measurement_variant, ElementTagType | NoneType):
            raise TypeError("ac_measurement_variant is not of type ElementTagType")
        
        if not isinstance(self.ac_measured_harmonic, ElementTagType | NoneType):
            raise TypeError("ac_measured_harmonic is not of type ElementTagType")
        
        if not isinstance(self.scope_type, ElementTagType | NoneType):
            raise TypeError("scope_type is not of type ElementTagType")
        
        if not isinstance(self.label, ElementTagType | NoneType):
            raise TypeError("label is not of type ElementTagType")
        
        if not isinstance(self.description, ElementTagType | NoneType):
            raise TypeError("description is not of type ElementTagType")
        
    def get_data(self):

        msg_data = []
        
        if self.electrical_connection_id is not None:
            msg_data.append({"electricalConnectionId": self.electrical_connection_id.get_data()})
        if self.parameter_id is not None:
            msg_data.append({"parameterId": self.parameter_id.get_data()})
        if self.measurement_id is not None:
            msg_data.append({"measurementId": self.measurement_id.get_data()})
        if self.voltage_type is not None:
            msg_data.append({"voltageType": self.voltage_type.get_data()})
        if self.ac_measured_phases is not None:
            msg_data.append({"acMeasuredPhases": self.ac_measured_phases.get_data()})
        if self.ac_measured_in_reference_to is not None:
            msg_data.append({"acMeasuredInReferenceTo": self.ac_measured_in_reference_to.get_data()})
        if self.ac_measurement_type is not None:
            msg_data.append({"acMeasurementType": self.ac_measurement_type.get_data()})
        if self.ac_measurement_variant is not None:
            msg_data.append({"acMeasurementVariant": self.ac_measurement_variant.get_data()})
        if self.ac_measured_harmonic is not None:
            msg_data.append({"acMeasuredHarmonic": self.ac_measured_harmonic.get_data()})
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
        if self.electrical_connection_id is not None:
            result_str += f"{sep}electricalConnectionId: {self.electrical_connection_id}"
            sep = ", "
        if self.parameter_id is not None:
            result_str += f"{sep}parameterId: {self.parameter_id}"
            sep = ", "
        if self.measurement_id is not None:
            result_str += f"{sep}measurementId: {self.measurement_id}"
            sep = ", "
        if self.voltage_type is not None:
            result_str += f"{sep}voltageType: {self.voltage_type}"
            sep = ", "
        if self.ac_measured_phases is not None:
            result_str += f"{sep}acMeasuredPhases: {self.ac_measured_phases}"
            sep = ", "
        if self.ac_measured_in_reference_to is not None:
            result_str += f"{sep}acMeasuredInReferenceTo: {self.ac_measured_in_reference_to}"
            sep = ", "
        if self.ac_measurement_type is not None:
            result_str += f"{sep}acMeasurementType: {self.ac_measurement_type}"
            sep = ", "
        if self.ac_measurement_variant is not None:
            result_str += f"{sep}acMeasurementVariant: {self.ac_measurement_variant}"
            sep = ", "
        if self.ac_measured_harmonic is not None:
            result_str += f"{sep}acMeasuredHarmonic: {self.ac_measured_harmonic}"
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
                electrical_connection_id=data_dict.get('electricalConnectionId'),
                parameter_id=data_dict.get('parameterId'),
                measurement_id=data_dict.get('measurementId'),
                voltage_type=data_dict.get('voltageType'),
                ac_measured_phases=data_dict.get('acMeasuredPhases'),
                ac_measured_in_reference_to=data_dict.get('acMeasuredInReferenceTo'),
                ac_measurement_type=data_dict.get('acMeasurementType'),
                ac_measurement_variant=data_dict.get('acMeasurementVariant'),
                ac_measured_harmonic=data_dict.get('acMeasuredHarmonic'),
                scope_type=data_dict.get('scopeType'),
                label=data_dict.get('label'),
                description=data_dict.get('description'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class ElectricalConnectionDescriptionDataElementsType: # EEBus_SPINE_TS_ElectricalConnection.xsd:ns_p:ElectricalConnectionDescriptionDataElementsType -> ComplexType
    def __init__(
            self,
            electrical_connection_id: ElementTagType = None,
            power_supply_type: ElementTagType = None,
            ac_connected_phases: ElementTagType = None,
            ac_rms_period_duration: ElementTagType = None,
            positive_energy_direction: ElementTagType = None,
            scope_type: ElementTagType = None,
            label: ElementTagType = None,
            description: ElementTagType = None,
    ):
        super().__init__()
        
        self.electrical_connection_id = electrical_connection_id
        self.power_supply_type = power_supply_type
        self.ac_connected_phases = ac_connected_phases
        self.ac_rms_period_duration = ac_rms_period_duration
        self.positive_energy_direction = positive_energy_direction
        self.scope_type = scope_type
        self.label = label
        self.description = description

        if not isinstance(self.electrical_connection_id, ElementTagType | NoneType):
            raise TypeError("electrical_connection_id is not of type ElementTagType")
        
        if not isinstance(self.power_supply_type, ElementTagType | NoneType):
            raise TypeError("power_supply_type is not of type ElementTagType")
        
        if not isinstance(self.ac_connected_phases, ElementTagType | NoneType):
            raise TypeError("ac_connected_phases is not of type ElementTagType")
        
        if not isinstance(self.ac_rms_period_duration, ElementTagType | NoneType):
            raise TypeError("ac_rms_period_duration is not of type ElementTagType")
        
        if not isinstance(self.positive_energy_direction, ElementTagType | NoneType):
            raise TypeError("positive_energy_direction is not of type ElementTagType")
        
        if not isinstance(self.scope_type, ElementTagType | NoneType):
            raise TypeError("scope_type is not of type ElementTagType")
        
        if not isinstance(self.label, ElementTagType | NoneType):
            raise TypeError("label is not of type ElementTagType")
        
        if not isinstance(self.description, ElementTagType | NoneType):
            raise TypeError("description is not of type ElementTagType")
        
    def get_data(self):

        msg_data = []
        
        if self.electrical_connection_id is not None:
            msg_data.append({"electricalConnectionId": self.electrical_connection_id.get_data()})
        if self.power_supply_type is not None:
            msg_data.append({"powerSupplyType": self.power_supply_type.get_data()})
        if self.ac_connected_phases is not None:
            msg_data.append({"acConnectedPhases": self.ac_connected_phases.get_data()})
        if self.ac_rms_period_duration is not None:
            msg_data.append({"acRmsPeriodDuration": self.ac_rms_period_duration.get_data()})
        if self.positive_energy_direction is not None:
            msg_data.append({"positiveEnergyDirection": self.positive_energy_direction.get_data()})
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
        if self.electrical_connection_id is not None:
            result_str += f"{sep}electricalConnectionId: {self.electrical_connection_id}"
            sep = ", "
        if self.power_supply_type is not None:
            result_str += f"{sep}powerSupplyType: {self.power_supply_type}"
            sep = ", "
        if self.ac_connected_phases is not None:
            result_str += f"{sep}acConnectedPhases: {self.ac_connected_phases}"
            sep = ", "
        if self.ac_rms_period_duration is not None:
            result_str += f"{sep}acRmsPeriodDuration: {self.ac_rms_period_duration}"
            sep = ", "
        if self.positive_energy_direction is not None:
            result_str += f"{sep}positiveEnergyDirection: {self.positive_energy_direction}"
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
                electrical_connection_id=data_dict.get('electricalConnectionId'),
                power_supply_type=data_dict.get('powerSupplyType'),
                ac_connected_phases=data_dict.get('acConnectedPhases'),
                ac_rms_period_duration=data_dict.get('acRmsPeriodDuration'),
                positive_energy_direction=data_dict.get('positiveEnergyDirection'),
                scope_type=data_dict.get('scopeType'),
                label=data_dict.get('label'),
                description=data_dict.get('description'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class ElectricalConnectionCharacteristicDataElementsType: # EEBus_SPINE_TS_ElectricalConnection.xsd:ns_p:ElectricalConnectionCharacteristicDataElementsType -> ComplexType
    def __init__(
            self,
            electrical_connection_id: ElementTagType = None,
            parameter_id: ElementTagType = None,
            characteristic_id: ElementTagType = None,
            characteristic_context: ElementTagType = None,
            characteristic_type: ElementTagType = None,
            value: ScaledNumberElementsType = None,
            unit: ElementTagType = None,
    ):
        super().__init__()
        
        self.electrical_connection_id = electrical_connection_id
        self.parameter_id = parameter_id
        self.characteristic_id = characteristic_id
        self.characteristic_context = characteristic_context
        self.characteristic_type = characteristic_type
        self.value = value
        self.unit = unit

        if not isinstance(self.electrical_connection_id, ElementTagType | NoneType):
            raise TypeError("electrical_connection_id is not of type ElementTagType")
        
        if not isinstance(self.parameter_id, ElementTagType | NoneType):
            raise TypeError("parameter_id is not of type ElementTagType")
        
        if not isinstance(self.characteristic_id, ElementTagType | NoneType):
            raise TypeError("characteristic_id is not of type ElementTagType")
        
        if not isinstance(self.characteristic_context, ElementTagType | NoneType):
            raise TypeError("characteristic_context is not of type ElementTagType")
        
        if not isinstance(self.characteristic_type, ElementTagType | NoneType):
            raise TypeError("characteristic_type is not of type ElementTagType")
        
        if not isinstance(self.value, ScaledNumberElementsType | NoneType):
            raise TypeError("value is not of type ScaledNumberElementsType")
        
        if not isinstance(self.unit, ElementTagType | NoneType):
            raise TypeError("unit is not of type ElementTagType")
        
    def get_data(self):

        msg_data = []
        
        if self.electrical_connection_id is not None:
            msg_data.append({"electricalConnectionId": self.electrical_connection_id.get_data()})
        if self.parameter_id is not None:
            msg_data.append({"parameterId": self.parameter_id.get_data()})
        if self.characteristic_id is not None:
            msg_data.append({"characteristicId": self.characteristic_id.get_data()})
        if self.characteristic_context is not None:
            msg_data.append({"characteristicContext": self.characteristic_context.get_data()})
        if self.characteristic_type is not None:
            msg_data.append({"characteristicType": self.characteristic_type.get_data()})
        if self.value is not None:
            msg_data.append({"value": self.value.get_data()})
        if self.unit is not None:
            msg_data.append({"unit": self.unit.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.electrical_connection_id is not None:
            result_str += f"{sep}electricalConnectionId: {self.electrical_connection_id}"
            sep = ", "
        if self.parameter_id is not None:
            result_str += f"{sep}parameterId: {self.parameter_id}"
            sep = ", "
        if self.characteristic_id is not None:
            result_str += f"{sep}characteristicId: {self.characteristic_id}"
            sep = ", "
        if self.characteristic_context is not None:
            result_str += f"{sep}characteristicContext: {self.characteristic_context}"
            sep = ", "
        if self.characteristic_type is not None:
            result_str += f"{sep}characteristicType: {self.characteristic_type}"
            sep = ", "
        if self.value is not None:
            result_str += f"{sep}value: {self.value}"
            sep = ", "
        if self.unit is not None:
            result_str += f"{sep}unit: {self.unit}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                electrical_connection_id=data_dict.get('electricalConnectionId'),
                parameter_id=data_dict.get('parameterId'),
                characteristic_id=data_dict.get('characteristicId'),
                characteristic_context=data_dict.get('characteristicContext'),
                characteristic_type=data_dict.get('characteristicType'),
                value=data_dict.get('value'),
                unit=data_dict.get('unit'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class ElectricalConnectionStateListDataSelectorsType: # EEBus_SPINE_TS_ElectricalConnection.xsd:ns_p:ElectricalConnectionStateListDataSelectorsType -> ComplexType
    def __init__(
            self,
            electrical_connection_id: ElectricalConnectionIdType = None,
    ):
        super().__init__()
        
        self.electrical_connection_id = electrical_connection_id

        if not isinstance(self.electrical_connection_id, ElectricalConnectionIdType | NoneType):
            raise TypeError("electrical_connection_id is not of type ElectricalConnectionIdType")
        
    def get_data(self):

        msg_data = []
        
        if self.electrical_connection_id is not None:
            msg_data.append({"electricalConnectionId": self.electrical_connection_id.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.electrical_connection_id is not None:
            result_str += f"{sep}electricalConnectionId: {self.electrical_connection_id}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                electrical_connection_id=data_dict.get('electricalConnectionId'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class ElectricalConnectionPermittedValueSetListDataSelectorsType: # EEBus_SPINE_TS_ElectricalConnection.xsd:ns_p:ElectricalConnectionPermittedValueSetListDataSelectorsType -> ComplexType
    def __init__(
            self,
            electrical_connection_id: ElectricalConnectionIdType = None,
            parameter_id: ElectricalConnectionParameterIdType = None,
    ):
        super().__init__()
        
        self.electrical_connection_id = electrical_connection_id
        self.parameter_id = parameter_id

        if not isinstance(self.electrical_connection_id, ElectricalConnectionIdType | NoneType):
            raise TypeError("electrical_connection_id is not of type ElectricalConnectionIdType")
        
        if not isinstance(self.parameter_id, ElectricalConnectionParameterIdType | NoneType):
            raise TypeError("parameter_id is not of type ElectricalConnectionParameterIdType")
        
    def get_data(self):

        msg_data = []
        
        if self.electrical_connection_id is not None:
            msg_data.append({"electricalConnectionId": self.electrical_connection_id.get_data()})
        if self.parameter_id is not None:
            msg_data.append({"parameterId": self.parameter_id.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.electrical_connection_id is not None:
            result_str += f"{sep}electricalConnectionId: {self.electrical_connection_id}"
            sep = ", "
        if self.parameter_id is not None:
            result_str += f"{sep}parameterId: {self.parameter_id}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                electrical_connection_id=data_dict.get('electricalConnectionId'),
                parameter_id=data_dict.get('parameterId'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class ElectricalConnectionParameterDescriptionListDataSelectorsType: # EEBus_SPINE_TS_ElectricalConnection.xsd:ns_p:ElectricalConnectionParameterDescriptionListDataSelectorsType -> ComplexType
    def __init__(
            self,
            electrical_connection_id: ElectricalConnectionIdType = None,
            parameter_id: ElectricalConnectionParameterIdType = None,
            measurement_id: MeasurementIdType = None,
            scope_type: ScopeTypeType = None,
    ):
        super().__init__()
        
        self.electrical_connection_id = electrical_connection_id
        self.parameter_id = parameter_id
        self.measurement_id = measurement_id
        self.scope_type = scope_type

        if not isinstance(self.electrical_connection_id, ElectricalConnectionIdType | NoneType):
            raise TypeError("electrical_connection_id is not of type ElectricalConnectionIdType")
        
        if not isinstance(self.parameter_id, ElectricalConnectionParameterIdType | NoneType):
            raise TypeError("parameter_id is not of type ElectricalConnectionParameterIdType")
        
        if not isinstance(self.measurement_id, MeasurementIdType | NoneType):
            raise TypeError("measurement_id is not of type MeasurementIdType")
        
        if not isinstance(self.scope_type, ScopeTypeType | NoneType):
            raise TypeError("scope_type is not of type ScopeTypeType")
        
    def get_data(self):

        msg_data = []
        
        if self.electrical_connection_id is not None:
            msg_data.append({"electricalConnectionId": self.electrical_connection_id.get_data()})
        if self.parameter_id is not None:
            msg_data.append({"parameterId": self.parameter_id.get_data()})
        if self.measurement_id is not None:
            msg_data.append({"measurementId": self.measurement_id.get_data()})
        if self.scope_type is not None:
            msg_data.append({"scopeType": self.scope_type.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.electrical_connection_id is not None:
            result_str += f"{sep}electricalConnectionId: {self.electrical_connection_id}"
            sep = ", "
        if self.parameter_id is not None:
            result_str += f"{sep}parameterId: {self.parameter_id}"
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
                electrical_connection_id=data_dict.get('electricalConnectionId'),
                parameter_id=data_dict.get('parameterId'),
                measurement_id=data_dict.get('measurementId'),
                scope_type=data_dict.get('scopeType'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class ElectricalConnectionDescriptionListDataSelectorsType: # EEBus_SPINE_TS_ElectricalConnection.xsd:ns_p:ElectricalConnectionDescriptionListDataSelectorsType -> ComplexType
    def __init__(
            self,
            electrical_connection_id: ElectricalConnectionIdType = None,
            scope_type: ScopeTypeType = None,
    ):
        super().__init__()
        
        self.electrical_connection_id = electrical_connection_id
        self.scope_type = scope_type

        if not isinstance(self.electrical_connection_id, ElectricalConnectionIdType | NoneType):
            raise TypeError("electrical_connection_id is not of type ElectricalConnectionIdType")
        
        if not isinstance(self.scope_type, ScopeTypeType | NoneType):
            raise TypeError("scope_type is not of type ScopeTypeType")
        
    def get_data(self):

        msg_data = []
        
        if self.electrical_connection_id is not None:
            msg_data.append({"electricalConnectionId": self.electrical_connection_id.get_data()})
        if self.scope_type is not None:
            msg_data.append({"scopeType": self.scope_type.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.electrical_connection_id is not None:
            result_str += f"{sep}electricalConnectionId: {self.electrical_connection_id}"
            sep = ", "
        if self.scope_type is not None:
            result_str += f"{sep}scopeType: {self.scope_type}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                electrical_connection_id=data_dict.get('electricalConnectionId'),
                scope_type=data_dict.get('scopeType'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class ElectricalConnectionCharacteristicListDataSelectorsType: # EEBus_SPINE_TS_ElectricalConnection.xsd:ns_p:ElectricalConnectionCharacteristicListDataSelectorsType -> ComplexType
    def __init__(
            self,
            electrical_connection_id: ElectricalConnectionIdType = None,
            parameter_id: ElectricalConnectionParameterIdType = None,
            characteristic_id: ElectricalConnectionCharacteristicIdType = None,
            characteristic_context: ElectricalConnectionCharacteristicContextType = None,
            characteristic_type: ElectricalConnectionCharacteristicTypeType = None,
    ):
        super().__init__()
        
        self.electrical_connection_id = electrical_connection_id
        self.parameter_id = parameter_id
        self.characteristic_id = characteristic_id
        self.characteristic_context = characteristic_context
        self.characteristic_type = characteristic_type

        if not isinstance(self.electrical_connection_id, ElectricalConnectionIdType | NoneType):
            raise TypeError("electrical_connection_id is not of type ElectricalConnectionIdType")
        
        if not isinstance(self.parameter_id, ElectricalConnectionParameterIdType | NoneType):
            raise TypeError("parameter_id is not of type ElectricalConnectionParameterIdType")
        
        if not isinstance(self.characteristic_id, ElectricalConnectionCharacteristicIdType | NoneType):
            raise TypeError("characteristic_id is not of type ElectricalConnectionCharacteristicIdType")
        
        if not isinstance(self.characteristic_context, ElectricalConnectionCharacteristicContextType | NoneType):
            raise TypeError("characteristic_context is not of type ElectricalConnectionCharacteristicContextType")
        
        if not isinstance(self.characteristic_type, ElectricalConnectionCharacteristicTypeType | NoneType):
            raise TypeError("characteristic_type is not of type ElectricalConnectionCharacteristicTypeType")
        
    def get_data(self):

        msg_data = []
        
        if self.electrical_connection_id is not None:
            msg_data.append({"electricalConnectionId": self.electrical_connection_id.get_data()})
        if self.parameter_id is not None:
            msg_data.append({"parameterId": self.parameter_id.get_data()})
        if self.characteristic_id is not None:
            msg_data.append({"characteristicId": self.characteristic_id.get_data()})
        if self.characteristic_context is not None:
            msg_data.append({"characteristicContext": self.characteristic_context.get_data()})
        if self.characteristic_type is not None:
            msg_data.append({"characteristicType": self.characteristic_type.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.electrical_connection_id is not None:
            result_str += f"{sep}electricalConnectionId: {self.electrical_connection_id}"
            sep = ", "
        if self.parameter_id is not None:
            result_str += f"{sep}parameterId: {self.parameter_id}"
            sep = ", "
        if self.characteristic_id is not None:
            result_str += f"{sep}characteristicId: {self.characteristic_id}"
            sep = ", "
        if self.characteristic_context is not None:
            result_str += f"{sep}characteristicContext: {self.characteristic_context}"
            sep = ", "
        if self.characteristic_type is not None:
            result_str += f"{sep}characteristicType: {self.characteristic_type}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                electrical_connection_id=data_dict.get('electricalConnectionId'),
                parameter_id=data_dict.get('parameterId'),
                characteristic_id=data_dict.get('characteristicId'),
                characteristic_context=data_dict.get('characteristicContext'),
                characteristic_type=data_dict.get('characteristicType'),
            )
        elif data:
            return cls(data)
        else:
            return cls()



