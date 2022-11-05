# ----> ITALIAN <----
# Si scriva un programma in linguaggio assembly MIPS che legga 
# da tastiera i valori delle lunghezze dei tre lati di un 
# triangolo e determina:
# se il triangolo è scaleno (porre $t0=0)
# se il triangolo è rettangolo (porre $t0=1)
# se il triangolo è isoscele (porre $t0=2)
# se il triangolo è equilatero (porre $t0=3)
# NB: non è necessario usare la radice quadra né i numeri in
# virgola mobile

.text
.globl main
main:
	la $a0, base 			# STAMPO SU CONSOLE IL TESTO SALVATO IN base
	li $v0, 4 			#
	syscall				#
	
	li $v0, 5				# CHIEDO IN INPUT UN INTERO
	syscall				#
	move $t0, $v0			# SPOSTO IN t0 IL VALORE IN v0
						# LATO 1
	la $a0, l1    			# STAMPO SU CONSOLE IL TESTO SALVATO in 11
	li $v0, 4				#
	syscall				#
	
	li $v0, 5				# CHIEDO IN INPUT UN INTERO
	syscall				#
	move $t1, $v0			# SPOSTO IN t1 IL VALORE IN v0
	
						# LATO 2
	la $a0, base    		# STAMPO SU CONSOLE IL TESTO SALVATO IN base
	li $v0, 4				#
	syscall				#
	
	li $v0, 5				# CHIEDO IN INPUT UN INTERO
	syscall				#
	move $t2, $v0			# SPOSTO IN t2 IL VALORE IN v0 
	
	bne $t0, $t1, check		# SE LA BASE E 11 SONO DIFFERENTI
	j check2				# JUMP
check:
	beq $t0, $t2, isosceles 	# SE 11 E 11 SONO DIFFERENTI
	bne $t1, $t2, scalene	# SE IL VALORE IN t1 NON E' UGUALE AL VALORE IN t2 VAI IN SCALENE
	j isosceles			# JUMP
check2:
	beq $t1, $t2, equilater 	# SE IL VALORE IN t1 E' UGUALE AL VALORE IN t2 VAI IN equilater
	j isosceles			# JUMP
scalene:
	la $a0, pSca			# STAMPA SU CONSOLE IL MESSAGGIO SALVATO IN pSCA
	li $v0, 4				#
	syscall				#
	
	li $v0, 4				# STAMPA SPAZIO
	la $a0, enter			# 
	syscall				#
	j ipotenusa			# JUMP
isosceles:
	la $a0, pIso			# STAMPO SU CONSOLE IL MESSAGGIO SALVATO IN pIso
	li $v0, 4				#
	syscall 				#
	j ipotenusa			# JUMP
	
equilater:	
	la $a0, pEqu			# STAMPA SU CONSOLE IL MESSAGGIO SALVATO IN pEqu
	li $v0, 4				#
	syscall				#
	j finish				# JUMP
ipotenusa:
	bgt $t0, $t1, ironman	# SE IL VALORE IN t0 E' MAGGIORE DEL VALORE IN t1 VAI IN ironman		
	j al					# JUMP
ironman:		
	bgt $t0, $t2, do		# SE IL VALORE IN t0 E' MAGGIORE DEL VALORE IN t2 VAI IN d0
do:
	mul $t8, $t0, $t0  		# A ALLA SECONDA
	mul $t4, $t1, $t1  		# B ALLA SECONDA
	mul $t5, $t2, $t2    	# C ALLA SECONDA
	add $t3, $t4, $t5  		# B ALLA SECONDA + C ALLA SECONDA
	beq $t8, $t3, checkRect	# SE IL VALORE IN t8 E' UGUALE AL VALORE IN t3 VAI IN checkRect
	j finish				# JUMP
al:	
	bgt $t1, $t2, lf		# SE IL VALORE IN t2 E' MAGGIORE DEL VALORE IN t2 VAI IN lf
	j bl					# JUMP
lf:		
	bgt $t1, $t0, di		# SE IL VALORE IN t1 E' MAGGIORE DEL VALORE IN t0 VAI IN di
di:
	mul $t8, $t1, $t1  		# B ALLA SECONDA
	mul $t4, $t0, $t0  		# A ALLA SECONDA
	mul $t5, $t2, $t2  		# C ALLA SECONDA
	add $t3, $t4, $t5  		# A ALLA SECONDA + C ALLA SECONDA
	beq $t8, $t3, checkRect	# SE IL VALORE IN t8 E' UGUALE A QUELLO IN t3 VAI IN checkRect
	j finish				# JUMP
bl:
	bgt $t2, $t0, hulk		# SE IL VALORE IN T2 E' MAGGIORE DEL VALORE IN t0 VAI IN hulk
	j finish				# JUMP
hulk:
	bgt $t2, $t1, du		# SE IL VALORE IN t2 E' MAGGIORE DEL VALORE IN t2 VAI IN du
du:
	mul $t8, $t2, $t2  		# C ALLA SECONDA
	mul $t4, $t0, $t0  		# A ALLA SECONDA
	mul $t5, $t1, $t1 		# B ALLA SECONDA
	add $t3, $t4, $t5		# A ALLA SECONDA + B ALLA SECONDA
	beq $t8, $t3, checkRect  # SE IL VALORE IN t8 E' UGUALE A QUELLO IN t3 VAI IN checkRect
	j finish				# JUMP
checkRect:
	la $a0, pRet			# STAMPA SU CONSOLE IL MESSAGGIO IN pRET
	li $v0, 4				#
	syscall				#
	j finish				# JUMP
finish:
	li $v0, 10			# FINE PROGRAMMA
	syscall				#
.data
base: .asciiz "Enter base value: "
l1: .asciiz "Enter l1 value: "
l2: .asciiz "Enter l2 value: "
buffer: .space 4
enter:.asciiz "\n"
pSca:.asciiz "The triangle is scalene"
pIso:.asciiz "The triangle is isosceles"	
pEqu:.asciiz "The triangle is equilater"
pRet:.asciiz "The triangle is rectangle"
