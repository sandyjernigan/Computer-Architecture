"""CPU functionality."""

import sys

LDI = 0b10000010
PRN = 0b01000111
HLT = 0b00000001

class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        # Program Counter
        self.pc = 0
        # Ram - 256 bytes of memory
        self.ram = [0] * 256
        # Registers - 8 general-purpose registers.
        self.registers = [0] * 8 

    def load(self):
        """Load a program into memory."""

        address = 0

        # For now, we've just hardcoded a program:

        program = [
            # From print8.ls8
            0b10000010, # LDI R0,8
            0b00000000,
            0b00001000,
            0b01000111, # PRN R0
            0b00000000,
            0b00000001, # HLT
        ]

        for instruction in program:
            self.ram[address] = instruction
            address += 1


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
        # ram_read() should accept the address to read and return the value stored there.
        return self.ram[address]

    def ram_write(self, address, value):
        self.ram[address] = value
    
    def run(self):
        """Run the CPU."""
        running = True

        while running:
            # read the memory address that's stored in register PC and store that result in IR
            IR = self.ram_read(self.pc)

            # exit the loop if a HLT instruction is encountered
            if IR == HLT:
                self.pc += 1
                running = False

            # This instruction sets a specified register to a specified value.
            elif IR == LDI:
                register = self.ram_read(self.pc + 1)
                value = self.ram_read(self.pc + 2)
                self.registers[register] = value
                self.pc += 3
            
            # Print numeric value stored in the given register.
            elif IR == PRN:
                # get register address from ram
                address = self.ram_read(self.pc + 1)
                # load value from registers
                register = self.registers[address]
                # print value
                print (register)
                # move to next line
                self.pc += 2
