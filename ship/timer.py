import time


class ShipTimer:

    def __init__(self, duration_sec=0):
        self.duration_sec = duration_sec
        self.start_time = 0
        self.is_running = False

    def start(self):
        if self.duration_sec <= 0:
            raise RuntimeError("time_sec has to be initialized with a value greater than zero")
        self.start_time = time.time()
        self.is_running = True

    def stop(self):
        self.start_time = 0
        self.is_running = False

    def set_duration(self, duration_sec):
        self.duration_sec = duration_sec

    def is_expired(self):

        if self.is_running is False:
            return False
        elif time.time() > self.start_time + self.duration_sec:
            return True
        else:
            return False
