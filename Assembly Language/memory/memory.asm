section .text
	global _start
_start:
	mov eax,45;NR_brk
	xor ebx,ebx
	int 0x80

	add eax,16384;number of bytes to reserve
	mov ebx,eax
	mov eax,45;NR_brk
	int 0x80

	cmp eax,0
	jl exit ;exit if err
	mov edi,eax;edi=highest available address
	sub edi,4 ;pointing to last Dword
	mov ecx,4096 ;number of Dwords allocated
	xor eax,eax;clear eax
	std ;backward
	rep stosd ;repeat for entire allocated area
	cld

	mov eax,4
	mov ebx,1
	mov ecx,msg
	mov edx,len
	int 0x80

exit:
	mov eax,1
	xor ebx,ebx
	int 0x80

section .data
msg db "Allocated 16 kilos of memory.Jk its kilo bytes",10
len equ $ -msg 

