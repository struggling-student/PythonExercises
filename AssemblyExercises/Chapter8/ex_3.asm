# ----> ITALIAN <----
# Si scriva un programma in linguaggio assembly MIPS che 
# mediante la subroutine ORDINA ordina un vettore immesso
# da input. La routine ORDINA ha come argomento il vettore 
# (cioè l'indirizzo del vettore), e restituisce il vettore 
# ordinato (l'indrizzo del vettore, con gli elementi ordinati).
# Ad esempio
# v=(1,10,6,3,2,4)
# ORDINA(v)=(1,2,3,4,6,10)

.macro spazio
	la $a0,newLine		# STAMPA SPAZIO
	li $v0,4			#
	syscall			#
.end_macro 
.macro stampa
	move $a0,$t9 		# STAMPA SU CONSOLE IL VALORE IN t5
	li $v0,1 			#
	syscall			#
.end_macro 
.macro stampa2
	move $a0,$t8		# STAMPA SU CONSOLE IL VALORE IN t5
	li $v0,1 			#
	syscall			#
.end_macro 
.macro fine_programma
	li $v0, 10 		# FINE PROGRAMMA
	syscall
.end_macro
.text
.globl main

main:
	la $s0,v
	li $v0,5
	syscall
	move $t0, $v0
	li $t1, 0
while:
	bge $t1, $t0, fine2
	li $v0, 5
	syscall
	sw $v0, ($s0)
	addi $s0, $s0, 4
	addi $t1, $t1, 1
	j while
fine2: 
	move $a0,$t0
	move $a1,$s0
	jal ORDINA
##############################################	
	move $t7,$v1
	move $s0,$v0
	la $s0,v
	lw $t9, 0($s0)
	stampa
	spazio
	li $t1, 1
	addi $s0,$s0,4
print:
	bge $t1,$t7,end
	lw $t8, ($s0)
	stampa2
	spazio
	addi $s0,$s0,4
	addi $t1, $t1, 1
	j print
end:
	fine_programma
##############################################	
ORDINA: 
	move $t0, $a0
	move $s0, $a1
	li $t9,0
	li $t6, 0
	la $s0,v
	lw $t1, 0($s0)
	li $t6, 1
	addi $s0,$s0,4
while1:
	bge $t6, $t0, fine
	lw $t2, ($s0)
	bgt $t1,$t2,swap
	move $t1,$t2
	addi $s0,$s0,4
	addi $t6, $t6, 1
	j while1
swap:
	sw $t2, -4($s0)  
	sw $t1, 0($s0) 
	addi $s0,$s0,4
	addi $t6, $t6, 1
		addi $t9, $t9, 1
	j while1
fine:
	beqz $t9,fine3
	j ORDINA
fine3:
	move $v0,$s0
	move $v1,$t6
	jr $ra	
	
.data
v: .space 1000
newLine: .asciiz "\t"
