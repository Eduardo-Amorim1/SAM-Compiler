import enum
from functions import *

class ConstantFunctionsName(enum.StrEnum):
    ADDSP = "ADDSP"
    JUMPC = "JUMPC"
    JUMP = "JUMP"
    JSR = "JSR"
    JUMPIND = "JUMPIND"
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
    GREATER = "GREATER"
    ISNIL = "ISNIL"
    LINK = "LINK"
    ADDF = "ADDF"
    WRITE = "WRITE"
    WRITESTR = "WRITESTR"


class MappingConstants:
    def __init__(self, functions: Functions):
        self.functions = functions

    @property
    def mapping_functions(self):
        return {
            ConstantFunctionsName.PUSHIMM: self.functions.pushimm,
            ConstantFunctionsName.TIMES: self.functions.times,
            ConstantFunctionsName.ADD: self.functions.add,
            ConstantFunctionsName.STOP: self.functions.stop,
            ConstantFunctionsName.SUB: self.functions.sub,
            ConstantFunctionsName.ADDSP: self.functions.addsp,
            ConstantFunctionsName.STOREABS: self.functions.storeabs,
            ConstantFunctionsName.PUSHABS: self.functions.pushabs,
            ConstantFunctionsName.LESS: self.functions.less,
            ConstantFunctionsName.JUMPC: self.functions.jumpc,
            ConstantFunctionsName.JUMP: self.functions.jump,
            ConstantFunctionsName.JSR: self.functions.jsr,
            ConstantFunctionsName.JUMPIND: self.functions.jumpind,
            ConstantFunctionsName.DIV: self.functions.div,
            ConstantFunctionsName.MOD: self.functions.mod,
            ConstantFunctionsName.LSHIFT: self.functions.lshift,
            ConstantFunctionsName.LSHIFTIND: self.functions.lshiftind,
            ConstantFunctionsName.RSHIFT: self.functions.rshift,
            ConstantFunctionsName.RSHIFTIND: self.functions.rshiftind,
            ConstantFunctionsName.AND: self.functions.logical_and,
            ConstantFunctionsName.OR: self.functions.logical_or,
            ConstantFunctionsName.NOR: self.functions.logical_nor,
            ConstantFunctionsName.NAND: self.functions.logical_nand,
            ConstantFunctionsName.XOR: self.functions.logical_xor,
            ConstantFunctionsName.NOT: self.functions.logical_not,
            ConstantFunctionsName.FTOI: self.functions.f_to_i,
            ConstantFunctionsName.FTOIR: self.functions.f_to_ir,
            ConstantFunctionsName.ITOF: self.functions.i_to_f,
            ConstantFunctionsName.PUSHIMMF: self.functions.pushimm_f,
            ConstantFunctionsName.PUSHIMMCH: self.functions.pushimm_ch,
            ConstantFunctionsName.PUSHIMMMA: self.functions.pushimm_ma,
            ConstantFunctionsName.PUSHIMMPA: self.functions.pushimm_pa,
            ConstantFunctionsName.PUSHIMMSTR: self.functions.pushimm_str,
            ConstantFunctionsName.PUSHSP: self.functions.push_sp,
            ConstantFunctionsName.PUSHFBR: self.functions.push_fbr,
            ConstantFunctionsName.POPSP: self.functions.pop_sp,
            ConstantFunctionsName.POPFBR: self.functions.pop_fbr,
            ConstantFunctionsName.DUP: self.functions.dup,
            ConstantFunctionsName.SWAP: self.functions.swap,
            ConstantFunctionsName.MALLOC: self.functions.malloc,
            ConstantFunctionsName.FREE: self.functions.free,
            ConstantFunctionsName.PUSHIND: self.functions.push_ind,
            ConstantFunctionsName.STOREIND: self.functions.store_ind,
            ConstantFunctionsName.PUSHOFF: self.functions.push_off,
            ConstantFunctionsName.STOREOFF: self.functions.store_off,
            ConstantFunctionsName.GREATER: self.functions.greater,
            ConstantFunctionsName.ISNIL: self.functions.isnil,
            ConstantFunctionsName.LINK: self.functions.link,
            ConstantFunctionsName.ADDF: self.functions.addf,
            ConstantFunctionsName.WRITE: self.functions.write,
            ConstantFunctionsName.WRITESTR: self.functions.write_str
        }

