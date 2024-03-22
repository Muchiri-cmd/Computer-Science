NR_write equ 4
NR_read equ 3
NR_exit equ 1
STDIN equ 0
STDOUT equ 1
STDERR equ 2

segment .data

	prompt1 db "Enter a number: "
	lenprompt1 equ $- prompt1
	prompt2 db "Enter second number: "
	lenprompt2 equ $- prompt2
	opMsg db "The sum is: ";output message
	lenopMsg  equ $- opMsg

segment .bss
	num1 resb 2
	num2 resb 2
	res resb 1

section .text
	global	_start
_start:
	;Prompt user to enter 1st Num
	mov eax,NR_write
	mov ebx,STDOUT
	mov ecx,prompt1
	mov edx,lenprompt1
	int 0x80

	;Read user first number
	mov eax,NR_read
	mov ebx,STDIN
	mov ecx,num1
	mov edx,2
	int 0x80

	;prompt user to enter 2nd num
	mov eax,NR_write
	mov ebx,STDOUT
	mov ecx,prompt2
	mov edx,lenprompt2
	int 0x80

	;Read 2nd input
	mov eax,NR_read
	mov ebx,STDIN
	mov ecx,num2
	mov edx,2
	int 0x80

	;Output (The Sum is:)
	mov eax,NR_write
	mov ebx,STDOUT
	mov ecx,opMsg
	mov edx,lenopMsg
	int 0x80

	;move 1st num to eax and second to ebx
	;subtract ascii '0' to convert it into decimal

	mov eax,[num1]
	sub eax,'0';convert to decimal

	mov ebx,[num2]
	sub ebx,'0';convert to decimal

	;add eax and ebx
	add eax,ebx
	;add '0' to convert to ascii
	add eax,'0'

	;store sum in memory location res
	mov [res],eax

	;output sum
	mov eax,NR_write
	mov ebx,STDOUT
	mov ecx,res
	mov edx,1
	int 0x80

exit:
	mov eax,NR_exit
	xor ebx,ebx
	int 0x80

