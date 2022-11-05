# ----> ITALIAN <----
# L'ISTAT ha rivisto le stime dell'aspettativa di vita 
# (life expentancy, LE) della popolazione italiana in 84.8 
# per le donne e 80.5 per gli uomini.
# Realizzare un programma in assembly MIPS che acquisca da 
# input un carattere F o M per discriminare il genere di 
# un campione e un valore intero che rappresenta l'età e
#  determinare se il campione immesso ha superato la 
# media oppure no. Il programma termina quando l'utente 
# inserisce il carattere X.
# ESEMPIO:
# F;85;
# M;80;
# M;82;
# F;45;
# X
# OUTPUT
# OLTRE LA MEDIA LE; SOTTO LA MEDIA LE; 
# OLTRE LA MEDIA LE; SOTTO LA MEDIA LE;

.text
.globl main
main:
	lb $t0,M # CARICO IN t0 LA LETTERA M (MASCHIO)
	lb $t1,F # # CARICO IN t0 LA LETTERA F (FEMMINA)
	lb $t2,fine # CARICO IN t0 LA LETTERA X (FINE)
	lwc1 $f3, uomo # CARICO IN f3 IL VALORE MEDIO PER GLI UOMINI
	lwc1 $f4, donna # CARICO IN f4 IL VALORE MEDIO PER LE DONNE
CICLO1:
	li $v0, 12 # CHIEDO IN INPUT UNA LETTERA
	syscall
	beq $t0,$v0,UOMO # CONTROLLO SE IL VALORE IN INPUT E' UGUALE ALLA LETTERA SALVATA IN t0 E SE VERO VADO IN UOMO
	beq $t1,$v0,DONNA # CONTROLLO SE IL VALORE IN INPUT E' UGUALE ALLA LETTERA SALVATA IN t1 E SE VERO VADO IN DONNA
	beq $t2,$v0,FINE # CONTROLLO SE IL VALORE IN INPUT E' UGUALE ALLA LETTERA SALVATA IN t2 E SE VERO VADO IN FINE
	j CICLO1 # JUMP
UOMO: 
	li $v0,6 # CHIEDO IN INPUT UN VALORE IN SINGOLA PRECISIONE (FLOAT)
	syscall
	c.lt.s $f0,$f3 # CONTROLLO SE IL VALORE IN f0 E' MINORE DEL VALORE IN f4
	bc1t VERO1 #  SE LA CONDITION FLAG E' VERA VADO IN VERO1
	bc1f FALSO1 # SE LA CONDITION FLAG E' FALSA VADO IN FALSO1
VERO1:
	la $a0,SM # STAMPO IN CONSOLE IL TESTO SALVATO IN SM
	li $v0,4
	syscall
	j CICLO1 # JUMP
FALSO1:
	la $a0,OM # STAMPO IN CONSOLE IL TESTO SALVATO IN OM
	li $v0,4
	syscall
	j CICLO1 # JUMP
DONNA:
	li $v0,6 # CHIEDO IN INPUT UN VALORE IN SINGOLA PRECISIONE (FLOAT)
	syscall
	c.lt.s $f0,$f4 # CONTROLLO SE IL VALORE IN f0 E' MINORE DEL VALORE IN f4
	bc1t VERO2 # SE LA CONDITION FLAG E' VERA VADO IN VERO2
	bc1f FALSO2 # SE LA CONDITION FLAG E' FALSA VADO IN FALSO2
VERO2:
	la $a0,SM # STAMPO IN CONSOLE IL TESTO SALVATO IN SM
	li $v0,4
	syscall
	j CICLO1 # JUMP
FALSO2:
	la $a0,OM # STAMPO IN CONSOLE IL TESTO SALVATO IN OM
	li $v0,4
	syscall
	j CICLO1 # JUMP	 
FINE:
	li $v0, 10 # FINE DEL PROGRAMMA
	syscall

.data
M: .asciiz "M"
F: .asciiz "F"
fine: .asciiz "X"
uomo: .float 80.5
donna: .float 84.8
OM: .asciiz "OLTRE LA MEDIA LE"
SM: .asciiz "SOTTO LA MEDIA LE"
