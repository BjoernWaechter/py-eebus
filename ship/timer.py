import time


class ShipTimer:

    def __init__(self, duration_sec=0):
        self.duration_sec = duration_sec
        self._start_time = 0
        self._is_running = False

    def start(self):
        if self.duration_sec <= 0:
            raise RuntimeError("time_sec has to be initialized with a value greater than zero")
        self._start_time = time.time()
        self._is_running = True

    def start_if_not_running(self):
        if self._start_time == 0:
            self.start()

    def stop(self):
        self._start_time = 0
        self._is_running = False

    def set_duration(self, duration_sec):
        self.duration_sec = duration_sec

    def get_time_left(self) -> float:
        if self._start_time == 0:
            return None
        else:
            return self.duration_sec-(time.time() - self._start_time)

    def is_expired(self):

        if self._is_running is False:
            return False
        elif time.time() > self._start_time + self.duration_sec:
            return True
        else:
            return False

    def is_running(self):
        return self._is_running
