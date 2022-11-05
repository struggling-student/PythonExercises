# ----> ITALIAN <----
# Si scriva un programma in linguaggio assembly MIPS che 
# legga da tastiera una serie di numeri interi fino a quando 
# la somma di tutti i numeri introdotti ﬁno a quel momento
# non supera il valore 1000. A quel punto, il programma stampa 
# il valore del prodotto di tutti i numeri inseriti.
# NB:la stampa deve avvenire da consolle output dell'emulatore MARS

.text
.globl main
main:
	lw $t0,limite # CARICO IL LIMITE, IL VALORE CHE NON DEVE SUPERARE LA SOMMMA OVVERO 1000
	lw $t2,somma # INZIALIZZO IL VALORE DELLA SOMMA A 0
	lw $t4,moltiplicazione	# INIZIALIZZO IL VALORE DELLA MOLTIPLICAZIONA A 1
			
WHILE: 
	blt $t2,$t0,DO_WHILE # SE IL VALORE DELLA SOMMA E' MINORE DI 1000 ALLORA ESEGUO IL WHILE, SE NO ESCO
	j EXIT_WHILE

DO_WHILE:
	li $v0,5  # INPUT DA TASTIERA OVVERO UN NUMERO
	syscall
	move $t1,$v0
	
	add $t3,$t1,$t2 # SOMMO IL MUMERO RICEVUTO IN INPUT CON IL VALORE CHE HO NELLA SOMMA
	
	move $t2,$t3 # SPOSTO IL RISULTATO DELLA SOMMA NEL REGISTRO t2 CHE CONTIENE IL VALORE FINALE DELLA SOMMA
	
	mul $t5,$t1,$t4 # MOLTIPLICO IL NUMERO RICEVUTO IN INPUT CON IL VALORE CHE HO NELLA MOLTIPLICAZIONE
	
	move $t4,$t5  # SPOSTO IL RISULTATO DELLA MOLTIPLICAZIONE NEL REGISTRO t5 CHE CONTIENE IL VALORE FINALE DELLA 
	 	      # MOLTIPLICAZIONE
	
	j WHILE # JUMP 
EXIT_WHILE:

	move $a0, $t4 # STAMPO IL VALORE CHE HO NEL REGISTRO t4 OVVERO LA MOLTIPLICAZIONE
	li $v0,1 
	syscall
	
	li $v0, 10 # FINE PROGRAMMA
	syscall
																	
.data
limite: .word 1000
somma: .word 0
moltiplicazione: .word 1
