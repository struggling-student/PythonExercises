# ----> ITALIAN <----
# Inizializzare, con valori casuali, un vettore di dimensione
# 10 con elementi word e realizzare la funzione
# INS(vettore, DIM, ELEM, POS)
# che inserisce l'elemento ELEM (immesso da tastiera) 
# alla posizione POS (immessa da tastiera) slittando a destra
#  gli elementi successivi alla posizione di inserimento
# ESEMPIO:
# v1=555,6,710,33,6071,789,5,-67,99,1000
# lunghezzav1=10
# INS(v1,10,2312,6)
# v1=555,6,710,33,6071,2312,789,5,-67,99,1000
# lunghezzav1=11
# PS: per evitare la gestione del caso in cui l'utente 
# inserisca una posizione al di fuori dal range [0,9] si 
# consiglia di stamapre su videoterminale un segnale di 
# avvertimento

.text
.globl main
main:
	la $s0,v1
	li $t0,10
	
	li $v0, 42  			# 42 is system call code to generate random int
	li $a1, 30			# $a1 is where you set the upper bound
	syscall     			# your generated number will be at $a0
	sw $a0, 0($s0)
	addi $s0, $s0, 4
	li $t1,1
while:
	bge $t1, $t0, fine2
	li $v0, 42  			
	li $a1, 30			
	syscall     	
	sw $a0, ($s0)
	addi $s0, $s0, 4
	addi $t1, $t1, 1
	j while
fine2:
	li $v0,5			# RICHIESTA ELEMENTO
	syscall			#
	move $a3,$v0		# SPOSTO IN VALORE NEL REGISTRO PRESERVANTE a0
	
	li $v0,5			# RICHIESTA POSIZIONE
	syscall			#
	move $a2,$v0		# SPOSTO IN VALORE NEL REGISTRO PRESERVANTE a0
	
	move $a0,$s0
	move $a1,$t0
	jal FUNZIONE
	
FUNZIONE:	# 3 2 5 3 5   
		# 2 6 7 8 5
		
		# 4 3 2 5 3   
		# 5 2 6 7 8 5
	move $s0,$a0
	move $t0,$a1
	move $t1,$a2 # POSIZIONE
	move $t2,$a3 # ELEMENTO
	la $s0,v1
	li $t3,0
	li $t9,11
	bne $t1,$t3,cicloNormale
	
	lw $t4, 0($s0) # PRENDO 3
	addi $t3,$t3,1 
	sw $t2, 0($s0) # CARICO ELEMEMENTO
	addi $s0,$s0,4 # INCREMENTO POSIZIONE 1

	lw $t5, ($s0) # PRENDO 2 
	sw $t4, ($s0) # CARICO 3
	addi $s0,$s0,4 # INCREMENTO POSIZIONE 2
	addi $t3,$t3,1
	lw $t6, ($s0) # PRENDO 5
	sw $t4, ($s0) # CARICO 2
	addi $s0,$s0,4
	srl 
	                                                       j cicloPostZero
cicloPostZero:
	lw $t7, ($s0) # PRENDO 3
	sw $t6, ($s0) # CARICO 5
	
hulk:
	bge $t3,$t9,fine
	addi $s0,$s0,4
	sw $t4, 0($s0)
	addi $t3,$t3,1
	addi $s0,$s0,4
	lw $t7, ($s0)
	addi $t3,$t3,1
	sw $t6, 0($s0)
	addi $s0,$s0,4
	j cicloPostZero
	
cicloNormale:

fine:
	li $v0, 10 		# FINE PROGRAMMA
	syscall

.data
v1: .word 0,0,0,0,0,0,0,0,0,0,0
