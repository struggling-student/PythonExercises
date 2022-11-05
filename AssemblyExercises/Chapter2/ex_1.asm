# ----> ITALIAN <----
# Implementare un programma in linguaggio assembly MIPS che:
# stampa a video “Primo numero: ” e prenda in input un numero a
# stampa a video “Secondo numero: ” e prenda in input un numero b
# stampa a video “Prodotto dei due numeri: ” e stampi a video axb
# *Esempio*
# OUTPUT: Primo Numero:
# INPUT:5
# OUTPUT:Secondo Numero:
# INPUT:6
# OUTPUT: Prodotto dei due numeri:30

.text
.globl main

main: 
	la $a0,mex1 #STAMPO A VIDEO IL MESSAGGIO PRIMO NUMERO:
	li $v0,4
	syscall 
	
	li $v0,5 # LETTURA DI UN INTERO DA TASTIERA
	syscall
	move $t0,$v0
	
	la $a0,mex2 #STAMPO A VIDEO IL MESSAGGIO SECONDO NUMERO:
	li $v0,4
	syscall 
	
	li $v0,5 # LETTURA DI UN INTERO DA TASTIERA
	syscall
	move $t1,$v0
	
	mul $t2,$t1,$t0 # MOLTIPLICAZIONE TRA IL PRIMO E IL SECONDO NUMERO 
	
	la $a0,mex3 # STAMPO A VIDEO IL MESSAGGIO IL PRODOTTO DEI DUE NUMERI:
	li $v0,4
	syscall
	
	move $a0,$t2 # SPOSTO IL RISULTATO DELLA MOLTIPLICAZIONE DA t2 in a0
	li $v0,1 # STAMPO A VIDEO IL RISULTATO
	syscall
	
	li $v0,10 # CHIUSURA PROGRAMMA
	syscall
	
.data
mex1: .asciiz "Primo numero:"
mex2: .asciiz "Secondo numero:"
mex3: .asciiz "Prodotto dei due numeri:"