// Box.asm for Roll No: 2501420044 (K=44)
// Box starts at row 44 (address 17792)
// Width: 16 pixels (1 word)
// Height: 20 rows

(MAIN)
@KBD
D=M
@SET_BLACK
D;JNE      // If any key is pressed, jump to SET_BLACK

// If no key, fill = 0 (white)
@0
D=A
@fill
M=D
@DRAW
0;JMP

(SET_BLACK)
// If key pressed, fill = -1 (black)
@1
D=-A
@fill
M=D

(DRAW)
// Set starting address (Row 44 = 16384 + 32*44 = 17792)
@17792
D=A
@ptr
M=D

// Set row counter to 20
@20
D=A
@row_count
M=D

(DRAW_ROW)
// Draw one word (16 pixels wide)
@fill
D=M
@ptr
A=M
M=D        // Write to screen memory

// Move pointer to the next row (+32)
@32
D=A
@ptr
M=M+D

// Decrement row counter
@row_count
M=M-1
D=M
@DRAW_ROW
D;JGT      // If row_count > 0, draw next row

@MAIN
0;JMP