from capstone import *

class asm_tool:
    def __init__(self):
        pass

    def run_capstone(self):
        CODE = b"\x55\x48\x8b\x05\xb8\x13\x00\x00"
        md = Cs(CS_ARCH_X86, CS_MODE_64)
        for i in md.disasm(CODE, 0x1000):
            print("0x%x:\t%s\t%s" % (i.address, i.mnemonic, i.op_str))

