# ----> ITALIAN <----
# Si scriva un programma in linguaggio assembly MIPS che stampa
# 1 se, in una sequenza di dieci numeri inseriti da tastiera, 
# ci sono almeno due o più numeri consecutivi uguali.
# NB:la stampa deve avvenire da consolle output dell'emulatore
# MARS. In caso di esito negativo stampare -1

.eqv CONT $t0
.eqv INCR $t2
.text
.globl main

main: 
	lw $t1, limite 		# CARICO IN t1 IL VALORE DEL LIMITE , OVVER 10. DEVO INSERIRE 10 NUMERI
	li CONT,1 			# INZIALIZZO IL CONTATORE A 1
	li INCR,1 			# INCREMENTO IL CONTATORE DI 1 AD OGNI CICLO	
	li $t6,-1 			# SETTO L'OUTPUT A -1, OVVERO CHE NON CI SONO DUE O PIU' NUMERI CONSECUTIVI UGUALI
	li $t7,2				# SETTO t7 A 2
	li $t8,0				# SETTO t8 A 0
	li $v0,5  			# INPUT NUMERO DA TASTIERA 
	syscall				#
	move $t9,$v0			#
	add CONT,CONT,INCR 		# AGGIORNO IL CONTATORE
FOR: 	
	bgt CONT,$t1,END_FOR 	# SE IL CONTATORE E' MINORE DI 10 ALLORA CONTINUO IL FOR, SE E' MAGGIORE ALLORA
			     		# ESCO DAL FOR
	li $v0,5  			# INPUT NUMERO DA TASTIERA 
	syscall				#
	move $t3,$v0			# SPOSTO IN t3 IL VALORE PRESTO DA INPUT
	beq $t3,$t9,DO_IF 		# CONTROLLO SE IL VALORE PRECEDENTE E' UGUALE AL VALORE CHE HO APPENA MESSSO
	move $t9,$t3			# SPOSTO IN t9 IL VALORE t3
	add CONT,CONT,INCR 		# AGGIORNO IL CONTATORE
	j FOR				# JUMP
DO_IF:
	add CONT,CONT,INCR 		# AGGIORNO IL CONTATORE
	addi $t8,$t8,1			# INCREMENTO t8 DI 1
	bge $t8,$t7,LOAD		# SE t8 E' MAGGIORE DI t7 VAI IN LOAD		
	move $t9,$t3			# SPOSTO IN t9 IL VALORE t3
	j FOR				# JUMP
LOAD:
	li $t6,1 				# SETTO L'OUTPUT A 1 CHE VA A DIRE CHE NELLA SEQUENZA CI SONO DUE O 
						# PIU' NUMERI CONSECUTIVI UGUALI
	move $t9,$t3			# SPOSTO IN t9 IL VALORE t3
	j FOR				# JUMP
END_FOR:
	move $a0, $t6 			# STAMPO IL VALORE CHE HO NEL INPUT 1 O -1
	li $v0,1 				# 
	syscall				#
	li $v0, 10 			# FINE PROGRAMMA
	syscall				#	
.data
limite: .word 10
