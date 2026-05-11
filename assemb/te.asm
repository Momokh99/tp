main:
    mov bp, sp
    mov ax, 0b1010
    mov bx, 0b1001
    add ax,bx


    sub rsp, 8
    mov rdi,format
    movzx rsi, ax
    mov eax, 0
    call printf
    add rsp, 8
    xor eax, eax
    ret
