section .data
    a dw 9
    b dw 3
    d dw 0
section .text
    global main

main:
mov ax, [a]
div ax, [b]
mov [d],ax
ret 