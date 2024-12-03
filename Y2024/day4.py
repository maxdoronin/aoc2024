from Solver import Solver
import math

class DayXSolver(Solver):
    def __init__(self, request, year, day, input=None):
        super().__init__(request, year, day, input)

    def check_for_problem_1(self, r, c, step):
        pattern = "XMAS"
        for k, l in enumerate(pattern):
            new_r = r + step[0] * k
            new_c = c + step[1] * k
            if new_r < 0 or new_r >= len(self.input) or new_c < 0 or new_c >= len(self.input[0]):
                return False
            if self.input[new_r][new_c] != l:
                return False
        return True

    def first_problem(self):
        result = 0
        step_options = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        for r in range(len(self.input)):
            for c in range(len(self.input[r])):
                if self.input[r][c] == "X":
                    for step in step_options:
                        result += self.check_for_problem_1(r, c, step)
        return result


    def word_for_problem_2(self, r, c, step):
        word = ""
        for k in range(3):
            new_r = r + step[0] * k
            new_c = c + step[1] * k
            word += self.input[new_r][new_c]
        return word
    
    def second_problem(self):
        result = 0
        d_steps = [(1, 1), (-1, 1)]

        for r in range(1, len(self.input) - 1):
            for c in range(1, len(self.input[r]) - 1):
                if self.input[r][c] == "A":

                    w1, w2 = "", ""
                    w1 = self.word_for_problem_2(r-1, c-1, d_steps[0])
                    if w1 == "MAS" or w1 == "SAM":
                        w2 = self.word_for_problem_2(r+1, c-1, d_steps[1])
                        if w2 == "MAS" or w2 == "SAM":
                            result += 1
        return result

    
def process(request, year, day):
    solver = DayXSolver(request, year, day)
    return (solver.process())