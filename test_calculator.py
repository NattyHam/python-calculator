import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    # Add the following test methods to the TestCalculator class:

    #Add
    def test_add_num(self):
        self.assertEqual(self.calc.add(1, 5), 6)

    def test_add_negnum(self):
        self.assertEqual(self.calc.add(-1, -5), -6)

    #subtract
    def test_subtract_posnum(self):
        self.assertEqual(self.calc.subtract(1, 5), -4)
    
    def test_subtract_negnum(self):
        self.assertEqual(self.calc.subtract(0, -5), 5)

    #Multiply
    def test_multiply_posnum(self):
        self.assertEqual(self.calc.multiply(50, 10), 500)

    def test_multiply_negnum(self):
        self.assertEqual(self.calc.multiply(-80, -10), 800)

    #Divide
    def test_divide_posnum(self):
        self.assertEqual(self.calc.divide(80, 10), 8)

    def test_divide_zero(self):
        self.assertEqual(self.calc.divide(80, 0), "Error")

    def test_divide_negnum(self):
        self.assertEqual(self.calc.divide(-80, 10), -8)

    #Modulo
    def test_mod_posnum(self):
        self.assertEqual(self.calc.modulo(5, 3), 2)
        self.assertEqual(self.calc.modulo(0, 3), 0)

    def test_mod_zero(self):
        self.assertEqual(self.calc.modulo(5, 0), "Error")

if __name__ == '__main__':
    unittest.main()