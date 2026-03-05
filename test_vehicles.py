'''
This is the unit testing file.
Author: Thuan Nguyen
'''

import pytest

from manufacturer import Manufacturer
from auto_model import AutoModel
from vehicle import Vehicle
# from sedan import Sedan
# from truck import Truck
# from garage import Garage


# ============================================================
#  Manufacturer tests
# ============================================================
class TestManufacturer:
    def test_constructor(self):
        m = Manufacturer("Ford", "USA")
        assert m.name == "Ford"
        assert m.country == "USA"

    def test_str(self):
        m = Manufacturer("BMW", "Germany")
        assert str(m) == "BMW, Germany"

    def test_constructor_2(self):
        m = Manufacturer("Honda", "Japan")
        assert m.name == "Honda"
        assert m.country == "Japan"
        assert str(m) == "Honda, Japan"

    
# ============================================================
#  AutoModel tests
# ============================================================
class TestAutoModel:
    def test_constructor(self):
        am = AutoModel("F150", True, [2020, 2021, 2022])
        assert am.name == "F150"
        assert am.in_production == True
        assert am.years == [2020, 2021, 2022]

    def test_first_year(self):
        am = AutoModel("Civic", False, [1996, 1997, 1998])
        assert am.first_year == 1996

    def test_str(self):
        am = AutoModel("Tundra", False, [1987, 1988])
        result = str(am)
        assert "Tundra" in result
        assert "False" in result
        assert "1987" in result

    def test_empty_years_raises(self):
        with pytest.raises(ValueError):
            AutoModel("Invisible Car", False, [])

    def test_years_defensive_copy(self):
        """Changing the original must not affect the model"""
        original_list = [2020, 2021]
        am = AutoModel("F150", True, original_list)
        original_list.clear()
        assert am.years == [2020, 2021]

    def test_years_getter_returns_copy(self):
        """Changing the original must not affect the model"""
        am = AutoModel("M3 Limited", False, [2015, 2016, 2017, 2018])
        returned = am.years
        returned.append(2019)
        assert len(am.years) == 4


# ============================================================
#  Vehicle / abstract contract tests
# ============================================================
class TestVehicleAbstract:
    def test_vehicle_cannot_be_directly_initialized(self):
        """Vehicle is abstract and should not be directly initialized"""
        with pytest.raises(TypeError):
            Vehicle(
                Manufacturer("Xavier", "Yelan"),
                AutoModel("Zhongli", True, [2025]),
                25.0
            )

    def test_subclass_must_implement_number_of_wheels(self):
        """A subclass that does not have number_of_wheels should not work"""
        # This incomplete version should raise TypeError
        with pytest.raises(TypeError):
            class Incompletion(Vehicle):
                pass
            Incompletion(
                Manufacturer("Xavier", "Yelan"),
                AutoModel("Zhongli", True, [2025]),
                30.0
            )