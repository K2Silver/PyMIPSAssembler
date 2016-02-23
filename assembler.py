# Convert MIPS assembly to binary instruction
import re

def assemble(instruction):
    pattern_rtype = "(\w{2,3})\s*\$([3][0-1]|[1-2]\d|\d),\s*\$([3][0-1]|[1-2]\d|\d),\s*\$([3][0-1]|[1-2]\d|\d)"
    prog   = re.compile(pattern_rtype)
    result = prog.match(instruction)
    print result.group(1)
    print result.group(2)
    print result.group(3)
    print result.group(4)

assemble("add $11, $4, $31")
