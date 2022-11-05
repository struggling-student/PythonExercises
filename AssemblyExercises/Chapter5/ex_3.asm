# ----> ITALIAN <----
# Un programma in linguaggio assembly MIPS deve inizializzare 
# quindici valori interi e calcolare la media aritmetica 
# (si deve usare il coprocessore matematico) degli elementi 
# alla posizioni pari, alla posizioni dispari e quella 
# complessiva.

.macro spazio
	la $a0,newLine 		# STAMPO SU CONSOLE UNO SPAZIO
	li $v0,4				#	
	syscall				#
.end_macro
.text
.globl main
main:
	la $s0,v 				# INDIRIZZO ASSOLUTO DEL VETTORE
	li $t0,15				# NUMERO ELEMENTI
	li $t1,0				# INZIALIZZO IL CONTATORE A 0
	li $t6,2				# SETTO IL REGISTRO t6 A 2 
	li $t7,0 				# REGISTRO PER SOMMA POSIZIONI PARI
	li $t8,0 				# REGISTRO PER SOMMA POSIZIONI DISPARI
	li $t9,0 				# REGISTRO PER SOMMA TOTALE
	mtc1 $t9,$f9			# CONVERTO IL VALORE IN t9 DA INTERO A SINGOLA PRECISIONE
	cvt.s.w $f9,$f9		#
	mtc1 $t8,$f8			# CONVERTO IL VALORE IN t8 DA INTERO A SINGOLA PRECISIONE
	cvt.s.w $f8,$f8		#
	mtc1 $t7,$f7			# CONVERTO IL VALORE IN t7 DA INTERO A SINGOLA PRECISIONE
	cvt.s.w $f7,$f7		#
	
ciclo1:
	bge $t1, $t0, hulk 		# SE t1 E' MAGGIOR UGUALE DI t0 VAI IN hulk
	li $v0, 5 			# RICHIESTA DI INPUT (NUMERO)
	syscall				#
	sw $v0, ($s0)			# CARICO IL VALORE RICEVUTO IN INPUT NEL VETTORE
	addi $s0, $s0, 4 		# INCREMENTO ALL'ELEMENTO SUCCESSIVO
	addi $t1, $t1, 1 		# INCREMENTO DI UNO
	j ciclo1 				# JUMP	
	
hulk:	
	la $s0,v				# INDIRIZZO ASSOLUTO DEL VETTORE
	lw $t2, 0($s0) 		# PRELIEVO DEL ELEMENTO
	li $t1, 1 			# CARICO IN t1 IL VALORE 1
	mtc1 $t2,$f6			# CONVERTO IL VALORE IN t2 DA INTERO A SINGOLA PRECISIONE
	cvt.s.w $f6,$f6		#		
	addi $s1, $s1, 4 		# INCREMENTO ALL'ELEMENTO SUCCESSIVO
	add.s $f7,$f7,$f6		# SOMMO IL VALORE f6 IN f7 OVVERO LA SOMMA PER LE POSIZIONI PARI
	add.s $f9,$f9,$f6		# SOMMO IL VALORE f6 IN f9 OVVERO LA SOMMA TOTALE
	
while1:
	bge $t1, $t0, end 		# SE t1 E' MAGGIOR UGUALE DI t0 VAI IN end
	lw $t3, ($s0) 			# PRELIEVO DEL ELEMENTO
	mtc1 $t3,$f5			# CONVERTO IL VALORE IN t3 DA INTERO A SINGOLA PRECISIONE
	cvt.s.w $f5,$f5		#
	add.s $f9,$f9,$f5		# SOMMO IL VALORE f5 IN f9 OVVERO LA SOMMA TOTALE
	addi $t1, $t1, 1 		# AUMENTO IL CONTATORE
	addi $s1, $s1, 4 		# INCREMENTO ALL'ELEMENTO SUCCESSIVO
	div $t1,$t6			# FACCIO LA DIVISIONE TRA IL VALORE IN t1(CONTATORE) E IL VALORE IN t6(2)
	mfhi $t5				# SALVO IL RESTO IN t5
	j check				# JUMP
check:
	beqz $t5,pari			# SE IL VALORE IN t5 E' UGUALE A 0 VADO IN PARI
	add.s $f8,$f8,$f5		# SOMMO IL VALORE f5 IN f8 OVVERO LA SOMMA PER LE POSIZIONI DISPARI
	j while1 				# JUMP
pari:
	add.s $f7,$f7,$f5		# SOMMO IL VALORE f5 IN f7 OVVERO LA SOMMA PER LE POSIZIONI PARI
	j while1				# JUMP
end:
	la $a0, mex1 			# STAMPO SU CONSOLE IL TESTO SALVATO IN mex1
	li $v0, 4				#
	syscall				#
	mov.s $f12,$f7			# STAMPO SU CONSOLE IL VALORE IN f7
	li $v0,2				#
	syscall				#
	spazio
	la $a0, mex2 			# STAMPO SU CONSOLE IL TESTO SALVATO IN mex2
	li $v0, 4				#
	syscall				#
	mov.s $f12,$f8			# STAMPO SU CONSOLE IL VALORE IN f8
	li $v0,2				#
	syscall				#
	spazio
	la $a0, mex3 			# STAMPO SU CONSOLE IL TESTO SALVATO IN mex3
	li $v0, 4				#
	syscall				#
	mov.s $f12,$f9			# STAMPO SU CONSOLE IL VALORE IN f9
	li $v0,2				#
	syscall				#
	li $v0, 10 			# FINE PROGRAMMA
	syscall				#
.data
v: .word 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  
mex1: .asciiz "SOMMA ELEMENTI POSIZIONI PARI: "
mex2: .asciiz "SOMMA ELEMENTI POSIZIONI DISPARI: "
mex3: .asciiz "SOMMA COMPLESSIVA: "
newLine: .asciiz "\n"
