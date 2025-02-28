from __future__ import annotations

from xmlschema import XsdType
from xmlschema.validators import XsdUnion

import xsd2code


class UnionType(xsd2code.DataType):

    @classmethod
    def can_create(cls, xsd_type: XsdType):
        if isinstance(xsd_type, XsdUnion):
            return xsd_type.display_name

        return None

    @classmethod
    def create_from_xsd(cls, xsd_type: XsdUnion) -> xsd2code.UnionType:

        union_type = xsd2code.UnionType(
            type_name=xsd_type.display_name,
            source_file=xsd_type.schema.name
        )

        # TODO: Add members
        return union_type

    def __init__(self, type_name, source_file, union_type_list: list[xsd2code.DataType] = None):
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
