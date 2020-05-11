# Inventory

* Make a list of files here.
* Write a short 3-10-word description of what each file does.
* Note what has been implemented, and what hasn't.
* Read this whole file.
* Skim the spec.

## ls8.py
> Main
Imports CPU, loads, and runs.

## cpu.py

> Main CPU class.

init
> Construct a new CPU.
Includes:
* `self.pc` = PC counter
* `self.ram` = 256 bytes of memory
* `self.registers` = 8 general purpose registers

load()
> Load a program into memory.
* Starts at address 0
* Currently hard coded - program from `print8.ls8`
* sends instruction from program and stores in `ram`

alu(op, reg_a, reg_b)
> ALU operations.
* `ADD` - adds 2 numbers reg_a + reg_b
* Work In Progress

trace()
> Handy function to print out the CPU state. 
* prints CPU state
* suggests possibly calling from run() for debugging

ram_read(address)
> Reads information stored in ram at given address.
* accepts an address 
* returns value of address

ram_write(address, value)
> Stores given value to ram at the given address.
* accepts an address and value
* stores value at the address in ram

run()
> Run the CPU.
* reads first address in memory
* based on value, runs given function
* if value is equal to HLT, this will halt (stop) run

## Examples

### call.ls8
* `LDI R1,MULT2PRINT`
* `LDI R0,10`
* `CALL R1`
* `LDI R0,15`
* `CALL R1`
* `LDI R0,18`
* `CALL R1`
* `LDI R0,30`
* `CALL R1`
* `HLT`
MULT2PRINT (address 24):
* `ADD R0,R0`
* `PRN R0`
* `RET`

### interrupts.ls8
* `LDI R0,0XF8`
* `LDI R1,INTHANDLER`
* `ST R0,R1`
* `LDI R5,1`
* `LDI R0,LOOP`
LOOP (address 15):
* `JMP R0`
INTHANDLER (address 17):
* `LDI R0,65`
* `PRA R0`
* `IRET`

### keyboard.ls8
* `LDI R0,0XF9`
* `LDI R1,INTHANDLER`
* `ST R0,R1`
* `LDI R5,2`
* `LDI R0,LOOP`
LOOP (address 15):
* `JMP R0`
INTHANDLER (address 17):
* `LDI R0,0XF4`
* `LD R1,R0`
* `PRA R1`
* `IRET`

### mult.ls8
> Multiply 2 integers and print value
* `LDI R0,8` -- set value to register 0
* `LDI R1,9` -- set value to register 1
* `MUL R0,R1` -- use function to multiply R0 and R1, overwrite R0
* `PRN R0` -- print register 0
* `HLT` -- stop

### print8.ls8
> Print the number 8
* `LDI R0,8` -- set value to register 0
* `PRN R0` -- print register 0
* `HLT` -- stop

### printstr.ls8
* `LDI R0,HELLO`
* `LDI R1,14`
* `LDI R2,PRINTSTR`
* `CALL R2`
* `HLT`
PRINTSTR (address 12):
* `LDI R2,0`
PRINTSTRLOOP (address 15):
* `CMP R1,R2`
* `LDI R3,PRINTSTREND`
* `JEQ R3`
* `LD R3,R0`
* `PRA R3`
* `INC R0`
* `DEC R1`
* `LDI R3,PRINTSTRLOOP`
* `JMP R3`
PRINTSTREND (address 37):
`RET`
HELLO (address 38):
`01001000 # H`
`01100101 # e`
`01101100 # l`
`01101100 # l`
`01101111 # o`
`00101100 # ,`
`00100000 # [space]`
`01110111 # w`
`01101111 # o`
`01110010 # r`
`01101100 # l`
`01100100 # d`
`00100001 # !`
`00001010 # 0x0a`

### stack.ls8
* LDI R0,1
* LDI R1,2
* PUSH R0
* PUSH R1
* LDI R0,3
* POP R0
* PRN R0
* LDI R0,4
* PUSH R0
* POP R2
* POP R1
* PRN R2
* PRN R1
* HLT

### stackoverflow.ls8
* LDI R0,0
* LDI R1,1
* LDI R3,LOOP
LOOP (address 9):
* PRN R0
* ADD R0,R1
* PUSH R0
* JMP R3