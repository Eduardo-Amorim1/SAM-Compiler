import os
from pathlib import Path

from stackmachine import StackMachine

def teste_all_files():
    path = os.path.join(Path(__file__).parent, "sams_code")
    for all_files in os.walk(path):
        files = all_files[2]
        for file in files:
            try:
                print(f"File: {file}")
                print("LOGS:")
                interpreter = StackMachine()
                interpreter.read_file(os.path.join(path, file))
                print("\n" + "-" * 50 + "\n")
            except Exception as error:
                print(error)
                
def one_file(file):
    try:
        print(f"File: {file}")
        print("LOGS:")
        interpreter = StackMachine()
        interpreter.read_file(file)
        print("\n" + "-" * 50 + "\n")
    except Exception as error:
        print(error)


if __name__ == "__main__":
    #teste_all_files()
    one_file("E:\\Faculdade\\Compiladores\\SAM-Compiler\\sams_code\\sam4_5.sam")
