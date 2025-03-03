# Jinja Template message_type.py.jinja2
from spine.base_type.commondatatypes import ElementTagType
from spine.base_type.commondatatypes import TimePeriodElementsType
from spine.base_type.commondatatypes import TimePeriodType
from spine.simple_type.identification import IdentificationIdType
from spine.simple_type.identification import IdentificationValueType
from spine.simple_type.identification import SessionIdType
from spine.simple_type.measurement import MeasurementIdType
from spine.union_type.identification import IdentificationTypeType
from types import NoneType
from spine import array_2_dict


class SessionMeasurementRelationDataType: # EEBus_SPINE_TS_Identification.xsd:ns_p:SessionMeasurementRelationDataType -> ComplexType
    def __init__(
            self,
            session_id: SessionIdType = None,
            measurement_id: list[MeasurementIdType] = None,
    ):
        super().__init__()
        
        self.session_id = session_id
        self.measurement_id = measurement_id

        if not isinstance(self.session_id, SessionIdType | NoneType):
            raise TypeError("session_id is not of type SessionIdType")
        
        if not isinstance(self.measurement_id, list | NoneType):
            raise TypeError("measurement_id is not of type list[MeasurementIdType]")
        
    def get_data(self):

        msg_data = []
        
        if self.session_id is not None:
            msg_data.append({"sessionId": self.session_id.get_data()})
        if self.measurement_id is not None:
            msg_data.append({"measurementId": [d.get_data() for d in self.measurement_id]})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.session_id is not None:
            result_str += f"{sep}sessionId: {self.session_id}"
            sep = ", "
        if self.measurement_id is not None:
            result_str += f"{sep}measurementId: {self.measurement_id}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                session_id=data_dict.get('sessionId'),
                measurement_id=data_dict.get('measurementId'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class SessionIdentificationDataType: # EEBus_SPINE_TS_Identification.xsd:ns_p:SessionIdentificationDataType -> ComplexType
    def __init__(
            self,
            session_id: SessionIdType = None,
            identification_id: IdentificationIdType = None,
            is_latest_session: bool = None,
            time_period: TimePeriodType = None,
    ):
        super().__init__()
        
        self.session_id = session_id
        self.identification_id = identification_id
        self.is_latest_session = is_latest_session
        self.time_period = time_period

        if not isinstance(self.session_id, SessionIdType | NoneType):
            raise TypeError("session_id is not of type SessionIdType")
        
        if not isinstance(self.identification_id, IdentificationIdType | NoneType):
            raise TypeError("identification_id is not of type IdentificationIdType")
        
        if not isinstance(self.is_latest_session, bool | NoneType):
            raise TypeError("is_latest_session is not of type bool")
        
        if not isinstance(self.time_period, TimePeriodType | NoneType):
            raise TypeError("time_period is not of type TimePeriodType")
        
    def get_data(self):

        msg_data = []
        
        if self.session_id is not None:
            msg_data.append({"sessionId": self.session_id.get_data()})
        if self.identification_id is not None:
            msg_data.append({"identificationId": self.identification_id.get_data()})
        if self.is_latest_session is not None:
            msg_data.append({"isLatestSession": self.is_latest_session})
        if self.time_period is not None:
            msg_data.append({"timePeriod": self.time_period.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.session_id is not None:
            result_str += f"{sep}sessionId: {self.session_id}"
            sep = ", "
        if self.identification_id is not None:
            result_str += f"{sep}identificationId: {self.identification_id}"
            sep = ", "
        if self.is_latest_session is not None:
            result_str += f"{sep}isLatestSession: {self.is_latest_session}"
            sep = ", "
        if self.time_period is not None:
            result_str += f"{sep}timePeriod: {self.time_period}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                session_id=data_dict.get('sessionId'),
                identification_id=data_dict.get('identificationId'),
                is_latest_session=data_dict.get('isLatestSession'),
                time_period=data_dict.get('timePeriod'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class IdentificationDataType: # EEBus_SPINE_TS_Identification.xsd:ns_p:IdentificationDataType -> ComplexType
    def __init__(
            self,
            identification_id: IdentificationIdType = None,
            identification_type: IdentificationTypeType = None,
            identification_value: IdentificationValueType = None,
            authorized: bool = None,
    ):
        super().__init__()
        
        self.identification_id = identification_id
        self.identification_type = identification_type
        self.identification_value = identification_value
        self.authorized = authorized

        if not isinstance(self.identification_id, IdentificationIdType | NoneType):
            raise TypeError("identification_id is not of type IdentificationIdType")
        
        if not isinstance(self.identification_type, IdentificationTypeType | NoneType):
            raise TypeError("identification_type is not of type IdentificationTypeType")
        
        if not isinstance(self.identification_value, IdentificationValueType | NoneType):
            raise TypeError("identification_value is not of type IdentificationValueType")
        
        if not isinstance(self.authorized, bool | NoneType):
            raise TypeError("authorized is not of type bool")
        
    def get_data(self):

        msg_data = []
        
        if self.identification_id is not None:
            msg_data.append({"identificationId": self.identification_id.get_data()})
        if self.identification_type is not None:
            msg_data.append({"identificationType": self.identification_type.get_data()})
        if self.identification_value is not None:
            msg_data.append({"identificationValue": self.identification_value.get_data()})
        if self.authorized is not None:
            msg_data.append({"authorized": self.authorized})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.identification_id is not None:
            result_str += f"{sep}identificationId: {self.identification_id}"
            sep = ", "
        if self.identification_type is not None:
            result_str += f"{sep}identificationType: {self.identification_type}"
            sep = ", "
        if self.identification_value is not None:
            result_str += f"{sep}identificationValue: {self.identification_value}"
            sep = ", "
        if self.authorized is not None:
            result_str += f"{sep}authorized: {self.authorized}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                identification_id=data_dict.get('identificationId'),
                identification_type=data_dict.get('identificationType'),
                identification_value=data_dict.get('identificationValue'),
                authorized=data_dict.get('authorized'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class SessionMeasurementRelationListDataType: # EEBus_SPINE_TS_Identification.xsd:ns_p:SessionMeasurementRelationListDataType -> ComplexType
    def __init__(
            self,
            session_measurement_relation_data: list[SessionMeasurementRelationDataType] = None,
    ):
        super().__init__()
        
        self.session_measurement_relation_data = session_measurement_relation_data

        if not isinstance(self.session_measurement_relation_data, list | NoneType):
            raise TypeError("session_measurement_relation_data is not of type list[SessionMeasurementRelationDataType]")
        
    def get_data(self):

        msg_data = []
        
        if self.session_measurement_relation_data is not None:
            msg_data.append({"sessionMeasurementRelationData": [d.get_data() for d in self.session_measurement_relation_data]})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.session_measurement_relation_data is not None:
            result_str += f"{sep}sessionMeasurementRelationData: {self.session_measurement_relation_data}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                session_measurement_relation_data=data_dict.get('sessionMeasurementRelationData'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class SessionIdentificationListDataType: # EEBus_SPINE_TS_Identification.xsd:ns_p:SessionIdentificationListDataType -> ComplexType
    def __init__(
            self,
            session_identification_data: list[SessionIdentificationDataType] = None,
    ):
        super().__init__()
        
        self.session_identification_data = session_identification_data

        if not isinstance(self.session_identification_data, list | NoneType):
            raise TypeError("session_identification_data is not of type list[SessionIdentificationDataType]")
        
    def get_data(self):

        msg_data = []
        
        if self.session_identification_data is not None:
            msg_data.append({"sessionIdentificationData": [d.get_data() for d in self.session_identification_data]})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.session_identification_data is not None:
            result_str += f"{sep}sessionIdentificationData: {self.session_identification_data}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                session_identification_data=data_dict.get('sessionIdentificationData'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class IdentificationListDataType: # EEBus_SPINE_TS_Identification.xsd:ns_p:IdentificationListDataType -> ComplexType
    def __init__(
            self,
            identification_data: list[IdentificationDataType] = None,
    ):
        super().__init__()
        
        self.identification_data = identification_data

        if not isinstance(self.identification_data, list | NoneType):
            raise TypeError("identification_data is not of type list[IdentificationDataType]")
        
    def get_data(self):

        msg_data = []
        
        if self.identification_data is not None:
            msg_data.append({"identificationData": [d.get_data() for d in self.identification_data]})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.identification_data is not None:
            result_str += f"{sep}identificationData: {self.identification_data}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                identification_data=data_dict.get('identificationData'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class SessionMeasurementRelationDataElementsType: # EEBus_SPINE_TS_Identification.xsd:ns_p:SessionMeasurementRelationDataElementsType -> ComplexType
    def __init__(
            self,
            session_id: ElementTagType = None,
            measurement_id: ElementTagType = None,
    ):
        super().__init__()
        
        self.session_id = session_id
        self.measurement_id = measurement_id

        if not isinstance(self.session_id, ElementTagType | NoneType):
            raise TypeError("session_id is not of type ElementTagType")
        
        if not isinstance(self.measurement_id, ElementTagType | NoneType):
            raise TypeError("measurement_id is not of type ElementTagType")
        
    def get_data(self):

        msg_data = []
        
        if self.session_id is not None:
            msg_data.append({"sessionId": self.session_id.get_data()})
        if self.measurement_id is not None:
            msg_data.append({"measurementId": self.measurement_id.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.session_id is not None:
            result_str += f"{sep}sessionId: {self.session_id}"
            sep = ", "
        if self.measurement_id is not None:
            result_str += f"{sep}measurementId: {self.measurement_id}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                session_id=data_dict.get('sessionId'),
                measurement_id=data_dict.get('measurementId'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class SessionIdentificationDataElementsType: # EEBus_SPINE_TS_Identification.xsd:ns_p:SessionIdentificationDataElementsType -> ComplexType
    def __init__(
            self,
            session_id: ElementTagType = None,
            identification_id: ElementTagType = None,
            is_latest_session: ElementTagType = None,
            time_period: TimePeriodElementsType = None,
    ):
        super().__init__()
        
        self.session_id = session_id
        self.identification_id = identification_id
        self.is_latest_session = is_latest_session
        self.time_period = time_period

        if not isinstance(self.session_id, ElementTagType | NoneType):
            raise TypeError("session_id is not of type ElementTagType")
        
        if not isinstance(self.identification_id, ElementTagType | NoneType):
            raise TypeError("identification_id is not of type ElementTagType")
        
        if not isinstance(self.is_latest_session, ElementTagType | NoneType):
            raise TypeError("is_latest_session is not of type ElementTagType")
        
        if not isinstance(self.time_period, TimePeriodElementsType | NoneType):
            raise TypeError("time_period is not of type TimePeriodElementsType")
        
    def get_data(self):

        msg_data = []
        
        if self.session_id is not None:
            msg_data.append({"sessionId": self.session_id.get_data()})
        if self.identification_id is not None:
            msg_data.append({"identificationId": self.identification_id.get_data()})
        if self.is_latest_session is not None:
            msg_data.append({"isLatestSession": self.is_latest_session.get_data()})
        if self.time_period is not None:
            msg_data.append({"timePeriod": self.time_period.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.session_id is not None:
            result_str += f"{sep}sessionId: {self.session_id}"
            sep = ", "
        if self.identification_id is not None:
            result_str += f"{sep}identificationId: {self.identification_id}"
            sep = ", "
        if self.is_latest_session is not None:
            result_str += f"{sep}isLatestSession: {self.is_latest_session}"
            sep = ", "
        if self.time_period is not None:
            result_str += f"{sep}timePeriod: {self.time_period}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                session_id=data_dict.get('sessionId'),
                identification_id=data_dict.get('identificationId'),
                is_latest_session=data_dict.get('isLatestSession'),
                time_period=data_dict.get('timePeriod'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class IdentificationDataElementsType: # EEBus_SPINE_TS_Identification.xsd:ns_p:IdentificationDataElementsType -> ComplexType
    def __init__(
            self,
            identification_id: ElementTagType = None,
            identification_type: ElementTagType = None,
            identification_value: ElementTagType = None,
            authorized: ElementTagType = None,
    ):
        super().__init__()
        
        self.identification_id = identification_id
        self.identification_type = identification_type
        self.identification_value = identification_value
        self.authorized = authorized

        if not isinstance(self.identification_id, ElementTagType | NoneType):
            raise TypeError("identification_id is not of type ElementTagType")
        
        if not isinstance(self.identification_type, ElementTagType | NoneType):
            raise TypeError("identification_type is not of type ElementTagType")
        
        if not isinstance(self.identification_value, ElementTagType | NoneType):
            raise TypeError("identification_value is not of type ElementTagType")
        
        if not isinstance(self.authorized, ElementTagType | NoneType):
            raise TypeError("authorized is not of type ElementTagType")
        
    def get_data(self):

        msg_data = []
        
        if self.identification_id is not None:
            msg_data.append({"identificationId": self.identification_id.get_data()})
        if self.identification_type is not None:
            msg_data.append({"identificationType": self.identification_type.get_data()})
        if self.identification_value is not None:
            msg_data.append({"identificationValue": self.identification_value.get_data()})
        if self.authorized is not None:
            msg_data.append({"authorized": self.authorized.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.identification_id is not None:
            result_str += f"{sep}identificationId: {self.identification_id}"
            sep = ", "
        if self.identification_type is not None:
            result_str += f"{sep}identificationType: {self.identification_type}"
            sep = ", "
        if self.identification_value is not None:
            result_str += f"{sep}identificationValue: {self.identification_value}"
            sep = ", "
        if self.authorized is not None:
            result_str += f"{sep}authorized: {self.authorized}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                identification_id=data_dict.get('identificationId'),
                identification_type=data_dict.get('identificationType'),
                identification_value=data_dict.get('identificationValue'),
                authorized=data_dict.get('authorized'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class SessionMeasurementRelationListDataSelectorsType: # EEBus_SPINE_TS_Identification.xsd:ns_p:SessionMeasurementRelationListDataSelectorsType -> ComplexType
    def __init__(
            self,
            session_id: SessionIdType = None,
            measurement_id: MeasurementIdType = None,
    ):
        super().__init__()
        
        self.session_id = session_id
        self.measurement_id = measurement_id

        if not isinstance(self.session_id, SessionIdType | NoneType):
            raise TypeError("session_id is not of type SessionIdType")
        
        if not isinstance(self.measurement_id, MeasurementIdType | NoneType):
            raise TypeError("measurement_id is not of type MeasurementIdType")
        
    def get_data(self):

        msg_data = []
        
        if self.session_id is not None:
            msg_data.append({"sessionId": self.session_id.get_data()})
        if self.measurement_id is not None:
            msg_data.append({"measurementId": self.measurement_id.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.session_id is not None:
            result_str += f"{sep}sessionId: {self.session_id}"
            sep = ", "
        if self.measurement_id is not None:
            result_str += f"{sep}measurementId: {self.measurement_id}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                session_id=data_dict.get('sessionId'),
                measurement_id=data_dict.get('measurementId'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class SessionIdentificationListDataSelectorsType: # EEBus_SPINE_TS_Identification.xsd:ns_p:SessionIdentificationListDataSelectorsType -> ComplexType
    def __init__(
            self,
            session_id: SessionIdType = None,
            identification_id: IdentificationIdType = None,
            is_latest_session: bool = None,
            time_period: TimePeriodType = None,
    ):
        super().__init__()
        
        self.session_id = session_id
        self.identification_id = identification_id
        self.is_latest_session = is_latest_session
        self.time_period = time_period

        if not isinstance(self.session_id, SessionIdType | NoneType):
            raise TypeError("session_id is not of type SessionIdType")
        
        if not isinstance(self.identification_id, IdentificationIdType | NoneType):
            raise TypeError("identification_id is not of type IdentificationIdType")
        
        if not isinstance(self.is_latest_session, bool | NoneType):
            raise TypeError("is_latest_session is not of type bool")
        
        if not isinstance(self.time_period, TimePeriodType | NoneType):
            raise TypeError("time_period is not of type TimePeriodType")
        
    def get_data(self):

        msg_data = []
        
        if self.session_id is not None:
            msg_data.append({"sessionId": self.session_id.get_data()})
        if self.identification_id is not None:
            msg_data.append({"identificationId": self.identification_id.get_data()})
        if self.is_latest_session is not None:
            msg_data.append({"isLatestSession": self.is_latest_session})
        if self.time_period is not None:
            msg_data.append({"timePeriod": self.time_period.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.session_id is not None:
            result_str += f"{sep}sessionId: {self.session_id}"
            sep = ", "
        if self.identification_id is not None:
            result_str += f"{sep}identificationId: {self.identification_id}"
            sep = ", "
        if self.is_latest_session is not None:
            result_str += f"{sep}isLatestSession: {self.is_latest_session}"
            sep = ", "
        if self.time_period is not None:
            result_str += f"{sep}timePeriod: {self.time_period}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                session_id=data_dict.get('sessionId'),
                identification_id=data_dict.get('identificationId'),
                is_latest_session=data_dict.get('isLatestSession'),
                time_period=data_dict.get('timePeriod'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class IdentificationListDataSelectorsType: # EEBus_SPINE_TS_Identification.xsd:ns_p:IdentificationListDataSelectorsType -> ComplexType
    def __init__(
            self,
            identification_id: IdentificationIdType = None,
            identification_type: IdentificationTypeType = None,
    ):
        super().__init__()
        
        self.identification_id = identification_id
        self.identification_type = identification_type

        if not isinstance(self.identification_id, IdentificationIdType | NoneType):
            raise TypeError("identification_id is not of type IdentificationIdType")
        
        if not isinstance(self.identification_type, IdentificationTypeType | NoneType):
            raise TypeError("identification_type is not of type IdentificationTypeType")
        
    def get_data(self):

        msg_data = []
        
        if self.identification_id is not None:
            msg_data.append({"identificationId": self.identification_id.get_data()})
        if self.identification_type is not None:
            msg_data.append({"identificationType": self.identification_type.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.identification_id is not None:
            result_str += f"{sep}identificationId: {self.identification_id}"
            sep = ", "
        if self.identification_type is not None:
            result_str += f"{sep}identificationType: {self.identification_type}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                identification_id=data_dict.get('identificationId'),
                identification_type=data_dict.get('identificationType'),
            )
        elif data:
            return cls(data)
        else:
            return cls()



