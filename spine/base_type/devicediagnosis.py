# Jinja Template message_type.py.jinja2
from spine.base_type.commondatatypes import ElementTagType
from spine.simple_type.devicediagnosis import LastErrorCodeType
from spine.simple_type.devicediagnosis import VendorStateCodeType
from spine.union_type.commondatatypes import AbsoluteOrRelativeTimeType
from spine.union_type.devicediagnosis import DeviceDiagnosisOperatingStateType
from spine.union_type.devicediagnosis import PowerSupplyConditionType
from types import NoneType
from spine import array_2_dict


class DeviceDiagnosisStateDataType: # EEBus_SPINE_TS_DeviceDiagnosis.xsd:ns_p:DeviceDiagnosisStateDataType -> ComplexType
    def __init__(
            self,
            timestamp: AbsoluteOrRelativeTimeType = None,
            operating_state: DeviceDiagnosisOperatingStateType = None,
            vendor_state_code: VendorStateCodeType = None,
            last_error_code: LastErrorCodeType = None,
            up_time: str = None,
            total_up_time: str = None,
            power_supply_condition: PowerSupplyConditionType = None,
    ):
        super().__init__()
        
        self.timestamp = timestamp
        self.operating_state = operating_state
        self.vendor_state_code = vendor_state_code
        self.last_error_code = last_error_code
        self.up_time = up_time
        self.total_up_time = total_up_time
        self.power_supply_condition = power_supply_condition

        if not isinstance(self.timestamp, AbsoluteOrRelativeTimeType | NoneType):
            raise TypeError("timestamp is not of type AbsoluteOrRelativeTimeType")
        
        if not isinstance(self.operating_state, DeviceDiagnosisOperatingStateType | NoneType):
            raise TypeError("operating_state is not of type DeviceDiagnosisOperatingStateType")
        
        if not isinstance(self.vendor_state_code, VendorStateCodeType | NoneType):
            raise TypeError("vendor_state_code is not of type VendorStateCodeType")
        
        if not isinstance(self.last_error_code, LastErrorCodeType | NoneType):
            raise TypeError("last_error_code is not of type LastErrorCodeType")
        
        if not isinstance(self.up_time, str | NoneType):
            raise TypeError("up_time is not of type str")
        
        if not isinstance(self.total_up_time, str | NoneType):
            raise TypeError("total_up_time is not of type str")
        
        if not isinstance(self.power_supply_condition, PowerSupplyConditionType | NoneType):
            raise TypeError("power_supply_condition is not of type PowerSupplyConditionType")
        
    def get_data(self):

        msg_data = []
        
        if self.timestamp is not None:
            msg_data.append({"timestamp": self.timestamp.get_data()})
        if self.operating_state is not None:
            msg_data.append({"operatingState": self.operating_state.get_data()})
        if self.vendor_state_code is not None:
            msg_data.append({"vendorStateCode": self.vendor_state_code.get_data()})
        if self.last_error_code is not None:
            msg_data.append({"lastErrorCode": self.last_error_code.get_data()})
        if self.up_time is not None:
            msg_data.append({"upTime": self.up_time})
        if self.total_up_time is not None:
            msg_data.append({"totalUpTime": self.total_up_time})
        if self.power_supply_condition is not None:
            msg_data.append({"powerSupplyCondition": self.power_supply_condition.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.timestamp is not None:
            result_str += f"{sep}timestamp: {self.timestamp}"
            sep = ", "
        if self.operating_state is not None:
            result_str += f"{sep}operatingState: {self.operating_state}"
            sep = ", "
        if self.vendor_state_code is not None:
            result_str += f"{sep}vendorStateCode: {self.vendor_state_code}"
            sep = ", "
        if self.last_error_code is not None:
            result_str += f"{sep}lastErrorCode: {self.last_error_code}"
            sep = ", "
        if self.up_time is not None:
            result_str += f"{sep}upTime: {self.up_time}"
            sep = ", "
        if self.total_up_time is not None:
            result_str += f"{sep}totalUpTime: {self.total_up_time}"
            sep = ", "
        if self.power_supply_condition is not None:
            result_str += f"{sep}powerSupplyCondition: {self.power_supply_condition}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                timestamp=data_dict.get('timestamp'),
                operating_state=data_dict.get('operatingState'),
                vendor_state_code=data_dict.get('vendorStateCode'),
                last_error_code=data_dict.get('lastErrorCode'),
                up_time=data_dict.get('upTime'),
                total_up_time=data_dict.get('totalUpTime'),
                power_supply_condition=data_dict.get('powerSupplyCondition'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class DeviceDiagnosisServiceDataType: # EEBus_SPINE_TS_DeviceDiagnosis.xsd:ns_p:DeviceDiagnosisServiceDataType -> ComplexType
    def __init__(
            self,
            timestamp: AbsoluteOrRelativeTimeType = None,
            installation_time: AbsoluteOrRelativeTimeType = None,
            boot_counter: int = None,
            next_service: AbsoluteOrRelativeTimeType = None,
    ):
        super().__init__()
        
        self.timestamp = timestamp
        self.installation_time = installation_time
        self.boot_counter = boot_counter
        self.next_service = next_service

        if not isinstance(self.timestamp, AbsoluteOrRelativeTimeType | NoneType):
            raise TypeError("timestamp is not of type AbsoluteOrRelativeTimeType")
        
        if not isinstance(self.installation_time, AbsoluteOrRelativeTimeType | NoneType):
            raise TypeError("installation_time is not of type AbsoluteOrRelativeTimeType")
        
        if not isinstance(self.boot_counter, int | NoneType):
            raise TypeError("boot_counter is not of type int")
        
        if not isinstance(self.next_service, AbsoluteOrRelativeTimeType | NoneType):
            raise TypeError("next_service is not of type AbsoluteOrRelativeTimeType")
        
    def get_data(self):

        msg_data = []
        
        if self.timestamp is not None:
            msg_data.append({"timestamp": self.timestamp.get_data()})
        if self.installation_time is not None:
            msg_data.append({"installationTime": self.installation_time.get_data()})
        if self.boot_counter is not None:
            msg_data.append({"bootCounter": self.boot_counter})
        if self.next_service is not None:
            msg_data.append({"nextService": self.next_service.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.timestamp is not None:
            result_str += f"{sep}timestamp: {self.timestamp}"
            sep = ", "
        if self.installation_time is not None:
            result_str += f"{sep}installationTime: {self.installation_time}"
            sep = ", "
        if self.boot_counter is not None:
            result_str += f"{sep}bootCounter: {self.boot_counter}"
            sep = ", "
        if self.next_service is not None:
            result_str += f"{sep}nextService: {self.next_service}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                timestamp=data_dict.get('timestamp'),
                installation_time=data_dict.get('installationTime'),
                boot_counter=data_dict.get('bootCounter'),
                next_service=data_dict.get('nextService'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class DeviceDiagnosisHeartbeatDataType: # EEBus_SPINE_TS_DeviceDiagnosis.xsd:ns_p:DeviceDiagnosisHeartbeatDataType -> ComplexType
    def __init__(
            self,
            timestamp: AbsoluteOrRelativeTimeType = None,
            heartbeat_counter: int = None,
            heartbeat_timeout: str = None,
    ):
        super().__init__()
        
        self.timestamp = timestamp
        self.heartbeat_counter = heartbeat_counter
        self.heartbeat_timeout = heartbeat_timeout

        if not isinstance(self.timestamp, AbsoluteOrRelativeTimeType | NoneType):
            raise TypeError("timestamp is not of type AbsoluteOrRelativeTimeType")
        
        if not isinstance(self.heartbeat_counter, int | NoneType):
            raise TypeError("heartbeat_counter is not of type int")
        
        if not isinstance(self.heartbeat_timeout, str | NoneType):
            raise TypeError("heartbeat_timeout is not of type str")
        
    def get_data(self):

        msg_data = []
        
        if self.timestamp is not None:
            msg_data.append({"timestamp": self.timestamp.get_data()})
        if self.heartbeat_counter is not None:
            msg_data.append({"heartbeatCounter": self.heartbeat_counter})
        if self.heartbeat_timeout is not None:
            msg_data.append({"heartbeatTimeout": self.heartbeat_timeout})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.timestamp is not None:
            result_str += f"{sep}timestamp: {self.timestamp}"
            sep = ", "
        if self.heartbeat_counter is not None:
            result_str += f"{sep}heartbeatCounter: {self.heartbeat_counter}"
            sep = ", "
        if self.heartbeat_timeout is not None:
            result_str += f"{sep}heartbeatTimeout: {self.heartbeat_timeout}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                timestamp=data_dict.get('timestamp'),
                heartbeat_counter=data_dict.get('heartbeatCounter'),
                heartbeat_timeout=data_dict.get('heartbeatTimeout'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class DeviceDiagnosisStateDataElementsType: # EEBus_SPINE_TS_DeviceDiagnosis.xsd:ns_p:DeviceDiagnosisStateDataElementsType -> ComplexType
    def __init__(
            self,
            timestamp: ElementTagType = None,
            operating_state: ElementTagType = None,
            vendor_state_code: ElementTagType = None,
            last_error_code: ElementTagType = None,
            up_time: ElementTagType = None,
            total_up_time: ElementTagType = None,
            power_supply_condition: ElementTagType = None,
    ):
        super().__init__()
        
        self.timestamp = timestamp
        self.operating_state = operating_state
        self.vendor_state_code = vendor_state_code
        self.last_error_code = last_error_code
        self.up_time = up_time
        self.total_up_time = total_up_time
        self.power_supply_condition = power_supply_condition

        if not isinstance(self.timestamp, ElementTagType | NoneType):
            raise TypeError("timestamp is not of type ElementTagType")
        
        if not isinstance(self.operating_state, ElementTagType | NoneType):
            raise TypeError("operating_state is not of type ElementTagType")
        
        if not isinstance(self.vendor_state_code, ElementTagType | NoneType):
            raise TypeError("vendor_state_code is not of type ElementTagType")
        
        if not isinstance(self.last_error_code, ElementTagType | NoneType):
            raise TypeError("last_error_code is not of type ElementTagType")
        
        if not isinstance(self.up_time, ElementTagType | NoneType):
            raise TypeError("up_time is not of type ElementTagType")
        
        if not isinstance(self.total_up_time, ElementTagType | NoneType):
            raise TypeError("total_up_time is not of type ElementTagType")
        
        if not isinstance(self.power_supply_condition, ElementTagType | NoneType):
            raise TypeError("power_supply_condition is not of type ElementTagType")
        
    def get_data(self):

        msg_data = []
        
        if self.timestamp is not None:
            msg_data.append({"timestamp": self.timestamp.get_data()})
        if self.operating_state is not None:
            msg_data.append({"operatingState": self.operating_state.get_data()})
        if self.vendor_state_code is not None:
            msg_data.append({"vendorStateCode": self.vendor_state_code.get_data()})
        if self.last_error_code is not None:
            msg_data.append({"lastErrorCode": self.last_error_code.get_data()})
        if self.up_time is not None:
            msg_data.append({"upTime": self.up_time.get_data()})
        if self.total_up_time is not None:
            msg_data.append({"totalUpTime": self.total_up_time.get_data()})
        if self.power_supply_condition is not None:
            msg_data.append({"powerSupplyCondition": self.power_supply_condition.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.timestamp is not None:
            result_str += f"{sep}timestamp: {self.timestamp}"
            sep = ", "
        if self.operating_state is not None:
            result_str += f"{sep}operatingState: {self.operating_state}"
            sep = ", "
        if self.vendor_state_code is not None:
            result_str += f"{sep}vendorStateCode: {self.vendor_state_code}"
            sep = ", "
        if self.last_error_code is not None:
            result_str += f"{sep}lastErrorCode: {self.last_error_code}"
            sep = ", "
        if self.up_time is not None:
            result_str += f"{sep}upTime: {self.up_time}"
            sep = ", "
        if self.total_up_time is not None:
            result_str += f"{sep}totalUpTime: {self.total_up_time}"
            sep = ", "
        if self.power_supply_condition is not None:
            result_str += f"{sep}powerSupplyCondition: {self.power_supply_condition}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                timestamp=data_dict.get('timestamp'),
                operating_state=data_dict.get('operatingState'),
                vendor_state_code=data_dict.get('vendorStateCode'),
                last_error_code=data_dict.get('lastErrorCode'),
                up_time=data_dict.get('upTime'),
                total_up_time=data_dict.get('totalUpTime'),
                power_supply_condition=data_dict.get('powerSupplyCondition'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class DeviceDiagnosisServiceDataElementsType: # EEBus_SPINE_TS_DeviceDiagnosis.xsd:ns_p:DeviceDiagnosisServiceDataElementsType -> ComplexType
    def __init__(
            self,
            timestamp: ElementTagType = None,
            installation_time: ElementTagType = None,
            boot_counter: ElementTagType = None,
            next_service: ElementTagType = None,
    ):
        super().__init__()
        
        self.timestamp = timestamp
        self.installation_time = installation_time
        self.boot_counter = boot_counter
        self.next_service = next_service

        if not isinstance(self.timestamp, ElementTagType | NoneType):
            raise TypeError("timestamp is not of type ElementTagType")
        
        if not isinstance(self.installation_time, ElementTagType | NoneType):
            raise TypeError("installation_time is not of type ElementTagType")
        
        if not isinstance(self.boot_counter, ElementTagType | NoneType):
            raise TypeError("boot_counter is not of type ElementTagType")
        
        if not isinstance(self.next_service, ElementTagType | NoneType):
            raise TypeError("next_service is not of type ElementTagType")
        
    def get_data(self):

        msg_data = []
        
        if self.timestamp is not None:
            msg_data.append({"timestamp": self.timestamp.get_data()})
        if self.installation_time is not None:
            msg_data.append({"installationTime": self.installation_time.get_data()})
        if self.boot_counter is not None:
            msg_data.append({"bootCounter": self.boot_counter.get_data()})
        if self.next_service is not None:
            msg_data.append({"nextService": self.next_service.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.timestamp is not None:
            result_str += f"{sep}timestamp: {self.timestamp}"
            sep = ", "
        if self.installation_time is not None:
            result_str += f"{sep}installationTime: {self.installation_time}"
            sep = ", "
        if self.boot_counter is not None:
            result_str += f"{sep}bootCounter: {self.boot_counter}"
            sep = ", "
        if self.next_service is not None:
            result_str += f"{sep}nextService: {self.next_service}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                timestamp=data_dict.get('timestamp'),
                installation_time=data_dict.get('installationTime'),
                boot_counter=data_dict.get('bootCounter'),
                next_service=data_dict.get('nextService'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class DeviceDiagnosisHeartbeatDataElementsType: # EEBus_SPINE_TS_DeviceDiagnosis.xsd:ns_p:DeviceDiagnosisHeartbeatDataElementsType -> ComplexType
    def __init__(
            self,
            timestamp: ElementTagType = None,
            heartbeat_counter: ElementTagType = None,
            heartbeat_timeout: ElementTagType = None,
    ):
        super().__init__()
        
        self.timestamp = timestamp
        self.heartbeat_counter = heartbeat_counter
        self.heartbeat_timeout = heartbeat_timeout

        if not isinstance(self.timestamp, ElementTagType | NoneType):
            raise TypeError("timestamp is not of type ElementTagType")
        
        if not isinstance(self.heartbeat_counter, ElementTagType | NoneType):
            raise TypeError("heartbeat_counter is not of type ElementTagType")
        
        if not isinstance(self.heartbeat_timeout, ElementTagType | NoneType):
            raise TypeError("heartbeat_timeout is not of type ElementTagType")
        
    def get_data(self):

        msg_data = []
        
        if self.timestamp is not None:
            msg_data.append({"timestamp": self.timestamp.get_data()})
        if self.heartbeat_counter is not None:
            msg_data.append({"heartbeatCounter": self.heartbeat_counter.get_data()})
        if self.heartbeat_timeout is not None:
            msg_data.append({"heartbeatTimeout": self.heartbeat_timeout.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.timestamp is not None:
            result_str += f"{sep}timestamp: {self.timestamp}"
            sep = ", "
        if self.heartbeat_counter is not None:
            result_str += f"{sep}heartbeatCounter: {self.heartbeat_counter}"
            sep = ", "
        if self.heartbeat_timeout is not None:
            result_str += f"{sep}heartbeatTimeout: {self.heartbeat_timeout}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                timestamp=data_dict.get('timestamp'),
                heartbeat_counter=data_dict.get('heartbeatCounter'),
                heartbeat_timeout=data_dict.get('heartbeatTimeout'),
            )
        elif data:
            return cls(data)
        else:
            return cls()



