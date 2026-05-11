section .data
    msg1 db "superieur"
    msg2 db "inferieur"
    a db 3
    b db 5
section .text
    global main
main:
    mov al, a
    add al, b

    cmp  al, 10
    jg sup
    mov dx, offset msg2
    mov ah, 09h
    int 21h
    jmp fin
    sup:
        mov dx, offset msg1
        mov ah, 09h
        int 21h
    fin:
        mov ah, 4ch
        int 21h
        main endp
        end main

