section .text
	global _start
_start:
	mov ax,9h;move 8 in ax == even
	and ax,1;and ax with 1
	jz even
	mov eax,4;NR_write
	mov ebx,1;Fd(stdout)
	mov ecx,oddMsg
	mov edx,oddLen
	int 80h
	jmp outprog

even:
	mov ah,09h
	mov eax,4;NR_write
	mov ebx,1;Stdout
	mov ecx,evenMsg
	mov edx,evenLen
	int 80h
	
outprog:
	mov eax,1
	int 0x80

section .data
evenMsg db 'Even Number!'
evenLen equ $ - evenMsg

oddMsg db 'Odd Number!'
oddLen equ $ - oddMsg
