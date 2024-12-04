import unittest
from Y2024.day5 import DayXSolver

class TestDayXSolver(unittest.TestCase):
    def setUp(self):
        self.test_input1 = [
            "47|53",
            "97|13",
            "97|61",
            "97|47",
            "75|29",
            "61|13",
            "75|53",
            "29|13",
            "97|29",
            "53|29",
            "61|53",
            "97|53",
            "61|29",
            "47|13",
            "75|47",
            "97|75",
            "47|61",
            "75|61",
            "47|29",
            "75|13",
            "53|13",
            "",
            "75,47,61,53,29",
            "97,61,53,29,13",
            "75,29,13",
            "75,97,47,61,53",
            "61,13,29",
            "97,13,75,29,47"
        ]

    def test_first_problem(self):
        solver = DayXSolver(None, None, None, self.test_input1)
        result = solver.first_problem()
        self.assertEqual(result, 143)

    def test_second_problem(self):
        solver = DayXSolver(None, None, None, self.test_input1)
        result = solver.second_problem()
        self.assertEqual(result, 123)

if __name__ == '__main__':
    unittest.main()