.org 100h

start:
  mov ax, 1010b
  mov bx, 1001b
  add ax, bx
  mov ah, 09h
  mov dx, msg1
  int 21h


  mov dl, '1'
  mov ah, 02h
  int 21h
  mov dl, '9'
  mov ah, 02h
  int 21h

  mov ah, 4Ch
  xor al, al
  int 21h

  msg1 db 'le rsultat est :$'
