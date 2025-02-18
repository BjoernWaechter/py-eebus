import re

import xmlschema
from jinja2 import Environment, FileSystemLoader
import networkx as nx

schemas = [
   # {"file": 'xsd/EEBus_SHIP_TS_TransferProtocol.xsd', "folder": "ship"},
    {"file": 'xsd/EEBus_SPINE_TS_Datagram.xsd', "folder": "spine"}
]


def get_source_name(type_object):
    return type_object.schema.name

def get_default_value(type, attr):
    if type is None or attr is None:
        return None

    return default_values.get(f"{type}.{attr.lower()}")


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

    enum_types = {}
    all_types = {}

    for ship_type in schema.types:
        type_name = type(schema.types[ship_type]).__name__
        type_obj = schema.types[ship_type]
        #print(f"{ship_type} - {type_name}")
        if type_name == "XsdAtomicRestriction" and type_obj.enumeration:
            enum_types[ship_type] = {"enums": type_obj.enumeration}
            print(get_source_name(type_obj))
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

                        all_types[sub_ship_type] = {"members": sub_members, "no_attrib_name": False}
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

            all_types[ship_type] = {"members": members, "no_attrib_name": True if ship_type in no_attr_name else False}

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
            all_types[ship_type] = {"members": members, "no_attrib_name": True if ship_type in no_attr_name else False}

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
            all_types[ship_type] = {"members": members, "no_attrib_name": True if ship_type in no_attr_name else False}

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

    choice_types = []
    for type_name in sorted_choices:
        if type_name in group_class:
            ch = group_class[type_name]
            ch["name"] = type_name
            choice_types.append(ch)

    # flip DataChoiceGroup and PayloadContributionGroup so PayloadContributionGroup can use DataChoiceGroup
    #group_class[2], group_class[3] = group_class[3], group_class[2]



    elements = []
    msg_type_names = []
    for ele in schema.elements:
        ele_obj = schema.elements[ele]
        #print(f"{ele_obj.local_name}")

        members = []
        if ele_obj.type.local_name in all_types:
            for m in all_types[ele_obj.type.local_name]["members"]:

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
        elif ele_obj.type.local_name in enum_types:
            members.append({
                "name": "value",
                "snake_case_name": camel_to_snake("value"),
                "data_type": ele_obj.type.local_name,
                "org_datatype": ele_obj.type.local_name,
                "default_value": None,
                "is_array": False,
                "is_optional": False,
                "source": "elements",
                "is_enum": True if ele_obj.type.local_name in enum_types else False,
                "type_simple": False
            })

        data_type = xsd_to_python_type(ele_obj.type)
        elements.append({
            "name": to_class_name(ele_obj.local_name),
            "msg_name": ele_obj.local_name,
            "data_type": data_type["type"],
            "msg_type_numeric": msg_group_value(groups.get(ele_obj.local_name)),
            "members": members
        })

        msg_type_names.append(ele_obj.type.local_name)

    data_type_graph = nx.DiGraph()

    for type_name in all_types:
        data_type_graph.add_node(type_name)
        for m in all_types[type_name]['members']:
            if isinstance(m['data_type'], str):
                data_type_graph.add_edge(type_name, m['data_type'])
            elif isinstance(m['data_type'], list):
                for dt in m['data_type']:
                    #print(f"{type_name} - {dt}")
                    data_type_graph.add_edge(type_name, dt)

    sorted_types = list(reversed(list(nx.topological_sort(data_type_graph))))

    #for st in sorted_types:
    #    print(st)

    msg_types = []
    base_types = []
    for type_name in sorted_types:
        if type_name in all_types:
            msg = all_types[type_name]
            msg["base_name"] = type_name
            if type_name in msg_type_names and folder == "ship":
                msg_types.append(msg)
            else:
                base_types.append(msg)

    #for ct in base_types:
    #    print(ct["base_name"])

    with open(f"{folder}/enums.py", "w") as text_file:
        text_file.write(template_enum.render(
            enum_types=enum_types,
            folder=folder
        ))

    with open(f"{folder}/base_type.py", "w") as text_file:
        text_file.write(template_message_type.render(
            folder=folder,
            ship_types=base_types,
            is_ship_msg_type=False,
            imports=[f"from {folder}.enums import *", f"from {folder}.choice_class import *"]
        ))

    with open(f"{folder}/message_type.py", "w") as text_file:
        text_file.write(template_message_type.render(
            ship_types=msg_types,
            is_ship_msg_type=True,
            imports=[f"from {folder}.base_type import *", f"from {folder}.enums import *"] if folder == "ship" else
            [f"from {folder}.base_type import *", f"from {folder}.enums import *",
             f"from {folder}.choice_class import *"],
            folder=folder
        ))

    with open(f"{folder}/message.py", "w") as text_file:
        text_file.write(template_message.render(
            elements=elements,
            base_types=base_types,
            folder=folder,
            imports=[f"from {folder}.enums import *"] if folder == "ship" else[],
        ))

    with open(f"{folder}/choice_class.py", "w") as text_file:
        text_file.write(template_choice_class.render(
            group_class=choice_types,
            folder=folder,
            imports=[f"from {folder}.message import *"],
        ))
