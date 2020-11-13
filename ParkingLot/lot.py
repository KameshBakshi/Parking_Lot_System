class ParkingLot(object):
    """
    This class represents a parking slot entity
    and all methods related to it.
    """

    def __init__(self, slot_id=None, empty=None):
        self.car = None
        self.slot_id = slot_id
        self.empty = empty

    def get_car(self):
        return self.car

    def set_car(self, car):
        self.car = car

    def get_slot_id(self):
        return self.slot_id

    def set_slot_id(self, value):
        self.slot_id = value

    def get_empty(self):
        return self.empty

    def set_empty(self, value):
        self.empty = value
