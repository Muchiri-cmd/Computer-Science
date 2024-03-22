section .text
	global _start
_start:
	mov ax,'9'
	sub ax,'0';decify
	mov bl,'3'
	sub bl,'0'
	div bl
	add ax,'0'

	mov [res],ax
	mov ecx,msg
	mov edx,len
	mov ebx,1
	mov eax,4
	int 0x80

	mov ecx,res
	mov edx,1
	mov ebx,1
	mov eax,4
	int 0x80

	mov eax,1
	int 0x80

section .data
msg db "Result: "
len equ $-msg

section .bss
res resb 1

