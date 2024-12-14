import unittest
from Y2024.day17 import DayXSolver

class TestDayXSolver(unittest.TestCase):
    def setUp(self):
        self.test_input1 = [
            "Register A: 729",
            "Register B: 0",
            "Register C: 0",
            "",
            "Program: 0,1,5,4,3,0"
        ]
        self.test_input2 = [
            "Register A: 2024",
            "Register B: 0",
            "Register C: 0",
            "",
            "Program: 0,1,5,4,3,0"
        ]
        self.test_input3 = [
            "Register A: 2024",
            "Register B: 0",
            "Register C: 0",
            "",
            "Program: 0,3,5,4,3,0"
        ]

    def test_first_problem(self):
        solver = DayXSolver(None, None, None, self.test_input1)
        self.assertEqual(solver.first_problem(), "4,6,3,5,6,3,5,2,1,0")
        print ("=========")
        solver = DayXSolver(None, None, None, self.test_input2)
        self.assertEqual(solver.first_problem(), "4,2,5,6,7,7,7,7,3,1,0")

    def test_second_problem(self):
        solver = DayXSolver(None, None, None, self.test_input3)
        self.assertEqual(solver.second_problem(), 117440)

if __name__ == '__main__':
    unittest.main()