
; You may customize this and other start-up templates; 
; The location of this template is c:\emu8086\inc\0_com_template.txt

org 100h

.DATA
    msg db 'hi mohamed$', 13, 10

.CODE
main PROC
    mov ax, @DATA
    mov ds, ax
    
    lea dx, msg
    mov ah, 09h
    int 21h
    
    
    mov ah, 4Ch
    int 21h 

main ENDP




