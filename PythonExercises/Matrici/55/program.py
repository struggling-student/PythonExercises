

def es55(sel,m,n,A):
    '''
    la funzione es55(sel,m,n,A) che, presi in input:
    - una stringa di testo contenente uno tra i caratteri 'r' e 'c'
    - due interi m e n
    - una matrice A di interi (rappresentata tramite lista di liste in cui ciascuna lista e' una riga della matrice)
    restituisce la coppia (tupla) di interi con  il minimo e il massimo tra gli elementi della matrice
    e la modifica distruttivamente.
    Al termine della funzione:
    -se sel='r' allora la  riga m e la riga n della matrice A risultano scambiate tra loro.
    -se sel='c' allora la colonna m e la colonna n della matrice A risultano scambiate tra loro
    Si puo' assumere che le dimensioni h e w della matrice siano tali che m,n <=h e m,n<=w.
    Ad esempio:
    - per sel='r', m=1,n=2 e A=[[2,0,-4],[5,10,20],[5,1,-1]] al termine dell'esecuzione della funzione
      verra' restituita la tupla (-4,10) e  si avra' A=[[2,0,-4],[5,1,-1],[5,10,20]]
    - per sel='c', m=0,n=1 e A=[[2,0,-4],[5,10,20],[5,1,-1]] al termine dell'esecuzione della funzione
      verra' restituita la tupla (-4,10) e  si avra' A=[[0,2,-4],[10,5,20],[1,5,-1]]
    '''
    # inserisci qui il tuo codice


