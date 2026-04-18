section .data
    a dw 2
    b dw 5
    d dw 0
section .text
    global main

main:
mov ax, [a]
mul ax, [b]
mov [d],ax
ret 