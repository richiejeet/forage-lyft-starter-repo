import unittest
from datetime import datetime

from battery.battery_types.nubbin_battery import NubbinBattery
from battery.battery_types.spindler_battery import SpindlerBattery


class TestNubbinBattery(unittest.TestCase):
    def test_needs_service_true(self):
        current_date = datetime.today().date()
        last_service_date = datetime(2018, 1, 9)
        bat = NubbinBattery(current_date, last_service_date)
        self.assertTrue(bat.needs_service())

    def test_needs_service_False(self):
        current_date = datetime.today().date()
        last_service_date = datetime(2020, 11, 9)
        bat = NubbinBattery(current_date, last_service_date)
        self.assertFalse(bat.needs_service())


class TestSpindlerBattery(unittest.TestCase):
    def test_needs_service_true(self):
        current_date = datetime.today().date()
        last_service_date = datetime(2020, 1, 9)
        bat = SpindlerBattery(current_date, last_service_date)
        self.assertTrue(bat.needs_service())

    def test_needs_service_False(self):
        current_date = datetime.today().date()
        last_service_date = datetime(2021, 11, 9)
        bat = SpindlerBattery(current_date, last_service_date)
        self.assertFalse(bat.needs_service())