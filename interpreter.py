import re
import sys

from constants import MappingConstants, ConstantFunctionsName
from functions import Functions
from schema import JumpConstant, Instruction, BuilderInstructions


class Interpreter:

    def __init__(self):
        self.functions = Functions()
        self.builderInstructions = BuilderInstructions()
        self.instructions = []
        self.mapping_functions = MappingConstants(self.functions).mapping_functions

    def strip_tokens(self, line_code: str, count_line: int) -> Instruction | JumpConstant:
        try:
            separated_tokens = line_code.split(" ")
            clean_tokens = []
            for index, token in enumerate(separated_tokens):
                original_token = token
                token = re.sub(r'[\t\n]|//.*$', '', token, flags=re.MULTILINE)
                if "//" in token or original_token.startswith("//"):
                    break
                if not token:
                    continue
                clean_tokens.append(token)
                if "//" in original_token:
                    break
            if re.compile(r"[a-zA-Z]+:").match(clean_tokens[0].strip()):
                return JumpConstant(clean_tokens[0].strip().replace(":", ""))
            type_function = ConstantFunctionsName(clean_tokens[0].strip())
            instruction = self.builderInstructions.build_instruction(
                function=self.mapping_functions[type_function],
                args=[arg.strip() for arg in clean_tokens[1:]],
                name=type_function,
                count_line=count_line+1
            )
            return instruction
        except Exception as error:
            print(error)

    def build_stack(self, instruction: list[Instruction | JumpConstant]) -> None:
        for instr in instruction:
            try:
                if len(self.functions.jumps) == 0 and not isinstance(instr, JumpConstant):
                    instr.function(*instr.args)
                else:
                    if len(self.functions.jumps) > 0 and instr.name == self.functions.jumps[-1]:
                        self.functions.jumps.pop()
            except Exception as error:
                print(error)

    def read_file(self, file_path):
        # if len(sys.argv) < 2:
        #     print("Pass the name of the file to compile")
        #     raise SystemExit(1)
        # file_path = sys.argv[1]
        tokens = []
        try:
            with open(file_path, "r") as file:
                count_line = -1
                for line_code in file.readlines():
                    count_line += 1
                    if line_code.startswith("//") or line_code.startswith("\n"):
                        continue
                    if "//" in line_code:
                        line_code = line_code.replace("//", "#")
                        if regex := re.search(r"#s*.*", line_code):
                            line_code = line_code[:regex.start()]
                            line_code = line_code.strip()
                    if not line_code:
                        continue
                    tokens.append(self.strip_tokens(line_code, count_line))
            self.build_stack(tokens)
            print("Program finish!")
        except FileNotFoundError:
            print(f"File {file_path} not found")
            raise SystemExit(1)
