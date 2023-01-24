from tire.tire import Tire


class OctoprimeTires(Tire):
    def __init__(self, tire_wear):
        self._tire_wear = tire_wear
        self._tire_need_to_service = 3.0

    def needs_service(self):
        return sum(self._tire_wear) >= self._tire_need_to_service

