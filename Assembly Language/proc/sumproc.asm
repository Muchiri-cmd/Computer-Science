section .text
	global _start
_start:
	mov ecx,'3'
	sub ecx,'0';conv to decimal
	mov edx,'4'
	sub edx,'0';convert to decimal

	call sum
	mov [res],eax
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
sum:
	mov eax,ecx
	add eax,edx
	add eax,'0'
	ret

section .data
msg db "The sum is:",0xA,0xD
len equ $- msg

segment .bss
res resb 1
