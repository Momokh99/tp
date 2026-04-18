section .bss
    buffer resb 16
section .text
global _start

_start:
    ;read
    mov rax, 0
    mov rdi, 0
    mov rsi, buffer
    mov rdx, 16
    syscall
    
    mov rsi, buffer
    xor rax, rax
    xor rbx, rbx
    
    mov bl, [rsi]
    cmp bl, '-'
    jne convert
    
    mov rbx, 1
    inc rsi
    
convert:
    xor rcx, rcx

next_digit:
    mov cl, [rsi]
    cmp cl, 10
    je done_convert
    
    sub cl, '0'
    imul raX, 10
    add rax, rcx
    
    inc rsi
    jmp next_digit
    
done_convert:
    cmp rbx, 1
    jne abs_check
    
    neg rax
    
abs_check:
    cmp rax, 0
    jge print
    
    neg rax
    
print:
    mov rbx, 10
    mov rdi, buffer + 15
    mov byte [rdi], 10
    
convert_back:
    dec rdi
    xor rdx, rdx
    div rbx
    add dl, '0'
    mov [rdi], dl
    
    test rax, rax
    jnz convert_back
    
    ;write
    mov rax, 1
    mov rdi, 1
    mov rsi, rdi 
    mov rdx, buffer + 16 - rdi
    syscall
    
    ;exit
    mov rax, 60
    xor rdi, rdi
    syscall


