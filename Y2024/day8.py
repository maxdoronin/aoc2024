from Solver import Solver

class DayXSolver(Solver):
    def __init__(self, request, year, day, input=None):
        super().__init__(request, year, day, input)
        self.towers = {}
        self.positions = {}
        for r, line in enumerate(self.input):
            for c, character in enumerate(line):
                if character != ".":
                    t = self.towers.get(character, [])
                    t.append((r, c))
                    self.towers[character] = t
                    self.positions[(r, c)] = character
        self.antinodes = set()
        self.h = len(self.input)
        self.w = len(self.input[0])
    
    def first_problem(self):
        for tower, pos_list in self.towers.items():
            for i in range(len(pos_list)):
                for j in range(i + 1, len(pos_list)):
                    tower1 = pos_list[i]
                    tower2 = pos_list[j]
                    dr = tower2[0] - tower1[0]
                    dc = tower2[1] - tower1[1]
                    f1 = (tower1[0] - dr, tower1[1] - dc)
                    f2 = (tower2[0] + dr, tower2[1] + dc)

                    if 0 <= f1[0] < self.h and 0 <= f1[1] < self.w and tower != self.positions.get(f1, "."):
                        self.antinodes.add(f1)
                    if 0 <= f2[0] < self.h and 0 <= f2[1] < self.w and tower != self.positions.get(f2, "."):
                        self.antinodes.add(f2)
        return len(self.antinodes)
            
    def second_problem(self):
        self.antinodes = set()
        for _, pos_list in self.towers.items():
            for i in range(len(pos_list)):
                for j in range(i + 1, len(pos_list)):
                    tower1 = pos_list[i]
                    tower2 = pos_list[j]
                    dr = tower2[0] - tower1[0]
                    dc = tower2[1] - tower1[1]
                    k = 0
                    while 0 <= tower1[0] - dr * k < self.h and 0 <= tower1[1] - dc * k < self.w:
                        self.antinodes.add((tower1[0] - dr * k, tower1[1] - dc * k))
                        k += 1
                    k = 0
                    while 0 <= tower2[0] + dr * k < self.h and 0 <= tower2[1] + dc * k < self.w:
                        self.antinodes.add((tower2[0] + dr * k, tower2[1] + dc * k))
                        k += 1
        return len(self.antinodes)

def process(request, year, day):
    solver = DayXSolver(request, year, day)
    return (solver.process())