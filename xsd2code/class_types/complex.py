from __future__ import annotations

from xmlschema import XsdType
from xmlschema.validators import XsdComplexType, XsdGroup

import xsd2code


class ComplexType(xsd2code.DataType):

    @classmethod
    def can_create(cls, xsd_type: XsdType):
        if isinstance(xsd_type, XsdComplexType):
            return xsd_type.display_name

        return None

    @classmethod
    def create_from_xsd(cls, xsd_type: XsdComplexType) -> xsd2code.ComplexType:

        comp_type = xsd2code.ComplexType(
            type_name=xsd_type.display_name,
            source_file=xsd_type.schema.name
        )
        # print(f"-------- {xsd_type.display_name} --------")
        if hasattr(xsd_type, "base_type") and hasattr(xsd_type.base_type, "display_name"):
            # print(f" create from basetype: {xsd_type.base_type.display_name}")
            comp_type.set_base_type(xsd2code.ALL_TYPES.get_or_create(xsd2code.create_type_from_xsd(xsd_type.base_type)))
            # print(f"-------- back  {xsd_type.display_name} --------")

        added_members = []
        if hasattr(xsd_type, "content"):
            if hasattr(xsd_type.content, "content"):
                for mem in xsd_type.content.content:

                    # print(f" - {mem}")

                    if hasattr(mem, "type") and mem.type.display_name:
                        # print(f"create mem {xsd_type.display_name}.{mem.display_name}")
                        added_members.append(mem.display_name)
                        mem_type = xsd2code.create_type_from_xsd(mem.type)
                        comp_type.add_member(xsd2code.Member(
                            fq_member_name=mem.display_name,
                            data_type=xsd2code.ALL_TYPES.get_or_create(mem_type),
                            is_optional=True if mem.min_occurs == 0 else False,
                            is_array=True if mem.max_occurs is None or mem.max_occurs > 1 else False
                        ))

                    if isinstance(mem, XsdGroup) and hasattr(mem, "display_name") and mem.display_name:
                        comp_type.add_group_type(
                            xsd2code.ALL_TYPES.get_or_create(xsd2code.create_type_from_xsd(mem))
                        )

                    if hasattr(mem, "content"):
                        for mem_ref in mem.content:
                            if hasattr(mem_ref, "display_name") and hasattr(mem_ref, "type"):
                                # print(f"create ref {comp_type.type_name}.{mem_ref.display_name}")
                                comp_type.add_member(xsd2code.Member(
                                    fq_member_name=mem_ref.display_name,
                                    data_type=xsd2code.ALL_TYPES.get_or_create(xsd2code.create_type_from_xsd(mem_ref.type)),
                                    is_optional=True,  # TODO: Try to figure out where this information is stored
                                    is_array=True if mem_ref.max_occurs is None or mem_ref.max_occurs > 1 else False
                                ))
                                # added_members.append(mem_ref.ref.display_name)

        return comp_type

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
