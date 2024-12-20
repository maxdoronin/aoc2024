import unittest
from Y2024.day20 import DayXSolver

class TestDayXSolver(unittest.TestCase):
    def setUp(self):
        self.test_input1 = [
            "###############",
            "#...#...#.....#",
            "#.#.#.#.#.###.#",
            "#S#...#.#.#...#",
            "#######.#.#.###",
            "#######.#.#...#",
            "#######.#.###.#",
            "###..E#...#...#",
            "###.#######.###",
            "#...###...#...#",
            "#.#####.#.###.#",
            "#.#...#.#.#...#",
            "#.#.#.#.#.#.###",
            "#...#...#...###",
            "###############"
        ]

    def test_first_problem(self):
        solver = DayXSolver(None, None, None, self.test_input1)
        visited = {}
        solver.chart_track(solver.sr, solver.sc, visited)
        cheats = solver.find_cheats(visited)
        cheat_times = sorted(cheats.values(), reverse=True)
        self.assertEqual(cheat_times.count(64), 1)
        self.assertEqual(cheat_times.count(40), 1)
        self.assertEqual(cheat_times.count(38), 1)
        self.assertEqual(cheat_times.count(12), 3)
        self.assertEqual(cheat_times.count(4), 14)
        self.assertEqual(cheat_times.count(2), 14)
        self.assertEqual(solver.first_problem(), 0)

    def test_second_problem(self):
        solver = DayXSolver(None, None, None, self.test_input1)
        self.assertEqual(solver.second_problem(), 0)

if __name__ == '__main__':
    unittest.main()