import re

import xmlschema
from jinja2 import Environment, FileSystemLoader
import networkx as nx

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

        nx_graph.add_node(ele['base_name'])
        if "data_type" in ele:
            if not ele["data_type"] in import_done:
                if ele["data_type"] in type_2_source:
                    if type_2_source[ele["data_type"]]["source_path"] != dest_folder:
                        import_done.append(ele["data_type"])
                        used_import.append(type_2_source[ele["data_type"]])
                        ele["type_source"] = type_2_source[ele["data_type"]]
                    nx_graph.add_edge(ele['base_name'], ele["data_type"])
                elif ele['data_type'] not in BASE_TYPES:
                    print(f"{ele['data_type']} not found in type_2_source")

        for mem in ele["members"]:

            #print(mem)
            #
            if isinstance(mem["data_type"], list):
                for m in mem["data_type"]:
                    if m in type_2_source:
                        if m not in import_done and type_2_source[m]["source_path"] != dest_folder:
                            import_done.append(m)
                            used_import.append(type_2_source[m])
                            mem["type_source"] = type_2_source[m]
                        nx_graph.add_edge(ele['base_name'], m)
                    elif m not in BASE_TYPES:
                        print(f"{m} not found in type_2_source")
            elif mem["data_type"] in type_2_source:
                if not mem["data_type"] in import_done and type_2_source[mem["data_type"]]["source_path"] != dest_folder:
                    import_done.append(mem["data_type"])
                    used_import.append(type_2_source[mem["data_type"]])
                    mem["type_source"] = type_2_source[mem["data_type"]]
                nx_graph.add_edge(ele['base_name'], mem["data_type"])
            elif mem["data_type"] not in BASE_TYPES:
                print(f"{mem['data_type']} not found in type_2_source")

        keyed_input[ele['base_name']] = ele

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


def camel_to_snake(name):
    if name is None:
        return None
    name = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', name).lower()


def xsd_to_python_type(xsd_type):
    if xsd_type.display_name == "xs:unsignedInt":
        return {"type": "int", "simple": True}
    elif xsd_type.display_name == "xs:unsignedByte":
        return {"type": "int", "simple": True}
    elif xsd_type.display_name == "xs:integer":
        return {"type": "int", "simple": True}
    elif xsd_type.display_name == "xs:boolean":
        return {"type": "bool", "simple": True}
    elif xsd_type.display_name == "xs:string":
        return {"type": "str", "simple": True}
    elif xsd_type.display_name == "xs:anyType":
        return {"type": "", "simple": True}
    elif xsd_type.display_name == "xs:decimal":
        return {"type": "float", "simple": True}
    elif xsd_type.display_name == "xs:hexBinary":
        return {"type": "str", "simple": True}
    if xsd_type.display_name == "xs:unsignedShort":
        return {"type": "int", "simple": True}
    if xsd_type.display_name == "xs:unsignedLong":
        return {"type": "int", "simple": True}
    if xsd_type.display_name == "xs:short":
        return {"type": "int", "simple": True}
    if xsd_type.display_name == "xs:long":
        return {"type": "int", "simple": True}
    if xsd_type.display_name == "xs:duration":
        return {"type": "str", "simple": True}
    if xsd_type.display_name == "xs:dateTime":
        return {"type": "str", "simple": True}
    if xsd_type.display_name == "xs:date":
        return {"type": "str", "simple": True}
    if xsd_type.display_name == "xs:time":
        return {"type": "str", "simple": True}
    if xsd_type.display_name == "xs:dateTime":
        return {"type": "str", "simple": True}
    elif xsd_type.display_name is None:
        return {"type": "", "simple": True}
    elif ":" in xsd_type.display_name:
        return {"type": f"{xsd_type.display_name.split(':')[1]}", "simple": False}
    else:
        return {"type": f"{xsd_type.python_type}", "simple": True}


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

    enum_types = {}
    all_types = {}

    for ship_type in schema.types:
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
        elif type_name == "XsdComplexType":
            #print(f"{ship_type}")

            members = []

            if hasattr(type_obj.content, "content"):
                #TODO: Missing xs:extension handling
                for m in type_obj.content.content:
                    #print(f"  {m.local_name} - {m.type.display_name}")

                    if hasattr(m, "parent") and m.parent.local_name is not None and ship_type not in ["FeatureAddressType", "EntityAddressElementsType","EntityAddressType", "FeatureAddressElementsType"]:
                        #print(f"{ship_type} - {type_name}")
                        #print("   ---- parent found")
                        #print(f"add: {ship_type}: {m.parent.local_name}")
                        members.append(
                            {
                                "name": "value",
                                "snake_case_name": "value",
                                "data_type": m.parent.local_name,
                                "org_datatype": m.parent.local_name,
                                "is_array": False,
                                "is_optional": True if m.min_occurs == 0 else False,
                                "default_value": get_default_value(ship_type, m.parent.local_name),
                                "source": "XsdComplexType",
                                "is_enum": False,
                                "type_simple": False
                            }
                        )


                    sub_ship_type = None
                    if hasattr(m, "type") and hasattr(m.type, "content") and not m.type.display_name:
                        #print("   ---- subtype found")
                        sub_ship_type = attr_2_type.get(f"{ship_type}.{m.local_name}", "NotSupported")
                        sub_members = []
                        for sub_m in m.type.content.content:
                            data_type = xsd_to_python_type(sub_m.type)
                            sub_members.append(
                                {
                                    "name": sub_m.local_name,
                                    "snake_case_name": camel_to_snake(sub_m.local_name),
                                    "data_type": data_type["type"],
                                    "is_array": True if sub_m.max_occurs is None or sub_m.max_occurs > 1 else False,
                                    "is_optional": True if sub_m.min_occurs == 0 else False,
                                    "default_value": default_values.get(f"{sub_ship_type}.{sub_m.local_name.lower()}"),
                                    "source": "XsdComplexType",
                                    "is_enum": True if data_type["type"] in enum_types else False,
                                    "type_simple": data_type["simple"]
                                }
                            )

                        all_types[source_xsd][sub_ship_type] = {"members": sub_members, "no_attrib_name": False}
                    #else:
                    #    print(f"{ship_type}: {type_name}")
                    #print(m)

                    if sub_ship_type:
                        data_type = {"type": sub_ship_type, "simple": False, "org_datatype": m.type.display_name}
                    elif hasattr(m, "type"):
                        data_type = xsd_to_python_type(m.type)
                        data_type["org_datatype"] = m.type.display_name
                    else:
                        #print(m.local_name)
                        data_type = {"type": m.local_name, "simple": False, "org_datatype": ""}

                    #data_type = {"type": sub_ship_type, "simple": False} if sub_ship_type else xsd_to_python_type(m.type.display_name) if m.type.display_name else m.local_name
                    if m.local_name:
                        members.append(
                            {
                                "name": m.local_name,
                                "snake_case_name": camel_to_snake(m.local_name),
                                "data_type": data_type["type"],
                                "org_datatype": data_type["org_datatype"],
                                "is_array": True if m.max_occurs is None or m.max_occurs > 1 else False,
                                "is_optional": True if m.min_occurs == 0 else False,
                                "default_value": get_default_value(ship_type, m.local_name),
                                "source": "XsdComplexType",
                                "is_enum": True if data_type["type"] in enum_types else False,
                                "type_simple": data_type["simple"]
                            }
                        )

            else:
                print(f"Not handeled: {ship_type}: {type_name}")

            all_types[source_xsd][ship_type] = {"members": members, "no_attrib_name": True if ship_type in no_attr_name else False}

        elif type_name == "XsdAtomicRestriction":
            #print(f"{ship_type} {type_obj.local_name} {type_obj.base_type.display_name}")
            data_type = xsd_to_python_type(type_obj.base_type)
            members = [{
                    "name": type_obj.local_name,
                    "snake_case_name": camel_to_snake(type_obj.local_name),
                    "data_type": data_type["type"],
                    "org_datatype": type_obj.base_type.display_name,
                    "is_array": False,
                    "is_optional": False,
                    "default_value": default_values.get(f"{ship_type}.{type_obj.local_name.lower()}"),
                    "source": "XsdAtomicRestriction",
                    "is_enum": True if type_obj.base_type.display_name in enum_types else False,
                    "type_simple": data_type["simple"]
                }]
            all_types[source_xsd][ship_type] = {"members": members, "no_attrib_name": True if ship_type in no_attr_name else False}

            # print(f"{ship_type}: {members}")
        elif type_name == "XsdUnion":
            #print(f"XsdUnion: {ship_type} members: {type_obj.local_name}")
            #data_type = xsd_to_python_type(type_obj.base_type.display_name)
            members = [{
                "name": type_obj.local_name,
                "snake_case_name": camel_to_snake(type_obj.local_name),
                "data_type": list(set([xsd_to_python_type(m)["type"] for m in type_obj.member_types])),
                "org_datatype": None,
                "is_array": False,
                "is_optional": False,
                "default_value": default_values.get(f"{ship_type}.{type_obj.local_name.lower()}"),
                "source": "XsdAtomicRestriction",
                "is_enum": False,
                "type_simple": False,
                "is_union": True
            }]
            all_types[source_xsd][ship_type] = {"members": members, "no_attrib_name": True if ship_type in no_attr_name else False}

        else:
            print(f"Not handeled: {ship_type}: {type_name}")

    groups = {}
    group_class = {}

    choice_graph = nx.DiGraph()

    for grp in schema.groups:
        grp_obj = schema.groups[grp]
        #print(f"{folder}-{grp_obj.local_name}")
        group_elements = []

        choice_graph.add_node(grp_obj.local_name)

        for ele in grp_obj.content:
            #print(f"{ele.local_name} - {grp_obj.local_name}")
            groups[ele.local_name] = grp_obj.local_name
            group_elements.append({"name": to_class_name(ele.local_name)})
            choice_graph.add_edge(grp_obj.local_name, ele.local_name)

        group_class[grp_obj.local_name] = {
            "folder": folder,
            "elements": group_elements
        }

    sorted_choices = list(reversed(list(nx.topological_sort(choice_graph))))

    type_2_source = {}
    choice_types = []
    for type_name in sorted_choices:
        if type_name in group_class:
            ch = group_class[type_name]
            ch["name"] = type_name
            choice_types.append(ch)
            type_2_source[type_name] = {
                    "source_path": f"{folder}.choice_class",
                    "source_class": type_name,
                    "type_name": type_name
                }

    # flip DataChoiceGroup and PayloadContributionGroup so PayloadContributionGroup can use DataChoiceGroup
    #group_class[2], group_class[3] = group_class[3], group_class[2]


    all_types_plain = dict_dict_2_dict(all_types)

    elements = []
    msg_type_names = []
    for ele in schema.elements:
        ele_obj = schema.elements[ele]
        #print(f"{ele_obj.local_name}")

        members = []
        if ele_obj.type.local_name in all_types_plain:
            for m in all_types_plain[ele_obj.type.local_name]["members"]:

                members.append({
                    "name": m["name"],
                    "snake_case_name": camel_to_snake(m["name"]),
                    "data_type": m["data_type"],
                    "org_datatype": m["org_datatype"],
                    "default_value": m["default_value"],
                    "is_array": m["is_array"],
                    "is_optional": m["is_optional"],
                    "source": "elements",
                    "is_enum": m["is_enum"],
                    "type_simple": m["type_simple"]
                })
        elif ele_obj.type.local_name in dict_dict_2_dict(enum_types):
            members.append({
                "name": "value",
                "snake_case_name": camel_to_snake("value"),
                "data_type": ele_obj.type.local_name,
                "org_datatype": ele_obj.type.local_name,
                "default_value": None,
                "is_array": False,
                "is_optional": False,
                "source": "elements",
                "is_enum": True,
                "type_simple": False
            })

        data_type = xsd_to_python_type(ele_obj.type)
        elements.append({
            "base_name": to_class_name(ele_obj.local_name),
            "msg_name": ele_obj.local_name,
            "data_type": data_type["type"],
            "msg_type_numeric": msg_group_value(groups.get(ele_obj.local_name)),
            "members": members
        })

        msg_type_names.append(ele_obj.type.local_name)

    data_type_graph = nx.DiGraph()

    # for type_name in all_types:
    #     data_type_graph.add_node(type_name)
    #     for m in all_types[type_name]['members']:
    #         if isinstance(m['data_type'], str):
    #             data_type_graph.add_edge(type_name, m['data_type'])
    #         elif isinstance(m['data_type'], list):
    #             for dt in m['data_type']:
    #                 #print(f"{type_name} - {dt}")
    #                 data_type_graph.add_edge(type_name, dt)
    #
    # sorted_types = list(reversed(list(nx.topological_sort(data_type_graph))))

    #for st in sorted_types:
    #    print(st)

    msg_types = {}
    base_types = {}

    for source_xsd in all_types:
        msg_types[source_xsd] = []
        base_types[source_xsd] = []
        for type_name in all_types[source_xsd]:
            msg = all_types[source_xsd][type_name]
            msg["base_name"] = type_name
            if type_name in msg_type_names:
                msg_types[source_xsd].append(msg)
                type_2_source[type_name] = {
                    "source_path": f"{folder}.message_type.{source_xsd.lower()}",
                    "source_class": type_name,
                    "type_name": type_name
                }
            else:
                base_types[source_xsd].append(msg)
                type_2_source[type_name] = {
                    "source_path": f"{folder}.base_type.{source_xsd.lower()}",
                    "source_class": type_name,
                    "type_name": type_name
                }

    for source_xsd in enum_types:
        for type_name in enum_types[source_xsd]:
            type_2_source[type_name] = {
                "source_path": f"{folder}.enums.{source_xsd.lower()}",
                "source_class": type_name,
                "type_name": type_name
            }


    for source_xsd in enum_types:

        with open(f"{folder}/enums/{source_xsd.lower()}.py", "w") as text_file:
            text_file.write(template_enum.render(
                enum_types=enum_types[source_xsd],
                folder=folder
            ))

    for source_xsd in base_types:

        used_import, sorted_elements = get_imports_and_sort(
            type_list=base_types[source_xsd],
            type_2_source=type_2_source,
            dest_folder=f"{folder}.base_type.{source_xsd.lower()}"
        )

        with open(f"{folder}/base_type/{source_xsd.lower()}.py", "w") as text_file:
            text_file.write(template_message_type.render(
                folder=folder,
                ship_types=sorted_elements,
                is_ship_msg_type=False,
                imports=used_import
            ))

    with open(f"{folder}/base_type/__init__.py", "w") as text_file:
        text_file.write(template_init_module.render(
            element=base_types
        ))

    for source_xsd in msg_types:

        if len(msg_types[source_xsd]) > 0:
            with open(f"{folder}/message_type/{source_xsd.lower()}.py", "w") as text_file:

                used_import, sorted_elements = get_imports_and_sort(
                    type_list=msg_types[source_xsd],
                    type_2_source=type_2_source,
                    dest_folder=f"{folder}.message_type.{source_xsd.lower()}"
                )

                text_file.write(template_message_type.render(
                    ship_types=sorted_elements,
                    is_ship_msg_type=True,
                    imports=used_import+["from spine.message_type.message_type import SpineMessageType"],
                    folder=folder
                ))

    with open(f"{folder}/message_type/__init__.py", "w") as text_file:
        text_file.write(template_init_module.render(
            element=msg_types
        ))

    with open(f"{folder}/message.py", "w") as text_file:

        used_import, sorted_elements = get_imports_and_sort(
            type_list=elements,
            type_2_source=type_2_source,
            dest_folder=f"{folder}.message"
        )

        text_file.write(template_message.render(
            elements=sorted_elements,
            base_types=base_types,
            folder=folder,
            imports=used_import+["from spine.message_type.message_type import SpineMessageType", "from spine.base_message import SpineMessage"],
        ))

    with open(f"{folder}/choice_class.py", "w") as text_file:
        text_file.write(template_choice_class.render(
            group_class=choice_types,
            folder=folder,
            imports=[f"from {folder}.message import *"],
        ))
