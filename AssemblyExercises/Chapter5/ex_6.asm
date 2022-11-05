# ----> ITALIAN <----
# Scrivere un programma in linguaggio assembly MIPS che legga
# una stringa introdotta da tastiera. La stringa contiene sia 
# caratteri maiuscoli che caratteri minuscoli, e 
# complessivamente al più 100 caratteri. Il programma deve 
# svolgere le seguenti operazioni:
# - Visualizzare la stringa inserita.
# - Costruire una nuova stringa in cui il primo carattere di ciascuna parola nella frase di partenza è stato reso maiuscolo. Tutti gli altri caratteri devono essere resi minuscoli. Il programma deve memorizzare la nuova stringa.
# - Visualizzare la nuova frase.
# Ad esempio la frase "cHe bElLA gIOrnaTa" diviene
# "Che Bella Giornata".

.macro stampa
		li $v0,11 # STAMPA CARATTERE
		move $a0,$t1 # SPOSTO L'ELEMENTO CHE VOGLIO SALVARE
		syscall
.end_macro

.macro incrementa
		add $t0,$t0,1 # INCREMENTO IL CONTATORE
.end_macro

.macro fine
		li $v0,10 # FINE PROGRAMMA
		syscall
.end_macro

.text
.globl main
main:	
	la $a0,txt # CARICO L'INDIRIZZO DOVE SALVERO' LA STRINGA
	li $a1,255 # CARICO IL NUMERO MASSIMO DI CARATTERI CHE POSSONO ESSERE PRESENTI NELLA STRINGA

	li $v0,8 # LETTURA STRINGA
	syscall
	
	li $t0,0 # INIZIALIZZAZIONE DI UN CONTATORE
     lb $t7,spazio # CARICO IL VALORE DEL CARATTERE SPAZIO DELLA TABELLA ASCII
	lb $t8,A # CARICO IL VALORE DELLA LETTERA A DELLA TABELLA ASCII
	lb $t9,a # CARICO IL VALORE DELLA LETTERA a DELLA TABELLA ASCII
	sub $t6,$t9,$t8 # SALVO LA DIFFERENZA FRA UPPER E LOWER(32)
	
	lb $t1,txt($t0) # CARICO L'I-ESIMO CARATTERE DELLA STRINGA
	blt $t1,$t9,SALVATAGGIO # CONTROLLO SE IL PRIMO CARATTERE E' MINORE DI 97(a), SE VERO VADO IN SALVATAGGIO PER STAMPARE
	sub $t1,$t1,$t6 # ALTRIMENTI SOTTRAGGO AL VALORE IN LOWER LA DIFFERENZA FRA UPPER E LOWER(32)
	stampa 
	incrementa
CICLO:
	lb $t1,txt($t0) # CARICO L'I-ESIMO CARATTERE DELLA STRINGA
	beq $t1,0,FINE # SE HO CARICATO UNO 0, HO CARICATO L'ULTIMO ELEMENTO, E SALTO ALLA FINE
	ble $t1,$t7,SPAZIO # SE IL VALORE IN t2 E' MINORE O UGUALE AL VALORE IN t7 VADO IN SPAZIO
	bge $t1,$t9 SALVATAGGIO # SE IL VALORE IN t1 E' MAGGIORE DEL VALORE IN t9 VADO IN SALVATAGGIO
	add $t1,$t1,$t6 # ALTRIMENTI AAGGIUNGO AL VALORE IN UPPER LA DIFFERENZA FRA UPPER E LOWER(32)
SALVATAGGIO:
	stampa
	incrementa
	j CICLO
SPAZIO: 
	stampa
	incrementa
	lb $t1,txt($t0) # CARICO L'I-ESIMO CARATTERE DELLA STRINGA
	blt $t1,$t9,SALVATAGGIO # CONTROLLO SE IL PRIMO CARATTERE E' MINORE DI 97(a), SE VERO VADO IN SALVATAGGIO PER STAMPARE
	sub $t1,$t1,$t6 # ALTRIMENTI SOTTRAGGO AL VALORE IN LOWER LA DIFFERENZA FRA UPPER E LOWER(32)
	stampa
	incrementa
	j CICLO
FINE:
	fine		
.data
A: .asciiz "A"
a: .asciiz "a"
spazio: .ascii " "
txt: .space 200
