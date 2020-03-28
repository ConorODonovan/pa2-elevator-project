class Elevator:

    def __init__(self, current_floor, total_floors):
        self._current_floor = current_floor
        self._total_floors = total_floors
        self._move_direction = 1

    # Getter for current_floor value
    @property
    def current_floor(self):
        return self._current_floor

    # Setter for current_floor value
    @current_floor.setter
    def current_floor(self, new_value):
        self._current_floor = new_value

    # Getter for move_direction value
    @property
    def move_direction(self):
        return self._move_direction

    # Setter for move_direction value
    @move_direction.setter
    def move_direction(self, new_value):
        self._move_direction = new_value

    # Getter for total_floors value
    @property
    def total_floors(self):
        return self._total_floors

    def move(self):
        if self.current_floor == 1:
            self.move_direction = 1

        if self.current_floor == self.total_floors:
            self.move_direction = -1

        self.current_floor += 1 * self.move_direction
