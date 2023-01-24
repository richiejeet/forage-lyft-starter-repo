from car import Car

from battery.battery_types.nubbin_battery import NubbinBattery
from battery.battery_types.spindler_battery import SpindlerBattery

from engine.engine_type.capulet_engine import CapuletEngine
from engine.engine_type.sternman_engine import SternmanEngine
from engine.engine_type.willoughby_engine import WilloughbyEngine


class CarFactory:

    @staticmethod
    def create_calliope(self, current_date, last_service_date, current_mileage, last_service_mileage):
        eng = CapuletEngine(current_mileage, last_service_mileage)
        bat = SpindlerBattery(current_date, last_service_date)
        car = Car(eng, bat)
        return car

    @staticmethod
    def create_glissade(self, current_date, last_service_date, current_mileage, last_service_mileage):
        eng = WilloughbyEngine(current_mileage, last_service_mileage)
        bat = SpindlerBattery(current_date, last_service_date)
        car = Car(eng, bat)
        return car

    @staticmethod
    def create_rorschach(self, current_date, last_service_date, current_mileage, last_service_mileage):
        eng = WilloughbyEngine(current_mileage, last_service_mileage)
        bat = NubbinBattery(current_date, last_service_date)
        car = Car(eng, bat)
        return car

    @staticmethod
    def create_thovex(self, current_date, last_service_date, current_mileage, last_service_mileage):
        eng = CapuletEngine(current_mileage, last_service_mileage)
        bat = NubbinBattery(current_date, last_service_date)
        car = Car(eng, bat)
        return car

    @staticmethod
    def create_palindrome(self, current_date, last_service_date, warning_light_on):
        eng = SternmanEngine(warning_light_on)
        bat = SpindlerBattery(current_date, last_service_date)
        car = Car(eng, bat)
        return car