import _pytest
from app.calc import Calculator

class TestCalcul:
    def setup(self):
        self.calc = Calculator

    def test_multiply_success(self):
        assert self.calc.multiply(self, 2, 3) == 6

    def test_division_success(self):
        assert self.calc.division(self, 8, 2) == 4

    def test_subtraction_success(self):
        assert self.calc.subtraction(self, 10, 5) == 5

    def test_adding_success(self):
        assert self.calc.adding(self, 3, 8) == 11

    def teardown(self):
        print('Выполнение метода Teardown')