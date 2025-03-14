# Jinja Template message_type.py.jinja2
from types import NoneType
from spine import array_2_dict


class IncentiveTableTierType: # EEBus_SPINE_TS_IncentiveTable.xsd:ns_p:IncentiveTableTierType -> ComplexType
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


class IncentiveTableTierElementsType: # EEBus_SPINE_TS_IncentiveTable.xsd:ns_p:IncentiveTableTierElementsType -> ComplexType
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


class IncentiveTableDescriptionTierType: # EEBus_SPINE_TS_IncentiveTable.xsd:ns_p:IncentiveTableDescriptionTierType -> ComplexType
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


class IncentiveTableIncentiveSlotType: # EEBus_SPINE_TS_IncentiveTable.xsd:ns_p:IncentiveTableIncentiveSlotType -> ComplexType
    def __init__(
            self,
            tier: list[IncentiveTableTierType] = None,
    ):
        super().__init__()
        
        self.tier = tier

        if not isinstance(self.tier, list | NoneType):
            raise TypeError("tier is not of type list[IncentiveTableTierType]")
        
    def get_data(self):

        msg_data = []
        
        if self.tier is not None:
            msg_data.append({"tier": [d.get_data() for d in self.tier]})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.tier is not None:
            result_str += f"{sep}tier: {self.tier}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                tier=data_dict.get('tier'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class IncentiveTableDescriptionTierElementsType: # EEBus_SPINE_TS_IncentiveTable.xsd:ns_p:IncentiveTableDescriptionTierElementsType -> ComplexType
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


class IncentiveTableIncentiveSlotElementsType: # EEBus_SPINE_TS_IncentiveTable.xsd:ns_p:IncentiveTableIncentiveSlotElementsType -> ComplexType
    def __init__(
            self,
            tier: IncentiveTableTierElementsType = None,
    ):
        super().__init__()
        
        self.tier = tier

        if not isinstance(self.tier, IncentiveTableTierElementsType | NoneType):
            raise TypeError("tier is not of type IncentiveTableTierElementsType")
        
    def get_data(self):

        msg_data = []
        
        if self.tier is not None:
            msg_data.append({"tier": self.tier.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.tier is not None:
            result_str += f"{sep}tier: {self.tier}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                tier=data_dict.get('tier'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class IncentiveTableDescriptionType: # EEBus_SPINE_TS_IncentiveTable.xsd:ns_p:IncentiveTableDescriptionType -> ComplexType
    def __init__(
            self,
            tier: list[IncentiveTableDescriptionTierType] = None,
    ):
        super().__init__()
        
        self.tier = tier

        if not isinstance(self.tier, list | NoneType):
            raise TypeError("tier is not of type list[IncentiveTableDescriptionTierType]")
        
    def get_data(self):

        msg_data = []
        
        if self.tier is not None:
            msg_data.append({"tier": [d.get_data() for d in self.tier]})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.tier is not None:
            result_str += f"{sep}tier: {self.tier}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                tier=data_dict.get('tier'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class IncentiveTableType: # EEBus_SPINE_TS_IncentiveTable.xsd:ns_p:IncentiveTableType -> ComplexType
    def __init__(
            self,
            incentive_slot: list[IncentiveTableIncentiveSlotType] = None,
    ):
        super().__init__()
        
        self.incentive_slot = incentive_slot

        if not isinstance(self.incentive_slot, list | NoneType):
            raise TypeError("incentive_slot is not of type list[IncentiveTableIncentiveSlotType]")
        
    def get_data(self):

        msg_data = []
        
        if self.incentive_slot is not None:
            msg_data.append({"incentiveSlot": [d.get_data() for d in self.incentive_slot]})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.incentive_slot is not None:
            result_str += f"{sep}incentiveSlot: {self.incentive_slot}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                incentive_slot=data_dict.get('incentiveSlot'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class IncentiveTableConstraintsType: # EEBus_SPINE_TS_IncentiveTable.xsd:ns_p:IncentiveTableConstraintsType -> ComplexType
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


class IncentiveTableDescriptionElementsType: # EEBus_SPINE_TS_IncentiveTable.xsd:ns_p:IncentiveTableDescriptionElementsType -> ComplexType
    def __init__(
            self,
            tier: IncentiveTableDescriptionTierElementsType = None,
    ):
        super().__init__()
        
        self.tier = tier

        if not isinstance(self.tier, IncentiveTableDescriptionTierElementsType | NoneType):
            raise TypeError("tier is not of type IncentiveTableDescriptionTierElementsType")
        
    def get_data(self):

        msg_data = []
        
        if self.tier is not None:
            msg_data.append({"tier": self.tier.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.tier is not None:
            result_str += f"{sep}tier: {self.tier}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                tier=data_dict.get('tier'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class IncentiveTableElementsType: # EEBus_SPINE_TS_IncentiveTable.xsd:ns_p:IncentiveTableElementsType -> ComplexType
    def __init__(
            self,
            incentive_slot: IncentiveTableIncentiveSlotElementsType = None,
    ):
        super().__init__()
        
        self.incentive_slot = incentive_slot

        if not isinstance(self.incentive_slot, IncentiveTableIncentiveSlotElementsType | NoneType):
            raise TypeError("incentive_slot is not of type IncentiveTableIncentiveSlotElementsType")
        
    def get_data(self):

        msg_data = []
        
        if self.incentive_slot is not None:
            msg_data.append({"incentiveSlot": self.incentive_slot.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.incentive_slot is not None:
            result_str += f"{sep}incentiveSlot: {self.incentive_slot}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                incentive_slot=data_dict.get('incentiveSlot'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class IncentiveTableConstraintsElementsType: # EEBus_SPINE_TS_IncentiveTable.xsd:ns_p:IncentiveTableConstraintsElementsType -> ComplexType
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


class IncentiveTableDescriptionDataType: # EEBus_SPINE_TS_IncentiveTable.xsd:ns_p:IncentiveTableDescriptionDataType -> ComplexType
    def __init__(
            self,
            incentive_table_description: list[IncentiveTableDescriptionType] = None,
    ):
        super().__init__()
        
        self.incentive_table_description = incentive_table_description

        if not isinstance(self.incentive_table_description, list | NoneType):
            raise TypeError("incentive_table_description is not of type list[IncentiveTableDescriptionType]")
        
    def get_data(self):

        msg_data = []
        
        if self.incentive_table_description is not None:
            msg_data.append({"incentiveTableDescription": [d.get_data() for d in self.incentive_table_description]})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.incentive_table_description is not None:
            result_str += f"{sep}incentiveTableDescription: {self.incentive_table_description}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                incentive_table_description=data_dict.get('incentiveTableDescription'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class IncentiveTableDataType: # EEBus_SPINE_TS_IncentiveTable.xsd:ns_p:IncentiveTableDataType -> ComplexType
    def __init__(
            self,
            incentive_table: list[IncentiveTableType] = None,
    ):
        super().__init__()
        
        self.incentive_table = incentive_table

        if not isinstance(self.incentive_table, list | NoneType):
            raise TypeError("incentive_table is not of type list[IncentiveTableType]")
        
    def get_data(self):

        msg_data = []
        
        if self.incentive_table is not None:
            msg_data.append({"incentiveTable": [d.get_data() for d in self.incentive_table]})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.incentive_table is not None:
            result_str += f"{sep}incentiveTable: {self.incentive_table}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                incentive_table=data_dict.get('incentiveTable'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class IncentiveTableConstraintsDataType: # EEBus_SPINE_TS_IncentiveTable.xsd:ns_p:IncentiveTableConstraintsDataType -> ComplexType
    def __init__(
            self,
            incentive_table_constraints: list[IncentiveTableConstraintsType] = None,
    ):
        super().__init__()
        
        self.incentive_table_constraints = incentive_table_constraints

        if not isinstance(self.incentive_table_constraints, list | NoneType):
            raise TypeError("incentive_table_constraints is not of type list[IncentiveTableConstraintsType]")
        
    def get_data(self):

        msg_data = []
        
        if self.incentive_table_constraints is not None:
            msg_data.append({"incentiveTableConstraints": [d.get_data() for d in self.incentive_table_constraints]})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.incentive_table_constraints is not None:
            result_str += f"{sep}incentiveTableConstraints: {self.incentive_table_constraints}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                incentive_table_constraints=data_dict.get('incentiveTableConstraints'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class IncentiveTableDescriptionDataElementsType: # EEBus_SPINE_TS_IncentiveTable.xsd:ns_p:IncentiveTableDescriptionDataElementsType -> ComplexType
    def __init__(
            self,
            incentive_table_description: IncentiveTableDescriptionElementsType = None,
    ):
        super().__init__()
        
        self.incentive_table_description = incentive_table_description

        if not isinstance(self.incentive_table_description, IncentiveTableDescriptionElementsType | NoneType):
            raise TypeError("incentive_table_description is not of type IncentiveTableDescriptionElementsType")
        
    def get_data(self):

        msg_data = []
        
        if self.incentive_table_description is not None:
            msg_data.append({"incentiveTableDescription": self.incentive_table_description.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.incentive_table_description is not None:
            result_str += f"{sep}incentiveTableDescription: {self.incentive_table_description}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                incentive_table_description=data_dict.get('incentiveTableDescription'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class IncentiveTableDataElementsType: # EEBus_SPINE_TS_IncentiveTable.xsd:ns_p:IncentiveTableDataElementsType -> ComplexType
    def __init__(
            self,
            incentive_table: IncentiveTableElementsType = None,
    ):
        super().__init__()
        
        self.incentive_table = incentive_table

        if not isinstance(self.incentive_table, IncentiveTableElementsType | NoneType):
            raise TypeError("incentive_table is not of type IncentiveTableElementsType")
        
    def get_data(self):

        msg_data = []
        
        if self.incentive_table is not None:
            msg_data.append({"incentiveTable": self.incentive_table.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.incentive_table is not None:
            result_str += f"{sep}incentiveTable: {self.incentive_table}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                incentive_table=data_dict.get('incentiveTable'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class IncentiveTableConstraintsDataElementsType: # EEBus_SPINE_TS_IncentiveTable.xsd:ns_p:IncentiveTableConstraintsDataElementsType -> ComplexType
    def __init__(
            self,
            incentive_table_constraints: IncentiveTableConstraintsElementsType = None,
    ):
        super().__init__()
        
        self.incentive_table_constraints = incentive_table_constraints

        if not isinstance(self.incentive_table_constraints, IncentiveTableConstraintsElementsType | NoneType):
            raise TypeError("incentive_table_constraints is not of type IncentiveTableConstraintsElementsType")
        
    def get_data(self):

        msg_data = []
        
        if self.incentive_table_constraints is not None:
            msg_data.append({"incentiveTableConstraints": self.incentive_table_constraints.get_data()})
        
        return msg_data


    def __str__(self):
        result_str = ""
        sep = ""
        if self.incentive_table_constraints is not None:
            result_str += f"{sep}incentiveTableConstraints: {self.incentive_table_constraints}"
        
        return result_str

    @classmethod
    def from_data(cls, data):
        if type(data) == list:
            data_dict = array_2_dict(data)
            return cls(
                incentive_table_constraints=data_dict.get('incentiveTableConstraints'),
            )
        elif data:
            return cls(data)
        else:
            return cls()


class IncentiveTableDescriptionDataSelectorsType: # EEBus_SPINE_TS_IncentiveTable.xsd:ns_p:IncentiveTableDescriptionDataSelectorsType -> ComplexType
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


class IncentiveTableDataSelectorsType: # EEBus_SPINE_TS_IncentiveTable.xsd:ns_p:IncentiveTableDataSelectorsType -> ComplexType
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


class IncentiveTableConstraintsDataSelectorsType: # EEBus_SPINE_TS_IncentiveTable.xsd:ns_p:IncentiveTableConstraintsDataSelectorsType -> ComplexType
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



