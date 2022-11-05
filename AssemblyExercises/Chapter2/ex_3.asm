# ----> ITALIAN <----
# Implementare un programma in linguaggio assembly MIPS che
# legga da input un intero e calcoli il numero di 1 della sua 
# rappresentazione binaria.
# Esempio
# INPUT: 521 (in binario 1000001001)
# OUTPUT:3

.eqv CONT $t5
.eqv INCR $t6

.text
.globl main
main:
	li INCR,1 # INCREMENTO IL CONTATORE DI UNO AD OGNI CICLO
	li CONT,0 # INIZIALIZZO IL CONTATORE A 0
	li $t1,2 # CARICO IN t2 IL VALORE DUE, OVVERO IL DIVISORE
	
	li $v0,5 # INPUT NUMERO INTERO DA TASTIERA 
	syscall
	move $t0,$v0

WHILE:
	bnez  $t0, DO_WHILE # SE IL VALORE IN t0 NON E' UGUALE A 0 DO WHILE SE NO OUT WHILE
	j OUT_WHILE
	
	
DO_WHILE:

	div $t0,$t1 # DIVISIONE TRA NUMERO IN INPUT E DUE  

	mfhi $t2 # SPOSTO IL RESTO IN t2
	mflo $t3 # SPOSTO IL QUOZIENTE IN t3
	
	move $t0,$t3 # SPOSTO IN t0 IL QUOZIENTE  
	
IF:
	bnez $t2, DO_IF # SE IL RESTO NON E' UGUALE A 0 DO IF SE NO OUT IF
	j OUT_IF
DO_IF:
	li $t9,1 # CARICO IN t9 IL VALORE 1

	add CONT,CONT,INCR # INCREMENTO IL CONTATORE DI 1
	j WHILE # JUMP
OUT_IF:
	li $t8,0 # CARICO IN  t8 IL VALORE 0
	 
	j WHILE # JUMP
OUT_WHILE:
	
	la $a0,Numero  # STAMPO SULLA CONSOLE IL TESTO
	li $v0,4
	syscall

	move $a0,$t5 # STAMPO SULLA CONSOLE IL VALORE CHE HO IN t5
	li $v0,1
	syscall
	
	li $v0,10 # CHIUDO IL PROGRAMMA 
	syscall
		
.data
Numero: .asciiz "\nNumero di 1 della rappresentazione binaria : 
