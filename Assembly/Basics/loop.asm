@5
D=A
@i
M=D

(LOOP)
@i
D=M

@0
M=D+M

@i
M=M-1
D=M

@LOOP
D;JGT

(END)
@END
0;JMP