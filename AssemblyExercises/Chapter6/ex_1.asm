# ----> ITALIAN <----
# Implementare in linguaggio asembly MIPS un programma che 
# calcola il massimo tra n elementi immessi in input 
# (la lettura termina quando si introduce un numero negativo. 
# Utilizzare la sub-routine (funzione) MASSIMO che presi 
# due elementi restituisce il massimo.
# Esempio:
# INPUT:
# 45; 66; 34; 156; 233; 234; 56; 0 ; -11
# ANALISI
# MASSIMONUM(45, 66, 34, 156,233,234,56,0,-11)=234
# MASSIMO(MASSIMO(MASSIMO(MASSIMO(MASSIMO(MASSIMO(MASSIMO(45,66),34),156),233),234),56),0)=234
# OUTPUT:
# 234

.text 
.globl main
main:
	li $v0,5			# RICHIESTA INPUT
	syscall			#
	move $a0,$v0		# SPOSTO IN VALORE NEL REGISTRO PRESERVANTE a0
hulk:	
	li $v0,5			# RICHIESTA INPUT
	syscall			#
	move $a1, $v0		# SPOSTO IN VALORE NEL REGISTRO PRESERVANTE a1
	jal MAX			# SALTO A FUNZIONE MAX
	move $a0, $v0		# RECUPERO DEL VALORE DI RITORNO DELLA FUNZIONE 
	j hulk			# SALTO A HULK PER RICHIEDERE UN VALORE IN INPUT
fine2:
	li $v0,1			# STAMPA RISULTATO
	syscall			#
	li $v0,10			# FINE PROGRAMMA
	syscall			#
MAX:	
	move $t0,$a0		# SPOSTO IL VALORE DAL REGISTRO PRESERVANTE IN UN REGISTO TEMPORANEO 
	move $t1,$a1		# SPOSTO IL VALORE DAL REGISTRO PRESERVANTE IN UN REGISTO TEMPORANEO 
	bltz $t0,fine2		# CONTROLLO SE IL VALORE IN t0 E' MINORE DI 0, SALTO IN FINE PERCHE' NEGATIVO
	bltz $t1,fine2		# CONTROLLO SE IL VALORE IN t0 E' MINORE DI 0, SALTO IN FINE PERCHE' NEGATIVO	
	move $t2,$t0		# SPOSTO IL VALORE IN t0 IN t2 E LO CONSIDERO IL VALORE MAX	
	blt $t1,$t0,fine	# CONFRONTO SE IL VALORE IN t1 E' MINORE DEL VALORE IN t0, SE VERO SALTO IN fine
	move $t2,$t1		# SPOSTO IN VALORE IN t1 IN T2 E LO CONSIDERO COME IL NUOV VALORE MAX
fine:
	move  $v0,$t2		# SPOSTO IL VALORE IN t2 NEL REGISTRO DI RITORNO DELLA FUNZIONE
	jr $ra			# SALTO PER IL RITORNO DEL MAIN
