# ----> ITALIAN <----
# Scrivere un programma in linguaggio assembly MIPS che riceve 
# in ingresso una sequenza di N numeri interi. I numeri sono 
# memorizzati in un vettore. Il valore N è inserito dall’utente
# prima della lettura del vettore, ma il vettore può contenere
# al massimo 30 numeri. Terminato l’inserimento della sequenza
# di numeri, il programma deve verificare se il vettore 
# contiene una sequenza di numeri ordinata in modo strettamente
# crescente.
# ESEMPIO:
# INPUT 5 - 3;5;8;10;22
# OUTPUT: ORDINAMENTO STRETTAMENTE CRESCENTE
# INPUT 5 - 3;5;8;22;10
# OUTPUT: ORDINAMENTO CASUALE

.text
.globl main
main:
	la $s0, v 		# INDIRIZZO ASSOLUTO DEL VETTORE
	li $v0, 5 		# RICHIESTA DI INPUT (NUMERO)
	syscall			#
	move $t0, $v0 		# N NUMERI DA INSERIRE
	li $t1, 0 		# INIZIALIZZO IL CONTATORE A 0
while:
	bge $t1, $t0, fine 	# SE t1 E' MAGGIOR UGUALE DI t0 VAI IN fine
	li $v0, 5 		# RICHIESTA DI INPUT (NUMERO)
	syscall			#
	sw $v0, ($s0)		# CARICO IL VALORE RICEVUTO IN INPUT NEL VETTORE
	addi $s0, $s0, 4 	# INCREMENTO ALL'ELEMENTO SUCCESSIVO
	addi $t1, $t1, 1 	# INCREMENTO DI UNO
	j while 			# JUMP
fine:
	li $t1,0			# RESETTO IL REGISTRO t1 CHE USO SEMPRE COME CONTATORE
	la $s1, v 		# INDIRIZZO ASSOLUTO DEL VETTORE
	lw $t2, 0($s1) 	# PRELIEVO DEL ELEMENTO
	li $t1, 1 		# CARICO IN t1 IL VALORE 1
	addi $s1, $s1, 4 	# INCREMENTO ALL'ELEMENTO SUCCESSIVO	
while1:
	bge $t1, $t0, hulk 	# SE t1 E' MAGGIOR UGUALE DI t0 VAI IN hulk
	lw $t3, ($s1) 		# PRELIEVO DEL ELEMENTO
	bne $t2, $t3, skip 	# SE IL VALORE IN t2 NON E' UGUALE AL VALORE IN t3 VAI IN skip
skip:
	bgt $t2,$t3,batman	# SE IL VALORE IN t2 E' MAGGIORE DEL VALORE IN t3 VADO IN batman
	move $t2,$t3		# SPOSTO IL VALORE IN t3 IN t2 COSI LO POSSO USARE PER IL PROSSIMO CONFRONTO
	addi $s1, $s1, 4 	# INCREMENTO ALL'ELEMENTO SUCCESSIVO
	addi $t1, $t1, 1 	# INCREMENTO DI UNO
	j while1			# JUMP
hulk:
	la $a0,output1		# STAMPO SU CONSOLE IL MESSAGGIO SALVATO IN output1
	li $v0,4			#
	syscall			#
	li $v0, 10 		# FINE PROGRAMMA
	syscall			#
batman:
	la $a0,output2		# STAMPO SU CONSOLE IL MESSAGGIO SALVATO IN output2
	li $v0,4			#
	syscall			#
	li $v0, 10 		# FINE PROGRAMMA
	syscall			#
.data
output1: .asciiz "ORDINAMENTO STRETTAMENTE CRESCENTE"
output2: .asciiz "ORDINAMENTO CASUALE"
v: .word 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
