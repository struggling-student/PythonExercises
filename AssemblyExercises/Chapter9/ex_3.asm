# ----> ITALIAN <----
# Si scriva un programma che definisca in memoria due vettori: 
# V1 un vettore di cinque elementi di byte e V2 un vettore di 
# cinque elementi di halfword.
# Si applichi ala programma una funzione:
# SOMMA(V1,V2,V3)
# Che ha come argomenti i due vettori definiti dall'utente 
# V1 e V2 e restituisce il vettore V3 formato dall'elemento 
# più grande alla stessa posizione dei vettori V1 e V2.
# ESEMPIO:
# V1=3,56,12,45,33
# V2=-4,67,89,11,47000
# V3=3,67,89,45,47000

.macro spazio
	la $a0,newLine		# STAMPA SPAZIO
	li $v0,4			#
	syscall			#
.end_macro 


.text
.globl main

main:
	la $s0,v1
	la $s1,v2
	la $s2,v3
	
	move $a0,$s0
	move $a1,$s1
	move $a2,$s2
	jal SOMMA
	move $s2,$v0
	la $s2,v3
	li $t1,5
	lh $t2, 0($s2)
	move $a0,$t2 		
	li $v0,1 			
	syscall	
	spazio
	addi $s2,$s2,2
	li $t0,1
ciclo2: 
	bge $t0,$t1,fine2
	lh $t2, ($s2)
	move $a0,$t2 		
	li $v0,1 			
	syscall	
	spazio
	addi $s2,$s2,2
	addi $t0,$t0,1
	j ciclo2
	
fine2:
	li $v0, 10 		# FINE PROGRAMMA
	syscall
SOMMA:
	move $s0,$a0
	move $s1,$a1
	move $s2,$a2
	
	la $s0,v1
	la $s1,v2
	la $s2,v3
	
	li $t0,0
	li $t1,10
		
	lb $t2, 0($s0)# BYTE
	lh $t3, 0($s1)# HALF
	
	bge $t2,$t3,save
	sh $t3, ($s2)
	addi $s0,$s0,1
	addi $s1,$s1,2
	
ciclo:
	bge $t0,$t1,fine
	lb $t2, ($s0) # 56
	lh $t3, ($s1) # 67
	bge $t2,$t3,save
	sh $t3, ($s2)
	addi $s2,$s2,2
	addi $s1,$s1,2
	addi $s0,$s0,1
	addi $t0,$t0,1
	addi $t0,$t0,1
	j ciclo
save:
	sb $t2, ($s2)
	addi $s2,$s2,2
	addi $s0,$s0,1
	addi $s1,$s1,2
	addi $t0,$t0,1
	addi $t0,$t0,1
	j ciclo
fine:
	move $v0,$s2
	jr $ra

.data
v1: .byte 3,56,12,45,33
v2: .half -4,67,89,11,31000
v3: .half 0,0,0,0,0
newLine: .asciiz "\n"
