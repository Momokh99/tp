org 100h

.DATA
    val1 dw 25
    val2 dw 10
    result dw ?
    
    
.CODE
main proc
    mov ax, @DATA
    mov ds, ax
    
    mov ax, val1
    add ax, val2
    mov result, ax
    
    mov ax, val1
    sub ax, val2
    
    
    mov ax, val1
    mov bx, val2
    mul bx
    
    
    mov ax, val1
    mov bl, 10
    div bl
    
    
    mov ah, 4Ch
    int 21h
    
main ENDP
END main
    
