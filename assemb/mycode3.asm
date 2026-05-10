
; You may customize this and other start-up templates; 
; The location of this template is c:\emu8086\inc\0_com_template.txt

org 100h

.DATA
    nb1 dw 45
    nb2 dw 72
    maxi dw ?
    msg1 db "le maximum est nb1$"   
    msg2 db "le maximum est nb2$"
    msg_ng db 'les deux nombre sont egaux$' 

.CODE
main PROC
    mov ax, @DATA
    mov ds, ax
    
    mov ax, nb1
    cmp ax, nb2   
    jg nb1_est_superieur
    je egaux
    
    ;nb2>nb1
    mov ax, nb2
    mov maxi, ax
    lea dx, msg1
    jmp afficher
    
    
    
nb1_est_superieur: 
    mov maxi, ax
    lea dx, msg1
    jmp afficher
    
egaux:
    lea dx, msg_ng
    
afficher:
    mov ah, 09h
    int 21h
    
    mov ah, 4Ch
    int 21h
    
main ENDP
END main
    




