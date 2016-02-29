# Convert MIPS assembly to binary instruction
import re
from bitstring import BitArray
import mips_table

def assemble(instruction):
    pattern_rtype = "(\w{2,3})\s*\$([3][0-1]|[1-2]\d|\d),\s*\$([3][0-1]|[1-2]\d|\d),\s*\$([3][0-1]|[1-2]\d|\d)"
    prog   = re.compile(pattern_rtype)
    result = prog.match(instruction)
    r_instruction = result.group(1)
    r1 = result.group(2)
    r2 = result.group(3)
    r3 = result.group(4)

    function_code = mips_table.function_codes[r_instruction];
    opcode = '0b000000';
    bin_inst = BitArray('0x00000000')
    bin_inst[0:6] = opcode
    bin_inst[6:11] = int(r2)
    bin_inst[11:16] = int(r3)
    bin_inst[16:21] = int(r1)
    bin_inst[21:26] = 0
    bin_inst[26:32] = function_code
    # .append(int(r2)).append(int(r3)).append(int(r1)).append('0b100000')
    print bin_inst

assemble("add $3, $2, $10")
