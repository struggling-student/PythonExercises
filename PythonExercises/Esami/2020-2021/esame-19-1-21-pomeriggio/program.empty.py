################################################################################
################################################################################
################################################################################

''' ATTENZIONE!!! INSERITE QUI SOTTO IL VOSTRO NOME, COGNOME E MATRICOLA '''

nome        = "NOME"
cognome     = "COGNOME"
matricola   = "MATRICOLA"

################################################################################
################################################################################
################################################################################
# SUGGERIMENTI PER IL DEBUG 
#   per eseguire solo parte dei test commentare parte della lista "tests"
#   alla fine di grade.py
#
#   per vedere lo stack trace degli errore scommentate la riga 36 di testlib.py 
################################################################################
################################################################################
################################################################################

################################################################################
################################################################################
################################################################################

'''
   Es 1: punti 7
   Si definisca la funzione es1(line, word) che riceve in ingresso una
   stringa "line" e una parola "word" (rappresentata a sua volta come
   una stringa).  La funziona deve cercare le occorrenze della parola
   dentro la stringa e restituire il numero di occorrenze.  La linea e
   la parola possono contenere caratteri upper case e lower case. La
   parole word deve essere cercata con il suo case opposto (word -->
   WORD oppure WORD --> word).  Se la parola in ingresso presenta case
   misti come 'WoRd' allora la funzione deve restituire -1.

   Ad esempio:
      1) se in ingresso abbiamo 'pippo' come word
      e se la linea è 'pluto   pippo ### paperPIPPOpippoPiPPopipp'
      allora la funzione deve restituire 1.
      2) se in ingresso abbiamo 'PIPPO' come word
      e se la linea è 'pluto   pippo ### paperPIPPOpippoPiPPopipp'
      allora la funzione deve restituire 2.
      3) se in ingresso abbiamo 'PIppO' come word
      e se la linea è 'pluto   pippo ### paperPIPPOpippoPiPPopipp'
      allora la funzione deve restituire -1.
'''


def es1(line, word):
    # scrivi qui il tuo codice
    pass


'''
    Es 2: punti 8

    Si definisca la funzione es2(board) che riceve in ingresso una
    matrice quadrata rappresentata come una lista di liste. La matrice ha lo
    stesso numero di righe e di colonne. La matrice contiene un
    carattere ' ' che rappresenta la posizione vuota. Inoltre la
    matrice puo' contenere altri caratteri diversi da ' '. La funzione
    deve trovare se esiste una riga o una colonna o la diagonale
    principale, o anti-diagonale della matrice che contiene
    elementi tutti dello stesso carattere (ovviamente escluso ' ').
    Se esiste deve ritornare una tupla che contiene:
        (True, lista che contiene gli elementi tutti uguali trovati)
    Se non esiste deve ritornare una tupla che contiene:
        (False, una lista vuota)

    NOTA: il caratter vuoto è ' ' ma gli altri caratteri possono
    variare.
  
    Ad esempio, per la matrice:

    'x'  'x'  'x'  'o'
    ' '  ' '  ' '  'o'
    ' '  ' '  ' '  'o'
    ' '  ' '  ' '  'o'

    si deve restituire (True, ['o','o','o','o'])

    Per:

    '+'  '-'  '-' 
    '+'  ' '  ' '
    '+'  ' '  ' '

    si deve restituire (True, ['+','+','+'])

    Per:

    '+'  '-'  '-' 
    '+'  ' '  ' '
    ' '  ' '  ' '

    si deve restituire (False, [])

    NOTA: Il caso sottostante con 2 o più risultati 
    NON compare nei test:

    '+'  ' '  'o' 
    '+'  ' '  'o'
    '+'  ' '  'o'
'''


def es2(board):
    # scrivi qui il tuo codice
    pass


'''
    Es 3: punti 8

    Si definisca la funzione es3(N) ricorsiva (o che fa uso di
    funzioni o metodi ricorsive/i) che riceve come parametro un numero
    intero N e restituisca tutti i possibli numeri binari codificabili
    su N posizioni.  Più nel dettaglio, N esprime il numero di
    posizioni su cui è possibile enumerare tutti i possibli numeri in
    formato binario.  Il codice deve restituire l'enumerazionde dei
    numeri binari come una lista.  Ogni elemento della lista contiene
    una tupla. La tupla contiene il numero binario secondo la seguente
    convenzione: il primo elemento della tupla contiene una stringa
    che indica il numero binario, il secondo elemento è un intero che
    corrisponde alla conversione in base 10 del numero binario.  La
    lista deve presentare i numeri in maniera ordinata.  
    Vale che N > 0.

    Ad esempio se in ingresso è dato N = 3, allora il codice deve restituire:
    [('000', 0), ('001', 1), ('010', 2), ('011', 3), ('100', 4), ('101', 5), ('110', 6), ('111', 7)]

    Non è necessario usare strutture addizionali per creare l'albero,
    comunque sia per facilitare, l'albero di ricorsione dietro
    l'enumerazione per questo esempio e' il seguente:

             _______|________                             
            |                |                          
            0                1                         
         ___|____         ___|____               
        |        |       |       |             
        0        1       0       1                    
      __|__    __|__   __|__   __|__
     |     |  |     | |     | |     |
     0     1  0     1 0     1 0     1
 
    NOTA: definite le vostre sottofunzioni a livello esterno
          altrimenti non passate il test di ricorsione
    '''


def es3(N):
    # scrivi qui il tuo codice
    pass


'''
    Es. 4: punti 9
    
    Si realizzi la funzione ricorsiva (o che usa funzioni ricorsive)
    che riceve come argomento il nome di una directory (dirname).
    Dirname può contenere altre directory e/o altri files e così via
    ricorsivamente.  La funzione ricorsiva deve esplorare le directory
    cercando quelle che sono "affette" da un possibile
    "virus". All'interno di ogni directory possono esserci un numero
    variabile di file testuali e altri file che iniziano con un punto
    (.). I file che iniziano con "." vanno ignorati.  Ogni file
    contiene l'informazione su una o più directory del livello
    corrente per capire se è affetta o meno da virus. Il file contiene
    del testo seguendo la convenzione "directory,virus". Le coppie
    nomedir,virus sono sempre contenute su una linea, ma possono
    essere presenti tabulazione e spazi. Fra diverse coppie, inoltre,
    possono, essere presenti anche linee vuote. Una directory non è
    affetta da virus se la stringa dopo "," contiene "None". Per
    riferimento si vedano i file xxx, yyy in dir_a. La funzione
    richiesta esplora la directorydirname e le sue sottodirectory alla
    ricerca tutte le directory che sono affette da virus e restituisce
    un dizionario. Se una directory non e' affetta da virus allora
    nemmeno le sue sottocartelle lo saranno e non conterrà nessun
    file. Le chiavi del dizionario sono tutte directory che sono
    affette da virus. Ogni directory usa il percorso relativo che
    parte dalla directory di partenza dirname.  Attributo di ciascuna
    chiave è il "tipo" di virus per quella dir.Ad esempio con dirname='dir_a'
    la funzione es4 deve restituire il dizionario:
    {'dir_a/aaa': 'trojan', 'dir_a/bbb': 'maleware',
         'dir_a/aaa/bbb': 'trojanhorse'}
   
    NOTA: è proibito usare la funzione os.walk 
    NOTA: definite le
    vostre sottofunzioni a livello esterno altrimenti non passate il
    test di ricorsione '''   


import os
def es4(dirname):
    # scrivi qui il tuo codice
    pass

######################################################################################################

if __name__ == '__main__':
    pass
    # inserisci qui i tuoi test