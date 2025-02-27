# Jinja Template message_type.py.jinja2
from spine.simple_type.bill import BillIdType
from spine.base_type.commondatatypes import ElementTagType
from spine.simple_type.bill import BillPositionCountType
from spine.union_type.commondatatypes import FunctionType
from spine.simple_type.identification import SessionIdType
from types import NoneType
from spine import array_2_dict


class BillDataType:
    def __init__(
            self,
            bill_id: BillIdType = None,
            bill_type: FunctionType = None,
            scope_type: FunctionType = None,
    ):
        super().__init__()
        
        self.bill_id = bill_id
        self.bill_type = bill_type
        self.scope_type = scope_type

        if not isinstance(self.bill_id, BillIdType | NoneType):
            raise TypeError("bill_id is not of type BillIdType")
        
        if not isinstance(self.bill_type, FunctionType | NoneType):
            raise TypeError("bill_type is not of type FunctionType")
        
        if not isinstance(self.scope_type, FunctionType | NoneType):
            raise TypeError("scope_type is not of type FunctionType")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.bill_id is not None:
            msg_data.append({"billId": self.bill_id.get_data()})
        if self.bill_type is not None:
            msg_data.append({"billType": self.bill_type.get_data()})
        if self.scope_type is not None:
            msg_data.append({"scopeType": self.scope_type.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.bill_id is not None:
            result_str += f"{sep}billId: {self.bill_id}"
            sep = ", "
        if self.bill_type is not None:
            result_str += f"{sep}billType: {self.bill_type}"
            sep = ", "
        if self.scope_type is not None:
            result_str += f"{sep}scopeType: {self.scope_type}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                bill_id=data_dict.get('billId'),
                bill_type=data_dict.get('billType'),
                scope_type=data_dict.get('scopeType'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class BillDescriptionDataType:
    def __init__(
            self,
            bill_id: BillIdType = None,
            bill_writeable: bool = None,
            update_required: bool = None,
            supported_bill_type: list[FunctionType] = None,
            session_id: SessionIdType = None,
    ):
        super().__init__()
        
        self.bill_id = bill_id
        self.bill_writeable = bill_writeable
        self.update_required = update_required
        self.supported_bill_type = supported_bill_type
        self.session_id = session_id

        if not isinstance(self.bill_id, BillIdType | NoneType):
            raise TypeError("bill_id is not of type BillIdType")
        
        if not isinstance(self.bill_writeable, bool | NoneType):
            raise TypeError("bill_writeable is not of type bool")
        
        if not isinstance(self.update_required, bool | NoneType):
            raise TypeError("update_required is not of type bool")
        
        if not isinstance(self.supported_bill_type, list | NoneType):
            raise TypeError("supported_bill_type is not of type list[FunctionType]")
        
        if not isinstance(self.session_id, SessionIdType | NoneType):
            raise TypeError("session_id is not of type SessionIdType")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.bill_id is not None:
            msg_data.append({"billId": self.bill_id.get_data()})
        if self.bill_writeable is not None:
            msg_data.append({"billWriteable": self.bill_writeable})
        if self.update_required is not None:
            msg_data.append({"updateRequired": self.update_required})
        if self.supported_bill_type is not None:
            msg_data.append({"supportedBillType": [d.get_data() for d in self.supported_bill_type]})
        if self.session_id is not None:
            msg_data.append({"sessionId": self.session_id.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.bill_id is not None:
            result_str += f"{sep}billId: {self.bill_id}"
            sep = ", "
        if self.bill_writeable is not None:
            result_str += f"{sep}billWriteable: {self.bill_writeable}"
            sep = ", "
        if self.update_required is not None:
            result_str += f"{sep}updateRequired: {self.update_required}"
            sep = ", "
        if self.supported_bill_type is not None:
            result_str += f"{sep}supportedBillType: {self.supported_bill_type}"
            sep = ", "
        if self.session_id is not None:
            result_str += f"{sep}sessionId: {self.session_id}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                bill_id=data_dict.get('billId'),
                bill_writeable=data_dict.get('billWriteable'),
                update_required=data_dict.get('updateRequired'),
                supported_bill_type=data_dict.get('supportedBillType'),
                session_id=data_dict.get('sessionId'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class BillConstraintsDataType:
    def __init__(
            self,
            bill_id: BillIdType = None,
            position_count_min: BillPositionCountType = None,
            position_count_max: BillPositionCountType = None,
    ):
        super().__init__()
        
        self.bill_id = bill_id
        self.position_count_min = position_count_min
        self.position_count_max = position_count_max

        if not isinstance(self.bill_id, BillIdType | NoneType):
            raise TypeError("bill_id is not of type BillIdType")
        
        if not isinstance(self.position_count_min, BillPositionCountType | NoneType):
            raise TypeError("position_count_min is not of type BillPositionCountType")
        
        if not isinstance(self.position_count_max, BillPositionCountType | NoneType):
            raise TypeError("position_count_max is not of type BillPositionCountType")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.bill_id is not None:
            msg_data.append({"billId": self.bill_id.get_data()})
        if self.position_count_min is not None:
            msg_data.append({"positionCountMin": self.position_count_min.get_data()})
        if self.position_count_max is not None:
            msg_data.append({"positionCountMax": self.position_count_max.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.bill_id is not None:
            result_str += f"{sep}billId: {self.bill_id}"
            sep = ", "
        if self.position_count_min is not None:
            result_str += f"{sep}positionCountMin: {self.position_count_min}"
            sep = ", "
        if self.position_count_max is not None:
            result_str += f"{sep}positionCountMax: {self.position_count_max}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                bill_id=data_dict.get('billId'),
                position_count_min=data_dict.get('positionCountMin'),
                position_count_max=data_dict.get('positionCountMax'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class BillListDataType:
    def __init__(
            self,
            bill_data: list[BillDataType] = None,
    ):
        super().__init__()
        
        self.bill_data = bill_data

        if not isinstance(self.bill_data, list | NoneType):
            raise TypeError("bill_data is not of type list[BillDataType]")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.bill_data is not None:
            msg_data.append({"billData": [d.get_data() for d in self.bill_data]})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.bill_data is not None:
            result_str += f"{sep}billData: {self.bill_data}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                bill_data=data_dict.get('billData'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class BillListDataSelectorsType:
    def __init__(
            self,
            bill_id: BillIdType = None,
            scope_type: FunctionType = None,
    ):
        super().__init__()
        
        self.bill_id = bill_id
        self.scope_type = scope_type

        if not isinstance(self.bill_id, BillIdType | NoneType):
            raise TypeError("bill_id is not of type BillIdType")
        
        if not isinstance(self.scope_type, FunctionType | NoneType):
            raise TypeError("scope_type is not of type FunctionType")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.bill_id is not None:
            msg_data.append({"billId": self.bill_id.get_data()})
        if self.scope_type is not None:
            msg_data.append({"scopeType": self.scope_type.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.bill_id is not None:
            result_str += f"{sep}billId: {self.bill_id}"
            sep = ", "
        if self.scope_type is not None:
            result_str += f"{sep}scopeType: {self.scope_type}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                bill_id=data_dict.get('billId'),
                scope_type=data_dict.get('scopeType'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class BillDescriptionListDataType:
    def __init__(
            self,
            bill_description_data: list[BillDescriptionDataType] = None,
    ):
        super().__init__()
        
        self.bill_description_data = bill_description_data

        if not isinstance(self.bill_description_data, list | NoneType):
            raise TypeError("bill_description_data is not of type list[BillDescriptionDataType]")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.bill_description_data is not None:
            msg_data.append({"billDescriptionData": [d.get_data() for d in self.bill_description_data]})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.bill_description_data is not None:
            result_str += f"{sep}billDescriptionData: {self.bill_description_data}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                bill_description_data=data_dict.get('billDescriptionData'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class BillDescriptionListDataSelectorsType:
    def __init__(
            self,
            bill_id: BillIdType = None,
    ):
        super().__init__()
        
        self.bill_id = bill_id

        if not isinstance(self.bill_id, BillIdType | NoneType):
            raise TypeError("bill_id is not of type BillIdType")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.bill_id is not None:
            msg_data.append({"billId": self.bill_id.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.bill_id is not None:
            result_str += f"{sep}billId: {self.bill_id}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                bill_id=data_dict.get('billId'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class BillDescriptionDataElementsType:
    def __init__(
            self,
            bill_id: ElementTagType = None,
            bill_writeable: ElementTagType = None,
            update_required: ElementTagType = None,
            supported_bill_type: ElementTagType = None,
            session_id: ElementTagType = None,
    ):
        super().__init__()
        
        self.bill_id = bill_id
        self.bill_writeable = bill_writeable
        self.update_required = update_required
        self.supported_bill_type = supported_bill_type
        self.session_id = session_id

        if not isinstance(self.bill_id, ElementTagType | NoneType):
            raise TypeError("bill_id is not of type ElementTagType")
        
        if not isinstance(self.bill_writeable, ElementTagType | NoneType):
            raise TypeError("bill_writeable is not of type ElementTagType")
        
        if not isinstance(self.update_required, ElementTagType | NoneType):
            raise TypeError("update_required is not of type ElementTagType")
        
        if not isinstance(self.supported_bill_type, ElementTagType | NoneType):
            raise TypeError("supported_bill_type is not of type ElementTagType")
        
        if not isinstance(self.session_id, ElementTagType | NoneType):
            raise TypeError("session_id is not of type ElementTagType")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.bill_id is not None:
            msg_data.append({"billId": self.bill_id.get_data()})
        if self.bill_writeable is not None:
            msg_data.append({"billWriteable": self.bill_writeable.get_data()})
        if self.update_required is not None:
            msg_data.append({"updateRequired": self.update_required.get_data()})
        if self.supported_bill_type is not None:
            msg_data.append({"supportedBillType": self.supported_bill_type.get_data()})
        if self.session_id is not None:
            msg_data.append({"sessionId": self.session_id.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.bill_id is not None:
            result_str += f"{sep}billId: {self.bill_id}"
            sep = ", "
        if self.bill_writeable is not None:
            result_str += f"{sep}billWriteable: {self.bill_writeable}"
            sep = ", "
        if self.update_required is not None:
            result_str += f"{sep}updateRequired: {self.update_required}"
            sep = ", "
        if self.supported_bill_type is not None:
            result_str += f"{sep}supportedBillType: {self.supported_bill_type}"
            sep = ", "
        if self.session_id is not None:
            result_str += f"{sep}sessionId: {self.session_id}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                bill_id=data_dict.get('billId'),
                bill_writeable=data_dict.get('billWriteable'),
                update_required=data_dict.get('updateRequired'),
                supported_bill_type=data_dict.get('supportedBillType'),
                session_id=data_dict.get('sessionId'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class BillDataElementsType:
    def __init__(
            self,
            bill_id: ElementTagType = None,
            bill_type: ElementTagType = None,
            scope_type: ElementTagType = None,
    ):
        super().__init__()
        
        self.bill_id = bill_id
        self.bill_type = bill_type
        self.scope_type = scope_type

        if not isinstance(self.bill_id, ElementTagType | NoneType):
            raise TypeError("bill_id is not of type ElementTagType")
        
        if not isinstance(self.bill_type, ElementTagType | NoneType):
            raise TypeError("bill_type is not of type ElementTagType")
        
        if not isinstance(self.scope_type, ElementTagType | NoneType):
            raise TypeError("scope_type is not of type ElementTagType")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.bill_id is not None:
            msg_data.append({"billId": self.bill_id.get_data()})
        if self.bill_type is not None:
            msg_data.append({"billType": self.bill_type.get_data()})
        if self.scope_type is not None:
            msg_data.append({"scopeType": self.scope_type.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.bill_id is not None:
            result_str += f"{sep}billId: {self.bill_id}"
            sep = ", "
        if self.bill_type is not None:
            result_str += f"{sep}billType: {self.bill_type}"
            sep = ", "
        if self.scope_type is not None:
            result_str += f"{sep}scopeType: {self.scope_type}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                bill_id=data_dict.get('billId'),
                bill_type=data_dict.get('billType'),
                scope_type=data_dict.get('scopeType'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class BillConstraintsListDataType:
    def __init__(
            self,
            bill_constraints_data: list[BillConstraintsDataType] = None,
    ):
        super().__init__()
        
        self.bill_constraints_data = bill_constraints_data

        if not isinstance(self.bill_constraints_data, list | NoneType):
            raise TypeError("bill_constraints_data is not of type list[BillConstraintsDataType]")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.bill_constraints_data is not None:
            msg_data.append({"billConstraintsData": [d.get_data() for d in self.bill_constraints_data]})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.bill_constraints_data is not None:
            result_str += f"{sep}billConstraintsData: {self.bill_constraints_data}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                bill_constraints_data=data_dict.get('billConstraintsData'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class BillConstraintsListDataSelectorsType:
    def __init__(
            self,
            bill_id: BillIdType = None,
    ):
        super().__init__()
        
        self.bill_id = bill_id

        if not isinstance(self.bill_id, BillIdType | NoneType):
            raise TypeError("bill_id is not of type BillIdType")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.bill_id is not None:
            msg_data.append({"billId": self.bill_id.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.bill_id is not None:
            result_str += f"{sep}billId: {self.bill_id}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                bill_id=data_dict.get('billId'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class BillConstraintsDataElementsType:
    def __init__(
            self,
            bill_id: ElementTagType = None,
            position_count_min: ElementTagType = None,
            position_count_max: ElementTagType = None,
    ):
        super().__init__()
        
        self.bill_id = bill_id
        self.position_count_min = position_count_min
        self.position_count_max = position_count_max

        if not isinstance(self.bill_id, ElementTagType | NoneType):
            raise TypeError("bill_id is not of type ElementTagType")
        
        if not isinstance(self.position_count_min, ElementTagType | NoneType):
            raise TypeError("position_count_min is not of type ElementTagType")
        
        if not isinstance(self.position_count_max, ElementTagType | NoneType):
            raise TypeError("position_count_max is not of type ElementTagType")
        
    def get_data(self): # ComplexType

        msg_data = []
        
        if self.bill_id is not None:
            msg_data.append({"billId": self.bill_id.get_data()})
        if self.position_count_min is not None:
            msg_data.append({"positionCountMin": self.position_count_min.get_data()})
        if self.position_count_max is not None:
            msg_data.append({"positionCountMax": self.position_count_max.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.bill_id is not None:
            result_str += f"{sep}billId: {self.bill_id}"
            sep = ", "
        if self.position_count_min is not None:
            result_str += f"{sep}positionCountMin: {self.position_count_min}"
            sep = ", "
        if self.position_count_max is not None:
            result_str += f"{sep}positionCountMax: {self.position_count_max}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                bill_id=data_dict.get('billId'),
                position_count_min=data_dict.get('positionCountMin'),
                position_count_max=data_dict.get('positionCountMax'),
            )
        elif data:
            return cls(data)
        else:
            return cls()



