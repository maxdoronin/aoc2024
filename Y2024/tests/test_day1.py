import unittest
from Y2024.day1 import DayXSolver

class TestDayXSolver(unittest.TestCase):
    def setUp(self):
        self.test_input = [
            "3   4",
            "4   3",
            "2   5",
            "1   3",
            "3   9",
            "3   3"
        ]

    def test_first_problem(self):
        solver = DayXSolver(None, None, None, self.test_input)
        result = solver.first_problem()
        self.assertEqual(result, 11)

    def test_second_problem(self):
        solver = DayXSolver(None, None, None, self.test_input)
        result = solver.second_problem()
        self.assertEqual(result, 31)

if __name__ == '__main__':
    unittest.main()