from Solver import Solver

class DayXSolver(Solver):
    def __init__(self, request, year, day, input=None):
        super().__init__(request, year, day, input)
        self.R = {}
        self.R[0] = int(self.input[0].split(":")[1].strip())
        self.R[1] = int(self.input[1].split(":")[1].strip())
        self.R[2] = int(self. input[2].split(":")[1].strip())
        self.prog = [int(x) for x in self.input[4].split(":")[1].strip().split(",")]
        self.ptr = 0
        self.dict = {0:self.adv, 1:self.bxl, 2:self.bst, 3:self.jnz, 4:self.bxc, 5:self.out, 6:self.bdv, 7:self.cdv}

    def combo(self, R, operand):
        if operand <= 3:
            return operand
        elif 3 < operand < 7:
            return R[operand - 4]
        else:
            raise ValueError(f"Invalid operand {operand}")
            
    def adv (self, R, operand, ptr, output):
        operand = self.combo(R, operand)
        R[0] = R[0] // (2 ** operand)
        return ptr + 2
    def bxl (self, R, operand, ptr, output):
        R[1] = R[1] ^ operand
        return ptr + 2
    def bst (self, R, operand, ptr, output):
        operand = self.combo(R, operand)
        R[1] = operand % 8
        return ptr + 2
    def jnz (self, R, operand, ptr, output):
        if R[0] != 0:
            return operand
        return ptr + 2
    def bxc (self, R, operand, ptr, output):
        R[1] = R[1] ^ R[2]
        return ptr + 2
    def out (self, R, operand, ptr, output):
        operand = self.combo(R, operand)
        output.append(operand % 8)
        return ptr + 2
    def bdv (self, R, operand, ptr, output):
        operand = self.combo(R, operand)
        R[1] = R[0] // (2 ** operand)
        return ptr + 2
    def cdv (self, R, operand, ptr, output):
        operand = self.combo(R, operand)
        R[2] = R[0] // (2 ** operand)
        return ptr + 2
    
    def run(self, R, prog):
        output = []
        ptr = 0
        while ptr < len(self.prog):
            opcode = self.prog[ptr]
            operand = self.prog[ptr + 1]
            ptr = self.dict[opcode](R, operand, ptr, output)
        return (output)
            
    def first_problem(self):
        output = self.run(self.R.copy(), self.prog)
        return ",".join(str(x) for x in output)

    def second_problem(self):
        def match_length(a1, a2):
            a1r = a1[::-1]
            a2r = a2[::-1]
            m = 0
            for a in a1r:
                if a == a2r[m]:
                    m += 1
                    continue
                else:
                    break
            return (m)
        
        def search_range(start, end, step):
            max_match = 0
            max_match_i = 0
            max_match_output = []
            for i in range (start, end, step):
                R = {0:i, 1:0, 2:0}
                output = self.run(R, self.prog)
                current_match_len = match_length(output, self.prog)
                if current_match_len > max_match:
                    max_match = current_match_len
                    max_match_i = i
                    max_match_output = output
                    print (i, match_length(output, self.prog), output, self.prog)
            return max_match_i, max_match_output
    
        i = 1
        while i < 64:
            R = {0:2 ** i, 1:0, 2:0}
            output = self.run(R, self.prog)
            if len(output) == len(self.prog):
                i -= 1
                break
            i += 1

        istart = i
        while i < 64:
            R = {0:2 ** i, 1:0, 2:0}
            output = self.run(R, self.prog)
            if len(output) > len(self.prog):
                break
            i += 1
        iend = i
        print (istart, iend)

        start = 2 ** istart
        end = 2 ** iend
        step = (end - start) // 10000
        if step == 0:
            step = 1
        i, output = search_range(start, end, step)
        while output != self.prog:
            start = i - step
            end = i + step
            step = (end - start) // 10000
            if step == 0:
                step = 1
            i, output = search_range(start, end, step)
        print (i, output)
        return i
             
def process(request, year, day):
    solver = DayXSolver(request, year, day)
    return (solver.process())