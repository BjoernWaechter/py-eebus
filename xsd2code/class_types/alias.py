from __future__ import annotations

from xmlschema import XsdType

import xsd2code
from xmlschema.validators import XsdAtomicRestriction


class AliasType(xsd2code.DataType):

    @classmethod
    def can_create(cls, xsd_type: XsdType):
        if isinstance(xsd_type, XsdAtomicRestriction) and not xsd_type.enumeration:
            return xsd_type.display_name

        return None

    @classmethod
    def create_from_xsd(cls, xsd_type: XsdAtomicRestriction) -> xsd2code.AliasType:

        return xsd2code.AliasType(
            type_name=xsd_type.display_name,
            source_file=xsd_type.schema.name,
            base_type=xsd2code.ALL_TYPES.get_or_create(xsd2code.create_type_from_xsd(xsd_type.base_type))
        )

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

    @property
    def depend_on_types(self):
        return [t._data_type for t in self.members]

    def get_as_code(self):
        return self.type_name

    @property
    def return_type(self):
        return "value"
