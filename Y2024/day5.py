from Solver import Solver
from functools import cmp_to_key 

class DayXSolver(Solver):
    def __init__(self, request, year, day, input=None):
        super().__init__(request, year, day, input)
        self.rules = {}
        self.pages = []
        
        i = 0
        while self.input[i].strip() != "":
            t = [int(x) for x in self.input[i].split("|")]
            current_mapping = self.rules.get(t[0], set())
            current_mapping.add(t[1])
            self.rules[t[0]] = current_mapping
            i += 1
        
        i += 1
        while i < len(self.input):
            self.pages.append([int(x) for x in self.input[i].split(",")])
            i += 1

    def compare(self, x, y):
        if x in self.rules:
            if y in self.rules[x]:
                return -1
        if y in self.rules:
            if x in self.rules[y]:
                return 1
        return 0

    def first_problem(self):
        result = 0
        for page in self.pages:
            t = sorted(page, key=cmp_to_key(self.compare))
            if t == page:
                result += t[len(t) // 2]
        return result

    def second_problem(self):
        result = 0
        for page in self.pages:
            t = sorted(page, key=cmp_to_key(self.compare))
            if t != page:
                result += t[len(t) // 2]
        return result

def process(request, year, day):
    solver = DayXSolver(request, year, day)
    return (solver.process())