# ----> ITALIAN <----
# Definita una matrice in memoria di 8 righe e 8 colonne con 
# elementi halfword,A_{8*8}, stampare in output una nuova 
# matrice B_{8*4} in cui le colonne sono date dal prodotto 
# degli elementi delle colonne della matrice originaria: cioè
# B_{4*8}b_{1,1}=a_{1,1}*a_{1,2};b_{1,2}=a_{1,3}*a_{1,4};b_{1,3}=a_{1,5}*a_{1,6};b_{1,4}=a_{1,7}*a_{1,8}.
# ESEMPIO :
# A
# 02 04 06 07 00 12 03 08
# 01 10 05 16 00 01 01 10
# 00 03 20 21 01 01 02 04
# 02 22 06 00 00 12 37 00
# 30 50 01 34 00 05 04 13
# 10 63 08 08 01 06 05 03
# 05 04 00 01 00 09 06 02
# 41 00 14 02 00 14 00 01
# B
# 0008 0042 0000 0024
# 0010 0080 0000 0010
# 0000 0421 0001 0008
# 0044 0000 0000 0000
# 1500 0340 0000 0052
# 0630 0064 0006 0015
# 0020 0000 0000 0012
# 0000 0028 0000 0000

.macro calcolo
	sub $t6,$t0,1 				# CALCOLO ELEMENTO R,C
	mul $t9,$t6,$t3 			# 
	sub $t7,$t1,1  			# r,c=C(r-1)+(c-1)
	add $t9,$t9,$t7 			# 
	mul $t9,$t9,2 				# MOLTIPLICAZIONE DIMENSIONE
.end_macro					#
.text						#
.globl main					#
main:						#
	li $t0,1 					# INDICE r	
	li $t1,1					# INDICE c
	lh $t2,R 					# NUMERO RIGHE 
	lh $t3,C 					# NUMERO COLONNE
analisi_riga:					#
	li $t1,1 					#
analisi_colonna:				#
	calcolo					#
	lh $t8,matrice($t9) 		# PRELIEVO ELEMENTO
	addi $t1,$t1,1				# INCREMENTO DI 1
	calcolo					#
	lh $t7,matrice($t9) 		# CARICO L'ELEMENTO IN t7
	addi $t1,$t1,1				# INCREMENTO DI 1
	mul $t6,$t7,$t8			# MOLTIPLICO IL PRIMO ELEMENTO CON IL SECONDO ELEMENTO
	move $a0,$t6 				# STAMPA ELEMENTO
	li $v0,1					#
	syscall					#
	la $a0,tabulato 			# PRINT SU CONSOLE
	li $v0,4					#
	syscall					#
	ble $t1,$t3,analisi_colonna	#
	la $a0,riga 				# PRINT SU CONSOLE
	li $v0,4					#
	syscall					#
	addi $t0,$t0,1				#
	ble $t0,$t2, analisi_riga	#
	li $v0, 10				# FINE PROGRAMMA
	syscall					#
.data
tabulato: .asciiz "\t"
riga: .asciiz" \n"
matrice: .half 02,04,06,07,00,12,03,08,01,10,05,16,00,01,01,10,00,03,20,21,01,01,02,04,02,22,06,00,00,12,37,00,30,50,01,34,00,05,04,13,10,63,08,08,01,06,05,03,05,04,00,01,00,09,06,02,41,00,14,02,00,14,00,01
R: .half 8
C: .half 8
