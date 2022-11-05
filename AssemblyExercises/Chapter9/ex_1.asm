# ----> ITALIAN <----
# Scrivere un programma che inizializza un vettore di 10 
# elementi a 16bit con valori casuali compresi tra 0 e 65000 e 
# che copia in un nuovo vettore il quadrato degli elementi del 
# primo (utilizzare una funziona per realizzare il quadrato 
# degli elementi).
# ESEMPIO:
# v1= 5,60000,0,1,45,76,99,456,4321,12876
# v2= 25,3600000000,0,1,2025,5776,9801,207936,18671041,165791376

.macro spazio
	la $a0,newLine		# STAMPA SPAZIO
	li $v0,4			#
	syscall			#
.end_macro 

.text
.globl main
main:
	la $s0,v
	li $t0,10
while:
	bge $t1, $t0, fine2
	li $v0, 42  			# 42 is system call code to generate random int
	li $a1, 46000			# $a1 is where you set the upper bound
	syscall     			# your generated number will be at $a0
	sw $a0, ($s0)
	addi $s0, $s0, 4
	addi $t1, $t1, 1
	j while

fine2:
	move $a0,$s0
	move $a1,$t0
	jal POTENZA
	li $t0,10
	move $s1,$v0
	la $s1, v1
	lw $t1, 0($s1)
	spazio
	move $a0,$t1 		# STAMPA SU CONSOLE IL VALORE IN t5
	li $v0,1 			#
	syscall	
	spazio
	addi $s1,$s1,4
	li $t9,1
	
circo:
	bge $t9,$t0,end
	lw $t2, ($s1)
	move $a0,$t2 		# STAMPA SU CONSOLE IL VALORE IN t5
	li $v0,1 			#
	syscall	
	spazio
	addi $s1,$s1,4
	addi $t9,$t9,1
	j circo
end:
	li $v0, 10 		# FINE PROGRAMMA
	syscall
POTENZA:
	move $s0, $a0
	move $t3, $a1
	la $s0,v	
	la $s1,v1
	lw $t1, 0($s0)
	move $a0,$t1 		# STAMPA SU CONSOLE IL VALORE IN t5
	li $v0,1 			#
	syscall	
	spazio
	mulou $t2,$t1,$t1
	sw $t2,($s1)
	addi $s1,$s1,4
	li $t0,1
	addi $s0,$s0,4
while1:
	bge $t0,$t3,fine
	lw $t4, ($s0)
	move $a0,$t4 		# STAMPA SU CONSOLE IL VALORE IN t5
	li $v0,1 			#
	syscall	
	spazio
	mulou $t5,$t4,$t4
	sw $t5, ($s1)
	addi $s1,$s1,4
	addi $t0,$t0,1
	addi $s0,$s0,4
	j while1

fine:
	move $v0,$s1
	jr $ra
.data
v: .space 10000
v1: .space 10000
newLine: .asciiz "\n"
