section .data
	count dw 0;initialize count to 0
	value db 10;initialize value to 10
section .text
	global _start
_start:
	;increment-decrement
	inc word [count];
	dec byte  [value];

	mov ebx,count
	inc word [ebx]

	mov esi,value
	dec byte [esi]

    	; Exit the program
    	mov eax, 1
    	int 0x80
