from __future__ import annotations

import os
from inspect import getframeinfo, stack

from xmlschema import XsdType


class DataType:

    @classmethod
    def can_create(cls, xsd_type: XsdType) -> str | None:
        raise RuntimeError(f"can_create needs to be implemented in {cls.__name__}")

    @classmethod
    def create_from_xsd(cls, xsd_type: XsdType) -> DataType:
        raise RuntimeError(f"create_from_xsd needs to be implemented in {cls.__name__}")

    def __init__(self, type_name, source_file):
        if type_name:
            self.namespace, self.type_name = type_name.split(":")
        else:
            self.namespace = None
            self.type_name = None

        step_back = 1
        caller_file = getframeinfo(stack()[step_back][0]).filename
        while "types.py" in caller_file:
            step_back += 1
            caller_file = getframeinfo(stack()[step_back][0]).filename

        caller = getframeinfo(stack()[step_back][0])
        self.first_creator = f"{caller.filename}:{caller.lineno}"

        self.source_file = source_file
        self.base_source = source_file.replace('EEBus_SPINE_TS_', '').replace('.xsd', '')

        self._module = None
        self._file_name = None
        self._jinja_template = None
        self._import_type = "FULL_PATH"


    @property
    def class_name(self):
        return self.type_name

    @property
    def fq_name(self):
        return f"{self.namespace}:{self.type_name}"

    def set_module(self, module):
        self._module = module

    def get_import(self):
        if self._import_type == "FULL_PATH":
            if self.module and self._file_name and self.class_name:
                return f"from {self.module}.{self._file_name.replace('.py','')} import {self.class_name}"

        return None

    @property
    def module(self):
        return self._module

    def set_file_name(self, file_name):
        self._file_name = eval(f'f"""{file_name}"""')

    def set_jinja_template(self, jinja_template):
        self._jinja_template = jinja_template

    def get_jinja_template(self):
        return self._jinja_template

    def get_full_path(self):
        if self._file_name and self._module:
            return f"{self._module.replace('.',os.sep)}{os.sep}{self._file_name}"
        else:
            return None

    def __eq__(self, other):
        if self.namespace == other.namespace and self.type_name == other.type_name:# and self._is_array == other._is_array:
            if type(self) is not type(other):
                raise RuntimeError(f"Same namespace and name but different types: {self.namespace}:{self.type_name}({type(self).__name__}/{type(other).__name__}) {self.first_creator}")
            return True
        else:
            return False

    def __hash__(self):
        return hash(self.namespace + self.type_name)

    def __str__(self):
        if self.get_full_path():
            return f"{self.namespace}:{self.type_name} ({self.get_full_path()})"
        else:
            return f"{self.namespace}:{self.type_name} (not set)"

    def get_as_code(self):
        pass

    @property
    def depend_on_types(self):
        return []

    @property
    def data_access_method(self):
        return ".get_data()"

    @property
    def return_type(self):
        return "array"

    @property
    def info_comment(self):
        return f"{self.source_file}: {type(self).__name__}"
