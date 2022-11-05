# ----> ITALIAN <----
# Implementare il seguente programma: $t0=1 se il valore della
# variabile Memole, definita in memoria, ha alla terza posizione
# meno significativa un 1. 

.text
.globl main

main: 
	lw $t1, memole # CARICO MEMOLE
	li $t2, 4 # CARICO 4 IN t2
	and $t3,$t1,$t2 # FACCIO L'AND BIT A BIT TRA MEMOLE E 4
	beq $t3,$t2, test # SE L'AND TORNA 4 CHIAMA TEST
	li $v0, 10 # FINE PROGRAMMA
	syscall
	
test:
	li $t0, 1 # SETTO t0 A 1
	
.data
memole: .word 12
