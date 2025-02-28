from __future__ import annotations

from xmlschema import XsdType
from xmlschema.validators import XsdAtomicRestriction

import xsd2code


class EnumType(xsd2code.DataType):

    @classmethod
    def can_create(cls, xsd_type: XsdType):
        if isinstance(xsd_type, XsdAtomicRestriction) and xsd_type.enumeration:
            return xsd_type.display_name

        return None

    @classmethod
    def create_from_xsd(cls, xsd_type: XsdAtomicRestriction) -> xsd2code.EnumType:
        return xsd2code.EnumType(
            type_name=xsd_type.display_name,
            source_file=xsd_type.schema.name,
            enum_values=xsd_type.enumeration
        )

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
