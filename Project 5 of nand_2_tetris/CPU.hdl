// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/5/CPU.hdl
/**
 * The Hack Central Processing unit (CPU).
 * Parses the binary code in the instruction input and executes it according to the
 * Hack machine language specification. In the case of a C-instruction, computes the
 * function specified by the instruction. If the instruction specifies to read a memory
 * value, the inM input is expected to contain this value. If the instruction specifies
 * to write a value to the memory, sets the outM output to this value, sets the addressM
 * output to the target address, and asserts the writeM output (when writeM = 0, any
 * value may appear in outM).
 * If the reset input is 0, computes the address of the next instruction and sets the
 * pc output to that value. If the reset input is 1, sets pc to 0.
 * Note: The outM and writeM outputs are combinational: they are affected by the
 * instruction's execution during the current cycle. The addressM and pc outputs are
 * clocked: although they are affected by the instruction's execution, they commit to
 * their new values only in the next cycle.
 */
CHIP CPU {

    IN  inM[16],         // M value input  (M = contents of RAM[A])
        instruction[16], // Instruction for execution
        reset;           // Signals whether to re-start the current
                         // program (reset==1) or continue executing
                         // the current program (reset==0).

    OUT outM[16],        // M value output
        writeM,          // Write to M? 
        addressM[15],    // Address in data memory (of M)
        pc[15];          // address of next instruction

   

    PARTS:
    // Decode instruction type
    // instruction[15]=0 → A instruction
    // instruction[15]=1 → C instruction
    Not(in=instruction[15], out=aInstruction);
    
    // A Register
    // Load A if: A-instruction OR C-instruction with dest A (instruction[5])
    And(a=instruction[15], b=instruction[5], out=cToA);
    Or(a=aInstruction, b=cToA, out=loadA);
    Mux16(a=instruction, b=aluOut, sel=instruction[15], out=aIn);
    ARegister(in=aIn, load=loadA, out=aOut, out[0..14]=addressM);
    
    // D Register
    // Load D if: C-instruction AND dest D (instruction[4])
    And(a=instruction[15], b=instruction[4], out=loadD);
    DRegister(in=aluOut, load=loadD, out=dOut);
    
    // ALU input: A or M based on instruction[12]
    Mux16(a=aOut, b=inM, sel=instruction[12], out=aluY);
    
    // ALU
    ALU(x=dOut, y=aluY,
        zx=instruction[11], nx=instruction[10],
        zy=instruction[9],  ny=instruction[8],
        f=instruction[7],   no=instruction[6],
        out=aluOut, out=outM, zr=zrOut, ng=ngOut);
    
    // Write to Memory if: C-instruction AND dest M (instruction[3])
    And(a=instruction[15], b=instruction[3], out=writeM);
    
    // Jump logic
    // instruction[2]=j1 (out<0)
    // instruction[1]=j2 (out=0)
    // instruction[0]=j3 (out>0)
    And(a=ngOut, b=instruction[2], out=jlt);
    And(a=zrOut, b=instruction[1], out=jeq);
    Or(a=ngOut, b=zrOut, out=notPos);
    Not(in=notPos, out=pos);
    And(a=pos, b=instruction[0], out=jgt);
    Or(a=jlt, b=jeq, out=j1);
    Or(a=j1, b=jgt, out=jump);
    And(a=instruction[15], b=jump, out=doJump);
    
    // PC
    Not(in=doJump, out=noJump);
    PC(in=aOut, load=doJump, inc=noJump, reset=reset, out[0..14]=pc);
}
