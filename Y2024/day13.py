from Solver import Solver
import numpy as np

class DayXSolver(Solver):
    def __init__(self, request, year, day, input=None):
        super().__init__(request, year, day, input)
        self.data1 = []
        self.data2 = []
        for i in range(0, len(self.input), 4):
            t = self.input[i].split(":")[1].split(",")
            a1 = int(t[0].split("+")[1])
            a2 = int(t[1].split("+")[1])
            t = self.input[i + 1].split(":")[1].split(",")
            b1 = int(t[0].split("+")[1])
            b2 = int(t[1].split("+")[1])
            t = self.input[i + 2].split(":")[1].split(",")
            x = int(t[0].split("=")[1])
            y = int(t[1].split("=")[1])
            self.data1.append({"a1": a1, "a2": a2, "b1": b1, "b2": b2, "x": x, "y": y})
            self.data2.append({"a1": a1, "a2": a2, "b1": b1, "b2": b2, "x": x + 10000000000000, "y": y + 10000000000000})
    
    def solve(self, d):
        M = np.array([[d["a1"], d["b1"]], [d["a2"], d["b2"]]])
        T = np.array([d["x"], d["y"]])
        a, b = np.linalg.solve(M, T)
        a, b = round(a), round(b)
        if not np.all(np.equal(np.dot(M, [a, b]), T)):
            a, b = 0, 0
        return a, b
        
    def first_problem(self):
        result = 0
        for d in self.data1:
            a, b = self.solve(d)
            result += a*3 + b
        return result
            
    def second_problem(self):
        result = 0
        for d in self.data2:
            a, b = self.solve(d)
            result += a*3 + b
        return result
             
def process(request, year, day):
    solver = DayXSolver(request, year, day)
    return (solver.process())