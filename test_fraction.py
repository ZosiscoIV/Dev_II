import unittest
from fraction import Fraction

class TestFraction(unittest.TestCase):

    # __init__
    def test_init_valid(self):
        f = Fraction(2, 4)
        self.assertEqual(str(f), "1/2")

    def test_init_negative_denominator(self):
        f = Fraction(2, -4)
        self.assertEqual(str(f), "-1/2")

    def test_init_zero_numerator(self):
        f = Fraction(0, 4)
        self.assertEqual(str(f), "0/1")

    def test_init_zero_denominator(self):
        with self.assertRaises(ZeroDivisionError):
            Fraction(2, 0)

    def test_init_non_integer_numerator(self):
        with self.assertRaises(ValueError):
            Fraction(2.5, 4)

    def test_init_non_integer_denominator(self):
        with self.assertRaises(ValueError):
            Fraction(2, 4.5)

    # __str__
    def test_str(self):
        f = Fraction(2, 4)
        self.assertEqual(str(f), "1/2")

    # as_mixed_number
    def test_as_mixed_number(self):
        f = Fraction(7, 3)
        self.assertEqual(f.as_mixed_number(), "2 + 1/3")

    def test_as_mixed_number_integer(self):
        f = Fraction(6, 3)
        self.assertEqual(f.as_mixed_number(), "2")

    def test_as_mixed_number_negative(self):
        f = Fraction(-7, 3)
        self.assertEqual(f.as_mixed_number(), "-2 - 1/3")

    def test_as_mixed_number_negative_integer(self):
        f = Fraction(-6, 3)
        self.assertEqual(f.as_mixed_number(), "-2")

    # __add__
    def test_add_plus_plus(self):
        f1 = Fraction(1, 2)
        f2 = Fraction(1, 4)
        self.assertEqual(f1 + f2, Fraction(3, 4))

    def test_add_plus_moins(self):
        f1 = Fraction(1, 2)
        f2 = Fraction(-1, 4)
        self.assertEqual(f1 + f2, Fraction(1, 4))

    def test_add_moins_plus(self):
        f1 = Fraction(-1, 2)
        f2 = Fraction(1, 4)
        self.assertEqual(f1 + f2, Fraction(-1, 4))

    def test_add_moins_moins(self):
        f1 = Fraction(-1, 2)
        f2 = Fraction(-1, 4)
        self.assertEqual(f1 + f2, Fraction(-3, 4))

    def test_add_zero_numerator(self):
        f1 = Fraction(1, 2)
        f2 = Fraction(0, 4)
        self.assertEqual(f1 + f2, Fraction(1, 2))

    def test_add_opposite(self):
        f1 = Fraction(1, 2)
        f2 = Fraction(-1, 2)
        self.assertEqual(f1 + f2, Fraction(0, 1))

    def test_add_non_fraction(self):
        f = Fraction(1, 2)
        with self.assertRaises(TypeError):
            f + 2

    # __sub__
    def test_sub_plus_plus(self):
        f1 = Fraction(3, 4)
        f2 = Fraction(1, 4)
        self.assertEqual(f1 - f2, Fraction(1, 2))

    def test_sub_plus_moins(self):
        f1 = Fraction(3, 4)
        f2 = Fraction(-1, 4)
        self.assertEqual(f1 - f2, Fraction(1, 1))

    def test_sub_moins_plus(self):
        f1 = Fraction(-3, 4)
        f2 = Fraction(1, 4)
        self.assertEqual(f1 - f2, Fraction(-1, 1))

    def test_sub_zero_numerator(self):
        f1 = Fraction(3, 4)
        f2 = Fraction(0, 4)
        self.assertEqual(f1 - f2, Fraction(3, 4))

    def test_sub_same_positive(self):
        f1 = Fraction(3, 4)
        f2 = Fraction(3, 4)
        self.assertEqual(f1 - f2, Fraction(0, 1))

    def test_sub_same_negative(self):
        f1 = Fraction(-3, 4)
        f2 = Fraction(-3, 4)
        self.assertEqual(f1 - f2, Fraction(0, 1))

    def test_sub_non_fraction(self):
        f = Fraction(3, 4)
        with self.assertRaises(TypeError):
            f - 2

    # __mul__
    def test_mul_plus_plus(self):
        f1 = Fraction(1, 2)
        f2 = Fraction(2, 3)
        self.assertEqual(f1 * f2, Fraction(1, 3))

    def test_mul_plus_moins(self):
        f1 = Fraction(1, 2)
        f2 = Fraction(-2, 3)
        self.assertEqual(f1 * f2, Fraction(-1, 3))

    def test_mul_moins_plus(self):
        f1 = Fraction(-1, 2)
        f2 = Fraction(2, 3)
        self.assertEqual(f1 * f2, Fraction(-1, 3))

    def test_mul_moins_moins(self):
        f1 = Fraction(-1, 2)
        f2 = Fraction(-2, 3)
        self.assertEqual(f1 * f2, Fraction(1, 3))

    def test_mul_zero_numerator(self):
        f1 = Fraction(1, 2)
        f2 = Fraction(0, 3)
        self.assertEqual(f1 * f2, Fraction(0, 1))

    def test_mul_non_fraction(self):
        f = Fraction(1, 2)
        with self.assertRaises(TypeError):
            f * 2

    # __truediv__
    def test_truediv_plus_plus(self):
        f1 = Fraction(1, 2)
        f2 = Fraction(2, 3)
        self.assertEqual(f1 / f2, Fraction(3, 4))

    def test_truediv_plus_moins(self):
        f1 = Fraction(1, 2)
        f2 = Fraction(-2, 3)
        self.assertEqual(f1 / f2, Fraction(-3, 4))

    def test_truediv_moins_plus(self):
        f1 = Fraction(-1, 2)
        f2 = Fraction(2, 3)
        self.assertEqual(f1 / f2, Fraction(-3, 4))

    def test_truediv_moins_moins(self):
        f1 = Fraction(-1, 2)
        f2 = Fraction(-2, 3)
        self.assertEqual(f1 / f2, Fraction(3, 4))

    def test_truediv_zero_numerator(self):
        f1 = Fraction(0, 4)
        f2 = Fraction(1, 4)
        self.assertEqual(f1 / f2, Fraction(0, 1))

    def test_truediv_zero_denominator(self):
        f1 = Fraction(1, 2)
        f2 = Fraction(0, 1)
        with self.assertRaises(ZeroDivisionError):
            f1 / f2

    def test_truediv_non_fraction(self):
        f = Fraction(1, 2)
        with self.assertRaises(TypeError):
            f / 2

    # __pow__
    def test_pow_positive(self):
        f = Fraction(2, 3)
        self.assertEqual(f ** 2, Fraction(4, 9))

    def test_pow_negative(self):
        f = Fraction(2, 3)
        self.assertEqual(f ** -1, Fraction(3, 2))

    def test_pow_zero(self):
        f = Fraction(2, 3)
        self.assertEqual(f ** 0, Fraction(1, 1))

    def test_pow_non_integer_exponent(self):
        f = Fraction(2, 3)
        with self.assertRaises(TypeError):
            f ** 0.5

    # __eq__
    def test_eq_equal(self):
        f1 = Fraction(1, 2)
        f2 = Fraction(2, 4)
        self.assertTrue(f1 == f2)

    def test_eq_unequal(self):
        f1 = Fraction(1, 2)
        f2 = Fraction(3, 4)
        self.assertFalse(f1 == f2)

    def test_eq_non_fraction(self):
        f1 = Fraction(1, 2)
        self.assertFalse(f1 == 2)

    # __float__
    def test_float(self):
        f = Fraction(1, 2)
        self.assertEqual(float(f), 0.5)

    def test_float_integer(self):
        f = Fraction(2, 2)
        self.assertEqual(float(f), 1)

    # __lt__
    def test_lt_true(self):
        f1 = Fraction(1, 2)
        f2 = Fraction(3, 4)
        self.assertTrue(f1 < f2)

    def test_lt_false(self):
        f1 = Fraction(1, 2)
        f2 = Fraction(3, 4)
        self.assertFalse(f2 < f1)

    def test_lt_false_equal(self):
        f1 = Fraction(1, 2)
        f2 = Fraction(1, 2)
        self.assertFalse(f2 < f1)

    def test_lt_non_fraction(self):
        f1 = Fraction(1, 2)
        with self.assertRaises(TypeError):
            f1 < 2



    # __gt__
    def test_gt_true(self):
        f1 = Fraction(1, 2)
        f2 = Fraction(3, 4)
        self.assertTrue(f2 > f1)

    def test_gt_false(self):
        f1 = Fraction(1, 2)
        f2 = Fraction(3, 4)
        self.assertFalse(f1 > f2)

    def test_gt_false_equal(self):
        f1 = Fraction(1, 2)
        f2 = Fraction(1, 2)
        self.assertFalse(f1 > f2)

    def test_gt_non_fraction(self):
        f1 = Fraction(1, 2)
        with self.assertRaises(TypeError):
            f1 > 2

    # is_zero
    def test_is_zero_true(self):
        f = Fraction(0, 1)
        self.assertTrue(f.is_zero())

    def test_is_zero_false(self):
        f = Fraction(1, 2)
        self.assertFalse(f.is_zero())

    def test_is_zero_false_negative(self):
        f = Fraction(-1, 2)
        self.assertFalse(f.is_zero())

    # is_integer
    def test_is_integer_true(self):
        f = Fraction(4, 2)
        self.assertTrue(f.is_integer())

    def test_is_integer_false(self):
        f = Fraction(3, 2)
        self.assertFalse(f.is_integer())

    def test_is_integer_true_negative(self):
        f = Fraction(-4, 2)
        self.assertTrue(f.is_integer())

    def test_is_integer_false_negative(self):
        f = Fraction(-3, 2)
        self.assertFalse(f.is_integer())

    def test_is_integer_zero(self):
        f = Fraction(0, 2)
        self.assertTrue(f.is_integer())

    # is_proper
    def test_is_proper_true(self):
        f = Fraction(1, 2)
        self.assertTrue(f.is_proper())

    def test_is_proper_false(self):
        f = Fraction(3, 2)
        self.assertFalse(f.is_proper())

    def test_is_proper_true_negative(self):
        f = Fraction(-1, 2)
        self.assertTrue(f.is_proper())

    def test_is_proper_false_negative(self):
        f = Fraction(-3, 2)
        self.assertFalse(f.is_proper())

    # is_unit
    def test_is_unit_true(self):
        f = Fraction(1, 3)
        self.assertTrue(f.is_unit())

    def test_is_unit_false(self):
        f = Fraction(2, 3)
        self.assertFalse(f.is_unit())

    def test_is_unit_false_negative(self):
        f = Fraction(-1, 3)
        self.assertFalse(f.is_unit())

    # is_adjacent_to
    def test_is_adjacent_to_false(self):
        f1 = Fraction(1, 2)
        f2 = Fraction(1, 3)
        self.assertTrue(f1.is_adjacent_to(f2))

    def test_is_adjacent_to_true(self):
        f1 = Fraction(1, 2)
        f2 = Fraction(9, 4)
        self.assertFalse(f1.is_adjacent_to(f2))

    def test_is_adjacent_to_false_negative(self):
        f1 = Fraction(-1, 2)
        f2 = Fraction(-1, 3)
        self.assertTrue(f1.is_adjacent_to(f2))

    def test_is_adjacent_to_true_negative(self):
        f1 = Fraction(-1, 2)
        f2 = Fraction(-9, 4)
        self.assertFalse(f1.is_adjacent_to(f2))

    def test_is_adjacent_to_invalid_argument(self):
        f1 = Fraction(1, 2)
        with self.assertRaises(TypeError):
            f1.is_adjacent_to(2)

if __name__ == '__main__':
    unittest.main()
