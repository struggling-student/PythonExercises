# ----> ITALIAN <----
# Implementare un programma in linguaggio assembly MIPS che 
# dati cinque interi positivi definiti in memoria calcola 
# la media aritmetica
# Esempio
# INPUT: a=0,b=11;c=7;d=1982;e=10051980
# OUTPUT:2010796

.text
.globl main
main:
	lw $t0,num1 # CARICO NUMERO 1 DA MEMORIA NEL REGISTRO t0
	lw $t1,num2 # CARICO NUMERO 2 DA MEMORIA NEL REGISTRO t1
	lw $t2,num3 # CARICO NUMERO 3 DA MEMORIA NEL REGISTRO t2
	lw $t3,num4 # CARICO NUMERO 4 DA MEMORIA NEL REGISTRO t3
	lw $t4,num5 # CARICO NUMERO 5 DA MEMORIA NEL REGISTRO t4
	
	li $t9,5 # CARICO IN t9 IL VALORE 5 OVVERO QUANTI NUMERI HO
	
	add $t8,$t0,$t1 # FACCIO LA SOMMA DI TUTTI E CINQUE I NUMERI
	add $t8,$t8,$t2
	add $t8,$t8,$t3
	add $t8,$t8,$t4
	
	div $t8,$t9 # DIVIDO IL RISULTATO DELLA SOMMA PER CINQUE
	
	mflo $t7 # SPOSTO IL VALORE DEL QUOZIENTE IN t7
	
	move $a0,$t7 # STAMPO IL RISULTATO DELLA MEDIA ARITMETICA
	li $v0,1
	syscall
	
	li $v0,10  # FINE PROGRAMMA
	syscall	
	
	
.data
num1: .word 0
num2: .word 11
num3: .word 7
num4: .word 1982
num5: .word 10051980
