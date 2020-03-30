from Elevator import Elevator
from Customer import Customer
import random


class Building:

    def __init__(self, floors):
        self._floors = floors
        self._customers_waiting = []
        self._customers_arrived = []

    @property
    def floors(self):
        """Returns number of floors of Building instance"""
        return self._floors

    @floors.setter
    def floors(self, new_value):
        """Allows user to change the number of floors to new_value"""
        self._floors = new_value

    @property
    def customers_waiting(self):
        return self._customers_waiting

    @property
    def customers_arrived(self):
        return self._customers_arrived

    # Create elevator
    def create_elevator(self):
        """Creates an instance of Elevator"""
        elevator_start_floor = random.randint(1, self._floors)
        elevator = Elevator(elevator_start_floor, self._floors)
        return elevator

    def create_customers(self, num_customers):
        # Create customers and add to waiting list
        for i in range(num_customers):
            customer = Customer(random.randint(1, self.floors), random.randint(1, self.floors))

            # For testing
            print(customer)

            self.customers_waiting.append(customer)
