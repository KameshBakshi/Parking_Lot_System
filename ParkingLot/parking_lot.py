#!/usr/bin/python
import os
import sys

import parking


class Commands(object):

    def __init__(self):
        self.parking = parking.Parking()

    def execute_command(self, input_command):
        command_list = input_command.split()

        if command_list[0]=='Create_parking_lot':
            number_of_slots = int(command_list[1])
            output = self.create_parking_lot(number_of_slots=number_of_slots)
            print(output)

        elif command_list[0]=='Park':
            registration_number = command_list[1]
            driver_age = int(command_list[3])
            output = self.park_car(registration_number=registration_number, driver_age=driver_age)
            print(output)

        elif command_list[0]=='Slot_numbers_for_driver_of_age':
            age = int(command_list[1])
            output = self.get_slot_numbers_for_given_driver_age(age=age)
            print(output)

        elif command_list[0]=='Slot_number_for_car_with_number':
            registration_number = command_list[1]
            output = self.get_slot_numbers_for_given_reg_no(registration_no=registration_number)
            print(output)

        elif command_list[0]=='Leave':
            slot_no = int(command_list[1])
            output = self.unpark_car(slot_number=slot_no)
            print(output)

        elif command_list[0]=='Vehicle_registration_number_for_driver_of_age':
            age = int(command_list[1])
            output = self.get_vehicle_registration_number_for_age(age=age)
            print(output)

        else:
            print("Invalid command->>", input_command)

    def create_parking_lot(self, number_of_slots):
        return self.parking.create_parking_lot(no_of_slots=number_of_slots)

    def park_car(self, registration_number, driver_age):
        return self.parking.park_car(registration_no=registration_number, driver_age=driver_age)

    def get_slot_numbers_for_given_driver_age(self, age):
        return self.parking.slot_numbers_for_cars_with_driver_age(driver_age=age)

    def get_slot_numbers_for_given_reg_no(self, registration_no):
        return self.parking.slot_number_for_registration_number(registration_number=registration_no)

    def unpark_car(self, slot_number):
        return self.parking.unpark_car(slot_no=slot_number)

    def get_vehicle_registration_number_for_age(self, age):
        return self.parking.registration_numbers_for_cars_with_driver_age(driver_age=age)


if __name__ == "__main__":

    file_path = input("Enter the file path -> ")

    # file_path = 'input.txt'

    if not os.path.exists(file_path):
        raise ValueError("Please enter valid file path")

    with open(file_path) as file:
        file_lines = file.readlines()
        file.close()

    if len(file_lines)==0:
        print("Empty File - No commands to run !! Exiting")
        exit()

    commands = Commands()
    for each_command in file_lines:
        commands.execute_command(input_command=each_command)
