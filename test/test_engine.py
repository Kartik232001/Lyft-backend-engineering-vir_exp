import unittest

from engine.engine_type.capulet_engine import CapuletEngine
from engine.engine_type.willoughby_engine import WilloughbyEngine
from engine.engine_type.sternman_engine import SternmanEngine 


class TestCapuletEngine(unittest.TestCase):

    def test_needs_service_true(self):
        current_mileage = 120000
        last_service_mileage = 40000
        engine = CapuletEngine(current_mileage=current_mileage, last_service_mileage=last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_needs_service_true(self):
        current_mileage = 40000
        last_service_mileage = 20000
        engine = CapuletEngine(current_mileage=current_mileage, last_service_mileage=last_service_mileage)
        self.assertFalse(engine.needs_service())


class TestWilloughbyEngine(unittest.TestCase):

    def test_needs_service_true(self):
        current_mileage = 120000
        last_service_mileage = 40000
        engine = WilloughbyEngine(current_mileage=current_mileage, last_service_mileage=last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_needs_service_true(self):
        current_mileage = 40000
        last_service_mileage = 20000
        engine = WilloughbyEngine(current_mileage=current_mileage, last_service_mileage=last_service_mileage)
        self.assertFalse(engine.needs_service())


class TestSternmanEngine(unittest.TestCase):

    def test_needs_service_true(self):
        warning_light_is_on = True
        engine = SternmanEngine(warning_light_is_on=warning_light_is_on)
        self.assertTrue(engine.needs_service())

    def test_needs_service_true(self):
        warning_light_is_on = False
        engine = SternmanEngine(warning_light_is_on=warning_light_is_on)
        self.assertFalse(engine.needs_service())


if __name__ == '__main__':
    unittest.main()