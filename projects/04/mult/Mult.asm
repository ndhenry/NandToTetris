// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

//////////////////////////////////////////
// Author: 			Nelson Henry		//
// Last Revised:	07/20/2016			//
//////////////////////////////////////////

// Inputs: R0, R1
// Intermediates: R16
// Output: R2

// Initialize Variables 
@R2
M=0

@counter
M=0

// Looping Structure
(LOOP)
	@counter	
	D=M			// Grabbing the counter value
	@R1			
	D=D-M		// Checking if R1 is greater than the counter (solving while loop logical expression)
	@END
	D;JGE		// Boolean logic to jump to exit loop
	@counter
	M=M+1		// Iterating the counter value
	@R0
	D=M
	@R2
	M=M+D		// Ith addition of the bass number to the running sum in R2
	@LOOP
	0;JMP		// Repeat the loop
(END)
	@END
	0;JMP		// Exit infinite loop