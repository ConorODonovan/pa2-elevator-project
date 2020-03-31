class Elevator:

    def __init__(self, current_floor, total_floors):
        self._current_floor = current_floor
        self._total_floors = total_floors
        self._move_direction = 1
        self._customers_in_elevator = []

    def __str__(self):
        return "Elevator, currently on floor {}".format(self.current_floor)

    # Getter for current_floor value
    @property
    def current_floor(self):
        """Returns the floor the elevator is currently stopped at"""
        return self._current_floor

    # Setter for current_floor value
    @current_floor.setter
    def current_floor(self, new_value):
        """Changes the current floor of the elevator to new_value"""
        self._current_floor = new_value

    # Getter for move_direction value
    @property
    def move_direction(self):
        """Returns whether the elevator is currently moving up (1) or down (-1)"""
        return self._move_direction

    # Setter for move_direction value
    @move_direction.setter
    def move_direction(self, new_value):
        """Changes the direction the elevator is moving in to up (1) or down (-1)"""
        self._move_direction = new_value

    # Getter for total_floors value
    @property
    def total_floors(self):
        """Returns the total number of floors in the building"""
        return self._total_floors

    @property
    def customers_in_elevator(self):
        return self._customers_in_elevator

    def enter(self, customer):
        self._customers_in_elevator.append(customer)

    def exit(self, customer):
        self._customers_in_elevator.remove(customer)

    def move(self):
        """Moves the elevator - it will move up until it reaches the top floor,
        then move down until it reaches the bottom floor"""
        if self.current_floor == 1:
            self.move_direction = 1

        if self.current_floor == self.total_floors:
            self.move_direction = -1

        self.current_floor += 1 * self.move_direction
