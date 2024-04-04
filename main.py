import enum
import re
import sys
from dataclasses import dataclass
from typing import Any
from collections import deque


# Functions
def jumpc(name_step: str):
    validate = stack.pop()
    if validate == 1:
        jumps.append(name_step)


def addsp(value: str):
    value = int(value)
    if value > 0:
        for _ in range(int(value)):
            stack.append(0)
    else:
        for _ in range(abs(int(value))):
            stack.pop()

def storeabs(value: str):
    stack[int(value)] = stack.pop()


def pushabs(value: str):
    stack.append(stack[int(value)])


def sub():
    stack.append(stack.pop() - stack.pop())


def less():
    stack.append(int(stack.pop() > stack.pop()))

def pushimm(value: str):
    stack.append(int(value))


def times():
    stack.append(stack.pop() * stack.pop())


def add():
    stack.append(stack.pop() + stack.pop())


def stop():
    print("Program compiled well")
    if len(stack) == 1:
        print(f"Result: {stack[-1]}")
    else:
        print("Error in the program")
        print("Finished STACK: ", stack)

def div():
    stack.append(stack.pop() // stack.pop())
    
def mod():
    stack.append(stack.pop() % stack.pop())

def lshift():
    stack.append(stack.pop() << stack.pop())

def lshiftind():
    shift_amount = stack.pop()
    address = stack.pop()
    value = stack.pop()
    stack[address << shift_amount] = value

def rshift():
    stack.append(stack.pop() >> stack.pop())

def rshiftind():
    shift_amount = stack.pop()
    address = stack.pop()
    value = stack.pop()
    stack[address >> shift_amount] = value
    
def logical_and():
    stack.append(stack.pop() & stack.pop())

def logical_or():
    stack.append(stack.pop() | stack.pop())

def logical_nor():
    stack.append(~(stack.pop() | stack.pop()))

def logical_nand():
    stack.append(~(stack.pop() & stack.pop()))

def logical_xor():
    stack.append(stack.pop() ^ stack.pop())

def logical_not():
    stack.append(~stack.pop() & 0xFFFF)
    
def f_to_i():
    stack.append(int(stack.pop()))

def f_to_ir():
    stack.append(round(stack.pop()))

def i_to_f():
    stack.append(float(stack.pop()))

def pushimm_f(value: str):
    stack.append(float(value))

def pushimm_ch(value: str):
    stack.append(ord(value[0]))

def pushimm_ma(value: str):
    stack.append(int(value, 16))

def pushimm_pa(value: str):
    stack.append(int(value))

def pushimm_str(value: str):
    for char in reversed(value):
        stack.append(ord(char))
        
def push_sp():
    stack.append(len(stack))

def push_fbr():
    stack.append(0) 

def pop_sp():
    if stack:
        stack.pop()

def pop_fbr():
    pass

def dup():
    if stack:
        value = stack[-1]
        stack.append(value)

def swap():
    if len(stack) >= 2:
        stack[-1], stack[-2] = stack[-2], stack[-1]
        
def malloc():
    pass

def free():
    stack.clear()
    
def push_ind():
    if stack:
        address = stack.pop()
        if address < len(stack):
            stack.append(stack[address])
        else:
            print("Error: Attempted to access out-of-bounds memory")

def store_ind():
    if len(stack) >= 2:
        value = stack.pop()
        address = stack.pop()
        if address < len(stack):
            stack[address] = value
        else:
            print("Error: Attempted to access out-of-bounds memory")

def push_off():
    if stack:
        offset = stack.pop()
        if len(stack) > offset >= 0:
            stack.append(stack[-1 - offset])
        else:
            print("Error: Attempted to access out-of-bounds memory")

def store_off():
    if len(stack) >= 2:
        value = stack.pop()
        offset = stack.pop()
        if len(stack) > offset >= 0:
            stack[-1 - offset] = value
        else:
            print("Error: Attempted to access out-of-bounds memory")

# Constants
class Function(enum.StrEnum):
    ADDSP = "ADDSP"
    JUMPC = "JUMPC"
    PUSHABS = "PUSHABS"
    LESS = "LESS"
    STOREABS = "STOREABS"
    PUSHIMM = "PUSHIMM"
    TIMES = "TIMES"
    ADD = "ADD"
    STOP = "STOP"
    SUB = "SUB"
    DIV = "DIV"
    MOD = "MOD"
    LSHIFT = "LSHIFT"
    LSHIFTIND = "LSHIFTIND"
    RSHIFT = "RSHIFT"
    RSHIFTIND = "RSHIFTIND"
    AND = "AND"
    OR = "OR"
    NOR = "NOR"
    NAND = "NAND"
    XOR = "XOR"
    NOT = "NOT"
    FTOI = "FTOI"
    FTOIR = "FTOIR"
    ITOF = "ITOF"
    PUSHIMMF = "PUSHIMMF"
    PUSHIMMCH = "PUSHIMMCH"
    PUSHIMMMA = "PUSHIMMMA"
    PUSHIMMPA = "PUSHIMMPA"
    PUSHIMMSTR = "PUSHIMMSTR"
    PUSHSP = "PUSHSP"
    PUSHFBR = "PUSHFBR"
    POPSP = "POPSP"
    POPFBR = "POPFBR"
    DUP = "DUP"
    SWAP = "SWAP"
    MALLOC = "MALLOC"
    FREE = "FREE"
    PUSHIND = "PUSHIND"
    STOREIND = "STOREIND"
    PUSHOFF = "PUSHOFF"
    STOREOFF = "STOREOFF"


mappings_functions = {
    Function.PUSHIMM: pushimm,
    Function.TIMES: times,
    Function.ADD: add,
    Function.STOP: stop,
    Function.SUB: sub,
    Function.ADDSP: addsp,
    Function.STOREABS: storeabs,
    Function.PUSHABS: pushabs,
    Function.LESS: less,
    Function.JUMPC: jumpc,
    Function.DIV: div,
    Function.MOD: mod,
    Function.LSHIFT: lshift,
    Function.LSHIFTIND: lshiftind,
    Function.RSHIFT: rshift,
    Function.RSHIFTIND: rshiftind,
    Function.AND: logical_and,
    Function.OR: logical_or,
    Function.NOR: logical_nor,
    Function.NAND: logical_nand,
    Function.XOR: logical_xor,
    Function.NOT: logical_not,
    Function.FTOI: f_to_i,
    Function.FTOIR: f_to_ir,
    Function.ITOF: i_to_f,
    Function.PUSHIMMF: pushimm_f,
    Function.PUSHIMMCH: pushimm_ch,
    Function.PUSHIMMMA: pushimm_ma,
    Function.PUSHIMMPA: pushimm_pa,
    Function.PUSHIMMSTR: pushimm_str,
    Function.PUSHSP: push_sp,
    Function.PUSHFBR: push_fbr,
    Function.POPSP: pop_sp,
    Function.POPFBR: pop_fbr,
    Function.DUP: dup,
    Function.SWAP: swap,
    Function.MALLOC: malloc,
    Function.FREE: free,
    Function.PUSHIND: push_ind,
    Function.STOREIND: store_ind,
    Function.PUSHOFF: push_off,
    Function.STOREOFF: store_off,
}


@dataclass
class Instruction:
    function: callable
    args: list[Any]


@dataclass
class JumpConstant:
    name: str


def separate_tokens(line_code: str) -> Instruction | JumpConstant:
    separated_tokens = line_code.split(" ")
    if re.compile(r"[a-zA-Z]+:").match(separated_tokens[0].strip()):
        return JumpConstant(separated_tokens[0].strip().replace(":", ""))
    type_function = Function(separated_tokens[0].strip())
    instruction = Instruction(
        function=mappings_functions[type_function],
        args=[arg.strip() for arg in separated_tokens[1:]]
    )
    return instruction


def build_stack(instruction: list[Instruction | JumpConstant]) -> None:
    for instr in instruction:
        if len(jumps) == 0:
            instr.function(*instr.args)
        else:
            if isinstance(instr, JumpConstant) and instr.name == jumps[-1]:
                jumps.pop()


def main():
    if len(sys.argv) < 2:
        print("Pass the name of the file to compile")
        raise SystemExit(1)
    file_path = sys.argv[1]
    tokens = []
    try:
        with open(file_path, "r") as file:
            for line_code in file.readlines():
                if line_code.startswith("//") or line_code.startswith("\n"):
                    continue
                tokens.append(separate_tokens(line_code))
        build_stack(tokens)
    except FileNotFoundError:
        print(f"File {file_path} not found")
        raise SystemExit(1)


if __name__ == "__main__":
    stack = deque()
    jumps = deque()
    main()
