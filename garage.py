from vehicle import Vehicle

class Garage:
    '''
    A garage is a place that stores a collection of vehicles
    '''

    # Constructor
    def __init__(self):
        """Initialize an empty list"""
        self._vehicles: list[Vehicle] = []

    # Getter
    @property
    def vehicles(self) -> list[Vehicle]:
        """Return a copy of the internal list (to protect encapsulation)"""
        return list(self._vehicles)

    def add_vehicle(self, vehicle: Vehicle) -> None:
        """Add a vehicle to the list"""
        self._vehicles.append(vehicle)

    def empty_garage(self):
        """Empties the garage of all the vehicles"""
        self._vehicles.clear()

    def sort_by_release_year(self):
        self._vehicles.sort()

    def __str__(self) -> str:
        return "\n".join(str(v) for v in self._vehicles) # str1.join(str2)