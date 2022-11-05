# ----> ITALIAN <---- 
# Simulare il gioco di carta, forbice e sasso di due giocatori 
# sapendo che:
# 1. la carta batte il sasso.
# 2. il sasso batte la forbice.
# 3. la forbice batte la carta.
# 4. il gioco termina dopo 10 lanci.
# 5. carta, sasso e forbice sono determinati in maniera casuale.
# il MIPS consente di generare un numero INTERO casuale 
# mediante la syscall 42 in $v0 (il numero casuale generato si 
# trova in $a0 dopo la chiamata a sistema). NB: prima dellaù
# chiamata a syscall è possibile impostare ad n il registro 
# $a1 per generare i valori interi inclusi tra 0 e n-1. 
# Ad esempio impostando a 6 il registro $a1, dopo la syscall 
# in $a0 si ha un numero compreso tra 0 e 5. In questo modo 
# è possibile pensare di assegnare al sasso, forbice e carta 
# un valore numerico che poi dovrà essere confrontato in base 
# alle regole a), b), c).
#
# Mostrare per ogni iterazione il segno prescelto dai 
# concorrenti e riportare, alla fine del gioco, il nome del 
# vincitore.

# NO SOLUTION