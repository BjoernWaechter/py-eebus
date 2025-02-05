import time

import pytest

from ship.timer import ShipTimer


class TestTimer:

    def test_init(self):

        timer = ShipTimer()
        assert timer.is_running is False

    def test_not_expired(self):

        timer = ShipTimer(2)
        timer.start()
        time.sleep(1)
        assert timer.is_expired() is False

    def test_expired(self):

        timer = ShipTimer(1)
        timer.start()
        time.sleep(2)
        assert timer.is_expired() is True

    def test_time_not_set(self):

        timer = ShipTimer()
        with pytest.raises(RuntimeError):
            timer.start()

        timer.set_duration(1)
        timer.start()
        assert timer.is_expired() is False

    def test_time_left(self):

        timer = ShipTimer(2)
        timer.start()
        time.sleep(1)
        assert int(round(timer.get_time_left())) == 1