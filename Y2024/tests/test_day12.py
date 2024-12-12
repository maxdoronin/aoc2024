import unittest
from Y2024.day12 import DayXSolver

class TestDayXSolver(unittest.TestCase):
    def setUp(self):
        self.test_input1 = [
            "RRRRIICCFF",
            "RRRRIICCCF",
            "VVRRRCCFFF",
            "VVRCCCJFFF",
            "VVVVCJJCFE",
            "VVIVCCJJEE",
            "VVIIICJJEE",
            "MIIIIIJJEE",
            "MIIISIJEEE",
            "MMMISSJEEE"
        ]
        self.test_input2 = [
            "AAAAAA",
            "AAABBA",
            "AAABBA",
            "ABBAAA",
            "ABBAAA",
            "AAAAAA"
        ]
        self.test_input3 = [
            "EEEEE",
            "EXXXX",
            "EEEEE",
            "EXXXX",
            "EEEEE"
        ]
        self.test_input4 = [
            "OOOOO",
            "OXOXO",
            "OOOOO",
            "OXOXO",
            "OOOOO"
        ]

    def test_first_problem(self):
        solver = DayXSolver(None, None, None, self.test_input4)
        self.assertEqual(solver.first_problem(), 772)
        solver = DayXSolver(None, None, None, self.test_input1)
        self.assertEqual(solver.first_problem(), 1930)

    def test_second_problem(self):
        solver = DayXSolver(None, None, None, self.test_input4)
        self.assertEqual(solver.first_problem(), 772)
        self.assertEqual(solver.second_problem(), 436)
        solver = DayXSolver(None, None, None, self.test_input3)
        self.assertEqual(solver.first_problem(), 692)
        self.assertEqual(solver.second_problem(), 236)
        solver = DayXSolver(None, None, None, self.test_input2)
        self.assertEqual(solver.first_problem(), 1184)
        self.assertEqual(solver.second_problem(), 368)
        solver = DayXSolver(None, None, None, self.test_input1)
        self.assertEqual(solver.first_problem(), 1930)
        self.assertEqual(solver.second_problem(), 1206)

if __name__ == '__main__':
    unittest.main()