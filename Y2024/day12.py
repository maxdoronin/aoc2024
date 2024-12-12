from Solver import Solver

class DayXSolver(Solver):
    def __init__(self, request, year, day, input=None):
        super().__init__(request, year, day, input)
        self.grid = self.input
    
    def bfs1(self, r, c, grid, visited):
        steps = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        area = 0
        perimeter = 0
        queue = [(r, c)]
        while queue:
            r, c = queue.pop(0)
            if (r, c) in visited:
                continue
            area += 1
            visited.add((r, c))
            plot_id = grid[r][c]
            for step in steps:
                nr, nc = r + step[0], c + step[1]
                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                    if plot_id != grid[nr][nc]:
                        perimeter += 1
                    elif (nr, nc) not in visited:
                        queue.append((nr, nc))
                else:
                    perimeter += 1
        return (area, perimeter)
    
    def first_problem(self):
        result = 0
        global_visited = set()
        for r in range(len(self.grid)):
            for c in range(len(self.grid[0])):
                if (r, c) not in global_visited:
                    a, p = self.bfs1(r, c, self.grid, global_visited)
                    result += a * p
        return result
            
    def second_problem(self):
        result = 0
        return result
             
def process(request, year, day):
    solver = DayXSolver(request, year, day)
    return (solver.process())