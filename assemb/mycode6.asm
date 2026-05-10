.org 100h

; Empeche le processeur d'executer les donnees comme des instructions
JMP main 

.DATA
    invite  DB 'Entrez une chaine (max 50 car.) : $'
    buf_max DB 52                       
    buf_len DB 0                        
    buf     DB 52 DUP(0)                
    msg_res DB 13, 10, 'Nombre de voyelles : $'

.CODE
main PROC
    ; Initialisation du segment de donnees
    MOV AX, @DATA
    MOV DS, AX

    ; Affichage de l'invite
    LEA DX, invite
    MOV AH, 09h
    INT 21h

    ; Lecture de la chaine (Fonction 0Ah)
    LEA DX, buf_max 
    MOV AH, 0Ah
    INT 21h

    ; --- CORRECTION ICI ---
    ; On doit pointer SI sur le texte reel. 
    ; Dans le buffer de la fonction 0Ah :
    ; [DX] = Max, [DX+1] = Longueur reelle, [DX+2] = Debut du texte
    LEA SI, buf_max
    ADD SI, 2                           ; On saute les 2 octets de controle pour arriver au texte
    
    MOV CL, buf_len                     
    MOV CH, 0                           
    MOV BX, 0                           ; BX = compteur de voyelles

compter:
    CMP CX, 0
    JE fin_comptage                     
    
    MOV AL, [SI]                        
    INC SI                              
    DEC CX                              

    ; Conversion en minuscule
    CMP AL, 'A'
    JB verifier_voyelle
    CMP AL, 'Z'
    JA verifier_voyelle
    OR AL, 20h                          

verifier_voyelle:
    CMP AL, 'a' 
    JE c_est_voyelle
    CMP AL, 'e' 
    JE c_est_voyelle
    CMP AL, 'i' 
    JE c_est_voyelle
    CMP AL, 'o' 
    JE c_est_voyelle
    CMP AL, 'u' 
    JE c_est_voyelle
    JMP compter

c_est_voyelle:
    INC BX                              
    JMP compter

fin_comptage:
    LEA DX, msg_res
    MOV AH, 09h
    INT 21h

    ; Affichage du chiffre final
    ADD BL, '0'                         
    MOV DL, BL
    MOV AH, 02h
    INT 21h

    MOV AH, 4Ch
    INT 21h
main ENDP
END main
