# DT249 - Programming & Algorithms 2 - Project
# Conor O'Donovan - D18125705

import random
import time


class Building:

    def __init__(self, floors):
        self._floors = floors
        self._customers_waiting = []
        self._customers_waiting_copy = []  # This is only used when running both elevator movement methods to compare
        self._customers_arrived = []

    def __str__(self):
        return "Building with {} floors".format(self.floors)

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
        """Returns list of customers currently waiting for elevator"""
        return self._customers_waiting

    @property
    def customers_waiting_copy(self):
        """Returns list of customers currently waiting for elevator - copy for comparison"""
        return self._customers_waiting_copy

    @property
    def customers_arrived(self):
        """Returns list of customers that have arrived at their floor"""
        return self._customers_arrived

    def create_elevator(self):
        """Creates an instance of Elevator at a random floor"""
        elevator_start_floor = random.randint(1, self._floors)
        building_elevator = Elevator(elevator_start_floor, self._floors)
        return building_elevator

    def create_customers(self, num_cust):
        """Creates the specified number of customers and adds them to the customers_waiting list"""
        for a in range(num_cust):
            customer = Customer(random.randint(1, self.floors), random.randint(1, self.floors))
            self.customers_waiting.append(customer)
            self.customers_waiting_copy.append(customer)


class Elevator:

    def __init__(self, current_floor, total_floors):
        self._current_floor = current_floor
        self._total_floors = total_floors
        self._move_direction = 1
        self._customers_in_elevator = []

    def __str__(self):
        return "Elevator, currently on floor {}".format(self.current_floor)

    @property
    def current_floor(self):
        """Returns the floor the elevator is currently stopped at"""
        return self._current_floor

    @current_floor.setter
    def current_floor(self, new_value):
        """Changes the current floor of the elevator to new_value"""
        self._current_floor = new_value

    @property
    def move_direction(self):
        """Returns whether the elevator is currently moving up (1) or down (-1)"""
        return self._move_direction

    @move_direction.setter
    def move_direction(self, new_value):
        """Changes the direction the elevator is moving in to up (1) or down (-1)"""
        self._move_direction = new_value

    @property
    def total_floors(self):
        """Returns the total number of floors in the building"""
        return self._total_floors

    @property
    def customers_in_elevator(self):
        """Returns the list of customers currently in the elevator"""
        return self._customers_in_elevator

    def enter(self, customer):
        """Adds customer to the list of customers currently in the elevator"""
        self._customers_in_elevator.append(customer)

    def exit(self, customer):
        """Removes customer from the list of customers currently in the elevator"""
        self._customers_in_elevator.remove(customer)

    def move(self):
        """Moves the elevator - it will move up until it reaches the top floor,
        then move down until it reaches the bottom floor"""
        if self.current_floor == 1:
            self.move_direction = 1

        if self.current_floor == self.total_floors:
            self.move_direction = -1

        self.current_floor += 1 * self.move_direction

    def move_optimally(self):
        """The elevator checks the destination floor of each customer currently in the lift,
        and moves to the closest floor that a customer wants to go to"""
        temp = 999

        if len(self._customers_in_elevator) == 0:
            self.move()
        else:
            for j in self._customers_in_elevator:
                a = abs(self.current_floor - j.destination_floor)
                if a < temp:
                    temp = j.destination_floor

            self.current_floor = temp


class Customer:

    def __init__(self, start_floor, destination_floor):
        self._start_floor = start_floor
        self._destination_floor = destination_floor

    def __str__(self):
        return "Start floor: {}; Destination floor: {}".format(self.start_floor, self.destination_floor)

    def __repr__(self):
        return "{}-{}".format(self.start_floor, self.destination_floor)

    @property
    def start_floor(self):
        """Returns start floor of Customer instance"""
        return self._start_floor

    @start_floor.setter
    def start_floor(self, new_value):
        """Allows user to change start floor of Customer instance to new_value"""
        self._start_floor = new_value

    @property
    def destination_floor(self):
        """Returns destination floor of Customer instance"""
        return self._destination_floor

    @destination_floor.setter
    def destination_floor(self, new_value):
        """Allows user to change destination floor of Customer instance to new_value"""
        self._destination_floor = new_value


if __name__ == "__main__":

    # Declare variables
    floors_entered = False
    num_floors = 0
    num_customers_entered = False
    num_customers = 0
    elevator_movement_selected = False
    elevator_movement = 0
    counter_standard = 0
    counter_optimal = 0
    initialise_optimal_method = False

    # Print title of project
    print("=" * 34)
    print("P&A2 Project - Elevator Simulation")
    print("=" * 34)
    time.sleep(1)

    # User entering number of floors
    while not floors_entered:
        floors_input = input("How many floors does the building have? (Min: 2, Max: 10)\n")

        try:
            num_floors = int(floors_input)
            if num_floors < 2:
                print("The building must have at least two floors")
                continue
            elif num_floors > 10:
                print("The building cannot have more than 10 floors")
                continue
            else:
                floors_entered = True
                continue
        except:
            print("This is not a valid entry - please enter a number between 2 and 10")
            continue

    # User entering number of customers
    while not num_customers_entered:
        num_customers_input = input("How many customers are in the building?\n")

        try:
            num_customers = int(num_customers_input)

            if num_customers < 1:
                print("There must be at least 1 customer in the building")
                continue
            elif num_customers > 10:
                print("There cannot be more than 10 customers in the building")
                continue
            else:
                num_customers_entered = True
                continue
        except:
            print("This is not a valid entry - please enter a number between 1 and 10")
            continue

    # Selecting elevator movement method
    while not elevator_movement_selected:
        elevator_movement_input = input("Please select the method for moving the elevator\n"
                                        "1 - Standard\n"
                                        "2 - Optimal\n"
                                        "3 - Both (and compare results)\n"
                                        "4 - See descriptions of elevator movement methods\n")

        try:
            elevator_movement = int(elevator_movement_input)
            if elevator_movement != 1 and elevator_movement != 2 and elevator_movement != 3 and elevator_movement != 4:
                print("Invalid selection\n")
                continue
            elif elevator_movement == 4:
                print("Standard:\n"
                      "The elevator moves up or down one floor at a time, switching direction when\n"
                      "it reaches the top or bottom floor. It does not take into account the destination\n"
                      "floors of customers in the elevator.\n")
                print("Optimal:\n"
                      "The elevator checks the destination floor of all customers currently in the elevator\n"
                      "and moves to the one closest to the elevator's current floor. If there are currently\n"
                      "no customers in the elevator, it simply moves based on the standard method until a"
                      "customer enters the elevator\n")
                time.sleep(2)
                continue
            else:
                elevator_movement_selected = True
                continue
        except:
            print("Invalid selection\n")
            continue

    # Create building instance
    building = Building(num_floors)
    elevator = building.create_elevator()
    building.create_customers(num_customers)

    print("Number of floors: {}".format(building.floors))
    print("Number of customers: {}\n".format(num_customers))
    print("INITIALISING SIMULATION...\n")
    time.sleep(1)

    # Primary loop for checking customers and moving elevator
    while True:
        if elevator_movement == 1 or elevator_movement == 2:
            if len(building.customers_waiting) == 0 and len(elevator.customers_in_elevator) == 0:
                print("All customers arrived!\n")
                break
        elif elevator_movement == 3:
            if len(building.customers_waiting) == 0 and len(building.customers_waiting_copy) == 0 and len(elevator.customers_in_elevator) == 0:
                print("All customers arrived!\n")
                break

        # Check customers waiting and move them into elevator
        for i in building.customers_waiting:
            if i.start_floor == elevator.current_floor:
                building.customers_waiting.remove(i)
                elevator.enter(i)

        # If running elevator movement method 3, check customers waiting in copy list
        if elevator_movement == 3 and len(building.customers_waiting) == 0:

            while not initialise_optimal_method:
                elevator.customers_in_elevator.clear()
                building.customers_waiting.clear()

                print("All customers arrived! (Standard movement method)\n")
                print("Starting again using optimal movement method\n")

                initialise_optimal_method = True

                time.sleep(1)

            for i in building.customers_waiting_copy:
                if i.start_floor == elevator.current_floor:
                    building.customers_waiting_copy.remove(i)
                    elevator.enter(i)

        # Check customers in elevator and move them onto correct floor
        for i in elevator.customers_in_elevator:
            if i.destination_floor == elevator.current_floor:
                elevator.exit(i)
                building.customers_arrived.append(i)

        if elevator_movement == 1:
            elevator.move()
            counter_standard += 1
        elif elevator_movement == 2:
            elevator.move_optimally()
            counter_optimal += 1
        elif elevator_movement == 3:
            if len(building.customers_waiting) > 0:
                elevator.move()
                counter_standard += 1
            else:
                elevator.move_optimally()
                counter_optimal += 1

        print("Current floor: {}".format(elevator.current_floor))

        if elevator_movement == 1 or elevator_movement == 2 or (elevator_movement == 3 and len(building.customers_waiting) > 0):
            print("Customers waiting: {}".format(building.customers_waiting))
        else:
            print("Customers waiting: {}".format(building.customers_waiting_copy))

        print("Customers in elevator: {}".format(elevator.customers_in_elevator))
        print("Customers arrived: {}\n".format(building.customers_arrived))

        time.sleep(1)

    if elevator_movement == 1:
        print("Number of floors visited: {}".format(counter_standard))

    if elevator_movement == 2:
        print("Number of floors visited: {}".format(counter_optimal))

    if elevator_movement == 3:
        print("Number of floors visited (standard movement method): {}".format(counter_standard))
        print("Number of floors visited: (optimal movement method): {}".format(counter_optimal))
