import unittest
from Y2024.day14 import DayXSolver

class TestDayXSolver(unittest.TestCase):
    def setUp(self):
        self.test_input1 = [
            "p=0,4 v=3,-3",
            "p=6,3 v=-1,-3",
            "p=10,3 v=-1,2",
            "p=2,0 v=2,-1",
            "p=0,0 v=1,3",
            "p=3,0 v=-2,-2",
            "p=7,6 v=-1,-3",
            "p=3,0 v=-1,-2",
            "p=9,3 v=2,3",
            "p=7,3 v=-1,2",
            "p=2,4 v=2,-3",
            "p=9,5 v=-3,-3"
        ]


    def test_first_problem(self):
        solver = DayXSolver(None, None, None, self.test_input1, 7, 11)
        self.assertEqual(solver.first_problem(), 12)

    def test_second_problem(self):
        solver = DayXSolver(None, None, None, self.test_input1, 7, 11)
        self.assertEqual(solver.second_problem(), 31) # It doesn't find the Christmas tree in the test input, just the max-symmetry point

if __name__ == '__main__':
    unittest.main()