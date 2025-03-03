# Jinja Template message_type.py.jinja2
from spine.base_type.commondatatypes import ElementTagType
from spine.simple_type.commondatatypes import DescriptionType
from spine.simple_type.commondatatypes import LabelType
from spine.simple_type.hvac import HvacOverrunIdType
from spine.simple_type.loadcontrol import LoadControlEventIdType
from spine.simple_type.powersequences import PowerSequenceIdType
from spine.simple_type.taskmanagement import TaskManagementJobIdType
from spine.union_type.commondatatypes import AbsoluteOrRelativeTimeType
from spine.union_type.taskmanagement import TaskManagementJobSourceType
from spine.union_type.taskmanagement import TaskManagementJobStateType
from types import NoneType
from spine import array_2_dict


class TaskManagementSmartEnergyManagementPsRelatedType: # EEBus_SPINE_TS_TaskManagement.xsd:ns_p:TaskManagementSmartEnergyManagementPsRelatedType -> ComplexType
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


class TaskManagementPowerSequencesRelatedType: # EEBus_SPINE_TS_TaskManagement.xsd:ns_p:TaskManagementPowerSequencesRelatedType -> ComplexType
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


class TaskManagementLoadControlReleatedType: # EEBus_SPINE_TS_TaskManagement.xsd:ns_p:TaskManagementLoadControlReleatedType -> ComplexType
    def __init__(
            self,
            event_id: LoadControlEventIdType = None,
    ):
        super().__init__()
        
        self.event_id = event_id

        if not isinstance(self.event_id, LoadControlEventIdType | NoneType):
            raise TypeError("event_id is not of type LoadControlEventIdType")
        
    def get_data(self):

        msg_data = []
        
        if self.event_id is not None:
            msg_data.append({"eventId": self.event_id.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.event_id is not None:
            result_str += f"{sep}eventId: {self.event_id}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                event_id=data_dict.get('eventId'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class TaskManagementHvacRelatedType: # EEBus_SPINE_TS_TaskManagement.xsd:ns_p:TaskManagementHvacRelatedType -> ComplexType
    def __init__(
            self,
            overrun_id: HvacOverrunIdType = None,
    ):
        super().__init__()
        
        self.overrun_id = overrun_id

        if not isinstance(self.overrun_id, HvacOverrunIdType | NoneType):
            raise TypeError("overrun_id is not of type HvacOverrunIdType")
        
    def get_data(self):

        msg_data = []
        
        if self.overrun_id is not None:
            msg_data.append({"overrunId": self.overrun_id.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.overrun_id is not None:
            result_str += f"{sep}overrunId: {self.overrun_id}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                overrun_id=data_dict.get('overrunId'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class TaskManagementDirectControlRelatedType: # EEBus_SPINE_TS_TaskManagement.xsd:ns_p:TaskManagementDirectControlRelatedType -> ComplexType
    def __init__(
            self,
    ):
        super().__init__()
        

    def get_data(self):

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


class TaskManagementJobRelationDataType: # EEBus_SPINE_TS_TaskManagement.xsd:ns_p:TaskManagementJobRelationDataType -> ComplexType
    def __init__(
            self,
            job_id: TaskManagementJobIdType = None,
            direct_control_related: TaskManagementDirectControlRelatedType = None,
            hvac_related: TaskManagementHvacRelatedType = None,
            load_control_releated: TaskManagementLoadControlReleatedType = None,
            power_sequences_related: TaskManagementPowerSequencesRelatedType = None,
            smart_energy_management_ps_related: TaskManagementSmartEnergyManagementPsRelatedType = None,
    ):
        super().__init__()
        
        self.job_id = job_id
        self.direct_control_related = direct_control_related
        self.hvac_related = hvac_related
        self.load_control_releated = load_control_releated
        self.power_sequences_related = power_sequences_related
        self.smart_energy_management_ps_related = smart_energy_management_ps_related

        if not isinstance(self.job_id, TaskManagementJobIdType | NoneType):
            raise TypeError("job_id is not of type TaskManagementJobIdType")
        
        if not isinstance(self.direct_control_related, TaskManagementDirectControlRelatedType | NoneType):
            raise TypeError("direct_control_related is not of type TaskManagementDirectControlRelatedType")
        
        if not isinstance(self.hvac_related, TaskManagementHvacRelatedType | NoneType):
            raise TypeError("hvac_related is not of type TaskManagementHvacRelatedType")
        
        if not isinstance(self.load_control_releated, TaskManagementLoadControlReleatedType | NoneType):
            raise TypeError("load_control_releated is not of type TaskManagementLoadControlReleatedType")
        
        if not isinstance(self.power_sequences_related, TaskManagementPowerSequencesRelatedType | NoneType):
            raise TypeError("power_sequences_related is not of type TaskManagementPowerSequencesRelatedType")
        
        if not isinstance(self.smart_energy_management_ps_related, TaskManagementSmartEnergyManagementPsRelatedType | NoneType):
            raise TypeError("smart_energy_management_ps_related is not of type TaskManagementSmartEnergyManagementPsRelatedType")
        
    def get_data(self):

        msg_data = []
        
        if self.job_id is not None:
            msg_data.append({"jobId": self.job_id.get_data()})
        if self.direct_control_related is not None:
            msg_data.append({"directControlRelated": self.direct_control_related.get_data()})
        if self.hvac_related is not None:
            msg_data.append({"hvacRelated": self.hvac_related.get_data()})
        if self.load_control_releated is not None:
            msg_data.append({"loadControlReleated": self.load_control_releated.get_data()})
        if self.power_sequences_related is not None:
            msg_data.append({"powerSequencesRelated": self.power_sequences_related.get_data()})
        if self.smart_energy_management_ps_related is not None:
            msg_data.append({"smartEnergyManagementPsRelated": self.smart_energy_management_ps_related.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.job_id is not None:
            result_str += f"{sep}jobId: {self.job_id}"
            sep = ", "
        if self.direct_control_related is not None:
            result_str += f"{sep}directControlRelated: {self.direct_control_related}"
            sep = ", "
        if self.hvac_related is not None:
            result_str += f"{sep}hvacRelated: {self.hvac_related}"
            sep = ", "
        if self.load_control_releated is not None:
            result_str += f"{sep}loadControlReleated: {self.load_control_releated}"
            sep = ", "
        if self.power_sequences_related is not None:
            result_str += f"{sep}powerSequencesRelated: {self.power_sequences_related}"
            sep = ", "
        if self.smart_energy_management_ps_related is not None:
            result_str += f"{sep}smartEnergyManagementPsRelated: {self.smart_energy_management_ps_related}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                job_id=data_dict.get('jobId'),
                direct_control_related=data_dict.get('directControlRelated'),
                hvac_related=data_dict.get('hvacRelated'),
                load_control_releated=data_dict.get('loadControlReleated'),
                power_sequences_related=data_dict.get('powerSequencesRelated'),
                smart_energy_management_ps_related=data_dict.get('smartEnergyManagementPsRelated'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class TaskManagementJobDataType: # EEBus_SPINE_TS_TaskManagement.xsd:ns_p:TaskManagementJobDataType -> ComplexType
    def __init__(
            self,
            job_id: TaskManagementJobIdType = None,
            timestamp: AbsoluteOrRelativeTimeType = None,
            job_state: TaskManagementJobStateType = None,
            elapsed_time: str = None,
            remaining_time: str = None,
    ):
        super().__init__()
        
        self.job_id = job_id
        self.timestamp = timestamp
        self.job_state = job_state
        self.elapsed_time = elapsed_time
        self.remaining_time = remaining_time

        if not isinstance(self.job_id, TaskManagementJobIdType | NoneType):
            raise TypeError("job_id is not of type TaskManagementJobIdType")
        
        if not isinstance(self.timestamp, AbsoluteOrRelativeTimeType | NoneType):
            raise TypeError("timestamp is not of type AbsoluteOrRelativeTimeType")
        
        if not isinstance(self.job_state, TaskManagementJobStateType | NoneType):
            raise TypeError("job_state is not of type TaskManagementJobStateType")
        
        if not isinstance(self.elapsed_time, str | NoneType):
            raise TypeError("elapsed_time is not of type str")
        
        if not isinstance(self.remaining_time, str | NoneType):
            raise TypeError("remaining_time is not of type str")
        
    def get_data(self):

        msg_data = []
        
        if self.job_id is not None:
            msg_data.append({"jobId": self.job_id.get_data()})
        if self.timestamp is not None:
            msg_data.append({"timestamp": self.timestamp.get_data()})
        if self.job_state is not None:
            msg_data.append({"jobState": self.job_state.get_data()})
        if self.elapsed_time is not None:
            msg_data.append({"elapsedTime": self.elapsed_time})
        if self.remaining_time is not None:
            msg_data.append({"remainingTime": self.remaining_time})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.job_id is not None:
            result_str += f"{sep}jobId: {self.job_id}"
            sep = ", "
        if self.timestamp is not None:
            result_str += f"{sep}timestamp: {self.timestamp}"
            sep = ", "
        if self.job_state is not None:
            result_str += f"{sep}jobState: {self.job_state}"
            sep = ", "
        if self.elapsed_time is not None:
            result_str += f"{sep}elapsedTime: {self.elapsed_time}"
            sep = ", "
        if self.remaining_time is not None:
            result_str += f"{sep}remainingTime: {self.remaining_time}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                job_id=data_dict.get('jobId'),
                timestamp=data_dict.get('timestamp'),
                job_state=data_dict.get('jobState'),
                elapsed_time=data_dict.get('elapsedTime'),
                remaining_time=data_dict.get('remainingTime'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class TaskManagementJobDescriptionDataType: # EEBus_SPINE_TS_TaskManagement.xsd:ns_p:TaskManagementJobDescriptionDataType -> ComplexType
    def __init__(
            self,
            job_id: TaskManagementJobIdType = None,
            job_source: TaskManagementJobSourceType = None,
            label: LabelType = None,
            description: DescriptionType = None,
    ):
        super().__init__()
        
        self.job_id = job_id
        self.job_source = job_source
        self.label = label
        self.description = description

        if not isinstance(self.job_id, TaskManagementJobIdType | NoneType):
            raise TypeError("job_id is not of type TaskManagementJobIdType")
        
        if not isinstance(self.job_source, TaskManagementJobSourceType | NoneType):
            raise TypeError("job_source is not of type TaskManagementJobSourceType")
        
        if not isinstance(self.label, LabelType | NoneType):
            raise TypeError("label is not of type LabelType")
        
        if not isinstance(self.description, DescriptionType | NoneType):
            raise TypeError("description is not of type DescriptionType")
        
    def get_data(self):

        msg_data = []
        
        if self.job_id is not None:
            msg_data.append({"jobId": self.job_id.get_data()})
        if self.job_source is not None:
            msg_data.append({"jobSource": self.job_source.get_data()})
        if self.label is not None:
            msg_data.append({"label": self.label.get_data()})
        if self.description is not None:
            msg_data.append({"description": self.description.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.job_id is not None:
            result_str += f"{sep}jobId: {self.job_id}"
            sep = ", "
        if self.job_source is not None:
            result_str += f"{sep}jobSource: {self.job_source}"
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
                job_id=data_dict.get('jobId'),
                job_source=data_dict.get('jobSource'),
                label=data_dict.get('label'),
                description=data_dict.get('description'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class TaskManagementSmartEnergyManagementPsRelatedElementsType: # EEBus_SPINE_TS_TaskManagement.xsd:ns_p:TaskManagementSmartEnergyManagementPsRelatedElementsType -> ComplexType
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


class TaskManagementPowerSequencesRelatedElementsType: # EEBus_SPINE_TS_TaskManagement.xsd:ns_p:TaskManagementPowerSequencesRelatedElementsType -> ComplexType
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


class TaskManagementLoadControlReleatedElementsType: # EEBus_SPINE_TS_TaskManagement.xsd:ns_p:TaskManagementLoadControlReleatedElementsType -> ComplexType
    def __init__(
            self,
            event_id: ElementTagType = None,
    ):
        super().__init__()
        
        self.event_id = event_id

        if not isinstance(self.event_id, ElementTagType | NoneType):
            raise TypeError("event_id is not of type ElementTagType")
        
    def get_data(self):

        msg_data = []
        
        if self.event_id is not None:
            msg_data.append({"eventId": self.event_id.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.event_id is not None:
            result_str += f"{sep}eventId: {self.event_id}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                event_id=data_dict.get('eventId'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class TaskManagementHvacRelatedElementsType: # EEBus_SPINE_TS_TaskManagement.xsd:ns_p:TaskManagementHvacRelatedElementsType -> ComplexType
    def __init__(
            self,
            overrun_id: ElementTagType = None,
    ):
        super().__init__()
        
        self.overrun_id = overrun_id

        if not isinstance(self.overrun_id, ElementTagType | NoneType):
            raise TypeError("overrun_id is not of type ElementTagType")
        
    def get_data(self):

        msg_data = []
        
        if self.overrun_id is not None:
            msg_data.append({"overrunId": self.overrun_id.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.overrun_id is not None:
            result_str += f"{sep}overrunId: {self.overrun_id}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                overrun_id=data_dict.get('overrunId'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class TaskManagementDirectControlRelatedElementsType: # EEBus_SPINE_TS_TaskManagement.xsd:ns_p:TaskManagementDirectControlRelatedElementsType -> ComplexType
    def __init__(
            self,
    ):
        super().__init__()
        

    def get_data(self):

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


class TaskManagementOverviewDataType: # EEBus_SPINE_TS_TaskManagement.xsd:ns_p:TaskManagementOverviewDataType -> ComplexType
    def __init__(
            self,
            remote_controllable: bool = None,
            jobs_active: bool = None,
    ):
        super().__init__()
        
        self.remote_controllable = remote_controllable
        self.jobs_active = jobs_active

        if not isinstance(self.remote_controllable, bool | NoneType):
            raise TypeError("remote_controllable is not of type bool")
        
        if not isinstance(self.jobs_active, bool | NoneType):
            raise TypeError("jobs_active is not of type bool")
        
    def get_data(self):

        msg_data = []
        
        if self.remote_controllable is not None:
            msg_data.append({"remoteControllable": self.remote_controllable})
        if self.jobs_active is not None:
            msg_data.append({"jobsActive": self.jobs_active})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.remote_controllable is not None:
            result_str += f"{sep}remoteControllable: {self.remote_controllable}"
            sep = ", "
        if self.jobs_active is not None:
            result_str += f"{sep}jobsActive: {self.jobs_active}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                remote_controllable=data_dict.get('remoteControllable'),
                jobs_active=data_dict.get('jobsActive'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class TaskManagementJobRelationListDataType: # EEBus_SPINE_TS_TaskManagement.xsd:ns_p:TaskManagementJobRelationListDataType -> ComplexType
    def __init__(
            self,
            task_management_job_relation_data: list[TaskManagementJobRelationDataType] = None,
    ):
        super().__init__()
        
        self.task_management_job_relation_data = task_management_job_relation_data

        if not isinstance(self.task_management_job_relation_data, list | NoneType):
            raise TypeError("task_management_job_relation_data is not of type list[TaskManagementJobRelationDataType]")
        
    def get_data(self):

        msg_data = []
        
        if self.task_management_job_relation_data is not None:
            msg_data.append({"taskManagementJobRelationData": [d.get_data() for d in self.task_management_job_relation_data]})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.task_management_job_relation_data is not None:
            result_str += f"{sep}taskManagementJobRelationData: {self.task_management_job_relation_data}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                task_management_job_relation_data=data_dict.get('taskManagementJobRelationData'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class TaskManagementJobListDataType: # EEBus_SPINE_TS_TaskManagement.xsd:ns_p:TaskManagementJobListDataType -> ComplexType
    def __init__(
            self,
            task_management_job_data: list[TaskManagementJobDataType] = None,
    ):
        super().__init__()
        
        self.task_management_job_data = task_management_job_data

        if not isinstance(self.task_management_job_data, list | NoneType):
            raise TypeError("task_management_job_data is not of type list[TaskManagementJobDataType]")
        
    def get_data(self):

        msg_data = []
        
        if self.task_management_job_data is not None:
            msg_data.append({"taskManagementJobData": [d.get_data() for d in self.task_management_job_data]})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.task_management_job_data is not None:
            result_str += f"{sep}taskManagementJobData: {self.task_management_job_data}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                task_management_job_data=data_dict.get('taskManagementJobData'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class TaskManagementJobDescriptionListDataType: # EEBus_SPINE_TS_TaskManagement.xsd:ns_p:TaskManagementJobDescriptionListDataType -> ComplexType
    def __init__(
            self,
            task_management_job_description_data: list[TaskManagementJobDescriptionDataType] = None,
    ):
        super().__init__()
        
        self.task_management_job_description_data = task_management_job_description_data

        if not isinstance(self.task_management_job_description_data, list | NoneType):
            raise TypeError("task_management_job_description_data is not of type list[TaskManagementJobDescriptionDataType]")
        
    def get_data(self):

        msg_data = []
        
        if self.task_management_job_description_data is not None:
            msg_data.append({"taskManagementJobDescriptionData": [d.get_data() for d in self.task_management_job_description_data]})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.task_management_job_description_data is not None:
            result_str += f"{sep}taskManagementJobDescriptionData: {self.task_management_job_description_data}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                task_management_job_description_data=data_dict.get('taskManagementJobDescriptionData'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class TaskManagementOverviewDataElementsType: # EEBus_SPINE_TS_TaskManagement.xsd:ns_p:TaskManagementOverviewDataElementsType -> ComplexType
    def __init__(
            self,
            remote_controllable: ElementTagType = None,
            jobs_active: ElementTagType = None,
    ):
        super().__init__()
        
        self.remote_controllable = remote_controllable
        self.jobs_active = jobs_active

        if not isinstance(self.remote_controllable, ElementTagType | NoneType):
            raise TypeError("remote_controllable is not of type ElementTagType")
        
        if not isinstance(self.jobs_active, ElementTagType | NoneType):
            raise TypeError("jobs_active is not of type ElementTagType")
        
    def get_data(self):

        msg_data = []
        
        if self.remote_controllable is not None:
            msg_data.append({"remoteControllable": self.remote_controllable.get_data()})
        if self.jobs_active is not None:
            msg_data.append({"jobsActive": self.jobs_active.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.remote_controllable is not None:
            result_str += f"{sep}remoteControllable: {self.remote_controllable}"
            sep = ", "
        if self.jobs_active is not None:
            result_str += f"{sep}jobsActive: {self.jobs_active}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                remote_controllable=data_dict.get('remoteControllable'),
                jobs_active=data_dict.get('jobsActive'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class TaskManagementJobRelationDataElementsType: # EEBus_SPINE_TS_TaskManagement.xsd:ns_p:TaskManagementJobRelationDataElementsType -> ComplexType
    def __init__(
            self,
            job_id: ElementTagType = None,
            direct_control_related: TaskManagementDirectControlRelatedElementsType = None,
            hvac_related: TaskManagementHvacRelatedElementsType = None,
            load_control_releated: TaskManagementLoadControlReleatedElementsType = None,
            power_sequences_related: TaskManagementPowerSequencesRelatedElementsType = None,
            smart_energy_management_ps_related: TaskManagementSmartEnergyManagementPsRelatedElementsType = None,
    ):
        super().__init__()
        
        self.job_id = job_id
        self.direct_control_related = direct_control_related
        self.hvac_related = hvac_related
        self.load_control_releated = load_control_releated
        self.power_sequences_related = power_sequences_related
        self.smart_energy_management_ps_related = smart_energy_management_ps_related

        if not isinstance(self.job_id, ElementTagType | NoneType):
            raise TypeError("job_id is not of type ElementTagType")
        
        if not isinstance(self.direct_control_related, TaskManagementDirectControlRelatedElementsType | NoneType):
            raise TypeError("direct_control_related is not of type TaskManagementDirectControlRelatedElementsType")
        
        if not isinstance(self.hvac_related, TaskManagementHvacRelatedElementsType | NoneType):
            raise TypeError("hvac_related is not of type TaskManagementHvacRelatedElementsType")
        
        if not isinstance(self.load_control_releated, TaskManagementLoadControlReleatedElementsType | NoneType):
            raise TypeError("load_control_releated is not of type TaskManagementLoadControlReleatedElementsType")
        
        if not isinstance(self.power_sequences_related, TaskManagementPowerSequencesRelatedElementsType | NoneType):
            raise TypeError("power_sequences_related is not of type TaskManagementPowerSequencesRelatedElementsType")
        
        if not isinstance(self.smart_energy_management_ps_related, TaskManagementSmartEnergyManagementPsRelatedElementsType | NoneType):
            raise TypeError("smart_energy_management_ps_related is not of type TaskManagementSmartEnergyManagementPsRelatedElementsType")
        
    def get_data(self):

        msg_data = []
        
        if self.job_id is not None:
            msg_data.append({"jobId": self.job_id.get_data()})
        if self.direct_control_related is not None:
            msg_data.append({"directControlRelated": self.direct_control_related.get_data()})
        if self.hvac_related is not None:
            msg_data.append({"hvacRelated": self.hvac_related.get_data()})
        if self.load_control_releated is not None:
            msg_data.append({"loadControlReleated": self.load_control_releated.get_data()})
        if self.power_sequences_related is not None:
            msg_data.append({"powerSequencesRelated": self.power_sequences_related.get_data()})
        if self.smart_energy_management_ps_related is not None:
            msg_data.append({"smartEnergyManagementPsRelated": self.smart_energy_management_ps_related.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.job_id is not None:
            result_str += f"{sep}jobId: {self.job_id}"
            sep = ", "
        if self.direct_control_related is not None:
            result_str += f"{sep}directControlRelated: {self.direct_control_related}"
            sep = ", "
        if self.hvac_related is not None:
            result_str += f"{sep}hvacRelated: {self.hvac_related}"
            sep = ", "
        if self.load_control_releated is not None:
            result_str += f"{sep}loadControlReleated: {self.load_control_releated}"
            sep = ", "
        if self.power_sequences_related is not None:
            result_str += f"{sep}powerSequencesRelated: {self.power_sequences_related}"
            sep = ", "
        if self.smart_energy_management_ps_related is not None:
            result_str += f"{sep}smartEnergyManagementPsRelated: {self.smart_energy_management_ps_related}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                job_id=data_dict.get('jobId'),
                direct_control_related=data_dict.get('directControlRelated'),
                hvac_related=data_dict.get('hvacRelated'),
                load_control_releated=data_dict.get('loadControlReleated'),
                power_sequences_related=data_dict.get('powerSequencesRelated'),
                smart_energy_management_ps_related=data_dict.get('smartEnergyManagementPsRelated'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class TaskManagementJobDescriptionDataElementsType: # EEBus_SPINE_TS_TaskManagement.xsd:ns_p:TaskManagementJobDescriptionDataElementsType -> ComplexType
    def __init__(
            self,
            job_id: ElementTagType = None,
            job_source: ElementTagType = None,
            label: ElementTagType = None,
            description: ElementTagType = None,
    ):
        super().__init__()
        
        self.job_id = job_id
        self.job_source = job_source
        self.label = label
        self.description = description

        if not isinstance(self.job_id, ElementTagType | NoneType):
            raise TypeError("job_id is not of type ElementTagType")
        
        if not isinstance(self.job_source, ElementTagType | NoneType):
            raise TypeError("job_source is not of type ElementTagType")
        
        if not isinstance(self.label, ElementTagType | NoneType):
            raise TypeError("label is not of type ElementTagType")
        
        if not isinstance(self.description, ElementTagType | NoneType):
            raise TypeError("description is not of type ElementTagType")
        
    def get_data(self):

        msg_data = []
        
        if self.job_id is not None:
            msg_data.append({"jobId": self.job_id.get_data()})
        if self.job_source is not None:
            msg_data.append({"jobSource": self.job_source.get_data()})
        if self.label is not None:
            msg_data.append({"label": self.label.get_data()})
        if self.description is not None:
            msg_data.append({"description": self.description.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.job_id is not None:
            result_str += f"{sep}jobId: {self.job_id}"
            sep = ", "
        if self.job_source is not None:
            result_str += f"{sep}jobSource: {self.job_source}"
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
                job_id=data_dict.get('jobId'),
                job_source=data_dict.get('jobSource'),
                label=data_dict.get('label'),
                description=data_dict.get('description'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class TaskManagementJobDataElementsType: # EEBus_SPINE_TS_TaskManagement.xsd:ns_p:TaskManagementJobDataElementsType -> ComplexType
    def __init__(
            self,
            job_id: ElementTagType = None,
            timestamp: ElementTagType = None,
            job_state: ElementTagType = None,
            elapsed_time: ElementTagType = None,
            remaining_time: ElementTagType = None,
    ):
        super().__init__()
        
        self.job_id = job_id
        self.timestamp = timestamp
        self.job_state = job_state
        self.elapsed_time = elapsed_time
        self.remaining_time = remaining_time

        if not isinstance(self.job_id, ElementTagType | NoneType):
            raise TypeError("job_id is not of type ElementTagType")
        
        if not isinstance(self.timestamp, ElementTagType | NoneType):
            raise TypeError("timestamp is not of type ElementTagType")
        
        if not isinstance(self.job_state, ElementTagType | NoneType):
            raise TypeError("job_state is not of type ElementTagType")
        
        if not isinstance(self.elapsed_time, ElementTagType | NoneType):
            raise TypeError("elapsed_time is not of type ElementTagType")
        
        if not isinstance(self.remaining_time, ElementTagType | NoneType):
            raise TypeError("remaining_time is not of type ElementTagType")
        
    def get_data(self):

        msg_data = []
        
        if self.job_id is not None:
            msg_data.append({"jobId": self.job_id.get_data()})
        if self.timestamp is not None:
            msg_data.append({"timestamp": self.timestamp.get_data()})
        if self.job_state is not None:
            msg_data.append({"jobState": self.job_state.get_data()})
        if self.elapsed_time is not None:
            msg_data.append({"elapsedTime": self.elapsed_time.get_data()})
        if self.remaining_time is not None:
            msg_data.append({"remainingTime": self.remaining_time.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.job_id is not None:
            result_str += f"{sep}jobId: {self.job_id}"
            sep = ", "
        if self.timestamp is not None:
            result_str += f"{sep}timestamp: {self.timestamp}"
            sep = ", "
        if self.job_state is not None:
            result_str += f"{sep}jobState: {self.job_state}"
            sep = ", "
        if self.elapsed_time is not None:
            result_str += f"{sep}elapsedTime: {self.elapsed_time}"
            sep = ", "
        if self.remaining_time is not None:
            result_str += f"{sep}remainingTime: {self.remaining_time}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                job_id=data_dict.get('jobId'),
                timestamp=data_dict.get('timestamp'),
                job_state=data_dict.get('jobState'),
                elapsed_time=data_dict.get('elapsedTime'),
                remaining_time=data_dict.get('remainingTime'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class TaskManagementJobRelationListDataSelectorsType: # EEBus_SPINE_TS_TaskManagement.xsd:ns_p:TaskManagementJobRelationListDataSelectorsType -> ComplexType
    def __init__(
            self,
            job_id: TaskManagementJobIdType = None,
    ):
        super().__init__()
        
        self.job_id = job_id

        if not isinstance(self.job_id, TaskManagementJobIdType | NoneType):
            raise TypeError("job_id is not of type TaskManagementJobIdType")
        
    def get_data(self):

        msg_data = []
        
        if self.job_id is not None:
            msg_data.append({"jobId": self.job_id.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.job_id is not None:
            result_str += f"{sep}jobId: {self.job_id}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                job_id=data_dict.get('jobId'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class TaskManagementJobListDataSelectorsType: # EEBus_SPINE_TS_TaskManagement.xsd:ns_p:TaskManagementJobListDataSelectorsType -> ComplexType
    def __init__(
            self,
            job_id: TaskManagementJobIdType = None,
            job_state: TaskManagementJobStateType = None,
    ):
        super().__init__()
        
        self.job_id = job_id
        self.job_state = job_state

        if not isinstance(self.job_id, TaskManagementJobIdType | NoneType):
            raise TypeError("job_id is not of type TaskManagementJobIdType")
        
        if not isinstance(self.job_state, TaskManagementJobStateType | NoneType):
            raise TypeError("job_state is not of type TaskManagementJobStateType")
        
    def get_data(self):

        msg_data = []
        
        if self.job_id is not None:
            msg_data.append({"jobId": self.job_id.get_data()})
        if self.job_state is not None:
            msg_data.append({"jobState": self.job_state.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.job_id is not None:
            result_str += f"{sep}jobId: {self.job_id}"
            sep = ", "
        if self.job_state is not None:
            result_str += f"{sep}jobState: {self.job_state}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                job_id=data_dict.get('jobId'),
                job_state=data_dict.get('jobState'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class TaskManagementJobDescriptionListDataSelectorsType: # EEBus_SPINE_TS_TaskManagement.xsd:ns_p:TaskManagementJobDescriptionListDataSelectorsType -> ComplexType
    def __init__(
            self,
            job_id: TaskManagementJobIdType = None,
            job_source: TaskManagementJobSourceType = None,
    ):
        super().__init__()
        
        self.job_id = job_id
        self.job_source = job_source

        if not isinstance(self.job_id, TaskManagementJobIdType | NoneType):
            raise TypeError("job_id is not of type TaskManagementJobIdType")
        
        if not isinstance(self.job_source, TaskManagementJobSourceType | NoneType):
            raise TypeError("job_source is not of type TaskManagementJobSourceType")
        
    def get_data(self):

        msg_data = []
        
        if self.job_id is not None:
            msg_data.append({"jobId": self.job_id.get_data()})
        if self.job_source is not None:
            msg_data.append({"jobSource": self.job_source.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.job_id is not None:
            result_str += f"{sep}jobId: {self.job_id}"
            sep = ", "
        if self.job_source is not None:
            result_str += f"{sep}jobSource: {self.job_source}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                job_id=data_dict.get('jobId'),
                job_source=data_dict.get('jobSource'),
            )
        elif data:
            return cls(data)
        else:
            return cls()



