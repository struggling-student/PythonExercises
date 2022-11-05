# ----> ITALIAN <----
# Si scriva un programma in linguaggio assembly MIPS che legge
# due stringhe da tastiera e al suo interno usa una subroutine,
# denominata SIMILITUDINE, che valuta quanti caratteri alle
# stesse posizioni delle due stringhe sono uguali.
# La routine riceve due parametri, "le stringhe" (cioè gli 
# indirizzi delle stringhe), e restituisce un numero
# intero e lo stampa a video.
# Ad esempio:
# - SIMILITUDINE ("ciao", "cielo") restituisce 2 in quanto i 
# primi due caratteri sono identici.
# - SIMILITUDINE("ciao", "salve") restituisce 0 in quanto 
# nessun carattere alle stesse posizioni sono uguali.

.text
.globl main
main:
	li $v0, 8 #read a string into a0
	la $a0, txt1
	move $a1, $a0
	syscall
	li $v0, 8 #read a string into a0
	la $a0, txt2
	syscall
	

	jal SIMILITUDINE
	
	move $t9,$v0
	move $a0,$t9
	li $v0,1
	syscall
	li $v0, 10 		# FINE PROGRAMMA
	syscall
SIMILITUDINE:
	li $t0,0
	li $t2,0
	li $t5, 0
CICLO:
	lb $t1, txt1($t0)
	lb $t3, txt2($t2)
	beq $t1,0,secondo
secondo:
	beq $t3,0,FINE
	beq $t1,$t3,hulk
	addi $t0,$t0,1
	addi $t2,$t2,1
	j CICLO
hulk:
	addi $t5,$t5,1
	addi $t0,$t0,1
	addi $t2,$t2,1
	j CICLO
	
FINE:
	move $v0,$t5
	jr $ra
.data
txt1: .space 200
txt2: .space 200
