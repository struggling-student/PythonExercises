

# Una matrice si dice sparsa se ha pochi valori diversi da zero. Per risparmiare spazio 
# di memoria, anzicche' utilizzare liste di liste  possiamo rappresentare matrici 
# sparse tramite dizionari. Il dizionario di una matrice sparsa M ha come chiavi delle tuple  
# e come attributo degli interi. Le tuple sono coppie e la coppia (i,j) e' presente nel dizionario 
# se e solo se M[i][j] e' diverso  da zero. L'attributo della chiave (i,j) sara' poi proprio M[i][j].
# ad ESEMPIO il dizionario 
# d={(0,2): 4,(1,0): 1, (1,1): 2, (2,1):8 } rappresenta la matrice quadrata  M=
# | 0 0 4 |
# | 1 2 0 |
# | 0 8 0 |

def es52(d1,d2):
    '''
    Si definisca la  funzione es52(d1,d2) che, 
    - riceve due dizionari di matrici sparse della stessa dimenzione.
    - restituisce un dizionario con la matrice sparsa somma delle due matrici avute in input.
    Ad ESEMPIO se
    d1={(0,2): 4,(1,0): 1, (1,1): 2, (2,1):8 } e d2={(0,0): 5,(1,1): 2, (2,2): 5, (1,0):2 }
    allora la funzione restituira' il dizionario 
    {(0,2): 4,(1,0): 3, (1,1): 4, (2,1):8, (0,0):5, (2,2):5 }
    I dizionari ricevuti non devono essere modificati
    '''
    # inserisci qui il tuo codice

