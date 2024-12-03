from Solver import Solver
import math

class DayXSolver(Solver):
    def __init__(self, request, year, day, input=None):
        super().__init__(request, year, day, input)
        self.list = []
        for line in self.input:
            self.list.append([int(x) for x in line.split()])

    def is_safe(self, report):
        prev_step = report[0]
        step = report[1]
        prev_direction = 0 
        safe = True
        for i in range (1, len(report)):
            step = report[i]
            if not 0 < abs(step - prev_step) < 4:
                safe = False
                break
            else:
                direction = abs(step - prev_step) // (step - prev_step) # 1 if step > prev_step, -1 if step < prev_step
                if prev_direction != 0 and prev_direction != direction:
                    safe = False
                    break
            prev_step = step
            prev_direction = direction
        return (safe, i)
    
    def first_problem(self):
        result = 0
        for report in self.list:
            result += self.is_safe(report)[0]
        return result

    def second_problem(self):
        result = 0
        for report in self.list:
            safe, i = self.is_safe(report)
            if not safe:
                report1 = report.copy()
                report2 = report.copy()
                report3 = report.copy()
                report1.pop(i)
                report2.pop(i-1)
                report3.pop(0)
                temp = self.is_safe(report1)[0] or self.is_safe(report2)[0] or self.is_safe(report3)[0]
                result += temp
            else:
                result += 1
        return result

def process(request, year, day):
    solver = DayXSolver(request, year, day)
    return (solver.process())