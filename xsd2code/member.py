from xsd2code.types import DataType


class Member:

    def __init__(self, member_name, data_type: DataType, is_optional=False, default_value=None):
        self._member_name = member_name
        self._data_type = data_type
        self._is_optional = is_optional
        self._default_value = default_value
