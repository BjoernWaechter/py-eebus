import inspect

from xmlschema import XsdElement
from xmlschema.validators import XsdAtomicRestriction, XsdType, XsdComplexType, XsdAtomicBuiltin, XsdUnion, XsdGroup

import xsd2code
from xsd2code.class_types.base import BaseType


def show_selected_attr(obj, interest, depth=0):
    spaces = "    "
    for attr in dir(obj):
        if attr in interest:
            value = getattr(obj, attr)
            #print(value)
            if hasattr(value, "__dict__"):
                print(f"{spaces * depth}{attr}(obj):")
                show_selected_attr(value, interest, depth + 1)
            elif isinstance(value, list):

                for idx in range(len(value)):
                    print(f"{spaces * depth}{attr}[{idx}]:")
                    show_selected_attr(value[idx], interest, depth + 1)
            elif value:
                print(f"{spaces * depth}{attr}: {value}")


def get_data_classes():
    """Yield the classes in module ``mod`` that inherit from ``cls``"""
    for name, obj in inspect.getmembers(xsd2code):
        if hasattr(obj, "__bases__") and xsd2code.DataType in obj.__bases__:
            yield obj


def create_type_from_xsd(xsd_type: XsdType):

    for data_class in get_data_classes():
        fq_name = data_class.can_create(xsd_type)

        if fq_name:

            res_type = xsd2code.ALL_TYPES.get_by_name(fq_name, throw_exe=False)

            if res_type:
                return res_type
            else:
                res_type = data_class.create_from_xsd(xsd_type)
                return res_type

    raise RuntimeError(f"Unknown XsdType: {xsd_type.display_name}-{type(xsd_type).__name__}")