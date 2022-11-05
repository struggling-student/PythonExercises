# ----> ITALIAN <----
# Si scriva un programma in linguaggio assembly MIPS per 
# calcolare il minimo comune multiplo (MCM) di due numeri 
# interi positivi immessi da tastiera. Stampare il MCM. 
# Dati due numeri interi N1 e N2, il minimo comune multiplo
# è il più piccolo numero M che è divisibile (con resto pari 
# a zero) sia per N1 che per N2.
# Suggerimento. Si considerino due numeri interi N1 e N2. Sia
# N1 più grande di N2. Il MCM è il primo multiplo di N1 che 
# è divisibile (con resto uguale a zero) per N2.
# NB:la stampa deve avvenire da consolle output dell'emulatore MARS.

.text
.globl main
main:
	li $v0,5 					# VALORE A
	syscall					#
	move $t0,$v0				#
	li $v0,5 					# VALORE B
	syscall					#
	move $t1,$v0				#
	mul $t9,$t0,$t1 			# CALCOLO LA MOLTIPLICAZIONE TRA A E B
IF:	
	beq $t0,$t1,DO_IF 			# SE A=B ALLORA VADO NEL IF SE NO OUT IF
	j OUT_IF					# JUMP
DO_IF:
	div $t9,$t0				# DIVIDO IL RISULTATO DELLA MOLTIPLICAZIONE PER IL MCD
	mflo $t8					# SPOSTO IL QUOZIENTE IN t8
	move $a0,$t8 				# STAMPO SU CONSOLE L'MCM
	li $v0,1					#
	syscall					#
	li $v0, 10 				# CHIUDO IL PROGRAMMA
	syscall					#
OUT_IF:
WHILE:	
	bgt $t0,$t1,DO_WHILE 		# SE A > B ALLORA DO WHILE SE NO OUT WHILE
	j OUT_WHILE				# JUMP
DO_WHILE:
	sub $t4,$t0,$t1 			# A - B E POI IL RISULTATO LO SPOSTO IN t0 OVVERO IL REGISTRO DOVE HO IL VALORE DI A
	move $t0,$t4 				# A = A-B
	j WHILE					# JUMP
OUT_WHILE:
WHILE2:
	bgt $t1,$t0,DO_WHILE2 		# SE B > A ALLORA DO WHILE SE NO OUT WHILE
	j OUT_WHILE2				# JUMP
DO_WHILE2:
	sub $t5,$t1,$t0 			# B - A E POI IL RISULTATO LO SPOSTO IN t1 OVVERO IL REGISTRO DOVE HO IL VALORE DI B
	move $t1,$t5 				# B = B - A
	j WHILE2					# JUMP
OUT_WHILE2:
	j IF 					# TORNO AL IF PER CONFRONTARE SE A = B
.data
