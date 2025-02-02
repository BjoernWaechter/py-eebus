import re

import xmlschema
from jinja2 import Environment, FileSystemLoader

schema = xmlschema.XMLSchema('xsd/EEBus_SHIP_TS_TransferProtocol.xsd')


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

def camel_to_snake(name):
    name = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', name).lower()


def xsd_to_python_type(xsd_type):
    if xsd_type == "xs:unsignedInt":
        return {"type": "int", "simple": True}
    elif xsd_type == "xs:unsignedByte":
        return {"type": "int", "simple": True}
    elif xsd_type == "xs:boolean":
        return {"type": "bool", "simple": True}
    elif xsd_type == "xs:string":
        return {"type": "str", "simple": True}
    elif xsd_type == "xs:anyType":
        return {"type": "", "simple": True}
    elif xsd_type == "xs:decimal":
        return {"type": "float", "simple": True}
    elif xsd_type == "xs:hexBinary":
        return {"type": "str", "simple": True}
    if xsd_type == "xs:unsignedShort":
        return {"type": "int", "simple": True}
    elif xsd_type is None:
        return {"type": "", "simple": True}
    else:
        return {"type": f"{xsd_type.replace('ship:','')}", "simple": False}


# Section: 13.4.2
def msg_group_value(group_name):
    if group_name == "MsgTypeControlGroup":
        return "MessageType.MSG_TYPE_CONTROL"
    elif group_name == "MsgTypeDataGroup":
        return "MessageType.MSG_TYPE_DATA"
    elif group_name == "MsgTypeEndGroup":
        return "MessageType.MSG_TYPE_END"


env = Environment(loader=FileSystemLoader("templates/"))

template_enum = env.get_template("enums.py.jinja2")
template_message_type = env.get_template("message_type.py.jinja2")
template_message = env.get_template("message.py.jinja2")

enum_types = {}
all_types = {}

msg_types = {}
base_types = {}

for ship_type in schema.types:
    type_name = type(schema.types[ship_type]).__name__
    type_obj = schema.types[ship_type]

    if type_name == "XsdAtomicRestriction" and type_obj.enumeration:
        enum_types[ship_type] = {"enums": type_obj.enumeration}
    elif type_name == "XsdComplexType":
        #print(f"{ship_type}")

        members = []
        for m in type_obj.content.content:
            #print(f"  {m.local_name} - {m.type.display_name}")
            sub_ship_type = None
            if hasattr(m.type, "content") and not m.type.display_name:
                #print("   ---- subtype found")
                sub_ship_type = attr_2_type[f"{ship_type}.{m.local_name}"]
                sub_members = []
                for sub_m in m.type.content.content:
                    data_type = xsd_to_python_type(sub_m.type.display_name)
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
            #    print(f"    {m.type.display_name}")
            data_type = {"type": sub_ship_type, "simple": False} if sub_ship_type else xsd_to_python_type(m.type.display_name)
            members.append(
                {
                    "name": m.local_name,
                    "snake_case_name": camel_to_snake(m.local_name),
                    "data_type": data_type["type"],
                    "org_datatype": m.type.display_name,
                    "is_array": True if m.max_occurs is None or m.max_occurs > 1 else False,
                    "is_optional": True if m.min_occurs == 0 else False,
                    "default_value": default_values.get(f"{ship_type}.{m.local_name.lower()}"),
                    "source": "XsdComplexType",
                    "is_enum": True if data_type["type"] in enum_types else False,
                    "type_simple": data_type["simple"]
                }
            )

        all_types[ship_type] = {"members": members, "no_attrib_name": True if ship_type in no_attr_name else False}

    elif type_name == "XsdAtomicRestriction":
        print(f"{ship_type} {type_obj.local_name} {type_obj.base_type.display_name}")
        data_type = xsd_to_python_type(type_obj.base_type.display_name)
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
    else:
        print(f"Not handeled: {ship_type}: {type_name}")

groups = {}

for grp in schema.groups:
    grp_obj = schema.groups[grp]
    for ele in grp_obj.content:
        #print(f"{ele.local_name} - {grp_obj.local_name}")
        groups[ele.local_name] = grp_obj.local_name

elements = []
msg_type_names = []
for ele in schema.elements:
    ele_obj = schema.elements[ele]
    #print(f"{ele_obj.local_name} - {groups[ele_obj.local_name]}({ele_obj.min_occurs}/{ele_obj.max_occurs})")

    members = []
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

    elements.append({
        "name": ele_obj.local_name[0].upper() + ele_obj.local_name[1:],
        "msg_name": ele_obj.local_name,
        "data_type": ele_obj.type.local_name,
        "msg_type_numeric": msg_group_value(groups[ele_obj.local_name]),
        "members": members
    })




    msg_type_names.append(ele_obj.type.local_name)

for type_name in all_types:
    if type_name in msg_type_names:
        msg_types[type_name] = all_types[type_name]
    else:
        base_types[type_name] = all_types[type_name]

with open("ship/enums.py", "w") as text_file:
    text_file.write(template_enum.render(enum_types=enum_types))

with open("ship/base_type.py", "w") as text_file:
    text_file.write(template_message_type.render(
        ship_types=base_types,
        is_ship_msg_type=False,
        imports=[]))

with open("ship/message_type.py", "w") as text_file:
    text_file.write(template_message_type.render(
        ship_types=msg_types,
        is_ship_msg_type=True,
        imports=["from ship.base_type import *","from ship.enums import *"]
    ))

with open("ship/message.py", "w") as text_file:
    text_file.write(template_message.render(elements=elements))
