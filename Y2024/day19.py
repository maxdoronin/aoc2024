from Solver import Solver

class DayXSolver(Solver):
    def __init__(self, request, year, day, input=None, **kwargs):
        super().__init__(request, year, day, input)
        self.patterns = set([x.strip() for x in self.input[0].split(",")])
        self.pattern_min_len = min([len(x) for x in self.patterns])
        self.pattern_max_len = max([len(x) for x in self.patterns])
        self.towels = self.input[2:]
        self.memory = {}

    def is_towel_possible(self, towel):
        if towel in self.memory:
            return self.memory[towel]
        for pattern_len in range(self.pattern_min_len, self.pattern_max_len + 1):
            if pattern_len > len(towel):
                self.memory[towel] = False
                return False
            if towel[:pattern_len] in self.patterns:
                if pattern_len == len(towel):
                    self.memory[towel] = True
                    return True
                if self.is_towel_possible(towel[pattern_len:]):
                    self.memory[towel] = True
                    return True
                else:
                    continue
        self.memory[towel] = False
        return False

    def count_combinations(self, towel):
        if towel in self.memory:
            return self.memory[towel]
        counter = 0
        for pattern in self.patterns:
            if len(pattern) > len(towel):
                continue
            if towel.startswith(pattern):
                if len(pattern) == len(towel):
                    counter += 1
                else:
                    counter += self.count_combinations(towel[len(pattern):])
        self.memory[towel] = counter
        return self.memory[towel]
                    
    def first_problem(self):
        self.memory = {}
        result = 0
        for towel in self.towels:
            result += self.is_towel_possible(towel)
        return result

    def second_problem(self):
        self.memory = {}
        result = 0
        for towel in self.towels:
            result += self.count_combinations(towel)
        return result
             
def process(request, year, day):
    solver = DayXSolver(request, year, day)
    return (solver.process())