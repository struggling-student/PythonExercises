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
    if not word.islower() and not word.isupper():
        return -1
    word_t = word.upper() if word.islower() else word.lower()
    w_size = len(word)
    count = 0
    for i in range(len(line)):
        if line[i:i+w_size] == word_t:
            count += 1
    return count


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


    NOTA: Il caso sottostante con 2 risultati 
    NON compare nei test:

    '+'  ' '  'o' 
    '+'  ' '  'o'
    '+'  ' '  'o'
'''


def es2(board):
    def check(uniq):
        return len(uniq) == 1 and ' ' not in uniq

    R = len(board)
    C = len(board[0])
    # rows and cols and diags
    uniq_dsx, uniq_ddx = set(), set()
    for c in range(C):
        uniq_c = set()
        for r in range(R):
            if c == 0:
                uniq_r = set(board[r])
                # check rows
                if check(uniq_r):
                    return (True, [uniq_r.pop()]*C)
                # add diags
                uniq_dsx.add(board[r][r])
                uniq_ddx.add(board[r][R-r-1])
        if c == 0:
            # check diags
            if check(uniq_dsx):
                return (True, [uniq_dsx.pop()]*R)
            if check(uniq_ddx):
                return (True, [uniq_ddx.pop()]*R)
            # add cols
            uniq_c.add(board[r][c])
        # check cols
        if check(uniq_c):
            return (True, [uniq_c.pop()]*R)
    return (False, [])


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


def enum_bin(n, bits=str(), digits=None):
    if digits is None:
        digits = []
    if n == 0:
        digits = [*digits, (bits, int(bits, 2))]
        return bits[:-1], digits
    bits += '0'
    bits, digits = enum_bin(n-1, bits=bits, digits=digits)
    bits += '1'
    bits, digits = enum_bin(n-1, bits=bits, digits=digits)
    return bits[:-1], digits


def es3(N):
    _, digits = enum_bin(N)
    return digits


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
    del testo seguendo la convenzione "directory,virus" ma sono
    presenti linee vuote, tabulazione e spazi. Una directory non è
    affetta da virus se la stringa dopo "," contiene "None". Per
    riferimento si vedano i file xxx, yyy in dir_a. La funzione
    richiesta esplora la directory dirname e le sue sottodirectory
    alla ricerca tutte le directory che sono affette da virus e
    restituisce un dizionario. Se una directory non e' affetta da
    virus allora nemmeno le sue sottocartelle lo saranno e non
    conterrà nessun file. Le chiavi del dizionario sono tutte
    directory che sono affette da virus. Ogni directory usa il
    percorso relativo che parte dalla directory di partenza dirname.
    Attributo di ciascuna chiave è il "tipo" di virus per quella dir.
    Ad esempio con dirname='dir_a'
    la funzione es4 deve restituire il dizionario:
    {'dir_a/aaa': 'trojan', 'dir_a/bbb': 'maleware',
         'dir_a/aaa/bbb': 'trojanhorse'}
   
    NOTA: è proibito usare la funzione os.walk 
    NOTA: definite le
    vostre sottofunzioni a livello esterno altrimenti non passate il
    test di ricorsione '''   


import os
def nav_dirs(dir_name, res=None):
    if res is None:
        res = {}

    list_items = os.listdir(dir_name)
    list_dirs, list_files = [], []
    for item in list_items:
        f_path = os.path.join(dir_name, item)
        if not item.startswith('.') and os.path.isfile(f_path):
            list_files.append(f_path)
        elif os.path.isdir(f_path):
            list_dirs.append(f_path)
        else:
            pass

    for f in list_files:
        with open(f) as fr:
            lines = fr.readlines()
            out = list(map(lambda x: (x.split(',')[0].strip(),
                                      x.split(',')[1].strip()),
                           filter(lambda x: ',' in x, lines)))
            for dirr, virus in out:
                f_path = os.path.join(dir_name, dirr)
                if 'None' not in virus:
                    res[f_path] = virus    

    # going in recursion
    for dirr in list_dirs:
        if dirr in res:
            res = nav_dirs(dirr, res=res)
    return res


def es4(dirname):
    return nav_dirs(dirname)

######################################################################################################
