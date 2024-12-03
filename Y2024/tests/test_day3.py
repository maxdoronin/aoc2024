import unittest
from Y2024.day3 import DayXSolver

class TestDayXSolver(unittest.TestCase):
    def setUp(self):
        self.test_input1 = [
            "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
        ]
        self.test_input2 = [
            "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
        ]

    def test_first_problem(self):
        solver = DayXSolver(None, None, None, self.test_input1)
        result = solver.first_problem()
        self.assertEqual(result, 161)

    def test_second_problem(self):
        solver = DayXSolver(None, None, None, self.test_input2)
        result = solver.second_problem()
        self.assertEqual(result, 48)

if __name__ == '__main__':
    unittest.main()