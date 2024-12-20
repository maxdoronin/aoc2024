from Solver import Solver

class DayXSolver(Solver):
    def __init__(self, request, year, day, input=None, rows=103, cols=101):
        super().__init__(request, year, day, input)
        self.grid = []
        self.walls = set()
        self.boxes = set()
        r = 0
        while self.input[r].strip() != "":
            for c, obj in enumerate(self.input[r]):
                if obj == "#":
                    self.walls.add((r, c))
                elif obj == "O":
                    self.boxes.add((r, c))
                elif obj == "@":
                    self.robot = (r, c)
            self.grid.append(self.input[r])
            r += 1
        self.moves = "".join(self.input[r:])
        self.dirs = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}

    def move(self, robot, move):
        r, c = robot[0], robot[1]
        dr, dc = self.dirs[move]
        r1, c1 = r + dr, c + dc
        if (r1, c1) in self.walls:
            return (r, c)
        box_stack = set()
        r2, c2 = r1, c1
        while (r2, c2) in self.boxes:
            box_stack.add((r2, c2))
            r2, c2 = r2 + dr, c2 + dc
        if (r2, c2) in self.walls:
            return (r, c)
        else:
            moved_box_stack = set()
            for box in box_stack:
                moved_box = (box[0] + dr, box[1] + dc)
                moved_box_stack.add(moved_box)
                self.boxes = self.boxes.difference(box_stack)
                self.boxes = self.boxes.union(moved_box_stack)
        return (r1, c1)
    
    def draw(self):
        for r in range(len(self.grid)):
            for c in range(len(self.grid[0])):
                if (r, c) in self.boxes:
                    print("O", end="")
                elif (r, c) in self.walls:
                    print("#", end="")
                elif (r, c) == self.robot:
                    print ("@", end="")
                else:
                    print(".", end="")
            print()

    def first_problem(self):
        for move in self.moves:
            self.robot = self.move(self.robot, move)
        self.draw()
        result = 0
        for box in self.boxes:
            result += 100 * box[0] + box[1]
        return result

    def second_problem(self):
        return 0
             
def process(request, year, day):
    solver = DayXSolver(request, year, day)
    return (solver.process())