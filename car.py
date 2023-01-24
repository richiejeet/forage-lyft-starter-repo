from serviceable import Serviceable

class Car(Serviceable):
    def __init__(self, eng, bat):
        self._engine = eng
        self._battery = bat

    def needs_service(self):
        return self._engine.needs_service() or self._battery.needs_service()
