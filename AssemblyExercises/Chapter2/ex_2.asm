# ----> ITALIAN <----
# Implementare un programma in linguaggio assembly MIPS che 
# legga da input un intero positivo *dividendo* (word) ed un 
# intero positivo (word) *divisore* e restituisca in output 
# il quoziente e resto della divisione a/b.
# Esempio
# INPUT (dividendo): 56
# INPUT (divisore): 23
# OUTPUT: Quoziente: 2 Resto:10

.text
.globl main
main:
	li $v0,5 # INPUT NUMERO 1 DA TASTIERA 
	syscall
	move $t0,$v0
	
	li $v0,5 # INPUT NUMERO 2 DA TASTIERA 
	syscall
	move $t1,$v0
	
	div $t0,$t1 # DIVISIONE TRA NUMERO 1 E NUMERO 2	  

	mfhi $t2 # SPOSTO IL RESTO IN t2
	mflo $t3 # SPOSTO IL QUOZIENTE IN t3
	
	la $a0,mex1 # SRIVO SU CONSOLE IL MESSAGGIO QUOZIENTE:
	li $v0,4
	syscall 
	
	move $a0,$t3 # SPOSTO IL RISULTATO DELLA MOLTIPLICAZIONE DA t2 in a0
	li $v0,1 # STAMPO A VIDEO IL RISULTATO
	syscall
	
	
	la $a0,mex2 # SRIVO SU CONSOLE IL MESSAGGIO RESTO:
	li $v0,4
	syscall 
	
	
	move $a0,$t2 # SPOSTO IL RISULTATO DELLA MOLTIPLICAZIONE DA t2 in a0
	li $v0,1 # STAMPO A VIDEO IL RISULTATO
	syscall
	
	li $v0, 10 # FINE DEL PROGRAMMA
	syscall
.data
mex1: .asciiz "\nQuoziente:"
mex2: .asciiz "\nResto
