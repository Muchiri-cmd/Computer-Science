section .text
	global _start
_start:
	mov al,'2'
	sub al,'0';convert to deci
	mov bl,'2'
	sub bl,'0';decify
	mul bl
	add al,'0'

	mov [res],al
	mov ecx,msg
	mov edx,len
	mov ebx,1
	mov eax,4
	int 80h

	mov ecx,res
	mov edx,1
	mov ebx,1
	mov eax,4
	int 80h

	mov eax,1
	int 80h

section .data
msg db "Result: "
len equ $-msg

section .bss
	res resb 1

