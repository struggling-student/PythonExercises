################################################################################
################################################################################
################################################################################

""" Operazioni da svolgere PRIMA DI TUTTO:
 1) Salvare questo file come program.py
 2) Indicare nelle variabili in basso il proprio
    NOME, COGNOME e NUMERO DI MATRICOLA"""
import json

nome        = "NOME"
cognome     = "COGNOME"
matricola   = "MATRICOLA"

################################################################################
################################################################################
################################################################################
# ---------------------------- SUGGERIMENTI PER IL DEBUG --------------------- #
# Per eseguire solo alcuni dei test, si possono commentare le voci con cui la
# lista 'test' è assegnata alla fine di grade.py
#
# Per controllare lo stack trace degli errori, si può decommentare la linea
# dedicata in testlib.py (vedere il commento nel corpo della funzione runOne)
################################################################################


# ----------------------------------- EX.1 ----------------------------------- #
'''
Es1: 7 punti
    Si scriva una funzione ex1(file_rows, file_cols, file_values) che
    prende in ingresso i percorsi di 3 file e restituisca in output
    una matrice, rappresentata come lista di liste.  Scopo
    dell'esercizio è ricostruire una matrice "out" codificata mediante
    tre matrici, "rows", "cols" e "values". A loro volta, le tre
    matrici sono codificate in tre file di testo i cui nomi sono dati
    in ingresso: file_rows, file_cols, file_values.

    I file contengono su diverse righe dei numeri interi separati da
    spazi e da una virgola (ogni intero è seguito da una virgola). Ogni
    riga del file è una riga della matrice, ovvero il c-esimo numero
    su una data riga corrisponde al c-esimo elemento (la colonna c)
    della riga corrispondente.  Ad esempio, se il file contiene:

    0  ,   1          ,     2,
    0,1,2,


    la matrice codificata come lista di liste è:

    [[0, 1, 2],
     [0, 1, 2]].

    La matrice "out" da restituire ha nella posizione (r,c) l'elemento
    della matrice "values" individuato dagli indici (i,j) tali che
    r = rows(i,j) e c = cols(i,j).
    Le dimensioni di "out" sono ottenibili osservando il massimo indice di riga
    e colonna presenti rispettivamente in "rows" and "cols".
    Nell'esempio sottostante la matrice "out" ha dimensioni 3x6 in quanto
    il massimo indice su "rows" e' 2 e su "cols" e' 5.

    Per tutti gli altri
    indici che non compaiono né in "rows" né in
    "cols", si deve scrivere None. Nel caso in cui
    "values" non sia accessible alla posizione (i,j), in quanto
    gli indici (i,j) sbordano dalla matrice "values", si deve scrivere la somma di
    tutti i valori di "cols" tranne quello alla posizione (i,j).

    Ad esempio: dati i tre file di ingresso che codificano le matrici
          "rows"              "cols"                     "values"
     0     1     2     |   1     5     3     |     5       2
     0     1     2     |   0     2     4     |     -10     3

    si deve restituire:

    "out" con dimensione 3x6:

    [[-10, 5, None, None, None, None],
    [None, None, 3, None, None, 2],
    [None, None, None, 12, 11, None]]

    infatti:
    - alla posizione di "out" (0,1) vi è 5 perché è stato prelevato da
    values alla posizione (0,0) e scritto in out(0,1), infatti
    rows(0,0) = 0 e cols(0,0) = 1.
    - in tutte le posizioni di "out" non indicizzate da "rows" e "cols" vi è None
    - alla posizione out(2,3) vi è 12 in quanto (2,3) non è accessible
    da "values" e quindi è sostituito con la sommma di cols (15) meno
    cols(0,2) (3) ossia 12.

    Nota: "rows" e "cols" hanno stesse dimensioni fra loro.
          "vals" può avere dimensioni diverse da "rows" e "cols".
'''

def leggimatrice(filename):
    M = []
    with open(filename, encoding='utf8') as F:
        for line in F:
            line = line.replace(',',' ')
            row = list(map(int, line.split()))
            M.append(row)
    return M

def ex1(file_rows, file_cols, file_values):
    rows = leggimatrice(file_rows)
    H    = max(map(max, rows)) + 1
    cols = leggimatrice(file_cols)
    W    = max(map(max, cols)) + 1
    vals = leggimatrice(file_values)
    M    = [ [None]*W for _ in range(H)]
    Somma= sum(map(sum, cols))
    print(rows, cols)
    # per tutte le coordinate della destinazione
    for y in range(H):
        for x in range(W):
            # per tutte le coordinate delle matrici si cerca una coppia che indica la posizione y,x
            for Y,riga in enumerate(rows):
                for X,R in enumerate(riga):
                    # se le coordinate ci sono
                    if R == y and cols[Y][X] == x:
                        # se vals[Y][X] non esiste
                        try:
                            M[y][x] = vals[Y][X]
                        except:
                            M[y][x] = Somma - cols[Y][X]
    return M


# ----------------------------------- EX.2 ----------------------------------- #

'''Ex2: 7 points
    
    A gang of space intruders is invading the pictures on our hard drive.
    Design and implement a function ex2(image_file, space_intruder_pic_file)
    that helps us find out the exact location of the space intruder
    (whose picture is stored in space_intruder_pic_file) inside the image
    (image_file).

    Both space_intruder_pic_file and image_file are paths to PNG images.

    The function should return a pair (x,y) with the x and y coordinates (from
    the top-left corner down to the bottom-right one) of the space intruder
    in the image, if it is entirely there (that is, if the whole space
    intruder's picture lies within the area of the image). If the indicated
    space intruder is not in the image (or only partially there), then the
    function should return (-1, -1).
     
    For example, if space_intruders_pic_file is "img/napoleon.png" and
    space_intruder_pic_file is "intruder-10.png", the function should return
    (79, 61). Notice that if space_intruders_pic_file is "img/napoleon.png"
    and space_intruder_pic_file is "intruder-11.png", the function should
    return (-1, -1) as that space intruder is not in the picture.
'''
import images

def ex2(image_file, space_intruder_pic_file):
    img = images.load(image_file)
    W,H = len(img[0]), len(img)
    spc = images.load(space_intruder_pic_file)
    sW,sH = len(spc[0]), len(spc)
    for x in range(W-sW):
        for y in range(H-sH):
            for Y,row in enumerate(spc):
                if row != img[y+Y][x:x+sW]:
                    break
            else:
                return x, y
    return (-1, -1)

# ----------------------------------- EX.3 ----------------------------------- #

'''Es3: 6+4 punti
    Date le informazioni genealogiche di una famiglia, vogliamo individuare
    quali sono gli eredi di un/a defunto/a.

Le informazioni sulla famiglia sono descritte da un dizionario che contiene:
    - come chiavi il nome di ciascuna persona presente nella famiglia
    - come valore associato a ciascuna chiave le informazioni relative a quella persona:
        'nomedellapersona' : { 
                'parents' : [ lista dei nomi dei genitori (se conosciuti) ],
                'spouse'  : nome del/la compagna/o (oppure None se non sposata/o o divorziata/o),
                'alive'   : True se vivo/a, False se deceduta/a,
                }

NOTA: non esistono persone con lo stesso nome.
NOTA: per ogni persona X che appare nelle proprietà di qualche persona, X esiste sempre nel dizionario principale.
NOTA: potete assumere che se un nome X è 'spouse' di Y allora Y è 'spouse' di X.
NOTA: possono esistere persone (divorziati o conviventi) che hanno dei figli in comune ma non sono sposate.
NOTA: possono esistere persone (sposate in seconde nozze) che hanno alcuni figli non in comune (da precedenti matrimoni)

Parte 1: 6 punti
    Realizzate la funzione avi(name, family), ricorsiva, che riceve come argomenti:
    - nome:    il nome di uno dei familiari, di cui vogliamo sapere tutti gli avi e la distanza dalla persona
    - family:  dizionario che descrive una famiglia, secondo il formato descritto prima
    NOTA: il dizionario family NON deve essere modificato
    La funzione deve tornare un dizionario che ha:
    - come chiavi il nome della persona e di tutti i suoi avi (usando SOLO la relazione 'parents' e non 'spouse')
    - come valore la corrispondente distanza minima dalla persona (che è 0 per la persona stessa)
    NOTA: le famiglie usate per i test possono contenere persone che hanno fatto figli con dei propri congiunti
    per cui lo stesso avo può apparire a distanze diverse a seconda di quale ramo di parentela si segue,
    in questo caso prendete la distanza MINIMA 
    (si veda il file families/Kassie.pdf come esempio degli avi di Kassie nella famiglia families/big.json)

Esempio: se la famiglia è la seguente (MAIUSCOLA=donna, minuscola=uomo)                        
                           a/B                    R/s
            ________________|___________________  |
            |         |            |            | |
            c         D            E            f/Q
       _____|___             ______|____   _____|__________
       |       |             |     |   |   |        |     |
       G       h             i     J   k   L        M     n

avi('L', family) tornerà il dizionario {'L':0, 'f':1, 'Q':1, 'R':2, 's':2, 'a':2, 'B':2}
'''
def avi(name, family):
    # scrivete qui il vostro codice
    return avi_(name, family, 0)

'''
Parte 2: 4 punti
    Realizzate la funzione ex3(family, name) che riceve come argomenti:
    - family:  dizionario che descrive una famiglia, secondo il formato descritto prima
    - nome:    il nome di uno dei familiari di cui vogliamo sapere gli eredi (viventi)
    NOTA: il dizionario family NON deve essere modificato
    Per individuare eredi seguite le seguenti regole, da applicare nell'ordine:
    - se ha compagno/a E/O ha figli viventi ereditano SOLO il/la compagno/a ed i figli 
    - se non ha figli nè compagno/a
        - ereditano i congiunti più vicini fino al 6° grado
    La funzione deve tornare come risultato un insieme che contiene i nomi dei soli eredi del/la defunto/a

Ad esempio se le persone (e la loro relazione genitore/figlio) sono le seguenti
          Carlo + Lucia
                |              
             Aurora - Giovanni
            ________|_________
            |                |
           Ciro            Federica 
gli eredi di Ciro sono solo Aurora e Giovanni visto che Ciro non ha nè figli nè moglie 
ed i suoi genitori sono vivi e sono più vicini (1 grado) della sorella Federica (2° grado).

Nota: Il grado di parentela è il numero minimo di relazioni di parentela da attraversare per andare da una persona all'altra.
Le relazioni da considarare sono esclusivamente quelle genitore-figlio (e non quelle date dal matrimonio).
In pratica per calcolare la distanza tra due persone X,Y bisogna:
 - ricavare gli avi di X e di Y con le loro distanze da X e da Y usando la funzione avi(persona, famiglia)
 - trovare l'avo comune Z tale che il percorso X--Z--Y è minimo
 - (se non esiste avo comune X ed Y non sono imparentati)
 
Esempio: se la famiglia è la seguente (MAIUSCOLA=donna, minuscola=uomo)                        
                           a/B                    R/s
            ________________|___________________  |
            |         |            |            | |
            c         D            E            f/Q
       _____|___             ______|____   _____|__________
       |       |             |     |   |   |        |     |
       G       h             i     J   k   L        M     n

Il grado di parentela tra G e J è 4 (il percorso più breve che li unisce è G-c-a/B-E-J e contiene 4 archi) 
infatti G e J hanno in comune gli avi a, B
'''
def ex3(family, name):
    # TODO
    # find inheritors
    return inheritors(name, family)

def avi_(person, family, d=0):
    '''torna tutti gli avi della persona e la loro distanza'''
    result = { person: d }
    for p in family[person]['parents']:
        for a,D in avi_(p, family, d+1).items():
            if a not in result:
                result[a] = D
            else:
                result[a] = min(D, result[a])
    return result

def distance(person, other, family):
    ''' torna la distanza tra due persone qualsiasi
        torna None se non hanno avi in comune'''
    avi1 = avi(person, family)
    avi2 = avi(other, family)
    common = set(avi1) & set(avi2)
    if common:
        return min( avi1[c]+avi2[c] for c in common )
    else:
        return None

def inheritors(person, family):
    '''torna gli eredi'''
    P = family[person]
    sons = [ s for s,v in family.items() if person in v['parents'] and v['alive'] ] # keep only alive sons
    SO   = P['spouse']
    if SO and not family[SO]['alive']:
        SO = None    # is the wife dead? ignore her
    # - if wife or sons: wife + sons
    if SO or sons:
        return { SO } | set(sons)
    # altrimenti non ci sono nè figli nè SO
    assert not sons
    assert not SO

    possible = {p:distance(person, p, family) for p,v in family.items() if v['alive']}
    if person in possible:
        del possible[person] # remove myself
    for p,v in possible.copy().items():
        if not v:
            del possible[p]  # remove 0 distance
    # find minimum distance
    if possible:
        D = min( possible.values() )
        if D > 6:
            return set()
        return { x for x,d in possible.items() if d == D }
    else:
        return set()


# filename = f'families/big'
# with open(f'{filename}.json') as FJ:
#     family = json.load(FJ)
#     print(avi('Kassie', family))

# ----------------------------------- EX.4 ----------------------------------- #

'''Es4: 8 points [BASED ON A TRUE STORY]

    An AI researcher tested some automated reasoning tools. These tools return
    one out of three possible results: 'sat', 'unsat', 'timeout' (in case the
    computation took too long). The researcher let those tools run on a
    number of benchmarks and collected the results in a rather peculiar way:
    given a root directory (e.g., "testbed/00") that contains all the results
    gathered during the "testbed/00" series of experiments,
    the first sub-directories of the root specify the tool names (e.g.,
    "fastsolver" and "powertool"). Then, for every tool-directory, each path to
    a text file identifies a benchmark. The text file contains the result of the
    automated reasoing task.
    
    For example, under "testbed/00" we have
    "fastsolver/alaska/demo-v2/demo-v-00.txt" and
    "powertool/alaska/demo-v2/demo-v-00.txt".
    Both files contain the string "sat", which means that both tools
    returned the same result.
    
    Notice that the sole filename does not suffice to uniquely identify a
    test: indeed, under "testbed/00" we have also
    "fastsolver/alaska/demo-v3/demo-v-00.txt" and
    "powertool/alaska/demo-v3/demo-v-00.txt",
    which are different tests than the ones listed above (see the "demo-v3"
    directory name in place of "demo-v2").
    
    Also, it might happen that some tools did not run over a given
    benchmark, thus some files or entire sub-directories could be missing
    under a tool whereas they occur under other tools
    (e.g., under "testbed/00/powertool" we have
    "alaska/demo-v2/demo-v-02.txt" though it does not occur under
    "testbed/00/fastsolver").
    
    To help our researcher properly summarise the results of the
    experiments, design and implement a function ex4(testbed_dir) such that:
    - it is recursive or uses recursive function(s)/method(s);
    - it receives the root directory (testbed_dir) with the test results,
      nested as explained above 
    - it returns the following data structure.
    
    The returned data structure is a pair containing
    1) the set of all tools used in this test (e.g., for ""testbed/00" the set
       should be {"fastsolver", "powertool"}), as per the subdirectories of
       testbed_dir;
    2) a dictionary that has
       as a key, the test name (e.g., "alaska/demo-v3/demo-v-00.txt"), and
       as the value, a dictionary associating to every tool its result on
         that benchmark (e.g., {'powertool': 'unsat', 'fastsolver': 'sat'}).

    The result of ex4("testbed/00"), for example, should be:
    ( {'powertool', 'fastsolver'}, 
      {'alaska/demo-v3/demo-v-00.txt': {'powertool': 'unsat', 'fastsolver': 'sat'},
       'alaska/demo-v2/demo-v-00.txt': {'powertool': 'sat', 'fastsolver': 'sat'},
       'alaska/demo-v2/demo-v-01.txt': {'powertool': 'sat', 'fastsolver': 'sat'},
       'alaska/demo-v2/demo-v-02.txt': {'powertool': 'sat'}}
    ).
'''
import os

def ex4(testbed_dir):
    tools = os.listdir(testbed_dir)
    results = {}
    for tool in tools:
        findresults(testbed_dir, tool, '', results)
    return set(tools), results

def findresults(path, tool, test, results):
    for name in os.listdir(f"{path}/{tool}/{test}"):
        fullname = f"{path}/{tool}/{test}/{name}"
        if os.path.isfile(fullname):
            test1 = test[1:] + '/' + name   # tolgo il primo carattere '/'
            with open(fullname) as F:
                if test1 not in results:
                    results[test1] = {}
                results[test1][tool] = F.read().strip()
        else:
            findresults(path, tool, f"{test}/{name}", results)

################################################################################
if __name__ == '__main__':
    # Insert your own tests here
    pass
    # print(ex4("testbed/00"))
    # print(ex4("testbed/01"))
    # print(ex4("testbed/02"))
    # print(ex4("testbed/03"))
