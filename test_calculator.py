import unittest
from .calculator import Calculator


class TestCalculator(unittest.TestCase):

    # functionality that adds two items
    ## add two numbers #covered
    ## allow addition of both negative and positive numbers #covered
    ## handle stringed numbers "57" #covered
    ## handle non stringed number "one" #covered
    ## 1\3 + 3\7 # accuracy
    ## ValueError, TypeError, NonMoneyError (you have to build this urself)
    def test_add_numbers(self):
        # 40 and 50 = 90
        # comparisons == assertions
        expected_value = 90
        result = Calculator.add(40, 50)
        self.assertEqual(result, expected_value)
        self.assertNotEqual(result, 100)

    def test_negative_numbers(self):
        expected_value = 200
        result = Calculator.add(-400, 600)
        self.assertEqual(result, expected_value)
        expected_value = -370
        result = Calculator.add(-368, -2)
        self.assertNotEqual(result, 100)

    def test_stringed_numbers(self):
        expected_value = 200
        result = Calculator.add("120", "80")
        self.assertEqual(result, expected_value)
        expected_value = 122.5
        result = Calculator.add("120.5", "2")
        self.assertEqual(result, expected_value)

    def test_non_stringed_numbers(self):
        expected_value = "two"
        result = Calculator.add("one", "one")
        self.assertNotEqual(result, expected_value)
        expected_value = "two"
        # tell unit test that we expect an error when this happens
        with self.assertRaises(TypeError):
            result = Calculator.add("one", "1")
        # self.assertNotEqual(result, expected_value) !=

    def test_subtract_positive_numbers(self):
        self.assertEqual(Calculator.subtract(50, 20), 30)
        self.assertEqual(Calculator.subtract(100.5, 50), 50.5)

    def test_subtract_negative_numbers(self):
        self.assertEqual(Calculator.subtract(10, -5), 15)
        self.assertEqual(Calculator.subtract(-50, 25), -75)

    def test_subtract_stringed_numbers(self):
        self.assertEqual(Calculator.subtract("100", "50"), 50)
        self.assertEqual(Calculator.subtract("75.5", "25"), 50.5)

    def test_subtract_non_number_strings(self):
        with self.assertRaises(TypeError):
            Calculator.subtract("one", "two")
        with self.assertRaises(TypeError):
            Calculator.subtract("100", "fifty")

    def test_subtract_type_mismatch(self):
        with self.assertRaises(TypeError):
            Calculator.subtract(100, "fifty")
        with self.assertRaises(TypeError):
            Calculator.subtract([1, 2], 5)

    def test_divide_positive_numbers(self):
        self.assertEqual(Calculator.divide(10, 2), 5)
        self.assertEqual(Calculator.divide(100, 4), 25)
        self.assertAlmostEqual(Calculator.divide(10, 3), 3.333333333)

    def test_divide_positive_and_negative_numbers(self):
        self.assertEqual(Calculator.divide(10, -2), -5)
        self.assertEqual(Calculator.divide(-20, 4), -5)

    def test_divide_stringed_numbers(self):
        self.assertEqual(Calculator.divide("100", "10"), 10)
        self.assertEqual(Calculator.divide("50.5", "2"), 25.25)

    def test_divide_by_zero_error(self):
        with self.assertRaises(ZeroDivisionError):
            Calculator.divide(10, 0)
        with self.assertRaises(ZeroDivisionError):
            Calculator.divide(10, "0")

    def test_divide_non_number_strings(self):
        with self.assertRaises(TypeError):
            Calculator.divide("ten", "two")
        with self.assertRaises(TypeError):
            Calculator.divide("10", "two")

    def test_divide_type_mismatch(self):
        with self.assertRaises(TypeError):
            Calculator.divide(10, [2])
        with self.assertRaises(TypeError):
            Calculator.divide("100", {"key": 10})
            
    def test_multiply_positive_numbers(self):
        self.assertEqual(Calculator.multiply(10, 5), 50)
        self.assertEqual(Calculator.multiply(2.5, 4), 10.0)

    def test_multiply_one_positive_and_one_negative_number(self):
        self.assertEqual(Calculator.multiply(10, -5), -50)
        self.assertEqual(Calculator.multiply(-3, 7), -21)

    def test_multiply_stringed_numbers(self):
        self.assertEqual(Calculator.multiply("10", "5"), 50)
        self.assertEqual(Calculator.multiply("3.5", "2"), 7.0)

    def test_multiply_non_number_strings(self):
        with self.assertRaises(TypeError):
            Calculator.multiply("ten", "five")
        with self.assertRaises(TypeError):
            Calculator.multiply("10", "five")

    def test_multiply_type_mismatch(self):
        with self.assertRaises(TypeError):
            Calculator.multiply(5, [1, 2])
        with self.assertRaises(TypeError):
            Calculator.multiply("10", [5])
            
    
    def test_result_accuracy(self):
        pass

    


if __name__ == "__main__":
    unittest.main()
