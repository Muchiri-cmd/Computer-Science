section .data ;stores constants and initialized data
	promptMsg db 'Please enter a number: ' ;prompt user to input number
	lenpromptMsg equ $-promptMsg ;calculate length of promptMsg
	
	opMsg db 'You have entered: ';output message
	lenopMsg equ $-opMsg	       ;calculate length of output msg

section .bss 	;stores uninitialized variables
	num resb 5 ;declare var num and reserve 5 bytes of memory space for value

section .text ;code segment (keeps actual code/instructions)
	global _start ;tells kernel where execution begins
_start:	;entry point (User Prompt)
	mov eax,4 ;sys_write call
	mov ebx,1 ;specifies variable for (sys_write) fd(stdout)
	mov ecx, promptMsg ;move promptMsg add to counter(ecx) register
	mov edx, lenpromptMsg ;move length of promptmsg to data (edx) register
	int 80h ;writes and returns control back to prg
	
	;Read and store user input
	mov eax,3 ;sys_read call
	mov ebx,0 ;fd for (stdin)
	mov ecx,num;moves address of num into ecx register
	mov edx,5;passes length 5 into edx (call should read upto 5 bytes)
	int 80h;syscall read input

	;output message (You entered :) 
	mov eax,4;sys_write call
	mov ebx,1;fd(stdout)
	mov ecx,opMsg;move address of opMsg to ecx register
	mov edx,lenopMsg ;pass length of output Message
	int 80h;syscall write output message

	;output number entered
	mov eax,4;syscall(write)
	mov ebx,1;fd(stdout)
	mov ecx,num;move address of number entered to ecx
	mov edx,5;pass length of num
	int 80h

	;Exit 
	mov eax,1;syscall exit
	mov ebx,0;terminate program
	int 80h;call kernel to teminate
