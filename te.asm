section .data
    format db "le résultat est :%d",10,0
section .text
    extern printf
    global main
main:
    mov rbp, rsp; for correct debugging
    ;write your code here
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
    
