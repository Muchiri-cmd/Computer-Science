section .text
	global _start
_start:
	;Write initial name (Zara Ali)
	mov eax,4; write
	mov ebx,1; stdout
	mov ecx,name;
	mov edx,9;name length
	int 0x80

	mov  [name] , dword 'Zari' ;change name
	
	;writing name (Zari Ali)
	mov eax,4
	mov ebx,1
	mov ecx,name
	mov edx,8 ;name length
	int 0x80

	mov eax,1
	int 0x80

section .data
name db 'Zara Ali'

