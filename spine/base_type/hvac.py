# Jinja Template message_type.py.jinja2
from spine.base_type.commondatatypes import ElementTagType
from spine.simple_type.commondatatypes import DescriptionType
from spine.simple_type.commondatatypes import LabelType
from spine.simple_type.hvac import HvacOperationModeIdType
from spine.simple_type.hvac import HvacOverrunIdType
from spine.simple_type.hvac import HvacSystemFunctionIdType
from spine.simple_type.powersequences import PowerSequenceIdType
from spine.simple_type.setpoint import SetpointIdType
from spine.simple_type.timetable import TimeTableIdType
from spine.union_type.hvac import HvacOperationModeTypeType
from spine.union_type.hvac import HvacOverrunStatusType
from spine.union_type.hvac import HvacOverrunTypeType
from spine.union_type.hvac import HvacSystemFunctionTypeType
from types import NoneType
from spine import array_2_dict


class HvacOverrunDescriptionDataType: # EEBus_SPINE_TS_HVAC.xsd: ComplexType
    def __init__(
            self,
            overrun_id: HvacOverrunIdType = None,
            overrun_type: HvacOverrunTypeType = None,
            affected_system_function_id: list[HvacSystemFunctionIdType] = None,
            label: LabelType = None,
            description: DescriptionType = None,
    ):
        super().__init__()
        
        self.overrun_id = overrun_id
        self.overrun_type = overrun_type
        self.affected_system_function_id = affected_system_function_id
        self.label = label
        self.description = description

        if not isinstance(self.overrun_id, HvacOverrunIdType | NoneType):
            raise TypeError("overrun_id is not of type HvacOverrunIdType")
        
        if not isinstance(self.overrun_type, HvacOverrunTypeType | NoneType):
            raise TypeError("overrun_type is not of type HvacOverrunTypeType")
        
        if not isinstance(self.affected_system_function_id, list | NoneType):
            raise TypeError("affected_system_function_id is not of type list[HvacSystemFunctionIdType]")
        
        if not isinstance(self.label, LabelType | NoneType):
            raise TypeError("label is not of type LabelType")
        
        if not isinstance(self.description, DescriptionType | NoneType):
            raise TypeError("description is not of type DescriptionType")
        
    def get_data(self):

        msg_data = []
        
        if self.overrun_id is not None:
            msg_data.append({"overrunId": self.overrun_id.get_data()})
        if self.overrun_type is not None:
            msg_data.append({"overrunType": self.overrun_type.get_data()})
        if self.affected_system_function_id is not None:
            msg_data.append({"affectedSystemFunctionId": [d.get_data() for d in self.affected_system_function_id]})
        if self.label is not None:
            msg_data.append({"label": self.label.get_data()})
        if self.description is not None:
            msg_data.append({"description": self.description.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.overrun_id is not None:
            result_str += f"{sep}overrunId: {self.overrun_id}"
            sep = ", "
        if self.overrun_type is not None:
            result_str += f"{sep}overrunType: {self.overrun_type}"
            sep = ", "
        if self.affected_system_function_id is not None:
            result_str += f"{sep}affectedSystemFunctionId: {self.affected_system_function_id}"
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
                overrun_id=data_dict.get('overrunId'),
                overrun_type=data_dict.get('overrunType'),
                affected_system_function_id=data_dict.get('affectedSystemFunctionId'),
                label=data_dict.get('label'),
                description=data_dict.get('description'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class HvacOverrunDataType: # EEBus_SPINE_TS_HVAC.xsd: ComplexType
    def __init__(
            self,
            overrun_id: HvacOverrunIdType = None,
            overrun_status: HvacOverrunStatusType = None,
            time_table_id: TimeTableIdType = None,
            is_overrun_status_changeable: bool = None,
    ):
        super().__init__()
        
        self.overrun_id = overrun_id
        self.overrun_status = overrun_status
        self.time_table_id = time_table_id
        self.is_overrun_status_changeable = is_overrun_status_changeable

        if not isinstance(self.overrun_id, HvacOverrunIdType | NoneType):
            raise TypeError("overrun_id is not of type HvacOverrunIdType")
        
        if not isinstance(self.overrun_status, HvacOverrunStatusType | NoneType):
            raise TypeError("overrun_status is not of type HvacOverrunStatusType")
        
        if not isinstance(self.time_table_id, TimeTableIdType | NoneType):
            raise TypeError("time_table_id is not of type TimeTableIdType")
        
        if not isinstance(self.is_overrun_status_changeable, bool | NoneType):
            raise TypeError("is_overrun_status_changeable is not of type bool")
        
    def get_data(self):

        msg_data = []
        
        if self.overrun_id is not None:
            msg_data.append({"overrunId": self.overrun_id.get_data()})
        if self.overrun_status is not None:
            msg_data.append({"overrunStatus": self.overrun_status.get_data()})
        if self.time_table_id is not None:
            msg_data.append({"timeTableId": self.time_table_id.get_data()})
        if self.is_overrun_status_changeable is not None:
            msg_data.append({"isOverrunStatusChangeable": self.is_overrun_status_changeable})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.overrun_id is not None:
            result_str += f"{sep}overrunId: {self.overrun_id}"
            sep = ", "
        if self.overrun_status is not None:
            result_str += f"{sep}overrunStatus: {self.overrun_status}"
            sep = ", "
        if self.time_table_id is not None:
            result_str += f"{sep}timeTableId: {self.time_table_id}"
            sep = ", "
        if self.is_overrun_status_changeable is not None:
            result_str += f"{sep}isOverrunStatusChangeable: {self.is_overrun_status_changeable}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                overrun_id=data_dict.get('overrunId'),
                overrun_status=data_dict.get('overrunStatus'),
                time_table_id=data_dict.get('timeTableId'),
                is_overrun_status_changeable=data_dict.get('isOverrunStatusChangeable'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class HvacOperationModeDescriptionDataType: # EEBus_SPINE_TS_HVAC.xsd: ComplexType
    def __init__(
            self,
            operation_mode_id: HvacOperationModeIdType = None,
            operation_mode_type: HvacOperationModeTypeType = None,
            label: LabelType = None,
            description: DescriptionType = None,
    ):
        super().__init__()
        
        self.operation_mode_id = operation_mode_id
        self.operation_mode_type = operation_mode_type
        self.label = label
        self.description = description

        if not isinstance(self.operation_mode_id, HvacOperationModeIdType | NoneType):
            raise TypeError("operation_mode_id is not of type HvacOperationModeIdType")
        
        if not isinstance(self.operation_mode_type, HvacOperationModeTypeType | NoneType):
            raise TypeError("operation_mode_type is not of type HvacOperationModeTypeType")
        
        if not isinstance(self.label, LabelType | NoneType):
            raise TypeError("label is not of type LabelType")
        
        if not isinstance(self.description, DescriptionType | NoneType):
            raise TypeError("description is not of type DescriptionType")
        
    def get_data(self):

        msg_data = []
        
        if self.operation_mode_id is not None:
            msg_data.append({"operationModeId": self.operation_mode_id.get_data()})
        if self.operation_mode_type is not None:
            msg_data.append({"operationModeType": self.operation_mode_type.get_data()})
        if self.label is not None:
            msg_data.append({"label": self.label.get_data()})
        if self.description is not None:
            msg_data.append({"description": self.description.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.operation_mode_id is not None:
            result_str += f"{sep}operationModeId: {self.operation_mode_id}"
            sep = ", "
        if self.operation_mode_type is not None:
            result_str += f"{sep}operationModeType: {self.operation_mode_type}"
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
                operation_mode_id=data_dict.get('operationModeId'),
                operation_mode_type=data_dict.get('operationModeType'),
                label=data_dict.get('label'),
                description=data_dict.get('description'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class HvacSystemFunctionDescriptionDataType: # EEBus_SPINE_TS_HVAC.xsd: ComplexType
    def __init__(
            self,
            system_function_id: HvacSystemFunctionIdType = None,
            system_function_type: HvacSystemFunctionTypeType = None,
            label: LabelType = None,
            description: DescriptionType = None,
    ):
        super().__init__()
        
        self.system_function_id = system_function_id
        self.system_function_type = system_function_type
        self.label = label
        self.description = description

        if not isinstance(self.system_function_id, HvacSystemFunctionIdType | NoneType):
            raise TypeError("system_function_id is not of type HvacSystemFunctionIdType")
        
        if not isinstance(self.system_function_type, HvacSystemFunctionTypeType | NoneType):
            raise TypeError("system_function_type is not of type HvacSystemFunctionTypeType")
        
        if not isinstance(self.label, LabelType | NoneType):
            raise TypeError("label is not of type LabelType")
        
        if not isinstance(self.description, DescriptionType | NoneType):
            raise TypeError("description is not of type DescriptionType")
        
    def get_data(self):

        msg_data = []
        
        if self.system_function_id is not None:
            msg_data.append({"systemFunctionId": self.system_function_id.get_data()})
        if self.system_function_type is not None:
            msg_data.append({"systemFunctionType": self.system_function_type.get_data()})
        if self.label is not None:
            msg_data.append({"label": self.label.get_data()})
        if self.description is not None:
            msg_data.append({"description": self.description.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.system_function_id is not None:
            result_str += f"{sep}systemFunctionId: {self.system_function_id}"
            sep = ", "
        if self.system_function_type is not None:
            result_str += f"{sep}systemFunctionType: {self.system_function_type}"
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
                system_function_id=data_dict.get('systemFunctionId'),
                system_function_type=data_dict.get('systemFunctionType'),
                label=data_dict.get('label'),
                description=data_dict.get('description'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class HvacSystemFunctionPowerSequenceRelationDataType: # EEBus_SPINE_TS_HVAC.xsd: ComplexType
    def __init__(
            self,
            system_function_id: HvacSystemFunctionIdType = None,
            sequence_id: list[PowerSequenceIdType] = None,
    ):
        super().__init__()
        
        self.system_function_id = system_function_id
        self.sequence_id = sequence_id

        if not isinstance(self.system_function_id, HvacSystemFunctionIdType | NoneType):
            raise TypeError("system_function_id is not of type HvacSystemFunctionIdType")
        
        if not isinstance(self.sequence_id, list | NoneType):
            raise TypeError("sequence_id is not of type list[PowerSequenceIdType]")
        
    def get_data(self):

        msg_data = []
        
        if self.system_function_id is not None:
            msg_data.append({"systemFunctionId": self.system_function_id.get_data()})
        if self.sequence_id is not None:
            msg_data.append({"sequenceId": [d.get_data() for d in self.sequence_id]})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.system_function_id is not None:
            result_str += f"{sep}systemFunctionId: {self.system_function_id}"
            sep = ", "
        if self.sequence_id is not None:
            result_str += f"{sep}sequenceId: {self.sequence_id}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                system_function_id=data_dict.get('systemFunctionId'),
                sequence_id=data_dict.get('sequenceId'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class HvacSystemFunctionSetpointRelationDataType: # EEBus_SPINE_TS_HVAC.xsd: ComplexType
    def __init__(
            self,
            system_function_id: HvacSystemFunctionIdType = None,
            operation_mode_id: HvacOperationModeIdType = None,
            setpoint_id: list[SetpointIdType] = None,
    ):
        super().__init__()
        
        self.system_function_id = system_function_id
        self.operation_mode_id = operation_mode_id
        self.setpoint_id = setpoint_id

        if not isinstance(self.system_function_id, HvacSystemFunctionIdType | NoneType):
            raise TypeError("system_function_id is not of type HvacSystemFunctionIdType")
        
        if not isinstance(self.operation_mode_id, HvacOperationModeIdType | NoneType):
            raise TypeError("operation_mode_id is not of type HvacOperationModeIdType")
        
        if not isinstance(self.setpoint_id, list | NoneType):
            raise TypeError("setpoint_id is not of type list[SetpointIdType]")
        
    def get_data(self):

        msg_data = []
        
        if self.system_function_id is not None:
            msg_data.append({"systemFunctionId": self.system_function_id.get_data()})
        if self.operation_mode_id is not None:
            msg_data.append({"operationModeId": self.operation_mode_id.get_data()})
        if self.setpoint_id is not None:
            msg_data.append({"setpointId": [d.get_data() for d in self.setpoint_id]})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.system_function_id is not None:
            result_str += f"{sep}systemFunctionId: {self.system_function_id}"
            sep = ", "
        if self.operation_mode_id is not None:
            result_str += f"{sep}operationModeId: {self.operation_mode_id}"
            sep = ", "
        if self.setpoint_id is not None:
            result_str += f"{sep}setpointId: {self.setpoint_id}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                system_function_id=data_dict.get('systemFunctionId'),
                operation_mode_id=data_dict.get('operationModeId'),
                setpoint_id=data_dict.get('setpointId'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class HvacSystemFunctionOperationModeRelationDataType: # EEBus_SPINE_TS_HVAC.xsd: ComplexType
    def __init__(
            self,
            system_function_id: HvacSystemFunctionIdType = None,
            operation_mode_id: list[HvacOperationModeIdType] = None,
    ):
        super().__init__()
        
        self.system_function_id = system_function_id
        self.operation_mode_id = operation_mode_id

        if not isinstance(self.system_function_id, HvacSystemFunctionIdType | NoneType):
            raise TypeError("system_function_id is not of type HvacSystemFunctionIdType")
        
        if not isinstance(self.operation_mode_id, list | NoneType):
            raise TypeError("operation_mode_id is not of type list[HvacOperationModeIdType]")
        
    def get_data(self):

        msg_data = []
        
        if self.system_function_id is not None:
            msg_data.append({"systemFunctionId": self.system_function_id.get_data()})
        if self.operation_mode_id is not None:
            msg_data.append({"operationModeId": [d.get_data() for d in self.operation_mode_id]})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.system_function_id is not None:
            result_str += f"{sep}systemFunctionId: {self.system_function_id}"
            sep = ", "
        if self.operation_mode_id is not None:
            result_str += f"{sep}operationModeId: {self.operation_mode_id}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                system_function_id=data_dict.get('systemFunctionId'),
                operation_mode_id=data_dict.get('operationModeId'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class HvacSystemFunctionDataType: # EEBus_SPINE_TS_HVAC.xsd: ComplexType
    def __init__(
            self,
            system_function_id: HvacSystemFunctionIdType = None,
            current_operation_mode_id: HvacOperationModeIdType = None,
            is_operation_mode_id_changeable: bool = None,
            current_setpoint_id: SetpointIdType = None,
            is_setpoint_id_changeable: bool = None,
            is_overrun_active: bool = None,
    ):
        super().__init__()
        
        self.system_function_id = system_function_id
        self.current_operation_mode_id = current_operation_mode_id
        self.is_operation_mode_id_changeable = is_operation_mode_id_changeable
        self.current_setpoint_id = current_setpoint_id
        self.is_setpoint_id_changeable = is_setpoint_id_changeable
        self.is_overrun_active = is_overrun_active

        if not isinstance(self.system_function_id, HvacSystemFunctionIdType | NoneType):
            raise TypeError("system_function_id is not of type HvacSystemFunctionIdType")
        
        if not isinstance(self.current_operation_mode_id, HvacOperationModeIdType | NoneType):
            raise TypeError("current_operation_mode_id is not of type HvacOperationModeIdType")
        
        if not isinstance(self.is_operation_mode_id_changeable, bool | NoneType):
            raise TypeError("is_operation_mode_id_changeable is not of type bool")
        
        if not isinstance(self.current_setpoint_id, SetpointIdType | NoneType):
            raise TypeError("current_setpoint_id is not of type SetpointIdType")
        
        if not isinstance(self.is_setpoint_id_changeable, bool | NoneType):
            raise TypeError("is_setpoint_id_changeable is not of type bool")
        
        if not isinstance(self.is_overrun_active, bool | NoneType):
            raise TypeError("is_overrun_active is not of type bool")
        
    def get_data(self):

        msg_data = []
        
        if self.system_function_id is not None:
            msg_data.append({"systemFunctionId": self.system_function_id.get_data()})
        if self.current_operation_mode_id is not None:
            msg_data.append({"currentOperationModeId": self.current_operation_mode_id.get_data()})
        if self.is_operation_mode_id_changeable is not None:
            msg_data.append({"isOperationModeIdChangeable": self.is_operation_mode_id_changeable})
        if self.current_setpoint_id is not None:
            msg_data.append({"currentSetpointId": self.current_setpoint_id.get_data()})
        if self.is_setpoint_id_changeable is not None:
            msg_data.append({"isSetpointIdChangeable": self.is_setpoint_id_changeable})
        if self.is_overrun_active is not None:
            msg_data.append({"isOverrunActive": self.is_overrun_active})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.system_function_id is not None:
            result_str += f"{sep}systemFunctionId: {self.system_function_id}"
            sep = ", "
        if self.current_operation_mode_id is not None:
            result_str += f"{sep}currentOperationModeId: {self.current_operation_mode_id}"
            sep = ", "
        if self.is_operation_mode_id_changeable is not None:
            result_str += f"{sep}isOperationModeIdChangeable: {self.is_operation_mode_id_changeable}"
            sep = ", "
        if self.current_setpoint_id is not None:
            result_str += f"{sep}currentSetpointId: {self.current_setpoint_id}"
            sep = ", "
        if self.is_setpoint_id_changeable is not None:
            result_str += f"{sep}isSetpointIdChangeable: {self.is_setpoint_id_changeable}"
            sep = ", "
        if self.is_overrun_active is not None:
            result_str += f"{sep}isOverrunActive: {self.is_overrun_active}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                system_function_id=data_dict.get('systemFunctionId'),
                current_operation_mode_id=data_dict.get('currentOperationModeId'),
                is_operation_mode_id_changeable=data_dict.get('isOperationModeIdChangeable'),
                current_setpoint_id=data_dict.get('currentSetpointId'),
                is_setpoint_id_changeable=data_dict.get('isSetpointIdChangeable'),
                is_overrun_active=data_dict.get('isOverrunActive'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class HvacOverrunDescriptionListDataType: # EEBus_SPINE_TS_HVAC.xsd: ComplexType
    def __init__(
            self,
            hvac_overrun_description_data: list[HvacOverrunDescriptionDataType] = None,
    ):
        super().__init__()
        
        self.hvac_overrun_description_data = hvac_overrun_description_data

        if not isinstance(self.hvac_overrun_description_data, list | NoneType):
            raise TypeError("hvac_overrun_description_data is not of type list[HvacOverrunDescriptionDataType]")
        
    def get_data(self):

        msg_data = []
        
        if self.hvac_overrun_description_data is not None:
            msg_data.append({"hvacOverrunDescriptionData": [d.get_data() for d in self.hvac_overrun_description_data]})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.hvac_overrun_description_data is not None:
            result_str += f"{sep}hvacOverrunDescriptionData: {self.hvac_overrun_description_data}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                hvac_overrun_description_data=data_dict.get('hvacOverrunDescriptionData'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class HvacOverrunListDataType: # EEBus_SPINE_TS_HVAC.xsd: ComplexType
    def __init__(
            self,
            hvac_overrun_data: list[HvacOverrunDataType] = None,
    ):
        super().__init__()
        
        self.hvac_overrun_data = hvac_overrun_data

        if not isinstance(self.hvac_overrun_data, list | NoneType):
            raise TypeError("hvac_overrun_data is not of type list[HvacOverrunDataType]")
        
    def get_data(self):

        msg_data = []
        
        if self.hvac_overrun_data is not None:
            msg_data.append({"hvacOverrunData": [d.get_data() for d in self.hvac_overrun_data]})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.hvac_overrun_data is not None:
            result_str += f"{sep}hvacOverrunData: {self.hvac_overrun_data}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                hvac_overrun_data=data_dict.get('hvacOverrunData'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class HvacOperationModeDescriptionListDataType: # EEBus_SPINE_TS_HVAC.xsd: ComplexType
    def __init__(
            self,
            hvac_operation_mode_description_data: list[HvacOperationModeDescriptionDataType] = None,
    ):
        super().__init__()
        
        self.hvac_operation_mode_description_data = hvac_operation_mode_description_data

        if not isinstance(self.hvac_operation_mode_description_data, list | NoneType):
            raise TypeError("hvac_operation_mode_description_data is not of type list[HvacOperationModeDescriptionDataType]")
        
    def get_data(self):

        msg_data = []
        
        if self.hvac_operation_mode_description_data is not None:
            msg_data.append({"hvacOperationModeDescriptionData": [d.get_data() for d in self.hvac_operation_mode_description_data]})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.hvac_operation_mode_description_data is not None:
            result_str += f"{sep}hvacOperationModeDescriptionData: {self.hvac_operation_mode_description_data}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                hvac_operation_mode_description_data=data_dict.get('hvacOperationModeDescriptionData'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class HvacSystemFunctionDescriptionListDataType: # EEBus_SPINE_TS_HVAC.xsd: ComplexType
    def __init__(
            self,
            hvac_system_function_description_data: list[HvacSystemFunctionDescriptionDataType] = None,
    ):
        super().__init__()
        
        self.hvac_system_function_description_data = hvac_system_function_description_data

        if not isinstance(self.hvac_system_function_description_data, list | NoneType):
            raise TypeError("hvac_system_function_description_data is not of type list[HvacSystemFunctionDescriptionDataType]")
        
    def get_data(self):

        msg_data = []
        
        if self.hvac_system_function_description_data is not None:
            msg_data.append({"hvacSystemFunctionDescriptionData": [d.get_data() for d in self.hvac_system_function_description_data]})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.hvac_system_function_description_data is not None:
            result_str += f"{sep}hvacSystemFunctionDescriptionData: {self.hvac_system_function_description_data}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                hvac_system_function_description_data=data_dict.get('hvacSystemFunctionDescriptionData'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class HvacSystemFunctionPowerSequenceRelationListDataType: # EEBus_SPINE_TS_HVAC.xsd: ComplexType
    def __init__(
            self,
            hvac_system_function_power_sequence_relation_data: list[HvacSystemFunctionPowerSequenceRelationDataType] = None,
    ):
        super().__init__()
        
        self.hvac_system_function_power_sequence_relation_data = hvac_system_function_power_sequence_relation_data

        if not isinstance(self.hvac_system_function_power_sequence_relation_data, list | NoneType):
            raise TypeError("hvac_system_function_power_sequence_relation_data is not of type list[HvacSystemFunctionPowerSequenceRelationDataType]")
        
    def get_data(self):

        msg_data = []
        
        if self.hvac_system_function_power_sequence_relation_data is not None:
            msg_data.append({"hvacSystemFunctionPowerSequenceRelationData": [d.get_data() for d in self.hvac_system_function_power_sequence_relation_data]})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.hvac_system_function_power_sequence_relation_data is not None:
            result_str += f"{sep}hvacSystemFunctionPowerSequenceRelationData: {self.hvac_system_function_power_sequence_relation_data}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                hvac_system_function_power_sequence_relation_data=data_dict.get('hvacSystemFunctionPowerSequenceRelationData'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class HvacSystemFunctionSetpointRelationListDataType: # EEBus_SPINE_TS_HVAC.xsd: ComplexType
    def __init__(
            self,
            hvac_system_function_setpoint_relation_data: list[HvacSystemFunctionSetpointRelationDataType] = None,
    ):
        super().__init__()
        
        self.hvac_system_function_setpoint_relation_data = hvac_system_function_setpoint_relation_data

        if not isinstance(self.hvac_system_function_setpoint_relation_data, list | NoneType):
            raise TypeError("hvac_system_function_setpoint_relation_data is not of type list[HvacSystemFunctionSetpointRelationDataType]")
        
    def get_data(self):

        msg_data = []
        
        if self.hvac_system_function_setpoint_relation_data is not None:
            msg_data.append({"hvacSystemFunctionSetpointRelationData": [d.get_data() for d in self.hvac_system_function_setpoint_relation_data]})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.hvac_system_function_setpoint_relation_data is not None:
            result_str += f"{sep}hvacSystemFunctionSetpointRelationData: {self.hvac_system_function_setpoint_relation_data}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                hvac_system_function_setpoint_relation_data=data_dict.get('hvacSystemFunctionSetpointRelationData'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class HvacSystemFunctionOperationModeRelationListDataType: # EEBus_SPINE_TS_HVAC.xsd: ComplexType
    def __init__(
            self,
            hvac_system_function_operation_mode_relation_data: list[HvacSystemFunctionOperationModeRelationDataType] = None,
    ):
        super().__init__()
        
        self.hvac_system_function_operation_mode_relation_data = hvac_system_function_operation_mode_relation_data

        if not isinstance(self.hvac_system_function_operation_mode_relation_data, list | NoneType):
            raise TypeError("hvac_system_function_operation_mode_relation_data is not of type list[HvacSystemFunctionOperationModeRelationDataType]")
        
    def get_data(self):

        msg_data = []
        
        if self.hvac_system_function_operation_mode_relation_data is not None:
            msg_data.append({"hvacSystemFunctionOperationModeRelationData": [d.get_data() for d in self.hvac_system_function_operation_mode_relation_data]})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.hvac_system_function_operation_mode_relation_data is not None:
            result_str += f"{sep}hvacSystemFunctionOperationModeRelationData: {self.hvac_system_function_operation_mode_relation_data}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                hvac_system_function_operation_mode_relation_data=data_dict.get('hvacSystemFunctionOperationModeRelationData'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class HvacSystemFunctionListDataType: # EEBus_SPINE_TS_HVAC.xsd: ComplexType
    def __init__(
            self,
            hvac_system_function_data: list[HvacSystemFunctionDataType] = None,
    ):
        super().__init__()
        
        self.hvac_system_function_data = hvac_system_function_data

        if not isinstance(self.hvac_system_function_data, list | NoneType):
            raise TypeError("hvac_system_function_data is not of type list[HvacSystemFunctionDataType]")
        
    def get_data(self):

        msg_data = []
        
        if self.hvac_system_function_data is not None:
            msg_data.append({"hvacSystemFunctionData": [d.get_data() for d in self.hvac_system_function_data]})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.hvac_system_function_data is not None:
            result_str += f"{sep}hvacSystemFunctionData: {self.hvac_system_function_data}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                hvac_system_function_data=data_dict.get('hvacSystemFunctionData'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class HvacSystemFunctionSetpointRelationDataElementsType: # EEBus_SPINE_TS_HVAC.xsd: ComplexType
    def __init__(
            self,
            system_function_id: ElementTagType = None,
            operation_mode_id: ElementTagType = None,
            setpoint_id: ElementTagType = None,
    ):
        super().__init__()
        
        self.system_function_id = system_function_id
        self.operation_mode_id = operation_mode_id
        self.setpoint_id = setpoint_id

        if not isinstance(self.system_function_id, ElementTagType | NoneType):
            raise TypeError("system_function_id is not of type ElementTagType")
        
        if not isinstance(self.operation_mode_id, ElementTagType | NoneType):
            raise TypeError("operation_mode_id is not of type ElementTagType")
        
        if not isinstance(self.setpoint_id, ElementTagType | NoneType):
            raise TypeError("setpoint_id is not of type ElementTagType")
        
    def get_data(self):

        msg_data = []
        
        if self.system_function_id is not None:
            msg_data.append({"systemFunctionId": self.system_function_id.get_data()})
        if self.operation_mode_id is not None:
            msg_data.append({"operationModeId": self.operation_mode_id.get_data()})
        if self.setpoint_id is not None:
            msg_data.append({"setpointId": self.setpoint_id.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.system_function_id is not None:
            result_str += f"{sep}systemFunctionId: {self.system_function_id}"
            sep = ", "
        if self.operation_mode_id is not None:
            result_str += f"{sep}operationModeId: {self.operation_mode_id}"
            sep = ", "
        if self.setpoint_id is not None:
            result_str += f"{sep}setpointId: {self.setpoint_id}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                system_function_id=data_dict.get('systemFunctionId'),
                operation_mode_id=data_dict.get('operationModeId'),
                setpoint_id=data_dict.get('setpointId'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class HvacSystemFunctionPowerSequenceRelationDataElementsType: # EEBus_SPINE_TS_HVAC.xsd: ComplexType
    def __init__(
            self,
            system_function_id: ElementTagType = None,
            sequence_id: ElementTagType = None,
    ):
        super().__init__()
        
        self.system_function_id = system_function_id
        self.sequence_id = sequence_id

        if not isinstance(self.system_function_id, ElementTagType | NoneType):
            raise TypeError("system_function_id is not of type ElementTagType")
        
        if not isinstance(self.sequence_id, ElementTagType | NoneType):
            raise TypeError("sequence_id is not of type ElementTagType")
        
    def get_data(self):

        msg_data = []
        
        if self.system_function_id is not None:
            msg_data.append({"systemFunctionId": self.system_function_id.get_data()})
        if self.sequence_id is not None:
            msg_data.append({"sequenceId": self.sequence_id.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.system_function_id is not None:
            result_str += f"{sep}systemFunctionId: {self.system_function_id}"
            sep = ", "
        if self.sequence_id is not None:
            result_str += f"{sep}sequenceId: {self.sequence_id}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                system_function_id=data_dict.get('systemFunctionId'),
                sequence_id=data_dict.get('sequenceId'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class HvacSystemFunctionOperationModeRelationDataElementsType: # EEBus_SPINE_TS_HVAC.xsd: ComplexType
    def __init__(
            self,
            system_function_id: ElementTagType = None,
            operation_mode_id: ElementTagType = None,
    ):
        super().__init__()
        
        self.system_function_id = system_function_id
        self.operation_mode_id = operation_mode_id

        if not isinstance(self.system_function_id, ElementTagType | NoneType):
            raise TypeError("system_function_id is not of type ElementTagType")
        
        if not isinstance(self.operation_mode_id, ElementTagType | NoneType):
            raise TypeError("operation_mode_id is not of type ElementTagType")
        
    def get_data(self):

        msg_data = []
        
        if self.system_function_id is not None:
            msg_data.append({"systemFunctionId": self.system_function_id.get_data()})
        if self.operation_mode_id is not None:
            msg_data.append({"operationModeId": self.operation_mode_id.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.system_function_id is not None:
            result_str += f"{sep}systemFunctionId: {self.system_function_id}"
            sep = ", "
        if self.operation_mode_id is not None:
            result_str += f"{sep}operationModeId: {self.operation_mode_id}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                system_function_id=data_dict.get('systemFunctionId'),
                operation_mode_id=data_dict.get('operationModeId'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class HvacSystemFunctionDescriptionDataElementsType: # EEBus_SPINE_TS_HVAC.xsd: ComplexType
    def __init__(
            self,
            system_function_id: ElementTagType = None,
            system_function_type: ElementTagType = None,
            label: ElementTagType = None,
            description: ElementTagType = None,
    ):
        super().__init__()
        
        self.system_function_id = system_function_id
        self.system_function_type = system_function_type
        self.label = label
        self.description = description

        if not isinstance(self.system_function_id, ElementTagType | NoneType):
            raise TypeError("system_function_id is not of type ElementTagType")
        
        if not isinstance(self.system_function_type, ElementTagType | NoneType):
            raise TypeError("system_function_type is not of type ElementTagType")
        
        if not isinstance(self.label, ElementTagType | NoneType):
            raise TypeError("label is not of type ElementTagType")
        
        if not isinstance(self.description, ElementTagType | NoneType):
            raise TypeError("description is not of type ElementTagType")
        
    def get_data(self):

        msg_data = []
        
        if self.system_function_id is not None:
            msg_data.append({"systemFunctionId": self.system_function_id.get_data()})
        if self.system_function_type is not None:
            msg_data.append({"systemFunctionType": self.system_function_type.get_data()})
        if self.label is not None:
            msg_data.append({"label": self.label.get_data()})
        if self.description is not None:
            msg_data.append({"description": self.description.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.system_function_id is not None:
            result_str += f"{sep}systemFunctionId: {self.system_function_id}"
            sep = ", "
        if self.system_function_type is not None:
            result_str += f"{sep}systemFunctionType: {self.system_function_type}"
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
                system_function_id=data_dict.get('systemFunctionId'),
                system_function_type=data_dict.get('systemFunctionType'),
                label=data_dict.get('label'),
                description=data_dict.get('description'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class HvacSystemFunctionDataElementsType: # EEBus_SPINE_TS_HVAC.xsd: ComplexType
    def __init__(
            self,
            system_function_id: ElementTagType = None,
            current_operation_mode_id: ElementTagType = None,
            is_operation_mode_id_changeable: ElementTagType = None,
            current_setpoint_id: ElementTagType = None,
            is_setpoint_id_changeable: ElementTagType = None,
            is_overrun_active: ElementTagType = None,
    ):
        super().__init__()
        
        self.system_function_id = system_function_id
        self.current_operation_mode_id = current_operation_mode_id
        self.is_operation_mode_id_changeable = is_operation_mode_id_changeable
        self.current_setpoint_id = current_setpoint_id
        self.is_setpoint_id_changeable = is_setpoint_id_changeable
        self.is_overrun_active = is_overrun_active

        if not isinstance(self.system_function_id, ElementTagType | NoneType):
            raise TypeError("system_function_id is not of type ElementTagType")
        
        if not isinstance(self.current_operation_mode_id, ElementTagType | NoneType):
            raise TypeError("current_operation_mode_id is not of type ElementTagType")
        
        if not isinstance(self.is_operation_mode_id_changeable, ElementTagType | NoneType):
            raise TypeError("is_operation_mode_id_changeable is not of type ElementTagType")
        
        if not isinstance(self.current_setpoint_id, ElementTagType | NoneType):
            raise TypeError("current_setpoint_id is not of type ElementTagType")
        
        if not isinstance(self.is_setpoint_id_changeable, ElementTagType | NoneType):
            raise TypeError("is_setpoint_id_changeable is not of type ElementTagType")
        
        if not isinstance(self.is_overrun_active, ElementTagType | NoneType):
            raise TypeError("is_overrun_active is not of type ElementTagType")
        
    def get_data(self):

        msg_data = []
        
        if self.system_function_id is not None:
            msg_data.append({"systemFunctionId": self.system_function_id.get_data()})
        if self.current_operation_mode_id is not None:
            msg_data.append({"currentOperationModeId": self.current_operation_mode_id.get_data()})
        if self.is_operation_mode_id_changeable is not None:
            msg_data.append({"isOperationModeIdChangeable": self.is_operation_mode_id_changeable.get_data()})
        if self.current_setpoint_id is not None:
            msg_data.append({"currentSetpointId": self.current_setpoint_id.get_data()})
        if self.is_setpoint_id_changeable is not None:
            msg_data.append({"isSetpointIdChangeable": self.is_setpoint_id_changeable.get_data()})
        if self.is_overrun_active is not None:
            msg_data.append({"isOverrunActive": self.is_overrun_active.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.system_function_id is not None:
            result_str += f"{sep}systemFunctionId: {self.system_function_id}"
            sep = ", "
        if self.current_operation_mode_id is not None:
            result_str += f"{sep}currentOperationModeId: {self.current_operation_mode_id}"
            sep = ", "
        if self.is_operation_mode_id_changeable is not None:
            result_str += f"{sep}isOperationModeIdChangeable: {self.is_operation_mode_id_changeable}"
            sep = ", "
        if self.current_setpoint_id is not None:
            result_str += f"{sep}currentSetpointId: {self.current_setpoint_id}"
            sep = ", "
        if self.is_setpoint_id_changeable is not None:
            result_str += f"{sep}isSetpointIdChangeable: {self.is_setpoint_id_changeable}"
            sep = ", "
        if self.is_overrun_active is not None:
            result_str += f"{sep}isOverrunActive: {self.is_overrun_active}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                system_function_id=data_dict.get('systemFunctionId'),
                current_operation_mode_id=data_dict.get('currentOperationModeId'),
                is_operation_mode_id_changeable=data_dict.get('isOperationModeIdChangeable'),
                current_setpoint_id=data_dict.get('currentSetpointId'),
                is_setpoint_id_changeable=data_dict.get('isSetpointIdChangeable'),
                is_overrun_active=data_dict.get('isOverrunActive'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class HvacOverrunDescriptionDataElementsType: # EEBus_SPINE_TS_HVAC.xsd: ComplexType
    def __init__(
            self,
            overrun_id: ElementTagType = None,
            overrun_type: ElementTagType = None,
            affected_system_function_id: ElementTagType = None,
            label: ElementTagType = None,
            description: ElementTagType = None,
    ):
        super().__init__()
        
        self.overrun_id = overrun_id
        self.overrun_type = overrun_type
        self.affected_system_function_id = affected_system_function_id
        self.label = label
        self.description = description

        if not isinstance(self.overrun_id, ElementTagType | NoneType):
            raise TypeError("overrun_id is not of type ElementTagType")
        
        if not isinstance(self.overrun_type, ElementTagType | NoneType):
            raise TypeError("overrun_type is not of type ElementTagType")
        
        if not isinstance(self.affected_system_function_id, ElementTagType | NoneType):
            raise TypeError("affected_system_function_id is not of type ElementTagType")
        
        if not isinstance(self.label, ElementTagType | NoneType):
            raise TypeError("label is not of type ElementTagType")
        
        if not isinstance(self.description, ElementTagType | NoneType):
            raise TypeError("description is not of type ElementTagType")
        
    def get_data(self):

        msg_data = []
        
        if self.overrun_id is not None:
            msg_data.append({"overrunId": self.overrun_id.get_data()})
        if self.overrun_type is not None:
            msg_data.append({"overrunType": self.overrun_type.get_data()})
        if self.affected_system_function_id is not None:
            msg_data.append({"affectedSystemFunctionId": self.affected_system_function_id.get_data()})
        if self.label is not None:
            msg_data.append({"label": self.label.get_data()})
        if self.description is not None:
            msg_data.append({"description": self.description.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.overrun_id is not None:
            result_str += f"{sep}overrunId: {self.overrun_id}"
            sep = ", "
        if self.overrun_type is not None:
            result_str += f"{sep}overrunType: {self.overrun_type}"
            sep = ", "
        if self.affected_system_function_id is not None:
            result_str += f"{sep}affectedSystemFunctionId: {self.affected_system_function_id}"
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
                overrun_id=data_dict.get('overrunId'),
                overrun_type=data_dict.get('overrunType'),
                affected_system_function_id=data_dict.get('affectedSystemFunctionId'),
                label=data_dict.get('label'),
                description=data_dict.get('description'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class HvacOverrunDataElementsType: # EEBus_SPINE_TS_HVAC.xsd: ComplexType
    def __init__(
            self,
            overrun_id: ElementTagType = None,
            overrun_status: ElementTagType = None,
            time_table_id: ElementTagType = None,
            is_overrun_status_changeable: ElementTagType = None,
    ):
        super().__init__()
        
        self.overrun_id = overrun_id
        self.overrun_status = overrun_status
        self.time_table_id = time_table_id
        self.is_overrun_status_changeable = is_overrun_status_changeable

        if not isinstance(self.overrun_id, ElementTagType | NoneType):
            raise TypeError("overrun_id is not of type ElementTagType")
        
        if not isinstance(self.overrun_status, ElementTagType | NoneType):
            raise TypeError("overrun_status is not of type ElementTagType")
        
        if not isinstance(self.time_table_id, ElementTagType | NoneType):
            raise TypeError("time_table_id is not of type ElementTagType")
        
        if not isinstance(self.is_overrun_status_changeable, ElementTagType | NoneType):
            raise TypeError("is_overrun_status_changeable is not of type ElementTagType")
        
    def get_data(self):

        msg_data = []
        
        if self.overrun_id is not None:
            msg_data.append({"overrunId": self.overrun_id.get_data()})
        if self.overrun_status is not None:
            msg_data.append({"overrunStatus": self.overrun_status.get_data()})
        if self.time_table_id is not None:
            msg_data.append({"timeTableId": self.time_table_id.get_data()})
        if self.is_overrun_status_changeable is not None:
            msg_data.append({"isOverrunStatusChangeable": self.is_overrun_status_changeable.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.overrun_id is not None:
            result_str += f"{sep}overrunId: {self.overrun_id}"
            sep = ", "
        if self.overrun_status is not None:
            result_str += f"{sep}overrunStatus: {self.overrun_status}"
            sep = ", "
        if self.time_table_id is not None:
            result_str += f"{sep}timeTableId: {self.time_table_id}"
            sep = ", "
        if self.is_overrun_status_changeable is not None:
            result_str += f"{sep}isOverrunStatusChangeable: {self.is_overrun_status_changeable}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                overrun_id=data_dict.get('overrunId'),
                overrun_status=data_dict.get('overrunStatus'),
                time_table_id=data_dict.get('timeTableId'),
                is_overrun_status_changeable=data_dict.get('isOverrunStatusChangeable'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class HvacOperationModeDescriptionDataElementsType: # EEBus_SPINE_TS_HVAC.xsd: ComplexType
    def __init__(
            self,
            operation_mode_id: ElementTagType = None,
            operation_mode_type: ElementTagType = None,
            label: ElementTagType = None,
            description: ElementTagType = None,
    ):
        super().__init__()
        
        self.operation_mode_id = operation_mode_id
        self.operation_mode_type = operation_mode_type
        self.label = label
        self.description = description

        if not isinstance(self.operation_mode_id, ElementTagType | NoneType):
            raise TypeError("operation_mode_id is not of type ElementTagType")
        
        if not isinstance(self.operation_mode_type, ElementTagType | NoneType):
            raise TypeError("operation_mode_type is not of type ElementTagType")
        
        if not isinstance(self.label, ElementTagType | NoneType):
            raise TypeError("label is not of type ElementTagType")
        
        if not isinstance(self.description, ElementTagType | NoneType):
            raise TypeError("description is not of type ElementTagType")
        
    def get_data(self):

        msg_data = []
        
        if self.operation_mode_id is not None:
            msg_data.append({"operationModeId": self.operation_mode_id.get_data()})
        if self.operation_mode_type is not None:
            msg_data.append({"operationModeType": self.operation_mode_type.get_data()})
        if self.label is not None:
            msg_data.append({"label": self.label.get_data()})
        if self.description is not None:
            msg_data.append({"description": self.description.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.operation_mode_id is not None:
            result_str += f"{sep}operationModeId: {self.operation_mode_id}"
            sep = ", "
        if self.operation_mode_type is not None:
            result_str += f"{sep}operationModeType: {self.operation_mode_type}"
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
                operation_mode_id=data_dict.get('operationModeId'),
                operation_mode_type=data_dict.get('operationModeType'),
                label=data_dict.get('label'),
                description=data_dict.get('description'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class HvacSystemFunctionSetpointRelationListDataSelectorsType: # EEBus_SPINE_TS_HVAC.xsd: ComplexType
    def __init__(
            self,
            system_function_id: HvacSystemFunctionIdType = None,
            operation_mode_id: HvacOperationModeIdType = None,
    ):
        super().__init__()
        
        self.system_function_id = system_function_id
        self.operation_mode_id = operation_mode_id

        if not isinstance(self.system_function_id, HvacSystemFunctionIdType | NoneType):
            raise TypeError("system_function_id is not of type HvacSystemFunctionIdType")
        
        if not isinstance(self.operation_mode_id, HvacOperationModeIdType | NoneType):
            raise TypeError("operation_mode_id is not of type HvacOperationModeIdType")
        
    def get_data(self):

        msg_data = []
        
        if self.system_function_id is not None:
            msg_data.append({"systemFunctionId": self.system_function_id.get_data()})
        if self.operation_mode_id is not None:
            msg_data.append({"operationModeId": self.operation_mode_id.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.system_function_id is not None:
            result_str += f"{sep}systemFunctionId: {self.system_function_id}"
            sep = ", "
        if self.operation_mode_id is not None:
            result_str += f"{sep}operationModeId: {self.operation_mode_id}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                system_function_id=data_dict.get('systemFunctionId'),
                operation_mode_id=data_dict.get('operationModeId'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class HvacSystemFunctionPowerSequenceRelationListDataSelectorsType: # EEBus_SPINE_TS_HVAC.xsd: ComplexType
    def __init__(
            self,
            system_function_id: HvacSystemFunctionIdType = None,
    ):
        super().__init__()
        
        self.system_function_id = system_function_id

        if not isinstance(self.system_function_id, HvacSystemFunctionIdType | NoneType):
            raise TypeError("system_function_id is not of type HvacSystemFunctionIdType")
        
    def get_data(self):

        msg_data = []
        
        if self.system_function_id is not None:
            msg_data.append({"systemFunctionId": self.system_function_id.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.system_function_id is not None:
            result_str += f"{sep}systemFunctionId: {self.system_function_id}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                system_function_id=data_dict.get('systemFunctionId'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class HvacSystemFunctionOperationModeRelationListDataSelectorsType: # EEBus_SPINE_TS_HVAC.xsd: ComplexType
    def __init__(
            self,
            system_function_id: HvacSystemFunctionIdType = None,
    ):
        super().__init__()
        
        self.system_function_id = system_function_id

        if not isinstance(self.system_function_id, HvacSystemFunctionIdType | NoneType):
            raise TypeError("system_function_id is not of type HvacSystemFunctionIdType")
        
    def get_data(self):

        msg_data = []
        
        if self.system_function_id is not None:
            msg_data.append({"systemFunctionId": self.system_function_id.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.system_function_id is not None:
            result_str += f"{sep}systemFunctionId: {self.system_function_id}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                system_function_id=data_dict.get('systemFunctionId'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class HvacSystemFunctionListDataSelectorsType: # EEBus_SPINE_TS_HVAC.xsd: ComplexType
    def __init__(
            self,
            system_function_id: HvacSystemFunctionIdType = None,
    ):
        super().__init__()
        
        self.system_function_id = system_function_id

        if not isinstance(self.system_function_id, HvacSystemFunctionIdType | NoneType):
            raise TypeError("system_function_id is not of type HvacSystemFunctionIdType")
        
    def get_data(self):

        msg_data = []
        
        if self.system_function_id is not None:
            msg_data.append({"systemFunctionId": self.system_function_id.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.system_function_id is not None:
            result_str += f"{sep}systemFunctionId: {self.system_function_id}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                system_function_id=data_dict.get('systemFunctionId'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class HvacSystemFunctionDescriptionListDataSelectorsType: # EEBus_SPINE_TS_HVAC.xsd: ComplexType
    def __init__(
            self,
            system_function_id: HvacSystemFunctionIdType = None,
    ):
        super().__init__()
        
        self.system_function_id = system_function_id

        if not isinstance(self.system_function_id, HvacSystemFunctionIdType | NoneType):
            raise TypeError("system_function_id is not of type HvacSystemFunctionIdType")
        
    def get_data(self):

        msg_data = []
        
        if self.system_function_id is not None:
            msg_data.append({"systemFunctionId": self.system_function_id.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.system_function_id is not None:
            result_str += f"{sep}systemFunctionId: {self.system_function_id}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                system_function_id=data_dict.get('systemFunctionId'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class HvacOverrunListDataSelectorsType: # EEBus_SPINE_TS_HVAC.xsd: ComplexType
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


class HvacOverrunDescriptionListDataSelectorsType: # EEBus_SPINE_TS_HVAC.xsd: ComplexType
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


class HvacOperationModeDescriptionListDataSelectorsType: # EEBus_SPINE_TS_HVAC.xsd: ComplexType
    def __init__(
            self,
            operation_mode_id: HvacOperationModeIdType = None,
    ):
        super().__init__()
        
        self.operation_mode_id = operation_mode_id

        if not isinstance(self.operation_mode_id, HvacOperationModeIdType | NoneType):
            raise TypeError("operation_mode_id is not of type HvacOperationModeIdType")
        
    def get_data(self):

        msg_data = []
        
        if self.operation_mode_id is not None:
            msg_data.append({"operationModeId": self.operation_mode_id.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.operation_mode_id is not None:
            result_str += f"{sep}operationModeId: {self.operation_mode_id}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                operation_mode_id=data_dict.get('operationModeId'),
            )
        elif data:
            return cls(data)
        else:
            return cls()



