from typing import cast

from ship.message import *
from ship.states import *
from ship.timer import ShipTimer


class HelloState(Enum):
    NO_STATE = auto()
    SME_HELLO_STATE_READY = auto()
    SME_HELLO_STATE_PENDING = auto()


# Ship section 13.4.3 & 13.4.4.1.3
class HelloSubState(Enum):
    SME_HELLO_STATE_READY_INIT = auto()
    SME_HELLO_STATE_READY_LISTEN = auto()
    SME_HELLO_STATE_OK = auto()
    SME_HELLO_STATE_READY_TIMEOUT = auto()

    SME_HELLO_STATE_PENDING_INIT = auto()
    SME_HELLO_STATE_PENDING_LISTEN = auto()
    SME_HELLO_STATE_PENDING_TIMEOUT = auto()


class HandleHello:

    def __init__(
            self,
            con,
            partner_known: bool,
            t_hello_init: float = 60
    ):
        self.con = con
        if partner_known:
            self._hello_state: HelloState = HelloState.SME_HELLO_STATE_READY
            self._hello_sub_state: HelloSubState = HelloSubState.SME_HELLO_STATE_READY_INIT
        else:
            self._hello_state: HelloState = HelloState.SME_HELLO_STATE_PENDING
            self._hello_sub_state: HelloSubState = HelloSubState.SME_HELLO_STATE_PENDING_INIT

        self._timer_wait_for_ready = ShipTimer(duration_sec=t_hello_init)
        self._timer_prolongation_request = ShipTimer()
        self._timer_prolongation_reply = ShipTimer()
        self._t_hello_prolong_thr_inc = 30
        self._t_hello_prolong_waiting_gap = 15
        self._t_hello_prolong_min = 1

    def set_hello_state(self, state: HelloState):
        self._hello_state = state

    def set_hello_sub_state(self, sub_state: HelloSubState):
        self._hello_sub_state = sub_state

    @property
    def hello_state(self):
        return self._hello_state

    @property
    def hello_sub_state(self):
        return self._hello_sub_state

    def start_handler(self):
        self._timer_wait_for_ready.start()
        self._timer_prolongation_request.stop()
        self._timer_prolongation_reply.stop()

    def handle_state(self, msg: ShipMessage) -> bool:
        print(f"handle helo state: {self.hello_state}/{self.hello_sub_state}")

        if self.hello_state == HelloState.SME_HELLO_STATE_READY:
            if self.hello_sub_state == HelloSubState.SME_HELLO_STATE_READY_INIT:

                return self.handle_state_sme_hello_state_ready_init()

            elif self.hello_sub_state == HelloSubState.SME_HELLO_STATE_READY_LISTEN:

                return self.handle_state_sme_hello_state_ready_listen(msg)

            elif self.hello_sub_state == HelloSubState.SME_HELLO_STATE_OK:

                self.con.set_con_state(ConState.PROTOCOL_HANDSHAKE)
                return True

        elif self.hello_state == HelloState.SME_HELLO_STATE_PENDING:
            if self.hello_sub_state == HelloSubState.SME_HELLO_STATE_PENDING_INIT:

                # TODO Server mode
                return self.handle_state_sme_hello_state_pending_init()

            elif self.hello_sub_state == HelloSubState.SME_HELLO_STATE_PENDING_LISTEN:

                return self.handle_state_sme_hello_state_pending_listen(msg)

            elif self.hello_sub_state == HelloSubState.SME_HELLO_STATE_OK:

                self.con.set_con_state(ConState.PROTOCOL_HANDSHAKE)
                return True

            else:
                print("Message not handled")
                return False

        else:
            return False

    def send_hello_update_msg(self):

        self.con.send_message(
            ConnectionHello(
                phase=ConnectionHelloPhaseType.READY if self._hello_state == HelloState.SME_HELLO_STATE_READY
                else ConnectionHelloPhaseType.PENDING,
                waiting=int(round(self._timer_wait_for_ready.get_time_left())) * 1000
            )
        )

    # State READY methods:
    def handle_state_sme_hello_state_ready_init(self):
        self._timer_wait_for_ready.start()
        self._timer_prolongation_request.stop()
        self._timer_prolongation_reply.stop()
        self.send_hello_update_msg()
        self.set_hello_sub_state(HelloSubState.SME_HELLO_STATE_READY_LISTEN)
        return False

    def handle_state_sme_hello_state_ready_listen(self, msg: ShipMessage):
        if not isinstance(msg, ConnectionHello):
            print(f"Wrong message type expected: ConnectionHello received: {type(msg)}")
            self.abort()
            return False

        if msg.msg().phase == ConnectionHelloPhaseType.READY:
            self.set_hello_sub_state(HelloSubState.SME_HELLO_STATE_OK)
            return True

        elif msg.msg().phase != ConnectionHelloPhaseType.PENDING:
            print(f"Ignoring message with phase: {msg.msg().phase}")
            return False

        elif msg.msg().phase != ConnectionHelloPhaseType.ABORTED:
            self.abort()
            return False

        return False

    # State PENDING methods:
    def handle_state_sme_hello_state_pending_init(self):
        self.con.send_message(ConnectionHello(phase=ConnectionHelloPhaseType.READY))
        self.set_hello_sub_state(HelloSubState.SME_HELLO_STATE_PENDING_LISTEN)
        return False

    def handle_state_sme_hello_state_pending_listen(self, msg: ShipMessage):
        if not isinstance(msg, ConnectionHello):
            print(f"Wrong message type expected: ConnectionHello received: {type(msg)}")
            self.abort()
            return False

        if msg.msg().phase == ConnectionHelloPhaseType.READY and msg.msg().waiting is not None:
            self._timer_wait_for_ready.stop()
            self._timer_prolongation_reply.stop()
            if msg.msg().waiting >= self._t_hello_prolong_thr_inc:
                new_wait_time = msg.msg().waiting - self._t_hello_prolong_waiting_gap
                if new_wait_time < self._t_hello_prolong_min:
                    self._timer_prolongation_request.stop()
                else:
                    self._timer_prolongation_request.set_duration(new_wait_time)
                    self._timer_prolongation_request.start()
            else:
                self._timer_prolongation_request.stop()

            print(f"Waiting should be set in in phase pending: {msg.msg().phase}")
            return False

        if msg.msg().phase != ConnectionHelloPhaseType.READY:
            print(f"Wrong message value expected READY received: {msg.msg().phase}")
            self.con.close()
            return False

        self.set_hello_sub_state(HelloSubState.SME_HELLO_STATE_OK)
        return True

    def abort(self):
        self._timer_wait_for_ready.stop()
        self._timer_prolongation_request.stop()
        self._timer_prolongation_reply.stop()
        self.con.send_message(ConnectionHello(phase=ConnectionHelloPhaseType.ABORTED))
        self.con.close()
