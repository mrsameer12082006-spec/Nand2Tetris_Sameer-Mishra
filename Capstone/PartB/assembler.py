#!/usr/bin/env python3
import sys
import os

# Standard Hack predefined symbols
PREDEFINED = {
    'SP':0, 'LCL':1, 'ARG':2, 'THIS':3, 'THAT':4,
    'R0':0, 'R1':1, 'R2':2, 'R3':3, 'R4':4, 'R5':5, 'R6':6, 'R7':7,
    'R8':8, 'R9':9, 'R10':10, 'R11':11, 'R12':12, 'R13':13, 'R14':14, 'R15':15,
    'SCREEN':16384, 'KBD':24576
}

COMP = {
    '0':'0101010', '1':'0111111', '-1':'0111010', 'D':'0001100', 'A':'0110000', '!D':'0001101',
    '!A':'0110001', '-D':'0001111', '-A':'0110011', 'D+1':'0011111', 'A+1':'0110111',
    'D-1':'0001110', 'A-1':'0110010', 'D+A':'0000010', 'D-A':'0010011', 'A-D':'0000111',
    'D&A':'0000000', 'D|A':'0010101', 'M':'1110000', '!M':'1110001', '-M':'1110011',
    'M+1':'1110111', 'M-1':'1110010', 'D+M':'1000010', 'D-M':'1010011', 'M-D':'1000111',
    'D&M':'1000000', 'D|M':'1010101'
}
# Aliases for commutative operations
COMP['A+D'] = COMP['D+A']; COMP['M+D'] = COMP['D+M']; COMP['A&D'] = COMP['D&A']; COMP['M&D'] = COMP['D&M']; COMP['A|D'] = COMP['D|A']; COMP['M|D'] = COMP['D|M']

DEST = {
    '':'000', 'M':'001', 'D':'010', 'MD':'011', 'A':'100', 
    'AM':'101', 'AD':'110', 'AMD':'111'
}

JUMP = {
    '':'000', 'JGT':'001', 'JEQ':'010', 'JGE':'011', 
    'JLT':'100', 'JNE':'101', 'JLE':'110', 'JMP':'111'
}

def assemble(filename):
    # 1. Read file and strip comments/blank lines
    with open(filename, 'r') as f:
        lines = f.readlines()

    cleaned_lines = []
    symbols = PREDEFINED.copy()
    symbol_address = 16

    # FIRST PASS: Handle Labels
    for line_num, line in enumerate(lines, 1):
        line = line.split('//')[0].strip()
        if not line:
            continue
        
        if line.startswith('(') and line.endswith(')'):
            label = line[1:-1].strip()
            # YOUR EXTRA FEATURE (K=44 -> K%3=2): Warn on duplicate labels
            if label in symbols:
                print(f"Warning: Duplicate label '{label}' found at line {line_num}!")
            else:
                symbols[label] = len(cleaned_lines)
        else:
            cleaned_lines.append((line, line_num))

    # SECOND PASS: Translate to binary
    binary_output = []
    for line, line_num in cleaned_lines:
        # A-Instruction (@value)
        if line.startswith('@'):
            value_str = line[1:].strip()
            if value_str.isdigit():
                address = int(value_str)
            else:
                # It's a variable or label
                if value_str not in symbols:
                    symbols[value_str] = symbol_address
                    symbol_address += 1
                address = symbols[value_str]
            
            if address < 0 or address > 32767:
                raise ValueError(f"Line {line_num}: Address out of bounds")
            
            binary_output.append(format(address, '016b'))
        
        # C-Instruction (dest=comp;jump)
        else:
            dest = ''
            comp = ''
            jump = ''

            if '=' in line:
                dest, line = line.split('=', 1)
            if ';' in line:
                comp, jump = line.split(';', 1)
            else:
                comp = line

            dest = dest.strip()
            comp = comp.strip()
            jump = jump.strip()

            if comp not in COMP:
                raise ValueError(f"Line {line_num}: Invalid comp '{comp}'")
            
            binary_output.append('111' + COMP[comp] + DEST[dest] + JUMP[jump])

    # Write output
    out_filename = filename.replace('.asm', '.hack')
    with open(out_filename, 'w') as f:
        for b in binary_output:
            f.write(b + '\n')
    
    print(f"Successfully assembled {filename} -> {out_filename}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python assembler.py <file.asm>")
        sys.exit(1)
    
    assemble(sys.argv[1])