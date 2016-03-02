# TYPE: R, I, B, MD, J, JR, MEM, MF, MD, SH, SP, L
instruction = {
    #INST      OP    FUNCT TYPE
    'add'   : [0x00, 0x20, "R"],
    'addi'  : [0x08, 0x00, "I"],
    'addiu' : [0x09, 0x00, "I"],
    'addu'  : [0x00, 0x21, "R"],
    'and'   : [0x00, 0x24, "R"],
    'andi'  : [0x0C, 0x00, "I"],
    'beq'   : [0x04, 0x00, "B"],
    'bne'   : [0x05, 0x00, "B"],
    'bgtz'  : [0x07, 0x00, "B"],
    'blez'  : [0x06, 0x00, "B"],
    'div'   : [0x00, 0x1A, "MD"],
    'divu'  : [0x00, 0x1B, "MD"],
    'j'     : [0x02, 0x00, "J"],
    'jal'   : [0x03, 0x00, "J"],
    'jalr'  : [0x00, 0x09, "JR"],
    'jr'    : [0x00, 0x08, "JR"],
    'lb'    : [0x20, 0x08, "MEM"],
    'lbu'   : [0x24, 0x00, "MEM"],
    'lh'    : [0x21, 0x00, "MEM"],
    'lhu'   : [0x25, 0x00, "MEM"],
    'li'    : [0x0D, 0x00, "L"], # 0x00 for RS
    'lui'   : [0x0F, 0x00, "L"], # 0x00 for RS
    'lw'    : [0x23, 0x00, "MEM"],
    'mfhi'  : [0x00, 0x10, "MF"],
    'mflo'  : [0x00, 0x12, "MF"],
    'mult'  : [0x00, 0x18, "MD"],
    'multu' : [0x00, 0x19, "MD"],
    'nor'   : [0x00, 0x27, "R"],
    'xor'   : [0x00, 0x26, "R"],
    'xori'  : [0x0e, 0x00, "I"],
    'or'    : [0x00, 0x25, "R"],
    'ori'   : [0x0D, 0x00, "I"],
    'sb'    : [0x28, 0x00, "MEM"],
    'sh'    : [0x29, 0x00, "MEM"],
    'sw'    : [0x2B, 0x00, "MEM"],
    'slt'   : [0x00, 0x2A, "R"],
    'slti'  : [0x0A, 0x00, "I"],
    'sltiu' : [0x0B, 0x00, "I"],
    'sltu'  : [0x00, 0x2B, "R"],
    'sll'   : [0x00, 0x00, "SH"],
    'sllv'  : [0x00, 0x04, "R"],
    'srl'   : [0x00, 0x02, "SH"],
    'sra'   : [0x00, 0x03, "SH"],
    'srlv'  : [0x00, 0x06, "R"],
    'srav'  : [0x00, 0x07, "R"],
    'sub'   : [0x00, 0x22, "R"],
    'subu'  : [0x00, 0x23, "R"],
    'syscall' : [0x00, 0x0C, "SP"],
    'nop'     : [0x00, 0x00, "SP"]
}
