import unittest
from datetime import datetime
# import battery
# import engine
#from carfactory import CarFactory
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine

class TestNubbinBattery(unittest.TestCase):
    def needs_service(self):
        current_date = datetime(2020, 1, 1)
        last_service_date = datetime(2015, 1, 1)
        battery = NubbinBattery(last_service_date, current_date)
        self.assertTrue(battery.service_needed())

    def doesnot_need_service(self):
        current_date = datetime(2020, 1, 1)
        last_service_date = datetime(2019, 1, 1)
        battery = NubbinBattery(last_service_date, current_date)
        self.assertFalse(battery.service_needed())

class TestSpindlerBattery(unittest.TestCase):
    def needs_service(self):
        current_date = datetime(2020, 1, 5)
        last_service_date = datetime(2018, 1, 1)
        battery = SpindlerBattery(last_service_date, current_date)
        self.assertTrue(battery.service_needed())

    def doesnot_need_service(self):
        current_date = datetime(2020, 1, 1)
        last_service_date = datetime(2019, 1, 1)
        battery = SpindlerBattery(last_service_date, current_date)
        self.assertFalse(battery.service_needed())

class TestCapuletEngine(unittest.TestCase):
    def needs_service(self):
        current_mileage = 70002
        last_service_mileage = 40000
        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.service_needed())

    def doesnot_need_service(self):
        current_mileage = 69000
        last_service_mileage = 50000
        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.service_needed())

class TestSternmanEngine(unittest.TestCase):
    def needs_service(self):
        warning_light_is_on = True
        engine = SternmanEngine(warning_light_is_on)
        self.assertTrue(engine.service_needed())

    def doesnot_need_service(self):
        warning_light_is_on = False
        engine = SternmanEngine(warning_light_is_on)
        self.assertFalse(engine.service_needed())

class TestWilloughbyEngine(unittest.TestCase):
    def needs_service(self):
        current_mileage = 100002
        last_service_mileage = 40000
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.service_needed())

    def doesnot_need_service(self):
        current_mileage = 69000
        last_service_mileage = 10000
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.service_needed())

if __name__ == '__main__':
    unittest.main()