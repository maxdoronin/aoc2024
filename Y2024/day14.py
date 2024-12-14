from Solver import Solver

class DayXSolver(Solver):
    def __init__(self, request, year, day, input=None, rows=103, cols=101):
        super().__init__(request, year, day, input)
        self.rows = rows
        self.cols = cols
        self.data = []
        for l in self.input:
            p = l.split(" v=")[0].split("p=")[1].split(",")
            v = l.split(" v=")[1].split(",")
            self.data.append({"p": {"r": int(p[1]), "c": int(p[0])}, "v": {"r": int(v[1]), "c": int(v[0])}})

    def first_problem(self):
        q0, q1, q2, q3 = 0, 0, 0, 0
        for robot in self.data:
            vr = robot["v"]["r"]
            posr = vr * 100
            r = (robot["p"]["r"] + posr) % self.rows
            vc = robot["v"]["c"]
            posc = vc * 100
            c = (robot["p"]["c"] + posc) % self.cols

            if r < self.rows // 2:
                if c < self.cols // 2:
                    q0 += 1
                elif c > self.cols // 2:
                    q1 += 1
            elif r > self.rows // 2:
                if c < self.cols // 2:
                    q2 += 1
                elif c > self.cols // 2:
                    q3 += 1
        return q0 * q1 * q2 * q3

    def second_problem(self):
        result = [len(self.data), 0]
        time = 0
        while time < self.rows * self.cols:
        # while result < 3:
            folded_positions = {}
            robots = set()
            for robot in self.data:
                vr = robot["v"]["r"]
                deltar = vr * time
                r = (robot["p"]["r"] + deltar) % self.rows
                vc = robot["v"]["c"]
                deltac = vc * time
                c = (robot["p"]["c"] + deltac) % self.cols
                robots.add((r, c))
                
                l = folded_positions.get(r, {})
                if c < self.cols // 2:
                    l[c] = l.get(c, 0) + 1
                    folded_positions[r] = l
                elif c > self.cols // 2:
                    l[c] = l.get(self.cols - c  - 1, 0) - 1
                    folded_positions[r] = l
            
            symmetry = 0
            for l in folded_positions.values():
                symmetry += sum([abs(x) for x in l.values()])
            if symmetry < result[0]:
                result = [symmetry, time]
            time += 1
        return result[1]
             
def process(request, year, day):
    solver = DayXSolver(request, year, day)
    return (solver.process())