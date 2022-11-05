# ----> ITALIAN <----
# Effettuare la sommatoria di numeri reali poistivi 
# immessi da input. La sommatoria è calcolata quando 
# il valore immesso dall'utente è nullo o negativo.
# INPUT
# 3.5;7.23;5.6;9.17;-1
# OUTPUT
# 25.5

.text
.globl main
main:
	li $v0,6 # CHIEDO IN INPUT UN NUMERO REAELE POSITIVO CHE VIENE AUTOMATICAMENTE MESSO IN f0
	syscall
	
	li $t9,0  # INIZIALIZZO in t9 IL VALORE 0
	mtc1 $t9,$f9  # CONVERTO IL NUMERO INTERO IN NUMERO REALE (FLOAT) USANDO IL COPROCESSORE MATEMATICO
	cvt.s.w $f9,$f9
	
	add.s $f5,$f9,$f0 # SOMMA A SINGOLA PRECISIONE TRA f9 e f0
	
	lw $t4, over # CARICO IN t4 IL VALORE -1 OVVERO QUANDO LA SOMMATORIA DEVE VENIRE CALCOLATA
	mtc1 $t4,$f8 # CONVERTO IL NUMERO INTERO IN NUMERO REALE (FLOAT) USANDO IL COPROCESSORE MATEMATICO
	cvt.s.w $f8,$f8

CICLO:	
	li $v0,6 # CHIEDO IN INPUT UN NUMERO REAELE POSITIVO CHE VIENE AUTOMATICAMENTE MESSO IN f0
	syscall
	c.eq.s $f8,$f0 # COMPARAZIONE DI UGUAGLIANZA IN SINGOLA PRECISIONE TRA f8 E f0
	bc1t FINE # SE LA CONDITION FLAG E' VERA VAI IN FINE
	
	bc1f HULK # SE LA CONDITION FLAG E' FALSA VAI IN HULK

HULK:
	add.s $f5,$f5,$f0 # SOMMA IN SINGOLA PRECISIONE TRA f5 E f0
	j CICLO # JUMP 
	
FINE:
	mov.s $f12,$f5 # SPOSTO IL VALORE CHE HO IN f5 IN f12 E LO STAMPO SU CONSOLE
	li $v0,2 
	syscall
	
.data
over: .word -1
errore: .asciiz "Hai terminato il programma senza inserire nessun numero"
