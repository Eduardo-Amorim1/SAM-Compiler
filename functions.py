# Functions
from collections import deque


class Functions:
    def __init__(self):
        self.stack = deque()
        self.jumps = deque()

    def jumpc(self, name_step: str):
        validate = self.stack.pop()
        if validate == 1:
            self.jumps.append(name_step)

    def jump(self, name_step: str):
        self.jumps.append(name_step)

    def addsp(self, value: str):
        value = int(value)
        if value > 0:
            for _ in range(int(value)):
                self.stack.append(0)
        else:
            for _ in range(abs(int(value))):
                self.stack.pop()

    def storeabs(self, value: str):
        self.stack[int(value)] = self.stack.pop()

    def pushabs(self, value: str):
        self.stack.append(self.stack[int(value)])

    def sub(self):
        self.stack.append(self.stack.pop() - self.stack.pop())

    def less(self):
        self.stack.append(int(self.stack.pop() > self.stack.pop()))

    def pushimm(self, value: str):
        self.stack.append(int(value))

    def times(self):
        self.stack.append(self.stack.pop() * self.stack.pop())

    def add(self):
        self.stack.append(self.stack.pop() + self.stack.pop())

    def stop(self):
        if len(self.stack) == 1:
            print(f"Result: {self.stack[-1]}")
        elif len(self.stack) > 1:
            print(f"Result: {self.stack[-1]}")
            print("Warning: There are more than one value in the stack")
        else:
            print("Error in the program")
            print("Finished self.stack: ", self.stack)

    def div(self):
        self.stack.append(self.stack.pop() // self.stack.pop())

    def mod(self):
        self.stack.append(self.stack.pop() % self.stack.pop())

    def lshift(self):
        self.stack.append(self.stack.pop() << self.stack.pop())

    def lshiftind(self):
        shift_amount = self.stack.pop()
        address = self.stack.pop()
        value = self.stack.pop()
        self.stack[address << shift_amount] = value

    def rshift(self):
        self.stack.append(self.stack.pop() >> self.stack.pop())

    def rshiftind(self):
        shift_amount = self.stack.pop()
        address = self.stack.pop()
        value = self.stack.pop()
        self.stack[address >> shift_amount] = value

    def logical_and(self):
        self.stack.append(self.stack.pop() & self.stack.pop())

    def logical_or(self):
        self.stack.append(self.stack.pop() | self.stack.pop())

    def logical_nor(self):
        self.stack.append(~(self.stack.pop() | self.stack.pop()))

    def logical_nand(self):
        self.stack.append(~(self.stack.pop() & self.stack.pop()))

    def logical_xor(self):
        self.stack.append(self.stack.pop() ^ self.stack.pop())

    def logical_not(self):
        self.stack.append(~self.stack.pop() & 0xFFFF)

    def f_to_i(self):
        self.stack.append(int(self.stack.pop()))

    def f_to_ir(self):
        self.stack.append(round(self.stack.pop()))

    def i_to_f(self):
        self.stack.append(float(self.stack.pop()))

    def pushimm_f(self, value: str):
        self.stack.append(float(value))

    def pushimm_ch(self, value: str):
        self.stack.append(ord(value[0]))

    def pushimm_ma(self, value: str):
        self.stack.append(int(value, 16))

    def pushimm_pa(self, value: str):
        self.stack.append(int(value))

    def pushimm_str(self, value: str):
        for char in reversed(value):
            self.stack.append(ord(char))

    def push_sp(self):
        self.stack.append(len(self.stack))

    def push_fbr(self):
        self.stack.append(0)

    def pop_sp(self):
        if self.stack:
            self.stack.pop()

    def pop_fbr(self):
        pass

    def dup(self):
        if self.stack:
            value = self.stack[-1]
            self.stack.append(value)

    def swap(self):
        if len(self.stack) >= 2:
            self.stack[-1], self.stack[-2] = self.stack[-2], self.stack[-1]

    def link(self):
        self.stack.append(len(self.stack))

    def malloc(self):
        pass

    def free(self):
        self.stack.clear()

    def push_ind(self):
        if self.stack:
            address = self.stack.pop()
            if address < len(self.stack):
                self.stack.append(self.stack[address])
            else:
                print("Error: Attempted to access out-of-bounds memory")

    def store_ind(self):
        if len(self.stack) >= 2:
            value = self.stack.pop()
            address = self.stack.pop()
            if address < len(self.stack):
                self.stack[address] = value
            else:
                print("Error: Attempted to access out-of-bounds memory")

    def push_off(self):
        if self.stack:
            offset = self.stack.pop()
            if len(self.stack) > offset >= 0:
                self.stack.append(self.stack[-1 - offset])
            else:
                print("Error: Attempted to access out-of-bounds memory")

    def store_off(self):
        if len(self.stack) >= 2:
            value = self.stack.pop()
            offset = self.stack.pop()
            if len(self.stack) > offset >= 0:
                self.stack[-1 - offset] = value
            else:
                print("Error: Attempted to access out-of-bounds memory")

    def greater(self):
        self.stack.append(int(self.stack.pop() < self.stack.pop()))

    def isnil(self):
        if self.stack.pop() == 0:
            self.stack.append(1)
        else:
            self.stack.append(0)

