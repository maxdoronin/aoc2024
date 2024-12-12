from Solver import Solver

class DayXSolver(Solver):
    def __init__(self, request, year, day, input=None):
        super().__init__(request, year, day, input)
        self.grid = self.input
        self.walls = {}
    
    def bfs1(self, r, c, grid, visited):
        def find_walls(grid, walls, steps, r, c):
            plot_id = grid[r][c]
            for step in steps:
                nr, nc = r + step[0], c + step[1]
                if not (0 <= nr < len(grid) and 0 <= nc < len(grid[0])) or grid[nr][nc] != plot_id:
                    if step[2] == "h":
                        coord1 = r + step[3]
                        coord2 = c + step[4]
                    else:
                        coord1 = c + step[4]
                        coord2 = r + step[3]
                    walls_set = walls[step[2]].get(coord1, set())
                    walls_set.add(coord2)
                    walls[step[2]][coord1] = walls_set

        steps = [(0, 1, "v", 0, 1), (0, -1, "v", 0, 0), (1, 0, "h", 1, 0), (-1, 0, "h", 0, 0)]
        area = 0
        perimeter = 0
        queue = [(r, c)]
        walls = {"h": {}, "v": {}}
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
                    find_walls(self.grid, walls, steps, r, c)
                    if plot_id != grid[nr][nc]:
                        perimeter += 1
                    elif (nr, nc) not in visited:
                        queue.append((nr, nc))
                else:
                    perimeter += 1

        return (area, perimeter, walls)

    def first_problem(self):
        result = 0
        global_visited = set()
        for r in range(len(self.grid)):
            for c in range(len(self.grid[0])):
                if (r, c) not in global_visited:
                    a, p, walls = self.bfs1(r, c, self.grid, global_visited)
                    area_walls = self.walls.get(self.grid[r][c], [])
                    area_walls.append((a, walls))
                    self.walls[self.grid[r][c]] = (area_walls)
                    result += a * p
        return result
            
    def second_problem(self):
        result = 0
        for area, walls in self.walls.items(): # loop through the same area id
            for a, area_instance_walls in walls: # different instances with the same area id
                wall_count = 0
                for coord, walls_at_coord in area_instance_walls["h"].items(): # horizontal walls
                    prev_wall_segment = -2
                    for wall_segment in sorted(list(walls_at_coord)): # wall segments
                        if wall_segment - prev_wall_segment > 1: # New wall after a gap
                            wall_count += 1
                        if  (coord - 1 in area_instance_walls["v"].get(wall_segment + 1, set()) and
                             coord in area_instance_walls["v"].get(wall_segment + 1, set())): # Moebius case
                            wall_count += 1
                        prev_wall_segment = wall_segment
                for coord, walls_at_coord in area_instance_walls["v"].items(): # vertical walls
                    prev_wall_segment = -2
                    for wall_segment in sorted(list(walls_at_coord)): # New wall after a gap
                        if wall_segment - prev_wall_segment > 1:
                            wall_count += 1
                        if  (coord - 1 in area_instance_walls["h"].get(wall_segment + 1, set()) and
                             coord in area_instance_walls["h"].get(wall_segment + 1, set())): # Moebius case
                            wall_count += 1
                        prev_wall_segment = wall_segment
                result += a * wall_count
        return result
             
def process(request, year, day):
    solver = DayXSolver(request, year, day)
    return (solver.process())