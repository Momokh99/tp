
; You may customize this and other start-up templates; 
; The location of this template is c:\emu8086\inc\0_com_template.txt

org 100h

.MODEL SMALL
.CODE
main PROC
    ; Initialisation
    MOV AX, @DATA
    MOV DS, AX

    ; 1. Chiffre 1
    LEA DX, msg1
    MOV AH, 09h
    INT 21h
    
    MOV AH, 01h
    INT 21h
    AND AL, 0Fh         ; ASTUCE PRO : Transforme '&', 'é', '"' ou '1', '2' en vrai chiffre
    MOV val1, AL

    ; 2. Operateur
    LEA DX, msg2
    MOV AH, 09h
    INT 21h
    MOV AH, 01h
    INT 21h
    MOV op, AL

    ; 3. Chiffre 2
    LEA DX, msg3
    MOV AH, 09h
    INT 21h
    
    MOV AH, 01h
    INT 21h
    AND AL, 0Fh         ; Même astuce pour AZERTY
    MOV val2, AL

    ; 4. Calcul
    MOV AL, val1
    MOV BL, val2
    
    CMP op, '+'
    JE addition
    CMP op, '-'
    JE soustraction
    CMP op, '*'
    JE multiplication
    JMP fin

addition:
    ADD AL, BL
    JMP afficher
soustraction:
    SUB AL, BL
    JMP afficher
multiplication:
    MUL BL
    JMP afficher

afficher:
    MOV res, AL
    LEA DX, msg_res
    MOV AH, 09h
    INT 21h
    
    MOV DL, res
    ADD DL, '0'         ; Convertir le résultat pour l'affichage
    MOV AH, 02h
    INT 21h

fin:
    MOV AH, 4Ch
    INT 21h
main ENDP

.DATA
    msg1    DB 'Nombre 1: $'
    msg2    DB 13, 10, 'Op (+,-,*): $'
    msg3    DB 13, 10, 'Nombre 2: $'
    msg_res DB 13, 10, 'Resultat = $'
    val1    DB 0
    val2    DB 0
    res     DB 0
    op      DB 0

END main



