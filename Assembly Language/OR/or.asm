section .text
	global _start
_start:
	mov al, 5
	mov bl, 3
	or al,bl
	add al,'0';convert decimal to ascii

	mov [result],al
	mov eax,4 ;NR_write
	mov ebx,1 ;stdout
	mov ecx,result
	mov edx,1; length 1 byte
	int 0x80

outprog:
	mov eax,1;NR_exit
	int 0x80

section .bss
	result resb 1;reserve 1 byte for result

