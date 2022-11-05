# ----> ITALIAN <----
# Dato un intero positivo a definito in memoria, stampare a 
# video "Terzo bit 1" nel caso in cui il terzo bit del 
# numero a sia 1 o "Terzo bit 0" altrimenti.

.text
.globl main

main: 
	lw $t1, val # CARICO MEMOLE
	li $t2, 4 # CARICO 4 IN t2
	and $t3,$t1,$t2 # FACCIO L'AND BIT A BIT TRA MEMOLE E 4
	beq $t3,$t2, test # SE L'AND TORNA 4 CHIAMA TEST
	
	la $a0,mex1 # STAMPO A VIDEO IL MESSAGGIO 
	li $v0,4
	syscall
	
	li $v0, 10 # FINE PROGRAMMA
	syscall
	
test:
	li $t0, 1 # SETTO t0 A 1
	
	la $a0,mex0 # STAMPO A VIDEO IL MESSAGGIO 
	li $v0,4
	syscall
	
.data
val: .word 36
mex0: .asciiz "Terzo bit 1"
mex1: .asciiz "Terzo bit 0"
