import unittest
from Y2024.day2 import DayXSolver

class TestDayXSolver(unittest.TestCase):
    def setUp(self):
        self.test_input = [
            "7 6 4 2 1",
            "1 2 7 8 9",
            "9 7 6 2 1",
            "1 3 2 4 5",
            "8 6 4 4 1",
            "1 3 6 7 9"
        ]

    def test_first_problem(self):
        solver = DayXSolver(None, None, None, self.test_input)
        result = solver.first_problem()
        self.assertEqual(result, 2)

    def test_second_problem(self):
        solver = DayXSolver(None, None, None, self.test_input)
        result = solver.second_problem()
        self.assertEqual(result, 4)

if __name__ == '__main__':
    unittest.main()