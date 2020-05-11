"""CPU functionality."""

import sys

# Opcodes
OPCODES = {
    "ADD":  {"type": 2, "code": "10100000"},
    "AND":  {"type": 2, "code": "10101000"},
    "CALL": {"type": 1, "code": "01010000"},
    "CMP":  {"type": 2, "code": "10100111"},
    "DEC":  {"type": 1, "code": "01100110"},
    "DIV":  {"type": 2, "code": "10100011"},
    "HLT":  {"type": 0, "code": "00000001"},
    "INC":  {"type": 1, "code": "01100101"},
    "INT":  {"type": 1, "code": "01010010"},
    "IRET": {"type": 0, "code": "00010011"},
    "JEQ":  {"type": 1, "code": "01010101"},
    "JGE":  {"type": 1, "code": "01011010"},
    "JGT":  {"type": 1, "code": "01010111"},
    "JLE":  {"type": 1, "code": "01011001"},
    "JLT":  {"type": 1, "code": "01011000"},
    "JMP":  {"type": 1, "code": "01010100"},
    "JNE":  {"type": 1, "code": "01010110"},
    "LD":   {"type": 2, "code": "10000011"},
    "LDI":  {"type": 8, "code": "10000010"},
    "MOD":  {"type": 2, "code": "10100100"},
    "MUL":  {"type": 2, "code": "10100010"},
    "NOP":  {"type": 0, "code": "00000000"},
    "NOT":  {"type": 1, "code": "01101001"},
    "OR":   {"type": 2, "code": "10101010"},
    "POP":  {"type": 1, "code": "01000110"},
    "PRA":  {"type": 1, "code": "01001000"},
    "PRN":  {"type": 1, "code": "01000111"},
    "PUSH": {"type": 1, "code": "01000101"},
    "RET":  {"type": 0, "code": "00010001"},
    "SHL":  {"type": 2, "code": "10101100"},
    "SHR":  {"type": 2, "code": "10101101"},
    "ST":   {"type": 2, "code": "10000100"},
    "SUB":  {"type": 2, "code": "10100001"},
    "XOR":  {"type": 2, "code": "10101011"},
}
def OP(opcode):
    # return int("0b" + OPCODES[opcode]["code"], 2)
    return int(OPCODES[opcode]["code"], 2)

class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        # `PC`: Program Counter, address of the currently executing instruction
        self.pc = 0
        # Ram - 256 bytes of memory
        self.ram = [0] * 256
        # Registers - 8 general-purpose registers.
        self.registers = [0] * 8

    def load(self):
        """Load a program into memory."""

        address = 0

        # reset the memory
        self.ram = [0] * 256

        # get the filename from arguments
        if len(sys.argv) != 2:
            print("Need filename to run program.")
            sys.exit(1)
        
        # read from file and load
        filename = sys.argv[1]

        with open(filename) as f:

            for line in f:

                # ignore blank lines
                if line == '':
                    continue

                # remove comment if exists
                comment_split = line.split('#')

                # Strip White Space
                line = str(comment_split[0]).strip(' ')
                line = str(line).replace('\n', '').replace('\r', '')

                # check if blank
                if line == '':
                    continue

                # get instruction binary number
                instruction = int(line,2)

                # add instruction to memory
                self.ram_write(address, instruction)

                # next memory address
                address += 1


        # program = [
        #     # From print8.ls8
        #     0b10000010, # LDI R0,8
        #     0b00000000,
        #     0b00001000,
        #     0b01000111, # PRN R0
        #     0b00000000,
        #     0b00000001, # HLT
        # ]

        # for instruction in program:
        #     self.ram[address] = instruction
        #     address += 1

    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        #elif op == "SUB": etc
        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            #self.fl,
            #self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    def ram_read(self, address):
        """Reads information stored in ram at given address."""
        # ram_read() should accept the address to read and return the value stored there.
        return self.ram[address]

    def ram_write(self, address, value):
        """Stores given value to ram at the given address."""
        self.ram[address] = value
    
    def run(self):
        """Run the CPU."""
        running = True
        i = 0

        while running and i < 4:
            i+=1
            # read the memory address that's stored in register PC and store that result in IR
            
            # `IR`: Instruction Register, contains a copy of the currently executing instruction
            IR = self.ram_read(self.pc)

            # HLT
            # exit the loop if a HLT instruction is encountered
            if IR == OP("HLT"):
                self.pc += 1
                # stop running
                # print ("Program Stopped.")
                running = False

            # LDI
            # This instruction sets a specified register to a specified value.
            elif IR == OP("LDI"):
                # get register address from ram value
                register = self.ram_read(self.pc + 1)
                # get value from the next ram value
                value = self.ram_read(self.pc + 2)
                # store value into specified register
                self.registers[register] = value
                # move to next counter
                self.pc += 3
            
            # PRN
            # Print numeric value stored in the given register.
            elif IR == OP("PRN"):
                # get register address from ram
                address = self.ram_read(self.pc + 1)
                # load value from registers
                register = self.registers[address]
                # print value
                print (register)
                # move to next counter
                self.pc += 2

