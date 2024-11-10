import unittest
from math_quiz import function_1, function_2, function_3

class TestMathGame(unittest.TestCase):

    def test_function_1(self):
        # Test if random numbers generated are within the specified range
        min_val = 0
        max_val = 8
        for _ in range(1000):  # Test a large number of random values
            rand_num = function_1(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_function_2(self):
        # Test if function_2 returns a valid operator
        operators = ['+', '-', '*']
        for _ in range(1000):
            op = function_2()
            self.assertIn(op, operators)

    def test_function_3(self):
        # Define test cases for function_3 with various operators
        test_cases = [
            (5, 2, '+', '5 + 2', 7),
            (5, 2, '-', '5 - 2', 3),
            (5, 2, '*', '5 * 2', 10),
            (8, 3, '+', '8 + 3', 11),
            (10, 4, '-', '10 - 4', 6),
            (6, 7, '*', '6 * 7', 42)
        ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            problem, answer = function_3(num1, num2, operator)
            self.assertEqual(problem, expected_problem)
            self.assertEqual(answer, expected_answer)

if __name__ == "__main__":
    unittest.main()
