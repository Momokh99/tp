
; You may customize this and other start-up templates; 
; The location of this template is c:\emu8086\inc\0_com_template.txt

org 100h

.DATA
  n dw 10
  somme dw 0

.CODE
main PROC
  mov ax, @DATA
  mov ds, ax

  mov cx, n
  mov ax, 0
  mov bx, 1

boucle:
  add ax, bx
  inc bx
  loop boucle

  mov somme, ax

  mov ah, 4Ch
  int 21h

main ENDP
END main




