// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input. 
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel. When no key is pressed, the
// program clears the screen, i.e. writes "white" in every pixel.

//////////////////////////////////////////
// Author: 			Nelson Henry		//
// Last Revised:	07/20/2016			//
//////////////////////////////////////////

// SCREEN 	= 16384
// PIXELS 	= 8192
// KBD 		= 24576

//////////////////////////////////////////
// 				Begin Code				//
//////////////////////////////////////////


// Setup Code
	// Initialize variables
    @i
    M=1
	@j
	M=0
	
	// Solving for last screen pixel address
	@SCREEN
	D=A
	@8192		// INPUT: # of pixels. MAX: 8192
	D=D+A
	@k
	M=D
	
// Master Loop
(LOOP0)
    @SCREEN		// Value == 16384
    D=A
    @j			// Setting up screen address counter
    M=D

    @KBD        // Keyboard input
    D=M
    @LOOP1
    D;JGT		// Jump if any keyboard input jump to Blacken screen loop
    @LOOP2
    0;JMP		// Else jump instead up above loop

// Black pixel output loop
(LOOP1)
    @j			// Pointer j: Screen starting pixel iterated
    A=M
    M=-1      	// Blacken screen: referenced j set to -1

    @j			
    MD=M+1		// Iterating to next pixel address & storing for logic check
    @k	
    D=M-D		// Solving for exit logic based on screen size

	// if & else jump selection
    @LOOP0
    D;JLE
    @LOOP1
    0;JMP
	
// White pixel output loop
(LOOP2)
    @j			// Pointer j: Screen starting pixel iterated
	A=M
    M=0        	// Clear Screen: referenced j set to zero

    @j			
	MD=M+1		// Iterating to next pixel address & storing for logic check
    @k
    D=M-D		// Solving for exit logic based on screen size
    
	// if & else jump selection
	@LOOP0
    D;JLE
    @LOOP2
    0;JMP