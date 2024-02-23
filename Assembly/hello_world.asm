;hello_world.asm

global _start
section .text:
_start:
	mov eax, 4 ;use write syscall
	mov ecx, 1;use stdout  as file descriptor
	mov ecx, message;message as buffer
	mov edx, message_length;
	int 0x80
	
	;Exit

	mov eax,0X1;exit
	mov ebx,0;return 0
	int 0x80
	

section .data:
	message:db "Hello World!", 0xA
	message_length equ $-message
