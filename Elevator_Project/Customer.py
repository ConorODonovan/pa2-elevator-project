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
