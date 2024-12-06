import unittest
from Y2024.day7 import DayXSolver

class TestDayXSolver(unittest.TestCase):
    def setUp(self):
        self.test_input1 = [
            "190: 10 19",
            "3267: 81 40 27",
            "83: 17 5",
            "156: 15 6",
            "7290: 6 8 6 15",
            "161011: 16 10 13",
            "192: 17 8 14",
            "21037: 9 7 18 13",
            "292: 11 6 16 20"
        ]

    def test_first_problem(self):
        solver = DayXSolver(None, None, None, self.test_input1)
        self.assertEqual(solver.dfs1(190), True)
        self.assertEqual(solver.dfs1(3267), True)
        self.assertEqual(solver.dfs1(292), True)
        self.assertEqual(solver.dfs1(161011), False)
        self.assertEqual(solver.dfs1(21037), False)
        self.assertEqual(solver.dfs1(83), False)
        self.assertEqual(solver.first_problem(), 3749)

    def test_second_problem(self):
        solver = DayXSolver(None, None, None, self.test_input1)
        self.assertEqual(solver.dfs2(156), True)
        self.assertEqual(solver.dfs2(7290), True)
        self.assertEqual(solver.dfs2(192), True)
        self.assertEqual(solver.dfs1(190), True)
        self.assertEqual(solver.dfs1(3267), True)
        self.assertEqual(solver.dfs1(292), True)
        self.assertEqual(solver.dfs2(21037), False)
        self.assertEqual(solver.dfs2(83), False)
        self.assertEqual(solver.dfs2(161011), False)
        self.assertEqual(solver.second_problem(), 11387)

if __name__ == '__main__':
    unittest.main()