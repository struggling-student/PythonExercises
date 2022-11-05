# ----> ITALIAN <----
# Un programma in linguaggio assembly MIPS deve leggere 
# dall’utente due vettori di 5 numeri interi ciascuno. 
# Il programma deve creare un ulteriore vettore, che contenga 
# la copia dei soli elementi pari presenti nei due vettori di 
# partenza, e stampare tale vettore.

.macro spazio
	la $a0,newLine		# STAMPA SPAZIO
	li $v0,4			#
	syscall			#
.end_macro 
.macro stampa
	move $a0,$t5 		# STAMPA SU CONSOLE IL VALORE IN t5
	li $v0,1 			#
	syscall			#
.end_macro 
.macro fine_programma
	li $v0, 10 		# FINE PROGRAMMA
	syscall
.end_macro 
.macro richiesta_input
	li $v0, 5 		# RICHIESTA DI INPUT (NUMERO)
	syscall
.end_macro 
.text
.globl main
main:
	la $s0, v1 		# INDIRIZZO ASSOLUTO DEL VETTORE 1
	la $s1, v2 		# INDIRIZZO ASSOLUTO DEL VETTORE 2
	la $s2, v3 		# INDIRIZZO ASSOLUTO DEL VETTORE 3
	li $t0, 10 		# INSERIAMO UN TOTALE DI 10 NUMERI, 5 PER IL VETTORE 1 E 5 PER IL VETTORE 2
	li $t1, 0  		# INIZIALIZZO IL CONTATORE A 0
	li $t6, 0           # INIZIALIZZO IL CONTATORE PER I NUMERI PARI A 0
	li $t9, 2           # IL VALORE DUE LO USO PER DIVIDERE I NUMERI E VERIFICARE SE SONO PARI
ciclo1: 
	bge $t1, $t0, fine  # SE IL VALORE IN t1 E' MAGGIORE O UGUALE DEL VALORE IN t0 SALTA IN fine
	richiesta_input
	sw $v0, ($s0)		# CARICO IL VALORE RICEVUTO IN INPUT NEL VETTORE
	addi $s0, $s0, 4 	# INCREMENTO ALL'ELEMENTO SUCCESSIVO
	addi $t1, $t1, 1 	# INCREMENTO DI UNO
	richiesta_input
	sw $v0, ($s0)		# CARICO IL VALORE RICEVUTO IN INPUT NEL VETTORE
	addi $s0, $s0, 4	# INCREMENTO ALL'ELEMENTO SUCCESSIVO
	addi $t1, $t1, 1 	# INCREMENTO DI UNO
	j ciclo1			# JUMP
fine:
	la $s0, v1 		# INDIRIZZO ASSOLUTO DEL VETTORE
	lw $t2, 0($s0) 	# PRELIEVO DEL ELEMENTO
	la $s1, v2 		# INDIRIZZO ASSOLUTO DEL VETTORE
	lw $t3, 0($s1)		# PRELIEVO DEL ELEMENTO
	div $t2, $t9        # DIVIDO IL VALORE IN t2 PER DUE
	mfhi $t8            # SPOSTO IL RESTO NEL REGISTRO t8
	div $t3, $t9        # DIVIDO IL VALORE IN t2 PER DUE
	mfhi $t7            # SPOSTO IL RESTO NEL REGISTRO t7
	li $t1,0            # CARICO IN t1 IL VALORE 0 PER RESETTARLO
	j check			# JUMP
ciclo2:
	bge $t1, $t0, print	# SE t1 E' MAGGIOR UGUALE DI t0 SALTA IN print
	addi $s0, $s0, 4 	# INCREMENTO ALL'ELEMENTO SUCCESSIVO
	addi $s1, $s1, 4 	# INCREMENTO ALL'ELEMENTO SUCCESSIVO
	lw $t2, ($s0) 		# PRELIEVO DEL ELEMENTO
	lw $t3, ($s1) 		# PRELIEVO DEL ELEMENTO
	div $t2, $t9		# DIVIDO IL VALORE IN t2 PER DUE
	mfhi $t8			# SPOSTO IL RESTO NEL REGISTRO t7
	div $t3, $t9		# DIVIDO IL VALORE IN t3 PER DUE
	mfhi $t7			# SPOSTO IL RESTO NEL REGISTRO t8
	j check			# JUMP
check:
	beqz $t8, save1	# SE IL VALORE IN t8 E' UGUALE A 0 SALTA IN save1
	beqz $t7, save2	# SE IL VALORE IN t8 E' UGUALE A 0 SALTA IN save2
	addi $t1, $t1, 1 	# AUMENTO IL CONTATORE DI UNO
	addi $t1, $t1, 1 	# AUMENTO IL CONTATORE DI UNO
	j ciclo2			# JUMP
save1:
	sw $t2, ($s2)		# SALVO IL VALORE CHE HO IN t2 NEL VETTORE v3
	addi $s2, $s2, 4	# INCREMENTO ALL'ELEMENTO SUCCESSIVO
	addi $t6, $t6, 1	# AUMENTO IL CONTATORE DEI NUMERI PARI DI UNO
	li $t8,1			# SETTO t8 A 1 
	j check
save2:
	sw $t3, ($s2)		# SALVO IL VALORE CHE HO IN t3 NEL VETTORE v3
	addi $s2, $s2, 4	# INCREMENTO ALL'ELEMENTO SUCCESSIVO
	addi $t6, $t6, 1	# AUMENTO IL CONTATORE DEI NUMERI PARI DI UNO
	li $t7,1			# SETTO t7 A 1 
	j check			# JUMP
print:
	la $s2, v3		# INDIRIZZO ASSOLUTO DEL VETTORE
	lw $t5, 0($s2)		# PRELIEVO DEL ELEMENTO
	stampa
	spazio
	li $t1, 1 		# CARICO IN t1 IL VALORE 1
	addi $s2,$s2, 4 	# INCREMENTO ALL'ELEMENTO SUCCESSIVO
ciclo3:				
	bge $t1,$t6,end 	# SE IL VALORE IN t2 E' MAGGIORE DEL VALORE IN t6 SALTO IN end
	lw $t5, ($s2)	     # PRELIEVO DEL ELEMENTO
	stampa
	spazio
	addi $s2,$s2, 4	# INCREMENTO ALL'ELEMENTO SUCCESSIVO
	addi $t1,$t1, 1	# AUMENTO IL CONTATORE DI UNO
	j ciclo3			# JUMP
end:
	fine_programma
.data
v1: .word 0, 0, 0, 0, 0
v2: .word 0, 0, 0, 0, 0
v3: .word 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
newLine: .asciiz "\t"
