class Customer:

    def __init__(self, start_floor, destination_floor):
        self._start_floor = start_floor
        self._destination_floor = destination_floor

    @property
    def start_floor(self):
        return self._start_floor

    @start_floor.setter
    def start_floor(self, new_value):
        self._start_floor = new_value

    @property
    def destination_floor(self):
        return self._destination_floor

    @destination_floor.setter
    def destination_floor(self, new_value):
        self._destination_floor = new_value
