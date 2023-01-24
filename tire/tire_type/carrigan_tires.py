from tire.tire import Tire

class CarriganTires(Tire):
    def __init__(self, tire_wear):
        self._tire_wear = tire_wear
        self._tire_need_to_service = 0.9

    def needs_service(self):
        for tire in self._tire_wear:
            if tire >= self._tire_need_to_service:
                return True
        return False
