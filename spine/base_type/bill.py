# Jinja Template message_type.py.jinja2
from spine.base_type.commondatatypes import ElementTagType
from spine.base_type.commondatatypes import ScaledNumberElementsType
from spine.base_type.commondatatypes import ScaledNumberType
from spine.base_type.commondatatypes import TimePeriodElementsType
from spine.base_type.commondatatypes import TimePeriodType
from spine.simple_type.bill import BillCostIdType
from spine.simple_type.bill import BillIdType
from spine.simple_type.bill import BillPositionCountType
from spine.simple_type.bill import BillPositionIdType
from spine.simple_type.bill import BillValueIdType
from spine.simple_type.commondatatypes import DescriptionType
from spine.simple_type.commondatatypes import LabelType
from spine.simple_type.identification import SessionIdType
from spine.union_type.bill import BillCostTypeType
from spine.union_type.bill import BillPositionTypeType
from spine.union_type.bill import BillTypeType
from spine.union_type.commondatatypes import CurrencyType
from spine.union_type.commondatatypes import ScopeTypeType
from spine.union_type.commondatatypes import UnitOfMeasurementType
from types import NoneType
from spine import array_2_dict


class BillCostElementsType: # EEBus_SPINE_TS_Bill.xsd:ns_p:BillCostElementsType -> ComplexType
    def __init__(
            self,
            cost_id: ElementTagType = None,
            cost_type: ElementTagType = None,
            value_id: ElementTagType = None,
            unit: ElementTagType = None,
            currency: ElementTagType = None,
            cost: ScaledNumberElementsType = None,
            cost_percentage: ScaledNumberElementsType = None,
    ):
        super().__init__()
        
        self.cost_id = cost_id
        self.cost_type = cost_type
        self.value_id = value_id
        self.unit = unit
        self.currency = currency
        self.cost = cost
        self.cost_percentage = cost_percentage

        if not isinstance(self.cost_id, ElementTagType | NoneType):
            raise TypeError("cost_id is not of type ElementTagType")
        
        if not isinstance(self.cost_type, ElementTagType | NoneType):
            raise TypeError("cost_type is not of type ElementTagType")
        
        if not isinstance(self.value_id, ElementTagType | NoneType):
            raise TypeError("value_id is not of type ElementTagType")
        
        if not isinstance(self.unit, ElementTagType | NoneType):
            raise TypeError("unit is not of type ElementTagType")
        
        if not isinstance(self.currency, ElementTagType | NoneType):
            raise TypeError("currency is not of type ElementTagType")
        
        if not isinstance(self.cost, ScaledNumberElementsType | NoneType):
            raise TypeError("cost is not of type ScaledNumberElementsType")
        
        if not isinstance(self.cost_percentage, ScaledNumberElementsType | NoneType):
            raise TypeError("cost_percentage is not of type ScaledNumberElementsType")
        
    def get_data(self):

        msg_data = []
        
        if self.cost_id is not None:
            msg_data.append({"costId": self.cost_id.get_data()})
        if self.cost_type is not None:
            msg_data.append({"costType": self.cost_type.get_data()})
        if self.value_id is not None:
            msg_data.append({"valueId": self.value_id.get_data()})
        if self.unit is not None:
            msg_data.append({"unit": self.unit.get_data()})
        if self.currency is not None:
            msg_data.append({"currency": self.currency.get_data()})
        if self.cost is not None:
            msg_data.append({"cost": self.cost.get_data()})
        if self.cost_percentage is not None:
            msg_data.append({"costPercentage": self.cost_percentage.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.cost_id is not None:
            result_str += f"{sep}costId: {self.cost_id}"
            sep = ", "
        if self.cost_type is not None:
            result_str += f"{sep}costType: {self.cost_type}"
            sep = ", "
        if self.value_id is not None:
            result_str += f"{sep}valueId: {self.value_id}"
            sep = ", "
        if self.unit is not None:
            result_str += f"{sep}unit: {self.unit}"
            sep = ", "
        if self.currency is not None:
            result_str += f"{sep}currency: {self.currency}"
            sep = ", "
        if self.cost is not None:
            result_str += f"{sep}cost: {self.cost}"
            sep = ", "
        if self.cost_percentage is not None:
            result_str += f"{sep}costPercentage: {self.cost_percentage}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                cost_id=data_dict.get('costId'),
                cost_type=data_dict.get('costType'),
                value_id=data_dict.get('valueId'),
                unit=data_dict.get('unit'),
                currency=data_dict.get('currency'),
                cost=data_dict.get('cost'),
                cost_percentage=data_dict.get('costPercentage'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class BillValueElementsType: # EEBus_SPINE_TS_Bill.xsd:ns_p:BillValueElementsType -> ComplexType
    def __init__(
            self,
            value_id: ElementTagType = None,
            unit: ElementTagType = None,
            value: ScaledNumberElementsType = None,
            value_percentage: ScaledNumberElementsType = None,
    ):
        super().__init__()
        
        self.value_id = value_id
        self.unit = unit
        self.value = value
        self.value_percentage = value_percentage

        if not isinstance(self.value_id, ElementTagType | NoneType):
            raise TypeError("value_id is not of type ElementTagType")
        
        if not isinstance(self.unit, ElementTagType | NoneType):
            raise TypeError("unit is not of type ElementTagType")
        
        if not isinstance(self.value, ScaledNumberElementsType | NoneType):
            raise TypeError("value is not of type ScaledNumberElementsType")
        
        if not isinstance(self.value_percentage, ScaledNumberElementsType | NoneType):
            raise TypeError("value_percentage is not of type ScaledNumberElementsType")
        
    def get_data(self):

        msg_data = []
        
        if self.value_id is not None:
            msg_data.append({"valueId": self.value_id.get_data()})
        if self.unit is not None:
            msg_data.append({"unit": self.unit.get_data()})
        if self.value is not None:
            msg_data.append({"value": self.value.get_data()})
        if self.value_percentage is not None:
            msg_data.append({"valuePercentage": self.value_percentage.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.value_id is not None:
            result_str += f"{sep}valueId: {self.value_id}"
            sep = ", "
        if self.unit is not None:
            result_str += f"{sep}unit: {self.unit}"
            sep = ", "
        if self.value is not None:
            result_str += f"{sep}value: {self.value}"
            sep = ", "
        if self.value_percentage is not None:
            result_str += f"{sep}valuePercentage: {self.value_percentage}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                value_id=data_dict.get('valueId'),
                unit=data_dict.get('unit'),
                value=data_dict.get('value'),
                value_percentage=data_dict.get('valuePercentage'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class BillCostType: # EEBus_SPINE_TS_Bill.xsd:ns_p:BillCostType -> ComplexType
    def __init__(
            self,
            cost_id: BillCostIdType = None,
            cost_type: BillCostTypeType = None,
            value_id: BillValueIdType = None,
            unit: UnitOfMeasurementType = None,
            currency: CurrencyType = None,
            cost: ScaledNumberType = None,
            cost_percentage: ScaledNumberType = None,
    ):
        super().__init__()
        
        self.cost_id = cost_id
        self.cost_type = cost_type
        self.value_id = value_id
        self.unit = unit
        self.currency = currency
        self.cost = cost
        self.cost_percentage = cost_percentage

        if not isinstance(self.cost_id, BillCostIdType | NoneType):
            raise TypeError("cost_id is not of type BillCostIdType")
        
        if not isinstance(self.cost_type, BillCostTypeType | NoneType):
            raise TypeError("cost_type is not of type BillCostTypeType")
        
        if not isinstance(self.value_id, BillValueIdType | NoneType):
            raise TypeError("value_id is not of type BillValueIdType")
        
        if not isinstance(self.unit, UnitOfMeasurementType | NoneType):
            raise TypeError("unit is not of type UnitOfMeasurementType")
        
        if not isinstance(self.currency, CurrencyType | NoneType):
            raise TypeError("currency is not of type CurrencyType")
        
        if not isinstance(self.cost, ScaledNumberType | NoneType):
            raise TypeError("cost is not of type ScaledNumberType")
        
        if not isinstance(self.cost_percentage, ScaledNumberType | NoneType):
            raise TypeError("cost_percentage is not of type ScaledNumberType")
        
    def get_data(self):

        msg_data = []
        
        if self.cost_id is not None:
            msg_data.append({"costId": self.cost_id.get_data()})
        if self.cost_type is not None:
            msg_data.append({"costType": self.cost_type.get_data()})
        if self.value_id is not None:
            msg_data.append({"valueId": self.value_id.get_data()})
        if self.unit is not None:
            msg_data.append({"unit": self.unit.get_data()})
        if self.currency is not None:
            msg_data.append({"currency": self.currency.get_data()})
        if self.cost is not None:
            msg_data.append({"cost": self.cost.get_data()})
        if self.cost_percentage is not None:
            msg_data.append({"costPercentage": self.cost_percentage.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.cost_id is not None:
            result_str += f"{sep}costId: {self.cost_id}"
            sep = ", "
        if self.cost_type is not None:
            result_str += f"{sep}costType: {self.cost_type}"
            sep = ", "
        if self.value_id is not None:
            result_str += f"{sep}valueId: {self.value_id}"
            sep = ", "
        if self.unit is not None:
            result_str += f"{sep}unit: {self.unit}"
            sep = ", "
        if self.currency is not None:
            result_str += f"{sep}currency: {self.currency}"
            sep = ", "
        if self.cost is not None:
            result_str += f"{sep}cost: {self.cost}"
            sep = ", "
        if self.cost_percentage is not None:
            result_str += f"{sep}costPercentage: {self.cost_percentage}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                cost_id=data_dict.get('costId'),
                cost_type=data_dict.get('costType'),
                value_id=data_dict.get('valueId'),
                unit=data_dict.get('unit'),
                currency=data_dict.get('currency'),
                cost=data_dict.get('cost'),
                cost_percentage=data_dict.get('costPercentage'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class BillValueType: # EEBus_SPINE_TS_Bill.xsd:ns_p:BillValueType -> ComplexType
    def __init__(
            self,
            value_id: BillValueIdType = None,
            unit: UnitOfMeasurementType = None,
            value: ScaledNumberType = None,
            value_percentage: ScaledNumberType = None,
    ):
        super().__init__()
        
        self.value_id = value_id
        self.unit = unit
        self.value = value
        self.value_percentage = value_percentage

        if not isinstance(self.value_id, BillValueIdType | NoneType):
            raise TypeError("value_id is not of type BillValueIdType")
        
        if not isinstance(self.unit, UnitOfMeasurementType | NoneType):
            raise TypeError("unit is not of type UnitOfMeasurementType")
        
        if not isinstance(self.value, ScaledNumberType | NoneType):
            raise TypeError("value is not of type ScaledNumberType")
        
        if not isinstance(self.value_percentage, ScaledNumberType | NoneType):
            raise TypeError("value_percentage is not of type ScaledNumberType")
        
    def get_data(self):

        msg_data = []
        
        if self.value_id is not None:
            msg_data.append({"valueId": self.value_id.get_data()})
        if self.unit is not None:
            msg_data.append({"unit": self.unit.get_data()})
        if self.value is not None:
            msg_data.append({"value": self.value.get_data()})
        if self.value_percentage is not None:
            msg_data.append({"valuePercentage": self.value_percentage.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.value_id is not None:
            result_str += f"{sep}valueId: {self.value_id}"
            sep = ", "
        if self.unit is not None:
            result_str += f"{sep}unit: {self.unit}"
            sep = ", "
        if self.value is not None:
            result_str += f"{sep}value: {self.value}"
            sep = ", "
        if self.value_percentage is not None:
            result_str += f"{sep}valuePercentage: {self.value_percentage}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                value_id=data_dict.get('valueId'),
                unit=data_dict.get('unit'),
                value=data_dict.get('value'),
                value_percentage=data_dict.get('valuePercentage'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class BillDataType: # EEBus_SPINE_TS_Bill.xsd:ns_p:BillDataType -> ComplexType
    def __init__(
            self,
            bill_id: BillIdType = None,
            bill_type: BillTypeType = None,
            scope_type: ScopeTypeType = None,
    ):
        super().__init__()
        
        self.bill_id = bill_id
        self.bill_type = bill_type
        self.scope_type = scope_type

        if not isinstance(self.bill_id, BillIdType | NoneType):
            raise TypeError("bill_id is not of type BillIdType")
        
        if not isinstance(self.bill_type, BillTypeType | NoneType):
            raise TypeError("bill_type is not of type BillTypeType")
        
        if not isinstance(self.scope_type, ScopeTypeType | NoneType):
            raise TypeError("scope_type is not of type ScopeTypeType")
        
    def get_data(self):

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


class BillDescriptionDataType: # EEBus_SPINE_TS_Bill.xsd:ns_p:BillDescriptionDataType -> ComplexType
    def __init__(
            self,
            bill_id: BillIdType = None,
            bill_writeable: bool = None,
            update_required: bool = None,
            supported_bill_type: list[BillTypeType] = None,
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
            raise TypeError("supported_bill_type is not of type list[BillTypeType]")
        
        if not isinstance(self.session_id, SessionIdType | NoneType):
            raise TypeError("session_id is not of type SessionIdType")
        
    def get_data(self):

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


class BillConstraintsDataType: # EEBus_SPINE_TS_Bill.xsd:ns_p:BillConstraintsDataType -> ComplexType
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
        
    def get_data(self):

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


class BillPositionElementsType: # EEBus_SPINE_TS_Bill.xsd:ns_p:BillPositionElementsType -> ComplexType
    def __init__(
            self,
            position_id: ElementTagType = None,
            position_type: ElementTagType = None,
            time_period: TimePeriodElementsType = None,
            value: BillValueElementsType = None,
            cost: BillCostElementsType = None,
            label: ElementTagType = None,
            description: ElementTagType = None,
    ):
        super().__init__()
        
        self.position_id = position_id
        self.position_type = position_type
        self.time_period = time_period
        self.value = value
        self.cost = cost
        self.label = label
        self.description = description

        if not isinstance(self.position_id, ElementTagType | NoneType):
            raise TypeError("position_id is not of type ElementTagType")
        
        if not isinstance(self.position_type, ElementTagType | NoneType):
            raise TypeError("position_type is not of type ElementTagType")
        
        if not isinstance(self.time_period, TimePeriodElementsType | NoneType):
            raise TypeError("time_period is not of type TimePeriodElementsType")
        
        if not isinstance(self.value, BillValueElementsType | NoneType):
            raise TypeError("value is not of type BillValueElementsType")
        
        if not isinstance(self.cost, BillCostElementsType | NoneType):
            raise TypeError("cost is not of type BillCostElementsType")
        
        if not isinstance(self.label, ElementTagType | NoneType):
            raise TypeError("label is not of type ElementTagType")
        
        if not isinstance(self.description, ElementTagType | NoneType):
            raise TypeError("description is not of type ElementTagType")
        
    def get_data(self):

        msg_data = []
        
        if self.position_id is not None:
            msg_data.append({"positionId": self.position_id.get_data()})
        if self.position_type is not None:
            msg_data.append({"positionType": self.position_type.get_data()})
        if self.time_period is not None:
            msg_data.append({"timePeriod": self.time_period.get_data()})
        if self.value is not None:
            msg_data.append({"value": self.value.get_data()})
        if self.cost is not None:
            msg_data.append({"cost": self.cost.get_data()})
        if self.label is not None:
            msg_data.append({"label": self.label.get_data()})
        if self.description is not None:
            msg_data.append({"description": self.description.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.position_id is not None:
            result_str += f"{sep}positionId: {self.position_id}"
            sep = ", "
        if self.position_type is not None:
            result_str += f"{sep}positionType: {self.position_type}"
            sep = ", "
        if self.time_period is not None:
            result_str += f"{sep}timePeriod: {self.time_period}"
            sep = ", "
        if self.value is not None:
            result_str += f"{sep}value: {self.value}"
            sep = ", "
        if self.cost is not None:
            result_str += f"{sep}cost: {self.cost}"
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
                position_id=data_dict.get('positionId'),
                position_type=data_dict.get('positionType'),
                time_period=data_dict.get('timePeriod'),
                value=data_dict.get('value'),
                cost=data_dict.get('cost'),
                label=data_dict.get('label'),
                description=data_dict.get('description'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class BillPositionType: # EEBus_SPINE_TS_Bill.xsd:ns_p:BillPositionType -> ComplexType
    def __init__(
            self,
            position_id: BillPositionIdType = None,
            position_type: BillPositionTypeType = None,
            time_period: TimePeriodType = None,
            value: list[BillValueType] = None,
            cost: list[BillCostType] = None,
            label: LabelType = None,
            description: DescriptionType = None,
    ):
        super().__init__()
        
        self.position_id = position_id
        self.position_type = position_type
        self.time_period = time_period
        self.value = value
        self.cost = cost
        self.label = label
        self.description = description

        if not isinstance(self.position_id, BillPositionIdType | NoneType):
            raise TypeError("position_id is not of type BillPositionIdType")
        
        if not isinstance(self.position_type, BillPositionTypeType | NoneType):
            raise TypeError("position_type is not of type BillPositionTypeType")
        
        if not isinstance(self.time_period, TimePeriodType | NoneType):
            raise TypeError("time_period is not of type TimePeriodType")
        
        if not isinstance(self.value, list | NoneType):
            raise TypeError("value is not of type list[BillValueType]")
        
        if not isinstance(self.cost, list | NoneType):
            raise TypeError("cost is not of type list[BillCostType]")
        
        if not isinstance(self.label, LabelType | NoneType):
            raise TypeError("label is not of type LabelType")
        
        if not isinstance(self.description, DescriptionType | NoneType):
            raise TypeError("description is not of type DescriptionType")
        
    def get_data(self):

        msg_data = []
        
        if self.position_id is not None:
            msg_data.append({"positionId": self.position_id.get_data()})
        if self.position_type is not None:
            msg_data.append({"positionType": self.position_type.get_data()})
        if self.time_period is not None:
            msg_data.append({"timePeriod": self.time_period.get_data()})
        if self.value is not None:
            msg_data.append({"value": [d.get_data() for d in self.value]})
        if self.cost is not None:
            msg_data.append({"cost": [d.get_data() for d in self.cost]})
        if self.label is not None:
            msg_data.append({"label": self.label.get_data()})
        if self.description is not None:
            msg_data.append({"description": self.description.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.position_id is not None:
            result_str += f"{sep}positionId: {self.position_id}"
            sep = ", "
        if self.position_type is not None:
            result_str += f"{sep}positionType: {self.position_type}"
            sep = ", "
        if self.time_period is not None:
            result_str += f"{sep}timePeriod: {self.time_period}"
            sep = ", "
        if self.value is not None:
            result_str += f"{sep}value: {self.value}"
            sep = ", "
        if self.cost is not None:
            result_str += f"{sep}cost: {self.cost}"
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
                position_id=data_dict.get('positionId'),
                position_type=data_dict.get('positionType'),
                time_period=data_dict.get('timePeriod'),
                value=data_dict.get('value'),
                cost=data_dict.get('cost'),
                label=data_dict.get('label'),
                description=data_dict.get('description'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class BillListDataType: # EEBus_SPINE_TS_Bill.xsd:ns_p:BillListDataType -> ComplexType
    def __init__(
            self,
            bill_data: list[BillDataType] = None,
    ):
        super().__init__()
        
        self.bill_data = bill_data

        if not isinstance(self.bill_data, list | NoneType):
            raise TypeError("bill_data is not of type list[BillDataType]")
        
    def get_data(self):

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


class BillDescriptionListDataType: # EEBus_SPINE_TS_Bill.xsd:ns_p:BillDescriptionListDataType -> ComplexType
    def __init__(
            self,
            bill_description_data: list[BillDescriptionDataType] = None,
    ):
        super().__init__()
        
        self.bill_description_data = bill_description_data

        if not isinstance(self.bill_description_data, list | NoneType):
            raise TypeError("bill_description_data is not of type list[BillDescriptionDataType]")
        
    def get_data(self):

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


class BillConstraintsListDataType: # EEBus_SPINE_TS_Bill.xsd:ns_p:BillConstraintsListDataType -> ComplexType
    def __init__(
            self,
            bill_constraints_data: list[BillConstraintsDataType] = None,
    ):
        super().__init__()
        
        self.bill_constraints_data = bill_constraints_data

        if not isinstance(self.bill_constraints_data, list | NoneType):
            raise TypeError("bill_constraints_data is not of type list[BillConstraintsDataType]")
        
    def get_data(self):

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


class BillDescriptionDataElementsType: # EEBus_SPINE_TS_Bill.xsd:ns_p:BillDescriptionDataElementsType -> ComplexType
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
        
    def get_data(self):

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


class BillDataElementsType: # EEBus_SPINE_TS_Bill.xsd:ns_p:BillDataElementsType -> ComplexType
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
        
    def get_data(self):

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


class BillConstraintsDataElementsType: # EEBus_SPINE_TS_Bill.xsd:ns_p:BillConstraintsDataElementsType -> ComplexType
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
        
    def get_data(self):

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


class BillListDataSelectorsType: # EEBus_SPINE_TS_Bill.xsd:ns_p:BillListDataSelectorsType -> ComplexType
    def __init__(
            self,
            bill_id: BillIdType = None,
            scope_type: ScopeTypeType = None,
    ):
        super().__init__()
        
        self.bill_id = bill_id
        self.scope_type = scope_type

        if not isinstance(self.bill_id, BillIdType | NoneType):
            raise TypeError("bill_id is not of type BillIdType")
        
        if not isinstance(self.scope_type, ScopeTypeType | NoneType):
            raise TypeError("scope_type is not of type ScopeTypeType")
        
    def get_data(self):

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


class BillDescriptionListDataSelectorsType: # EEBus_SPINE_TS_Bill.xsd:ns_p:BillDescriptionListDataSelectorsType -> ComplexType
    def __init__(
            self,
            bill_id: BillIdType = None,
    ):
        super().__init__()
        
        self.bill_id = bill_id

        if not isinstance(self.bill_id, BillIdType | NoneType):
            raise TypeError("bill_id is not of type BillIdType")
        
    def get_data(self):

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


class BillConstraintsListDataSelectorsType: # EEBus_SPINE_TS_Bill.xsd:ns_p:BillConstraintsListDataSelectorsType -> ComplexType
    def __init__(
            self,
            bill_id: BillIdType = None,
    ):
        super().__init__()
        
        self.bill_id = bill_id

        if not isinstance(self.bill_id, BillIdType | NoneType):
            raise TypeError("bill_id is not of type BillIdType")
        
    def get_data(self):

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



