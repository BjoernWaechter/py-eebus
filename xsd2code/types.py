import os

from xmlschema import XsdElement
from xmlschema.validators import XsdAtomicRestriction, XsdType, XsdComplexType, XsdAtomicBuiltin, XsdUnion, XsdGroup
from inspect import getframeinfo, stack

import xsd2code


class DataType:

    def __init__(self, type_name, source_file):
        if type_name:
            self.namespace, self.type_name = type_name.split(":")
        else:
            self.namespace = None
            self.type_name = None

        step_back = 1
        caller_file = getframeinfo(stack()[step_back][0]).filename
        while "types.py" in caller_file:
            step_back += 1
            caller_file = getframeinfo(stack()[step_back][0]).filename

        caller = getframeinfo(stack()[step_back][0])
        self.first_creator = f"{caller.filename}:{caller.lineno}"

        self.source_file = source_file
        self.base_source = source_file.replace('EEBus_SPINE_TS_', '').replace('.xsd', '')

        self._module = None
        self._file_name = None
        self._jinja_template = None
        self._import_type = "FULL_PATH"


    @property
    def class_name(self):
        return self.type_name

    @property
    def fq_name(self):
        return f"{self.namespace}:{self.type_name}"

    def set_module(self, module):
        self._module = module

    def get_import(self):
        if self._import_type == "FULL_PATH":
            if self.module and self._file_name and self.class_name:
                return f"from {self.module}.{self._file_name.replace('.py','')} import {self.class_name}"

        return None

    @property
    def module(self):
        return self._module

    def set_file_name(self, file_name):
        self._file_name = eval(f'f"""{file_name}"""')

    def set_jinja_template(self, jinja_template):
        self._jinja_template = jinja_template

    def get_jinja_template(self):
        return self._jinja_template

    def get_full_path(self):
        if self._file_name and self._module:
            return f"{self._module.replace('.',os.sep)}{os.sep}{self._file_name}"
        else:
            return None

    def __eq__(self, other):
        if self.namespace == other.namespace and self.type_name == other.type_name:# and self._is_array == other._is_array:
            if type(self) is not type(other):
                raise RuntimeError(f"Same namespace and name but different types: {self.namespace}:{self.type_name}({type(self).__name__}/{type(other).__name__}) {self.first_creator}")
            return True
        else:
            return False

    def __hash__(self):
        return hash(self.namespace + self.type_name)

    def __str__(self):
        if self.get_full_path():
            return f"{self.namespace}:{self.type_name} ({self.get_full_path()})"
        else:
            return f"{self.namespace}:{self.type_name} (not set)"

    def get_as_code(self):
        pass

    @property
    def depend_on_types(self):
        return []

    @property
    def data_access_method(self):
        return ".get_data()"

    @property
    def return_type(self):
        return "array"

    @property
    def info_comment(self):
        return type(self).__name__


class BaseType(DataType):
    def __init__(self, type_name: str, source_file):
        super().__init__(type_name, source_file)

    def get_as_code(self):
        return self.type_name

    @staticmethod
    def xsd_to_python_type(xsd_type):
        if xsd_type == "xs:unsignedInt":
            return "int"
        elif xsd_type == "xs:unsignedByte":
            return "int"
        elif xsd_type == "xs:integer":
            return "int"
        elif xsd_type == "xs:boolean":
            return "bool"
        elif xsd_type == "xs:string":
            return "str"
        elif xsd_type == "xs:anyType":
            return ""
        elif xsd_type == "xs:decimal":
            return "float"
        elif xsd_type == "xs:hexBinary":
            return "str"
        elif xsd_type == "xs:unsignedShort":
            return "int"
        elif xsd_type == "xs:unsignedLong":
            return "int"
        elif xsd_type == "xs:short":
            return "int"
        elif xsd_type == "xs:long":
            return "int"
        elif xsd_type == "xs:duration":
            return "str"
        elif xsd_type == "xs:dateTime":
            return "str"
        elif xsd_type == "xs:date":
            return "str"
        elif xsd_type == "xs:time":
            return "str"
        elif xsd_type == "xs:dateTime":
            return "str"

    @property
    def class_name(self):
        return self.xsd_to_python_type(self.fq_name)

    @property
    def data_access_method(self):
        return ""

    @property
    def return_type(self):
        return "value"


class SimpleType(DataType):

    def __init__(self, type_name: str, source_file):
        super().__init__(type_name, source_file)

    def get_as_code(self):
        return self.type_name


# class ArrayType(DataType):
#
#     def __init__(self, type_name: str):
#         super().__init__(type_name)
#         self._is_array = True
#
#     def get_as_code(self):
#         return self._type_name


class UnionType(DataType):

    def __init__(self, type_name, source_file, union_type_list: list[DataType] = None):
        super().__init__(type_name, source_file)
        if union_type_list is None:
            self._union_type_list = []
        else:
            self._union_type_list = union_type_list

    def add_union_type(self, add_type):
        self._union_type_list.append(add_type)

    def __hash__(self):
        return hash(self.namespace + self.type_name)

    def __eq__(self, other):
        if type(self) is not type(other):
            return False
        elif len(self._union_type_list) != len(other._union_type_list):
            return False

        for s_type in self._union_type_list:
            if s_type not in other._union_type_list:
                return False

        for o_type in other._union_type_list:
            if o_type not in self._union_type_list:
                return False

        return True

    def get_as_code(self):
        return " | ".join(self.type_list)


class ChoiceType(DataType):

    def __init__(self, type_name: str, source_file):
        if not type_name:
            raise RuntimeError(f"Missing type_name from {source_file}")
        super().__init__(type_name, source_file)

        self._choice_members = []
        self._choice_types = []

    def add_choice_member(self, add_member):
        if add_member not in self._choice_members:
            self._choice_members.append(add_member)

    def add_choice_type(self, choice_type):
        if choice_type not in self._choice_types:
            self._choice_types.append(choice_type)

    def get_as_code(self):
        return self.type_name

    @property
    def members(self):
        return self._choice_members

    @property
    def depend_on_types(self):
        return [t._data_type for t in self.members]


class EnumType(DataType):

    def __init__(self, type_name: str, source_file, enum_values: list[str]):
        super().__init__(type_name, source_file)

        self._enum_values = enum_values

    @property
    def enum_values(self):
        return self._enum_values

    def get_as_code(self):
        return self.type_name

    @property
    def data_access_method(self):
        return ".value"


class AliasType(DataType):

    def __init__(self, type_name: str, source_file, base_type):
        super().__init__(type_name, source_file)

        self._base_type = base_type

        self._members = [xsd2code.Member(
            fq_member_name=":value",
            data_type=xsd2code.ALL_TYPES.get_or_create(base_type),
        )]

    @property
    def members(self):
        return self._members

    def get_as_code(self):
        return self.type_name

    @property
    def return_type(self):
        return "value"


class ComplexType(DataType):

    def __init__(self, type_name: str, source_file):
        super().__init__(type_name, source_file)

        self._members = []
        self._group_types = []
        self._base_type = None

    def add_member(self, add_member):
        if add_member in self._members:
            raise RuntimeError(f"Member {add_member} was already added to type {self.type_name}")
            #print(f"Member {add_member} was already added to type {self.type_name}")
        else:
            self._members.append(add_member)

    def add_group_type(self, add_group_type):
        self._group_types.append(add_group_type)

    @property
    def members(self):
        if self._base_type:
            result = self._base_type.members.copy()
            for m in self._members:
                replaced_existing = False
                for idx in range(len(result)):
                    # If there is already the same member name it could be overwritten with other datatype ...
                    if m.fq_name == result[idx].fq_name:
                        result[idx] = m
                        replaced_existing = True
                if not replaced_existing:
                    result.append(m)
            return result
        else:
            return self._members

    def get_as_code(self):
        return self.type_name

    def set_base_type(self, base_type):
        self._base_type = base_type

    @property
    def base_type(self):
        return self._base_type

    @property
    def depend_on_types(self):
        if self._base_type:
            return [t._data_type for t in self.members]+[self._base_type]
        else:
            return [t._data_type for t in self.members]


def show_selected_attr(obj, interest, depth=0):
    spaces = "    "
    for attr in dir(obj):
        if attr in interest:
            value = getattr(obj, attr)
            #print(value)
            if hasattr(value, "__dict__"):
                print(f"{spaces * depth}{attr}(obj):")
                show_selected_attr(value, interest, depth + 1)
            elif isinstance(value, list):

                for idx in range(len(value)):
                    print(f"{spaces * depth}{attr}[{idx}]:")
                    show_selected_attr(value[idx], interest, depth + 1)
            elif value:
                print(f"{spaces * depth}{attr}: {value}")

def create_type_from_xsd(xsd_type: XsdType):
    if isinstance(xsd_type, XsdAtomicRestriction):
        if xsd_type.enumeration:
            return EnumType(
                type_name=xsd_type.display_name,
                source_file=xsd_type.schema.name,
                enum_values=xsd_type.enumeration
            )
        else:
            return AliasType(
                type_name=xsd_type.display_name,
                source_file=xsd_type.schema.name,
                base_type=xsd2code.ALL_TYPES.get_or_create(create_type_from_xsd(xsd_type.base_type))
            )
    elif isinstance(xsd_type, XsdComplexType):


        comp_type = ComplexType(
            type_name=xsd_type.display_name,
            source_file=xsd_type.schema.name
        )
        #print(f"-------- {xsd_type.display_name} --------")
        if hasattr(xsd_type, "base_type") and hasattr(xsd_type.base_type, "display_name"):
            #print(f" create from basetype: {xsd_type.base_type.display_name}")
            comp_type.set_base_type(xsd2code.ALL_TYPES.get_or_create(create_type_from_xsd(xsd_type.base_type)))
            #print(f"-------- back  {xsd_type.display_name} --------")

        added_members = []
        if hasattr(xsd_type, "content"):
            if hasattr(xsd_type.content, "content"):
                for mem in xsd_type.content.content:

                    #print(f" - {mem}")

                    if hasattr(mem, "type") and mem.type.display_name:
                        #print(f"create mem {xsd_type.display_name}.{mem.display_name}")
                        added_members.append(mem.display_name)
                        comp_type.add_member(xsd2code.Member(
                            fq_member_name=mem.display_name,
                            data_type=xsd2code.ALL_TYPES.get_or_create(create_type_from_xsd(mem.type)),
                            is_optional=True if mem.min_occurs == 0 else False,
                            is_array=True if mem.max_occurs is None or mem.max_occurs > 1 else False
                        ))

                    if isinstance(mem, XsdGroup) and hasattr(mem, "display_name") and mem.display_name:
                        comp_type.add_group_type(
                            xsd2code.ALL_TYPES.get_or_create(create_type_from_xsd(mem))
                        )

                    if hasattr(mem, "content"):
                        for mem_ref in mem.content:
                            if hasattr(mem_ref, "display_name") and hasattr(mem_ref, "type"):



                                #print(f"create ref {comp_type.type_name}.{mem_ref.display_name}")
                                comp_type.add_member(xsd2code.Member(
                                    fq_member_name=mem_ref.display_name,
                                    data_type=xsd2code.ALL_TYPES.get_or_create(create_type_from_xsd(mem_ref.type)),
                                    is_optional=True, # TODO: Try to figure out where this information is stored
                                    is_array=True if mem_ref.max_occurs is None or mem_ref.max_occurs > 1 else False
                                ))
                                #added_members.append(mem_ref.ref.display_name)

        return comp_type

    elif isinstance(xsd_type, XsdAtomicBuiltin):
        if xsd_type.display_name.split(":")[0] == "xs":
            return BaseType(
                type_name=xsd_type.display_name,
                source_file=xsd_type.schema.name,
                #base_type=xsd_type.display_name.split(":")[1]
            )
    elif isinstance(xsd_type, XsdUnion):

        union_type = UnionType(
            type_name=xsd_type.display_name,
            source_file=xsd_type.schema.name
        )

        # TODO: Add members
        return union_type

    elif isinstance(xsd_type, XsdGroup):

        group_type = ChoiceType(
            type_name=xsd_type.display_name,
            source_file=xsd_type.schema.name
        )

        for ele in xsd_type.content:
            #print(f"   -{ele.display_name} {type(ele).__name__}")
            if isinstance(ele, XsdElement):
                group_type.add_choice_member(
                    xsd2code.Member(
                        fq_member_name=ele.display_name,
                        data_type=xsd2code.ALL_TYPES.get_or_create(create_type_from_xsd(ele.type)),
                        is_optional=True if ele.min_occurs == 0 else False,
                        is_array=True if ele.max_occurs is None or ele.max_occurs > 1 else False
                    )
                )
            elif isinstance(ele, XsdGroup):
                group_type.add_choice_type(
                    xsd2code.ALL_TYPES.get_or_create(
                        ChoiceType(type_name=ele.display_name, source_file=ele.schema.name)
                    )
                )

        return group_type


    #ArrayType(type_name=m.type.display_name)) if m.max_occurs is None or m.max_occurs > 1 else type_list.get_or_create(SimpleType(type_name=m.type.display_name)

    raise RuntimeError(f"Unknown XsdType: {xsd_type.display_name}-{type(xsd_type).__name__}")