from Solver import Solver
import collections

class DataBlock:
    def __init__(self, id, pos, size):
        self.id = id
        self.pos = pos
        self.size = size

class DayXSolver(Solver):
    def __init__(self, request, year, day, input=None):
        super().__init__(request, year, day, input)
        self.input[0] = self.input[0].strip()
        self.data = []
        c_pos = 0
        for i, c in enumerate(self.input[0]):
            if i % 2 == 0: # data
                id = (i // 2)
                self.data.append(DataBlock(id, c_pos, int(c))) # id, start, size
            c_pos += int(c)
        self.size = c_pos

    def find_first_free_block(self, data, start, min_size=1):
        if start >= len(data):
            return (data[-1].id, data[-1].pos + data[-1].size, self.size - data[-1].pos - data[-1].size)
        next_block_pos = data[start].pos + data[start].size
        next_block_index = start + 1
        while next_block_index < len(data) and next_block_pos + min_size > data[next_block_index].pos:
            next_block_pos = data[next_block_index].pos + data[next_block_index].size
            next_block_index += 1
        if next_block_index == len(data):
            size = self.size - next_block_pos
        else:
            size = data[next_block_index].pos - next_block_pos
        return (next_block_index - 1, next_block_pos, size) # index, pos, size

    def checksum(self, data):
        result = 0
        i = 0
        for block in data:
            for j in range(block.size):
                result += block.id * (block.pos + j)
                i += 1
        return result

    def first_problem(self):
        data = self.data.copy()
        next_free_block = self.find_first_free_block(data, 0)
        while next_free_block[0] < len(data) - 1:
            last_block = data.pop()
            if last_block.size <= next_free_block[2]:
                data.insert(next_free_block[0] + 1, DataBlock(last_block.id, next_free_block[1], last_block.size))
                next_free_block = self.find_first_free_block(data, next_free_block[0] + 1)
            else:
                part1 = DataBlock(last_block.id, next_free_block[1], next_free_block[2])
                part2 = DataBlock(last_block.id, last_block.pos, last_block.size - next_free_block[2])
                data.insert(next_free_block[0] + 1, part1)
                data.append(part2)
                next_free_block = self.find_first_free_block(data, next_free_block[0] + 1)
        return self.checksum(data)
            
    def second_problem(self):
        data = self.data.copy()
        move_candidate_index = len(data) - 1
        while move_candidate_index > 0:
            next_free_block = self.find_first_free_block(data, 0, data[move_candidate_index].size)
            if next_free_block[0] >= move_candidate_index:
                move_candidate_index -= 1
                continue
            block_to_move = data.pop(move_candidate_index)
            data.insert(next_free_block[0] + 1, DataBlock(block_to_move.id, next_free_block[1], block_to_move.size))
        return self.checksum(data)
            
def process(request, year, day):
    solver = DayXSolver(request, year, day)
    return (solver.process())