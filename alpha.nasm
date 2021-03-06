; Filename: alpha.nasm
;
; Purpose: to understand alphanumeeric shellcode

global _start			

section .text
_start:

        jmp short call_decoder

decoder:
        pop esi            ; put the obfuscated shellcode to esi
        push esi           ; save the starting point to the stack
                           ;  "DBMAFAGICPCPHDGIGICPGCGJGOIJODFAIJOCFDIJOBLAALMNIA"
        lea edi, [esi+1]   ; put the shellcode to the edi. one char right
                           ;  "BMAFAGICPCPHDGIGICPGCGJGOIJODFAIJOCFDIJOBLAALMNIA"   
        xor eax,eax           
        xor ebx,ebx
        mov al,1           ; I think I tried to use this as a counter?

decode:
        mov bl,byte [esi]  ; move the first byte to ebcx
        sub bl, 41h        ; deduce 41h (so back to the first 4 bit)
        shl bl, 4          ; slide 4 bit to the left
        add bl,byte [edi]  ; add the next value to the ebx
        sub bl, 41h        ; deduce 41h
        mov byte [esi],bl  ; overwrite first byte (so D-41h --> 4 bit left --> add B-41h)
decode_second:	
        inc esi               ; BMAFAGICPCPHDGIGICPGCGJGOIJODFAIJOCFDIJOBLAALMNIA
        inc edi
        inc edi               ; AFAGICPCPHDGIGICPGCGJGOIJODFAIJOCFDIJOBLAALMNIA
        cmp byte [edi], 0x41  ; I tried to use sign flag (if the negative value, SF is on )
        js  final             ; so this part should be skipped while reading the shellcode
        mov bl,byte [esi+eax] 
        sub bl, 41h 
        shl bl, 4
        add bl,byte [edi]
        sub bl, 41h
        mov byte [esi],bl
        add al,1
        jmp short decode_second

final:
        pop esi
        call esi

call_decoder:

        call decoder
        Shellcode: db 0x44,0x42,0x4d,0x41,0x46,0x41,0x47,0x49,0x43,0x50,0x43,0x50,0x47,0x4d,0x48,0x44,0x47,0x49,0x43,0x50,0x47,0x43,0x47,0x4a,0x47,0x4f,0x49,0x4a,0x4f,0x44,0x46,0x41,0x49,0x4a,0x4f,0x43,0x46,0x44,0x49,0x4a,0x4f,0x42,0x4c,0x41,0x41,0x4c,0x4d,0x4e,0x49,0x41,0x40,0x40
