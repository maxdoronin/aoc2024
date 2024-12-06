from Solver import Solver
import copy

class DayXSolver(Solver):
    def __init__(self, request, year, day, input=None):
        super().__init__(request, year, day, input)
        self.directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        self.directions_map = {"^": 0, ">": 1, "v": 2, "<": 3}
        self.start_r, self.start_c, self.start_dir = self.find_start()

    def set_map(self, r, c, value, map):
        map[r] = map[r][:c] + value + map[r][c+1:]

    def step(self, r, c, dir):
        r += self.directions[dir][0]
        c += self.directions[dir][1]
        return (r, c)
    
    def step_back(self, r, c, dir):
        r -= self.directions[dir][0]
        c -= self.directions[dir][1]
        return (r, c)

    def is_in_bounds(self, r, c):
        return 0 <= r < len(self.input) and 0 <= c < len(self.input[0])
    
    def find_start(self):
        for r, list_line in enumerate (self.input):
            for c, char in enumerate(list_line):
                if char in self.directions_map:
                    self.set_map(r, c, ".", self.input)
                    return (r, c, self.directions_map[char])

    def go1(self, r, c, dir, map):
        result = 0
        turns = set()   # needed for the second problem

        while self.is_in_bounds(r, c):
            if map[r][c] == ".":
                result += 1
            self.set_map(r, c, str(dir), map)
            r, c = self.step(r, c, dir)
            if self.is_in_bounds(r, c) and map[r][c] == "#":
                r, c = self.step_back(r, c, dir)
                dir += 1
                dir %= 4

                # this part checks if we are in a loop
                turn = (r, c, dir)
                if turn in turns:
                    return -1
                turns.add(turn)
        return result
    
    def go2(self, r, c, dir, map):
        result = set()
        while self.is_in_bounds(r, c):
            r1, c1 = self.step(r, c, dir)
            if self.is_in_bounds(r1, c1) and map[r1][c1] == "." and (r1, c1) not in result:
                t_map = copy.deepcopy(self.input)
                self.set_map(r1, c1, "#", t_map)
                if (r1, c1) != (self.start_r, self.start_c):
                    if self.go1(r, c, (dir + 1) % 4, t_map) == -1:
                        result.add((r1,c1))
            self.set_map(r, c, str(dir), map)
            r, c = self.step(r, c, dir)
            if self.is_in_bounds(r, c) and map[r][c] == "#":
                r, c = self.step_back(r, c, dir)
                dir += 1
                dir %= 4
            
        return result    
                            
    def first_problem(self):
        input_copy = copy.deepcopy(self.input)
        result = self.go1(self.start_r, self.start_c, self.start_dir, input_copy)
        return result

    def second_problem(self):
        input_copy = copy.deepcopy(self.input)
        result = self.go2(self.start_r, self.start_c, self.start_dir, input_copy)
        return len(result)

def process(request, year, day):
    solver = DayXSolver(request, year, day)
    return (solver.process())