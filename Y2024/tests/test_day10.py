import unittest
from Y2024.day10 import DayXSolver

class TestDayXSolver(unittest.TestCase):
    def setUp(self):
        self.test_input1 = [
            "89010123",
            "78121874",
            "87430965",
            "96549874",
            "45678903",
            "32019012",
            "01329801",
            "10456732"
        ]
    
    def test_next_start(self):
        solver = DayXSolver(None, None, None, self.test_input1)
        self.assertEqual(solver.next_start(0, 0), (0, 2))        
        self.assertEqual(solver.next_start(0, 2), (0, 4))        
        self.assertEqual(solver.next_start(0, 4), (2, 4))        
        self.assertEqual(solver.next_start(2, 4), (4, 6))        

    def test_first_problem(self):
        solver = DayXSolver(None, None, None, self.test_input1)
        test_paths = {
            (0, 2): 5,
            (0, 4): 6,
            (2, 4): 5,
            (4, 6): 3,
            (5, 2): 1,
            (5, 5): 3,
            (6, 0): 5,
            (6, 6): 3,
            (7, 1): 5
        }
        for start, expected in test_paths.items():
            self.assertEqual(len(solver.dfs1(*start, set())), expected)
        self.assertEqual(solver.first_problem(), 36)

    def test_second_problem(self):
        solver = DayXSolver(None, None, None, self.test_input1)
        test_paths = {
            (0, 2): 20,
            (0, 4): 24,
            (2, 4): 10,
            (4, 6): 4,
            (5, 2): 1,
            (5, 5): 4,
            (6, 0): 5,
            (6, 6): 8,
            (7, 1): 5
        }
        for start, expected in test_paths.items():
            self.assertEqual(solver.dfs2(*start), expected)
        self.assertEqual(solver.second_problem(), 81)
if __name__ == '__main__':
    unittest.main()