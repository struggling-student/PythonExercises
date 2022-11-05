# ----> ITALIAN <----
# Creare una funzione int DIVISORE (int n) che calcola quanti 
# divisori ha un numero naturale n.
# Creare poi un programma che ricevuto dall’utente un 
# numero naturale n stampi il numero d che indica quanti 
# divisori ha n.
# ESEMPIO:
# READ(x) //immessione di x=33
# Y=DIVISORE(X)
# PRINT(Y) //risultato 2 (cioè 3 e 11)

.text
.globl main

main:
	li $v0, 5 # RICHIESTA DI INPUT (NUMERO)
	syscall
	move $t0, $v0 # N NUMERI DA INSERIRE
	move $a0,$t0
	jal DIVISORE
	move $t0,$v0
	move $a0,$t0		# STAMPA SU CONSOLE IL VALORE IN t5
	li $v0,1 			#
	syscall	
	
	li $v0, 10 		# FINE PROGRAMMA
	syscall
DIVISORE:
	move $t0,$a0
	li $t1,0
	li $t2,2
ciclo:
	beq $t2,$t0,fine
	div $t0,$t2
	mfhi $t3
	beqz $t3, divisore
	addi $t2,$t2,1
	j ciclo
divisore:
	addi $t1,$t1,1
	addi $t2,$t2,1
	j ciclo

fine:
	move $v0,$t1
	jr $ra
	
.data
