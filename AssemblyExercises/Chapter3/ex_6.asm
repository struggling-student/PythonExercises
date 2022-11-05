# ----> ITALIAN <----
# Confrontare due interi positivi a e b, definiti in memoria,
# e mettere in $t0 il valore 0 se a e'maggiore di b, 1
# altrimenti. Non è possibile utilizzare l'istruzione 
# di comparazione tra valori: operare sui singoli bit 
# dei valori.

.text
.globl main
main:
	lw $t0,a # CARICO IN t0 IL VALORE DI a
	lw $t1,b # CARICO IN t1 IL VALORE DI b
	li $t9,0 # INIZIALIZZO IL CONTATORE
	li $t8,1 # INIZIALIZZO IL VALORE DA RITORNARE
	
RIPETI:
	addi $t9,$t9,1 # INCREMENTO IL CONTATORE
	bgt $t9,32,FINE # SALTA A FINE SE SONO STATE FATTE 32 ITERAZIONI
	rol $t0,$t0,1 # RUOTO t0 DI UN BIT VERSO SINISTRA
	rol $t1,$t1,1 # RUOTO t1 DI UN BIT VERSO SINISTRA
	remu $t2,$t0,2 # PRENDO L'ULTIMO BIT DI t0
	remu $t3,$t1,2 # PRENDO L'ULTIMO BIT DI t1
	beq $t2,$t3,RIPETI # SE I DUE BIT SONO UGUALI SALTA A RIPETI
	
	beq $t2,0,FINE # SALTA A FINE SE IL PRIMO BIT DI t0 E' 0
	li $t8,0 # SE E' 1, ALLORA IL PRIMO BIT DI t2 E' 0

FINE:
	move $t0,$t8 # METTO IN t0 IL  VALORE DESIDERATO
	li $v0,10 # FINE PROGRAMMA
	syscall
	
.data
a: .word 1802434
b: .word 56
