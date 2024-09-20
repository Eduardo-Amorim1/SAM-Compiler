import os
from pathlib import Path

from stackmachine import StackMachine

def teste_all_files():
    path = os.path.join(Path(__file__).parent, "sams_code")
    for all_files in os.walk(path):
        files = all_files[2]
        for file in files:
            try:
                # print(f"File: {file}")
                # print("LOGS:")
                interpreter = StackMachine()
                interpreter.read_file(os.path.join(path, file))
                # print("\n" + "-" * 50 + "\n")
            except Exception as error:
                print(error)
                
def sam_compiler(file):
    try:
        interpreter = StackMachine()
        result, memory = interpreter.read_file(file)
        return result, memory
    except Exception as error:
        print(error)

def testes(file):
    try:
        print(f"File: {file}")
        print("LOGS:")
        interpreter = StackMachine()
        result, memory = interpreter.read_file(file)
        print("Result: ", result)
        print("Memory: ", memory)
        print("\n" + "-" * 50 + "\n")
    except Exception as error:
        print(error)

if __name__ == "__main__":
    #teste_all_files()
    testes("E:\Faculdade\Compiladores\sam_code.sam")
