# ----> ITALIAN <----
# Definita una matrice in memoria di 4 righe e 3 colonne
# A_{4x3} con elementi word, stampare in output la matrice 
# trasposta A^{t}_{3*4^{'}}.  La matrice trasposta A^t è 
# costituita dagli elementi alla posizione inversa della 
# matrice originale A: cioè A(a_{i,j}) si trova in A^{t}(a_{i;j}).
# ESEMPIO:
# A
# 12 74 06 07
# 99 10 11 16
# 00 03 20 21
# A^t
# 12 99 00
# 74 10 03
# 06 11 20
# 07 16 21

.text
.globl main
main:
	li $t0, 1				# CARICO IL VALORE 1 IN t0
	li $t1, 1				# CARICO IL VALORE 1 IN t1
	lb $t2, R				# CARICO IL NUMERO DELLE RIGHE
	lb $t3, C				# CARICO IL NUMERO DELLE COLONNE
	la $a0, prima			# STAMPA SU CONSOLE IL TESTO SALVATO IN prima
	li $v0, 4				#
	syscall				#
before:
	sub $t7, $t0, 1		#	(r-1)
	sub $t8, $t1, 1		#	(c-1)
	mul $t4, $t3, $t7 		#	C(r-1)
	add $t5, $t4, $t8		#	C(r-1)+(c-1)
	lb $t6, matrice($t5)	# CARICO L'ELEMENTO DELLA MATRICE IN t6
	move $a0, $t6			# STAMPO SU CONSOLE IL VALORE IN t6
	li $v0, 1				#
	syscall				#
	la $a0, tabulato		# STAMPA SU CONSOLE IL TABULATO
	li $v0, 4				#
	syscall				#
	add $t1, $t1, 1		# INCREMENTO t1 DI 1
	ble $t1, $t3, before	# SE t1 E' MINORE O UGUALE A te VA IN before
	li $t1, 1				# SETTO t1 A 1
	add $t0, $t0, 1		# INCREMENTO t0 DI 1
	la $a0, riga			# STAMPA SU CONSOLE LA RIGA
	li $v0, 4				#
	syscall				#
	ble $t0, $t2, before	# SE t0 E' MINORE O UGUALE A t2 VA IN before
	la $a0, riga			# STAMPA SU CONSOLE LA RIGA
	li $v0, 4 			#
	syscall				#
	la $a0, dopo			# STAMPO SU CONSOLE IL TESTO SALVATO IN dopo
	li $v0, 4				#
	syscall				#
	li $t0, 1				# CARICO IL VALORE 1 IN t0
	li $t1, 1				# CARICO IL VALORE 1 IN t1
	lb $t2, R				# CARICO IL NUMERO DELLE RIGHE
	lb $t3, C				# CARICO IL NUMERO DELLE COLONNE
	
# DA QUESTO PUNTO, DOPO OGNI ITERAZIONE, INVECE DI AUMENTARE LA COLONNA SI AUMENTA LA RIGA PER PRIMA.	
after:
	sub $t7, $t0, 1		#	(r-1)
	sub $t8, $t1, 1		#	(c-1)
	mul $t4, $t3, $t7 		#	C(r-1)
	add $t5, $t4, $t8		#	C(r-1)+(c-1)
	lb $t6, matrice($t5)	# CARICO L'ELEMENTO DELLA MATRICE IN t6
	move $a0, $t6			# STAMPO SU CONSOLE IL VALORE IN t6
	li $v0, 1				#
	syscall				#
	la $a0, tabulato		# STAMPA SU CONSOLE IL TABULATO
	li $v0, 4				#
	syscall				#
	add $t0, $t0, 1		# INCREMENTO t0 DI 1
	ble $t0, $t2, after		# SE IL VALORE IN t0 E' MINORE UGUALE DEL VALORE IN T2 VA IN AFTER
	li $t0, 1				# SETTO t0 A 1
	add $t1, $t1, 1		# INCREMENTO t1 DI 1
	la $a0, riga			# STAMPA SU CONSOLE LA RIGA
	li $v0, 4				#
	syscall				#
	ble $t1, $t3, after		# SE IL VALORE IN t2 E' MINORE UGUALE DEL VALORE IN t3 VA IN AFTER
	li $v0, 10			# FINE PROGRAMMA
	syscall				#
.data
prima: .asciiz "La matrice prima:\n"
dopo:  .asciiz "La matrice dopo:\n"
tabulato: .asciiz "\t"
riga: .asciiz "\n"
matrice: .byte 12,74,06,07,99,10,11,16,00,03,20,21
R: .byte 3
C: .byte 4
