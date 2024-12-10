from Solver import Solver

class DayXSolver(Solver):
    def __init__(self, request, year, day, input=None):
        super().__init__(request, year, day, input)
        self.data = []
        for line in self.input:
            self.data.append(line)
        self.h = len(self.data)
        self.w = len(self.data[0])
        self.memory = {}


    def next_start(self, r, c):
        for i in range(r * self.w + c + 1, self.h * self.w):
            if self.data[i // self.w][i % self.w] == "0":
                return (i // self.w, i % self.w)
        return (-1, -1)
    
    def dfs1(self, r, c, trail_end_set):
        steps = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for step in steps:
            nr = r + step[0]
            nc = c + step[1]
            if 0 <= nr < self.h and 0 <= nc < self.w and int(self.data[nr][nc]) == int(self.data[r][c]) + 1:
                if self.data[nr][nc] == "9":
                    trail_end_set.add((nr,nc))
                else:
                    trail_end_set.union(self.dfs1(nr, nc, trail_end_set))
        return trail_end_set

    def dfs2(self, r, c):
        steps = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        result = 0
        for step in steps:
            nr = r + step[0]
            nc = c + step[1]
            if 0 <= nr < self.h and 0 <= nc < self.w and int(self.data[nr][nc]) == int(self.data[r][c]) + 1:
                if self.data[nr][nc] == "9":
                    result += 1
                else:
                    if (nr, nc) not in self.memory:
                        self.memory[(nr, nc)] = self.dfs2(nr, nc)
                    result += self.memory[(nr, nc)]
        return result
    
    def first_problem(self):
        result = 0
        r, c = self.next_start(0, -1)
        while (r, c) != (-1, -1):
            result += len(self.dfs1 (r, c, set()))
            r, c = self.next_start(r, c)
        return result
            
    def second_problem(self):
        result = 0
        r, c = self.next_start(0, -1)
        while (r, c) != (-1, -1):
            result += self.dfs2 (r, c)
            r, c = self.next_start(r, c)
        return result
            
def process(request, year, day):
    solver = DayXSolver(request, year, day)
    return (solver.process())