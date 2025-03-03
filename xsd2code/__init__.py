import re

from .class_types.data_type import DataType
from .types import create_type_from_xsd
from .class_types.base import BaseType
from .class_types.union import UnionType
from .class_types.choice import ChoiceType
from .class_types.enum import EnumType
from .class_types.alias import AliasType
from .class_types.complex import ComplexType
from .type_list import ALL_TYPES
from .member import Member


def to_snake_case(var_name):
    name = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', var_name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', name).lower()