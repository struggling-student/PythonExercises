# ----> ITALIAN <----
# Si scriva un programma in linguaggio assembly MIPS per 
# calcolare il massimo comun divisore (MCD) di due numeri 
# interi positivi. Il MCD è deﬁnito come il massimo tra i 
# divisori comuni ai due numeri. Stampare il MCD.
# Suggerimento. Si considerino due numeri interi N1 e N2. 
# Il MCD di N1 e N2 è il massimo tra i numeri che sono divisori
# (con resto uguale a zero) sia di N2 che di N1. In
# particolare, si supponga che sia N1 minore di N2.
# Il MCD è il massimo tra i numeri compresi tra 1 e N1 che 
# sono divisori (con resto uguale a zero) sia di N1 che di N2.

.text
.globl main

main:
	li $v0,5 # VALORE A
	syscall
	move $t0,$v0
	
	li $v0,5 # VALORE B
	syscall
	move $t1,$v0
IF:	
	beq $t0,$t1,DO_IF # SE A=B ALLORA VADO NEL IF SE NO OUT IF
	j OUT_IF

DO_IF:
	move $a0,$t0 # STAMPO IL VALORE DI A SU CONSOLE PERCHE' SE A=B ALLORA IL VALORE DI A E' L'MCD
	li $v0,1
	syscall
	
	li $v0, 10 # CHIUDO IL PROGRAMMA
	syscall
	
OUT_IF:
	
WHILE:	
	bgt $t0,$t1,DO_WHILE # SE A > B ALLORA DO WHILE SE NO OUT WHILE
	j OUT_WHILE
	
DO_WHILE:
	sub $t4,$t0,$t1 # A - B E POI IL RISULTATO LO SPOSTO IN t0 OVVERO IL REGISTRO DOVE HO IL VALORE DI A
	move $t0,$t4 # A = A-B
	j WHILE
	
OUT_WHILE:

WHILE2:
	bgt $t1,$t0,DO_WHILE2 # SE B > A ALLORA DO WHILE SE NO OUT WHILE
	j OUT_WHILE2
	
DO_WHILE2:
	sub $t5,$t1,$t0 # B - A E POI IL RISULTATO LO SPOSTO IN t1 OVVERO IL REGISTRO DOVE HO IL VALORE DI B
	move $t1,$t5 # B = B - A
	j WHILE2
	
OUT_WHILE2:
	j IF # TORNO AL IF PER CONFRONTARE SE A = B
	
.data
