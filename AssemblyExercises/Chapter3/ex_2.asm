# ----> ITALIAN <----
# Implementare un programma in linguaggio assembly MIPS che 
# legga da input un intero positivo $a>2(word) ed un 
# intero positivo $b>1(word) e ne restituisca in output 
# il prodotto a*b. senza utilizzare l'istruzione mul.
# Esempio:
# INPUT (a): 10
# INPUT (b): 5
# OUTPUT: 50

.eqv CONT $t0 
.eqv INCR $t1

.text
.globl main
main:
	li CONT,0 # INIZIALIZZO IL CONTATORE A 0
	li INCR,1 # INCREMENTO DI UNO AD OGNI CICLO
	li $t8,0 # INZIALIZZO IL REGISTRO t8 A 0
	
	li $v0,5 # INPUT NUMERO A
	syscall
	move $t2,$v0
	
	li $v0,5 # INPUT NUMERO B
	syscall
	move $t3,$v0
	
FOR: bge CONT,$t3,END_FOR # SE IL CONTATORE E' MAGGIORE O UGUAL DEL INPUT NUMERO B ALLORA END FOR

	add $t4,$t8,$t2 # SOMMO IL VALORE CHE HO NEL REGISTRO t8 AL VALORE CHE HO NEL REGISTRO t2
	move $t8,$t4 # SPOSTO IL RISULTATO DELLA SOMMA in t8
	add CONT,CONT,INCR # INCREMENTO DI UNO IL CONTATORE
	j FOR # JUMP
	
END_FOR:
	move $a0,$t4 # PRINTA SU CONSOLE
	li $v0,1
	syscall
	
	li $v0,10 # CHIUSURA DEL PROGRAMMA
	syscall	

.data
