import unittest
from Y2024.day8 import DayXSolver

class TestDayXSolver(unittest.TestCase):
    def setUp(self):
        self.test_input1 = [
            "............",
            "........0...",
            ".....0......",
            ".......0....",
            "....0.......",
            "......A.....",
            "............",
            "............",
            "........A...",
            ".........A..",
            "............",
            "............"
        ]

    def test_first_problem(self):
        solver = DayXSolver(None, None, None, self.test_input1)
        self.assertEqual(solver.first_problem(), 14)

    def test_second_problem(self):
        solver = DayXSolver(None, None, None, self.test_input1)
        self.assertEqual(solver.second_problem(), 34)

if __name__ == '__main__':
    unittest.main()