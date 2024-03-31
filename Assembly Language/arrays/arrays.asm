section .text
	global _start
_start:
	mov eax,3;number of bytes to be summed
	mov ebx,0;stores sum
	mov ecx,x;pointer to curr elem

l1: add ebx,[ecx]
	add ecx,1;move pointer to next elem
	dec eax;decrements counter
	jnz l1;if counter not zero reiterate
done:
	add ebx,'0'
	mov [sum],ebx;move result to sum
display:
	mov edx,1
	mov ecx,sum
	mov ebx,1
	mov eax,4
	int 0x80

	mov eax,1
	int 0x80
section .data
global x
x:
	db 1
	db 2
	db 3
sum:
	db 0
