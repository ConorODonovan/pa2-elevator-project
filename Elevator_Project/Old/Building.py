from Elevator import Elevator
from Customer import Customer
import random


class Building:

    def __init__(self, floors):
        self._floors = floors

    # Getter for floors value
    @property
    def floors(self):
        """Returns number of floors of Building instance"""
        return self._floors

    # Setter for floors value
    @floors.setter
    def floors(self, new_value):
        """Allows user to change the number of floors to new_value"""
        self._floors = new_value

    # Create elevator
    def create_elevator(self):
        """Creates an instance of Elevator"""
        elevator_start_floor = random.randint(1, self._floors)
        elevator = Elevator(elevator_start_floor, self._floors)
        return elevator
