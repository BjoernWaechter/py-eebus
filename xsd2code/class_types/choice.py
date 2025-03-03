from __future__ import annotations

from xmlschema import XsdType, XsdElement
from xmlschema.validators import XsdGroup

import xsd2code


class ChoiceType(xsd2code.DataType):

    @classmethod
    def can_create(cls, xsd_type: XsdType):
        if isinstance(xsd_type, XsdGroup):
            return xsd_type.display_name

        return None

    @classmethod
    def create_from_xsd(cls, xsd_type: XsdGroup) -> xsd2code.ChoiceType:

        group_type = xsd2code.ChoiceType(
            type_name=xsd_type.display_name,
            source_file=xsd_type.schema.name
        )

        for ele in xsd_type.content:
            # print(f"   -{ele.display_name} {type(ele).__name__}")
            if isinstance(ele, XsdElement):
                group_type.add_choice_member(
                    xsd2code.Member(
                        fq_member_name=ele.display_name,
                        data_type=xsd2code.ALL_TYPES.get_or_create(xsd2code.create_type_from_xsd(ele.type)),
                        is_optional=True if ele.min_occurs == 0 else False,
                        is_array=True if ele.max_occurs is None or ele.max_occurs > 1 else False
                    )
                )
            elif isinstance(ele, XsdGroup):
                group_type.add_choice_type(
                    xsd2code.ALL_TYPES.get_or_create(
                        #xsd2code.ChoiceType(type_name=ele.display_name, source_file=ele.schema.name)
                        xsd2code.ALL_TYPES.get_or_create(xsd2code.create_type_from_xsd(ele))
                    )
                )

        return group_type

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
        result = self._choice_members.copy()
        for ct in self._choice_types:
            result += ct.members
        return result

    @property
    def depend_on_types(self):
        return [t._data_type for t in self.members]
