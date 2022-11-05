# ----> ITALIAN <----
# Creare una funzione SUBFMAX(int val1, int val2) che ricevuti 
# due valori sottrae al maggiore metà del valore del minore e 
# divida per tre il minore.
# Creare una programma che applica tre volte la funzione a 
# valori inseriti dall’utente.
# ESEMPIO:
# x=30;
# y=56;
# SUBFMAN(x,y); #dopo l'esecuzione: x=10 y=41
# SUBFMAN(x,y); #dopo l'esecuzione: x=3 y=36
# SUBFMAN(x,y); #dopo l'esecuzione: x=1 y=35
# PRINT(x); stampa 1
# PRINT(y); stampa 35

.macro spazio
	la $a0,newLine		# STAMPA SPAZIO
	li $v0,4			#
	syscall			#
.end_macro 
.text
.globl main

main:
	la $a0, x
	la $a1, y
	jal SUBFMAN

	jal SUBFMAN
	
	jal SUBFMAN
	
	move $t0,$v0
	move $t1,$v1
	
	move $a0,$t0 		# STAMPA SU CONSOLE IL VALORE IN t5
	li $v0,1 			#
	syscall			#
	spazio
	move $a0,$t1		# STAMPA SU CONSOLE IL VALORE IN t5
	li $v0,1 			#
	syscall			#
	
	
	li $v0,10
	syscall

SUBFMAN:	
	lw $t0,($a0) # 30 x
	lw $t1,($a1) # 56 y
	li $t5,3
	li $t9,2
	bge $t0,$t1,hulk
	div $t0,$t9 		# x / 2
	mflo $t8 			# x/2 = 15
	sub $t7,$t1,$t8     # y = y - (x/2) = 56 - 15
	
	div $t0,$t5		# x / 3
	mflo $t6			# x = 10
	j fine
hulk:
	div $t1,$t9
	mflo $t8
	sub $t7,$t0,$t8
	
	div $t1,$t8
	mflo $t6
	j fine
	
fine:
	sw $t6,($a0) # x 
	sw $t7,($a1) # y
	move $v0,$t6 # x
	move $v1,$t7 # y
	jr $ra
	
.data
x: .word 30
y: .word 56
newLine: .asciiz "\n"
