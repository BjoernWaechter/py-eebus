# Jinja Template message_type.py.jinja2
from types import NoneType
from spine import array_2_dict


class NetworkManagementScanSetupType: # EEBus_SPINE_TS_NetworkManagement.xsd:ns_p:NetworkManagementScanSetupType -> AliasType
    def __init__(
            self,
            value: str,
    ):
        super().__init__()
        
        self.value = value

        if not isinstance(self.value, str):
            raise TypeError("value is not of type str")
        
    def get_data(self):

        return self.value


    def __str__(self):
        result_str = ""
        sep = ""
        if self.value is not None:
            result_str += f"{sep}value: {self.value}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                value=data_dict.get('value'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class NetworkManagementCandidateSetupType: # EEBus_SPINE_TS_NetworkManagement.xsd:ns_p:NetworkManagementCandidateSetupType -> AliasType
    def __init__(
            self,
            value: str,
    ):
        super().__init__()
        
        self.value = value

        if not isinstance(self.value, str):
            raise TypeError("value is not of type str")
        
    def get_data(self):

        return self.value


    def __str__(self):
        result_str = ""
        sep = ""
        if self.value is not None:
            result_str += f"{sep}value: {self.value}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                value=data_dict.get('value'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class NetworkManagementSetupType: # EEBus_SPINE_TS_NetworkManagement.xsd:ns_p:NetworkManagementSetupType -> AliasType
    def __init__(
            self,
            value: str,
    ):
        super().__init__()
        
        self.value = value

        if not isinstance(self.value, str):
            raise TypeError("value is not of type str")
        
    def get_data(self):

        return self.value


    def __str__(self):
        result_str = ""
        sep = ""
        if self.value is not None:
            result_str += f"{sep}value: {self.value}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                value=data_dict.get('value'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class NetworkManagementMinimumTrustLevelType: # EEBus_SPINE_TS_NetworkManagement.xsd:ns_p:NetworkManagementMinimumTrustLevelType -> AliasType
    def __init__(
            self,
            value: str,
    ):
        super().__init__()
        
        self.value = value

        if not isinstance(self.value, str):
            raise TypeError("value is not of type str")
        
    def get_data(self):

        return self.value


    def __str__(self):
        result_str = ""
        sep = ""
        if self.value is not None:
            result_str += f"{sep}value: {self.value}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                value=data_dict.get('value'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class NetworkManagementCommunicationsTechnologyInformationType: # EEBus_SPINE_TS_NetworkManagement.xsd:ns_p:NetworkManagementCommunicationsTechnologyInformationType -> AliasType
    def __init__(
            self,
            value: str,
    ):
        super().__init__()
        
        self.value = value

        if not isinstance(self.value, str):
            raise TypeError("value is not of type str")
        
    def get_data(self):

        return self.value


    def __str__(self):
        result_str = ""
        sep = ""
        if self.value is not None:
            result_str += f"{sep}value: {self.value}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                value=data_dict.get('value'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class NetworkManagementTechnologyAddressType: # EEBus_SPINE_TS_NetworkManagement.xsd:ns_p:NetworkManagementTechnologyAddressType -> AliasType
    def __init__(
            self,
            value: str,
    ):
        super().__init__()
        
        self.value = value

        if not isinstance(self.value, str):
            raise TypeError("value is not of type str")
        
    def get_data(self):

        return self.value


    def __str__(self):
        result_str = ""
        sep = ""
        if self.value is not None:
            result_str += f"{sep}value: {self.value}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                value=data_dict.get('value'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class NetworkManagementProcessTimeoutType: # EEBus_SPINE_TS_NetworkManagement.xsd:ns_p:NetworkManagementProcessTimeoutType -> AliasType
    def __init__(
            self,
            value: str,
    ):
        super().__init__()
        
        self.value = value

        if not isinstance(self.value, str):
            raise TypeError("value is not of type str")
        
    def get_data(self):

        return self.value


    def __str__(self):
        result_str = ""
        sep = ""
        if self.value is not None:
            result_str += f"{sep}value: {self.value}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                value=data_dict.get('value'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class NetworkManagementNativeSetupType: # EEBus_SPINE_TS_NetworkManagement.xsd:ns_p:NetworkManagementNativeSetupType -> AliasType
    def __init__(
            self,
            value: str,
    ):
        super().__init__()
        
        self.value = value

        if not isinstance(self.value, str):
            raise TypeError("value is not of type str")
        
    def get_data(self):

        return self.value


    def __str__(self):
        result_str = ""
        sep = ""
        if self.value is not None:
            result_str += f"{sep}value: {self.value}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                value=data_dict.get('value'),
            )
        elif data:
            return cls(data)
        else:
            return cls()



