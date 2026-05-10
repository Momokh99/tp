.org 100h


.CODE 
DATA_SEG segment
    msg1    DB 'Nombre 1 (0-9): $'
    msg2    DB 13, 10, 'Operateur (+,-,*,/): $'
    msg3    DB 13, 10, 'Nombre 2 (0-9): $'
    msg_res DB 13, 10, 'Resultat = $'
    msg_err DB 13, 10, 'Erreur: Div par 0!$'
    val1    DW 0
    val2    DW 0
    op      DB 0     

DATA_SEG EDNS
CODE_SEG segment
    assume cs:CODE_SEG,
DS:DATA_SEG

main PROC
    ; Initialisation obligatoire du segment de donnees
    MOV AX, DATA_seg
    MOV DS, AX

    ; --- 1. Saisie du premier chiffre ---
    LEA DX, msg1
    MOV AH, 09h
    INT 21h
    MOV AH, 01h         ; Lire un caractere clavier
    INT 21h
    SUB AL, '0'         ; Conversion ASCII vers numerique
    MOV AH, 0
    MOV val1, AX

    ; --- 2. Saisie de l'operateur ---
    LEA DX, msg2
    MOV AH, 09h
    INT 21h
    MOV AH, 01h
    INT 21h
    MOV op, AL

    ; --- 3. Saisie du deuxieme chiffre ---
    LEA DX, msg3
    MOV AH, 09h
    INT 21h
    MOV AH, 01h
    INT 21h
    SUB AL, '0'
    MOV AH, 0
    MOV val2, AX

    ; --- 4. Calcul et affichage du resultat ---
    LEA DX, msg_res
    MOV AH, 09h
    INT 21h

    MOV AX, val1
    MOV BX, val2

    ; Comparaison de l'operateur saisi
    CMP op, '+'
    JE addition
    CMP op, '-'
    JE soustraction
    CMP op, '*'
    JE multiplication
    CMP op, '/'
    JE division
    JMP fin

addition:
    ADD AX, BX
    JMP afficher

soustraction:
    SUB AX, BX
    JMP afficher

multiplication:
    MUL BL              ; AX = AL * BL
    JMP afficher

division:
    CMP BX, 0           ; Gestion de la division par zero
    JE erreur_div
    MOV DX, 0
    DIV BL              ; AL = quotient
    MOV AH, 0
    JMP afficher

erreur_div:
    LEA DX, msg_err
    MOV AH, 09h
    INT 21h
    JMP fin

afficher:
    CALL affiche_entier ; Appel du sous-programme d'affichage

fin:
    MOV AH, 4Ch         ; Fin propre du programme
    INT 21h
main ENDP

; --- Sous-programme d'affichage (Exercice 5) ---
affiche_entier PROC
    PUSH AX
    PUSH BX
    PUSH CX
    PUSH DX
    MOV BX, 10
    MOV CX, 0
extraire:
    MOV DX, 0
    DIV BX
    PUSH DX
    INC CX
    CMP AX, 0
    JNE extraire
afficher_boucle:
    POP DX
    ADD DL, '0'
    MOV AH, 02h
    INT 21h
    LOOP afficher_boucle
    POP DX
    POP CX
    POP BX
    POP AX
    RET
affiche_entier ENDP


END main
