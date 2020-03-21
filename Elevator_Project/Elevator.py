class Elevator:

    def __init__(self, current_floor):
        self._current_floor = current_floor

    # Getter for current_floor value
    @property
    def current_floor(self):
        return self._current_floor

    # Setter for next_floor value
    @current_floor.setter
    def current_floor(self, new_value):
        self._current_floor = new_value
