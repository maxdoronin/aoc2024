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
        self.assertEqual(len(solver.dfs1(0, 2, set())), 5)
        self.assertEqual(len(solver.dfs1(0, 4, set())), 6)
        self.assertEqual(len(solver.dfs1(2, 4, set())), 5)
        self.assertEqual(len(solver.dfs1(4, 6, set())), 3)
        self.assertEqual(len(solver.dfs1(5, 2, set())), 1)
        self.assertEqual(len(solver.dfs1(5, 5, set())), 3)
        self.assertEqual(len(solver.dfs1(6, 0, set())), 5)
        self.assertEqual(len(solver.dfs1(6, 6, set())), 3)
        self.assertEqual(len(solver.dfs1(7, 1, set())), 5)
        self.assertEqual(solver.first_problem(), 36)

    def test_second_problem(self):
        solver = DayXSolver(None, None, None, self.test_input1)
        self.assertEqual(solver.dfs2(0, 2), 20)
        self.assertEqual(solver.dfs2(0, 4), 24)
        self.assertEqual(solver.dfs2(2, 4), 10)
        self.assertEqual(solver.dfs2(4, 6), 4)
        self.assertEqual(solver.dfs2(5, 2), 1)
        self.assertEqual(solver.dfs2(5, 5), 4)
        self.assertEqual(solver.dfs2(6, 0), 5)
        self.assertEqual(solver.dfs2(6, 6), 8)
        self.assertEqual(solver.dfs2(7, 1), 5)
        self.assertEqual(solver.second_problem(), 81)
if __name__ == '__main__':
    unittest.main()