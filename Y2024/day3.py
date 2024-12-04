from Solver import Solver
import math

class DayXSolver(Solver):
    def __init__(self, request, year, day, input=None):
        super().__init__(request, year, day, input)

    def first_problem(self):
        result = 0
        for line in self.input:
            i = 0
            while i < len(line) - 3:
                if line[i:i + len("mul(")] == "mul(":
                    j = i + 4
                    k = 0
                    while line[j + k] != "," and k < 4 and line[j + k].isdigit():
                        k += 1
                    if line[j + k] == "," and 0 < k < 4 and line[j + k - 1].isdigit():
                        x = int(line[j:j + k])
                        i = j + k
                    else:
                        i = j + k
                        continue
                    if line[j + k] != ",":
                        i = j + k
                        continue
                    j = i + 1
                    k = 0
                    while line[j + k] != ")" and k < 4 and line[j + k].isdigit():
                        k += 1
                    if line[j + k] == ")" and 0 < k < 4 and line[j + k - 1].isdigit():
                        y = int(line[j:j + k])
                    else:
                        i = j + k
                        continue
                    result += x * y
                    i = j + k
                i += 1
        return result


    def second_problem(self):
        result = 0
        do = True
        for line in self.input:
            i = 0
            while i < len(line) - 3:
                if line[i:i + len("do()")] == "do()":
                    do = True
                if line[i:i + len("don't()")] == "don't()":
                    do = False
                if line[i:i + len("mul(")] == "mul(":
                    j = i + 4
                    k = 0
                    while line[j + k] != "," and k < 4 and line[j + k].isdigit():
                        k += 1
                    if line[j + k] == "," and 0 < k < 4 and line[j + k - 1].isdigit():
                        x = int(line[j:j + k])
                        i = j + k
                    else:
                        i = j + k
                        continue
                    if line[j + k] != ",":
                        i = j + k
                        continue
                    j = i + 1
                    k = 0
                    while line[j + k] != ")" and k < 4 and line[j + k].isdigit():
                        k += 1
                    if line[j + k] == ")" and 0 < k < 4 and line[j + k - 1].isdigit():
                        y = int(line[j:j + k])
                    else:
                        i = j + k
                        continue
                    if do:
                        result += x * y
                    i = j + k
                i += 1
        return result
    
def process(request, year, day):
    solver = DayXSolver(request, year, day)
    return (solver.process())