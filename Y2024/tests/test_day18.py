import unittest
from Y2024.day18 import DayXSolver

class TestDayXSolver(unittest.TestCase):
    def setUp(self):
        self.test_input1 = [
            "5,4",
            "4,2",
            "4,5",
            "3,0",
            "2,1",
            "6,3",
            "2,4",
            "1,5",
            "0,6",
            "3,3",
            "2,6",
            "5,1",
            "1,2",
            "5,5",
            "2,5",
            "6,5",
            "1,4",
            "0,4",
            "6,4",
            "1,1",
            "6,1",
            "1,0",
            "0,5",
            "1,6",
            "2,0"
        ]

    def test_first_problem(self):
        solver = DayXSolver(None, None, None, self.test_input1, rows=7, cols=7, byte_count=12)
        self.assertEqual(solver.first_problem(), 22)

    def test_second_problem(self):
        solver = DayXSolver(None, None, None, self.test_input1, rows=7, cols=7, byte_count=12)
        self.assertEqual(solver.second_problem(), (6,1))

if __name__ == '__main__':
    unittest.main()