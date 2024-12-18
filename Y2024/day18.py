from Solver import Solver

class DayXSolver(Solver):
    def __init__(self, request, year, day, input=None, **kwargs):
        super().__init__(request, year, day, input)
        self.data = []
        self.visited = {}
        for line in self.input:
            coords = line.split(",")
            self.data.append((int(coords[1]), int(coords[0])))
        self.rows = kwargs.get("rows", 71)
        self.cols = kwargs.get("cols", 71)
        self.byte_count = kwargs.get("byte_count", 1024)

    def dfs(self, r, c, bad_bytes, visited):
        stack = [((r, c), 0)]

        while stack:
            (r, c), time = stack.pop()

            if not (0 <= r < self.rows and 0 <= c < self.cols):
                continue
            if (r, c) in visited and visited[(r, c)] <= time:
                continue
            if (r, c) in bad_bytes:
                continue
            visited[(r, c)] = time

            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                stack.append(((r + dr, c + dc), time + 1))
        return

    def draw(self, visited):
        print ()
        for r in range(self.rows):
            for c in range(self.cols):
                if (r, c) in visited:
                    print("{:02d}".format(visited[(r, c)]), end="|")
                else:
                    print("..", end="|")
            print()

    def first_problem(self):
        self.visited = {}
        bad_bytes = self.data[0:self.byte_count]
        self.dfs(self.rows - 1, self.cols - 1, bad_bytes, self.visited)
        return self.visited[(0, 0)]

    def second_problem(self):
        self.visited = {}
        baddest_byte_no = len(self.data) - 1
        while (0, 0) not in self.visited:
            self.visited = {}
            bad_bytes = self.data[0:baddest_byte_no]
            self.dfs(self.rows - 1, self.cols - 1, bad_bytes, self.visited)
            baddest_byte_no -= 1
        return (self.data[baddest_byte_no + 1][1], self.data[baddest_byte_no + 1][0])
             
def process(request, year, day):
    solver = DayXSolver(request, year, day)
    return (solver.process())