import os
import re

import xmlschema
from jinja2 import Environment, FileSystemLoader
import networkx as nx
from xmlschema import XsdElement
from xmlschema.validators import XsdGroup

from xsd2code import Member, ALL_TYPES

from xsd2code import ChoiceType, EnumType, create_type_from_xsd, ComplexType
from xsd2code.types import UnionType, AliasType

schemas = [
   # {"file": 'xsd/EEBus_SHIP_TS_TransferProtocol.xsd', "folder": "ship"},
    {"file": 'xsd/EEBus_SPINE_TS_Datagram.xsd', "folder": "spine"}
]

BASE_TYPES = ["str", "int", "bool"]


def get_source_name(type_object):
    result = type_object.schema.name.replace('EEBus_SPINE_TS_', '').replace('.xsd','')
    return result


def get_default_value(type, attr):
    if type is None or attr is None:
        return None

    return default_values.get(f"{type}.{attr.lower()}")


def dict_dict_2_dict(val):
    result = {}
    for x in val:
        result |= val[x]

    return result


def get_imports_and_sort(type_list, type_2_source, dest_folder):
    used_import = []
    import_done = []

    nx_graph = nx.DiGraph()
    keyed_input = {}
    input_size = len(type_list)

    for ele in type_list:

        nx_graph.add_node(ele.fq_name)
        keyed_input[ele.fq_name] = ele

        for dep in ele.depend_on_types:

            nx_graph.add_edge(ele.fq_name, dep)

    sorted_graph = list(reversed(list(nx.topological_sort(nx_graph))))
    sorted_elements = []
    for type_name in sorted_graph:
        if type_name in keyed_input:
            sorted_elements.append(keyed_input[type_name])

    if input_size != len(sorted_elements):
        raise RuntimeError(f"Sorting failed {input_size} != {len(sorted_elements)}")

    all_imports = [f"import {'.'.join(imp['source_path'].split('.')[:-1])} as {imp['source_path'].split('.')[-2]}" for imp in used_import]
    unique_imports = list(set(all_imports))
    return unique_imports, sorted_elements


# Section: 13.4.2
def msg_group_value(group_name):

    if group_name == "MsgTypeControlGroup":
        return "MessageType.MSG_TYPE_CONTROL"
    elif group_name == "MsgTypeDataGroup":
        return "MessageType.MSG_TYPE_DATA"
    elif group_name == "MsgTypeEndGroup":
        return "MessageType.MSG_TYPE_END"
    else:
        return None


def to_class_name(name):
    return name[0].upper() + name[1:]

for schema_cfg in schemas:
    schema = xmlschema.XMLSchema(schema_cfg["file"])

    folder = schema_cfg["folder"]

    default_values = {
        "ConnectionHelloType.waiting": 60000,
        "MessageProtocolHandshakeType.version": 'Version(major=1, minor=0)',
        "MessageProtocolHandshakeType.formats": 'MessageProtocolFormatsType(format=[MessageProtocolFormatType("JSON-UTF8")])',
        "ProtocolIdType.protocolidtype": "'ee1.0'"
    }

    no_attr_name = {
        "ProtocolIdType",
        "MessageProtocolFormatType"
    }

    attr_2_type = {
        "MessageProtocolHandshakeType.version": "Version",
        "AccessMethodsType.dnsSd_mDns": "DnsSd_MDns",
        "AccessMethodsType.dns": "Dns"

    }

    env = Environment(loader=FileSystemLoader("templates/"))

    template_enum = env.get_template("enums.py.jinja2")
    template_message_type = env.get_template("message_type.py.jinja2")
    template_message = env.get_template("message.py.jinja2")
    template_choice_class = env.get_template("choice_class.py.jinja2")
    template_init_module = env.get_template("module_init.py.jinja2")

    #type_list = TypeList()

    enum_types = {}
    all_types = {}

    # for ele in schema.elements:
    #     ele_obj = schema.elements[ele]
    #     #print(f"{ele_obj.display_name}")

    # for group in schema.groups:
    #     print(group)

    for ship_type in schema.types:
        if ship_type not in ["CmdType"]:
            continue

        type_name = type(schema.types[ship_type]).__name__
        type_obj = schema.types[ship_type]
        source_xsd = get_source_name(type_obj)
        #print(f"{ship_type} - {type_name} - {source_xsd}")

        if source_xsd not in all_types:
            all_types[source_xsd] = {}
        if source_xsd not in enum_types:
            enum_types[source_xsd] = {}

        if type_name == "XsdAtomicRestriction" and type_obj.enumeration:
            enum_types[source_xsd][ship_type] = {"enums": type_obj.enumeration}
            ALL_TYPES.get_or_create(create_type_from_xsd(type_obj))
        elif type_name == "XsdComplexType":

            ALL_TYPES.get_or_create(create_type_from_xsd(type_obj))

        elif type_name == "XsdAtomicRestriction":
            #print(f"{ship_type} {type_obj.local_name} {type_obj.base_type.display_name}")
            #data_type = xsd_to_python_type(type_obj.base_type)
            members = [
                Member(
                    fq_member_name=type_obj.display_name,
                    data_type=ALL_TYPES.get_or_create(add_type=create_type_from_xsd(type_obj.base_type)),
                    is_optional=False,
                    default_value=default_values.get(f"{ship_type}.{type_obj.local_name.lower()}")
                )]
            all_types[source_xsd][ship_type] = {"members": members, "no_attrib_name": True if ship_type in no_attr_name else False}

            # print(f"{ship_type}: {members}")
        elif type_name == "XsdUnion":
            #print(f"XsdUnion: {ship_type} members: {type_obj.local_name}")
            #data_type = xsd_to_python_type(type_obj.base_type.display_name)
            members = [
                Member(
                    fq_member_name=type_obj.display_name,
                    data_type=ALL_TYPES.get_or_create(create_type_from_xsd(type_obj)),
                    is_optional=False,
                    default_value=default_values.get(f"{ship_type}.{type_obj.local_name.lower()}")
                )]
            all_types[source_xsd][ship_type] = {"members": members, "no_attrib_name": True if ship_type in no_attr_name else False}

        else:
            print(f"Not handeled: {ship_type}: {type_name}")

    groups = {}
    group_class = {}

    #print(ALL_TYPES)

    # for t in ALL_TYPES.types:
    #     if hasattr(t, "_base_type") and t._base_type:
    #         print(f"class {t.class_name}({t._base_type.class_name}):")
    #     else:
    #         print(f"class {t.class_name}:")
    #
    #     if hasattr(t, "_members"):
    #         for m in t._members:
    #             print(f"  {m}:{m.class_name}")

    # choice_graph = nx.DiGraph()
    #
    for grp in schema.groups:
        grp_obj = schema.groups[grp]
        print(f"{folder}-{grp_obj.display_name}")

        ALL_TYPES.get_or_create(
            create_type_from_xsd(grp_obj)
        )

        # for ele in grp_obj.content:
        #     print(f"   -{ele.display_name} {type(ele).__name__}")
        #     if isinstance(ele, XsdElement):
        #         group_type.add_choice_member(
        #             Member(
        #                 fq_member_name=ele.display_name,
        #                 data_type=ALL_TYPES.get_or_create(create_type_from_xsd(ele.type)),
        #                 is_optional=True if ele.min_occurs == 0 else False,
        #                 is_array=True if ele.max_occurs is None or ele.max_occurs > 1 else False
        #             )
        #         )
        #     elif isinstance(ele, XsdGroup):
        #         group_type.add_choice_type(
        #             ALL_TYPES.get_or_create(
        #                 ChoiceType(type_name=ele.display_name, source_file=ele.schema.name)
        #             )
        #         )



    #
    # sorted_choices = list(reversed(list(nx.topological_sort(choice_graph))))
    #
    # type_2_source = {}
    # choice_types = []
    # for type_name in sorted_choices:
    #     if type_name in group_class:
    #         ch = group_class[type_name]
    #         ch["name"] = type_name
    #         choice_types.append(ch)
    #         type_2_source[type_name] = {
    #                 "source_path": f"{folder}.choice_class",
    #                 "source_class": type_name,
    #                 "type_name": type_name
    #             }

    ALL_TYPES.set_template_options_by_type(
        data_type=EnumType,
        module=f"{folder}.enums",
        file_name="{self.base_source.lower()}.py",
        jinja_template=template_enum
    )

    ALL_TYPES.set_template_options_by_type(
        data_type=ComplexType,
        module=f"{folder}.base_type",
        file_name="{self.base_source.lower()}.py",
        jinja_template=template_message_type
    )

    ALL_TYPES.set_template_options_by_type(
        data_type=UnionType,
        module=f"{folder}.union_type",
        file_name="{self.base_source.lower()}.py",
        jinja_template=template_message_type
    )

    ALL_TYPES.set_template_options_by_type(
        data_type=AliasType,
        module=f"{folder}.simple_type",
        file_name="{self.base_source.lower()}.py",
        jinja_template=template_message_type
    )

    ALL_TYPES.set_template_options_by_type(
        data_type=ChoiceType,
        module=f"{folder}.choice_type",
        file_name="{self.base_source.lower()}.py",
        jinja_template=template_message_type
    )

    ALL_TYPES.sort_by_name()

    missing_dest = ALL_TYPES.get_types_without_template_options()
    for m in missing_dest:
        print(m)

    ALL_TYPES.write_all_files()
