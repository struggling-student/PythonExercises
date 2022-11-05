# ----> ITALIAN <----
# Creare una funzione che ricevuti tre importi di denaro 
# sposta gli eventuali debiti (si considerino debiti gli
# importi negativi) sul primo importo STOCK(int a, int b, int c).
# Creare un main per testare la funzione:
# ESEMPIO
# X=5;
# Y=-1;
# Z=-2;
# STOCK (X,Y,Z);
# Print(X); stampa 2
# Print(Y); stampa 0
# Print(Z); stampa 0

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
	la $a2, z
	jal STOCK
	move $t0,$v0
	move $t1,$v1
	
	move $a0,$t0 		# STAMPA SU CONSOLE IL VALORE IN t5
	li $v0,1 			#
	syscall			#
	spazio
	move $a0,$t1		# STAMPA SU CONSOLE IL VALORE IN t5
	li $v0,1 			#
	syscall			#
	spazio
	move $a0,$t1		# STAMPA SU CONSOLE IL VALORE IN t5
	li $v0,1 			#
	syscall			#
	
	
	li $v0,10
	syscall
STOCK:
	lw $t0,($a0) # x
	lw $t1,($a1) # y
	lw $t2,($a2) # z

check:	
	bltz $t1,debito1
	bltz $t2,debito2
debito1:
	add $t3,$t0,$t1
	li $t9,0	
	li $t1,1
	j check
debito2:
	add $t3,$t3,$t2
	li $t1,1
	li $t9,0	
	j fine
fine:
	sw $t3,($a0) 
	sw $t9,($a1)
	move $v0,$t3 # x
	move $v1,$t9
	jr $ra 
	
.data
x: .word 500
y: .word -127
z: .word -232
newLine: .asciiz "\n"
