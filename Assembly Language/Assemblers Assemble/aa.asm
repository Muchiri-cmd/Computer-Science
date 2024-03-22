;Declare constants
NR_write equ 4
NR_exit equ 1
STDIN equ 0
STDOUT equ 1
STDERR equ 2

section .text
	global _start;where exec begins
_start:;entry point
	
	;output message 1
	mov eax,NR_write
	mov ebx,STDOUT
	mov ecx,msg1
	mov edx,lenmsg1
	int 80h

	;output message 2
	mov eax,NR_write
	mov ebx,STDOUT
	mov ecx,msg2
	mov edx,lenmsg2
	int 80h

	;output message 3
	mov eax,NR_write
	mov ebx,STDOUT
	mov ecx,msg3
	mov edx,lenmsg3
	int 80h

	mov eax,NR_exit; Terminate program
	int 80h

section .data
msg1 db 'Why did the assembly dev go broke?Coz he spent all his bytes on rent',0xa,0xD
lenmsg1 equ $-msg1

msg2 db 'Why was the assembly dev divorced? Coz he always did JMPed to conclusions',0xa,0xD
lenmsg2 equ $-msg2

msg3 db 'Linux assembly  is for builders,not those who cling to (windows) of limitation',0xa,0xD
lenmsg3 equ $-msg3

	



