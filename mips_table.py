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
    'jalr'  : [0x00, 0x09, "JR"], # rd, rs or rs
    'jr'    : [0x00, 0x08, "JR"],
    'lb'    : [0x20, 0x08, "MEM"],
    'lbu'   : [0x24, 0x00, "MEM"],
    'lh'    : [0x21, 0x00, "MEM"],
    'lhu'   : [0x25, 0x00, "MEM"],
    'li'    : [0x0D, 0x00, "PS"], # pseudo instructions
    'lui'   : [0x0F, 0x00, "L"],
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
    'sllv'  : [0x00, 0x04, "SHV"],
    'srl'   : [0x00, 0x02, "SH"],
    'sra'   : [0x00, 0x03, "SH"],
    'srlv'  : [0x00, 0x06, "SHV"],
    'srav'  : [0x00, 0x07, "SHV"],
    'sub'   : [0x00, 0x22, "R"],
    'subu'  : [0x00, 0x23, "R"],
    'syscall' : [0x00, 0x0C, "SP"],
    'nop'     : [0x00, 0x00, "SP"]
}

register_name = {
    'zero' : 0,  # [zero]
    'at'   : 1,  # [assermbler temporary], reserved by assembler
    'v0'   : 2,  # [values] from expression evaluation and function results
    'v1'   : 3,
    'a0'   : 4,  # [arguments] first four paramters for subroutines
    'a1'   : 5,
    'a2'   : 6,
    'a3'   : 7,
    't0'   : 8,  # [temporaries] caller saved if needed, not preserved across procedure calls
    't1'   : 9,  #               subroutines can use without saving
    't2'   : 10,
    't3'   : 11,
    't4'   : 12,
    't5'   : 13,
    't6'   : 14,
    't7'   : 15,
    's0'   : 16, # [saved] callee saved, preserved across procedure calls
    's1'   : 17, #         subroutine must save original and restore if used
    's2'   : 18,
    's3'   : 19,
    's4'   : 20,
    's5'   : 21,
    's6'   : 22,
    's7'   : 23,
    't8'   : 24,
    't9'   : 25,
    'k0'   : 26, # reserved for interrupt/trap handler
    'k1'   : 27,
    'gp'   : 28, # [global pointer] middle of 64K block in static data
    'sp'   : 29, # [stack pointer] last location in stack
    'fp'   : 30, # [frame pointer]
    'ra'   : 31, # [return address]

    '0'    : 0,  # [zero]
    '1'    : 1,  # [assermbler temporary], reserved by assembler
    '2'    : 2,  # [values] from expression evaluation and function results
    '3'    : 3,
    '4'    : 4,  # [arguments] first four paramters for subroutines
    '5'    : 5,
    '6'    : 6,
    '7'    : 7,
    '8'    : 8,  # [temporaries] caller saved if needed, not preserved across procedure calls
    '9'    : 9,  #               subroutines can use without saving
    '10'   : 10,
    '11'   : 11,
    '12'   : 12,
    '13'   : 13,
    '14'   : 14,
    '15'   : 15,
    '16'   : 16, # [saved] callee saved, preserved across procedure calls
    '17'   : 17, #         subroutine must save original and restore if used
    '18'   : 18,
    '19'   : 19,
    '20'   : 20,
    '21'   : 21,
    '22'   : 22,
    '23'   : 23,
    '24'   : 24,
    '25'   : 25,
    '26'   : 26, # reserved for interrupt/trap handler
    '27'   : 27,
    '28'   : 28, # [global pointer] middle of 64K block in static data
    '29'   : 29, # [stack pointer] last location in stack
    '30'   : 30, # [frame pointer]
    '31'   : 31, # [return address]
}
