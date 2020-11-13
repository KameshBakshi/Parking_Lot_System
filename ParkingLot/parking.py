import car
import lot


"""
    This class represents the parking space with parking lots and
    the different operations performed on them.
"""


class Parking(object):
    """
    It has 3 attributes: 
    parking_lots, a dict which contains lot number and it's lot object
    lots_filled, an integer to check how many lots are already occupied
    parking_capacity, an integer which represents the parking capacity of parking lot.
    """
    def __init__(self):
        self.parking_lots = dict()
        self.lots_filled = 0
        self.parking_capacity = 0

    def is_slot_full(self):
        """
        This method checks if parking lot has empty slot to park a car or not.
        :return: bool
        """
        if self.parking_capacity == self.lots_filled:
            return True
        return False

    def slot_exists(self):
        """
        This method checks if parking lot has been created or not.
        :return: bool
        """
        if self.parking_capacity == 0:
            return False
        return True

    def create_parking_lot(self, no_of_slots):
        """
        This method creates parking lot with given number of lots.
        Input: no_of_slots - Integer
        :return: string
        """

        if len(self.parking_lots) > 0:
            return "Parking Lot already exists"

        if no_of_slots <= 0:
            return "Parking Lot cannot be made with capacity 0 or less then 0, please enter valid size."

        self.parking_capacity = no_of_slots
        
        for slot_number in range(1, no_of_slots + 1):
            _lot = lot.ParkingLot(slot_id=slot_number, empty=True)
            self.parking_lots[slot_number] = _lot

        return "Created Parking of {} slots".format(self.parking_capacity)

    def get_nearest_available_slot(self):
        """
        This Method finds the nearest empty slot for parking.
        :return: Integer
        """

        for slot_no in range(1, self.parking_capacity+1):
            if slot_no not in self.parking_lots:
                return slot_no

            _lot = self.parking_lots[slot_no]
            if _lot.get_empty():
                return slot_no

        return -1

    def park_car(self, registration_no, driver_age):
        """
        This method Parks the incoming car at closest available slot.
        If parking lot is full, then a message will be printed regarding the condition.
        Input: registration_no - String & driver_age - Integer.
        :return: string
        """

        if not self.slot_exists():
            return "Parking Lot not created. Please do create one."

        if self.is_slot_full():
            return "Our Parking Lot is FULL. Please look for other Parking Lot."

        available_slot = self.get_nearest_available_slot()

        if available_slot == -1:
            return "Something went wrong while fetching nearest available slot, you found a bug!!!"

        _car = car.Car(registration_no, driver_age)

        self.parking_lots[available_slot].set_car(car=_car)

        self.parking_lots[available_slot].set_empty(value=False)

        # Increasing the value of variable to store the current occupied lots.
        self.lots_filled += 1

        return "Car with vehicle registration number '{}' has been parked at slot number {}".format(registration_no, available_slot)

    def unpark_car(self, slot_no):
        """
        This method empties slot by removing the car parked at given slot_no.
        Input: slot_no - Integer
        :return: string
        """
        if not self.slot_exists():
            return "Parking Lot not created. Please do create one."

        if self.lots_filled == 0:
            return "No car present in the Parking Lot."

        if slot_no not in self.parking_lots:
            return "Sorry, slot number does not exist in parking lot."

        parking_slot = self.parking_lots[slot_no]

        if parking_slot.get_empty():
            return "No car is present at given slot number"

        _car = parking_slot.car
        registration_number = _car.get_registration_no()
        driver_age = _car.get_driver_age()

        parking_slot.set_car(car=None)
        parking_slot.set_empty(value=True)

        self.lots_filled -= 1

        return "Slot number {} vacated, the car with vehicle registration number '{}' left the space, the driver of " \
               "the car was of age {}".format(slot_no, registration_number, driver_age)

    def registration_numbers_for_cars_with_driver_age(self, driver_age):
        """
        This method will find Vehicle Registration numbers for all cars which are parked
        by the driver of a certain age.
        Input: driver_age - Integer.
        :return: string
        """

        if not self.slot_exists():
            return "Parking Lot not created. Please do create one."

        if self.lots_filled == 0:
            return "No car present in the Parking Lot."

        registration_numbers = list()

        for slot_no in self.parking_lots:
            parking_lot = self.parking_lots[slot_no]

            if parking_lot.get_empty():
                continue

            _car = parking_lot.get_car()
            age = _car.get_driver_age()
            if age == driver_age:
                reg_no = _car.get_registration_no()
                registration_numbers.append(reg_no)

        if len(registration_numbers) > 0:
            return " ".join(registration_numbers)
        return "Not found any registration number with given driver age."

    def slot_number_for_registration_number(self, registration_number):
        """
        This method finds the slot number corresponding to particular registration number
        Input: registration_number - String
        :return: string
        """

        if not self.slot_exists():
            return "Parking Lot not created. Please do create one."

        if self.lots_filled == 0:
            return "No car present in the Parking Lot."

        for slot_no in self.parking_lots:

            _lot = self.parking_lots[slot_no]

            if _lot.get_empty():
                continue

            _car = _lot.get_car()
            _reg_no = _car.get_registration_no()
            if _reg_no==registration_number:
                return slot_no

        return "No Car found with given Registration Number"

    def slot_numbers_for_cars_with_driver_age(self, driver_age):
        """
        This method will return all the slot numbers which have car parked by
        driver of particular age.
        Input: driver_age - Integer type
        """

        if not self.slot_exists():
            return "Parking Lot not created. Please do create one."

        if self.lots_filled == 0:
            return "No car present in the Parking Lot."

        lot_numbers = []
        for slot_no in self.parking_lots:

            _lot = self.parking_lots[slot_no]

            if _lot.get_empty():
                continue

            _car = _lot.get_car()
            age = _car.get_driver_age()
            if age == driver_age:
                lot_numbers.append(slot_no)

        if len(lot_numbers) > 0:
            return " ".join([str(i) for i in lot_numbers])
        return "Not found any slots with given driver age"
