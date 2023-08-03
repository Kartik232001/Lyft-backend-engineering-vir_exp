from battery.battery import Battery

class NubbinBattery(Battery):
    def __init__(self, current_date, last_service_date):
        self.current_date = current_date
        self.last_service_date = last_service_date
        self.nubbin_year_need_service = 4

    def needs_service(self):
        date_need_service = self.last_service_date.replace(year=self.last_service_date.year + self.nubbin_year_need_service)
        if self.current_date > date_need_service:
            return True
        else:
            return False