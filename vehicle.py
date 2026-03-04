from abc import ABC, abstractmethod
# from functools import total_ordering  # sorting purposes

from manufacturer import Manufacturer
from auto_model import AutoModel

class Vehicle(ABC):
    """
    Abstract base class (ABC) for all vehicles
    """
    # constructor
    def __init__(self,
                 manufacturer: Manufacturer,
                 model: AutoModel,
                 mpg: float):
        self._manufacturer = manufacturer
        self._model = model
        self._mpg = mpg

    @property
    def manufacturer(self) -> Manufacturer:
        return self._manufacturer
    
    @property
    def automodel(self) -> AutoModel:
        return self._model
    
    @property
    def mpg(self) -> float:
        return self._mpg
    
    @property
    def release_year(self) -> int:
        """"""
        return self._model.years[0]
    
    # ----- concrete methods -----
    def how_far_with(self, num_of_gallons: int) -> float:
        return self._mpg * num_of_gallons
    
    # ----- abstract methods -----
    @abstractmethod
    def number_of_wheels(self) -> int:
        ...


    # ---- comparison criteria ----

    def __eq__(self, other) -> bool:
        if not isinstance(other, Vehicle):
            return NotImplemented
        return self.release_year == other.release_year

    def __lt__(self, other) -> bool:
        if not isinstance(other, Vehicle):
            return NotImplemented
        return self.release_year < other.release_year
    
    def __hash__(self, other) -> bool:
        return hash(self.release_year)

