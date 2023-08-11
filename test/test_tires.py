import unittest

from tires.tires_type.carrigan import CarriganTires
from tires.tires_type.octoprime import OctoprimeTires


class TestCarriganTires(unittest.TestCase):
    def test_needs_service_true(self):
        tires_wear = [0.3, 0.2, 0.9, 0.1]
        tires = CarriganTires(tires_wear)
        self.assertTrue(tires.needs_service())

    def test_needs_service_false(self):
        tires_wear = [0.3, 0.2, 0.8, 0.1]
        tires = CarriganTires(tires_wear)
        self.assertFalse(tires.needs_service())


class TestOctoprimeTires(unittest.TestCase):
    def test_needs_service_true(self):
        tires_wear = [1, 2, 3, 4]
        tires = CarriganTires(tires_wear)
        self.assertTrue(tires.needs_service())

    def test_needs_service_false(self):
        tires_wear = [0.3, 0.2, 0.8, 0.1]
        tires = OctoprimeTires(tires_wear)
        self.assertFalse(tires.needs_service())


if __name__ == '__main__':
    unittest.main()