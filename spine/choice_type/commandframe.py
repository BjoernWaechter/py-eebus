# Jinja Template message_type.py.jinja2
from spine.base_type.supplycondition import SupplyConditionDescriptionListDataSelectorsType
from spine.base_type.powersequences import PowerSequenceScheduleDataElementsType
from spine.base_type.bindingmanagement import BindingManagementEntryDataElementsType
from spine.base_type.taskmanagement import TaskManagementOverviewDataElementsType
from spine.base_type.tariffinformation import TariffOverallConstraintsDataElementsType
from spine.base_type.devicediagnosis import DeviceDiagnosisHeartbeatDataElementsType
from spine.base_type.networkmanagement import NetworkManagementDeviceDescriptionDataElementsType
from spine.base_type.timeseries import TimeSeriesConstraintsDataElementsType
from spine.base_type.timeinformation import TimeDistributorDataElementsType
from spine.base_type.loadcontrol import LoadControlStateDataElementsType
from spine.base_type.nodemanagement import NodeManagementBindingDataSelectorsType
from spine.base_type.tariffinformation import TariffListDataSelectorsType
from spine.base_type.measurement import MeasurementDataElementsType
from spine.base_type.taskmanagement import TaskManagementJobRelationDataElementsType
from spine.base_type.electricalconnection import ElectricalConnectionParameterDescriptionListDataSelectorsType
from spine.base_type.loadcontrol import LoadControlLimitDescriptionListDataSelectorsType
from spine.base_type.powersequences import PowerTimeSlotScheduleDataElementsType
from spine.base_type.tariffinformation import TierBoundaryListDataSelectorsType
from spine.base_type.powersequences import PowerSequenceSchedulePreferenceListDataSelectorsType
from spine.base_type.incentivetable import IncentiveTableDescriptionDataElementsType
from spine.base_type.identification import IdentificationDataElementsType
from spine.base_type.directcontrol import DirectControlActivityListDataSelectorsType
from spine.base_type.setpoint import SetpointDescriptionListDataSelectorsType
from spine.base_type.version import SpecificationVersionDataElementsType
from spine.base_type.setpoint import SetpointDescriptionDataElementsType
from spine.base_type.operatingconstraints import OperatingConstraintsResumeImplicationDataElementsType
from spine.base_type.messaging import MessagingListDataSelectorsType
from spine.base_type.setpoint import SetpointConstraintsListDataSelectorsType
from spine.base_type.loadcontrol import LoadControlLimitConstraintsListDataSelectorsType
from spine.base_type.networkmanagement import NetworkManagementEntityDescriptionDataElementsType
from spine.base_type.smartenergymanagementps import SmartEnergyManagementPsPriceCalculationRequestCallElementsType
from spine.base_type.identification import IdentificationListDataSelectorsType
from spine.base_type.networkmanagement import NetworkManagementDiscoverCallElementsType
from spine.base_type.hvac import HvacSystemFunctionDescriptionDataElementsType
from spine.base_type.hvac import HvacSystemFunctionDataElementsType
from spine.base_type.deviceconfiguration import DeviceConfigurationKeyValueDescriptionDataElementsType
from spine.base_type.directcontrol import DirectControlDescriptionDataElementsType
from spine.base_type.electricalconnection import ElectricalConnectionCharacteristicListDataSelectorsType
from spine.base_type.supplycondition import SupplyConditionThresholdRelationDataElementsType
from spine.base_type.hvac import HvacOverrunDataElementsType
from spine.base_type.hvac import HvacSystemFunctionListDataSelectorsType
from spine.base_type.tariffinformation import TariffDescriptionListDataSelectorsType
from spine.base_type.powersequences import PowerSequenceScheduleConfigurationRequestCallElementsType
from spine.base_type.timeseries import TimeSeriesDataElementsType
from spine.base_type.incentivetable import IncentiveTableDescriptionDataSelectorsType
from spine.base_type.threshold import ThresholdConstraintsDataElementsType
from spine.base_type.incentivetable import IncentiveTableConstraintsDataSelectorsType
from spine.base_type.powersequences import PowerSequencePriceCalculationRequestCallElementsType
from spine.base_type.tariffinformation import TierBoundaryDataElementsType
from spine.base_type.tariffinformation import TariffTierRelationListDataSelectorsType
from spine.base_type.electricalconnection import ElectricalConnectionDescriptionDataElementsType
from spine.base_type.loadcontrol import LoadControlLimitDescriptionDataElementsType
from spine.base_type.electricalconnection import ElectricalConnectionStateDataElementsType
from spine.base_type.nodemanagement import NodeManagementDetailedDiscoveryDataSelectorsType
from spine.base_type.timeseries import TimeSeriesListDataSelectorsType
from spine.base_type.tariffinformation import TariffDescriptionDataElementsType
from spine.base_type.bill import BillDescriptionListDataSelectorsType
from spine.base_type.devicediagnosis import DeviceDiagnosisServiceDataElementsType
from spine.base_type.powersequences import PowerTimeSlotValueDataElementsType
from spine.base_type.tariffinformation import IncentiveListDataSelectorsType
from spine.base_type.networkmanagement import NetworkManagementDeviceDescriptionListDataSelectorsType
from spine.base_type.tariffinformation import TariffBoundaryRelationListDataSelectorsType
from spine.base_type.tariffinformation import TierIncentiveRelationDataElementsType
from spine.base_type.hvac import HvacSystemFunctionPowerSequenceRelationListDataSelectorsType
from spine.base_type.loadcontrol import LoadControlEventDataElementsType
from spine.base_type.powersequences import PowerSequenceAlternativesRelationDataElementsType
from spine.base_type.tariffinformation import TierDescriptionDataElementsType
from spine.base_type.networkmanagement import NetworkManagementJoiningModeDataElementsType
from spine.base_type.deviceconfiguration import DeviceConfigurationKeyValueDescriptionListDataSelectorsType
from spine.base_type.supplycondition import SupplyConditionThresholdRelationListDataSelectorsType
from spine.base_type.hvac import HvacSystemFunctionSetpointRelationListDataSelectorsType
from spine.base_type.powersequences import PowerSequencePriceListDataSelectorsType
from spine.base_type.electricalconnection import ElectricalConnectionParameterDescriptionDataElementsType
from spine.base_type.powersequences import PowerTimeSlotScheduleConstraintsListDataSelectorsType
from spine.base_type.operatingconstraints import OperatingConstraintsPowerRangeListDataSelectorsType
from spine.base_type.threshold import ThresholdConstraintsListDataSelectorsType
from spine.base_type.actuatorlevel import ActuatorLevelDataElementsType
from spine.base_type.deviceconfiguration import DeviceConfigurationKeyValueConstraintsDataElementsType
from spine.base_type.timeinformation import TimePrecisionDataElementsType
from spine.base_type.tariffinformation import IncentiveDataElementsType
from spine.base_type.operatingconstraints import OperatingConstraintsPowerDescriptionListDataSelectorsType
from spine.base_type.tariffinformation import TierListDataSelectorsType
from spine.base_type.devicediagnosis import DeviceDiagnosisStateDataElementsType
from spine.base_type.operatingconstraints import OperatingConstraintsDurationDataElementsType
from spine.base_type.nodemanagement import NodeManagementSubscriptionDataElementsType
from spine.base_type.loadcontrol import LoadControlEventListDataSelectorsType
from spine.base_type.powersequences import PowerTimeSlotScheduleConstraintsDataElementsType
from spine.base_type.setpoint import SetpointDataElementsType
from spine.base_type.powersequences import PowerSequencePriceDataElementsType
from spine.base_type.networkmanagement import NetworkManagementModifyNodeCallElementsType
from spine.base_type.tariffinformation import TierDataElementsType
from spine.base_type.setpoint import SetpointListDataSelectorsType
from spine.base_type.electricalconnection import ElectricalConnectionDescriptionListDataSelectorsType
from spine.base_type.operatingconstraints import OperatingConstraintsPowerLevelListDataSelectorsType
from spine.base_type.tariffinformation import TariffDataElementsType
from spine.base_type.networkmanagement import NetworkManagementReportCandidateDataElementsType
from spine.base_type.powersequences import PowerSequenceDescriptionDataElementsType
from spine.base_type.measurement import MeasurementThresholdRelationDataElementsType
from spine.base_type.subscriptionmanagement import SubscriptionManagementEntryDataElementsType
from spine.base_type.networkmanagement import NetworkManagementRemoveNodeCallElementsType
from spine.base_type.measurement import MeasurementConstraintsListDataSelectorsType
from spine.base_type.incentivetable import IncentiveTableDataElementsType
from spine.base_type.tariffinformation import TierIncentiveRelationListDataSelectorsType
from spine.base_type.measurement import MeasurementConstraintsDataElementsType
from spine.base_type.usecaseinformation import UseCaseInformationListDataSelectorsType
from spine.base_type.hvac import HvacSystemFunctionOperationModeRelationListDataSelectorsType
from spine.base_type.sensing import SensingDescriptionDataElementsType
from spine.base_type.nodemanagement import NodeManagementBindingDeleteCallElementsType
from spine.base_type.identification import SessionIdentificationDataElementsType
from spine.base_type.electricalconnection import ElectricalConnectionCharacteristicDataElementsType
from spine.base_type.tariffinformation import TariffBoundaryRelationDataElementsType
from spine.base_type.nodemanagement import NodeManagementDestinationListDataSelectorsType
from spine.base_type.measurement import MeasurementListDataSelectorsType
from spine.base_type.bill import BillDescriptionDataElementsType
from spine.base_type.hvac import HvacSystemFunctionOperationModeRelationDataElementsType
from spine.base_type.networkmanagement import NetworkManagementProcessStateDataElementsType
from spine.base_type.nodemanagement import NodeManagementSubscriptionDataSelectorsType
from spine.base_type.timeseries import TimeSeriesDescriptionDataElementsType
from spine.base_type.networkmanagement import NetworkManagementScanNetworkCallElementsType
from spine.base_type.loadcontrol import LoadControlNodeDataElementsType
from spine.base_type.nodemanagement import NodeManagementBindingDataElementsType
from spine.base_type.operatingconstraints import OperatingConstraintsDurationListDataSelectorsType
from spine.base_type.hvac import HvacSystemFunctionSetpointRelationDataElementsType
from spine.base_type.nodemanagement import NodeManagementUseCaseDataElementsType
from spine.base_type.sensing import SensingDataElementsType
from spine.base_type.deviceconfiguration import DeviceConfigurationKeyValueDataElementsType
from spine.base_type.deviceclassification import DeviceClassificationUserDataElementsType
from spine.base_type.powersequences import PowerSequenceNodeScheduleInformationDataElementsType
from spine.base_type.identification import SessionIdentificationListDataSelectorsType
from spine.base_type.bill import BillListDataSelectorsType
from spine.base_type.timeseries import TimeSeriesDescriptionListDataSelectorsType
from spine.base_type.networkmanagement import NetworkManagementAddNodeCallElementsType
from spine.base_type.loadcontrol import LoadControlLimitDataElementsType
from spine.base_type.hvac import HvacOverrunListDataSelectorsType
from spine.base_type.bindingmanagement import BindingManagementDeleteCallElementsType
from spine.base_type.measurement import MeasurementDescriptionDataElementsType
from spine.base_type.tariffinformation import TariffTierRelationDataElementsType
from spine.base_type.deviceconfiguration import DeviceConfigurationKeyValueListDataSelectorsType
from spine.base_type.datatunneling import DataTunnelingCallElementsType
from spine.base_type.taskmanagement import TaskManagementJobDescriptionListDataSelectorsType
from spine.base_type.threshold import ThresholdDescriptionDataElementsType
from spine.base_type.bindingmanagement import BindingManagementEntryListDataSelectorsType
from spine.base_type.threshold import ThresholdDataElementsType
from spine.base_type.operatingconstraints import OperatingConstraintsPowerLevelDataElementsType
from spine.base_type.loadcontrol import LoadControlLimitListDataSelectorsType
from spine.base_type.operatingconstraints import OperatingConstraintsInterruptDataElementsType
from spine.base_type.subscriptionmanagement import SubscriptionManagementRequestCallElementsType
from spine.base_type.tariffinformation import IncentiveDescriptionDataElementsType
from spine.base_type.measurement import MeasurementDescriptionListDataSelectorsType
from spine.base_type.alarm import AlarmDataElementsType
from spine.base_type.actuatorswitch import ActuatorSwitchDataElementsType
from spine.base_type.operatingconstraints import OperatingConstraintsResumeImplicationListDataSelectorsType
from spine.base_type.networkmanagement import NetworkManagementAbortCallElementsType
from spine.base_type.identification import SessionMeasurementRelationDataElementsType
from spine.base_type.operatingconstraints import OperatingConstraintsPowerRangeDataElementsType
from spine.base_type.taskmanagement import TaskManagementJobDataElementsType
from spine.base_type.smartenergymanagementps import SmartEnergyManagementPsDataElementsType
from spine.base_type.powersequences import PowerSequenceStateListDataSelectorsType
from spine.base_type.powersequences import PowerSequenceStateDataElementsType
from spine.base_type.timetable import TimeTableConstraintsListDataSelectorsType
from spine.base_type.usecaseinformation import UseCaseInformationDataElementsType
from spine.base_type.measurement import MeasurementThresholdRelationListDataSelectorsType
from spine.base_type.loadcontrol import LoadControlStateListDataSelectorsType
from spine.base_type.timeseries import TimeSeriesConstraintsListDataSelectorsType
from spine.base_type.measurement import MeasurementSeriesDataElementsType
from spine.base_type.electricalconnection import ElectricalConnectionPermittedValueSetListDataSelectorsType
from spine.base_type.measurement import MeasurementSeriesListDataSelectorsType
from spine.base_type.powersequences import PowerSequenceScheduleConstraintsListDataSelectorsType
from spine.base_type.version import SpecificationVersionListDataSelectorsType
from spine.base_type.networkmanagement import NetworkManagementFeatureDescriptionDataElementsType
from spine.base_type.supplycondition import SupplyConditionListDataSelectorsType
from spine.base_type.loadcontrol import LoadControlLimitConstraintsDataElementsType
from spine.base_type.timetable import TimeTableConstraintsDataElementsType
from spine.base_type.operatingconstraints import OperatingConstraintsPowerDescriptionDataElementsType
from spine.base_type.nodemanagement import NodeManagementBindingRequestCallElementsType
from spine.base_type.hvac import HvacOperationModeDescriptionListDataSelectorsType
from spine.base_type.stateinformation import StateInformationListDataSelectorsType
from spine.base_type.taskmanagement import TaskManagementJobDescriptionDataElementsType
from spine.base_type.incentivetable import IncentiveTableDataSelectorsType
from spine.base_type.timetable import TimeTableListDataSelectorsType
from spine.base_type.stateinformation import StateInformationDataElementsType
from spine.base_type.incentivetable import IncentiveTableConstraintsDataElementsType
from spine.base_type.actuatorswitch import ActuatorSwitchDescriptionDataElementsType
from spine.base_type.hvac import HvacOperationModeDescriptionDataElementsType
from spine.base_type.timeinformation import TimeDistributorEnquiryCallElementsType
from spine.base_type.threshold import ThresholdListDataSelectorsType
from spine.base_type.nodemanagement import NodeManagementSubscriptionRequestCallElementsType
from spine.base_type.nodemanagement import NodeManagementDetailedDiscoveryDataElementsType
from spine.base_type.supplycondition import SupplyConditionDataElementsType
from spine.base_type.bill import BillDataElementsType
from spine.base_type.nodemanagement import NodeManagementSubscriptionDeleteCallElementsType
from spine.base_type.sensing import SensingListDataSelectorsType
from spine.base_type.hvac import HvacSystemFunctionPowerSequenceRelationDataElementsType
from spine.base_type.tariffinformation import CommodityListDataSelectorsType
from spine.base_type.tariffinformation import CommodityDataElementsType
from spine.base_type.subscriptionmanagement import SubscriptionManagementDeleteCallElementsType
from spine.base_type.tariffinformation import TierBoundaryDescriptionDataElementsType
from spine.base_type.hvac import HvacSystemFunctionDescriptionListDataSelectorsType
from spine.base_type.bill import BillConstraintsDataElementsType
from spine.base_type.networkmanagement import NetworkManagementFeatureDescriptionListDataSelectorsType
from spine.base_type.nodemanagement import NodeManagementUseCaseDataSelectorsType
from spine.base_type.timetable import TimeTableDataElementsType
from spine.base_type.subscriptionmanagement import SubscriptionManagementEntryListDataSelectorsType
from spine.base_type.alarm import AlarmListDataSelectorsType
from spine.base_type.hvac import HvacOverrunDescriptionDataElementsType
from spine.base_type.bindingmanagement import BindingManagementRequestCallElementsType
from spine.base_type.tariffinformation import TierBoundaryDescriptionListDataSelectorsType
from spine.base_type.timetable import TimeTableDescriptionListDataSelectorsType
from spine.base_type.tariffinformation import TierDescriptionListDataSelectorsType
from spine.base_type.supplycondition import SupplyConditionDescriptionDataElementsType
from spine.base_type.powersequences import PowerTimeSlotScheduleListDataSelectorsType
from spine.base_type.bill import BillConstraintsListDataSelectorsType
from spine.base_type.taskmanagement import TaskManagementJobListDataSelectorsType
from spine.base_type.directcontrol import DirectControlActivityDataElementsType
from spine.base_type.powersequences import PowerSequenceSchedulePreferenceDataElementsType
from spine.base_type.deviceconfiguration import DeviceConfigurationKeyValueConstraintsListDataSelectorsType
from spine.base_type.operatingconstraints import OperatingConstraintsInterruptListDataSelectorsType
from spine.base_type.nodemanagement import NodeManagementDestinationDataElementsType
from spine.base_type.electricalconnection import ElectricalConnectionStateListDataSelectorsType
from spine.base_type.smartenergymanagementps import SmartEnergyManagementPsConfigurationRequestCallElementsType
from spine.base_type.timetable import TimeTableDescriptionDataElementsType
from spine.base_type.messaging import MessagingDataElementsType
from spine.base_type.smartenergymanagementps import SmartEnergyManagementPsPriceDataSelectorsType
from spine.base_type.powersequences import PowerSequenceScheduleListDataSelectorsType
from spine.base_type.setpoint import SetpointConstraintsDataElementsType
from spine.base_type.smartenergymanagementps import SmartEnergyManagementPsDataSelectorsType
from spine.base_type.timeinformation import TimeInformationDataElementsType
from spine.base_type.actuatorlevel import ActuatorLevelDescriptionDataElementsType
from spine.base_type.smartenergymanagementps import SmartEnergyManagementPsPriceDataElementsType
from spine.base_type.electricalconnection import ElectricalConnectionPermittedValueSetDataElementsType
from spine.base_type.identification import SessionMeasurementRelationListDataSelectorsType
from spine.base_type.networkmanagement import NetworkManagementEntityDescriptionListDataSelectorsType
from spine.base_type.threshold import ThresholdDescriptionListDataSelectorsType
from spine.base_type.powersequences import PowerTimeSlotValueListDataSelectorsType
from spine.base_type.hvac import HvacOverrunDescriptionListDataSelectorsType
from spine.base_type.taskmanagement import TaskManagementJobRelationListDataSelectorsType
from spine.base_type.powersequences import PowerSequenceScheduleConstraintsDataElementsType
from spine.base_type.deviceclassification import DeviceClassificationManufacturerDataElementsType
from spine.base_type.tariffinformation import IncentiveDescriptionListDataSelectorsType
from spine.base_type.powersequences import PowerSequenceAlternativesRelationListDataSelectorsType
from spine.base_type.powersequences import PowerSequenceDescriptionListDataSelectorsType
from types import NoneType
from spine import array_2_dict


class PayloadContributionGroup:
    def __init__(
            self,
    ):
        super().__init__()
        

    def get_data(self): # ChoiceType

        msg_data = []
        
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
            )
        elif data:
            return cls(data)
        else:
            return cls()


class DataSelectorsChoiceGroup:
    def __init__(
            self,
            alarm_list_data_selectors: AlarmListDataSelectorsType,
            bill_constraints_list_data_selectors: BillConstraintsListDataSelectorsType,
            bill_description_list_data_selectors: BillDescriptionListDataSelectorsType,
            bill_list_data_selectors: BillListDataSelectorsType,
            binding_management_entry_list_data_selectors: BindingManagementEntryListDataSelectorsType,
            commodity_list_data_selectors: CommodityListDataSelectorsType,
            device_configuration_key_value_constraints_list_data_selectors: DeviceConfigurationKeyValueConstraintsListDataSelectorsType,
            device_configuration_key_value_description_list_data_selectors: DeviceConfigurationKeyValueDescriptionListDataSelectorsType,
            device_configuration_key_value_list_data_selectors: DeviceConfigurationKeyValueListDataSelectorsType,
            direct_control_activity_list_data_selectors: DirectControlActivityListDataSelectorsType,
            electrical_connection_characteristic_list_data_selectors: ElectricalConnectionCharacteristicListDataSelectorsType,
            electrical_connection_description_list_data_selectors: ElectricalConnectionDescriptionListDataSelectorsType,
            electrical_connection_parameter_description_list_data_selectors: ElectricalConnectionParameterDescriptionListDataSelectorsType,
            electrical_connection_permitted_value_set_list_data_selectors: ElectricalConnectionPermittedValueSetListDataSelectorsType,
            electrical_connection_state_list_data_selectors: ElectricalConnectionStateListDataSelectorsType,
            hvac_operation_mode_description_list_data_selectors: HvacOperationModeDescriptionListDataSelectorsType,
            hvac_overrun_description_list_data_selectors: HvacOverrunDescriptionListDataSelectorsType,
            hvac_overrun_list_data_selectors: HvacOverrunListDataSelectorsType,
            hvac_system_function_description_list_data_selectors: HvacSystemFunctionDescriptionListDataSelectorsType,
            hvac_system_function_list_data_selectors: HvacSystemFunctionListDataSelectorsType,
            hvac_system_function_operation_mode_relation_list_data_selectors: HvacSystemFunctionOperationModeRelationListDataSelectorsType,
            hvac_system_function_power_sequence_relation_list_data_selectors: HvacSystemFunctionPowerSequenceRelationListDataSelectorsType,
            hvac_system_function_setpoint_relation_list_data_selectors: HvacSystemFunctionSetpointRelationListDataSelectorsType,
            identification_list_data_selectors: IdentificationListDataSelectorsType,
            incentive_description_list_data_selectors: IncentiveDescriptionListDataSelectorsType,
            incentive_list_data_selectors: IncentiveListDataSelectorsType,
            incentive_table_constraints_data_selectors: IncentiveTableConstraintsDataSelectorsType,
            incentive_table_data_selectors: IncentiveTableDataSelectorsType,
            incentive_table_description_data_selectors: IncentiveTableDescriptionDataSelectorsType,
            load_control_event_list_data_selectors: LoadControlEventListDataSelectorsType,
            load_control_limit_constraints_list_data_selectors: LoadControlLimitConstraintsListDataSelectorsType,
            load_control_limit_description_list_data_selectors: LoadControlLimitDescriptionListDataSelectorsType,
            load_control_limit_list_data_selectors: LoadControlLimitListDataSelectorsType,
            load_control_state_list_data_selectors: LoadControlStateListDataSelectorsType,
            measurement_constraints_list_data_selectors: MeasurementConstraintsListDataSelectorsType,
            measurement_description_list_data_selectors: MeasurementDescriptionListDataSelectorsType,
            measurement_list_data_selectors: MeasurementListDataSelectorsType,
            measurement_series_list_data_selectors: MeasurementSeriesListDataSelectorsType,
            measurement_threshold_relation_list_data_selectors: MeasurementThresholdRelationListDataSelectorsType,
            messaging_list_data_selectors: MessagingListDataSelectorsType,
            network_management_device_description_list_data_selectors: NetworkManagementDeviceDescriptionListDataSelectorsType,
            network_management_entity_description_list_data_selectors: NetworkManagementEntityDescriptionListDataSelectorsType,
            network_management_feature_description_list_data_selectors: NetworkManagementFeatureDescriptionListDataSelectorsType,
            node_management_binding_data_selectors: NodeManagementBindingDataSelectorsType,
            node_management_destination_list_data_selectors: NodeManagementDestinationListDataSelectorsType,
            node_management_detailed_discovery_data_selectors: NodeManagementDetailedDiscoveryDataSelectorsType,
            node_management_subscription_data_selectors: NodeManagementSubscriptionDataSelectorsType,
            node_management_use_case_data_selectors: NodeManagementUseCaseDataSelectorsType,
            operating_constraints_duration_list_data_selectors: OperatingConstraintsDurationListDataSelectorsType,
            operating_constraints_interrupt_list_data_selectors: OperatingConstraintsInterruptListDataSelectorsType,
            operating_constraints_power_description_list_data_selectors: OperatingConstraintsPowerDescriptionListDataSelectorsType,
            operating_constraints_power_level_list_data_selectors: OperatingConstraintsPowerLevelListDataSelectorsType,
            operating_constraints_power_range_list_data_selectors: OperatingConstraintsPowerRangeListDataSelectorsType,
            operating_constraints_resume_implication_list_data_selectors: OperatingConstraintsResumeImplicationListDataSelectorsType,
            power_sequence_alternatives_relation_list_data_selectors: PowerSequenceAlternativesRelationListDataSelectorsType,
            power_sequence_description_list_data_selectors: PowerSequenceDescriptionListDataSelectorsType,
            power_sequence_price_list_data_selectors: PowerSequencePriceListDataSelectorsType,
            power_sequence_schedule_constraints_list_data_selectors: PowerSequenceScheduleConstraintsListDataSelectorsType,
            power_sequence_schedule_list_data_selectors: PowerSequenceScheduleListDataSelectorsType,
            power_sequence_schedule_preference_list_data_selectors: PowerSequenceSchedulePreferenceListDataSelectorsType,
            power_sequence_state_list_data_selectors: PowerSequenceStateListDataSelectorsType,
            power_time_slot_schedule_constraints_list_data_selectors: PowerTimeSlotScheduleConstraintsListDataSelectorsType,
            power_time_slot_schedule_list_data_selectors: PowerTimeSlotScheduleListDataSelectorsType,
            power_time_slot_value_list_data_selectors: PowerTimeSlotValueListDataSelectorsType,
            sensing_list_data_selectors: SensingListDataSelectorsType,
            session_identification_list_data_selectors: SessionIdentificationListDataSelectorsType,
            session_measurement_relation_list_data_selectors: SessionMeasurementRelationListDataSelectorsType,
            setpoint_constraints_list_data_selectors: SetpointConstraintsListDataSelectorsType,
            setpoint_description_list_data_selectors: SetpointDescriptionListDataSelectorsType,
            setpoint_list_data_selectors: SetpointListDataSelectorsType,
            smart_energy_management_ps_data_selectors: SmartEnergyManagementPsDataSelectorsType,
            smart_energy_management_ps_price_data_selectors: SmartEnergyManagementPsPriceDataSelectorsType,
            specification_version_list_data_selectors: SpecificationVersionListDataSelectorsType,
            state_information_list_data_selectors: StateInformationListDataSelectorsType,
            subscription_management_entry_list_data_selectors: SubscriptionManagementEntryListDataSelectorsType,
            supply_condition_description_list_data_selectors: SupplyConditionDescriptionListDataSelectorsType,
            supply_condition_list_data_selectors: SupplyConditionListDataSelectorsType,
            supply_condition_threshold_relation_list_data_selectors: SupplyConditionThresholdRelationListDataSelectorsType,
            tariff_boundary_relation_list_data_selectors: TariffBoundaryRelationListDataSelectorsType,
            tariff_description_list_data_selectors: TariffDescriptionListDataSelectorsType,
            tariff_list_data_selectors: TariffListDataSelectorsType,
            tariff_tier_relation_list_data_selectors: TariffTierRelationListDataSelectorsType,
            task_management_job_description_list_data_selectors: TaskManagementJobDescriptionListDataSelectorsType,
            task_management_job_list_data_selectors: TaskManagementJobListDataSelectorsType,
            task_management_job_relation_list_data_selectors: TaskManagementJobRelationListDataSelectorsType,
            threshold_constraints_list_data_selectors: ThresholdConstraintsListDataSelectorsType,
            threshold_description_list_data_selectors: ThresholdDescriptionListDataSelectorsType,
            threshold_list_data_selectors: ThresholdListDataSelectorsType,
            tier_boundary_description_list_data_selectors: TierBoundaryDescriptionListDataSelectorsType,
            tier_boundary_list_data_selectors: TierBoundaryListDataSelectorsType,
            tier_description_list_data_selectors: TierDescriptionListDataSelectorsType,
            tier_incentive_relation_list_data_selectors: TierIncentiveRelationListDataSelectorsType,
            tier_list_data_selectors: TierListDataSelectorsType,
            time_series_constraints_list_data_selectors: TimeSeriesConstraintsListDataSelectorsType,
            time_series_description_list_data_selectors: TimeSeriesDescriptionListDataSelectorsType,
            time_series_list_data_selectors: TimeSeriesListDataSelectorsType,
            time_table_constraints_list_data_selectors: TimeTableConstraintsListDataSelectorsType,
            time_table_description_list_data_selectors: TimeTableDescriptionListDataSelectorsType,
            time_table_list_data_selectors: TimeTableListDataSelectorsType,
            use_case_information_list_data_selectors: UseCaseInformationListDataSelectorsType,
    ):
        super().__init__()
        
        self.alarm_list_data_selectors = alarm_list_data_selectors
        self.bill_constraints_list_data_selectors = bill_constraints_list_data_selectors
        self.bill_description_list_data_selectors = bill_description_list_data_selectors
        self.bill_list_data_selectors = bill_list_data_selectors
        self.binding_management_entry_list_data_selectors = binding_management_entry_list_data_selectors
        self.commodity_list_data_selectors = commodity_list_data_selectors
        self.device_configuration_key_value_constraints_list_data_selectors = device_configuration_key_value_constraints_list_data_selectors
        self.device_configuration_key_value_description_list_data_selectors = device_configuration_key_value_description_list_data_selectors
        self.device_configuration_key_value_list_data_selectors = device_configuration_key_value_list_data_selectors
        self.direct_control_activity_list_data_selectors = direct_control_activity_list_data_selectors
        self.electrical_connection_characteristic_list_data_selectors = electrical_connection_characteristic_list_data_selectors
        self.electrical_connection_description_list_data_selectors = electrical_connection_description_list_data_selectors
        self.electrical_connection_parameter_description_list_data_selectors = electrical_connection_parameter_description_list_data_selectors
        self.electrical_connection_permitted_value_set_list_data_selectors = electrical_connection_permitted_value_set_list_data_selectors
        self.electrical_connection_state_list_data_selectors = electrical_connection_state_list_data_selectors
        self.hvac_operation_mode_description_list_data_selectors = hvac_operation_mode_description_list_data_selectors
        self.hvac_overrun_description_list_data_selectors = hvac_overrun_description_list_data_selectors
        self.hvac_overrun_list_data_selectors = hvac_overrun_list_data_selectors
        self.hvac_system_function_description_list_data_selectors = hvac_system_function_description_list_data_selectors
        self.hvac_system_function_list_data_selectors = hvac_system_function_list_data_selectors
        self.hvac_system_function_operation_mode_relation_list_data_selectors = hvac_system_function_operation_mode_relation_list_data_selectors
        self.hvac_system_function_power_sequence_relation_list_data_selectors = hvac_system_function_power_sequence_relation_list_data_selectors
        self.hvac_system_function_setpoint_relation_list_data_selectors = hvac_system_function_setpoint_relation_list_data_selectors
        self.identification_list_data_selectors = identification_list_data_selectors
        self.incentive_description_list_data_selectors = incentive_description_list_data_selectors
        self.incentive_list_data_selectors = incentive_list_data_selectors
        self.incentive_table_constraints_data_selectors = incentive_table_constraints_data_selectors
        self.incentive_table_data_selectors = incentive_table_data_selectors
        self.incentive_table_description_data_selectors = incentive_table_description_data_selectors
        self.load_control_event_list_data_selectors = load_control_event_list_data_selectors
        self.load_control_limit_constraints_list_data_selectors = load_control_limit_constraints_list_data_selectors
        self.load_control_limit_description_list_data_selectors = load_control_limit_description_list_data_selectors
        self.load_control_limit_list_data_selectors = load_control_limit_list_data_selectors
        self.load_control_state_list_data_selectors = load_control_state_list_data_selectors
        self.measurement_constraints_list_data_selectors = measurement_constraints_list_data_selectors
        self.measurement_description_list_data_selectors = measurement_description_list_data_selectors
        self.measurement_list_data_selectors = measurement_list_data_selectors
        self.measurement_series_list_data_selectors = measurement_series_list_data_selectors
        self.measurement_threshold_relation_list_data_selectors = measurement_threshold_relation_list_data_selectors
        self.messaging_list_data_selectors = messaging_list_data_selectors
        self.network_management_device_description_list_data_selectors = network_management_device_description_list_data_selectors
        self.network_management_entity_description_list_data_selectors = network_management_entity_description_list_data_selectors
        self.network_management_feature_description_list_data_selectors = network_management_feature_description_list_data_selectors
        self.node_management_binding_data_selectors = node_management_binding_data_selectors
        self.node_management_destination_list_data_selectors = node_management_destination_list_data_selectors
        self.node_management_detailed_discovery_data_selectors = node_management_detailed_discovery_data_selectors
        self.node_management_subscription_data_selectors = node_management_subscription_data_selectors
        self.node_management_use_case_data_selectors = node_management_use_case_data_selectors
        self.operating_constraints_duration_list_data_selectors = operating_constraints_duration_list_data_selectors
        self.operating_constraints_interrupt_list_data_selectors = operating_constraints_interrupt_list_data_selectors
        self.operating_constraints_power_description_list_data_selectors = operating_constraints_power_description_list_data_selectors
        self.operating_constraints_power_level_list_data_selectors = operating_constraints_power_level_list_data_selectors
        self.operating_constraints_power_range_list_data_selectors = operating_constraints_power_range_list_data_selectors
        self.operating_constraints_resume_implication_list_data_selectors = operating_constraints_resume_implication_list_data_selectors
        self.power_sequence_alternatives_relation_list_data_selectors = power_sequence_alternatives_relation_list_data_selectors
        self.power_sequence_description_list_data_selectors = power_sequence_description_list_data_selectors
        self.power_sequence_price_list_data_selectors = power_sequence_price_list_data_selectors
        self.power_sequence_schedule_constraints_list_data_selectors = power_sequence_schedule_constraints_list_data_selectors
        self.power_sequence_schedule_list_data_selectors = power_sequence_schedule_list_data_selectors
        self.power_sequence_schedule_preference_list_data_selectors = power_sequence_schedule_preference_list_data_selectors
        self.power_sequence_state_list_data_selectors = power_sequence_state_list_data_selectors
        self.power_time_slot_schedule_constraints_list_data_selectors = power_time_slot_schedule_constraints_list_data_selectors
        self.power_time_slot_schedule_list_data_selectors = power_time_slot_schedule_list_data_selectors
        self.power_time_slot_value_list_data_selectors = power_time_slot_value_list_data_selectors
        self.sensing_list_data_selectors = sensing_list_data_selectors
        self.session_identification_list_data_selectors = session_identification_list_data_selectors
        self.session_measurement_relation_list_data_selectors = session_measurement_relation_list_data_selectors
        self.setpoint_constraints_list_data_selectors = setpoint_constraints_list_data_selectors
        self.setpoint_description_list_data_selectors = setpoint_description_list_data_selectors
        self.setpoint_list_data_selectors = setpoint_list_data_selectors
        self.smart_energy_management_ps_data_selectors = smart_energy_management_ps_data_selectors
        self.smart_energy_management_ps_price_data_selectors = smart_energy_management_ps_price_data_selectors
        self.specification_version_list_data_selectors = specification_version_list_data_selectors
        self.state_information_list_data_selectors = state_information_list_data_selectors
        self.subscription_management_entry_list_data_selectors = subscription_management_entry_list_data_selectors
        self.supply_condition_description_list_data_selectors = supply_condition_description_list_data_selectors
        self.supply_condition_list_data_selectors = supply_condition_list_data_selectors
        self.supply_condition_threshold_relation_list_data_selectors = supply_condition_threshold_relation_list_data_selectors
        self.tariff_boundary_relation_list_data_selectors = tariff_boundary_relation_list_data_selectors
        self.tariff_description_list_data_selectors = tariff_description_list_data_selectors
        self.tariff_list_data_selectors = tariff_list_data_selectors
        self.tariff_tier_relation_list_data_selectors = tariff_tier_relation_list_data_selectors
        self.task_management_job_description_list_data_selectors = task_management_job_description_list_data_selectors
        self.task_management_job_list_data_selectors = task_management_job_list_data_selectors
        self.task_management_job_relation_list_data_selectors = task_management_job_relation_list_data_selectors
        self.threshold_constraints_list_data_selectors = threshold_constraints_list_data_selectors
        self.threshold_description_list_data_selectors = threshold_description_list_data_selectors
        self.threshold_list_data_selectors = threshold_list_data_selectors
        self.tier_boundary_description_list_data_selectors = tier_boundary_description_list_data_selectors
        self.tier_boundary_list_data_selectors = tier_boundary_list_data_selectors
        self.tier_description_list_data_selectors = tier_description_list_data_selectors
        self.tier_incentive_relation_list_data_selectors = tier_incentive_relation_list_data_selectors
        self.tier_list_data_selectors = tier_list_data_selectors
        self.time_series_constraints_list_data_selectors = time_series_constraints_list_data_selectors
        self.time_series_description_list_data_selectors = time_series_description_list_data_selectors
        self.time_series_list_data_selectors = time_series_list_data_selectors
        self.time_table_constraints_list_data_selectors = time_table_constraints_list_data_selectors
        self.time_table_description_list_data_selectors = time_table_description_list_data_selectors
        self.time_table_list_data_selectors = time_table_list_data_selectors
        self.use_case_information_list_data_selectors = use_case_information_list_data_selectors

        if not isinstance(self.alarm_list_data_selectors, AlarmListDataSelectorsType):
            raise TypeError("alarm_list_data_selectors is not of type AlarmListDataSelectorsType")
        
        if not isinstance(self.bill_constraints_list_data_selectors, BillConstraintsListDataSelectorsType):
            raise TypeError("bill_constraints_list_data_selectors is not of type BillConstraintsListDataSelectorsType")
        
        if not isinstance(self.bill_description_list_data_selectors, BillDescriptionListDataSelectorsType):
            raise TypeError("bill_description_list_data_selectors is not of type BillDescriptionListDataSelectorsType")
        
        if not isinstance(self.bill_list_data_selectors, BillListDataSelectorsType):
            raise TypeError("bill_list_data_selectors is not of type BillListDataSelectorsType")
        
        if not isinstance(self.binding_management_entry_list_data_selectors, BindingManagementEntryListDataSelectorsType):
            raise TypeError("binding_management_entry_list_data_selectors is not of type BindingManagementEntryListDataSelectorsType")
        
        if not isinstance(self.commodity_list_data_selectors, CommodityListDataSelectorsType):
            raise TypeError("commodity_list_data_selectors is not of type CommodityListDataSelectorsType")
        
        if not isinstance(self.device_configuration_key_value_constraints_list_data_selectors, DeviceConfigurationKeyValueConstraintsListDataSelectorsType):
            raise TypeError("device_configuration_key_value_constraints_list_data_selectors is not of type DeviceConfigurationKeyValueConstraintsListDataSelectorsType")
        
        if not isinstance(self.device_configuration_key_value_description_list_data_selectors, DeviceConfigurationKeyValueDescriptionListDataSelectorsType):
            raise TypeError("device_configuration_key_value_description_list_data_selectors is not of type DeviceConfigurationKeyValueDescriptionListDataSelectorsType")
        
        if not isinstance(self.device_configuration_key_value_list_data_selectors, DeviceConfigurationKeyValueListDataSelectorsType):
            raise TypeError("device_configuration_key_value_list_data_selectors is not of type DeviceConfigurationKeyValueListDataSelectorsType")
        
        if not isinstance(self.direct_control_activity_list_data_selectors, DirectControlActivityListDataSelectorsType):
            raise TypeError("direct_control_activity_list_data_selectors is not of type DirectControlActivityListDataSelectorsType")
        
        if not isinstance(self.electrical_connection_characteristic_list_data_selectors, ElectricalConnectionCharacteristicListDataSelectorsType):
            raise TypeError("electrical_connection_characteristic_list_data_selectors is not of type ElectricalConnectionCharacteristicListDataSelectorsType")
        
        if not isinstance(self.electrical_connection_description_list_data_selectors, ElectricalConnectionDescriptionListDataSelectorsType):
            raise TypeError("electrical_connection_description_list_data_selectors is not of type ElectricalConnectionDescriptionListDataSelectorsType")
        
        if not isinstance(self.electrical_connection_parameter_description_list_data_selectors, ElectricalConnectionParameterDescriptionListDataSelectorsType):
            raise TypeError("electrical_connection_parameter_description_list_data_selectors is not of type ElectricalConnectionParameterDescriptionListDataSelectorsType")
        
        if not isinstance(self.electrical_connection_permitted_value_set_list_data_selectors, ElectricalConnectionPermittedValueSetListDataSelectorsType):
            raise TypeError("electrical_connection_permitted_value_set_list_data_selectors is not of type ElectricalConnectionPermittedValueSetListDataSelectorsType")
        
        if not isinstance(self.electrical_connection_state_list_data_selectors, ElectricalConnectionStateListDataSelectorsType):
            raise TypeError("electrical_connection_state_list_data_selectors is not of type ElectricalConnectionStateListDataSelectorsType")
        
        if not isinstance(self.hvac_operation_mode_description_list_data_selectors, HvacOperationModeDescriptionListDataSelectorsType):
            raise TypeError("hvac_operation_mode_description_list_data_selectors is not of type HvacOperationModeDescriptionListDataSelectorsType")
        
        if not isinstance(self.hvac_overrun_description_list_data_selectors, HvacOverrunDescriptionListDataSelectorsType):
            raise TypeError("hvac_overrun_description_list_data_selectors is not of type HvacOverrunDescriptionListDataSelectorsType")
        
        if not isinstance(self.hvac_overrun_list_data_selectors, HvacOverrunListDataSelectorsType):
            raise TypeError("hvac_overrun_list_data_selectors is not of type HvacOverrunListDataSelectorsType")
        
        if not isinstance(self.hvac_system_function_description_list_data_selectors, HvacSystemFunctionDescriptionListDataSelectorsType):
            raise TypeError("hvac_system_function_description_list_data_selectors is not of type HvacSystemFunctionDescriptionListDataSelectorsType")
        
        if not isinstance(self.hvac_system_function_list_data_selectors, HvacSystemFunctionListDataSelectorsType):
            raise TypeError("hvac_system_function_list_data_selectors is not of type HvacSystemFunctionListDataSelectorsType")
        
        if not isinstance(self.hvac_system_function_operation_mode_relation_list_data_selectors, HvacSystemFunctionOperationModeRelationListDataSelectorsType):
            raise TypeError("hvac_system_function_operation_mode_relation_list_data_selectors is not of type HvacSystemFunctionOperationModeRelationListDataSelectorsType")
        
        if not isinstance(self.hvac_system_function_power_sequence_relation_list_data_selectors, HvacSystemFunctionPowerSequenceRelationListDataSelectorsType):
            raise TypeError("hvac_system_function_power_sequence_relation_list_data_selectors is not of type HvacSystemFunctionPowerSequenceRelationListDataSelectorsType")
        
        if not isinstance(self.hvac_system_function_setpoint_relation_list_data_selectors, HvacSystemFunctionSetpointRelationListDataSelectorsType):
            raise TypeError("hvac_system_function_setpoint_relation_list_data_selectors is not of type HvacSystemFunctionSetpointRelationListDataSelectorsType")
        
        if not isinstance(self.identification_list_data_selectors, IdentificationListDataSelectorsType):
            raise TypeError("identification_list_data_selectors is not of type IdentificationListDataSelectorsType")
        
        if not isinstance(self.incentive_description_list_data_selectors, IncentiveDescriptionListDataSelectorsType):
            raise TypeError("incentive_description_list_data_selectors is not of type IncentiveDescriptionListDataSelectorsType")
        
        if not isinstance(self.incentive_list_data_selectors, IncentiveListDataSelectorsType):
            raise TypeError("incentive_list_data_selectors is not of type IncentiveListDataSelectorsType")
        
        if not isinstance(self.incentive_table_constraints_data_selectors, IncentiveTableConstraintsDataSelectorsType):
            raise TypeError("incentive_table_constraints_data_selectors is not of type IncentiveTableConstraintsDataSelectorsType")
        
        if not isinstance(self.incentive_table_data_selectors, IncentiveTableDataSelectorsType):
            raise TypeError("incentive_table_data_selectors is not of type IncentiveTableDataSelectorsType")
        
        if not isinstance(self.incentive_table_description_data_selectors, IncentiveTableDescriptionDataSelectorsType):
            raise TypeError("incentive_table_description_data_selectors is not of type IncentiveTableDescriptionDataSelectorsType")
        
        if not isinstance(self.load_control_event_list_data_selectors, LoadControlEventListDataSelectorsType):
            raise TypeError("load_control_event_list_data_selectors is not of type LoadControlEventListDataSelectorsType")
        
        if not isinstance(self.load_control_limit_constraints_list_data_selectors, LoadControlLimitConstraintsListDataSelectorsType):
            raise TypeError("load_control_limit_constraints_list_data_selectors is not of type LoadControlLimitConstraintsListDataSelectorsType")
        
        if not isinstance(self.load_control_limit_description_list_data_selectors, LoadControlLimitDescriptionListDataSelectorsType):
            raise TypeError("load_control_limit_description_list_data_selectors is not of type LoadControlLimitDescriptionListDataSelectorsType")
        
        if not isinstance(self.load_control_limit_list_data_selectors, LoadControlLimitListDataSelectorsType):
            raise TypeError("load_control_limit_list_data_selectors is not of type LoadControlLimitListDataSelectorsType")
        
        if not isinstance(self.load_control_state_list_data_selectors, LoadControlStateListDataSelectorsType):
            raise TypeError("load_control_state_list_data_selectors is not of type LoadControlStateListDataSelectorsType")
        
        if not isinstance(self.measurement_constraints_list_data_selectors, MeasurementConstraintsListDataSelectorsType):
            raise TypeError("measurement_constraints_list_data_selectors is not of type MeasurementConstraintsListDataSelectorsType")
        
        if not isinstance(self.measurement_description_list_data_selectors, MeasurementDescriptionListDataSelectorsType):
            raise TypeError("measurement_description_list_data_selectors is not of type MeasurementDescriptionListDataSelectorsType")
        
        if not isinstance(self.measurement_list_data_selectors, MeasurementListDataSelectorsType):
            raise TypeError("measurement_list_data_selectors is not of type MeasurementListDataSelectorsType")
        
        if not isinstance(self.measurement_series_list_data_selectors, MeasurementSeriesListDataSelectorsType):
            raise TypeError("measurement_series_list_data_selectors is not of type MeasurementSeriesListDataSelectorsType")
        
        if not isinstance(self.measurement_threshold_relation_list_data_selectors, MeasurementThresholdRelationListDataSelectorsType):
            raise TypeError("measurement_threshold_relation_list_data_selectors is not of type MeasurementThresholdRelationListDataSelectorsType")
        
        if not isinstance(self.messaging_list_data_selectors, MessagingListDataSelectorsType):
            raise TypeError("messaging_list_data_selectors is not of type MessagingListDataSelectorsType")
        
        if not isinstance(self.network_management_device_description_list_data_selectors, NetworkManagementDeviceDescriptionListDataSelectorsType):
            raise TypeError("network_management_device_description_list_data_selectors is not of type NetworkManagementDeviceDescriptionListDataSelectorsType")
        
        if not isinstance(self.network_management_entity_description_list_data_selectors, NetworkManagementEntityDescriptionListDataSelectorsType):
            raise TypeError("network_management_entity_description_list_data_selectors is not of type NetworkManagementEntityDescriptionListDataSelectorsType")
        
        if not isinstance(self.network_management_feature_description_list_data_selectors, NetworkManagementFeatureDescriptionListDataSelectorsType):
            raise TypeError("network_management_feature_description_list_data_selectors is not of type NetworkManagementFeatureDescriptionListDataSelectorsType")
        
        if not isinstance(self.node_management_binding_data_selectors, NodeManagementBindingDataSelectorsType):
            raise TypeError("node_management_binding_data_selectors is not of type NodeManagementBindingDataSelectorsType")
        
        if not isinstance(self.node_management_destination_list_data_selectors, NodeManagementDestinationListDataSelectorsType):
            raise TypeError("node_management_destination_list_data_selectors is not of type NodeManagementDestinationListDataSelectorsType")
        
        if not isinstance(self.node_management_detailed_discovery_data_selectors, NodeManagementDetailedDiscoveryDataSelectorsType):
            raise TypeError("node_management_detailed_discovery_data_selectors is not of type NodeManagementDetailedDiscoveryDataSelectorsType")
        
        if not isinstance(self.node_management_subscription_data_selectors, NodeManagementSubscriptionDataSelectorsType):
            raise TypeError("node_management_subscription_data_selectors is not of type NodeManagementSubscriptionDataSelectorsType")
        
        if not isinstance(self.node_management_use_case_data_selectors, NodeManagementUseCaseDataSelectorsType):
            raise TypeError("node_management_use_case_data_selectors is not of type NodeManagementUseCaseDataSelectorsType")
        
        if not isinstance(self.operating_constraints_duration_list_data_selectors, OperatingConstraintsDurationListDataSelectorsType):
            raise TypeError("operating_constraints_duration_list_data_selectors is not of type OperatingConstraintsDurationListDataSelectorsType")
        
        if not isinstance(self.operating_constraints_interrupt_list_data_selectors, OperatingConstraintsInterruptListDataSelectorsType):
            raise TypeError("operating_constraints_interrupt_list_data_selectors is not of type OperatingConstraintsInterruptListDataSelectorsType")
        
        if not isinstance(self.operating_constraints_power_description_list_data_selectors, OperatingConstraintsPowerDescriptionListDataSelectorsType):
            raise TypeError("operating_constraints_power_description_list_data_selectors is not of type OperatingConstraintsPowerDescriptionListDataSelectorsType")
        
        if not isinstance(self.operating_constraints_power_level_list_data_selectors, OperatingConstraintsPowerLevelListDataSelectorsType):
            raise TypeError("operating_constraints_power_level_list_data_selectors is not of type OperatingConstraintsPowerLevelListDataSelectorsType")
        
        if not isinstance(self.operating_constraints_power_range_list_data_selectors, OperatingConstraintsPowerRangeListDataSelectorsType):
            raise TypeError("operating_constraints_power_range_list_data_selectors is not of type OperatingConstraintsPowerRangeListDataSelectorsType")
        
        if not isinstance(self.operating_constraints_resume_implication_list_data_selectors, OperatingConstraintsResumeImplicationListDataSelectorsType):
            raise TypeError("operating_constraints_resume_implication_list_data_selectors is not of type OperatingConstraintsResumeImplicationListDataSelectorsType")
        
        if not isinstance(self.power_sequence_alternatives_relation_list_data_selectors, PowerSequenceAlternativesRelationListDataSelectorsType):
            raise TypeError("power_sequence_alternatives_relation_list_data_selectors is not of type PowerSequenceAlternativesRelationListDataSelectorsType")
        
        if not isinstance(self.power_sequence_description_list_data_selectors, PowerSequenceDescriptionListDataSelectorsType):
            raise TypeError("power_sequence_description_list_data_selectors is not of type PowerSequenceDescriptionListDataSelectorsType")
        
        if not isinstance(self.power_sequence_price_list_data_selectors, PowerSequencePriceListDataSelectorsType):
            raise TypeError("power_sequence_price_list_data_selectors is not of type PowerSequencePriceListDataSelectorsType")
        
        if not isinstance(self.power_sequence_schedule_constraints_list_data_selectors, PowerSequenceScheduleConstraintsListDataSelectorsType):
            raise TypeError("power_sequence_schedule_constraints_list_data_selectors is not of type PowerSequenceScheduleConstraintsListDataSelectorsType")
        
        if not isinstance(self.power_sequence_schedule_list_data_selectors, PowerSequenceScheduleListDataSelectorsType):
            raise TypeError("power_sequence_schedule_list_data_selectors is not of type PowerSequenceScheduleListDataSelectorsType")
        
        if not isinstance(self.power_sequence_schedule_preference_list_data_selectors, PowerSequenceSchedulePreferenceListDataSelectorsType):
            raise TypeError("power_sequence_schedule_preference_list_data_selectors is not of type PowerSequenceSchedulePreferenceListDataSelectorsType")
        
        if not isinstance(self.power_sequence_state_list_data_selectors, PowerSequenceStateListDataSelectorsType):
            raise TypeError("power_sequence_state_list_data_selectors is not of type PowerSequenceStateListDataSelectorsType")
        
        if not isinstance(self.power_time_slot_schedule_constraints_list_data_selectors, PowerTimeSlotScheduleConstraintsListDataSelectorsType):
            raise TypeError("power_time_slot_schedule_constraints_list_data_selectors is not of type PowerTimeSlotScheduleConstraintsListDataSelectorsType")
        
        if not isinstance(self.power_time_slot_schedule_list_data_selectors, PowerTimeSlotScheduleListDataSelectorsType):
            raise TypeError("power_time_slot_schedule_list_data_selectors is not of type PowerTimeSlotScheduleListDataSelectorsType")
        
        if not isinstance(self.power_time_slot_value_list_data_selectors, PowerTimeSlotValueListDataSelectorsType):
            raise TypeError("power_time_slot_value_list_data_selectors is not of type PowerTimeSlotValueListDataSelectorsType")
        
        if not isinstance(self.sensing_list_data_selectors, SensingListDataSelectorsType):
            raise TypeError("sensing_list_data_selectors is not of type SensingListDataSelectorsType")
        
        if not isinstance(self.session_identification_list_data_selectors, SessionIdentificationListDataSelectorsType):
            raise TypeError("session_identification_list_data_selectors is not of type SessionIdentificationListDataSelectorsType")
        
        if not isinstance(self.session_measurement_relation_list_data_selectors, SessionMeasurementRelationListDataSelectorsType):
            raise TypeError("session_measurement_relation_list_data_selectors is not of type SessionMeasurementRelationListDataSelectorsType")
        
        if not isinstance(self.setpoint_constraints_list_data_selectors, SetpointConstraintsListDataSelectorsType):
            raise TypeError("setpoint_constraints_list_data_selectors is not of type SetpointConstraintsListDataSelectorsType")
        
        if not isinstance(self.setpoint_description_list_data_selectors, SetpointDescriptionListDataSelectorsType):
            raise TypeError("setpoint_description_list_data_selectors is not of type SetpointDescriptionListDataSelectorsType")
        
        if not isinstance(self.setpoint_list_data_selectors, SetpointListDataSelectorsType):
            raise TypeError("setpoint_list_data_selectors is not of type SetpointListDataSelectorsType")
        
        if not isinstance(self.smart_energy_management_ps_data_selectors, SmartEnergyManagementPsDataSelectorsType):
            raise TypeError("smart_energy_management_ps_data_selectors is not of type SmartEnergyManagementPsDataSelectorsType")
        
        if not isinstance(self.smart_energy_management_ps_price_data_selectors, SmartEnergyManagementPsPriceDataSelectorsType):
            raise TypeError("smart_energy_management_ps_price_data_selectors is not of type SmartEnergyManagementPsPriceDataSelectorsType")
        
        if not isinstance(self.specification_version_list_data_selectors, SpecificationVersionListDataSelectorsType):
            raise TypeError("specification_version_list_data_selectors is not of type SpecificationVersionListDataSelectorsType")
        
        if not isinstance(self.state_information_list_data_selectors, StateInformationListDataSelectorsType):
            raise TypeError("state_information_list_data_selectors is not of type StateInformationListDataSelectorsType")
        
        if not isinstance(self.subscription_management_entry_list_data_selectors, SubscriptionManagementEntryListDataSelectorsType):
            raise TypeError("subscription_management_entry_list_data_selectors is not of type SubscriptionManagementEntryListDataSelectorsType")
        
        if not isinstance(self.supply_condition_description_list_data_selectors, SupplyConditionDescriptionListDataSelectorsType):
            raise TypeError("supply_condition_description_list_data_selectors is not of type SupplyConditionDescriptionListDataSelectorsType")
        
        if not isinstance(self.supply_condition_list_data_selectors, SupplyConditionListDataSelectorsType):
            raise TypeError("supply_condition_list_data_selectors is not of type SupplyConditionListDataSelectorsType")
        
        if not isinstance(self.supply_condition_threshold_relation_list_data_selectors, SupplyConditionThresholdRelationListDataSelectorsType):
            raise TypeError("supply_condition_threshold_relation_list_data_selectors is not of type SupplyConditionThresholdRelationListDataSelectorsType")
        
        if not isinstance(self.tariff_boundary_relation_list_data_selectors, TariffBoundaryRelationListDataSelectorsType):
            raise TypeError("tariff_boundary_relation_list_data_selectors is not of type TariffBoundaryRelationListDataSelectorsType")
        
        if not isinstance(self.tariff_description_list_data_selectors, TariffDescriptionListDataSelectorsType):
            raise TypeError("tariff_description_list_data_selectors is not of type TariffDescriptionListDataSelectorsType")
        
        if not isinstance(self.tariff_list_data_selectors, TariffListDataSelectorsType):
            raise TypeError("tariff_list_data_selectors is not of type TariffListDataSelectorsType")
        
        if not isinstance(self.tariff_tier_relation_list_data_selectors, TariffTierRelationListDataSelectorsType):
            raise TypeError("tariff_tier_relation_list_data_selectors is not of type TariffTierRelationListDataSelectorsType")
        
        if not isinstance(self.task_management_job_description_list_data_selectors, TaskManagementJobDescriptionListDataSelectorsType):
            raise TypeError("task_management_job_description_list_data_selectors is not of type TaskManagementJobDescriptionListDataSelectorsType")
        
        if not isinstance(self.task_management_job_list_data_selectors, TaskManagementJobListDataSelectorsType):
            raise TypeError("task_management_job_list_data_selectors is not of type TaskManagementJobListDataSelectorsType")
        
        if not isinstance(self.task_management_job_relation_list_data_selectors, TaskManagementJobRelationListDataSelectorsType):
            raise TypeError("task_management_job_relation_list_data_selectors is not of type TaskManagementJobRelationListDataSelectorsType")
        
        if not isinstance(self.threshold_constraints_list_data_selectors, ThresholdConstraintsListDataSelectorsType):
            raise TypeError("threshold_constraints_list_data_selectors is not of type ThresholdConstraintsListDataSelectorsType")
        
        if not isinstance(self.threshold_description_list_data_selectors, ThresholdDescriptionListDataSelectorsType):
            raise TypeError("threshold_description_list_data_selectors is not of type ThresholdDescriptionListDataSelectorsType")
        
        if not isinstance(self.threshold_list_data_selectors, ThresholdListDataSelectorsType):
            raise TypeError("threshold_list_data_selectors is not of type ThresholdListDataSelectorsType")
        
        if not isinstance(self.tier_boundary_description_list_data_selectors, TierBoundaryDescriptionListDataSelectorsType):
            raise TypeError("tier_boundary_description_list_data_selectors is not of type TierBoundaryDescriptionListDataSelectorsType")
        
        if not isinstance(self.tier_boundary_list_data_selectors, TierBoundaryListDataSelectorsType):
            raise TypeError("tier_boundary_list_data_selectors is not of type TierBoundaryListDataSelectorsType")
        
        if not isinstance(self.tier_description_list_data_selectors, TierDescriptionListDataSelectorsType):
            raise TypeError("tier_description_list_data_selectors is not of type TierDescriptionListDataSelectorsType")
        
        if not isinstance(self.tier_incentive_relation_list_data_selectors, TierIncentiveRelationListDataSelectorsType):
            raise TypeError("tier_incentive_relation_list_data_selectors is not of type TierIncentiveRelationListDataSelectorsType")
        
        if not isinstance(self.tier_list_data_selectors, TierListDataSelectorsType):
            raise TypeError("tier_list_data_selectors is not of type TierListDataSelectorsType")
        
        if not isinstance(self.time_series_constraints_list_data_selectors, TimeSeriesConstraintsListDataSelectorsType):
            raise TypeError("time_series_constraints_list_data_selectors is not of type TimeSeriesConstraintsListDataSelectorsType")
        
        if not isinstance(self.time_series_description_list_data_selectors, TimeSeriesDescriptionListDataSelectorsType):
            raise TypeError("time_series_description_list_data_selectors is not of type TimeSeriesDescriptionListDataSelectorsType")
        
        if not isinstance(self.time_series_list_data_selectors, TimeSeriesListDataSelectorsType):
            raise TypeError("time_series_list_data_selectors is not of type TimeSeriesListDataSelectorsType")
        
        if not isinstance(self.time_table_constraints_list_data_selectors, TimeTableConstraintsListDataSelectorsType):
            raise TypeError("time_table_constraints_list_data_selectors is not of type TimeTableConstraintsListDataSelectorsType")
        
        if not isinstance(self.time_table_description_list_data_selectors, TimeTableDescriptionListDataSelectorsType):
            raise TypeError("time_table_description_list_data_selectors is not of type TimeTableDescriptionListDataSelectorsType")
        
        if not isinstance(self.time_table_list_data_selectors, TimeTableListDataSelectorsType):
            raise TypeError("time_table_list_data_selectors is not of type TimeTableListDataSelectorsType")
        
        if not isinstance(self.use_case_information_list_data_selectors, UseCaseInformationListDataSelectorsType):
            raise TypeError("use_case_information_list_data_selectors is not of type UseCaseInformationListDataSelectorsType")
        
    def get_data(self): # ChoiceType

        msg_data = []
        
        if self.alarm_list_data_selectors is not None:
            msg_data.append({"alarmListDataSelectors": self.alarm_list_data_selectors.get_data()})
        if self.bill_constraints_list_data_selectors is not None:
            msg_data.append({"billConstraintsListDataSelectors": self.bill_constraints_list_data_selectors.get_data()})
        if self.bill_description_list_data_selectors is not None:
            msg_data.append({"billDescriptionListDataSelectors": self.bill_description_list_data_selectors.get_data()})
        if self.bill_list_data_selectors is not None:
            msg_data.append({"billListDataSelectors": self.bill_list_data_selectors.get_data()})
        if self.binding_management_entry_list_data_selectors is not None:
            msg_data.append({"bindingManagementEntryListDataSelectors": self.binding_management_entry_list_data_selectors.get_data()})
        if self.commodity_list_data_selectors is not None:
            msg_data.append({"commodityListDataSelectors": self.commodity_list_data_selectors.get_data()})
        if self.device_configuration_key_value_constraints_list_data_selectors is not None:
            msg_data.append({"deviceConfigurationKeyValueConstraintsListDataSelectors": self.device_configuration_key_value_constraints_list_data_selectors.get_data()})
        if self.device_configuration_key_value_description_list_data_selectors is not None:
            msg_data.append({"deviceConfigurationKeyValueDescriptionListDataSelectors": self.device_configuration_key_value_description_list_data_selectors.get_data()})
        if self.device_configuration_key_value_list_data_selectors is not None:
            msg_data.append({"deviceConfigurationKeyValueListDataSelectors": self.device_configuration_key_value_list_data_selectors.get_data()})
        if self.direct_control_activity_list_data_selectors is not None:
            msg_data.append({"directControlActivityListDataSelectors": self.direct_control_activity_list_data_selectors.get_data()})
        if self.electrical_connection_characteristic_list_data_selectors is not None:
            msg_data.append({"electricalConnectionCharacteristicListDataSelectors": self.electrical_connection_characteristic_list_data_selectors.get_data()})
        if self.electrical_connection_description_list_data_selectors is not None:
            msg_data.append({"electricalConnectionDescriptionListDataSelectors": self.electrical_connection_description_list_data_selectors.get_data()})
        if self.electrical_connection_parameter_description_list_data_selectors is not None:
            msg_data.append({"electricalConnectionParameterDescriptionListDataSelectors": self.electrical_connection_parameter_description_list_data_selectors.get_data()})
        if self.electrical_connection_permitted_value_set_list_data_selectors is not None:
            msg_data.append({"electricalConnectionPermittedValueSetListDataSelectors": self.electrical_connection_permitted_value_set_list_data_selectors.get_data()})
        if self.electrical_connection_state_list_data_selectors is not None:
            msg_data.append({"electricalConnectionStateListDataSelectors": self.electrical_connection_state_list_data_selectors.get_data()})
        if self.hvac_operation_mode_description_list_data_selectors is not None:
            msg_data.append({"hvacOperationModeDescriptionListDataSelectors": self.hvac_operation_mode_description_list_data_selectors.get_data()})
        if self.hvac_overrun_description_list_data_selectors is not None:
            msg_data.append({"hvacOverrunDescriptionListDataSelectors": self.hvac_overrun_description_list_data_selectors.get_data()})
        if self.hvac_overrun_list_data_selectors is not None:
            msg_data.append({"hvacOverrunListDataSelectors": self.hvac_overrun_list_data_selectors.get_data()})
        if self.hvac_system_function_description_list_data_selectors is not None:
            msg_data.append({"hvacSystemFunctionDescriptionListDataSelectors": self.hvac_system_function_description_list_data_selectors.get_data()})
        if self.hvac_system_function_list_data_selectors is not None:
            msg_data.append({"hvacSystemFunctionListDataSelectors": self.hvac_system_function_list_data_selectors.get_data()})
        if self.hvac_system_function_operation_mode_relation_list_data_selectors is not None:
            msg_data.append({"hvacSystemFunctionOperationModeRelationListDataSelectors": self.hvac_system_function_operation_mode_relation_list_data_selectors.get_data()})
        if self.hvac_system_function_power_sequence_relation_list_data_selectors is not None:
            msg_data.append({"hvacSystemFunctionPowerSequenceRelationListDataSelectors": self.hvac_system_function_power_sequence_relation_list_data_selectors.get_data()})
        if self.hvac_system_function_setpoint_relation_list_data_selectors is not None:
            msg_data.append({"hvacSystemFunctionSetpointRelationListDataSelectors": self.hvac_system_function_setpoint_relation_list_data_selectors.get_data()})
        if self.identification_list_data_selectors is not None:
            msg_data.append({"identificationListDataSelectors": self.identification_list_data_selectors.get_data()})
        if self.incentive_description_list_data_selectors is not None:
            msg_data.append({"incentiveDescriptionListDataSelectors": self.incentive_description_list_data_selectors.get_data()})
        if self.incentive_list_data_selectors is not None:
            msg_data.append({"incentiveListDataSelectors": self.incentive_list_data_selectors.get_data()})
        if self.incentive_table_constraints_data_selectors is not None:
            msg_data.append({"incentiveTableConstraintsDataSelectors": self.incentive_table_constraints_data_selectors.get_data()})
        if self.incentive_table_data_selectors is not None:
            msg_data.append({"incentiveTableDataSelectors": self.incentive_table_data_selectors.get_data()})
        if self.incentive_table_description_data_selectors is not None:
            msg_data.append({"incentiveTableDescriptionDataSelectors": self.incentive_table_description_data_selectors.get_data()})
        if self.load_control_event_list_data_selectors is not None:
            msg_data.append({"loadControlEventListDataSelectors": self.load_control_event_list_data_selectors.get_data()})
        if self.load_control_limit_constraints_list_data_selectors is not None:
            msg_data.append({"loadControlLimitConstraintsListDataSelectors": self.load_control_limit_constraints_list_data_selectors.get_data()})
        if self.load_control_limit_description_list_data_selectors is not None:
            msg_data.append({"loadControlLimitDescriptionListDataSelectors": self.load_control_limit_description_list_data_selectors.get_data()})
        if self.load_control_limit_list_data_selectors is not None:
            msg_data.append({"loadControlLimitListDataSelectors": self.load_control_limit_list_data_selectors.get_data()})
        if self.load_control_state_list_data_selectors is not None:
            msg_data.append({"loadControlStateListDataSelectors": self.load_control_state_list_data_selectors.get_data()})
        if self.measurement_constraints_list_data_selectors is not None:
            msg_data.append({"measurementConstraintsListDataSelectors": self.measurement_constraints_list_data_selectors.get_data()})
        if self.measurement_description_list_data_selectors is not None:
            msg_data.append({"measurementDescriptionListDataSelectors": self.measurement_description_list_data_selectors.get_data()})
        if self.measurement_list_data_selectors is not None:
            msg_data.append({"measurementListDataSelectors": self.measurement_list_data_selectors.get_data()})
        if self.measurement_series_list_data_selectors is not None:
            msg_data.append({"measurementSeriesListDataSelectors": self.measurement_series_list_data_selectors.get_data()})
        if self.measurement_threshold_relation_list_data_selectors is not None:
            msg_data.append({"measurementThresholdRelationListDataSelectors": self.measurement_threshold_relation_list_data_selectors.get_data()})
        if self.messaging_list_data_selectors is not None:
            msg_data.append({"messagingListDataSelectors": self.messaging_list_data_selectors.get_data()})
        if self.network_management_device_description_list_data_selectors is not None:
            msg_data.append({"networkManagementDeviceDescriptionListDataSelectors": self.network_management_device_description_list_data_selectors.get_data()})
        if self.network_management_entity_description_list_data_selectors is not None:
            msg_data.append({"networkManagementEntityDescriptionListDataSelectors": self.network_management_entity_description_list_data_selectors.get_data()})
        if self.network_management_feature_description_list_data_selectors is not None:
            msg_data.append({"networkManagementFeatureDescriptionListDataSelectors": self.network_management_feature_description_list_data_selectors.get_data()})
        if self.node_management_binding_data_selectors is not None:
            msg_data.append({"nodeManagementBindingDataSelectors": self.node_management_binding_data_selectors.get_data()})
        if self.node_management_destination_list_data_selectors is not None:
            msg_data.append({"nodeManagementDestinationListDataSelectors": self.node_management_destination_list_data_selectors.get_data()})
        if self.node_management_detailed_discovery_data_selectors is not None:
            msg_data.append({"nodeManagementDetailedDiscoveryDataSelectors": self.node_management_detailed_discovery_data_selectors.get_data()})
        if self.node_management_subscription_data_selectors is not None:
            msg_data.append({"nodeManagementSubscriptionDataSelectors": self.node_management_subscription_data_selectors.get_data()})
        if self.node_management_use_case_data_selectors is not None:
            msg_data.append({"nodeManagementUseCaseDataSelectors": self.node_management_use_case_data_selectors.get_data()})
        if self.operating_constraints_duration_list_data_selectors is not None:
            msg_data.append({"operatingConstraintsDurationListDataSelectors": self.operating_constraints_duration_list_data_selectors.get_data()})
        if self.operating_constraints_interrupt_list_data_selectors is not None:
            msg_data.append({"operatingConstraintsInterruptListDataSelectors": self.operating_constraints_interrupt_list_data_selectors.get_data()})
        if self.operating_constraints_power_description_list_data_selectors is not None:
            msg_data.append({"operatingConstraintsPowerDescriptionListDataSelectors": self.operating_constraints_power_description_list_data_selectors.get_data()})
        if self.operating_constraints_power_level_list_data_selectors is not None:
            msg_data.append({"operatingConstraintsPowerLevelListDataSelectors": self.operating_constraints_power_level_list_data_selectors.get_data()})
        if self.operating_constraints_power_range_list_data_selectors is not None:
            msg_data.append({"operatingConstraintsPowerRangeListDataSelectors": self.operating_constraints_power_range_list_data_selectors.get_data()})
        if self.operating_constraints_resume_implication_list_data_selectors is not None:
            msg_data.append({"operatingConstraintsResumeImplicationListDataSelectors": self.operating_constraints_resume_implication_list_data_selectors.get_data()})
        if self.power_sequence_alternatives_relation_list_data_selectors is not None:
            msg_data.append({"powerSequenceAlternativesRelationListDataSelectors": self.power_sequence_alternatives_relation_list_data_selectors.get_data()})
        if self.power_sequence_description_list_data_selectors is not None:
            msg_data.append({"powerSequenceDescriptionListDataSelectors": self.power_sequence_description_list_data_selectors.get_data()})
        if self.power_sequence_price_list_data_selectors is not None:
            msg_data.append({"powerSequencePriceListDataSelectors": self.power_sequence_price_list_data_selectors.get_data()})
        if self.power_sequence_schedule_constraints_list_data_selectors is not None:
            msg_data.append({"powerSequenceScheduleConstraintsListDataSelectors": self.power_sequence_schedule_constraints_list_data_selectors.get_data()})
        if self.power_sequence_schedule_list_data_selectors is not None:
            msg_data.append({"powerSequenceScheduleListDataSelectors": self.power_sequence_schedule_list_data_selectors.get_data()})
        if self.power_sequence_schedule_preference_list_data_selectors is not None:
            msg_data.append({"powerSequenceSchedulePreferenceListDataSelectors": self.power_sequence_schedule_preference_list_data_selectors.get_data()})
        if self.power_sequence_state_list_data_selectors is not None:
            msg_data.append({"powerSequenceStateListDataSelectors": self.power_sequence_state_list_data_selectors.get_data()})
        if self.power_time_slot_schedule_constraints_list_data_selectors is not None:
            msg_data.append({"powerTimeSlotScheduleConstraintsListDataSelectors": self.power_time_slot_schedule_constraints_list_data_selectors.get_data()})
        if self.power_time_slot_schedule_list_data_selectors is not None:
            msg_data.append({"powerTimeSlotScheduleListDataSelectors": self.power_time_slot_schedule_list_data_selectors.get_data()})
        if self.power_time_slot_value_list_data_selectors is not None:
            msg_data.append({"powerTimeSlotValueListDataSelectors": self.power_time_slot_value_list_data_selectors.get_data()})
        if self.sensing_list_data_selectors is not None:
            msg_data.append({"sensingListDataSelectors": self.sensing_list_data_selectors.get_data()})
        if self.session_identification_list_data_selectors is not None:
            msg_data.append({"sessionIdentificationListDataSelectors": self.session_identification_list_data_selectors.get_data()})
        if self.session_measurement_relation_list_data_selectors is not None:
            msg_data.append({"sessionMeasurementRelationListDataSelectors": self.session_measurement_relation_list_data_selectors.get_data()})
        if self.setpoint_constraints_list_data_selectors is not None:
            msg_data.append({"setpointConstraintsListDataSelectors": self.setpoint_constraints_list_data_selectors.get_data()})
        if self.setpoint_description_list_data_selectors is not None:
            msg_data.append({"setpointDescriptionListDataSelectors": self.setpoint_description_list_data_selectors.get_data()})
        if self.setpoint_list_data_selectors is not None:
            msg_data.append({"setpointListDataSelectors": self.setpoint_list_data_selectors.get_data()})
        if self.smart_energy_management_ps_data_selectors is not None:
            msg_data.append({"smartEnergyManagementPsDataSelectors": self.smart_energy_management_ps_data_selectors.get_data()})
        if self.smart_energy_management_ps_price_data_selectors is not None:
            msg_data.append({"smartEnergyManagementPsPriceDataSelectors": self.smart_energy_management_ps_price_data_selectors.get_data()})
        if self.specification_version_list_data_selectors is not None:
            msg_data.append({"specificationVersionListDataSelectors": self.specification_version_list_data_selectors.get_data()})
        if self.state_information_list_data_selectors is not None:
            msg_data.append({"stateInformationListDataSelectors": self.state_information_list_data_selectors.get_data()})
        if self.subscription_management_entry_list_data_selectors is not None:
            msg_data.append({"subscriptionManagementEntryListDataSelectors": self.subscription_management_entry_list_data_selectors.get_data()})
        if self.supply_condition_description_list_data_selectors is not None:
            msg_data.append({"supplyConditionDescriptionListDataSelectors": self.supply_condition_description_list_data_selectors.get_data()})
        if self.supply_condition_list_data_selectors is not None:
            msg_data.append({"supplyConditionListDataSelectors": self.supply_condition_list_data_selectors.get_data()})
        if self.supply_condition_threshold_relation_list_data_selectors is not None:
            msg_data.append({"supplyConditionThresholdRelationListDataSelectors": self.supply_condition_threshold_relation_list_data_selectors.get_data()})
        if self.tariff_boundary_relation_list_data_selectors is not None:
            msg_data.append({"tariffBoundaryRelationListDataSelectors": self.tariff_boundary_relation_list_data_selectors.get_data()})
        if self.tariff_description_list_data_selectors is not None:
            msg_data.append({"tariffDescriptionListDataSelectors": self.tariff_description_list_data_selectors.get_data()})
        if self.tariff_list_data_selectors is not None:
            msg_data.append({"tariffListDataSelectors": self.tariff_list_data_selectors.get_data()})
        if self.tariff_tier_relation_list_data_selectors is not None:
            msg_data.append({"tariffTierRelationListDataSelectors": self.tariff_tier_relation_list_data_selectors.get_data()})
        if self.task_management_job_description_list_data_selectors is not None:
            msg_data.append({"taskManagementJobDescriptionListDataSelectors": self.task_management_job_description_list_data_selectors.get_data()})
        if self.task_management_job_list_data_selectors is not None:
            msg_data.append({"taskManagementJobListDataSelectors": self.task_management_job_list_data_selectors.get_data()})
        if self.task_management_job_relation_list_data_selectors is not None:
            msg_data.append({"taskManagementJobRelationListDataSelectors": self.task_management_job_relation_list_data_selectors.get_data()})
        if self.threshold_constraints_list_data_selectors is not None:
            msg_data.append({"thresholdConstraintsListDataSelectors": self.threshold_constraints_list_data_selectors.get_data()})
        if self.threshold_description_list_data_selectors is not None:
            msg_data.append({"thresholdDescriptionListDataSelectors": self.threshold_description_list_data_selectors.get_data()})
        if self.threshold_list_data_selectors is not None:
            msg_data.append({"thresholdListDataSelectors": self.threshold_list_data_selectors.get_data()})
        if self.tier_boundary_description_list_data_selectors is not None:
            msg_data.append({"tierBoundaryDescriptionListDataSelectors": self.tier_boundary_description_list_data_selectors.get_data()})
        if self.tier_boundary_list_data_selectors is not None:
            msg_data.append({"tierBoundaryListDataSelectors": self.tier_boundary_list_data_selectors.get_data()})
        if self.tier_description_list_data_selectors is not None:
            msg_data.append({"tierDescriptionListDataSelectors": self.tier_description_list_data_selectors.get_data()})
        if self.tier_incentive_relation_list_data_selectors is not None:
            msg_data.append({"tierIncentiveRelationListDataSelectors": self.tier_incentive_relation_list_data_selectors.get_data()})
        if self.tier_list_data_selectors is not None:
            msg_data.append({"tierListDataSelectors": self.tier_list_data_selectors.get_data()})
        if self.time_series_constraints_list_data_selectors is not None:
            msg_data.append({"timeSeriesConstraintsListDataSelectors": self.time_series_constraints_list_data_selectors.get_data()})
        if self.time_series_description_list_data_selectors is not None:
            msg_data.append({"timeSeriesDescriptionListDataSelectors": self.time_series_description_list_data_selectors.get_data()})
        if self.time_series_list_data_selectors is not None:
            msg_data.append({"timeSeriesListDataSelectors": self.time_series_list_data_selectors.get_data()})
        if self.time_table_constraints_list_data_selectors is not None:
            msg_data.append({"timeTableConstraintsListDataSelectors": self.time_table_constraints_list_data_selectors.get_data()})
        if self.time_table_description_list_data_selectors is not None:
            msg_data.append({"timeTableDescriptionListDataSelectors": self.time_table_description_list_data_selectors.get_data()})
        if self.time_table_list_data_selectors is not None:
            msg_data.append({"timeTableListDataSelectors": self.time_table_list_data_selectors.get_data()})
        if self.use_case_information_list_data_selectors is not None:
            msg_data.append({"useCaseInformationListDataSelectors": self.use_case_information_list_data_selectors.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.alarm_list_data_selectors is not None:
            result_str += f"{sep}alarmListDataSelectors: {self.alarm_list_data_selectors}"
            sep = ", "
        if self.bill_constraints_list_data_selectors is not None:
            result_str += f"{sep}billConstraintsListDataSelectors: {self.bill_constraints_list_data_selectors}"
            sep = ", "
        if self.bill_description_list_data_selectors is not None:
            result_str += f"{sep}billDescriptionListDataSelectors: {self.bill_description_list_data_selectors}"
            sep = ", "
        if self.bill_list_data_selectors is not None:
            result_str += f"{sep}billListDataSelectors: {self.bill_list_data_selectors}"
            sep = ", "
        if self.binding_management_entry_list_data_selectors is not None:
            result_str += f"{sep}bindingManagementEntryListDataSelectors: {self.binding_management_entry_list_data_selectors}"
            sep = ", "
        if self.commodity_list_data_selectors is not None:
            result_str += f"{sep}commodityListDataSelectors: {self.commodity_list_data_selectors}"
            sep = ", "
        if self.device_configuration_key_value_constraints_list_data_selectors is not None:
            result_str += f"{sep}deviceConfigurationKeyValueConstraintsListDataSelectors: {self.device_configuration_key_value_constraints_list_data_selectors}"
            sep = ", "
        if self.device_configuration_key_value_description_list_data_selectors is not None:
            result_str += f"{sep}deviceConfigurationKeyValueDescriptionListDataSelectors: {self.device_configuration_key_value_description_list_data_selectors}"
            sep = ", "
        if self.device_configuration_key_value_list_data_selectors is not None:
            result_str += f"{sep}deviceConfigurationKeyValueListDataSelectors: {self.device_configuration_key_value_list_data_selectors}"
            sep = ", "
        if self.direct_control_activity_list_data_selectors is not None:
            result_str += f"{sep}directControlActivityListDataSelectors: {self.direct_control_activity_list_data_selectors}"
            sep = ", "
        if self.electrical_connection_characteristic_list_data_selectors is not None:
            result_str += f"{sep}electricalConnectionCharacteristicListDataSelectors: {self.electrical_connection_characteristic_list_data_selectors}"
            sep = ", "
        if self.electrical_connection_description_list_data_selectors is not None:
            result_str += f"{sep}electricalConnectionDescriptionListDataSelectors: {self.electrical_connection_description_list_data_selectors}"
            sep = ", "
        if self.electrical_connection_parameter_description_list_data_selectors is not None:
            result_str += f"{sep}electricalConnectionParameterDescriptionListDataSelectors: {self.electrical_connection_parameter_description_list_data_selectors}"
            sep = ", "
        if self.electrical_connection_permitted_value_set_list_data_selectors is not None:
            result_str += f"{sep}electricalConnectionPermittedValueSetListDataSelectors: {self.electrical_connection_permitted_value_set_list_data_selectors}"
            sep = ", "
        if self.electrical_connection_state_list_data_selectors is not None:
            result_str += f"{sep}electricalConnectionStateListDataSelectors: {self.electrical_connection_state_list_data_selectors}"
            sep = ", "
        if self.hvac_operation_mode_description_list_data_selectors is not None:
            result_str += f"{sep}hvacOperationModeDescriptionListDataSelectors: {self.hvac_operation_mode_description_list_data_selectors}"
            sep = ", "
        if self.hvac_overrun_description_list_data_selectors is not None:
            result_str += f"{sep}hvacOverrunDescriptionListDataSelectors: {self.hvac_overrun_description_list_data_selectors}"
            sep = ", "
        if self.hvac_overrun_list_data_selectors is not None:
            result_str += f"{sep}hvacOverrunListDataSelectors: {self.hvac_overrun_list_data_selectors}"
            sep = ", "
        if self.hvac_system_function_description_list_data_selectors is not None:
            result_str += f"{sep}hvacSystemFunctionDescriptionListDataSelectors: {self.hvac_system_function_description_list_data_selectors}"
            sep = ", "
        if self.hvac_system_function_list_data_selectors is not None:
            result_str += f"{sep}hvacSystemFunctionListDataSelectors: {self.hvac_system_function_list_data_selectors}"
            sep = ", "
        if self.hvac_system_function_operation_mode_relation_list_data_selectors is not None:
            result_str += f"{sep}hvacSystemFunctionOperationModeRelationListDataSelectors: {self.hvac_system_function_operation_mode_relation_list_data_selectors}"
            sep = ", "
        if self.hvac_system_function_power_sequence_relation_list_data_selectors is not None:
            result_str += f"{sep}hvacSystemFunctionPowerSequenceRelationListDataSelectors: {self.hvac_system_function_power_sequence_relation_list_data_selectors}"
            sep = ", "
        if self.hvac_system_function_setpoint_relation_list_data_selectors is not None:
            result_str += f"{sep}hvacSystemFunctionSetpointRelationListDataSelectors: {self.hvac_system_function_setpoint_relation_list_data_selectors}"
            sep = ", "
        if self.identification_list_data_selectors is not None:
            result_str += f"{sep}identificationListDataSelectors: {self.identification_list_data_selectors}"
            sep = ", "
        if self.incentive_description_list_data_selectors is not None:
            result_str += f"{sep}incentiveDescriptionListDataSelectors: {self.incentive_description_list_data_selectors}"
            sep = ", "
        if self.incentive_list_data_selectors is not None:
            result_str += f"{sep}incentiveListDataSelectors: {self.incentive_list_data_selectors}"
            sep = ", "
        if self.incentive_table_constraints_data_selectors is not None:
            result_str += f"{sep}incentiveTableConstraintsDataSelectors: {self.incentive_table_constraints_data_selectors}"
            sep = ", "
        if self.incentive_table_data_selectors is not None:
            result_str += f"{sep}incentiveTableDataSelectors: {self.incentive_table_data_selectors}"
            sep = ", "
        if self.incentive_table_description_data_selectors is not None:
            result_str += f"{sep}incentiveTableDescriptionDataSelectors: {self.incentive_table_description_data_selectors}"
            sep = ", "
        if self.load_control_event_list_data_selectors is not None:
            result_str += f"{sep}loadControlEventListDataSelectors: {self.load_control_event_list_data_selectors}"
            sep = ", "
        if self.load_control_limit_constraints_list_data_selectors is not None:
            result_str += f"{sep}loadControlLimitConstraintsListDataSelectors: {self.load_control_limit_constraints_list_data_selectors}"
            sep = ", "
        if self.load_control_limit_description_list_data_selectors is not None:
            result_str += f"{sep}loadControlLimitDescriptionListDataSelectors: {self.load_control_limit_description_list_data_selectors}"
            sep = ", "
        if self.load_control_limit_list_data_selectors is not None:
            result_str += f"{sep}loadControlLimitListDataSelectors: {self.load_control_limit_list_data_selectors}"
            sep = ", "
        if self.load_control_state_list_data_selectors is not None:
            result_str += f"{sep}loadControlStateListDataSelectors: {self.load_control_state_list_data_selectors}"
            sep = ", "
        if self.measurement_constraints_list_data_selectors is not None:
            result_str += f"{sep}measurementConstraintsListDataSelectors: {self.measurement_constraints_list_data_selectors}"
            sep = ", "
        if self.measurement_description_list_data_selectors is not None:
            result_str += f"{sep}measurementDescriptionListDataSelectors: {self.measurement_description_list_data_selectors}"
            sep = ", "
        if self.measurement_list_data_selectors is not None:
            result_str += f"{sep}measurementListDataSelectors: {self.measurement_list_data_selectors}"
            sep = ", "
        if self.measurement_series_list_data_selectors is not None:
            result_str += f"{sep}measurementSeriesListDataSelectors: {self.measurement_series_list_data_selectors}"
            sep = ", "
        if self.measurement_threshold_relation_list_data_selectors is not None:
            result_str += f"{sep}measurementThresholdRelationListDataSelectors: {self.measurement_threshold_relation_list_data_selectors}"
            sep = ", "
        if self.messaging_list_data_selectors is not None:
            result_str += f"{sep}messagingListDataSelectors: {self.messaging_list_data_selectors}"
            sep = ", "
        if self.network_management_device_description_list_data_selectors is not None:
            result_str += f"{sep}networkManagementDeviceDescriptionListDataSelectors: {self.network_management_device_description_list_data_selectors}"
            sep = ", "
        if self.network_management_entity_description_list_data_selectors is not None:
            result_str += f"{sep}networkManagementEntityDescriptionListDataSelectors: {self.network_management_entity_description_list_data_selectors}"
            sep = ", "
        if self.network_management_feature_description_list_data_selectors is not None:
            result_str += f"{sep}networkManagementFeatureDescriptionListDataSelectors: {self.network_management_feature_description_list_data_selectors}"
            sep = ", "
        if self.node_management_binding_data_selectors is not None:
            result_str += f"{sep}nodeManagementBindingDataSelectors: {self.node_management_binding_data_selectors}"
            sep = ", "
        if self.node_management_destination_list_data_selectors is not None:
            result_str += f"{sep}nodeManagementDestinationListDataSelectors: {self.node_management_destination_list_data_selectors}"
            sep = ", "
        if self.node_management_detailed_discovery_data_selectors is not None:
            result_str += f"{sep}nodeManagementDetailedDiscoveryDataSelectors: {self.node_management_detailed_discovery_data_selectors}"
            sep = ", "
        if self.node_management_subscription_data_selectors is not None:
            result_str += f"{sep}nodeManagementSubscriptionDataSelectors: {self.node_management_subscription_data_selectors}"
            sep = ", "
        if self.node_management_use_case_data_selectors is not None:
            result_str += f"{sep}nodeManagementUseCaseDataSelectors: {self.node_management_use_case_data_selectors}"
            sep = ", "
        if self.operating_constraints_duration_list_data_selectors is not None:
            result_str += f"{sep}operatingConstraintsDurationListDataSelectors: {self.operating_constraints_duration_list_data_selectors}"
            sep = ", "
        if self.operating_constraints_interrupt_list_data_selectors is not None:
            result_str += f"{sep}operatingConstraintsInterruptListDataSelectors: {self.operating_constraints_interrupt_list_data_selectors}"
            sep = ", "
        if self.operating_constraints_power_description_list_data_selectors is not None:
            result_str += f"{sep}operatingConstraintsPowerDescriptionListDataSelectors: {self.operating_constraints_power_description_list_data_selectors}"
            sep = ", "
        if self.operating_constraints_power_level_list_data_selectors is not None:
            result_str += f"{sep}operatingConstraintsPowerLevelListDataSelectors: {self.operating_constraints_power_level_list_data_selectors}"
            sep = ", "
        if self.operating_constraints_power_range_list_data_selectors is not None:
            result_str += f"{sep}operatingConstraintsPowerRangeListDataSelectors: {self.operating_constraints_power_range_list_data_selectors}"
            sep = ", "
        if self.operating_constraints_resume_implication_list_data_selectors is not None:
            result_str += f"{sep}operatingConstraintsResumeImplicationListDataSelectors: {self.operating_constraints_resume_implication_list_data_selectors}"
            sep = ", "
        if self.power_sequence_alternatives_relation_list_data_selectors is not None:
            result_str += f"{sep}powerSequenceAlternativesRelationListDataSelectors: {self.power_sequence_alternatives_relation_list_data_selectors}"
            sep = ", "
        if self.power_sequence_description_list_data_selectors is not None:
            result_str += f"{sep}powerSequenceDescriptionListDataSelectors: {self.power_sequence_description_list_data_selectors}"
            sep = ", "
        if self.power_sequence_price_list_data_selectors is not None:
            result_str += f"{sep}powerSequencePriceListDataSelectors: {self.power_sequence_price_list_data_selectors}"
            sep = ", "
        if self.power_sequence_schedule_constraints_list_data_selectors is not None:
            result_str += f"{sep}powerSequenceScheduleConstraintsListDataSelectors: {self.power_sequence_schedule_constraints_list_data_selectors}"
            sep = ", "
        if self.power_sequence_schedule_list_data_selectors is not None:
            result_str += f"{sep}powerSequenceScheduleListDataSelectors: {self.power_sequence_schedule_list_data_selectors}"
            sep = ", "
        if self.power_sequence_schedule_preference_list_data_selectors is not None:
            result_str += f"{sep}powerSequenceSchedulePreferenceListDataSelectors: {self.power_sequence_schedule_preference_list_data_selectors}"
            sep = ", "
        if self.power_sequence_state_list_data_selectors is not None:
            result_str += f"{sep}powerSequenceStateListDataSelectors: {self.power_sequence_state_list_data_selectors}"
            sep = ", "
        if self.power_time_slot_schedule_constraints_list_data_selectors is not None:
            result_str += f"{sep}powerTimeSlotScheduleConstraintsListDataSelectors: {self.power_time_slot_schedule_constraints_list_data_selectors}"
            sep = ", "
        if self.power_time_slot_schedule_list_data_selectors is not None:
            result_str += f"{sep}powerTimeSlotScheduleListDataSelectors: {self.power_time_slot_schedule_list_data_selectors}"
            sep = ", "
        if self.power_time_slot_value_list_data_selectors is not None:
            result_str += f"{sep}powerTimeSlotValueListDataSelectors: {self.power_time_slot_value_list_data_selectors}"
            sep = ", "
        if self.sensing_list_data_selectors is not None:
            result_str += f"{sep}sensingListDataSelectors: {self.sensing_list_data_selectors}"
            sep = ", "
        if self.session_identification_list_data_selectors is not None:
            result_str += f"{sep}sessionIdentificationListDataSelectors: {self.session_identification_list_data_selectors}"
            sep = ", "
        if self.session_measurement_relation_list_data_selectors is not None:
            result_str += f"{sep}sessionMeasurementRelationListDataSelectors: {self.session_measurement_relation_list_data_selectors}"
            sep = ", "
        if self.setpoint_constraints_list_data_selectors is not None:
            result_str += f"{sep}setpointConstraintsListDataSelectors: {self.setpoint_constraints_list_data_selectors}"
            sep = ", "
        if self.setpoint_description_list_data_selectors is not None:
            result_str += f"{sep}setpointDescriptionListDataSelectors: {self.setpoint_description_list_data_selectors}"
            sep = ", "
        if self.setpoint_list_data_selectors is not None:
            result_str += f"{sep}setpointListDataSelectors: {self.setpoint_list_data_selectors}"
            sep = ", "
        if self.smart_energy_management_ps_data_selectors is not None:
            result_str += f"{sep}smartEnergyManagementPsDataSelectors: {self.smart_energy_management_ps_data_selectors}"
            sep = ", "
        if self.smart_energy_management_ps_price_data_selectors is not None:
            result_str += f"{sep}smartEnergyManagementPsPriceDataSelectors: {self.smart_energy_management_ps_price_data_selectors}"
            sep = ", "
        if self.specification_version_list_data_selectors is not None:
            result_str += f"{sep}specificationVersionListDataSelectors: {self.specification_version_list_data_selectors}"
            sep = ", "
        if self.state_information_list_data_selectors is not None:
            result_str += f"{sep}stateInformationListDataSelectors: {self.state_information_list_data_selectors}"
            sep = ", "
        if self.subscription_management_entry_list_data_selectors is not None:
            result_str += f"{sep}subscriptionManagementEntryListDataSelectors: {self.subscription_management_entry_list_data_selectors}"
            sep = ", "
        if self.supply_condition_description_list_data_selectors is not None:
            result_str += f"{sep}supplyConditionDescriptionListDataSelectors: {self.supply_condition_description_list_data_selectors}"
            sep = ", "
        if self.supply_condition_list_data_selectors is not None:
            result_str += f"{sep}supplyConditionListDataSelectors: {self.supply_condition_list_data_selectors}"
            sep = ", "
        if self.supply_condition_threshold_relation_list_data_selectors is not None:
            result_str += f"{sep}supplyConditionThresholdRelationListDataSelectors: {self.supply_condition_threshold_relation_list_data_selectors}"
            sep = ", "
        if self.tariff_boundary_relation_list_data_selectors is not None:
            result_str += f"{sep}tariffBoundaryRelationListDataSelectors: {self.tariff_boundary_relation_list_data_selectors}"
            sep = ", "
        if self.tariff_description_list_data_selectors is not None:
            result_str += f"{sep}tariffDescriptionListDataSelectors: {self.tariff_description_list_data_selectors}"
            sep = ", "
        if self.tariff_list_data_selectors is not None:
            result_str += f"{sep}tariffListDataSelectors: {self.tariff_list_data_selectors}"
            sep = ", "
        if self.tariff_tier_relation_list_data_selectors is not None:
            result_str += f"{sep}tariffTierRelationListDataSelectors: {self.tariff_tier_relation_list_data_selectors}"
            sep = ", "
        if self.task_management_job_description_list_data_selectors is not None:
            result_str += f"{sep}taskManagementJobDescriptionListDataSelectors: {self.task_management_job_description_list_data_selectors}"
            sep = ", "
        if self.task_management_job_list_data_selectors is not None:
            result_str += f"{sep}taskManagementJobListDataSelectors: {self.task_management_job_list_data_selectors}"
            sep = ", "
        if self.task_management_job_relation_list_data_selectors is not None:
            result_str += f"{sep}taskManagementJobRelationListDataSelectors: {self.task_management_job_relation_list_data_selectors}"
            sep = ", "
        if self.threshold_constraints_list_data_selectors is not None:
            result_str += f"{sep}thresholdConstraintsListDataSelectors: {self.threshold_constraints_list_data_selectors}"
            sep = ", "
        if self.threshold_description_list_data_selectors is not None:
            result_str += f"{sep}thresholdDescriptionListDataSelectors: {self.threshold_description_list_data_selectors}"
            sep = ", "
        if self.threshold_list_data_selectors is not None:
            result_str += f"{sep}thresholdListDataSelectors: {self.threshold_list_data_selectors}"
            sep = ", "
        if self.tier_boundary_description_list_data_selectors is not None:
            result_str += f"{sep}tierBoundaryDescriptionListDataSelectors: {self.tier_boundary_description_list_data_selectors}"
            sep = ", "
        if self.tier_boundary_list_data_selectors is not None:
            result_str += f"{sep}tierBoundaryListDataSelectors: {self.tier_boundary_list_data_selectors}"
            sep = ", "
        if self.tier_description_list_data_selectors is not None:
            result_str += f"{sep}tierDescriptionListDataSelectors: {self.tier_description_list_data_selectors}"
            sep = ", "
        if self.tier_incentive_relation_list_data_selectors is not None:
            result_str += f"{sep}tierIncentiveRelationListDataSelectors: {self.tier_incentive_relation_list_data_selectors}"
            sep = ", "
        if self.tier_list_data_selectors is not None:
            result_str += f"{sep}tierListDataSelectors: {self.tier_list_data_selectors}"
            sep = ", "
        if self.time_series_constraints_list_data_selectors is not None:
            result_str += f"{sep}timeSeriesConstraintsListDataSelectors: {self.time_series_constraints_list_data_selectors}"
            sep = ", "
        if self.time_series_description_list_data_selectors is not None:
            result_str += f"{sep}timeSeriesDescriptionListDataSelectors: {self.time_series_description_list_data_selectors}"
            sep = ", "
        if self.time_series_list_data_selectors is not None:
            result_str += f"{sep}timeSeriesListDataSelectors: {self.time_series_list_data_selectors}"
            sep = ", "
        if self.time_table_constraints_list_data_selectors is not None:
            result_str += f"{sep}timeTableConstraintsListDataSelectors: {self.time_table_constraints_list_data_selectors}"
            sep = ", "
        if self.time_table_description_list_data_selectors is not None:
            result_str += f"{sep}timeTableDescriptionListDataSelectors: {self.time_table_description_list_data_selectors}"
            sep = ", "
        if self.time_table_list_data_selectors is not None:
            result_str += f"{sep}timeTableListDataSelectors: {self.time_table_list_data_selectors}"
            sep = ", "
        if self.use_case_information_list_data_selectors is not None:
            result_str += f"{sep}useCaseInformationListDataSelectors: {self.use_case_information_list_data_selectors}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                alarm_list_data_selectors=data_dict.get('alarmListDataSelectors'),
                bill_constraints_list_data_selectors=data_dict.get('billConstraintsListDataSelectors'),
                bill_description_list_data_selectors=data_dict.get('billDescriptionListDataSelectors'),
                bill_list_data_selectors=data_dict.get('billListDataSelectors'),
                binding_management_entry_list_data_selectors=data_dict.get('bindingManagementEntryListDataSelectors'),
                commodity_list_data_selectors=data_dict.get('commodityListDataSelectors'),
                device_configuration_key_value_constraints_list_data_selectors=data_dict.get('deviceConfigurationKeyValueConstraintsListDataSelectors'),
                device_configuration_key_value_description_list_data_selectors=data_dict.get('deviceConfigurationKeyValueDescriptionListDataSelectors'),
                device_configuration_key_value_list_data_selectors=data_dict.get('deviceConfigurationKeyValueListDataSelectors'),
                direct_control_activity_list_data_selectors=data_dict.get('directControlActivityListDataSelectors'),
                electrical_connection_characteristic_list_data_selectors=data_dict.get('electricalConnectionCharacteristicListDataSelectors'),
                electrical_connection_description_list_data_selectors=data_dict.get('electricalConnectionDescriptionListDataSelectors'),
                electrical_connection_parameter_description_list_data_selectors=data_dict.get('electricalConnectionParameterDescriptionListDataSelectors'),
                electrical_connection_permitted_value_set_list_data_selectors=data_dict.get('electricalConnectionPermittedValueSetListDataSelectors'),
                electrical_connection_state_list_data_selectors=data_dict.get('electricalConnectionStateListDataSelectors'),
                hvac_operation_mode_description_list_data_selectors=data_dict.get('hvacOperationModeDescriptionListDataSelectors'),
                hvac_overrun_description_list_data_selectors=data_dict.get('hvacOverrunDescriptionListDataSelectors'),
                hvac_overrun_list_data_selectors=data_dict.get('hvacOverrunListDataSelectors'),
                hvac_system_function_description_list_data_selectors=data_dict.get('hvacSystemFunctionDescriptionListDataSelectors'),
                hvac_system_function_list_data_selectors=data_dict.get('hvacSystemFunctionListDataSelectors'),
                hvac_system_function_operation_mode_relation_list_data_selectors=data_dict.get('hvacSystemFunctionOperationModeRelationListDataSelectors'),
                hvac_system_function_power_sequence_relation_list_data_selectors=data_dict.get('hvacSystemFunctionPowerSequenceRelationListDataSelectors'),
                hvac_system_function_setpoint_relation_list_data_selectors=data_dict.get('hvacSystemFunctionSetpointRelationListDataSelectors'),
                identification_list_data_selectors=data_dict.get('identificationListDataSelectors'),
                incentive_description_list_data_selectors=data_dict.get('incentiveDescriptionListDataSelectors'),
                incentive_list_data_selectors=data_dict.get('incentiveListDataSelectors'),
                incentive_table_constraints_data_selectors=data_dict.get('incentiveTableConstraintsDataSelectors'),
                incentive_table_data_selectors=data_dict.get('incentiveTableDataSelectors'),
                incentive_table_description_data_selectors=data_dict.get('incentiveTableDescriptionDataSelectors'),
                load_control_event_list_data_selectors=data_dict.get('loadControlEventListDataSelectors'),
                load_control_limit_constraints_list_data_selectors=data_dict.get('loadControlLimitConstraintsListDataSelectors'),
                load_control_limit_description_list_data_selectors=data_dict.get('loadControlLimitDescriptionListDataSelectors'),
                load_control_limit_list_data_selectors=data_dict.get('loadControlLimitListDataSelectors'),
                load_control_state_list_data_selectors=data_dict.get('loadControlStateListDataSelectors'),
                measurement_constraints_list_data_selectors=data_dict.get('measurementConstraintsListDataSelectors'),
                measurement_description_list_data_selectors=data_dict.get('measurementDescriptionListDataSelectors'),
                measurement_list_data_selectors=data_dict.get('measurementListDataSelectors'),
                measurement_series_list_data_selectors=data_dict.get('measurementSeriesListDataSelectors'),
                measurement_threshold_relation_list_data_selectors=data_dict.get('measurementThresholdRelationListDataSelectors'),
                messaging_list_data_selectors=data_dict.get('messagingListDataSelectors'),
                network_management_device_description_list_data_selectors=data_dict.get('networkManagementDeviceDescriptionListDataSelectors'),
                network_management_entity_description_list_data_selectors=data_dict.get('networkManagementEntityDescriptionListDataSelectors'),
                network_management_feature_description_list_data_selectors=data_dict.get('networkManagementFeatureDescriptionListDataSelectors'),
                node_management_binding_data_selectors=data_dict.get('nodeManagementBindingDataSelectors'),
                node_management_destination_list_data_selectors=data_dict.get('nodeManagementDestinationListDataSelectors'),
                node_management_detailed_discovery_data_selectors=data_dict.get('nodeManagementDetailedDiscoveryDataSelectors'),
                node_management_subscription_data_selectors=data_dict.get('nodeManagementSubscriptionDataSelectors'),
                node_management_use_case_data_selectors=data_dict.get('nodeManagementUseCaseDataSelectors'),
                operating_constraints_duration_list_data_selectors=data_dict.get('operatingConstraintsDurationListDataSelectors'),
                operating_constraints_interrupt_list_data_selectors=data_dict.get('operatingConstraintsInterruptListDataSelectors'),
                operating_constraints_power_description_list_data_selectors=data_dict.get('operatingConstraintsPowerDescriptionListDataSelectors'),
                operating_constraints_power_level_list_data_selectors=data_dict.get('operatingConstraintsPowerLevelListDataSelectors'),
                operating_constraints_power_range_list_data_selectors=data_dict.get('operatingConstraintsPowerRangeListDataSelectors'),
                operating_constraints_resume_implication_list_data_selectors=data_dict.get('operatingConstraintsResumeImplicationListDataSelectors'),
                power_sequence_alternatives_relation_list_data_selectors=data_dict.get('powerSequenceAlternativesRelationListDataSelectors'),
                power_sequence_description_list_data_selectors=data_dict.get('powerSequenceDescriptionListDataSelectors'),
                power_sequence_price_list_data_selectors=data_dict.get('powerSequencePriceListDataSelectors'),
                power_sequence_schedule_constraints_list_data_selectors=data_dict.get('powerSequenceScheduleConstraintsListDataSelectors'),
                power_sequence_schedule_list_data_selectors=data_dict.get('powerSequenceScheduleListDataSelectors'),
                power_sequence_schedule_preference_list_data_selectors=data_dict.get('powerSequenceSchedulePreferenceListDataSelectors'),
                power_sequence_state_list_data_selectors=data_dict.get('powerSequenceStateListDataSelectors'),
                power_time_slot_schedule_constraints_list_data_selectors=data_dict.get('powerTimeSlotScheduleConstraintsListDataSelectors'),
                power_time_slot_schedule_list_data_selectors=data_dict.get('powerTimeSlotScheduleListDataSelectors'),
                power_time_slot_value_list_data_selectors=data_dict.get('powerTimeSlotValueListDataSelectors'),
                sensing_list_data_selectors=data_dict.get('sensingListDataSelectors'),
                session_identification_list_data_selectors=data_dict.get('sessionIdentificationListDataSelectors'),
                session_measurement_relation_list_data_selectors=data_dict.get('sessionMeasurementRelationListDataSelectors'),
                setpoint_constraints_list_data_selectors=data_dict.get('setpointConstraintsListDataSelectors'),
                setpoint_description_list_data_selectors=data_dict.get('setpointDescriptionListDataSelectors'),
                setpoint_list_data_selectors=data_dict.get('setpointListDataSelectors'),
                smart_energy_management_ps_data_selectors=data_dict.get('smartEnergyManagementPsDataSelectors'),
                smart_energy_management_ps_price_data_selectors=data_dict.get('smartEnergyManagementPsPriceDataSelectors'),
                specification_version_list_data_selectors=data_dict.get('specificationVersionListDataSelectors'),
                state_information_list_data_selectors=data_dict.get('stateInformationListDataSelectors'),
                subscription_management_entry_list_data_selectors=data_dict.get('subscriptionManagementEntryListDataSelectors'),
                supply_condition_description_list_data_selectors=data_dict.get('supplyConditionDescriptionListDataSelectors'),
                supply_condition_list_data_selectors=data_dict.get('supplyConditionListDataSelectors'),
                supply_condition_threshold_relation_list_data_selectors=data_dict.get('supplyConditionThresholdRelationListDataSelectors'),
                tariff_boundary_relation_list_data_selectors=data_dict.get('tariffBoundaryRelationListDataSelectors'),
                tariff_description_list_data_selectors=data_dict.get('tariffDescriptionListDataSelectors'),
                tariff_list_data_selectors=data_dict.get('tariffListDataSelectors'),
                tariff_tier_relation_list_data_selectors=data_dict.get('tariffTierRelationListDataSelectors'),
                task_management_job_description_list_data_selectors=data_dict.get('taskManagementJobDescriptionListDataSelectors'),
                task_management_job_list_data_selectors=data_dict.get('taskManagementJobListDataSelectors'),
                task_management_job_relation_list_data_selectors=data_dict.get('taskManagementJobRelationListDataSelectors'),
                threshold_constraints_list_data_selectors=data_dict.get('thresholdConstraintsListDataSelectors'),
                threshold_description_list_data_selectors=data_dict.get('thresholdDescriptionListDataSelectors'),
                threshold_list_data_selectors=data_dict.get('thresholdListDataSelectors'),
                tier_boundary_description_list_data_selectors=data_dict.get('tierBoundaryDescriptionListDataSelectors'),
                tier_boundary_list_data_selectors=data_dict.get('tierBoundaryListDataSelectors'),
                tier_description_list_data_selectors=data_dict.get('tierDescriptionListDataSelectors'),
                tier_incentive_relation_list_data_selectors=data_dict.get('tierIncentiveRelationListDataSelectors'),
                tier_list_data_selectors=data_dict.get('tierListDataSelectors'),
                time_series_constraints_list_data_selectors=data_dict.get('timeSeriesConstraintsListDataSelectors'),
                time_series_description_list_data_selectors=data_dict.get('timeSeriesDescriptionListDataSelectors'),
                time_series_list_data_selectors=data_dict.get('timeSeriesListDataSelectors'),
                time_table_constraints_list_data_selectors=data_dict.get('timeTableConstraintsListDataSelectors'),
                time_table_description_list_data_selectors=data_dict.get('timeTableDescriptionListDataSelectors'),
                time_table_list_data_selectors=data_dict.get('timeTableListDataSelectors'),
                use_case_information_list_data_selectors=data_dict.get('useCaseInformationListDataSelectors'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class DataExtendGroup:
    def __init__(
            self,
    ):
        super().__init__()
        

    def get_data(self): # ChoiceType

        msg_data = []
        
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
            )
        elif data:
            return cls(data)
        else:
            return cls()


class DataElementsChoiceGroup:
    def __init__(
            self,
            actuator_level_data_elements: ActuatorLevelDataElementsType,
            actuator_level_description_data_elements: ActuatorLevelDescriptionDataElementsType,
            actuator_switch_data_elements: ActuatorSwitchDataElementsType,
            actuator_switch_description_data_elements: ActuatorSwitchDescriptionDataElementsType,
            alarm_data_elements: AlarmDataElementsType,
            bill_constraints_data_elements: BillConstraintsDataElementsType,
            bill_data_elements: BillDataElementsType,
            bill_description_data_elements: BillDescriptionDataElementsType,
            binding_management_delete_call_elements: BindingManagementDeleteCallElementsType,
            binding_management_entry_data_elements: BindingManagementEntryDataElementsType,
            binding_management_request_call_elements: BindingManagementRequestCallElementsType,
            commodity_data_elements: CommodityDataElementsType,
            data_tunneling_call_elements: DataTunnelingCallElementsType,
            device_classification_manufacturer_data_elements: DeviceClassificationManufacturerDataElementsType,
            device_classification_user_data_elements: DeviceClassificationUserDataElementsType,
            device_configuration_key_value_constraints_data_elements: DeviceConfigurationKeyValueConstraintsDataElementsType,
            device_configuration_key_value_data_elements: DeviceConfigurationKeyValueDataElementsType,
            device_configuration_key_value_description_data_elements: DeviceConfigurationKeyValueDescriptionDataElementsType,
            device_diagnosis_heartbeat_data_elements: DeviceDiagnosisHeartbeatDataElementsType,
            device_diagnosis_service_data_elements: DeviceDiagnosisServiceDataElementsType,
            device_diagnosis_state_data_elements: DeviceDiagnosisStateDataElementsType,
            direct_control_activity_data_elements: DirectControlActivityDataElementsType,
            direct_control_description_data_elements: DirectControlDescriptionDataElementsType,
            electrical_connection_characteristic_data_elements: ElectricalConnectionCharacteristicDataElementsType,
            electrical_connection_description_data_elements: ElectricalConnectionDescriptionDataElementsType,
            electrical_connection_parameter_description_data_elements: ElectricalConnectionParameterDescriptionDataElementsType,
            electrical_connection_permitted_value_set_data_elements: ElectricalConnectionPermittedValueSetDataElementsType,
            electrical_connection_state_data_elements: ElectricalConnectionStateDataElementsType,
            hvac_operation_mode_description_data_elements: HvacOperationModeDescriptionDataElementsType,
            hvac_overrun_data_elements: HvacOverrunDataElementsType,
            hvac_overrun_description_data_elements: HvacOverrunDescriptionDataElementsType,
            hvac_system_function_data_elements: HvacSystemFunctionDataElementsType,
            hvac_system_function_description_data_elements: HvacSystemFunctionDescriptionDataElementsType,
            hvac_system_function_operation_mode_relation_data_elements: HvacSystemFunctionOperationModeRelationDataElementsType,
            hvac_system_function_power_sequence_relation_data_elements: HvacSystemFunctionPowerSequenceRelationDataElementsType,
            hvac_system_function_setpoint_relation_data_elements: HvacSystemFunctionSetpointRelationDataElementsType,
            identification_data_elements: IdentificationDataElementsType,
            incentive_data_elements: IncentiveDataElementsType,
            incentive_description_data_elements: IncentiveDescriptionDataElementsType,
            incentive_table_constraints_data_elements: IncentiveTableConstraintsDataElementsType,
            incentive_table_data_elements: IncentiveTableDataElementsType,
            incentive_table_description_data_elements: IncentiveTableDescriptionDataElementsType,
            load_control_event_data_elements: LoadControlEventDataElementsType,
            load_control_limit_constraints_data_elements: LoadControlLimitConstraintsDataElementsType,
            load_control_limit_data_elements: LoadControlLimitDataElementsType,
            load_control_limit_description_data_elements: LoadControlLimitDescriptionDataElementsType,
            load_control_node_data_elements: LoadControlNodeDataElementsType,
            load_control_state_data_elements: LoadControlStateDataElementsType,
            measurement_constraints_data_elements: MeasurementConstraintsDataElementsType,
            measurement_data_elements: MeasurementDataElementsType,
            measurement_description_data_elements: MeasurementDescriptionDataElementsType,
            measurement_series_data_elements: MeasurementSeriesDataElementsType,
            measurement_threshold_relation_data_elements: MeasurementThresholdRelationDataElementsType,
            messaging_data_elements: MessagingDataElementsType,
            network_management_abort_call_elements: NetworkManagementAbortCallElementsType,
            network_management_add_node_call_elements: NetworkManagementAddNodeCallElementsType,
            network_management_device_description_data_elements: NetworkManagementDeviceDescriptionDataElementsType,
            network_management_discover_call_elements: NetworkManagementDiscoverCallElementsType,
            network_management_entity_description_data_elements: NetworkManagementEntityDescriptionDataElementsType,
            network_management_feature_description_data_elements: NetworkManagementFeatureDescriptionDataElementsType,
            network_management_joining_mode_data_elements: NetworkManagementJoiningModeDataElementsType,
            network_management_modify_node_call_elements: NetworkManagementModifyNodeCallElementsType,
            network_management_process_state_data_elements: NetworkManagementProcessStateDataElementsType,
            network_management_remove_node_call_elements: NetworkManagementRemoveNodeCallElementsType,
            network_management_report_candidate_data_elements: NetworkManagementReportCandidateDataElementsType,
            network_management_scan_network_call_elements: NetworkManagementScanNetworkCallElementsType,
            node_management_binding_data_elements: NodeManagementBindingDataElementsType,
            node_management_binding_delete_call_elements: NodeManagementBindingDeleteCallElementsType,
            node_management_binding_request_call_elements: NodeManagementBindingRequestCallElementsType,
            node_management_destination_data_elements: NodeManagementDestinationDataElementsType,
            node_management_detailed_discovery_data_elements: NodeManagementDetailedDiscoveryDataElementsType,
            node_management_subscription_data_elements: NodeManagementSubscriptionDataElementsType,
            node_management_subscription_delete_call_elements: NodeManagementSubscriptionDeleteCallElementsType,
            node_management_subscription_request_call_elements: NodeManagementSubscriptionRequestCallElementsType,
            node_management_use_case_data_elements: NodeManagementUseCaseDataElementsType,
            operating_constraints_duration_data_elements: OperatingConstraintsDurationDataElementsType,
            operating_constraints_interrupt_data_elements: OperatingConstraintsInterruptDataElementsType,
            operating_constraints_power_description_data_elements: OperatingConstraintsPowerDescriptionDataElementsType,
            operating_constraints_power_level_data_elements: OperatingConstraintsPowerLevelDataElementsType,
            operating_constraints_power_range_data_elements: OperatingConstraintsPowerRangeDataElementsType,
            operating_constraints_resume_implication_data_elements: OperatingConstraintsResumeImplicationDataElementsType,
            power_sequence_alternatives_relation_data_elements: PowerSequenceAlternativesRelationDataElementsType,
            power_sequence_description_data_elements: PowerSequenceDescriptionDataElementsType,
            power_sequence_node_schedule_information_data_elements: PowerSequenceNodeScheduleInformationDataElementsType,
            power_sequence_price_calculation_request_call_elements: PowerSequencePriceCalculationRequestCallElementsType,
            power_sequence_price_data_elements: PowerSequencePriceDataElementsType,
            power_sequence_schedule_configuration_request_call_elements: PowerSequenceScheduleConfigurationRequestCallElementsType,
            power_sequence_schedule_constraints_data_elements: PowerSequenceScheduleConstraintsDataElementsType,
            power_sequence_schedule_data_elements: PowerSequenceScheduleDataElementsType,
            power_sequence_schedule_preference_data_elements: PowerSequenceSchedulePreferenceDataElementsType,
            power_sequence_state_data_elements: PowerSequenceStateDataElementsType,
            power_time_slot_schedule_constraints_data_elements: PowerTimeSlotScheduleConstraintsDataElementsType,
            power_time_slot_schedule_data_elements: PowerTimeSlotScheduleDataElementsType,
            power_time_slot_value_data_elements: PowerTimeSlotValueDataElementsType,
            sensing_data_elements: SensingDataElementsType,
            sensing_description_data_elements: SensingDescriptionDataElementsType,
            session_identification_data_elements: SessionIdentificationDataElementsType,
            session_measurement_relation_data_elements: SessionMeasurementRelationDataElementsType,
            setpoint_constraints_data_elements: SetpointConstraintsDataElementsType,
            setpoint_data_elements: SetpointDataElementsType,
            setpoint_description_data_elements: SetpointDescriptionDataElementsType,
            smart_energy_management_ps_configuration_request_call_elements: SmartEnergyManagementPsConfigurationRequestCallElementsType,
            smart_energy_management_ps_data_elements: SmartEnergyManagementPsDataElementsType,
            smart_energy_management_ps_price_calculation_request_call_elements: SmartEnergyManagementPsPriceCalculationRequestCallElementsType,
            smart_energy_management_ps_price_data_elements: SmartEnergyManagementPsPriceDataElementsType,
            specification_version_data_elements: SpecificationVersionDataElementsType,
            state_information_data_elements: StateInformationDataElementsType,
            subscription_management_delete_call_elements: SubscriptionManagementDeleteCallElementsType,
            subscription_management_entry_data_elements: SubscriptionManagementEntryDataElementsType,
            subscription_management_request_call_elements: SubscriptionManagementRequestCallElementsType,
            supply_condition_data_elements: SupplyConditionDataElementsType,
            supply_condition_description_data_elements: SupplyConditionDescriptionDataElementsType,
            supply_condition_threshold_relation_data_elements: SupplyConditionThresholdRelationDataElementsType,
            tariff_boundary_relation_data_elements: TariffBoundaryRelationDataElementsType,
            tariff_data_elements: TariffDataElementsType,
            tariff_description_data_elements: TariffDescriptionDataElementsType,
            tariff_overall_constraints_data_elements: TariffOverallConstraintsDataElementsType,
            tariff_tier_relation_data_elements: TariffTierRelationDataElementsType,
            task_management_job_data_elements: TaskManagementJobDataElementsType,
            task_management_job_description_data_elements: TaskManagementJobDescriptionDataElementsType,
            task_management_job_relation_data_elements: TaskManagementJobRelationDataElementsType,
            task_management_overview_data_elements: TaskManagementOverviewDataElementsType,
            threshold_constraints_data_elements: ThresholdConstraintsDataElementsType,
            threshold_data_elements: ThresholdDataElementsType,
            threshold_description_data_elements: ThresholdDescriptionDataElementsType,
            tier_boundary_data_elements: TierBoundaryDataElementsType,
            tier_boundary_description_data_elements: TierBoundaryDescriptionDataElementsType,
            tier_data_elements: TierDataElementsType,
            tier_description_data_elements: TierDescriptionDataElementsType,
            tier_incentive_relation_data_elements: TierIncentiveRelationDataElementsType,
            time_distributor_data_elements: TimeDistributorDataElementsType,
            time_distributor_enquiry_call_elements: TimeDistributorEnquiryCallElementsType,
            time_information_data_elements: TimeInformationDataElementsType,
            time_precision_data_elements: TimePrecisionDataElementsType,
            time_series_constraints_data_elements: TimeSeriesConstraintsDataElementsType,
            time_series_data_elements: TimeSeriesDataElementsType,
            time_series_description_data_elements: TimeSeriesDescriptionDataElementsType,
            time_table_constraints_data_elements: TimeTableConstraintsDataElementsType,
            time_table_data_elements: TimeTableDataElementsType,
            time_table_description_data_elements: TimeTableDescriptionDataElementsType,
            use_case_information_data_elements: UseCaseInformationDataElementsType,
    ):
        super().__init__()
        
        self.actuator_level_data_elements = actuator_level_data_elements
        self.actuator_level_description_data_elements = actuator_level_description_data_elements
        self.actuator_switch_data_elements = actuator_switch_data_elements
        self.actuator_switch_description_data_elements = actuator_switch_description_data_elements
        self.alarm_data_elements = alarm_data_elements
        self.bill_constraints_data_elements = bill_constraints_data_elements
        self.bill_data_elements = bill_data_elements
        self.bill_description_data_elements = bill_description_data_elements
        self.binding_management_delete_call_elements = binding_management_delete_call_elements
        self.binding_management_entry_data_elements = binding_management_entry_data_elements
        self.binding_management_request_call_elements = binding_management_request_call_elements
        self.commodity_data_elements = commodity_data_elements
        self.data_tunneling_call_elements = data_tunneling_call_elements
        self.device_classification_manufacturer_data_elements = device_classification_manufacturer_data_elements
        self.device_classification_user_data_elements = device_classification_user_data_elements
        self.device_configuration_key_value_constraints_data_elements = device_configuration_key_value_constraints_data_elements
        self.device_configuration_key_value_data_elements = device_configuration_key_value_data_elements
        self.device_configuration_key_value_description_data_elements = device_configuration_key_value_description_data_elements
        self.device_diagnosis_heartbeat_data_elements = device_diagnosis_heartbeat_data_elements
        self.device_diagnosis_service_data_elements = device_diagnosis_service_data_elements
        self.device_diagnosis_state_data_elements = device_diagnosis_state_data_elements
        self.direct_control_activity_data_elements = direct_control_activity_data_elements
        self.direct_control_description_data_elements = direct_control_description_data_elements
        self.electrical_connection_characteristic_data_elements = electrical_connection_characteristic_data_elements
        self.electrical_connection_description_data_elements = electrical_connection_description_data_elements
        self.electrical_connection_parameter_description_data_elements = electrical_connection_parameter_description_data_elements
        self.electrical_connection_permitted_value_set_data_elements = electrical_connection_permitted_value_set_data_elements
        self.electrical_connection_state_data_elements = electrical_connection_state_data_elements
        self.hvac_operation_mode_description_data_elements = hvac_operation_mode_description_data_elements
        self.hvac_overrun_data_elements = hvac_overrun_data_elements
        self.hvac_overrun_description_data_elements = hvac_overrun_description_data_elements
        self.hvac_system_function_data_elements = hvac_system_function_data_elements
        self.hvac_system_function_description_data_elements = hvac_system_function_description_data_elements
        self.hvac_system_function_operation_mode_relation_data_elements = hvac_system_function_operation_mode_relation_data_elements
        self.hvac_system_function_power_sequence_relation_data_elements = hvac_system_function_power_sequence_relation_data_elements
        self.hvac_system_function_setpoint_relation_data_elements = hvac_system_function_setpoint_relation_data_elements
        self.identification_data_elements = identification_data_elements
        self.incentive_data_elements = incentive_data_elements
        self.incentive_description_data_elements = incentive_description_data_elements
        self.incentive_table_constraints_data_elements = incentive_table_constraints_data_elements
        self.incentive_table_data_elements = incentive_table_data_elements
        self.incentive_table_description_data_elements = incentive_table_description_data_elements
        self.load_control_event_data_elements = load_control_event_data_elements
        self.load_control_limit_constraints_data_elements = load_control_limit_constraints_data_elements
        self.load_control_limit_data_elements = load_control_limit_data_elements
        self.load_control_limit_description_data_elements = load_control_limit_description_data_elements
        self.load_control_node_data_elements = load_control_node_data_elements
        self.load_control_state_data_elements = load_control_state_data_elements
        self.measurement_constraints_data_elements = measurement_constraints_data_elements
        self.measurement_data_elements = measurement_data_elements
        self.measurement_description_data_elements = measurement_description_data_elements
        self.measurement_series_data_elements = measurement_series_data_elements
        self.measurement_threshold_relation_data_elements = measurement_threshold_relation_data_elements
        self.messaging_data_elements = messaging_data_elements
        self.network_management_abort_call_elements = network_management_abort_call_elements
        self.network_management_add_node_call_elements = network_management_add_node_call_elements
        self.network_management_device_description_data_elements = network_management_device_description_data_elements
        self.network_management_discover_call_elements = network_management_discover_call_elements
        self.network_management_entity_description_data_elements = network_management_entity_description_data_elements
        self.network_management_feature_description_data_elements = network_management_feature_description_data_elements
        self.network_management_joining_mode_data_elements = network_management_joining_mode_data_elements
        self.network_management_modify_node_call_elements = network_management_modify_node_call_elements
        self.network_management_process_state_data_elements = network_management_process_state_data_elements
        self.network_management_remove_node_call_elements = network_management_remove_node_call_elements
        self.network_management_report_candidate_data_elements = network_management_report_candidate_data_elements
        self.network_management_scan_network_call_elements = network_management_scan_network_call_elements
        self.node_management_binding_data_elements = node_management_binding_data_elements
        self.node_management_binding_delete_call_elements = node_management_binding_delete_call_elements
        self.node_management_binding_request_call_elements = node_management_binding_request_call_elements
        self.node_management_destination_data_elements = node_management_destination_data_elements
        self.node_management_detailed_discovery_data_elements = node_management_detailed_discovery_data_elements
        self.node_management_subscription_data_elements = node_management_subscription_data_elements
        self.node_management_subscription_delete_call_elements = node_management_subscription_delete_call_elements
        self.node_management_subscription_request_call_elements = node_management_subscription_request_call_elements
        self.node_management_use_case_data_elements = node_management_use_case_data_elements
        self.operating_constraints_duration_data_elements = operating_constraints_duration_data_elements
        self.operating_constraints_interrupt_data_elements = operating_constraints_interrupt_data_elements
        self.operating_constraints_power_description_data_elements = operating_constraints_power_description_data_elements
        self.operating_constraints_power_level_data_elements = operating_constraints_power_level_data_elements
        self.operating_constraints_power_range_data_elements = operating_constraints_power_range_data_elements
        self.operating_constraints_resume_implication_data_elements = operating_constraints_resume_implication_data_elements
        self.power_sequence_alternatives_relation_data_elements = power_sequence_alternatives_relation_data_elements
        self.power_sequence_description_data_elements = power_sequence_description_data_elements
        self.power_sequence_node_schedule_information_data_elements = power_sequence_node_schedule_information_data_elements
        self.power_sequence_price_calculation_request_call_elements = power_sequence_price_calculation_request_call_elements
        self.power_sequence_price_data_elements = power_sequence_price_data_elements
        self.power_sequence_schedule_configuration_request_call_elements = power_sequence_schedule_configuration_request_call_elements
        self.power_sequence_schedule_constraints_data_elements = power_sequence_schedule_constraints_data_elements
        self.power_sequence_schedule_data_elements = power_sequence_schedule_data_elements
        self.power_sequence_schedule_preference_data_elements = power_sequence_schedule_preference_data_elements
        self.power_sequence_state_data_elements = power_sequence_state_data_elements
        self.power_time_slot_schedule_constraints_data_elements = power_time_slot_schedule_constraints_data_elements
        self.power_time_slot_schedule_data_elements = power_time_slot_schedule_data_elements
        self.power_time_slot_value_data_elements = power_time_slot_value_data_elements
        self.sensing_data_elements = sensing_data_elements
        self.sensing_description_data_elements = sensing_description_data_elements
        self.session_identification_data_elements = session_identification_data_elements
        self.session_measurement_relation_data_elements = session_measurement_relation_data_elements
        self.setpoint_constraints_data_elements = setpoint_constraints_data_elements
        self.setpoint_data_elements = setpoint_data_elements
        self.setpoint_description_data_elements = setpoint_description_data_elements
        self.smart_energy_management_ps_configuration_request_call_elements = smart_energy_management_ps_configuration_request_call_elements
        self.smart_energy_management_ps_data_elements = smart_energy_management_ps_data_elements
        self.smart_energy_management_ps_price_calculation_request_call_elements = smart_energy_management_ps_price_calculation_request_call_elements
        self.smart_energy_management_ps_price_data_elements = smart_energy_management_ps_price_data_elements
        self.specification_version_data_elements = specification_version_data_elements
        self.state_information_data_elements = state_information_data_elements
        self.subscription_management_delete_call_elements = subscription_management_delete_call_elements
        self.subscription_management_entry_data_elements = subscription_management_entry_data_elements
        self.subscription_management_request_call_elements = subscription_management_request_call_elements
        self.supply_condition_data_elements = supply_condition_data_elements
        self.supply_condition_description_data_elements = supply_condition_description_data_elements
        self.supply_condition_threshold_relation_data_elements = supply_condition_threshold_relation_data_elements
        self.tariff_boundary_relation_data_elements = tariff_boundary_relation_data_elements
        self.tariff_data_elements = tariff_data_elements
        self.tariff_description_data_elements = tariff_description_data_elements
        self.tariff_overall_constraints_data_elements = tariff_overall_constraints_data_elements
        self.tariff_tier_relation_data_elements = tariff_tier_relation_data_elements
        self.task_management_job_data_elements = task_management_job_data_elements
        self.task_management_job_description_data_elements = task_management_job_description_data_elements
        self.task_management_job_relation_data_elements = task_management_job_relation_data_elements
        self.task_management_overview_data_elements = task_management_overview_data_elements
        self.threshold_constraints_data_elements = threshold_constraints_data_elements
        self.threshold_data_elements = threshold_data_elements
        self.threshold_description_data_elements = threshold_description_data_elements
        self.tier_boundary_data_elements = tier_boundary_data_elements
        self.tier_boundary_description_data_elements = tier_boundary_description_data_elements
        self.tier_data_elements = tier_data_elements
        self.tier_description_data_elements = tier_description_data_elements
        self.tier_incentive_relation_data_elements = tier_incentive_relation_data_elements
        self.time_distributor_data_elements = time_distributor_data_elements
        self.time_distributor_enquiry_call_elements = time_distributor_enquiry_call_elements
        self.time_information_data_elements = time_information_data_elements
        self.time_precision_data_elements = time_precision_data_elements
        self.time_series_constraints_data_elements = time_series_constraints_data_elements
        self.time_series_data_elements = time_series_data_elements
        self.time_series_description_data_elements = time_series_description_data_elements
        self.time_table_constraints_data_elements = time_table_constraints_data_elements
        self.time_table_data_elements = time_table_data_elements
        self.time_table_description_data_elements = time_table_description_data_elements
        self.use_case_information_data_elements = use_case_information_data_elements

        if not isinstance(self.actuator_level_data_elements, ActuatorLevelDataElementsType):
            raise TypeError("actuator_level_data_elements is not of type ActuatorLevelDataElementsType")
        
        if not isinstance(self.actuator_level_description_data_elements, ActuatorLevelDescriptionDataElementsType):
            raise TypeError("actuator_level_description_data_elements is not of type ActuatorLevelDescriptionDataElementsType")
        
        if not isinstance(self.actuator_switch_data_elements, ActuatorSwitchDataElementsType):
            raise TypeError("actuator_switch_data_elements is not of type ActuatorSwitchDataElementsType")
        
        if not isinstance(self.actuator_switch_description_data_elements, ActuatorSwitchDescriptionDataElementsType):
            raise TypeError("actuator_switch_description_data_elements is not of type ActuatorSwitchDescriptionDataElementsType")
        
        if not isinstance(self.alarm_data_elements, AlarmDataElementsType):
            raise TypeError("alarm_data_elements is not of type AlarmDataElementsType")
        
        if not isinstance(self.bill_constraints_data_elements, BillConstraintsDataElementsType):
            raise TypeError("bill_constraints_data_elements is not of type BillConstraintsDataElementsType")
        
        if not isinstance(self.bill_data_elements, BillDataElementsType):
            raise TypeError("bill_data_elements is not of type BillDataElementsType")
        
        if not isinstance(self.bill_description_data_elements, BillDescriptionDataElementsType):
            raise TypeError("bill_description_data_elements is not of type BillDescriptionDataElementsType")
        
        if not isinstance(self.binding_management_delete_call_elements, BindingManagementDeleteCallElementsType):
            raise TypeError("binding_management_delete_call_elements is not of type BindingManagementDeleteCallElementsType")
        
        if not isinstance(self.binding_management_entry_data_elements, BindingManagementEntryDataElementsType):
            raise TypeError("binding_management_entry_data_elements is not of type BindingManagementEntryDataElementsType")
        
        if not isinstance(self.binding_management_request_call_elements, BindingManagementRequestCallElementsType):
            raise TypeError("binding_management_request_call_elements is not of type BindingManagementRequestCallElementsType")
        
        if not isinstance(self.commodity_data_elements, CommodityDataElementsType):
            raise TypeError("commodity_data_elements is not of type CommodityDataElementsType")
        
        if not isinstance(self.data_tunneling_call_elements, DataTunnelingCallElementsType):
            raise TypeError("data_tunneling_call_elements is not of type DataTunnelingCallElementsType")
        
        if not isinstance(self.device_classification_manufacturer_data_elements, DeviceClassificationManufacturerDataElementsType):
            raise TypeError("device_classification_manufacturer_data_elements is not of type DeviceClassificationManufacturerDataElementsType")
        
        if not isinstance(self.device_classification_user_data_elements, DeviceClassificationUserDataElementsType):
            raise TypeError("device_classification_user_data_elements is not of type DeviceClassificationUserDataElementsType")
        
        if not isinstance(self.device_configuration_key_value_constraints_data_elements, DeviceConfigurationKeyValueConstraintsDataElementsType):
            raise TypeError("device_configuration_key_value_constraints_data_elements is not of type DeviceConfigurationKeyValueConstraintsDataElementsType")
        
        if not isinstance(self.device_configuration_key_value_data_elements, DeviceConfigurationKeyValueDataElementsType):
            raise TypeError("device_configuration_key_value_data_elements is not of type DeviceConfigurationKeyValueDataElementsType")
        
        if not isinstance(self.device_configuration_key_value_description_data_elements, DeviceConfigurationKeyValueDescriptionDataElementsType):
            raise TypeError("device_configuration_key_value_description_data_elements is not of type DeviceConfigurationKeyValueDescriptionDataElementsType")
        
        if not isinstance(self.device_diagnosis_heartbeat_data_elements, DeviceDiagnosisHeartbeatDataElementsType):
            raise TypeError("device_diagnosis_heartbeat_data_elements is not of type DeviceDiagnosisHeartbeatDataElementsType")
        
        if not isinstance(self.device_diagnosis_service_data_elements, DeviceDiagnosisServiceDataElementsType):
            raise TypeError("device_diagnosis_service_data_elements is not of type DeviceDiagnosisServiceDataElementsType")
        
        if not isinstance(self.device_diagnosis_state_data_elements, DeviceDiagnosisStateDataElementsType):
            raise TypeError("device_diagnosis_state_data_elements is not of type DeviceDiagnosisStateDataElementsType")
        
        if not isinstance(self.direct_control_activity_data_elements, DirectControlActivityDataElementsType):
            raise TypeError("direct_control_activity_data_elements is not of type DirectControlActivityDataElementsType")
        
        if not isinstance(self.direct_control_description_data_elements, DirectControlDescriptionDataElementsType):
            raise TypeError("direct_control_description_data_elements is not of type DirectControlDescriptionDataElementsType")
        
        if not isinstance(self.electrical_connection_characteristic_data_elements, ElectricalConnectionCharacteristicDataElementsType):
            raise TypeError("electrical_connection_characteristic_data_elements is not of type ElectricalConnectionCharacteristicDataElementsType")
        
        if not isinstance(self.electrical_connection_description_data_elements, ElectricalConnectionDescriptionDataElementsType):
            raise TypeError("electrical_connection_description_data_elements is not of type ElectricalConnectionDescriptionDataElementsType")
        
        if not isinstance(self.electrical_connection_parameter_description_data_elements, ElectricalConnectionParameterDescriptionDataElementsType):
            raise TypeError("electrical_connection_parameter_description_data_elements is not of type ElectricalConnectionParameterDescriptionDataElementsType")
        
        if not isinstance(self.electrical_connection_permitted_value_set_data_elements, ElectricalConnectionPermittedValueSetDataElementsType):
            raise TypeError("electrical_connection_permitted_value_set_data_elements is not of type ElectricalConnectionPermittedValueSetDataElementsType")
        
        if not isinstance(self.electrical_connection_state_data_elements, ElectricalConnectionStateDataElementsType):
            raise TypeError("electrical_connection_state_data_elements is not of type ElectricalConnectionStateDataElementsType")
        
        if not isinstance(self.hvac_operation_mode_description_data_elements, HvacOperationModeDescriptionDataElementsType):
            raise TypeError("hvac_operation_mode_description_data_elements is not of type HvacOperationModeDescriptionDataElementsType")
        
        if not isinstance(self.hvac_overrun_data_elements, HvacOverrunDataElementsType):
            raise TypeError("hvac_overrun_data_elements is not of type HvacOverrunDataElementsType")
        
        if not isinstance(self.hvac_overrun_description_data_elements, HvacOverrunDescriptionDataElementsType):
            raise TypeError("hvac_overrun_description_data_elements is not of type HvacOverrunDescriptionDataElementsType")
        
        if not isinstance(self.hvac_system_function_data_elements, HvacSystemFunctionDataElementsType):
            raise TypeError("hvac_system_function_data_elements is not of type HvacSystemFunctionDataElementsType")
        
        if not isinstance(self.hvac_system_function_description_data_elements, HvacSystemFunctionDescriptionDataElementsType):
            raise TypeError("hvac_system_function_description_data_elements is not of type HvacSystemFunctionDescriptionDataElementsType")
        
        if not isinstance(self.hvac_system_function_operation_mode_relation_data_elements, HvacSystemFunctionOperationModeRelationDataElementsType):
            raise TypeError("hvac_system_function_operation_mode_relation_data_elements is not of type HvacSystemFunctionOperationModeRelationDataElementsType")
        
        if not isinstance(self.hvac_system_function_power_sequence_relation_data_elements, HvacSystemFunctionPowerSequenceRelationDataElementsType):
            raise TypeError("hvac_system_function_power_sequence_relation_data_elements is not of type HvacSystemFunctionPowerSequenceRelationDataElementsType")
        
        if not isinstance(self.hvac_system_function_setpoint_relation_data_elements, HvacSystemFunctionSetpointRelationDataElementsType):
            raise TypeError("hvac_system_function_setpoint_relation_data_elements is not of type HvacSystemFunctionSetpointRelationDataElementsType")
        
        if not isinstance(self.identification_data_elements, IdentificationDataElementsType):
            raise TypeError("identification_data_elements is not of type IdentificationDataElementsType")
        
        if not isinstance(self.incentive_data_elements, IncentiveDataElementsType):
            raise TypeError("incentive_data_elements is not of type IncentiveDataElementsType")
        
        if not isinstance(self.incentive_description_data_elements, IncentiveDescriptionDataElementsType):
            raise TypeError("incentive_description_data_elements is not of type IncentiveDescriptionDataElementsType")
        
        if not isinstance(self.incentive_table_constraints_data_elements, IncentiveTableConstraintsDataElementsType):
            raise TypeError("incentive_table_constraints_data_elements is not of type IncentiveTableConstraintsDataElementsType")
        
        if not isinstance(self.incentive_table_data_elements, IncentiveTableDataElementsType):
            raise TypeError("incentive_table_data_elements is not of type IncentiveTableDataElementsType")
        
        if not isinstance(self.incentive_table_description_data_elements, IncentiveTableDescriptionDataElementsType):
            raise TypeError("incentive_table_description_data_elements is not of type IncentiveTableDescriptionDataElementsType")
        
        if not isinstance(self.load_control_event_data_elements, LoadControlEventDataElementsType):
            raise TypeError("load_control_event_data_elements is not of type LoadControlEventDataElementsType")
        
        if not isinstance(self.load_control_limit_constraints_data_elements, LoadControlLimitConstraintsDataElementsType):
            raise TypeError("load_control_limit_constraints_data_elements is not of type LoadControlLimitConstraintsDataElementsType")
        
        if not isinstance(self.load_control_limit_data_elements, LoadControlLimitDataElementsType):
            raise TypeError("load_control_limit_data_elements is not of type LoadControlLimitDataElementsType")
        
        if not isinstance(self.load_control_limit_description_data_elements, LoadControlLimitDescriptionDataElementsType):
            raise TypeError("load_control_limit_description_data_elements is not of type LoadControlLimitDescriptionDataElementsType")
        
        if not isinstance(self.load_control_node_data_elements, LoadControlNodeDataElementsType):
            raise TypeError("load_control_node_data_elements is not of type LoadControlNodeDataElementsType")
        
        if not isinstance(self.load_control_state_data_elements, LoadControlStateDataElementsType):
            raise TypeError("load_control_state_data_elements is not of type LoadControlStateDataElementsType")
        
        if not isinstance(self.measurement_constraints_data_elements, MeasurementConstraintsDataElementsType):
            raise TypeError("measurement_constraints_data_elements is not of type MeasurementConstraintsDataElementsType")
        
        if not isinstance(self.measurement_data_elements, MeasurementDataElementsType):
            raise TypeError("measurement_data_elements is not of type MeasurementDataElementsType")
        
        if not isinstance(self.measurement_description_data_elements, MeasurementDescriptionDataElementsType):
            raise TypeError("measurement_description_data_elements is not of type MeasurementDescriptionDataElementsType")
        
        if not isinstance(self.measurement_series_data_elements, MeasurementSeriesDataElementsType):
            raise TypeError("measurement_series_data_elements is not of type MeasurementSeriesDataElementsType")
        
        if not isinstance(self.measurement_threshold_relation_data_elements, MeasurementThresholdRelationDataElementsType):
            raise TypeError("measurement_threshold_relation_data_elements is not of type MeasurementThresholdRelationDataElementsType")
        
        if not isinstance(self.messaging_data_elements, MessagingDataElementsType):
            raise TypeError("messaging_data_elements is not of type MessagingDataElementsType")
        
        if not isinstance(self.network_management_abort_call_elements, NetworkManagementAbortCallElementsType):
            raise TypeError("network_management_abort_call_elements is not of type NetworkManagementAbortCallElementsType")
        
        if not isinstance(self.network_management_add_node_call_elements, NetworkManagementAddNodeCallElementsType):
            raise TypeError("network_management_add_node_call_elements is not of type NetworkManagementAddNodeCallElementsType")
        
        if not isinstance(self.network_management_device_description_data_elements, NetworkManagementDeviceDescriptionDataElementsType):
            raise TypeError("network_management_device_description_data_elements is not of type NetworkManagementDeviceDescriptionDataElementsType")
        
        if not isinstance(self.network_management_discover_call_elements, NetworkManagementDiscoverCallElementsType):
            raise TypeError("network_management_discover_call_elements is not of type NetworkManagementDiscoverCallElementsType")
        
        if not isinstance(self.network_management_entity_description_data_elements, NetworkManagementEntityDescriptionDataElementsType):
            raise TypeError("network_management_entity_description_data_elements is not of type NetworkManagementEntityDescriptionDataElementsType")
        
        if not isinstance(self.network_management_feature_description_data_elements, NetworkManagementFeatureDescriptionDataElementsType):
            raise TypeError("network_management_feature_description_data_elements is not of type NetworkManagementFeatureDescriptionDataElementsType")
        
        if not isinstance(self.network_management_joining_mode_data_elements, NetworkManagementJoiningModeDataElementsType):
            raise TypeError("network_management_joining_mode_data_elements is not of type NetworkManagementJoiningModeDataElementsType")
        
        if not isinstance(self.network_management_modify_node_call_elements, NetworkManagementModifyNodeCallElementsType):
            raise TypeError("network_management_modify_node_call_elements is not of type NetworkManagementModifyNodeCallElementsType")
        
        if not isinstance(self.network_management_process_state_data_elements, NetworkManagementProcessStateDataElementsType):
            raise TypeError("network_management_process_state_data_elements is not of type NetworkManagementProcessStateDataElementsType")
        
        if not isinstance(self.network_management_remove_node_call_elements, NetworkManagementRemoveNodeCallElementsType):
            raise TypeError("network_management_remove_node_call_elements is not of type NetworkManagementRemoveNodeCallElementsType")
        
        if not isinstance(self.network_management_report_candidate_data_elements, NetworkManagementReportCandidateDataElementsType):
            raise TypeError("network_management_report_candidate_data_elements is not of type NetworkManagementReportCandidateDataElementsType")
        
        if not isinstance(self.network_management_scan_network_call_elements, NetworkManagementScanNetworkCallElementsType):
            raise TypeError("network_management_scan_network_call_elements is not of type NetworkManagementScanNetworkCallElementsType")
        
        if not isinstance(self.node_management_binding_data_elements, NodeManagementBindingDataElementsType):
            raise TypeError("node_management_binding_data_elements is not of type NodeManagementBindingDataElementsType")
        
        if not isinstance(self.node_management_binding_delete_call_elements, NodeManagementBindingDeleteCallElementsType):
            raise TypeError("node_management_binding_delete_call_elements is not of type NodeManagementBindingDeleteCallElementsType")
        
        if not isinstance(self.node_management_binding_request_call_elements, NodeManagementBindingRequestCallElementsType):
            raise TypeError("node_management_binding_request_call_elements is not of type NodeManagementBindingRequestCallElementsType")
        
        if not isinstance(self.node_management_destination_data_elements, NodeManagementDestinationDataElementsType):
            raise TypeError("node_management_destination_data_elements is not of type NodeManagementDestinationDataElementsType")
        
        if not isinstance(self.node_management_detailed_discovery_data_elements, NodeManagementDetailedDiscoveryDataElementsType):
            raise TypeError("node_management_detailed_discovery_data_elements is not of type NodeManagementDetailedDiscoveryDataElementsType")
        
        if not isinstance(self.node_management_subscription_data_elements, NodeManagementSubscriptionDataElementsType):
            raise TypeError("node_management_subscription_data_elements is not of type NodeManagementSubscriptionDataElementsType")
        
        if not isinstance(self.node_management_subscription_delete_call_elements, NodeManagementSubscriptionDeleteCallElementsType):
            raise TypeError("node_management_subscription_delete_call_elements is not of type NodeManagementSubscriptionDeleteCallElementsType")
        
        if not isinstance(self.node_management_subscription_request_call_elements, NodeManagementSubscriptionRequestCallElementsType):
            raise TypeError("node_management_subscription_request_call_elements is not of type NodeManagementSubscriptionRequestCallElementsType")
        
        if not isinstance(self.node_management_use_case_data_elements, NodeManagementUseCaseDataElementsType):
            raise TypeError("node_management_use_case_data_elements is not of type NodeManagementUseCaseDataElementsType")
        
        if not isinstance(self.operating_constraints_duration_data_elements, OperatingConstraintsDurationDataElementsType):
            raise TypeError("operating_constraints_duration_data_elements is not of type OperatingConstraintsDurationDataElementsType")
        
        if not isinstance(self.operating_constraints_interrupt_data_elements, OperatingConstraintsInterruptDataElementsType):
            raise TypeError("operating_constraints_interrupt_data_elements is not of type OperatingConstraintsInterruptDataElementsType")
        
        if not isinstance(self.operating_constraints_power_description_data_elements, OperatingConstraintsPowerDescriptionDataElementsType):
            raise TypeError("operating_constraints_power_description_data_elements is not of type OperatingConstraintsPowerDescriptionDataElementsType")
        
        if not isinstance(self.operating_constraints_power_level_data_elements, OperatingConstraintsPowerLevelDataElementsType):
            raise TypeError("operating_constraints_power_level_data_elements is not of type OperatingConstraintsPowerLevelDataElementsType")
        
        if not isinstance(self.operating_constraints_power_range_data_elements, OperatingConstraintsPowerRangeDataElementsType):
            raise TypeError("operating_constraints_power_range_data_elements is not of type OperatingConstraintsPowerRangeDataElementsType")
        
        if not isinstance(self.operating_constraints_resume_implication_data_elements, OperatingConstraintsResumeImplicationDataElementsType):
            raise TypeError("operating_constraints_resume_implication_data_elements is not of type OperatingConstraintsResumeImplicationDataElementsType")
        
        if not isinstance(self.power_sequence_alternatives_relation_data_elements, PowerSequenceAlternativesRelationDataElementsType):
            raise TypeError("power_sequence_alternatives_relation_data_elements is not of type PowerSequenceAlternativesRelationDataElementsType")
        
        if not isinstance(self.power_sequence_description_data_elements, PowerSequenceDescriptionDataElementsType):
            raise TypeError("power_sequence_description_data_elements is not of type PowerSequenceDescriptionDataElementsType")
        
        if not isinstance(self.power_sequence_node_schedule_information_data_elements, PowerSequenceNodeScheduleInformationDataElementsType):
            raise TypeError("power_sequence_node_schedule_information_data_elements is not of type PowerSequenceNodeScheduleInformationDataElementsType")
        
        if not isinstance(self.power_sequence_price_calculation_request_call_elements, PowerSequencePriceCalculationRequestCallElementsType):
            raise TypeError("power_sequence_price_calculation_request_call_elements is not of type PowerSequencePriceCalculationRequestCallElementsType")
        
        if not isinstance(self.power_sequence_price_data_elements, PowerSequencePriceDataElementsType):
            raise TypeError("power_sequence_price_data_elements is not of type PowerSequencePriceDataElementsType")
        
        if not isinstance(self.power_sequence_schedule_configuration_request_call_elements, PowerSequenceScheduleConfigurationRequestCallElementsType):
            raise TypeError("power_sequence_schedule_configuration_request_call_elements is not of type PowerSequenceScheduleConfigurationRequestCallElementsType")
        
        if not isinstance(self.power_sequence_schedule_constraints_data_elements, PowerSequenceScheduleConstraintsDataElementsType):
            raise TypeError("power_sequence_schedule_constraints_data_elements is not of type PowerSequenceScheduleConstraintsDataElementsType")
        
        if not isinstance(self.power_sequence_schedule_data_elements, PowerSequenceScheduleDataElementsType):
            raise TypeError("power_sequence_schedule_data_elements is not of type PowerSequenceScheduleDataElementsType")
        
        if not isinstance(self.power_sequence_schedule_preference_data_elements, PowerSequenceSchedulePreferenceDataElementsType):
            raise TypeError("power_sequence_schedule_preference_data_elements is not of type PowerSequenceSchedulePreferenceDataElementsType")
        
        if not isinstance(self.power_sequence_state_data_elements, PowerSequenceStateDataElementsType):
            raise TypeError("power_sequence_state_data_elements is not of type PowerSequenceStateDataElementsType")
        
        if not isinstance(self.power_time_slot_schedule_constraints_data_elements, PowerTimeSlotScheduleConstraintsDataElementsType):
            raise TypeError("power_time_slot_schedule_constraints_data_elements is not of type PowerTimeSlotScheduleConstraintsDataElementsType")
        
        if not isinstance(self.power_time_slot_schedule_data_elements, PowerTimeSlotScheduleDataElementsType):
            raise TypeError("power_time_slot_schedule_data_elements is not of type PowerTimeSlotScheduleDataElementsType")
        
        if not isinstance(self.power_time_slot_value_data_elements, PowerTimeSlotValueDataElementsType):
            raise TypeError("power_time_slot_value_data_elements is not of type PowerTimeSlotValueDataElementsType")
        
        if not isinstance(self.sensing_data_elements, SensingDataElementsType):
            raise TypeError("sensing_data_elements is not of type SensingDataElementsType")
        
        if not isinstance(self.sensing_description_data_elements, SensingDescriptionDataElementsType):
            raise TypeError("sensing_description_data_elements is not of type SensingDescriptionDataElementsType")
        
        if not isinstance(self.session_identification_data_elements, SessionIdentificationDataElementsType):
            raise TypeError("session_identification_data_elements is not of type SessionIdentificationDataElementsType")
        
        if not isinstance(self.session_measurement_relation_data_elements, SessionMeasurementRelationDataElementsType):
            raise TypeError("session_measurement_relation_data_elements is not of type SessionMeasurementRelationDataElementsType")
        
        if not isinstance(self.setpoint_constraints_data_elements, SetpointConstraintsDataElementsType):
            raise TypeError("setpoint_constraints_data_elements is not of type SetpointConstraintsDataElementsType")
        
        if not isinstance(self.setpoint_data_elements, SetpointDataElementsType):
            raise TypeError("setpoint_data_elements is not of type SetpointDataElementsType")
        
        if not isinstance(self.setpoint_description_data_elements, SetpointDescriptionDataElementsType):
            raise TypeError("setpoint_description_data_elements is not of type SetpointDescriptionDataElementsType")
        
        if not isinstance(self.smart_energy_management_ps_configuration_request_call_elements, SmartEnergyManagementPsConfigurationRequestCallElementsType):
            raise TypeError("smart_energy_management_ps_configuration_request_call_elements is not of type SmartEnergyManagementPsConfigurationRequestCallElementsType")
        
        if not isinstance(self.smart_energy_management_ps_data_elements, SmartEnergyManagementPsDataElementsType):
            raise TypeError("smart_energy_management_ps_data_elements is not of type SmartEnergyManagementPsDataElementsType")
        
        if not isinstance(self.smart_energy_management_ps_price_calculation_request_call_elements, SmartEnergyManagementPsPriceCalculationRequestCallElementsType):
            raise TypeError("smart_energy_management_ps_price_calculation_request_call_elements is not of type SmartEnergyManagementPsPriceCalculationRequestCallElementsType")
        
        if not isinstance(self.smart_energy_management_ps_price_data_elements, SmartEnergyManagementPsPriceDataElementsType):
            raise TypeError("smart_energy_management_ps_price_data_elements is not of type SmartEnergyManagementPsPriceDataElementsType")
        
        if not isinstance(self.specification_version_data_elements, SpecificationVersionDataElementsType):
            raise TypeError("specification_version_data_elements is not of type SpecificationVersionDataElementsType")
        
        if not isinstance(self.state_information_data_elements, StateInformationDataElementsType):
            raise TypeError("state_information_data_elements is not of type StateInformationDataElementsType")
        
        if not isinstance(self.subscription_management_delete_call_elements, SubscriptionManagementDeleteCallElementsType):
            raise TypeError("subscription_management_delete_call_elements is not of type SubscriptionManagementDeleteCallElementsType")
        
        if not isinstance(self.subscription_management_entry_data_elements, SubscriptionManagementEntryDataElementsType):
            raise TypeError("subscription_management_entry_data_elements is not of type SubscriptionManagementEntryDataElementsType")
        
        if not isinstance(self.subscription_management_request_call_elements, SubscriptionManagementRequestCallElementsType):
            raise TypeError("subscription_management_request_call_elements is not of type SubscriptionManagementRequestCallElementsType")
        
        if not isinstance(self.supply_condition_data_elements, SupplyConditionDataElementsType):
            raise TypeError("supply_condition_data_elements is not of type SupplyConditionDataElementsType")
        
        if not isinstance(self.supply_condition_description_data_elements, SupplyConditionDescriptionDataElementsType):
            raise TypeError("supply_condition_description_data_elements is not of type SupplyConditionDescriptionDataElementsType")
        
        if not isinstance(self.supply_condition_threshold_relation_data_elements, SupplyConditionThresholdRelationDataElementsType):
            raise TypeError("supply_condition_threshold_relation_data_elements is not of type SupplyConditionThresholdRelationDataElementsType")
        
        if not isinstance(self.tariff_boundary_relation_data_elements, TariffBoundaryRelationDataElementsType):
            raise TypeError("tariff_boundary_relation_data_elements is not of type TariffBoundaryRelationDataElementsType")
        
        if not isinstance(self.tariff_data_elements, TariffDataElementsType):
            raise TypeError("tariff_data_elements is not of type TariffDataElementsType")
        
        if not isinstance(self.tariff_description_data_elements, TariffDescriptionDataElementsType):
            raise TypeError("tariff_description_data_elements is not of type TariffDescriptionDataElementsType")
        
        if not isinstance(self.tariff_overall_constraints_data_elements, TariffOverallConstraintsDataElementsType):
            raise TypeError("tariff_overall_constraints_data_elements is not of type TariffOverallConstraintsDataElementsType")
        
        if not isinstance(self.tariff_tier_relation_data_elements, TariffTierRelationDataElementsType):
            raise TypeError("tariff_tier_relation_data_elements is not of type TariffTierRelationDataElementsType")
        
        if not isinstance(self.task_management_job_data_elements, TaskManagementJobDataElementsType):
            raise TypeError("task_management_job_data_elements is not of type TaskManagementJobDataElementsType")
        
        if not isinstance(self.task_management_job_description_data_elements, TaskManagementJobDescriptionDataElementsType):
            raise TypeError("task_management_job_description_data_elements is not of type TaskManagementJobDescriptionDataElementsType")
        
        if not isinstance(self.task_management_job_relation_data_elements, TaskManagementJobRelationDataElementsType):
            raise TypeError("task_management_job_relation_data_elements is not of type TaskManagementJobRelationDataElementsType")
        
        if not isinstance(self.task_management_overview_data_elements, TaskManagementOverviewDataElementsType):
            raise TypeError("task_management_overview_data_elements is not of type TaskManagementOverviewDataElementsType")
        
        if not isinstance(self.threshold_constraints_data_elements, ThresholdConstraintsDataElementsType):
            raise TypeError("threshold_constraints_data_elements is not of type ThresholdConstraintsDataElementsType")
        
        if not isinstance(self.threshold_data_elements, ThresholdDataElementsType):
            raise TypeError("threshold_data_elements is not of type ThresholdDataElementsType")
        
        if not isinstance(self.threshold_description_data_elements, ThresholdDescriptionDataElementsType):
            raise TypeError("threshold_description_data_elements is not of type ThresholdDescriptionDataElementsType")
        
        if not isinstance(self.tier_boundary_data_elements, TierBoundaryDataElementsType):
            raise TypeError("tier_boundary_data_elements is not of type TierBoundaryDataElementsType")
        
        if not isinstance(self.tier_boundary_description_data_elements, TierBoundaryDescriptionDataElementsType):
            raise TypeError("tier_boundary_description_data_elements is not of type TierBoundaryDescriptionDataElementsType")
        
        if not isinstance(self.tier_data_elements, TierDataElementsType):
            raise TypeError("tier_data_elements is not of type TierDataElementsType")
        
        if not isinstance(self.tier_description_data_elements, TierDescriptionDataElementsType):
            raise TypeError("tier_description_data_elements is not of type TierDescriptionDataElementsType")
        
        if not isinstance(self.tier_incentive_relation_data_elements, TierIncentiveRelationDataElementsType):
            raise TypeError("tier_incentive_relation_data_elements is not of type TierIncentiveRelationDataElementsType")
        
        if not isinstance(self.time_distributor_data_elements, TimeDistributorDataElementsType):
            raise TypeError("time_distributor_data_elements is not of type TimeDistributorDataElementsType")
        
        if not isinstance(self.time_distributor_enquiry_call_elements, TimeDistributorEnquiryCallElementsType):
            raise TypeError("time_distributor_enquiry_call_elements is not of type TimeDistributorEnquiryCallElementsType")
        
        if not isinstance(self.time_information_data_elements, TimeInformationDataElementsType):
            raise TypeError("time_information_data_elements is not of type TimeInformationDataElementsType")
        
        if not isinstance(self.time_precision_data_elements, TimePrecisionDataElementsType):
            raise TypeError("time_precision_data_elements is not of type TimePrecisionDataElementsType")
        
        if not isinstance(self.time_series_constraints_data_elements, TimeSeriesConstraintsDataElementsType):
            raise TypeError("time_series_constraints_data_elements is not of type TimeSeriesConstraintsDataElementsType")
        
        if not isinstance(self.time_series_data_elements, TimeSeriesDataElementsType):
            raise TypeError("time_series_data_elements is not of type TimeSeriesDataElementsType")
        
        if not isinstance(self.time_series_description_data_elements, TimeSeriesDescriptionDataElementsType):
            raise TypeError("time_series_description_data_elements is not of type TimeSeriesDescriptionDataElementsType")
        
        if not isinstance(self.time_table_constraints_data_elements, TimeTableConstraintsDataElementsType):
            raise TypeError("time_table_constraints_data_elements is not of type TimeTableConstraintsDataElementsType")
        
        if not isinstance(self.time_table_data_elements, TimeTableDataElementsType):
            raise TypeError("time_table_data_elements is not of type TimeTableDataElementsType")
        
        if not isinstance(self.time_table_description_data_elements, TimeTableDescriptionDataElementsType):
            raise TypeError("time_table_description_data_elements is not of type TimeTableDescriptionDataElementsType")
        
        if not isinstance(self.use_case_information_data_elements, UseCaseInformationDataElementsType):
            raise TypeError("use_case_information_data_elements is not of type UseCaseInformationDataElementsType")
        
    def get_data(self): # ChoiceType

        msg_data = []
        
        if self.actuator_level_data_elements is not None:
            msg_data.append({"actuatorLevelDataElements": self.actuator_level_data_elements.get_data()})
        if self.actuator_level_description_data_elements is not None:
            msg_data.append({"actuatorLevelDescriptionDataElements": self.actuator_level_description_data_elements.get_data()})
        if self.actuator_switch_data_elements is not None:
            msg_data.append({"actuatorSwitchDataElements": self.actuator_switch_data_elements.get_data()})
        if self.actuator_switch_description_data_elements is not None:
            msg_data.append({"actuatorSwitchDescriptionDataElements": self.actuator_switch_description_data_elements.get_data()})
        if self.alarm_data_elements is not None:
            msg_data.append({"alarmDataElements": self.alarm_data_elements.get_data()})
        if self.bill_constraints_data_elements is not None:
            msg_data.append({"billConstraintsDataElements": self.bill_constraints_data_elements.get_data()})
        if self.bill_data_elements is not None:
            msg_data.append({"billDataElements": self.bill_data_elements.get_data()})
        if self.bill_description_data_elements is not None:
            msg_data.append({"billDescriptionDataElements": self.bill_description_data_elements.get_data()})
        if self.binding_management_delete_call_elements is not None:
            msg_data.append({"bindingManagementDeleteCallElements": self.binding_management_delete_call_elements.get_data()})
        if self.binding_management_entry_data_elements is not None:
            msg_data.append({"bindingManagementEntryDataElements": self.binding_management_entry_data_elements.get_data()})
        if self.binding_management_request_call_elements is not None:
            msg_data.append({"bindingManagementRequestCallElements": self.binding_management_request_call_elements.get_data()})
        if self.commodity_data_elements is not None:
            msg_data.append({"commodityDataElements": self.commodity_data_elements.get_data()})
        if self.data_tunneling_call_elements is not None:
            msg_data.append({"dataTunnelingCallElements": self.data_tunneling_call_elements.get_data()})
        if self.device_classification_manufacturer_data_elements is not None:
            msg_data.append({"deviceClassificationManufacturerDataElements": self.device_classification_manufacturer_data_elements.get_data()})
        if self.device_classification_user_data_elements is not None:
            msg_data.append({"deviceClassificationUserDataElements": self.device_classification_user_data_elements.get_data()})
        if self.device_configuration_key_value_constraints_data_elements is not None:
            msg_data.append({"deviceConfigurationKeyValueConstraintsDataElements": self.device_configuration_key_value_constraints_data_elements.get_data()})
        if self.device_configuration_key_value_data_elements is not None:
            msg_data.append({"deviceConfigurationKeyValueDataElements": self.device_configuration_key_value_data_elements.get_data()})
        if self.device_configuration_key_value_description_data_elements is not None:
            msg_data.append({"deviceConfigurationKeyValueDescriptionDataElements": self.device_configuration_key_value_description_data_elements.get_data()})
        if self.device_diagnosis_heartbeat_data_elements is not None:
            msg_data.append({"deviceDiagnosisHeartbeatDataElements": self.device_diagnosis_heartbeat_data_elements.get_data()})
        if self.device_diagnosis_service_data_elements is not None:
            msg_data.append({"deviceDiagnosisServiceDataElements": self.device_diagnosis_service_data_elements.get_data()})
        if self.device_diagnosis_state_data_elements is not None:
            msg_data.append({"deviceDiagnosisStateDataElements": self.device_diagnosis_state_data_elements.get_data()})
        if self.direct_control_activity_data_elements is not None:
            msg_data.append({"directControlActivityDataElements": self.direct_control_activity_data_elements.get_data()})
        if self.direct_control_description_data_elements is not None:
            msg_data.append({"directControlDescriptionDataElements": self.direct_control_description_data_elements.get_data()})
        if self.electrical_connection_characteristic_data_elements is not None:
            msg_data.append({"electricalConnectionCharacteristicDataElements": self.electrical_connection_characteristic_data_elements.get_data()})
        if self.electrical_connection_description_data_elements is not None:
            msg_data.append({"electricalConnectionDescriptionDataElements": self.electrical_connection_description_data_elements.get_data()})
        if self.electrical_connection_parameter_description_data_elements is not None:
            msg_data.append({"electricalConnectionParameterDescriptionDataElements": self.electrical_connection_parameter_description_data_elements.get_data()})
        if self.electrical_connection_permitted_value_set_data_elements is not None:
            msg_data.append({"electricalConnectionPermittedValueSetDataElements": self.electrical_connection_permitted_value_set_data_elements.get_data()})
        if self.electrical_connection_state_data_elements is not None:
            msg_data.append({"electricalConnectionStateDataElements": self.electrical_connection_state_data_elements.get_data()})
        if self.hvac_operation_mode_description_data_elements is not None:
            msg_data.append({"hvacOperationModeDescriptionDataElements": self.hvac_operation_mode_description_data_elements.get_data()})
        if self.hvac_overrun_data_elements is not None:
            msg_data.append({"hvacOverrunDataElements": self.hvac_overrun_data_elements.get_data()})
        if self.hvac_overrun_description_data_elements is not None:
            msg_data.append({"hvacOverrunDescriptionDataElements": self.hvac_overrun_description_data_elements.get_data()})
        if self.hvac_system_function_data_elements is not None:
            msg_data.append({"hvacSystemFunctionDataElements": self.hvac_system_function_data_elements.get_data()})
        if self.hvac_system_function_description_data_elements is not None:
            msg_data.append({"hvacSystemFunctionDescriptionDataElements": self.hvac_system_function_description_data_elements.get_data()})
        if self.hvac_system_function_operation_mode_relation_data_elements is not None:
            msg_data.append({"hvacSystemFunctionOperationModeRelationDataElements": self.hvac_system_function_operation_mode_relation_data_elements.get_data()})
        if self.hvac_system_function_power_sequence_relation_data_elements is not None:
            msg_data.append({"hvacSystemFunctionPowerSequenceRelationDataElements": self.hvac_system_function_power_sequence_relation_data_elements.get_data()})
        if self.hvac_system_function_setpoint_relation_data_elements is not None:
            msg_data.append({"hvacSystemFunctionSetpointRelationDataElements": self.hvac_system_function_setpoint_relation_data_elements.get_data()})
        if self.identification_data_elements is not None:
            msg_data.append({"identificationDataElements": self.identification_data_elements.get_data()})
        if self.incentive_data_elements is not None:
            msg_data.append({"incentiveDataElements": self.incentive_data_elements.get_data()})
        if self.incentive_description_data_elements is not None:
            msg_data.append({"incentiveDescriptionDataElements": self.incentive_description_data_elements.get_data()})
        if self.incentive_table_constraints_data_elements is not None:
            msg_data.append({"incentiveTableConstraintsDataElements": self.incentive_table_constraints_data_elements.get_data()})
        if self.incentive_table_data_elements is not None:
            msg_data.append({"incentiveTableDataElements": self.incentive_table_data_elements.get_data()})
        if self.incentive_table_description_data_elements is not None:
            msg_data.append({"incentiveTableDescriptionDataElements": self.incentive_table_description_data_elements.get_data()})
        if self.load_control_event_data_elements is not None:
            msg_data.append({"loadControlEventDataElements": self.load_control_event_data_elements.get_data()})
        if self.load_control_limit_constraints_data_elements is not None:
            msg_data.append({"loadControlLimitConstraintsDataElements": self.load_control_limit_constraints_data_elements.get_data()})
        if self.load_control_limit_data_elements is not None:
            msg_data.append({"loadControlLimitDataElements": self.load_control_limit_data_elements.get_data()})
        if self.load_control_limit_description_data_elements is not None:
            msg_data.append({"loadControlLimitDescriptionDataElements": self.load_control_limit_description_data_elements.get_data()})
        if self.load_control_node_data_elements is not None:
            msg_data.append({"loadControlNodeDataElements": self.load_control_node_data_elements.get_data()})
        if self.load_control_state_data_elements is not None:
            msg_data.append({"loadControlStateDataElements": self.load_control_state_data_elements.get_data()})
        if self.measurement_constraints_data_elements is not None:
            msg_data.append({"measurementConstraintsDataElements": self.measurement_constraints_data_elements.get_data()})
        if self.measurement_data_elements is not None:
            msg_data.append({"measurementDataElements": self.measurement_data_elements.get_data()})
        if self.measurement_description_data_elements is not None:
            msg_data.append({"measurementDescriptionDataElements": self.measurement_description_data_elements.get_data()})
        if self.measurement_series_data_elements is not None:
            msg_data.append({"measurementSeriesDataElements": self.measurement_series_data_elements.get_data()})
        if self.measurement_threshold_relation_data_elements is not None:
            msg_data.append({"measurementThresholdRelationDataElements": self.measurement_threshold_relation_data_elements.get_data()})
        if self.messaging_data_elements is not None:
            msg_data.append({"messagingDataElements": self.messaging_data_elements.get_data()})
        if self.network_management_abort_call_elements is not None:
            msg_data.append({"networkManagementAbortCallElements": self.network_management_abort_call_elements.get_data()})
        if self.network_management_add_node_call_elements is not None:
            msg_data.append({"networkManagementAddNodeCallElements": self.network_management_add_node_call_elements.get_data()})
        if self.network_management_device_description_data_elements is not None:
            msg_data.append({"networkManagementDeviceDescriptionDataElements": self.network_management_device_description_data_elements.get_data()})
        if self.network_management_discover_call_elements is not None:
            msg_data.append({"networkManagementDiscoverCallElements": self.network_management_discover_call_elements.get_data()})
        if self.network_management_entity_description_data_elements is not None:
            msg_data.append({"networkManagementEntityDescriptionDataElements": self.network_management_entity_description_data_elements.get_data()})
        if self.network_management_feature_description_data_elements is not None:
            msg_data.append({"networkManagementFeatureDescriptionDataElements": self.network_management_feature_description_data_elements.get_data()})
        if self.network_management_joining_mode_data_elements is not None:
            msg_data.append({"networkManagementJoiningModeDataElements": self.network_management_joining_mode_data_elements.get_data()})
        if self.network_management_modify_node_call_elements is not None:
            msg_data.append({"networkManagementModifyNodeCallElements": self.network_management_modify_node_call_elements.get_data()})
        if self.network_management_process_state_data_elements is not None:
            msg_data.append({"networkManagementProcessStateDataElements": self.network_management_process_state_data_elements.get_data()})
        if self.network_management_remove_node_call_elements is not None:
            msg_data.append({"networkManagementRemoveNodeCallElements": self.network_management_remove_node_call_elements.get_data()})
        if self.network_management_report_candidate_data_elements is not None:
            msg_data.append({"networkManagementReportCandidateDataElements": self.network_management_report_candidate_data_elements.get_data()})
        if self.network_management_scan_network_call_elements is not None:
            msg_data.append({"networkManagementScanNetworkCallElements": self.network_management_scan_network_call_elements.get_data()})
        if self.node_management_binding_data_elements is not None:
            msg_data.append({"nodeManagementBindingDataElements": self.node_management_binding_data_elements.get_data()})
        if self.node_management_binding_delete_call_elements is not None:
            msg_data.append({"nodeManagementBindingDeleteCallElements": self.node_management_binding_delete_call_elements.get_data()})
        if self.node_management_binding_request_call_elements is not None:
            msg_data.append({"nodeManagementBindingRequestCallElements": self.node_management_binding_request_call_elements.get_data()})
        if self.node_management_destination_data_elements is not None:
            msg_data.append({"nodeManagementDestinationDataElements": self.node_management_destination_data_elements.get_data()})
        if self.node_management_detailed_discovery_data_elements is not None:
            msg_data.append({"nodeManagementDetailedDiscoveryDataElements": self.node_management_detailed_discovery_data_elements.get_data()})
        if self.node_management_subscription_data_elements is not None:
            msg_data.append({"nodeManagementSubscriptionDataElements": self.node_management_subscription_data_elements.get_data()})
        if self.node_management_subscription_delete_call_elements is not None:
            msg_data.append({"nodeManagementSubscriptionDeleteCallElements": self.node_management_subscription_delete_call_elements.get_data()})
        if self.node_management_subscription_request_call_elements is not None:
            msg_data.append({"nodeManagementSubscriptionRequestCallElements": self.node_management_subscription_request_call_elements.get_data()})
        if self.node_management_use_case_data_elements is not None:
            msg_data.append({"nodeManagementUseCaseDataElements": self.node_management_use_case_data_elements.get_data()})
        if self.operating_constraints_duration_data_elements is not None:
            msg_data.append({"operatingConstraintsDurationDataElements": self.operating_constraints_duration_data_elements.get_data()})
        if self.operating_constraints_interrupt_data_elements is not None:
            msg_data.append({"operatingConstraintsInterruptDataElements": self.operating_constraints_interrupt_data_elements.get_data()})
        if self.operating_constraints_power_description_data_elements is not None:
            msg_data.append({"operatingConstraintsPowerDescriptionDataElements": self.operating_constraints_power_description_data_elements.get_data()})
        if self.operating_constraints_power_level_data_elements is not None:
            msg_data.append({"operatingConstraintsPowerLevelDataElements": self.operating_constraints_power_level_data_elements.get_data()})
        if self.operating_constraints_power_range_data_elements is not None:
            msg_data.append({"operatingConstraintsPowerRangeDataElements": self.operating_constraints_power_range_data_elements.get_data()})
        if self.operating_constraints_resume_implication_data_elements is not None:
            msg_data.append({"operatingConstraintsResumeImplicationDataElements": self.operating_constraints_resume_implication_data_elements.get_data()})
        if self.power_sequence_alternatives_relation_data_elements is not None:
            msg_data.append({"powerSequenceAlternativesRelationDataElements": self.power_sequence_alternatives_relation_data_elements.get_data()})
        if self.power_sequence_description_data_elements is not None:
            msg_data.append({"powerSequenceDescriptionDataElements": self.power_sequence_description_data_elements.get_data()})
        if self.power_sequence_node_schedule_information_data_elements is not None:
            msg_data.append({"powerSequenceNodeScheduleInformationDataElements": self.power_sequence_node_schedule_information_data_elements.get_data()})
        if self.power_sequence_price_calculation_request_call_elements is not None:
            msg_data.append({"powerSequencePriceCalculationRequestCallElements": self.power_sequence_price_calculation_request_call_elements.get_data()})
        if self.power_sequence_price_data_elements is not None:
            msg_data.append({"powerSequencePriceDataElements": self.power_sequence_price_data_elements.get_data()})
        if self.power_sequence_schedule_configuration_request_call_elements is not None:
            msg_data.append({"powerSequenceScheduleConfigurationRequestCallElements": self.power_sequence_schedule_configuration_request_call_elements.get_data()})
        if self.power_sequence_schedule_constraints_data_elements is not None:
            msg_data.append({"powerSequenceScheduleConstraintsDataElements": self.power_sequence_schedule_constraints_data_elements.get_data()})
        if self.power_sequence_schedule_data_elements is not None:
            msg_data.append({"powerSequenceScheduleDataElements": self.power_sequence_schedule_data_elements.get_data()})
        if self.power_sequence_schedule_preference_data_elements is not None:
            msg_data.append({"powerSequenceSchedulePreferenceDataElements": self.power_sequence_schedule_preference_data_elements.get_data()})
        if self.power_sequence_state_data_elements is not None:
            msg_data.append({"powerSequenceStateDataElements": self.power_sequence_state_data_elements.get_data()})
        if self.power_time_slot_schedule_constraints_data_elements is not None:
            msg_data.append({"powerTimeSlotScheduleConstraintsDataElements": self.power_time_slot_schedule_constraints_data_elements.get_data()})
        if self.power_time_slot_schedule_data_elements is not None:
            msg_data.append({"powerTimeSlotScheduleDataElements": self.power_time_slot_schedule_data_elements.get_data()})
        if self.power_time_slot_value_data_elements is not None:
            msg_data.append({"powerTimeSlotValueDataElements": self.power_time_slot_value_data_elements.get_data()})
        if self.sensing_data_elements is not None:
            msg_data.append({"sensingDataElements": self.sensing_data_elements.get_data()})
        if self.sensing_description_data_elements is not None:
            msg_data.append({"sensingDescriptionDataElements": self.sensing_description_data_elements.get_data()})
        if self.session_identification_data_elements is not None:
            msg_data.append({"sessionIdentificationDataElements": self.session_identification_data_elements.get_data()})
        if self.session_measurement_relation_data_elements is not None:
            msg_data.append({"sessionMeasurementRelationDataElements": self.session_measurement_relation_data_elements.get_data()})
        if self.setpoint_constraints_data_elements is not None:
            msg_data.append({"setpointConstraintsDataElements": self.setpoint_constraints_data_elements.get_data()})
        if self.setpoint_data_elements is not None:
            msg_data.append({"setpointDataElements": self.setpoint_data_elements.get_data()})
        if self.setpoint_description_data_elements is not None:
            msg_data.append({"setpointDescriptionDataElements": self.setpoint_description_data_elements.get_data()})
        if self.smart_energy_management_ps_configuration_request_call_elements is not None:
            msg_data.append({"smartEnergyManagementPsConfigurationRequestCallElements": self.smart_energy_management_ps_configuration_request_call_elements.get_data()})
        if self.smart_energy_management_ps_data_elements is not None:
            msg_data.append({"smartEnergyManagementPsDataElements": self.smart_energy_management_ps_data_elements.get_data()})
        if self.smart_energy_management_ps_price_calculation_request_call_elements is not None:
            msg_data.append({"smartEnergyManagementPsPriceCalculationRequestCallElements": self.smart_energy_management_ps_price_calculation_request_call_elements.get_data()})
        if self.smart_energy_management_ps_price_data_elements is not None:
            msg_data.append({"smartEnergyManagementPsPriceDataElements": self.smart_energy_management_ps_price_data_elements.get_data()})
        if self.specification_version_data_elements is not None:
            msg_data.append({"specificationVersionDataElements": self.specification_version_data_elements.get_data()})
        if self.state_information_data_elements is not None:
            msg_data.append({"stateInformationDataElements": self.state_information_data_elements.get_data()})
        if self.subscription_management_delete_call_elements is not None:
            msg_data.append({"subscriptionManagementDeleteCallElements": self.subscription_management_delete_call_elements.get_data()})
        if self.subscription_management_entry_data_elements is not None:
            msg_data.append({"subscriptionManagementEntryDataElements": self.subscription_management_entry_data_elements.get_data()})
        if self.subscription_management_request_call_elements is not None:
            msg_data.append({"subscriptionManagementRequestCallElements": self.subscription_management_request_call_elements.get_data()})
        if self.supply_condition_data_elements is not None:
            msg_data.append({"supplyConditionDataElements": self.supply_condition_data_elements.get_data()})
        if self.supply_condition_description_data_elements is not None:
            msg_data.append({"supplyConditionDescriptionDataElements": self.supply_condition_description_data_elements.get_data()})
        if self.supply_condition_threshold_relation_data_elements is not None:
            msg_data.append({"supplyConditionThresholdRelationDataElements": self.supply_condition_threshold_relation_data_elements.get_data()})
        if self.tariff_boundary_relation_data_elements is not None:
            msg_data.append({"tariffBoundaryRelationDataElements": self.tariff_boundary_relation_data_elements.get_data()})
        if self.tariff_data_elements is not None:
            msg_data.append({"tariffDataElements": self.tariff_data_elements.get_data()})
        if self.tariff_description_data_elements is not None:
            msg_data.append({"tariffDescriptionDataElements": self.tariff_description_data_elements.get_data()})
        if self.tariff_overall_constraints_data_elements is not None:
            msg_data.append({"tariffOverallConstraintsDataElements": self.tariff_overall_constraints_data_elements.get_data()})
        if self.tariff_tier_relation_data_elements is not None:
            msg_data.append({"tariffTierRelationDataElements": self.tariff_tier_relation_data_elements.get_data()})
        if self.task_management_job_data_elements is not None:
            msg_data.append({"taskManagementJobDataElements": self.task_management_job_data_elements.get_data()})
        if self.task_management_job_description_data_elements is not None:
            msg_data.append({"taskManagementJobDescriptionDataElements": self.task_management_job_description_data_elements.get_data()})
        if self.task_management_job_relation_data_elements is not None:
            msg_data.append({"taskManagementJobRelationDataElements": self.task_management_job_relation_data_elements.get_data()})
        if self.task_management_overview_data_elements is not None:
            msg_data.append({"taskManagementOverviewDataElements": self.task_management_overview_data_elements.get_data()})
        if self.threshold_constraints_data_elements is not None:
            msg_data.append({"thresholdConstraintsDataElements": self.threshold_constraints_data_elements.get_data()})
        if self.threshold_data_elements is not None:
            msg_data.append({"thresholdDataElements": self.threshold_data_elements.get_data()})
        if self.threshold_description_data_elements is not None:
            msg_data.append({"thresholdDescriptionDataElements": self.threshold_description_data_elements.get_data()})
        if self.tier_boundary_data_elements is not None:
            msg_data.append({"tierBoundaryDataElements": self.tier_boundary_data_elements.get_data()})
        if self.tier_boundary_description_data_elements is not None:
            msg_data.append({"tierBoundaryDescriptionDataElements": self.tier_boundary_description_data_elements.get_data()})
        if self.tier_data_elements is not None:
            msg_data.append({"tierDataElements": self.tier_data_elements.get_data()})
        if self.tier_description_data_elements is not None:
            msg_data.append({"tierDescriptionDataElements": self.tier_description_data_elements.get_data()})
        if self.tier_incentive_relation_data_elements is not None:
            msg_data.append({"tierIncentiveRelationDataElements": self.tier_incentive_relation_data_elements.get_data()})
        if self.time_distributor_data_elements is not None:
            msg_data.append({"timeDistributorDataElements": self.time_distributor_data_elements.get_data()})
        if self.time_distributor_enquiry_call_elements is not None:
            msg_data.append({"timeDistributorEnquiryCallElements": self.time_distributor_enquiry_call_elements.get_data()})
        if self.time_information_data_elements is not None:
            msg_data.append({"timeInformationDataElements": self.time_information_data_elements.get_data()})
        if self.time_precision_data_elements is not None:
            msg_data.append({"timePrecisionDataElements": self.time_precision_data_elements.get_data()})
        if self.time_series_constraints_data_elements is not None:
            msg_data.append({"timeSeriesConstraintsDataElements": self.time_series_constraints_data_elements.get_data()})
        if self.time_series_data_elements is not None:
            msg_data.append({"timeSeriesDataElements": self.time_series_data_elements.get_data()})
        if self.time_series_description_data_elements is not None:
            msg_data.append({"timeSeriesDescriptionDataElements": self.time_series_description_data_elements.get_data()})
        if self.time_table_constraints_data_elements is not None:
            msg_data.append({"timeTableConstraintsDataElements": self.time_table_constraints_data_elements.get_data()})
        if self.time_table_data_elements is not None:
            msg_data.append({"timeTableDataElements": self.time_table_data_elements.get_data()})
        if self.time_table_description_data_elements is not None:
            msg_data.append({"timeTableDescriptionDataElements": self.time_table_description_data_elements.get_data()})
        if self.use_case_information_data_elements is not None:
            msg_data.append({"useCaseInformationDataElements": self.use_case_information_data_elements.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.actuator_level_data_elements is not None:
            result_str += f"{sep}actuatorLevelDataElements: {self.actuator_level_data_elements}"
            sep = ", "
        if self.actuator_level_description_data_elements is not None:
            result_str += f"{sep}actuatorLevelDescriptionDataElements: {self.actuator_level_description_data_elements}"
            sep = ", "
        if self.actuator_switch_data_elements is not None:
            result_str += f"{sep}actuatorSwitchDataElements: {self.actuator_switch_data_elements}"
            sep = ", "
        if self.actuator_switch_description_data_elements is not None:
            result_str += f"{sep}actuatorSwitchDescriptionDataElements: {self.actuator_switch_description_data_elements}"
            sep = ", "
        if self.alarm_data_elements is not None:
            result_str += f"{sep}alarmDataElements: {self.alarm_data_elements}"
            sep = ", "
        if self.bill_constraints_data_elements is not None:
            result_str += f"{sep}billConstraintsDataElements: {self.bill_constraints_data_elements}"
            sep = ", "
        if self.bill_data_elements is not None:
            result_str += f"{sep}billDataElements: {self.bill_data_elements}"
            sep = ", "
        if self.bill_description_data_elements is not None:
            result_str += f"{sep}billDescriptionDataElements: {self.bill_description_data_elements}"
            sep = ", "
        if self.binding_management_delete_call_elements is not None:
            result_str += f"{sep}bindingManagementDeleteCallElements: {self.binding_management_delete_call_elements}"
            sep = ", "
        if self.binding_management_entry_data_elements is not None:
            result_str += f"{sep}bindingManagementEntryDataElements: {self.binding_management_entry_data_elements}"
            sep = ", "
        if self.binding_management_request_call_elements is not None:
            result_str += f"{sep}bindingManagementRequestCallElements: {self.binding_management_request_call_elements}"
            sep = ", "
        if self.commodity_data_elements is not None:
            result_str += f"{sep}commodityDataElements: {self.commodity_data_elements}"
            sep = ", "
        if self.data_tunneling_call_elements is not None:
            result_str += f"{sep}dataTunnelingCallElements: {self.data_tunneling_call_elements}"
            sep = ", "
        if self.device_classification_manufacturer_data_elements is not None:
            result_str += f"{sep}deviceClassificationManufacturerDataElements: {self.device_classification_manufacturer_data_elements}"
            sep = ", "
        if self.device_classification_user_data_elements is not None:
            result_str += f"{sep}deviceClassificationUserDataElements: {self.device_classification_user_data_elements}"
            sep = ", "
        if self.device_configuration_key_value_constraints_data_elements is not None:
            result_str += f"{sep}deviceConfigurationKeyValueConstraintsDataElements: {self.device_configuration_key_value_constraints_data_elements}"
            sep = ", "
        if self.device_configuration_key_value_data_elements is not None:
            result_str += f"{sep}deviceConfigurationKeyValueDataElements: {self.device_configuration_key_value_data_elements}"
            sep = ", "
        if self.device_configuration_key_value_description_data_elements is not None:
            result_str += f"{sep}deviceConfigurationKeyValueDescriptionDataElements: {self.device_configuration_key_value_description_data_elements}"
            sep = ", "
        if self.device_diagnosis_heartbeat_data_elements is not None:
            result_str += f"{sep}deviceDiagnosisHeartbeatDataElements: {self.device_diagnosis_heartbeat_data_elements}"
            sep = ", "
        if self.device_diagnosis_service_data_elements is not None:
            result_str += f"{sep}deviceDiagnosisServiceDataElements: {self.device_diagnosis_service_data_elements}"
            sep = ", "
        if self.device_diagnosis_state_data_elements is not None:
            result_str += f"{sep}deviceDiagnosisStateDataElements: {self.device_diagnosis_state_data_elements}"
            sep = ", "
        if self.direct_control_activity_data_elements is not None:
            result_str += f"{sep}directControlActivityDataElements: {self.direct_control_activity_data_elements}"
            sep = ", "
        if self.direct_control_description_data_elements is not None:
            result_str += f"{sep}directControlDescriptionDataElements: {self.direct_control_description_data_elements}"
            sep = ", "
        if self.electrical_connection_characteristic_data_elements is not None:
            result_str += f"{sep}electricalConnectionCharacteristicDataElements: {self.electrical_connection_characteristic_data_elements}"
            sep = ", "
        if self.electrical_connection_description_data_elements is not None:
            result_str += f"{sep}electricalConnectionDescriptionDataElements: {self.electrical_connection_description_data_elements}"
            sep = ", "
        if self.electrical_connection_parameter_description_data_elements is not None:
            result_str += f"{sep}electricalConnectionParameterDescriptionDataElements: {self.electrical_connection_parameter_description_data_elements}"
            sep = ", "
        if self.electrical_connection_permitted_value_set_data_elements is not None:
            result_str += f"{sep}electricalConnectionPermittedValueSetDataElements: {self.electrical_connection_permitted_value_set_data_elements}"
            sep = ", "
        if self.electrical_connection_state_data_elements is not None:
            result_str += f"{sep}electricalConnectionStateDataElements: {self.electrical_connection_state_data_elements}"
            sep = ", "
        if self.hvac_operation_mode_description_data_elements is not None:
            result_str += f"{sep}hvacOperationModeDescriptionDataElements: {self.hvac_operation_mode_description_data_elements}"
            sep = ", "
        if self.hvac_overrun_data_elements is not None:
            result_str += f"{sep}hvacOverrunDataElements: {self.hvac_overrun_data_elements}"
            sep = ", "
        if self.hvac_overrun_description_data_elements is not None:
            result_str += f"{sep}hvacOverrunDescriptionDataElements: {self.hvac_overrun_description_data_elements}"
            sep = ", "
        if self.hvac_system_function_data_elements is not None:
            result_str += f"{sep}hvacSystemFunctionDataElements: {self.hvac_system_function_data_elements}"
            sep = ", "
        if self.hvac_system_function_description_data_elements is not None:
            result_str += f"{sep}hvacSystemFunctionDescriptionDataElements: {self.hvac_system_function_description_data_elements}"
            sep = ", "
        if self.hvac_system_function_operation_mode_relation_data_elements is not None:
            result_str += f"{sep}hvacSystemFunctionOperationModeRelationDataElements: {self.hvac_system_function_operation_mode_relation_data_elements}"
            sep = ", "
        if self.hvac_system_function_power_sequence_relation_data_elements is not None:
            result_str += f"{sep}hvacSystemFunctionPowerSequenceRelationDataElements: {self.hvac_system_function_power_sequence_relation_data_elements}"
            sep = ", "
        if self.hvac_system_function_setpoint_relation_data_elements is not None:
            result_str += f"{sep}hvacSystemFunctionSetpointRelationDataElements: {self.hvac_system_function_setpoint_relation_data_elements}"
            sep = ", "
        if self.identification_data_elements is not None:
            result_str += f"{sep}identificationDataElements: {self.identification_data_elements}"
            sep = ", "
        if self.incentive_data_elements is not None:
            result_str += f"{sep}incentiveDataElements: {self.incentive_data_elements}"
            sep = ", "
        if self.incentive_description_data_elements is not None:
            result_str += f"{sep}incentiveDescriptionDataElements: {self.incentive_description_data_elements}"
            sep = ", "
        if self.incentive_table_constraints_data_elements is not None:
            result_str += f"{sep}incentiveTableConstraintsDataElements: {self.incentive_table_constraints_data_elements}"
            sep = ", "
        if self.incentive_table_data_elements is not None:
            result_str += f"{sep}incentiveTableDataElements: {self.incentive_table_data_elements}"
            sep = ", "
        if self.incentive_table_description_data_elements is not None:
            result_str += f"{sep}incentiveTableDescriptionDataElements: {self.incentive_table_description_data_elements}"
            sep = ", "
        if self.load_control_event_data_elements is not None:
            result_str += f"{sep}loadControlEventDataElements: {self.load_control_event_data_elements}"
            sep = ", "
        if self.load_control_limit_constraints_data_elements is not None:
            result_str += f"{sep}loadControlLimitConstraintsDataElements: {self.load_control_limit_constraints_data_elements}"
            sep = ", "
        if self.load_control_limit_data_elements is not None:
            result_str += f"{sep}loadControlLimitDataElements: {self.load_control_limit_data_elements}"
            sep = ", "
        if self.load_control_limit_description_data_elements is not None:
            result_str += f"{sep}loadControlLimitDescriptionDataElements: {self.load_control_limit_description_data_elements}"
            sep = ", "
        if self.load_control_node_data_elements is not None:
            result_str += f"{sep}loadControlNodeDataElements: {self.load_control_node_data_elements}"
            sep = ", "
        if self.load_control_state_data_elements is not None:
            result_str += f"{sep}loadControlStateDataElements: {self.load_control_state_data_elements}"
            sep = ", "
        if self.measurement_constraints_data_elements is not None:
            result_str += f"{sep}measurementConstraintsDataElements: {self.measurement_constraints_data_elements}"
            sep = ", "
        if self.measurement_data_elements is not None:
            result_str += f"{sep}measurementDataElements: {self.measurement_data_elements}"
            sep = ", "
        if self.measurement_description_data_elements is not None:
            result_str += f"{sep}measurementDescriptionDataElements: {self.measurement_description_data_elements}"
            sep = ", "
        if self.measurement_series_data_elements is not None:
            result_str += f"{sep}measurementSeriesDataElements: {self.measurement_series_data_elements}"
            sep = ", "
        if self.measurement_threshold_relation_data_elements is not None:
            result_str += f"{sep}measurementThresholdRelationDataElements: {self.measurement_threshold_relation_data_elements}"
            sep = ", "
        if self.messaging_data_elements is not None:
            result_str += f"{sep}messagingDataElements: {self.messaging_data_elements}"
            sep = ", "
        if self.network_management_abort_call_elements is not None:
            result_str += f"{sep}networkManagementAbortCallElements: {self.network_management_abort_call_elements}"
            sep = ", "
        if self.network_management_add_node_call_elements is not None:
            result_str += f"{sep}networkManagementAddNodeCallElements: {self.network_management_add_node_call_elements}"
            sep = ", "
        if self.network_management_device_description_data_elements is not None:
            result_str += f"{sep}networkManagementDeviceDescriptionDataElements: {self.network_management_device_description_data_elements}"
            sep = ", "
        if self.network_management_discover_call_elements is not None:
            result_str += f"{sep}networkManagementDiscoverCallElements: {self.network_management_discover_call_elements}"
            sep = ", "
        if self.network_management_entity_description_data_elements is not None:
            result_str += f"{sep}networkManagementEntityDescriptionDataElements: {self.network_management_entity_description_data_elements}"
            sep = ", "
        if self.network_management_feature_description_data_elements is not None:
            result_str += f"{sep}networkManagementFeatureDescriptionDataElements: {self.network_management_feature_description_data_elements}"
            sep = ", "
        if self.network_management_joining_mode_data_elements is not None:
            result_str += f"{sep}networkManagementJoiningModeDataElements: {self.network_management_joining_mode_data_elements}"
            sep = ", "
        if self.network_management_modify_node_call_elements is not None:
            result_str += f"{sep}networkManagementModifyNodeCallElements: {self.network_management_modify_node_call_elements}"
            sep = ", "
        if self.network_management_process_state_data_elements is not None:
            result_str += f"{sep}networkManagementProcessStateDataElements: {self.network_management_process_state_data_elements}"
            sep = ", "
        if self.network_management_remove_node_call_elements is not None:
            result_str += f"{sep}networkManagementRemoveNodeCallElements: {self.network_management_remove_node_call_elements}"
            sep = ", "
        if self.network_management_report_candidate_data_elements is not None:
            result_str += f"{sep}networkManagementReportCandidateDataElements: {self.network_management_report_candidate_data_elements}"
            sep = ", "
        if self.network_management_scan_network_call_elements is not None:
            result_str += f"{sep}networkManagementScanNetworkCallElements: {self.network_management_scan_network_call_elements}"
            sep = ", "
        if self.node_management_binding_data_elements is not None:
            result_str += f"{sep}nodeManagementBindingDataElements: {self.node_management_binding_data_elements}"
            sep = ", "
        if self.node_management_binding_delete_call_elements is not None:
            result_str += f"{sep}nodeManagementBindingDeleteCallElements: {self.node_management_binding_delete_call_elements}"
            sep = ", "
        if self.node_management_binding_request_call_elements is not None:
            result_str += f"{sep}nodeManagementBindingRequestCallElements: {self.node_management_binding_request_call_elements}"
            sep = ", "
        if self.node_management_destination_data_elements is not None:
            result_str += f"{sep}nodeManagementDestinationDataElements: {self.node_management_destination_data_elements}"
            sep = ", "
        if self.node_management_detailed_discovery_data_elements is not None:
            result_str += f"{sep}nodeManagementDetailedDiscoveryDataElements: {self.node_management_detailed_discovery_data_elements}"
            sep = ", "
        if self.node_management_subscription_data_elements is not None:
            result_str += f"{sep}nodeManagementSubscriptionDataElements: {self.node_management_subscription_data_elements}"
            sep = ", "
        if self.node_management_subscription_delete_call_elements is not None:
            result_str += f"{sep}nodeManagementSubscriptionDeleteCallElements: {self.node_management_subscription_delete_call_elements}"
            sep = ", "
        if self.node_management_subscription_request_call_elements is not None:
            result_str += f"{sep}nodeManagementSubscriptionRequestCallElements: {self.node_management_subscription_request_call_elements}"
            sep = ", "
        if self.node_management_use_case_data_elements is not None:
            result_str += f"{sep}nodeManagementUseCaseDataElements: {self.node_management_use_case_data_elements}"
            sep = ", "
        if self.operating_constraints_duration_data_elements is not None:
            result_str += f"{sep}operatingConstraintsDurationDataElements: {self.operating_constraints_duration_data_elements}"
            sep = ", "
        if self.operating_constraints_interrupt_data_elements is not None:
            result_str += f"{sep}operatingConstraintsInterruptDataElements: {self.operating_constraints_interrupt_data_elements}"
            sep = ", "
        if self.operating_constraints_power_description_data_elements is not None:
            result_str += f"{sep}operatingConstraintsPowerDescriptionDataElements: {self.operating_constraints_power_description_data_elements}"
            sep = ", "
        if self.operating_constraints_power_level_data_elements is not None:
            result_str += f"{sep}operatingConstraintsPowerLevelDataElements: {self.operating_constraints_power_level_data_elements}"
            sep = ", "
        if self.operating_constraints_power_range_data_elements is not None:
            result_str += f"{sep}operatingConstraintsPowerRangeDataElements: {self.operating_constraints_power_range_data_elements}"
            sep = ", "
        if self.operating_constraints_resume_implication_data_elements is not None:
            result_str += f"{sep}operatingConstraintsResumeImplicationDataElements: {self.operating_constraints_resume_implication_data_elements}"
            sep = ", "
        if self.power_sequence_alternatives_relation_data_elements is not None:
            result_str += f"{sep}powerSequenceAlternativesRelationDataElements: {self.power_sequence_alternatives_relation_data_elements}"
            sep = ", "
        if self.power_sequence_description_data_elements is not None:
            result_str += f"{sep}powerSequenceDescriptionDataElements: {self.power_sequence_description_data_elements}"
            sep = ", "
        if self.power_sequence_node_schedule_information_data_elements is not None:
            result_str += f"{sep}powerSequenceNodeScheduleInformationDataElements: {self.power_sequence_node_schedule_information_data_elements}"
            sep = ", "
        if self.power_sequence_price_calculation_request_call_elements is not None:
            result_str += f"{sep}powerSequencePriceCalculationRequestCallElements: {self.power_sequence_price_calculation_request_call_elements}"
            sep = ", "
        if self.power_sequence_price_data_elements is not None:
            result_str += f"{sep}powerSequencePriceDataElements: {self.power_sequence_price_data_elements}"
            sep = ", "
        if self.power_sequence_schedule_configuration_request_call_elements is not None:
            result_str += f"{sep}powerSequenceScheduleConfigurationRequestCallElements: {self.power_sequence_schedule_configuration_request_call_elements}"
            sep = ", "
        if self.power_sequence_schedule_constraints_data_elements is not None:
            result_str += f"{sep}powerSequenceScheduleConstraintsDataElements: {self.power_sequence_schedule_constraints_data_elements}"
            sep = ", "
        if self.power_sequence_schedule_data_elements is not None:
            result_str += f"{sep}powerSequenceScheduleDataElements: {self.power_sequence_schedule_data_elements}"
            sep = ", "
        if self.power_sequence_schedule_preference_data_elements is not None:
            result_str += f"{sep}powerSequenceSchedulePreferenceDataElements: {self.power_sequence_schedule_preference_data_elements}"
            sep = ", "
        if self.power_sequence_state_data_elements is not None:
            result_str += f"{sep}powerSequenceStateDataElements: {self.power_sequence_state_data_elements}"
            sep = ", "
        if self.power_time_slot_schedule_constraints_data_elements is not None:
            result_str += f"{sep}powerTimeSlotScheduleConstraintsDataElements: {self.power_time_slot_schedule_constraints_data_elements}"
            sep = ", "
        if self.power_time_slot_schedule_data_elements is not None:
            result_str += f"{sep}powerTimeSlotScheduleDataElements: {self.power_time_slot_schedule_data_elements}"
            sep = ", "
        if self.power_time_slot_value_data_elements is not None:
            result_str += f"{sep}powerTimeSlotValueDataElements: {self.power_time_slot_value_data_elements}"
            sep = ", "
        if self.sensing_data_elements is not None:
            result_str += f"{sep}sensingDataElements: {self.sensing_data_elements}"
            sep = ", "
        if self.sensing_description_data_elements is not None:
            result_str += f"{sep}sensingDescriptionDataElements: {self.sensing_description_data_elements}"
            sep = ", "
        if self.session_identification_data_elements is not None:
            result_str += f"{sep}sessionIdentificationDataElements: {self.session_identification_data_elements}"
            sep = ", "
        if self.session_measurement_relation_data_elements is not None:
            result_str += f"{sep}sessionMeasurementRelationDataElements: {self.session_measurement_relation_data_elements}"
            sep = ", "
        if self.setpoint_constraints_data_elements is not None:
            result_str += f"{sep}setpointConstraintsDataElements: {self.setpoint_constraints_data_elements}"
            sep = ", "
        if self.setpoint_data_elements is not None:
            result_str += f"{sep}setpointDataElements: {self.setpoint_data_elements}"
            sep = ", "
        if self.setpoint_description_data_elements is not None:
            result_str += f"{sep}setpointDescriptionDataElements: {self.setpoint_description_data_elements}"
            sep = ", "
        if self.smart_energy_management_ps_configuration_request_call_elements is not None:
            result_str += f"{sep}smartEnergyManagementPsConfigurationRequestCallElements: {self.smart_energy_management_ps_configuration_request_call_elements}"
            sep = ", "
        if self.smart_energy_management_ps_data_elements is not None:
            result_str += f"{sep}smartEnergyManagementPsDataElements: {self.smart_energy_management_ps_data_elements}"
            sep = ", "
        if self.smart_energy_management_ps_price_calculation_request_call_elements is not None:
            result_str += f"{sep}smartEnergyManagementPsPriceCalculationRequestCallElements: {self.smart_energy_management_ps_price_calculation_request_call_elements}"
            sep = ", "
        if self.smart_energy_management_ps_price_data_elements is not None:
            result_str += f"{sep}smartEnergyManagementPsPriceDataElements: {self.smart_energy_management_ps_price_data_elements}"
            sep = ", "
        if self.specification_version_data_elements is not None:
            result_str += f"{sep}specificationVersionDataElements: {self.specification_version_data_elements}"
            sep = ", "
        if self.state_information_data_elements is not None:
            result_str += f"{sep}stateInformationDataElements: {self.state_information_data_elements}"
            sep = ", "
        if self.subscription_management_delete_call_elements is not None:
            result_str += f"{sep}subscriptionManagementDeleteCallElements: {self.subscription_management_delete_call_elements}"
            sep = ", "
        if self.subscription_management_entry_data_elements is not None:
            result_str += f"{sep}subscriptionManagementEntryDataElements: {self.subscription_management_entry_data_elements}"
            sep = ", "
        if self.subscription_management_request_call_elements is not None:
            result_str += f"{sep}subscriptionManagementRequestCallElements: {self.subscription_management_request_call_elements}"
            sep = ", "
        if self.supply_condition_data_elements is not None:
            result_str += f"{sep}supplyConditionDataElements: {self.supply_condition_data_elements}"
            sep = ", "
        if self.supply_condition_description_data_elements is not None:
            result_str += f"{sep}supplyConditionDescriptionDataElements: {self.supply_condition_description_data_elements}"
            sep = ", "
        if self.supply_condition_threshold_relation_data_elements is not None:
            result_str += f"{sep}supplyConditionThresholdRelationDataElements: {self.supply_condition_threshold_relation_data_elements}"
            sep = ", "
        if self.tariff_boundary_relation_data_elements is not None:
            result_str += f"{sep}tariffBoundaryRelationDataElements: {self.tariff_boundary_relation_data_elements}"
            sep = ", "
        if self.tariff_data_elements is not None:
            result_str += f"{sep}tariffDataElements: {self.tariff_data_elements}"
            sep = ", "
        if self.tariff_description_data_elements is not None:
            result_str += f"{sep}tariffDescriptionDataElements: {self.tariff_description_data_elements}"
            sep = ", "
        if self.tariff_overall_constraints_data_elements is not None:
            result_str += f"{sep}tariffOverallConstraintsDataElements: {self.tariff_overall_constraints_data_elements}"
            sep = ", "
        if self.tariff_tier_relation_data_elements is not None:
            result_str += f"{sep}tariffTierRelationDataElements: {self.tariff_tier_relation_data_elements}"
            sep = ", "
        if self.task_management_job_data_elements is not None:
            result_str += f"{sep}taskManagementJobDataElements: {self.task_management_job_data_elements}"
            sep = ", "
        if self.task_management_job_description_data_elements is not None:
            result_str += f"{sep}taskManagementJobDescriptionDataElements: {self.task_management_job_description_data_elements}"
            sep = ", "
        if self.task_management_job_relation_data_elements is not None:
            result_str += f"{sep}taskManagementJobRelationDataElements: {self.task_management_job_relation_data_elements}"
            sep = ", "
        if self.task_management_overview_data_elements is not None:
            result_str += f"{sep}taskManagementOverviewDataElements: {self.task_management_overview_data_elements}"
            sep = ", "
        if self.threshold_constraints_data_elements is not None:
            result_str += f"{sep}thresholdConstraintsDataElements: {self.threshold_constraints_data_elements}"
            sep = ", "
        if self.threshold_data_elements is not None:
            result_str += f"{sep}thresholdDataElements: {self.threshold_data_elements}"
            sep = ", "
        if self.threshold_description_data_elements is not None:
            result_str += f"{sep}thresholdDescriptionDataElements: {self.threshold_description_data_elements}"
            sep = ", "
        if self.tier_boundary_data_elements is not None:
            result_str += f"{sep}tierBoundaryDataElements: {self.tier_boundary_data_elements}"
            sep = ", "
        if self.tier_boundary_description_data_elements is not None:
            result_str += f"{sep}tierBoundaryDescriptionDataElements: {self.tier_boundary_description_data_elements}"
            sep = ", "
        if self.tier_data_elements is not None:
            result_str += f"{sep}tierDataElements: {self.tier_data_elements}"
            sep = ", "
        if self.tier_description_data_elements is not None:
            result_str += f"{sep}tierDescriptionDataElements: {self.tier_description_data_elements}"
            sep = ", "
        if self.tier_incentive_relation_data_elements is not None:
            result_str += f"{sep}tierIncentiveRelationDataElements: {self.tier_incentive_relation_data_elements}"
            sep = ", "
        if self.time_distributor_data_elements is not None:
            result_str += f"{sep}timeDistributorDataElements: {self.time_distributor_data_elements}"
            sep = ", "
        if self.time_distributor_enquiry_call_elements is not None:
            result_str += f"{sep}timeDistributorEnquiryCallElements: {self.time_distributor_enquiry_call_elements}"
            sep = ", "
        if self.time_information_data_elements is not None:
            result_str += f"{sep}timeInformationDataElements: {self.time_information_data_elements}"
            sep = ", "
        if self.time_precision_data_elements is not None:
            result_str += f"{sep}timePrecisionDataElements: {self.time_precision_data_elements}"
            sep = ", "
        if self.time_series_constraints_data_elements is not None:
            result_str += f"{sep}timeSeriesConstraintsDataElements: {self.time_series_constraints_data_elements}"
            sep = ", "
        if self.time_series_data_elements is not None:
            result_str += f"{sep}timeSeriesDataElements: {self.time_series_data_elements}"
            sep = ", "
        if self.time_series_description_data_elements is not None:
            result_str += f"{sep}timeSeriesDescriptionDataElements: {self.time_series_description_data_elements}"
            sep = ", "
        if self.time_table_constraints_data_elements is not None:
            result_str += f"{sep}timeTableConstraintsDataElements: {self.time_table_constraints_data_elements}"
            sep = ", "
        if self.time_table_data_elements is not None:
            result_str += f"{sep}timeTableDataElements: {self.time_table_data_elements}"
            sep = ", "
        if self.time_table_description_data_elements is not None:
            result_str += f"{sep}timeTableDescriptionDataElements: {self.time_table_description_data_elements}"
            sep = ", "
        if self.use_case_information_data_elements is not None:
            result_str += f"{sep}useCaseInformationDataElements: {self.use_case_information_data_elements}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                actuator_level_data_elements=data_dict.get('actuatorLevelDataElements'),
                actuator_level_description_data_elements=data_dict.get('actuatorLevelDescriptionDataElements'),
                actuator_switch_data_elements=data_dict.get('actuatorSwitchDataElements'),
                actuator_switch_description_data_elements=data_dict.get('actuatorSwitchDescriptionDataElements'),
                alarm_data_elements=data_dict.get('alarmDataElements'),
                bill_constraints_data_elements=data_dict.get('billConstraintsDataElements'),
                bill_data_elements=data_dict.get('billDataElements'),
                bill_description_data_elements=data_dict.get('billDescriptionDataElements'),
                binding_management_delete_call_elements=data_dict.get('bindingManagementDeleteCallElements'),
                binding_management_entry_data_elements=data_dict.get('bindingManagementEntryDataElements'),
                binding_management_request_call_elements=data_dict.get('bindingManagementRequestCallElements'),
                commodity_data_elements=data_dict.get('commodityDataElements'),
                data_tunneling_call_elements=data_dict.get('dataTunnelingCallElements'),
                device_classification_manufacturer_data_elements=data_dict.get('deviceClassificationManufacturerDataElements'),
                device_classification_user_data_elements=data_dict.get('deviceClassificationUserDataElements'),
                device_configuration_key_value_constraints_data_elements=data_dict.get('deviceConfigurationKeyValueConstraintsDataElements'),
                device_configuration_key_value_data_elements=data_dict.get('deviceConfigurationKeyValueDataElements'),
                device_configuration_key_value_description_data_elements=data_dict.get('deviceConfigurationKeyValueDescriptionDataElements'),
                device_diagnosis_heartbeat_data_elements=data_dict.get('deviceDiagnosisHeartbeatDataElements'),
                device_diagnosis_service_data_elements=data_dict.get('deviceDiagnosisServiceDataElements'),
                device_diagnosis_state_data_elements=data_dict.get('deviceDiagnosisStateDataElements'),
                direct_control_activity_data_elements=data_dict.get('directControlActivityDataElements'),
                direct_control_description_data_elements=data_dict.get('directControlDescriptionDataElements'),
                electrical_connection_characteristic_data_elements=data_dict.get('electricalConnectionCharacteristicDataElements'),
                electrical_connection_description_data_elements=data_dict.get('electricalConnectionDescriptionDataElements'),
                electrical_connection_parameter_description_data_elements=data_dict.get('electricalConnectionParameterDescriptionDataElements'),
                electrical_connection_permitted_value_set_data_elements=data_dict.get('electricalConnectionPermittedValueSetDataElements'),
                electrical_connection_state_data_elements=data_dict.get('electricalConnectionStateDataElements'),
                hvac_operation_mode_description_data_elements=data_dict.get('hvacOperationModeDescriptionDataElements'),
                hvac_overrun_data_elements=data_dict.get('hvacOverrunDataElements'),
                hvac_overrun_description_data_elements=data_dict.get('hvacOverrunDescriptionDataElements'),
                hvac_system_function_data_elements=data_dict.get('hvacSystemFunctionDataElements'),
                hvac_system_function_description_data_elements=data_dict.get('hvacSystemFunctionDescriptionDataElements'),
                hvac_system_function_operation_mode_relation_data_elements=data_dict.get('hvacSystemFunctionOperationModeRelationDataElements'),
                hvac_system_function_power_sequence_relation_data_elements=data_dict.get('hvacSystemFunctionPowerSequenceRelationDataElements'),
                hvac_system_function_setpoint_relation_data_elements=data_dict.get('hvacSystemFunctionSetpointRelationDataElements'),
                identification_data_elements=data_dict.get('identificationDataElements'),
                incentive_data_elements=data_dict.get('incentiveDataElements'),
                incentive_description_data_elements=data_dict.get('incentiveDescriptionDataElements'),
                incentive_table_constraints_data_elements=data_dict.get('incentiveTableConstraintsDataElements'),
                incentive_table_data_elements=data_dict.get('incentiveTableDataElements'),
                incentive_table_description_data_elements=data_dict.get('incentiveTableDescriptionDataElements'),
                load_control_event_data_elements=data_dict.get('loadControlEventDataElements'),
                load_control_limit_constraints_data_elements=data_dict.get('loadControlLimitConstraintsDataElements'),
                load_control_limit_data_elements=data_dict.get('loadControlLimitDataElements'),
                load_control_limit_description_data_elements=data_dict.get('loadControlLimitDescriptionDataElements'),
                load_control_node_data_elements=data_dict.get('loadControlNodeDataElements'),
                load_control_state_data_elements=data_dict.get('loadControlStateDataElements'),
                measurement_constraints_data_elements=data_dict.get('measurementConstraintsDataElements'),
                measurement_data_elements=data_dict.get('measurementDataElements'),
                measurement_description_data_elements=data_dict.get('measurementDescriptionDataElements'),
                measurement_series_data_elements=data_dict.get('measurementSeriesDataElements'),
                measurement_threshold_relation_data_elements=data_dict.get('measurementThresholdRelationDataElements'),
                messaging_data_elements=data_dict.get('messagingDataElements'),
                network_management_abort_call_elements=data_dict.get('networkManagementAbortCallElements'),
                network_management_add_node_call_elements=data_dict.get('networkManagementAddNodeCallElements'),
                network_management_device_description_data_elements=data_dict.get('networkManagementDeviceDescriptionDataElements'),
                network_management_discover_call_elements=data_dict.get('networkManagementDiscoverCallElements'),
                network_management_entity_description_data_elements=data_dict.get('networkManagementEntityDescriptionDataElements'),
                network_management_feature_description_data_elements=data_dict.get('networkManagementFeatureDescriptionDataElements'),
                network_management_joining_mode_data_elements=data_dict.get('networkManagementJoiningModeDataElements'),
                network_management_modify_node_call_elements=data_dict.get('networkManagementModifyNodeCallElements'),
                network_management_process_state_data_elements=data_dict.get('networkManagementProcessStateDataElements'),
                network_management_remove_node_call_elements=data_dict.get('networkManagementRemoveNodeCallElements'),
                network_management_report_candidate_data_elements=data_dict.get('networkManagementReportCandidateDataElements'),
                network_management_scan_network_call_elements=data_dict.get('networkManagementScanNetworkCallElements'),
                node_management_binding_data_elements=data_dict.get('nodeManagementBindingDataElements'),
                node_management_binding_delete_call_elements=data_dict.get('nodeManagementBindingDeleteCallElements'),
                node_management_binding_request_call_elements=data_dict.get('nodeManagementBindingRequestCallElements'),
                node_management_destination_data_elements=data_dict.get('nodeManagementDestinationDataElements'),
                node_management_detailed_discovery_data_elements=data_dict.get('nodeManagementDetailedDiscoveryDataElements'),
                node_management_subscription_data_elements=data_dict.get('nodeManagementSubscriptionDataElements'),
                node_management_subscription_delete_call_elements=data_dict.get('nodeManagementSubscriptionDeleteCallElements'),
                node_management_subscription_request_call_elements=data_dict.get('nodeManagementSubscriptionRequestCallElements'),
                node_management_use_case_data_elements=data_dict.get('nodeManagementUseCaseDataElements'),
                operating_constraints_duration_data_elements=data_dict.get('operatingConstraintsDurationDataElements'),
                operating_constraints_interrupt_data_elements=data_dict.get('operatingConstraintsInterruptDataElements'),
                operating_constraints_power_description_data_elements=data_dict.get('operatingConstraintsPowerDescriptionDataElements'),
                operating_constraints_power_level_data_elements=data_dict.get('operatingConstraintsPowerLevelDataElements'),
                operating_constraints_power_range_data_elements=data_dict.get('operatingConstraintsPowerRangeDataElements'),
                operating_constraints_resume_implication_data_elements=data_dict.get('operatingConstraintsResumeImplicationDataElements'),
                power_sequence_alternatives_relation_data_elements=data_dict.get('powerSequenceAlternativesRelationDataElements'),
                power_sequence_description_data_elements=data_dict.get('powerSequenceDescriptionDataElements'),
                power_sequence_node_schedule_information_data_elements=data_dict.get('powerSequenceNodeScheduleInformationDataElements'),
                power_sequence_price_calculation_request_call_elements=data_dict.get('powerSequencePriceCalculationRequestCallElements'),
                power_sequence_price_data_elements=data_dict.get('powerSequencePriceDataElements'),
                power_sequence_schedule_configuration_request_call_elements=data_dict.get('powerSequenceScheduleConfigurationRequestCallElements'),
                power_sequence_schedule_constraints_data_elements=data_dict.get('powerSequenceScheduleConstraintsDataElements'),
                power_sequence_schedule_data_elements=data_dict.get('powerSequenceScheduleDataElements'),
                power_sequence_schedule_preference_data_elements=data_dict.get('powerSequenceSchedulePreferenceDataElements'),
                power_sequence_state_data_elements=data_dict.get('powerSequenceStateDataElements'),
                power_time_slot_schedule_constraints_data_elements=data_dict.get('powerTimeSlotScheduleConstraintsDataElements'),
                power_time_slot_schedule_data_elements=data_dict.get('powerTimeSlotScheduleDataElements'),
                power_time_slot_value_data_elements=data_dict.get('powerTimeSlotValueDataElements'),
                sensing_data_elements=data_dict.get('sensingDataElements'),
                sensing_description_data_elements=data_dict.get('sensingDescriptionDataElements'),
                session_identification_data_elements=data_dict.get('sessionIdentificationDataElements'),
                session_measurement_relation_data_elements=data_dict.get('sessionMeasurementRelationDataElements'),
                setpoint_constraints_data_elements=data_dict.get('setpointConstraintsDataElements'),
                setpoint_data_elements=data_dict.get('setpointDataElements'),
                setpoint_description_data_elements=data_dict.get('setpointDescriptionDataElements'),
                smart_energy_management_ps_configuration_request_call_elements=data_dict.get('smartEnergyManagementPsConfigurationRequestCallElements'),
                smart_energy_management_ps_data_elements=data_dict.get('smartEnergyManagementPsDataElements'),
                smart_energy_management_ps_price_calculation_request_call_elements=data_dict.get('smartEnergyManagementPsPriceCalculationRequestCallElements'),
                smart_energy_management_ps_price_data_elements=data_dict.get('smartEnergyManagementPsPriceDataElements'),
                specification_version_data_elements=data_dict.get('specificationVersionDataElements'),
                state_information_data_elements=data_dict.get('stateInformationDataElements'),
                subscription_management_delete_call_elements=data_dict.get('subscriptionManagementDeleteCallElements'),
                subscription_management_entry_data_elements=data_dict.get('subscriptionManagementEntryDataElements'),
                subscription_management_request_call_elements=data_dict.get('subscriptionManagementRequestCallElements'),
                supply_condition_data_elements=data_dict.get('supplyConditionDataElements'),
                supply_condition_description_data_elements=data_dict.get('supplyConditionDescriptionDataElements'),
                supply_condition_threshold_relation_data_elements=data_dict.get('supplyConditionThresholdRelationDataElements'),
                tariff_boundary_relation_data_elements=data_dict.get('tariffBoundaryRelationDataElements'),
                tariff_data_elements=data_dict.get('tariffDataElements'),
                tariff_description_data_elements=data_dict.get('tariffDescriptionDataElements'),
                tariff_overall_constraints_data_elements=data_dict.get('tariffOverallConstraintsDataElements'),
                tariff_tier_relation_data_elements=data_dict.get('tariffTierRelationDataElements'),
                task_management_job_data_elements=data_dict.get('taskManagementJobDataElements'),
                task_management_job_description_data_elements=data_dict.get('taskManagementJobDescriptionDataElements'),
                task_management_job_relation_data_elements=data_dict.get('taskManagementJobRelationDataElements'),
                task_management_overview_data_elements=data_dict.get('taskManagementOverviewDataElements'),
                threshold_constraints_data_elements=data_dict.get('thresholdConstraintsDataElements'),
                threshold_data_elements=data_dict.get('thresholdDataElements'),
                threshold_description_data_elements=data_dict.get('thresholdDescriptionDataElements'),
                tier_boundary_data_elements=data_dict.get('tierBoundaryDataElements'),
                tier_boundary_description_data_elements=data_dict.get('tierBoundaryDescriptionDataElements'),
                tier_data_elements=data_dict.get('tierDataElements'),
                tier_description_data_elements=data_dict.get('tierDescriptionDataElements'),
                tier_incentive_relation_data_elements=data_dict.get('tierIncentiveRelationDataElements'),
                time_distributor_data_elements=data_dict.get('timeDistributorDataElements'),
                time_distributor_enquiry_call_elements=data_dict.get('timeDistributorEnquiryCallElements'),
                time_information_data_elements=data_dict.get('timeInformationDataElements'),
                time_precision_data_elements=data_dict.get('timePrecisionDataElements'),
                time_series_constraints_data_elements=data_dict.get('timeSeriesConstraintsDataElements'),
                time_series_data_elements=data_dict.get('timeSeriesDataElements'),
                time_series_description_data_elements=data_dict.get('timeSeriesDescriptionDataElements'),
                time_table_constraints_data_elements=data_dict.get('timeTableConstraintsDataElements'),
                time_table_data_elements=data_dict.get('timeTableDataElements'),
                time_table_description_data_elements=data_dict.get('timeTableDescriptionDataElements'),
                use_case_information_data_elements=data_dict.get('useCaseInformationDataElements'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class DataChoiceGroup:
    def __init__(
            self,
    ):
        super().__init__()
        

    def get_data(self): # ChoiceType

        msg_data = []
        
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
            )
        elif data:
            return cls(data)
        else:
            return cls()


class CmdOptionGroup:
    def __init__(
            self,
    ):
        super().__init__()
        

    def get_data(self): # ChoiceType

        msg_data = []
        
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
            )
        elif data:
            return cls(data)
        else:
            return cls()



