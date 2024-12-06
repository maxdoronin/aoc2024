from Solver import Solver

class DayXSolver(Solver):
    def __init__(self, request, year, day, input=None):
        super().__init__(request, year, day, input)

    def first_problem(self):
        result = 0
        return result

    def second_problem(self):
        result = 0
        return len(result)

def process(request, year, day):
    solver = DayXSolver(request, year, day)
    return (solver.process())