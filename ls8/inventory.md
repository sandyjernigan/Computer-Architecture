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
* `LDI R1,MULT2PRINT`  -- set line pointer value to register 1
* `LDI R0,10` -- set value 10 to register 0
* `CALL R1` -- Call subroutine based on pointer in register 1
* `LDI R0,15` -- set value 15 to register 0
* `CALL R1` -- Call subroutine based on pointer in register 1
* `LDI R0,18` -- set value 18 to register 0
* `CALL R1` -- Call subroutine based on pointer in register 1
* `LDI R0,30` -- set value 30 to register 0
* `CALL R1` -- Call subroutine based on pointer in register 1
* `HLT` -- Stop
MULT2PRINT (address 24):
* `ADD R0,R0` -- Add value from register 0 to itself
* `PRN R0` -- print new value from register 0
* `RET` -- return to pointer on stack

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
* `LDI R0,8` -- set value "8" to register 0
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
* `LDI R0,1` -- set value "1" to register 0
* `LDI R1,2` -- set value "2" to register 1
* `PUSH R0` -- push value from register 0 to stack
* `PUSH R1` -- push value from register 1 to stack
* `LDI R0,3` -- set value "3" to register 0
* `POP R0` -- pop value to register 0
* `PRN R0` -- print value on register 0 (Prints 2 because the orginial register 0 was removed)
* `LDI R0,4` -- set value "4" to register 0
* `PUSH R0` -- push value from register 0 to stack
* `POP R2` -- pop value to register 2
* `POP R1` -- pop value to register 1
* `PRN R2` -- print value in register 2
* `PRN R1` -- print value in register 1
* `HLT` -- Stop

### stackoverflow.ls8
* LDI R0,0
* LDI R1,1
* LDI R3,LOOP
LOOP (address 9):
* PRN R0
* ADD R0,R1
* PUSH R0
* JMP R3

# Opcodes

## Type 0 - OP with no arguments

### HLT
> Halt the CPU (and exit the emulator).
"HLT":  "code": "00000001"

## Type 1 - OP with 1 argument

### PRN
> Print numeric value stored in the given register.
"PRN":  "code": "01000111"

### PUSH
> Push the value in the given register on the stack.
"PUSH": "code": "01000101"

### POP
> Pop the value at the top of the stack into the given register.
"POP":  "code": "01000110"

## Type 2 - OP with 2 arguments

### LDI
> Set the value of a register to an integer.
"LDI": "code": "10000010"

## Type 8 - ALU Operations

### MUL
> ALU operation - Multiply the values in two registers together and store the result in registerA.
  "MUL":  {"type": 2, "code": "10100010"}



## Type 9 - TO DO 

### CALL
> To Do
  "CALL": {"type": 1, "code": "01010000"}

### DEC
> To Do
  "DEC":  {"type": 1, "code": "01100110"}

### INC
> To Do
  "INC":  {"type": 1, "code": "01100101"}

### INT
> To Do
  "INT":  {"type": 1, "code": "01010010"}

### JEQ
> To Do
  "JEQ":  {"type": 1, "code": "01010101"}

### ADD
> To Do
  "ADD":  {"type": 2, "code": "10100000"}

### AND
> To Do
  "AND":  {"type": 2, "code": "10101000"}

### CMP
> To Do
  "CMP":  {"type": 2, "code": "10100111"}

### DIV
> To Do
  "DIV":  {"type": 2, "code": "10100011"}

### IRET
> To Do
  "IRET": {"type": 0, "code": "00010011"}

### JGE
> To Do
  "JGE":  {"type": 1, "code": "01011010"}
### JGT
> To Do
  "JGT":  {"type": 1, "code": "01010111"}
### JLE
> To Do
  "JLE":  {"type": 1, "code": "01011001"}
### JLT
> To Do
  "JLT":  {"type": 1, "code": "01011000"}
### JMP
> To Do
  "JMP":  {"type": 1, "code": "01010100"}
### JNE
> To Do
  "JNE":  {"type": 1, "code": "01010110"}
### LD
> To Do
  "LD":   {"type": 2, "code": "10000011"}
### MOD
> To Do
  "MOD":  {"type": 2, "code": "10100100"}
### NOP
> To Do
  "NOP":  {"type": 0, "code": "00000000"}
### NOT
> To Do
  "NOT":  {"type": 1, "code": "01101001"}
### OR
> To Do
  "OR":   {"type": 2, "code": "10101010"}
### PRA
> To Do
  "PRA":  {"type": 1, "code": "01001000"}
### RET
> To Do
  "RET":  {"type": 0, "code": "00010001"}

### SHL
> To Do
  "SHL":  {"type": 2, "code": "10101100"}

### SHR
> To Do
  "SHR":  {"type": 2, "code": "10101101"}

### ST
> To Do
  "ST":   {"type": 2, "code": "10000100"}

### SUB
> To Do
  "SUB":  {"type": 2, "code": "10100001"}

### XOR
> To Do
  "XOR":  {"type": 2, "code": "10101011"}