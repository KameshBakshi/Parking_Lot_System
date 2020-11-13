class Car(object):
    """
    This class which represents Car entity.
    """

    def __init__(self, registration_no, age):
        self.registration_id = registration_no
        self.driver_age = age

    def get_registration_no(self):
        return self.registration_id

    def get_driver_age(self):
        return self.driver_age
