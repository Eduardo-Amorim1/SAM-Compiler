from constants import ConstantFunctionsName


def is_int(value: str) -> tuple[bool, str]:
    try:
        int(value)
        return False, ''
    except ValueError:
        return True, "The value is not an integer"


def is_positive_int(value: str) -> tuple[bool, str]:
    try:
        if int(value) >= 0:
            return False, ''
        return True, "The value is not a positive integer"
    except ValueError:
        return True, "The value is not an integer"


def cn_args(args: list[str], number_args: int) -> tuple[bool, str]:
    if len(args) == number_args:
        return False, ''
    return True, f"The number of arguments is not correct, expected {number_args} arguments"


class ValidateArguments:

    def __init__(self):
        ...

    @property
    def val_functions(self) -> dict:
        return {
            ConstantFunctionsName.JUMPC: self.val_jumpc,
            ConstantFunctionsName.ADDSP: self.val_int_value,
            ConstantFunctionsName.STOREABS: self.val_positive_int_value,
            ConstantFunctionsName.PUSHABS: self.val_positive_int_value,
            ConstantFunctionsName.PUSHIMM: self.val_int_value,
            # add other validations ...
        }

    @property
    def validate_keys(self) -> set:
        return set(self.val_functions.keys())

    @staticmethod
    def val_jumpc(arguments: list[str]):
        error, msg = cn_args(arguments, 1)
        if error:
            raise ValueError(msg)

    @staticmethod
    def val_int_value(arguments: list[str]):
        error, msg = cn_args(arguments, 1)
        if error:
            raise ValueError(msg)
        error, msg = is_int(arguments[0])
        if error:
            raise ValueError(msg)

    @staticmethod
    def val_positive_int_value(arguments: list[str]):
        error, msg = cn_args(arguments, 1)
        if error:
            raise ValueError(msg)
        error, msg = is_positive_int(arguments[0])
        if error:
            raise ValueError(msg)

    def validate_arguments(self, name_function, arguments: list[str]):
        self.val_functions[name_function](arguments)

