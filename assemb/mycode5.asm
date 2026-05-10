
; You may customize this and other start-up templates; 
; The location of this template is c:\emu8086\inc\0_com_template.txt

.MODEL SMALL
.STACK 100h

.DATA
    nombre dw 2025
    msg    dw 'Nombre : $'
    newline db 13,10, '$'
    
.CODE
affich_car proc
    mov ah, 02h
    int 21h
    ret
affich_car ENDP

affich_ent proc
  push ax
  push dx
  push cx 
  push bx

  mov bx, 10
  mov cx, 0

extraire:
  mov dx, 0
  div bx
  push dx
  inc cx
  cmp ax, 0                             
  jne extraire
affich_chif:
  pop dx 
  add dl, '0'
  CALL affich_car
  LOOP affich_chif

  pop bx
  pop cx
  pop dx
  pop ax
  ret
affich_ent ENDP                                                                                                                                                    


main proc
  mov ax, @DATA
  mov ds, ax

  lea dx, msg
  mov ah, 09h
  int 21h

  mov ax, nombre
  call affich_ent

  lea dx, newline
  mov ah, 09h
  int 21h

  mov ah, 4CH
  int 21h

main ENDP
END main




       