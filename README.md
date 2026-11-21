# Nand2Tetris Laboratory Work

Semester 3 implementations for the Nand2Tetris course. This repository contains HDL chips and Hack assembly programs that build progressively from Boolean logic to a complete computer.

## Repository Contents

| Directory | Work covered |
| --- | --- |
| [`Project 1 of nand_2_tetris`](Project%201%20of%20nand_2_tetris) | Boolean logic and elementary gates |
| [`project 2 of nand_2_tetris`](project%202%20of%20nand_2_tetris) | Arithmetic and the 16-bit ALU |
| [`project 3 of nand_2_tetris`](project%203%20of%20nand_2_tetris) | Sequential logic and memory |
| [`Project 5 of nand_2_tetris`](Project%205%20of%20nand_2_tetris) | Hack CPU, memory map, and computer |
| [`Assembly/Basics`](Assembly/Basics) | Addition, branching, and looping |
| [`Assembly/IO`](Assembly/IO) | Keyboard, screen, and instruction-format examples |
| [`Capstone`](Capstone) | Custom assembler and complete computer demonstrations |

## Project 1 — Boolean Logic

Elementary gate implementations built with HDL:

- Basic gates: `And`, `Or`, `Xor`, `Not`
- 16-bit gates: `And16`, `Or16`, `Not16`
- Multi-way OR: `Or8Way`
- Multiplexers: `Mux`, `Mux16`, `Mux4Way16`, `Mux8Way16`
- Demultiplexers: `DMux`, `DMux4Way`, `DMux8Way`

## Project 2 — Arithmetic

Arithmetic chips and the Hack Arithmetic Logic Unit:

- `HalfAdder`
- `FullAdder`
- `Add16`
- `Inc16`
- `ALU`

The ALU computes arithmetic and Boolean functions and produces the `zr` and `ng` status flags.

## Project 3 — Memory

Sequential logic and a hierarchy of memory chips:

- `Bit`
- `Register`
- `PC`
- `RAM8`
- `RAM64`
- `RAM512`
- `RAM4K`
- `RAM16K`

## Project 5 — Computer Architecture

The major chips that compose the Hack computer:

- [`CPU.hdl`](Project%205%20of%20nand_2_tetris/CPU.hdl) decodes instructions, executes operations through the ALU, reads memory, writes memory, and controls jumps.
- [`Memory.hdl`](Project%205%20of%20nand_2_tetris/Memory.hdl) maps RAM, screen memory, and keyboard memory.
- [`Computer.hdl`](Project%205%20of%20nand_2_tetris/Computer.hdl) connects the ROM, CPU, and memory.

## Assembly Programs

### Basics

- [`Add.asm`](Assembly/Basics/Add.asm) adds `R0` and `R1` and stores the result in `R2`.
- [`branching.asm`](Assembly/Basics/branching.asm) compares two values and stores the larger value in `R2`.
- [`loop.asm`](Assembly/Basics/loop.asm) repeatedly adds a value and decrements a loop counter.

### Input and Output

- [`keyboard.asm`](Assembly/IO/keyboard.asm) reads the keyboard and exits the loop when the `q` key is detected.
- [`screen.asm`](Assembly/IO/screen.asm) writes values to selected screen-memory locations.
- [`Hack-to-Binary.asm`](Assembly/IO/Hack-to-Binary.asm) lists the binary instruction fields for example Hack assembly instructions.

## Capstone Project

The [`Capstone`](Capstone) directory extends the course work with an assembler and additional computer demonstrations:

- [`Part A`](Capstone/PartA) contains complete CPU, memory, and computer HDL implementations, with screenshots from the Hardware Simulator.
- [`Part B`](Capstone/PartB) provides `Add.asm`, duplicate-label testing, and the Python assembler used to produce Hack machine code.
- [`Part C`](Capstone/PartC) contains the interactive `Box.asm` graphics program and screenshots demonstrating keyboard input and screen output.
- The `assembler.py` scripts support assembly, symbol handling, and generation of `.hack` files.

## Repository Structure

```text
Nand2Tetris/
├── Project 1 of nand_2_tetris/
├── project 2 of nand_2_tetris/
├── project 3 of nand_2_tetris/
├── Project 5 of nand_2_tetris/
│   ├── CPU.hdl
│   ├── Memory.hdl
│   └── Computer.hdl
├── Assembly/
    ├── Basics/
    │   ├── Add.asm
    │   ├── branching.asm
    │   └── loop.asm
    └── IO/
        ├── Hack-to-Binary.asm
        ├── keyboard.asm
        └── screen.asm
└── Capstone/
│   ├── PartA/
│   ├── PartB/
│   └── PartC/
```

## Running the HDL Projects

1. Install the official Nand2Tetris software suite.
2. Open `HardwareSimulator`.
3. Load an `.hdl` file.
4. Load the matching `.tst` and `.cmp` scripts supplied with the course.
5. Run the test and verify that the output shows no mismatches.

## Running Assembly Programs

1. Open the Nand2Tetris `Assembler`.
2. Load an `.asm` file from `Assembly/Basics` or `Assembly/IO`.
3. Assemble it to produce a `.hack` machine-language file.
4. Load the result into `CPUEmulator` for execution.

## Submission PDFs

- [Project 1 lab submission](Project%201%20of%20nand_2_tetris/Nand2Tetris_Lab1_Project1_Sameer_Mishra.pdf)
- [Project 3 HDL code and screenshots](project%203%20of%20nand_2_tetris/Nand2Tetris_Project3_HDL_Code_and_Screenshots_Updated.pdf)

## Author

**Sameer Mishra**
