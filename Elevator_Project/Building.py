from Elevator import Elevator
from Customer import Customer
import random


class Building:

    def __init__(self, floors):
        self._floors = floors

    # Getter for floors value
    @property
    def floors(self):
        return self._floors

    # Setter for floors value
    @floors.setter
    def floors(self, new_value):
        self._floors = new_value

    # Create elevator
    def create_elevator(self):
        elevator_start_floor = random.randint(0, self._floors)
        elevator = Elevator(elevator_start_floor, self._floors)
        return elevator
