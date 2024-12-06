from Solver import Solver

class DayXSolver(Solver):
    def __init__(self, request, year, day, input=None):
        super().__init__(request, year, day, input)
        self.calibration_values = {}
        for line in self.input:
            target_s, operands_s = line.split(":")
            target = int(target_s)
            operands = [int(x) for x in operands_s.strip().split(" ")]
            self.calibration_values[target] = operands

    def dfs1 (self, target, i=0, c_target=0):
        operands = self.calibration_values[target]
        if c_target > target:
            return False
        if i == len(operands):
            return c_target == target
        
        return (self.dfs1 (target, i + 1, c_target + operands[i]) or
                self.dfs1 (target, i + 1, c_target * operands[i]))

    def dfs2 (self, target, i=0, c_target=0):
        operands = self.calibration_values[target]
        if c_target > target:
            return False
        if i == len(operands):
            return c_target == target
        
        return (self.dfs2 (target, i + 1, c_target + operands[i]) or
                self.dfs2 (target, i + 1, c_target * operands[i]) or
                self.dfs2 (target, i + 1, int(str(c_target) + str(operands[i]))))

    
    def first_problem(self):
        result = 0
        for target in self.calibration_values.keys():
            if self.dfs1(target):
                result += target
        return result

    def second_problem(self):
        result = 0
        for target in self.calibration_values.keys():
           if self.dfs2(target):
               result += target
        return result

def process(request, year, day):
    solver = DayXSolver(request, year, day)
    return (solver.process())