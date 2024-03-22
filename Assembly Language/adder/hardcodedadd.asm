section .text
	global _start
_start:
	mov eax,'1'
	sub eax , '0' ;convert to decimal
	mov ebx,'2'
	sub ebx,'0'
	add eax,ebx
	add eax,'0'
	
	mov [sum] ,eax;move eax to sum memory location to free eax for system call
	mov ecx,op;move output message to ecx
	mov edx,opLength;move op message length to edx
	mov ebx,1;specify stdout for sys_write operation
	mov eax,4;sys_write
	int 80h

	mov ecx,sum;mov sum to ecx
	mov edx,1;move (length of sum) to edx
	mov ebx,1;stdout-specifies operand to sys_write
	mov eax,4;system call to write
	int 80h
	
	mov eax,1;exit
	int 80h

section .data
	op db "Sum : "
	opLength equ $-op
section .bss
	sum resb 1
