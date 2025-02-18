from ship.message import *


class HandleAccessMethods:

    def __init__(self, con):
        self._con = con
        self._request_send = False

    @property
    def request_send(self):
        return self._request_send

    def handle_state(self, msg: ShipMessage) -> bool:

        if self._request_send is False:
            self._con.send_message(AccessMethodsRequest())
            self._request_send = True
            return False

        elif isinstance(msg, AccessMethodsRequest):
            self._con.send_message(AccessMethods(id=self._con._local_device.name))
            return False








