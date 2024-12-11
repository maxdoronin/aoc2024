from Solver import Solver

class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None
    
    def __str__(self):
        res = ""
        current = self
        while current != None:
            res += f"{current.value} -> "
            current = current.next
        return res

class DayXSolver(Solver):
    def __init__(self, request, year, day, input=None):
        super().__init__(request, year, day, input)
        self.length = 0
        self.head = ListNode(-1)
        current = self.head
        for x in self.input[0].split(" "):
            current.next = ListNode(int(x))
            current = current.next
            self.length += 1
        
        self.data = {}
        for x in self.input[0].split(" "):
            self.data[int(x)] = self.data.get(int(x), 0) + 1

    
    def first_problem(self):
        for i in range(25):
            current = self.head.next
            while current != None:
                value_s = str(current.value)
                if current.value == 0:
                    current.value = 1
                elif current.value > 0 and len(value_s) % 2 == 0:
                    self.length += 1
                    value1 = int(value_s[0:len(value_s)//2])
                    value2 = int(value_s[len(value_s)//2:])
                    current.value = value1
                    new_node = ListNode(value2)
                    new_node.next = current.next
                    current.next = new_node
                    current = current.next
                else:
                    current.value = current.value * 2024
                current = current.next
        return self.length
            
    def second_problem(self):
        for i in range(75):
            new_data = {}
            for key, value in self.data.items():
                key_s = str(key)
                if key == 0:
                    new_key = 1
                    new_data[new_key] = new_data.get(new_key, 0) + value
                elif len(key_s) % 2 == 0:
                    new_key1 = int(key_s[0:len(key_s)//2])
                    new_key2 = int(key_s[len(key_s)//2:])
                    new_data[new_key1] = new_data.get(new_key1, 0) + value
                    new_data[new_key2] = new_data.get(new_key2, 0) + value
                else:
                    new_key = key * 2024
                    new_data[new_key] = new_data.get(new_key, 0) + value
            self.data = new_data

        return sum(self.data.values())
            
            
def process(request, year, day):
    solver = DayXSolver(request, year, day)
    return (solver.process())