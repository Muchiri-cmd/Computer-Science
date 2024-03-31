section .text
	global _start
_start:
	mov bx,3;calculate factorial of 3
	call factorial
	add ax,30h
	mov [fact],ax

	;display message
	mov edx,len
	mov ecx,msg
	mov ebx,1;stdout
	mov eax,4;NR_write
	int 0x80

	;display factorial
	mov edx,1
	mov ecx,fact
	mov ebx,1
	mov eax,4
	int 0x80

	mov eax,1
	int 0x80

factorial:
	cmp bl,1
	jg calculate
	mov ax,1
	ret

calculate:
	dec bl
	call factorial
	inc bl
	mul bl;ax=al*bl
	ret

section .data
msg db 'Factorial 3 is:',0xa
len equ $ - msg

section .bss
fact resb 1
