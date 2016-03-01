# Convert MIPS assembly to binary instruction
import re
from bitstring import BitArray
import mips_table

OPCODE = 0
SHIFT_AMT = 4
FUNCTION_CODE = 5

def assemble(instruction):
    pattern_rtype = "(\w{2,3})\s*\$([3][0-1]|[1-2]\d|\d),\s*\$([3][0-1]|[1-2]\d|\d),\s*\$([3][0-1]|[1-2]\d|\d)"
    prog   = re.compile(pattern_rtype)
    result = prog.match(instruction)
    instruction_name = result.group(1)
    r0 = result.group(2)
    r1 = result.group(3)
    r2 = result.group(4)

    instr_info = mips_table.instruction_info[instruction_name];
    print instr_info

    bin_inst = BitArray('0x00000000')
    bin_inst[0:6] = instr_info[OPCODE]
    bin_inst[6:11] = int(r1)
    bin_inst[11:16] = int(r2)
    bin_inst[16:21] = int(r0)
    bin_inst[21:26] = instr_info[SHIFT_AMT]
    bin_inst[26:32] = instr_info[FUNCTION_CODE]
    print bin_inst
    return bin_inst
instr_bin = assemble(input("Enter MIPS instruction:"))
print instr_bin
