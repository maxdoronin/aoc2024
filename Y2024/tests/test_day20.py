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
        cheats = solver.find_cheats(visited, 2)
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
        visited = {}
        solver.chart_track(solver.sr, solver.sc, visited)
        cheats = solver.find_cheats(visited, 20)
        cheat_times = sorted(cheats.values(), reverse=True)
        self.assertEqual(cheat_times.count(76), 3)
        self.assertEqual(cheat_times.count(74), 4)
        self.assertEqual(cheat_times.count(72), 22)
        self.assertEqual(cheat_times.count(70), 12)
        self.assertEqual(cheat_times.count(50), 32)
        self.assertEqual(cheat_times.count(52), 31)
        self.assertEqual(solver.second_problem(), 0)

if __name__ == '__main__':
    unittest.main()