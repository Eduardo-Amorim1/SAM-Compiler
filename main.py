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
    print("Program compile well")
    if len(stack) == 1:
        print(f"Result: {stack[-1]}")
    else:
        print("Error in the program")
        print("Finished STACK: ", stack)


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
    SUB = "SUB"
    STOP = "STOP"


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
    Function.JUMPC: jumpc
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
