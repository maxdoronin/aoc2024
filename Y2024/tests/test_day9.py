import unittest
from Y2024.day9 import DayXSolver

class TestDayXSolver(unittest.TestCase):
    def setUp(self):
        self.test_input1 = [
            "2333133121414131402"
        ]

    def test_init(self):
        solver = DayXSolver(None, None, None, self.test_input1)
        data_blocks1 = str([x.size for x in solver.data])
        data_blocks2 = str([int(solver.input[0][i*2]) for i in range(len(solver.input[0])//2 + 1)]) # parsing is accurate
        self.assertEqual(data_blocks1, data_blocks2)

    def test_find_first_free_block(self):
        solver = DayXSolver(None, None, None, self.test_input1)
        # size 1
        self.assertEqual(solver.find_first_free_block(solver.data, 0), (0, 2, 3))
        self.assertEqual(solver.find_first_free_block(solver.data, 1), (1, 8, 3))
        self.assertEqual(solver.find_first_free_block(solver.data, 2), (2, 12, 3))
        self.assertEqual(solver.find_first_free_block(solver.data, 9), (9, 42, 0))
        self.assertEqual(solver.find_first_free_block(solver.data, 10), (9, 42, 0))
        # size > 1
        self.assertEqual(solver.find_first_free_block(solver.data, 0, 2), (0, 2, 3))
        self.assertEqual(solver.find_first_free_block(solver.data, 0, 4), (9, 42, 0))
        self.assertEqual(solver.find_first_free_block(solver.data, 2, 2), (2, 12, 3))
        self.assertEqual(solver.find_first_free_block(solver.data, 2, 4), (9, 42, 0))

    def test_first_problem(self):
        solver = DayXSolver(None, None, None, self.test_input1)
        self.assertEqual(solver.first_problem(), 1928)

    def test_second_problem(self):
        solver = DayXSolver(None, None, None, self.test_input1)
        self.assertEqual(solver.second_problem(), 2858)

if __name__ == '__main__':
    unittest.main()