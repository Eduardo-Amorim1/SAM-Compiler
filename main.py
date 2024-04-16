import os
from pathlib import Path

from interpreter import Interpreter


def teste_all_files():
    path = os.path.join(Path(__file__).parent, "sams_code")
    for all_files in os.walk(path):
        files = all_files[2]
        for file in files:
            try:
                # if file == "exercise.sam":
                print(f"File: {file}")
                print("LOGS:")
                interpreter = Interpreter()
                interpreter.read_file(os.path.join(path, file))

                print("\n" + "-" * 50 + "\n")
            except Exception as error:
                print(error)


if __name__ == "__main__":
    teste_all_files()
    # interpreter = Interpreter()
    # interpreter.read_file()
