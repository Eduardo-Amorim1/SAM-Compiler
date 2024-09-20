from dataclasses import dataclass
from typing import Any

from constants_sam import ConstantFunctionsName
from validate import ValidateArguments


@dataclass
class Instruction:
    function: callable
    name: ConstantFunctionsName
    args: list[Any]
    line: int


class BuilderInstructions:
    def __init__(self):
        self.validater = ValidateArguments()

    def build_instruction(self, function: callable, name: ConstantFunctionsName, args: list[str], count_line: int) -> Instruction:
        if name in self.validater.validate_keys:
            try:
                self.validater.validate_arguments(name, args)
            except ValueError as e:
                raise ValueError(f"ERROR - {e}\nInvalid argument: {args} - Instruction {name.value} - LINE: {count_line}")
        return Instruction(
            function=function,
            name=name,
            args=args,
            line=count_line
        )


@dataclass
class JumpConstant:
    name: str
