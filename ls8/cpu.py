"""CPU functionality."""

import sys

# Opcodes
OPCODES = {
    "ADD":  {"type": 8, "code": "10100000"},
    "AND":  {"type": 8, "code": "10101000"},
    "CALL": {"type": 7, "code": "01010000"},
    "CMP":  {"type": 9, "code": "10100111"},
    "DEC":  {"type": 9, "code": "01100110"},
    "DIV":  {"type": 9, "code": "10100011"},
    "HLT":  {"type": 0, "code": "00000001"},
    "INC":  {"type": 9, "code": "01100101"},
    "INT":  {"type": 9, "code": "01010010"},
    "IRET": {"type": 9, "code": "00010011"},
    "JEQ":  {"type": 9, "code": "01010101"},
    "JGE":  {"type": 9, "code": "01011010"},
    "JGT":  {"type": 9, "code": "01010111"},
    "JLE":  {"type": 9, "code": "01011001"},
    "JLT":  {"type": 9, "code": "01011000"},
    "JMP":  {"type": 9, "code": "01010100"},
    "JNE":  {"type": 9, "code": "01010110"},
    "LD":   {"type": 9, "code": "10000011"},
    "LDI":  {"type": 2, "code": "10000010"},
    "MOD":  {"type": 9, "code": "10100100"},
    "MUL":  {"type": 8, "code": "10100010"},
    "NOP":  {"type": 9, "code": "00000000"},
    "NOT":  {"type": 9, "code": "01101001"},
    "OR":   {"type": 9, "code": "10101010"},
    "POP":  {"type": 1, "code": "01000110"},
    "PRA":  {"type": 9, "code": "01001000"},
    "PRN":  {"type": 1, "code": "01000111"},
    "PUSH": {"type": 1, "code": "01000101"},
    "RAM":  {"type": 1, "code": "11101100"},
    "RET":  {"type": 7, "code": "00010001"},
    "SHL":  {"type": 9, "code": "10101100"},
    "SHR":  {"type": 9, "code": "10101101"},
    "ST":   {"type": 2, "code": "10000100"},
    "SUB":  {"type": 9, "code": "10100001"},
    "XOR":  {"type": 9, "code": "10101011"},
}
# def OP(opcode):
#     return int(OPCODES[opcode]["code"], 2)

class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        # `PC`: Program Counter, address of the currently executing instruction
        self.pc = 0
        # Ram - 256 bytes of memory
        self.ram = [0] * 256
        # Registers - 8 general-purpose registers.
        self.reg = [0] * 8

        """ General Registers """
        # R5 is reserved as the interrupt mask (IM)
        self.IM = 5

        # R6 is reserved as the interrupt status (IS)
        self.IS = 6

        # R7 is reserved as the stack pointer (SP)
        self.SP = 7
        # store the top of memory into Register 7
        self.reg[self.SP] = len(self.ram) - 1

        """Internal Registers"""
        # IR: Instruction Register, contains a copy of the currently executing instruction
        self.ir = 0
        # MAR: Memory Address Register, holds the memory address we're reading or writing
        self.mar = 0
        # MDR: Memory Data Register, holds the value to write or the value just read
        self.mdr = 0


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

    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            # Add the value in two registers and store the result in registerA.
            self.reg[reg_a] += self.reg[reg_b]
        elif op == "AND":
            # Bitwise-AND the values in registerA and registerB, then store the result in registerA.
            self.reg[reg_a] &= self.reg[reg_b]
        # TODO
        elif op == "CMP":
            """
            Compare the values in two registers.

            * If they are equal, set the Equal `E` flag to 1, otherwise set it to 0.

            * If registerA is less than registerB, set the Less-than `L` flag to 1,
            otherwise set it to 0.

            * If registerA is greater than registerB, set the Greater-than `G` flag
            to 1, otherwise set it to 0.
            """
            pass
        # TODO
        elif op == "DEC":
            """Decrement (subtract 1 from) the value in the given register."""
            pass
        # TODO
        elif op == "DIV":
            """
            Divide the value in the first register by the value in the second,
            storing the result in registerA.

            If the value in the second register is 0, the system should print an
            error message and halt.
            """
            pass
        # TODO
        elif op == "INC":
            """Increment (add 1 to) the value in the given register."""
            pass
        # TODO
        elif op == "MOD":
            """
            Divide the value in the first register by the value in the second,  storing the _remainder_ of the result in registerA.
            If the value in the second register is 0, the system should print an error message and halt.
            """
            pass
        elif op == "MUL":
            """ Multiply the values in two registers together and store the result in registerA. """
            self.reg[reg_a] *= self.reg[reg_b]
        # TODO
        elif op == "NOT":
            """ Perform a bitwise-NOT on the value in a register, storing the result in the register. """
            pass
        # TODO
        elif op == "OR":
            """ Perform a bitwise-OR between the values in registerA and registerB, storing the result in registerA. """
            pass
        # TODO
        elif op == "SHL":
            """ Shift the value in registerA left by the number of bits specified in registerB, 
                filling the low bits with 0. """
            pass
        # TODO
        elif op == "SHR":
            """ Shift the value in registerA right by the number of bits specified in registerB,
                filling the high bits with 0. """
            pass
        # TODO
        elif op == "SUB":
            """ Subtract the value in the second register from the first, storing the result in registerA. """
            pass
        # TODO
        elif op == "XOR":
            """ Perform a bitwise-XOR between the values in registerA and registerB, storing the
                result in registerA. """
            pass
        # TODO
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

        while running and i < 99:
            i+=1
            # read the memory address that's stored in register PC and store that result in IR
            self.ir = self.ram_read(self.pc)
            OP = ""
            OP_type = ""

            for opcode in OPCODES:
                if int(OPCODES[opcode]["code"], 2) == self.ir:
                    OP = opcode
                    OP_type = OPCODES[opcode]["type"]
                    break

            if OP == "HLT":
                """ Halt the CPU (and exit the emulator). """
                # stop running
                print ("End")
                running = False

            elif not OP == "":
                # Check Type
                if OP_type == 0:
                    self.OPS(OP)
                    # move to next counter
                    self.pc += 1

                elif OP_type == 1:
                    # Operations with 1 argument
                    self.OPS(OP, self.pc + 1)
                    # move to next counter
                    self.pc += 2

                elif OP_type == 2:
                    # Operations with 2 arguments
                    self.OPS(OP, self.pc + 1, self.pc + 2)
                    # move to next counter
                    self.pc += 3
                
                elif OP_type == 7:
                    # PC mutators
                    self.OPS(OP)

                elif OP_type == 8:
                    # ALU Functions - self.alu(op, reg_a, reg_b)
                    self.alu(OP, self.ram_read(self.pc + 1), self.ram_read(self.pc + 2))
                    # move to next counter
                    self.pc += 3

                elif OP_type == 9:
                    print(f"Operation {OP} set TODO. This is incomplete.")
                    self.pc += 1

                else:
                    print (f"Operation {OP} type not found.")
                    self.pc += 1

            # Else
            else:
                print (f"Unknown request on line: {self.pc}")
                self.pc += 1
            
            # self.trace()

    def OPS(self, op, *args):
        # Call Operation by opcode

        if op == "CALL":
            """ Calls a subroutine (function) at the address stored in the register. """
            """
            1. The address of the ***instruction*** _directly after_ `CALL` is pushed onto the stack. This allows us to return to where we left off when the subroutine finishes executing.
            2. The PC is set to the address stored in the given register. We jump to that location in RAM and execute the first instruction in the subroutine. The PC can move forward or backwards from its current location.
            """
            # store next line to execute onto the stack
            self.reg[self.SP] -= 1
            self.ram[self.reg[self.SP]] = self.pc + 2
            # read which register stores out next line passed
            register = self.ram[self.pc + 1]
            # set the PC to the value in that register
            self.pc = self.reg[register]

        # TODO
        elif op == "INT":
            """ Issue the interrupt number stored in the given register. """
            # This will set the _n_th bit in the `IS` register to the value in the given register.
            pass

        # TODO
        elif op == "IRET":
            """ Return from an interrupt handler.
            1. Registers R6-R0 are popped off the stack in that order.
            2. The `FL` register is popped off the stack.
            3. The return address is popped off the stack and stored in `PC`.
            4. Interrupts are re-enabled
            """
            pass
        
        # TODO
        elif op == "JEQ":
            """ If `equal` flag is set (true), jump to the address stored in the given register. """
            pass

        # TODO
        elif op == "JGE":
            """ If `greater-than` flag or `equal` flag is set (true), jump to the address stored in the given register. """
            pass

        # TODO
        elif op == "JGT":
            """ If `greater-than` flag is set (true), jump to the address stored in the given register. """
            pass

        # TODO
        elif op == "JLE":
            """ If `less-than` flag or `equal` flag is set (true), jump to the address stored in the given register."""
            pass

        # TODO
        elif op == "JLT":
            """ If `less-than` flag is set (true), jump to the address stored in the given register. """
            pass

        # TODO
        elif op == "JMP":
            """ Jump to the address stored in the given register. """
            # Set the `PC` to the address stored in the given register.
            pass

        # TODO
        elif op == "JNE":
            """ If `E` flag is clear (false, 0), jump to the address stored in the given register. """
            pass

        # TODO
        elif op == "LD":
            """ Loads registerA with the value at the memory address stored in registerB. """
            # This opcode reads from memory.
            register = self.ram_read(args[0])

        elif op == "LDI":
            """ Set the value of a register to an integer. """
            # get register address from ram value
            register = self.ram_read(args[0])
            # get value from the next ram value
            value = self.ram_read(args[1])
            # store value into specified register
            self.reg[register] = value
        
        # TODO
        elif op == "NOP":
            """ No operation. Do nothing for this instruction. """
            pass

        elif op == "POP":
            """ Pop the value at the top of the stack into the given register. """
            # Copy the value from the address pointed to by `SP` to the given register.
            self.reg[self.ram[args[0]]] = self.ram[self.reg[self.SP]]
            # Increment `SP`.
            self.reg[self.SP] += 1

        # TODO
        elif op == "PRA":
            """ Print alpha character value stored in the given register. """
            # Print to the console the ASCII character corresponding to the value in the register.
            pass
        
        elif op == "PRN":
            """ Print numeric value stored in the given register. """
            # Print to the console the decimal integer value that is stored in the given register.
            # get register address from ram
            address = self.ram_read(args[0])
            # load value from registers
            register = self.reg[address]
            # print value
            print (register)

        elif op == "PUSH":
            """ Push the value in the given register on the stack. """
            # Decrement the `SP`.
            self.reg[self.SP] -= 1
            # Copy the value in the given register to the address pointed to by `SP`.
            self.ram[self.reg[self.SP]] = self.reg[self.ram[args[0]]]

        elif op == "RET":
            """ Return from subroutine. """
            # Pop the value from the top of the stack and store it in the `PC`.
            return_address = self.ram[self.reg[self.SP]]
            # increment the stack pointer
            self.reg[self.SP] += 1
            # set the pc to that value
            self.pc = return_address

        elif op == "ST": 
            """ Store value in registerB in the address stored in registerA. """
            # This opcode writes to memory.
            # register A, the address
            address = self.reg[self.ram_read(args[0])]
            # register B, value
            value = self.reg[self.ram_read(args[1])]
            # store in ram
            self.ram_write(address, value)
        
        elif op == "RAM":
            """ Print numeric value stored in the given ram. """
            address = self.ram_read(args[0])
            print(self.ram_read(address))

        else:
            print (f"Operation {op} invalid.")