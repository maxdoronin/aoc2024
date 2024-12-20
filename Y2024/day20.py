from Solver import Solver

class DayXSolver(Solver):
    def __init__(self, request, year, day, input=None, **kwargs):
        super().__init__(request, year, day, input)
        self.directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        for r, line in enumerate(self.input):
            for c, char in enumerate(line):
                if char == "S":
                    self.sr = r
                    self.sc = c
                    break

    def chart_track(self, r, c, visited):
        
        time = 0
        queue = [((r, c), 0)]

        while queue:
            (r, c), time = queue.pop(0)

            visited[(r, c)] = time
            if self.input[r][c] == "E":
                return
            for dr, dc in self.directions:
                if self.input[r + dr][c + dc] == "#" or (r + dr, c + dc) in visited:
                    continue
                queue.append(((r + dr, c + dc), time + 1))
        return
    
    def find_cheats(self, visited):
        cheats = {}
        for (r, c), time in visited.items():
            for dir in self.directions:
                r1 = r + dir[0] * 2
                c1 = c + dir[1] * 2
                if (r1, c1) in visited and visited[(r1, c1)] > time + 2:
                    cheats[((r, c), (r1, c1))] = visited[(r1, c1)] - time - 2
        return cheats
                       
    def first_problem(self):
        visited = {}
        self.chart_track(self.sr, self.sc, visited)
        cheats = self.find_cheats(visited)

        result = 0
        target = 100
        for cut_time in sorted(cheats.values(), reverse=True):
            if cut_time >= target:
                result += 1
        return result

    def second_problem(self):
        result = 0
        return result
             
def process(request, year, day):
    solver = DayXSolver(request, year, day)
    return (solver.process())