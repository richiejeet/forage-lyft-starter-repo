from battery import Battery


class SpindlerBattery(Battery):
    def __init__(self, current_date, last_service_date):
        self._current_date = current_date
        self._last_service_date = last_service_date
        self._spindler_year_needs_service = 3

    def needs_service(self):
        date_needs_service = self._last_service_date.replace(year=self._last_service_date.year + self._spinder_year_needs_service)
        if date_needs_service < self._current_date:
            return True
        else:
            return False