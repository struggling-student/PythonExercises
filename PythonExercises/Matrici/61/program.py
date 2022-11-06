

def es61(ftesto, op, sel):
    '''
    La funzione es62(ftesto, op, sel) che, legge una matrice di interi contenuta
    nel file di testo ftesto e restituisce una lista di interi.
    La matrice e' memorizzata nel file per righe con  gli interi nelle righe separati da un numero
    arbitrario di spazi.
    La lista da tornare contiene i risultati di una operazione da effetture sulle righe, le colonne
    o le diagonali della matrice. Il parametro 'op' specifica il tipo di operazione, e
    puo' assumere tre diversi valori:
        'max' (per il calcolo del massimo),
        'min' (per il calcolo del minimo)
        e 'sum' (per il calcolo della somma).
    Il parametro 'sel' specifica su quali elementi della matrice  l'operazione deve operare.
    puo' assumere i seguenti valori:
        'row' (per applicarla alle varie righe della  matrice, in ordine crescente),
        'col' (per applicarla alle varie colonne della  matrice, in ordine crescente),
        'dp' (per applicarla  alla diagonale principale)
        e 'ds' per applicarla alla diagonale  secondaria.
    Ad esempio se la matrice contenuta nel file di testo e':
    2  0   -4
    5  10  20
    5  1   -1

    a seconda dei parametri si avra':

    es61(ftesto, 'max','row')= [2, 20, 5]
    es61(ftesto, 'min','row')= [-4, 5,-1]
    es61(ftesto, 'sum','row')= [-2, 35, 5]
    es61(ftesto, 'max','col')= [ 5,  10, 20]
    es61(ftesto, 'min','col')= [ 2,  0, -4]
    es61(ftesto, 'sum','col')= [ 12, 11, 15]
    es61(ftesto, 'max','dp' )= [10]
    es61(ftesto, 'min','dp' )= [-1]
    es61(ftesto, 'sum','dp' )= [11]
    es61(ftesto, 'max','ds' )= [10]
    es61(ftesto, 'min','ds' )= [-4]
    es61(ftesto, 'sum','ds' )= [11]
    '''
    # inserisci qui il tuo codice
