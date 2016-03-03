# Convert MIPS assembly to binary instruction
import re
from bitstring import BitArray
import mips_table

OPCODE = 0
FUNCTION_CODE = 1
INSTRUCTION_TYPE = 2

def assemble(instruction):
    regex_instr = re.compile("(\w{1,5})").match(instruction)
    instruction_name = regex_instr.group(1)
    instr_info = mips_table.instruction[instruction_name]

    bin_inst = BitArray('0x00000000')
    bin_inst = assembler_dispatch[instr_info[INSTRUCTION_TYPE]](bin_inst, instr_info, instruction)
    return bin_inst

def assembler_r_type(bin_inst, instr_info, instruction):
    tokens = re.compile("^\s*\w{1,5}\s*\$([3][0-1]|[1-2]\d|\d),\s*\$([3][0-1]|[1-2]\d|\d),\s*\$([3][0-1]|[1-2]\d|\d)").match(instruction)
    rd = tokens.group(1)
    rs = tokens.group(2)
    rt = tokens.group(3)
    bin_inst[0:6] = instr_info[OPCODE]
    bin_inst[6:11] = int(rs)
    bin_inst[11:16] = int(rt)
    bin_inst[16:21] = int(rd)
    bin_inst[21:26] = 0x00
    bin_inst[26:32] = instr_info[FUNCTION_CODE]
    return bin_inst

def assembler_i_type(bin_inst, instr_info, instruction):
    tokens = re.compile("^\s*\w{1,5}\s*\$([3][0-1]|[1-2]\d|\d),\s*\$([3][0-1]|[1-2]\d|\d),\s*(3[0-2][0-7][0-6][0-7]|-3[0-2][0-7][0-6][0-8]|-?1\d{4}|-?2\d{4}|-?\d{1,4})\s*$").match(instruction)
    rt = tokens.group(1)
    rs = tokens.group(2)
    imval = tokens.group(3)
    bin_inst[0:6] = instr_info[OPCODE]
    bin_inst[6:11] = int(rs)
    bin_inst[11:16] = int(rt)
    bin_inst[16:32] = int(imval)
    return bin_inst

def assembler_j_type(bin_inst, instr_info, instruction):
    tokens = re.compile("^\s*\w{1,5}\s*(0x0[\dA-Fa-f]{6}[048Cc])\s*$").match(instruction)
    target_address = tokens.group(1)
    bin_inst[0:6] = instr_info[OPCODE]
    bin_inst[6:32] = BitArray(target_address)[4:30]
    return bin_inst

def assembler_mem_type(bin_inst, instr_info, instruction):
    tokens = re.compile("^\s*\w{1,5}\s*\$([3][0-1]|[1-2]\d|\d),\s*(3[0-2][0-7][0-6][0-7]|-3[0-2][0-7][0-6][0-8]|-?1\d{4}|-?2\d{4}|-?\d{1,4})\s*\(\s*\$([3][0-1]|[1-2]\d|\d)\s*\)\s*$").match(instruction)
    rt = tokens.group(1)
    offset = tokens.group(2)
    rs = tokens.group(3)
    bin_inst[0:6] = instr_info[OPCODE]
    bin_inst[6:11] = int(rs)
    bin_inst[11:16] = int(rt)
    bin_inst[16:32] = int(offset)
    return bin_inst

def assembler_b_type(bin_inst, instr_info, instruction):
    tokens = re.compile("^\s*\w{1,5}\s*\$([3][0-1]|[1-2]\d|\d),\s*\$([3][0-1]|[1-2]\d|\d),\s*(3[0-2][0-7][0-6][0-7]|-3[0-2][0-7][0-6][0-8]|-?1\d{4}|-?2\d{4}|-?\d{1,4})\s*$").match(instruction)
    rs = tokens.group(1)
    rt = tokens.group(2)
    offset = tokens.group(3)
    bin_inst[0:6] = instr_info[OPCODE]
    bin_inst[6:11] = int(rs)
    bin_inst[11:16] = int(rt)
    bin_inst[16:32] = int(offset)
    return bin_inst

def assembler_md_type(bin_inst, instr_info, instruction):
    tokens = re.compile("^\s*\w{1,5}\s*\$([3][0-1]|[1-2]\d|\d),\s*\$([3][0-1]|[1-2]\d|\d)\s*$").match(instruction)
    rs = tokens.group(1)
    rt = tokens.group(2)
    bin_inst[0:6] = instr_info[OPCODE]
    bin_inst[6:11] = int(rs)
    bin_inst[11:16] = int(rt)
    bin_inst[16:21] = 0x00
    bin_inst[21:26] = 0x00
    bin_inst[26:32] = instr_info[FUNCTION_CODE]
    return bin_inst

def assembler_mf_type(bin_inst, instr_info, instruction):
    tokens = re.compile("^\s*\w{1,5}\s*\$([3][0-1]|[1-2]\d|\d)\s*$").match(instruction)
    rd = tokens.group(1)
    bin_inst[0:6] = instr_info[OPCODE]
    bin_inst[6:11] = 0x00
    bin_inst[11:16] = 0x00
    bin_inst[16:21] = int(rd)
    bin_inst[21:26] = 0x00
    bin_inst[26:32] = instr_info[FUNCTION_CODE]
    return bin_inst

assembler_dispatch = {
    'R': assembler_r_type,
    'I': assembler_i_type,
    'J': assembler_j_type,
    'MEM' : assembler_mem_type,
    'B': assembler_b_type,
    'MD' : assembler_md_type,
    'MF' : assembler_mf_type
    # 'JR' : assembler_jr_type,
    # 'SH' : assembler_sh_type,
    # 'SP' : assembler_sp_type,
    # 'L' : assembler_l_type
}

# instr_bin = assemble(input("Enter MIPS instruction:"))
with open('instructions.txt', 'r') as infile:
    for line in infile:
        print assemble(line)
infile.close()
