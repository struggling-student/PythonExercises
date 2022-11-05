# ----> ITALIAN <----
# Trasformare il programma nella Traccia 1 in una macro.

.macro stampa_matrice
analisi_riga:
	li $t3,1 
analisi_colonna:
	sub $t6,$t2,1 	# CALCOLO ELEMENTO R,C
	mul $t9,$t6,$t1 # 
	sub $t7,$t3,1   #  r,c=C(r-1)+(c-1)
	add $t9,$t9,$t7 # 
	mul $t9,$t9,4 	# MOLTIPLICAZIONE DIMENSIONE (4=WORD)
	lw $t8,matrice($t9) # PRELIEVO ELEMENTO
	
	move $a0,$t8 	# STAMPA ELEMENTO
	li $v0,1
	syscall
	
	la $a0,tabulato # PRINT SU CONSOLE
	li $v0,4
	syscall
	
	addi $t3,$t3,1 # INCREMENTO COLONNA
	ble $t3,$t1,analisi_colonna
	
	la $a0,riga # PRINT SU CONSOLE
	li $v0,4
	syscall
	
	addi $t2,$t2,1 # INCREMENTO RIGA
	ble $t2,$t0,analisi_riga
.end_macro
.text
.globl main
main:
	lw $t0,R # NUMERO RIGHE R
	lw $t1,C # NUMERO COLONNE C
	li $t2,1 # INDICE r
	li $t3,1 # INDICE c
	
	stampa_matrice
	
	li $v0,10 # FINE PROGRAMMA
	syscall

.data
matrice: .word 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20
R: .word 5
C: .word 4
tabulato: .asciiz "\t"
riga: .asciiz"\n"
