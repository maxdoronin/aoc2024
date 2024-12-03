import unittest
from Y2024.day4 import DayXSolver

class TestDayXSolver(unittest.TestCase):
    def setUp(self):
        self.test_input1 = [
            "MMMSXXMASM",
            "MSAMXMSMSA",
            "AMXSXMAAMM",
            "MSAMASMSMX",
            "XMASAMXAMM",
            "XXAMMXXAMA",
            "SMSMSASXSS",
            "SAXAMASAAA",
            "MAMMMXMMMM",
            "MXMXAXMASX"
        ]
    def test_first_problem(self):
        solver = DayXSolver(None, None, None, self.test_input1)
        result = solver.first_problem()
        self.assertEqual(result, 18)

    def test_second_problem(self):
        solver = DayXSolver(None, None, None, self.test_input1)
        result = solver.second_problem()
        self.assertEqual(result, 9)

if __name__ == '__main__':
    unittest.main()