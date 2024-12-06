import unittest
from Y2024.day6 import DayXSolver

class TestDayXSolver(unittest.TestCase):
    def setUp(self):
        self.test_input1 = [
            "....#.....",
            ".........#",
            "..........",
            "..#.......",
            ".......#..",
            "..........",
            ".#..^.....",
            "........#.",
            "#.........",
            "......#..."
        ]

    def test_first_problem(self):
        solver = DayXSolver(None, None, None, self.test_input1)
        result = solver.first_problem()
        self.assertEqual(result, 41)

    def test_second_problem(self):
        solver = DayXSolver(None, None, None, self.test_input1)
        result = solver.second_problem()
        self.assertEqual(result, 6)

if __name__ == '__main__':
    unittest.main()