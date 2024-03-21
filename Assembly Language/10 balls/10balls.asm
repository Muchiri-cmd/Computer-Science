section .text
	global _start  ;tells kernel where prog execution begins -must be declared for linker
_start: ;entry point. sort of like int main
	
	;write the message (Displaying 10 balls) to stdout 
	mov edx,len ;move message length to data register
	mov ecx,msg ;move address of message to ecx(count register)
	mov ebx,1   ;specifies writing to fd (stdout) 
	mov eax,4   ;specifies system call num 4 writing to stdout
	
	int 0x80    ;makes call to os(kernel) to perform the instructions
	
	;Write 10( O's )to stdout
	mov edx,10   ;move length of 10 0's to data register
	mov ecx,s2   ;move address of 0's  to count register
	mov ebx,1    ;stdout
	mov eax,4    ;write to stdout
	
	int 0x80   ;call kernel
	
	;Exit program
	mov eax,1  ;system call number (sys_exit)
	
	int 0x80   ;call kernel to terminate prog

section .data
msg db 'Displaying 10 balls',0xa ;define message to be displayed,terminated by new line
len equ $ - msg ; calc length of message
s2 times 10 db 'O';defines sequence of 10 'O's
	
