import unittest
from Y2024.day19 import DayXSolver

class TestDayXSolver(unittest.TestCase):
    def setUp(self):
        self.test_input1 = [
            "r, wr, b, g, bwu, rb, gb, br",
            "",
            "brwrr",
            "bggr",
            "gbbr",
            "rrbgbr",
            "ubwu",
            "bwurrg",
            "brgr",
            "bbrgwb"
        ]

    def test_first_problem(self):
        solver = DayXSolver(None, None, None, self.test_input1)
        self.assertEqual(solver.is_towel_possible("brwrr"), True)
        self.assertEqual(solver.is_towel_possible("bggr"), True)
        self.assertEqual(solver.is_towel_possible("ubwu"), False)
        self.assertEqual(solver.first_problem(), 6)

    def test_second_problem(self):
        solver = DayXSolver(None, None, None, self.test_input1)
        self.assertEqual(solver.count_combinations("brwrr"), 2)
        self.assertEqual(solver.count_combinations("rrbgbr"), 6)
        self.assertEqual(solver.count_combinations("bwurrg"), 1)
        self.assertEqual(solver.second_problem(), 16)

if __name__ == '__main__':
    unittest.main()