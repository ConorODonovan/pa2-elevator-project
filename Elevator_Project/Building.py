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
