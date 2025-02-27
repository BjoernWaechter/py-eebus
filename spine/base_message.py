from dataclasses import dataclass
import json

from spine import SpineMessageType
from spine.base_type.datagram import DatagramType



def get_object_data(obj):
    return obj.get_data()


@dataclass()
class SpineMessage:
    def __init__(
            self,
            datagram: DatagramType
    ):
        self._root_tag = "datagram"
        
        self._msg: datagram

    def get_msg_bytes(self):
        json_data = self.get_data()
        data_bytes = json_data.encode('utf8')
        return data_bytes

    @classmethod
    def from_data(cls, bin_msg):
        first_byte = bin_msg[0:1]
        
        data = json.loads(bin_msg[1:].decode("utf8"))
        root_tag = list(data.keys())[0]
        msg = ROOT_TAG_2_TYPE[root_tag].from_data(data[root_tag])

        return msg

    def get_data(self):
        if self._msg:
            return json.dumps({self._root_tag: self._msg.get_data()}, separators=(',', ':'), default=get_object_data)
        else:
            return ""

    def __str__(self):
        return f"{self.__class__.__name__}, {self._msg})"

    def msg(self):
        return self._msg


ROOT_TAG_2_TYPE = {}