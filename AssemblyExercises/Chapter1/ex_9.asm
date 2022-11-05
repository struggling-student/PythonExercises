# ----> ITALIAN <----
# Si scriva un programma in linguaggio assembly MIPS per il 
# calcolo dei quadrati perfetti per una sequenza di numeri. 
# Il programma deve prima leggere un numero inserito da 
# tastiera, e quindi stampare i primi quadrati perfetti sino 
# al quadrato del numero.
# ES:
# INPUT=5
# OUTPUT=1,4,9,16,25

.eqv CONT $t0 
.eqv INCR $t2

.text
.globl main 
main:	
	li $v0,5 # INPUT NUMERO 1 DA TASTIERA 
	syscall
	move $t3,$v0
	
	li CONT,1 # INZIALIZZAZIONE DEL CONTATORE
	lw $t1, limite # CARICO IN t1 IL VALORE 0 DEL LIMITE
	lw $t4, hulk # CARICO In t4 IL VALORE 1 DI HULK
	add $t6,$t1,$t3 # SOMMO IL LIMITE E L'INPUT, COSI HO IL LIMITE IN t6
	li INCR, 1 # ASSEGNAZIONE DEL PASSO DI INCREMENTO
	
FOR: bgt CONT,$t6,END_FOR # IL FOR HA COME INZIALIZZAZIONE DEL CONTATORE A 1, LA CONDIZIONE MAGGIORE DEL LIMITE E 
			  # L'INCREMENTO DEL CONTATORE DI 1 AD OGNI CICLO

	la $a0, newLine # SERVER PER DARE ORDINE IN OUTPUT
	addi $v0,$0, 4
	syscall
	
	mul $t5,$t4,$t4 # MOLTIPLICO HULK PER SE STESSO COSI HO IL QUADRATO
	move $a0, $t5 # SPOSTO IL VALORE DELLA MOLTIPLICAZIONE in a0
	li $v0,1 # STAMPO IL RISULTATO DELLA MOLTIPLICAZIONE
	syscall
	
	add $t4, $t4,1 # SOMMO AD HULK 1 
	
	add CONT, CONT, INCR # INCREMENTO IL CONTATORE DI UNO
	j FOR # JUMP PER TORNARE AL FOR E RICOMINCIARE IL FOR SE POSSIBILE


END_FOR:
	li $v0, 10 # FINE DEL PROGRAMMA
	syscall
	
	
	
.data
limite: .word 0
hulk: .word 1
newLine: .asciiz "\n"
