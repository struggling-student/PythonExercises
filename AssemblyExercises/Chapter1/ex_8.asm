# ----> ITALIAN <----
# Un utente inserisce da tastiera una serie di numeri interi 
# positivi, ed il termine della serie è indicato 
# dall’inserimento del valore -1. Il programma in linguaggio
# assembly MIPS, al termine dell’inserimento, stampa quanti 
# numeri in totale sono stati inseriti
# NB:la stampa deve avvenire da consolle output dell'emulatore MARS

.eqv CONT $t0 
.eqv INCR $t2

.text
.globl main
main:
	li $v0,5 # INPUT 1, ASSEGNO UN NUMERO CHE VOGLIO IO DA TASTIERA
	syscall
	move $t3,$v0
	
	lw $t4, over # CARICO IL VALORE OVER CHE FUNZIONA DA STOP PROGRAM
	
	bgt $t3,$t4, DO_IF # SE IL VALORE CHE HO IN INPUT 1 E' MAGGIORE DI -1 ALLORA VADO IN DO_IF
	j OUT_IF # SE NO JUMP IN OUT_IF
	
DO_IF:
	li CONT,0 # INIZIALIZZAZIONE DEL CONTATOREE
	li INCR,1 # ASSEGNAZIONE DEL PASSO DI INCREMENTO
	
FOR:	beq  $t4,$t3, END_FOR # SE t3 HA LO STESSO VALORE DI t4 VADO NEL END_FOR
	li $v0,5  # INPUT 1, ASSEGNO UN NUMERO CHE VOGLIO IO DA TASTIERA
	syscall
	move $t3,$v0 
	
	add CONT, CONT, INCR  # AUMENTO IL CONTATORE DI 1
	j FOR  # JUMPP PER TRNARE AL FOR E RICOMINCIARE IL FOR SE POSSIBILE
	
END_FOR:	

	move $a0,$t0  # STAMPO IL VALORE DEL CONTATORE, CHE SAREBBE IL NUMERO TOTALE DI INSERIMENTI
	li $v0,1
	syscall
	
	li $v0, 10 # CHIUDO IL PROGRAMMA
	syscall
	
OUT_IF:

	la $a0,errore # PRINT ERRORE NEL CASO INSERISCO -1 COME PRIMO VALORE
	li $v0,4
	syscall
	
	li $v0, 10 # CHIUDO IL PROGRAMMA
	syscall
	
		
	
.data
over: .word -1
errore: .asciiz "Hai terminato il programma senza inserire nessun numero"
