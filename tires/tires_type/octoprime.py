from tires.tires import Tires

class OctoprimeTires(Tires):

    def __init__(self, tires_wear):
        self.tires_wear = tires_wear
        self.tires_need_service = 3

    def needs_service(self):
        sum = 0
        for i in self.tires_wear:
            sum += i
        
        if sum >= self.tires_need_service:
            return True
        else:
            return False