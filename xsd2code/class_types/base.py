from __future__ import annotations

from xmlschema import XsdType
from xmlschema.validators import XsdAtomicRestriction, XsdAtomicBuiltin

import xsd2code


class BaseType(xsd2code.DataType):

    @classmethod
    def can_create(cls, xsd_type: XsdType):

        if isinstance(xsd_type, XsdAtomicBuiltin) and xsd_type.display_name.split(":")[0] == "xs":
            return xsd_type.display_name

        return None

    @classmethod
    def create_from_xsd(cls, xsd_type: XsdAtomicBuiltin) -> xsd2code.BaseType:

        return BaseType(
            type_name=xsd_type.display_name,
            source_file=xsd_type.schema.name,
        )

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
