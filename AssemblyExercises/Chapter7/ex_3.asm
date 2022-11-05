# ----> ITALIAN <----
# Definita in memoria una matrice di 4 righe e 4 colonne con 
# elementi byte, stampare in output la somma degli elementi 
# presenti lungo una colonna.
# ESEMPIO:
# MEMORIA
# 3 6 7 8
# 1 5 2 0
# 6 8 10 5
# 4 1 -9 2
# OUTPUT
# COLONNA 1: 14
# COLONNA 2: 20
# COLONNA 3: 10
# COLONNA 4: 15

.macro colonna_uno
la $a0,prima
li $v0,4
syscall

move $a0,$s0
li $v0,1
syscall
.end_macro

.macro colonna_due
la $a0,seconda
li $v0,4
syscall

move $a0,$s1
li $v0,1
syscall
.end_macro

.macro colonna_tre
la $a0,terza
li $v0,4
syscall

move $a0,$s2
li $v0,1
syscall
.end_macro

.macro colonna_quattro
la $a0,quarta
li $v0,4
syscall

move $a0,$s3
li $v0,1
syscall
.end_macro

.macro calcolo
sub $t6,$t0,1		# r - 1
mul $t9,$t6,$t3	# C(r-1)
sub $t7,$t1,1		# c - 1
add $t9,$t9,$t7	# C(r-1) + (c-1)
mul $t9,$t9,1		# MOLTIPLICO L'INDICE PER LA DIMENSIONE DELL'ELEMENTO (byte = 1)
.end_macro

.macro accapo
la $a0,spazio
li $v0,4
syscall
.end_macro

.text
.globl main
main:
	li $t0,1			# r
	li $t1,1			# c
	lw $t2,R			# R
	lw $t3,C			# C
	
ciclo1:
	calcolo
	lb $t8,matrice($t9)	# SALVO L'ELEMENTO DELLA MATRICE DENTRO AL REGISTRO
	add $s0,$s0,$t8	# INCREMENTO IL CONTATORE
	add $t0,$t0,1		# INCREMENTO RIGA
	ble $t0,$t2,ciclo1	# se $t0 < $t2 salta
	li $t0,1			# RINIZIALIZZO R
	
ciclo2:	
	li $t1,2			# INIZIALIZZO ALLA COLONNA 2
	calcolo
	lb $t8,matrice($t9)	# SALVO L'ELEMENTO DELLA MATRICE DENTRO AL REGISTRO
	add $s1,$s1,$t8	# INCREMENTO IL CONTATORE
	add $t0,$t0,1		# INCREMENTO RIGA
	ble $t0,$t2,ciclo2	# se $t0 < $t2 salta
	li $t0,1			# RINIZIALIZZO R
	
ciclo3:		
	li $t1,3			# INIZIALIZZO ALLA COLONNA 3
	calcolo	
	lb $t8,matrice($t9)	# SALVO L'ELEMENTO DELLA MATRICE DENTRO AL REGISTRO
	add $s2,$s2,$t8	# INCREMENTO IL CONTATORE
	add $t0,$t0,1		# INCREMENTO RIGA
	ble $t0,$t2,ciclo3	# se $t0 < $t2 salta
	li $t0,1			# RINIZIALIZZO R
	
ciclo4:
	li $t1,4			# INIZIALIZZO ALLA COLONNA 4
	calcolo
	lb $t8,matrice($t9)	# SALVO L'ELEMENTO DELLA MATRICE DENTRO AL REGISTRO
	add $s3,$s3,$t8	# INCREMENTO IL CONTATORE
	add $t0,$t0,1		# INCREMENTO RIGA
	ble $t0,$t2,ciclo4	# se $t0 < $t2 salta
	
	colonna_uno		# MACRO 1
	accapo			# VA A CAPO
	
	colonna_due		# MACRO 2
	accapo			# VA A CAPO
	
	colonna_tre		# MACRO 3
	accapo			# VA A CAPO
	
	colonna_quattro	# MACRO 4
	
	li $v0,10			# CHIUSURA DEL PROGRAMMA
	syscall
	
.data
matrice: .byte 3,6,7,8, 1,5,2,0, 6,8,10,5, 4,1,-9,2
R: .word 4
C: .word 4
prima: .asciiz "La somma della prima colonna è: "
seconda: .asciiz "La somma della seconda colonna è: "
terza: .asciiz "La somma della terza colonna è: "
quarta: .asciiz "La somma della quarta colonna è: "
spazio: .asciiz "\n"
