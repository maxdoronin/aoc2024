from Solver import Solver
import heapq

class DayXSolver(Solver):
    def __init__(self, request, year, day, input=None):
        super().__init__(request, year, day, input)
        self.list1 = []
        self.list2 = []
        for line in self.input:
            t = line.split()
            self.list1.append(int(t[0]))
            self.list2.append(int(t[1]))

    def first_problem(self):
        result = 0
        list1 = self.list1.copy()
        list2 = self.list2.copy()
        heapq.heapify(list1)
        heapq.heapify(list2)
        while list1:
            result += abs(heapq.heappop(list1) - heapq.heappop(list2))
        return result

    def second_problem(self):
        result = 0
        l2_counter = {}
        for l in self.list2:
            l2_counter[l] = l2_counter.get(l, 0) + 1
        for l in self.list1:
            result += l * l2_counter.get(l, 0)
        return result

def process(request, year, day):
    solver = DayXSolver(request, year, day)
    return (solver.process())