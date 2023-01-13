

def es40(jsonFile,k):
    ''' 
    Data una matrice di interi M, diciamo che la sua coordinata  (x,y)  individua un quadrato di lato k
    se nelle 4 posizioni M[y][x], M[y][x+k], M[y+k][x+k] e M[y+k][x] troviamo  nell'ordine una sequenza
    crescente di 4 interi.
    Ad esempio nella matrice
      2  3  3  6  1
      2  8  5  1  9 
      5  4 40  4  5
      9 10  1  7  6
     12 11  9  8 10
     la coordinata (1,1) individua un quadrato di lato 3 (la cui sequenza e' 8,9,10,11) mentre 
     la coordinata (3,2) individua un quadrato di lato 1 (la cui sequenza e' 4,5,6,7)
     la coordinata (0,3) individua un quadrato di lato 1 (la cui sequenza e' 9,10,11,12)
    
    si definisca la funzione es40(jsonFile, k), che presi come argomenti:
    - jsonFile: il path di un file json contenente una matrice rappresentata come  lista di liste di interi
    - un intero k
    ricerca all'interno della matrice nel file json l'eventuale presenza di un quadrato di lato k.
    La funzione deve restituire  la tupla che rappresenta la coordinata (x,y) che individua il quadrato di lato k.
    Nel caso la matrice  contenga piu' quadrati di lato k, bisogna  restituire la coordinata che individua quello piu' 
    in basso a destra (vale a dire quello per cui risulta massima la riga ed a parita' la colonna).
    Nel caso la matrice non contenga quadrati di lato k bisogna restituire la tupla (-1,-1).
    Per la matrice dell'esempio e k = 2 la funzione restituisce (-1,-1).
    Per la matrice dell'esempio e k = 1 la funzione restituisce (0, 3).
    '''
    # inserisci qui il tuo codice











