# ----> ITALIAN <----
# Si scriva un programma in linguaggio assembly MIPS che 
# acquisisca tre numeri interi da tastiera e metta in $t0 
# del valore maggiore.

.text 
.globl main
main:
	li $v0,5 			# INPUT NUMERO 1 DA TASTIERA
	syscall			#
	move $t1,$v0		#
	li $v0,5 			# INPUT NUMERO 2 DA TASTIERA
	syscall			#
	move $t2,$v0		#
	li $v0,5 			# INPUT NUMERO 1 DA TASTIERA
	syscall			#
	move $t3,$v0		#
	move $t0,$t1  		# SPOSTO INPUT NUMERO 1 IN MAX E LO CONSIDERO TEMPORANEAMENTE COME VALORE MAX
	bgt $t2,$t1, DO_IF  # CONTROLLO SE INPUT 2 E' MAGGIORE DI INPUT 1
	j OUT_IF	    		# SE VERO ALLORA DO_IF
		  	    		# SE FALSO ALLORA OUT_IF
DO_IF:
	move $t0,$t2  		# SPOSTO INPUT 2 IN MAX E LO CONSIDERO COME IL NUOVO VALORE MAX
	bgt $t0,$t3,OUT_IF2 # SE t0 E' MAGGIORE DI t3 VADO IN OUT_IF2
	move $t0,$t3 		# SE t0 E' MINORE DI t3, SPOSTO t3 IN t0
	j OUT_IF2			# JUMP
OUT_IF:
	bgt $t3,$t1, DO_IF2 # CONTROLLO SE INPUT 3 E' MAGGIORE DI INPUT 1
	j OUT_IF2 	    	# SE VERO ALLORA DO_IF2
	                    # SE FALSO ALLORA OUT_IF2
DO_IF2:
	move $t0,$t3 		# SPOSTO INPUT 3 IN MAX E LO CONSIDERO IL VALORE MAX
OUT_IF2:
	sw $t0,massimo 	# ARCHIVIO IL VALORE MAX IN T0
	li $v0,10 		# CHIUSURA PROGRAMMA
	syscall			#
.data
massimo: .word 0
