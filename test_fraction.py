import unittest
from fraction import Fraction

class TestFraction(unittest.TestCase):

    def test_initialization(self):
        f = Fraction(10, 20)
        self.assertEqual(f.numerator, 1)
        self.assertEqual(f.denominator, 2)

        f = Fraction(5, 1)
        self.assertEqual(f.numerator, 5)
        self.assertEqual(f.denominator, 1)

        f = Fraction(-10, 20)
        self.assertEqual(f.numerator, -1)
        self.assertEqual(f.denominator, 2)

        f = Fraction(5, -7)
        self.assertEqual(f.numerator, -5)
        self.assertEqual(f.denominator, 7)

    def test_str(self):
        f = Fraction(10, 20)
        self.assertEqual(str(f), "1/2")

    def test_as_mixed_number(self):
        # Test for a proper fraction
        f = Fraction(5, 2)
        self.assertEqual(f.as_mixed_number(), "2 + 1/2")

        # Test for an improper fraction
        f = Fraction(3, 3)
        self.assertEqual(f.as_mixed_number(), "1")

    def test_addition(self):
        f1 = Fraction(1, 2)
        f2 = Fraction(1, 3)
        result = f1 + f2
        self.assertEqual(result.numerator, 5)
        self.assertEqual(result.denominator, 6)
        with self.assertRaises(TypeError):
            f1 + "brol"

    def test_subtraction(self):
        f1 = Fraction(1, 2)
        f2 = Fraction(1, 3)
        result = f1 - f2
        self.assertEqual(result.numerator, 1)
        self.assertEqual(result.denominator, 6)
        with self.assertRaises(TypeError):
            f1 - "brol"

    def test_multiplication(self):
        f1 = Fraction(2, 3)
        f2 = Fraction(3, 4)
        result = f1 * f2
        self.assertEqual(result.numerator, 1)
        self.assertEqual(result.denominator, 2)
        with self.assertRaises(TypeError):
            f1 * "brol"

    def test_division(self):
        f1 = Fraction(2, 3)
        f2 = Fraction(3, 4)
        f3 = Fraction(0, 5)
        result = f1 / f2
        self.assertEqual(result.numerator, 8)
        self.assertEqual(result.denominator, 9)
        with self.assertRaises(TypeError):
            f1 / "brol"
        with self.assertRaises(ZeroDivisionError):
            f1 / f3

    def test_power(self):
        f1 = Fraction(2, 3)
        result = f1 ** 2
        f2 = Fraction(3, 4)
        result2 = f2 ** -2
        self.assertEqual(result.numerator, 4)
        self.assertEqual(result.denominator, 9)
        self.assertEqual(result2.numerator, 16)
        self.assertEqual(result2.denominator, 9)
        with self.assertRaises(TypeError):
            f1 ** "brol"

    def test_equality(self):
        f1 = Fraction(2, 3)
        f2 = Fraction(4, 6)
        self.assertTrue(f1 == f2)
        f3 = Fraction(1, 2)
        self.assertFalse(f1 == f3)
        with self.assertRaises(TypeError):
            f1 == "brol"

    def test_float_conversion(self):
        f = Fraction(1, 2)
        self.assertEqual(float(f), 0.5)

    def test_invalid_initialization(self):
        with self.assertRaises(ValueError):
            Fraction(1, 0)

    def test_lesser_than(self):
        f1 = Fraction(1, 5)
        f2 = Fraction(2, 3)
        self.assertTrue(f1 < f2)
        with self.assertRaises(TypeError):
            f1 < "brol"

    def test_greater_than(self):
        f1 = Fraction(1, 2)
        f2 = Fraction(1, 3)
        self.assertTrue(f1 > f2)
        with self.assertRaises(TypeError):
            f1 > "brol"

    def test_is_zero(self):
        f = Fraction(0, 3)
        self.assertTrue(f.is_zero())

    def test_is_integer(self):
        f1 = Fraction(4, 2)
        self.assertTrue(f1.is_integer())
        f2 = Fraction(3, 2)
        self.assertFalse(f2.is_integer())

    def test_is_proper(self):
        f1 = Fraction(1, 2)
        self.assertTrue(f1.is_proper())
        f2 = Fraction(3, 2)
        self.assertFalse(f2.is_proper())

    def test_is_unit(self):
        f1 = Fraction(1, 3)
        self.assertTrue(f1.is_unit())
        f2 = Fraction(2, 3)
        self.assertFalse(f2.is_unit())

    def test_is_adjacent_to(self):
        f1 = Fraction(1, 2)
        f2 = Fraction(1, 3)
        self.assertTrue(f1.is_adjacent_to(f2))
        f3 = Fraction(3, 4)
        self.assertFalse(f1.is_adjacent_to(f3))
        with self.assertRaises(TypeError):
            f1.is_adjacent_to("brol")


if __name__ == "__main__":
    unittest.main()
