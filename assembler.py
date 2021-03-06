# Convert MIPS assembly to binary instruction
import re
import sys
from bitstring import BitArray
import mips_table

OPCODE = 0
FUNCTION_CODE = 1
INSTRUCTION_TYPE = 2

RE_INST_CAPTURE = "(\w{1,5})";
RE_INST = "\s*\w{1,5}\s*"
RE_REG = "\s*\$([3][0-1]|[1-2]\d|\d|zero|at|v[0-1]|a[0-3]|t[0-9]|s[0-7]|k[0-1]|gp|sp|fp|ra)\s*"
RE_IMVAL = "\s*(3[0-2][0-7][0-6][0-7]|-3[0-2][0-7][0-6][0-8]|-?1\d{4}|-?2\d{4}|-?\d{1,4})\s*"
RE_SHAMT = "\s*([3][0-1]|[1-2]\d|\d)\s*"
RE_ADDR = "\s*(0x0[\dA-Fa-f]{6}[048Cc])\s*"

def assemble(instruction):
    regex_instr = re.compile(RE_INST_CAPTURE).match(instruction)
    instruction_name = regex_instr.group(1)
    instr_info = mips_table.instruction[instruction_name]

    bin_inst = BitArray('0x00000000')
    bin_inst = assembler_dispatch[instr_info[INSTRUCTION_TYPE]](bin_inst, instr_info, instruction)
    return bin_inst

def assembler_r_type(bin_inst, instr_info, instruction):
    tokens = re.compile("^" + RE_INST + RE_REG + "," + RE_REG + "," + RE_REG + "$").match(instruction)
    rd = tokens.group(1)
    rs = tokens.group(2)
    rt = tokens.group(3)
    bin_inst[0:6] = instr_info[OPCODE]
    bin_inst[6:11] = mips_table.register_name[rs]
    bin_inst[11:16] = mips_table.register_name[rt]
    bin_inst[16:21] = mips_table.register_name[rd]
    bin_inst[21:26] = 0x00
    bin_inst[26:32] = instr_info[FUNCTION_CODE]
    return bin_inst

def assembler_i_type(bin_inst, instr_info, instruction):
    tokens = re.compile("^" + RE_INST + RE_REG + "," + RE_REG + "," + RE_IMVAL + "$").match(instruction)
    rt = tokens.group(1)
    rs = tokens.group(2)
    imval = tokens.group(3)
    bin_inst[0:6] = instr_info[OPCODE]
    bin_inst[6:11] = mips_table.register_name[rs]
    bin_inst[11:16] = mips_table.register_name[rt]
    bin_inst[16:32] = int(imval)
    return bin_inst

def assembler_j_type(bin_inst, instr_info, instruction):
    tokens = re.compile("^" + RE_INST + RE_ADDR + "$").match(instruction)
    target_address = tokens.group(1)
    bin_inst[0:6] = instr_info[OPCODE]
    bin_inst[6:32] = BitArray(target_address)[4:30]
    return bin_inst

def assembler_mem_type(bin_inst, instr_info, instruction):
    tokens = re.compile("^" + RE_INST + RE_REG + "," + RE_IMVAL + "\(" + RE_REG + "\)" + "\s*$").match(instruction)
    rt = tokens.group(1)
    offset = tokens.group(2)
    rs = tokens.group(3)
    bin_inst[0:6] = instr_info[OPCODE]
    bin_inst[6:11] = mips_table.register_name[rs]
    bin_inst[11:16] = mips_table.register_name[rt]
    bin_inst[16:32] = int(offset)
    return bin_inst

def assembler_b_type(bin_inst, instr_info, instruction):
    tokens = re.compile("^" + RE_INST + RE_REG + "," + RE_REG + "," + RE_IMVAL + "$").match(instruction)
    rs = tokens.group(1)
    rt = tokens.group(2)
    offset = tokens.group(3)
    bin_inst[0:6] = instr_info[OPCODE]
    bin_inst[6:11] = mips_table.register_name[rs]
    bin_inst[11:16] = mips_table.register_name[rt]
    bin_inst[16:32] = int(offset)
    return bin_inst

def assembler_md_type(bin_inst, instr_info, instruction):
    tokens = re.compile("^" + RE_INST + RE_REG + "," + RE_REG + "$").match(instruction)
    rs = tokens.group(1)
    rt = tokens.group(2)
    bin_inst[0:6] = instr_info[OPCODE]
    bin_inst[6:11] = mips_table.register_name[rs]
    bin_inst[11:16] = mips_table.register_name[rt]
    bin_inst[16:21] = 0x00
    bin_inst[21:26] = 0x00
    bin_inst[26:32] = instr_info[FUNCTION_CODE]
    return bin_inst

def assembler_mf_type(bin_inst, instr_info, instruction):
    tokens = re.compile("^" + RE_INST + RE_REG + "$").match(instruction)
    rd = tokens.group(1)
    bin_inst[0:6] = instr_info[OPCODE]
    bin_inst[6:11] = 0x00
    bin_inst[11:16] = 0x00
    bin_inst[16:21] = mips_table.register_name[rd]
    bin_inst[21:26] = 0x00
    bin_inst[26:32] = instr_info[FUNCTION_CODE]
    return bin_inst

def assembler_sh_type(bin_inst, instr_info, instruction):
    tokens = re.compile("^" + RE_INST + RE_REG + "," + RE_REG + "," + RE_SHAMT + "$").match(instruction)
    rd = tokens.group(1)
    rt = tokens.group(2)
    shamt = tokens.group(3)
    bin_inst[0:6] = instr_info[OPCODE]
    bin_inst[6:11] = 0x00
    bin_inst[11:16] = mips_table.register_name[rt]
    bin_inst[16:21] = mips_table.register_name[rd]
    bin_inst[21:26] = int(shamt)
    bin_inst[26:32] = instr_info[FUNCTION_CODE]
    return bin_inst

def assembler_shv_type(bin_inst, instr_info, instruction):
    tokens = re.compile("^" + RE_INST + RE_REG + "," + RE_REG + "," + RE_REG + "$").match(instruction)
    rd = tokens.group(1)
    rt = tokens.group(2)
    rs = tokens.group(3)
    bin_inst[0:6] = instr_info[OPCODE]
    bin_inst[6:11] = mips_table.register_name[rs]
    bin_inst[11:16] = mips_table.register_name[rt]
    bin_inst[16:21] = mips_table.register_name[rd]
    bin_inst[21:26] = 0x00
    bin_inst[26:32] = instr_info[FUNCTION_CODE]
    return bin_inst

def assembler_jr_type(bin_inst, instr_info, instruction):
    tokens = re.compile("^" + RE_INST + RE_REG + "$").match(instruction)
    rs = tokens.group(1)
    bin_inst[0:6] = instr_info[OPCODE]
    bin_inst[6:11] = mips_table.register_name[rs]
    bin_inst[11:16] = 0x00
    bin_inst[16:21] = 0x00
    bin_inst[21:26] = 0x00
    bin_inst[26:32] = instr_info[FUNCTION_CODE]
    return bin_inst

def assembler_l_type(bin_inst, instr_info, instruction):
    tokens = re.compile("^" + RE_INST + RE_REG + "," + RE_IMVAL + "$").match(instruction)
    rt = tokens.group(1)
    imval = tokens.group(2)
    bin_inst[0:6] = instr_info[OPCODE]
    bin_inst[6:11] = 0x000
    bin_inst[11:16] = mips_table.register_name[rt]
    bin_inst[16:32] = int(imval)
    return bin_inst

assembler_dispatch = {
    'R': assembler_r_type,
    'I': assembler_i_type,
    'J': assembler_j_type,
    'MEM' : assembler_mem_type,
    'B': assembler_b_type,
    'MD' : assembler_md_type,
    'MF' : assembler_mf_type,
    'SH' : assembler_sh_type,
    'SHV': assembler_shv_type,
    'JR' : assembler_jr_type,
    'L' : assembler_l_type
    # 'PS': assembler_ps_type
    # 'SP' : assembler_sp_type,
}

if len(sys.argv) == 2:
    with open(sys.argv[1], 'r') as infile:
        for line in infile:
            print assemble(line), ':', line
    infile.close()
elif len(sys.argv) == 1:
    instr_bin = assemble(input("Enter MIPS instruction:"))
else:
    print "Invalid program call" # TODO: Explain usage
