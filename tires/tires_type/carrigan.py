from tires.tires import Tires

class CarriganTires(Tires):

    def __init__(self, tires_wear):
        self.tires_wear = tires_wear
        self.tires_need_service = 0.9

    def needs_service(self):
        for i in self.tires_wear:
            if i >= self.tires_need_service:
                return True
        return False