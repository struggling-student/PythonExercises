################################################################################
################################################################################
################################################################################

""" Operazioni da svolgere PRIMA DI TUTTO:
 1) Salvare questo file come program.py
 2) Indicare nelle variabili in basso il proprio
    NOME, COGNOME e NUMERO DI MATRICOLA"""

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

    - La matrice "out" da restituire ha nella posizione (r,c)
    l'elemento della matrice "values" individuato dagli indici (i,j)
    tali che r = rows(i,j) e c = cols(i,j).
    - Le dimensioni della matrice "out" possono essere recuperate
    osservando il massimo dei valori di "rows" e "cols". In
    particolare, il massimo dei valori di "rows" e "cols" corrisponde
    rispettivamente all'ultimo indice di riga e colonna scrivibile in
    "out".  
    - Per tutti gli altri indici non specificati da "rows" e "cols" e
    si deve scrivere None.
    - Nel caso in cui "values" non sia accessible alla posizione
    (i,j), in quanto gli indici (i,j) sbordano dalla matrice "values",
    si deve scrivere la somma di tutti i valori di "cols" tranne
    quello alla posizione (i,j).
 
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
    - in tutte le posizioni di "out" non indicizzate da "rows" e
      "cols" vi è None
    - alla posizione out(2,3) vi è 12 in quanto (2,3) non è accessible
    da "values" e quindi è sostituito con la sommma di cols (15) meno
    cols(0,2) (3) ossia 12.

    Nota: "rows" e "cols" hanno stesse dimensioni fra loro.
          "vals" può avere dimensioni diverse da "rows" e "cols".
'''

def ex1(file_rows, file_cols, file_values):
    pass
    # Inserire qui il proprio codice


# ----------------------------------- EX.2 ----------------------------------- #

'''Es2: 7 punti

    Un gruppo di space intruders sta cercando di "invadere" le
    immagini sul nostro disco rigido. Progetta e implementa una
    funzione ex2(image_file, space_intruder_pic_file) che ci aiuta a
    trovare la locazione esatta dello space intruder nell'immagine
    specificata da image_file. L'immagine dello space intruder da
    cercare è specificata da space_intruder_pic_file.

    Sia space_intruder_pic_file che image_file sono percorsi a file
    che puntano ad immagini PNG.

    La funzione deve ritornare una coppia (x,y) con x e y le
    coordinate dello space intruder nell'immagine, se lo space
    intruder è contenuto interamente nell'immagine indicata da
    image_file (ossia se l'intera immagine dello space intruder giace
    nell'immagine image_file). (x,y) rappresenta il pixel più in alto
    a sinistra dell'immagine image_file in cui inizia l'immagine dello
    space intruder. Se l'immagine dello space intruder fornita non è
    nell'immagine o è anche parzialmente contenuta in essa, allora la
    funzione deve restituire (-1,-1).

    Il sistema di coordinate dell'immagine ha l'origine in alto a
    sinistra ed è orientato dal alto verso il basso, e da sinistra
    verso destra.

    Ad esempio, se image_file è "img/pastel.png" e
    space_intruder_pic_file è "intruder-00.png", la funzione deve
    restituire (91,52). Si noti che se image_file è "img/napoleon.png"
    e space_intruder_pic_file è "intruder-00.png", la funzione deve
    rendere (-1,-1) poiché lo space intruder non è nell'immagine.  
'''

import images

def ex2(image_file, space_intruder_pic_file):
    pass
    # Inserire qui il proprio codice


# ----------------------------------- EX.3 ----------------------------------- #
'''Es3: 6+4 punti
    Date le informazioni genealogiche di una famiglia, vogliamo
    individuare quali sono gli eredi di un/a defunto/a.

    Le informazioni sulla famiglia sono descritte da un dizionario che
    contiene: 
    - come chiavi il nome di ciascuna persona presente nella famiglia
    - come valore associato a ciascuna chiave le informazioni relative
      a quella persona:

        'nomedellapersona' : { 
                'parents' : [ lista dei nomi dei genitori 
                                              (se conosciuti) ],
                'spouse'  : nome del/la compagna/o 
                                   (oppure None se non sposata/o
                                    o divorziata/o),
                'alive'   : True se vivo/a, False se deceduta/a,
                }

    NOTA: non esistono persone con lo stesso nome.
    NOTA: per ogni persona X che appare nelle proprietà di qualche
    persona, X esiste sempre nel dizionario principale.
    NOTA: potete assumere che se un nome X è 'spouse' di Y allora Y è
    'spouse' di X.
    NOTA: possono esistere persone (divorziati o conviventi) che hanno
    dei figli in comune ma non sono sposate.
    NOTA: possono esistere persone (sposate in seconde nozze) che
    hanno alcuni figli non in comune (da precedenti matrimoni)

Parte 1: 6 punti
    Realizzate la funzione avi(name, family), ricorsiva, che riceve
    come argomenti:

    - nome: il nome di uno dei familiari, di cui vogliamo sapere tutti
      gli avi e la distanza dalla persona
    - family: dizionario che descrive una famiglia, secondo il formato
      descritto prima

    NOTA: il dizionario family NON deve essere modificato

    La funzione deve tornare un dizionario che ha:
    - come chiavi il nome della persona e di tutti i suoi avi (usando
      SOLO la relazione 'parents' e non 'spouse')
    - come valore la corrispondente distanza minima dalla persona (che
      è 0 per la persona stessa)

    NOTA: le famiglie usate per i test possono contenere persone che
    hanno fatto figli con dei propri congiunti per cui lo stesso avo
    può apparire a distanze diverse a seconda di quale ramo di
    parentela si segue, in questo caso prendete la distanza MINIMA (si
    veda il file families/Kassie.pdf come esempio degli avi di Kassie
    nella famiglia families/big.json)

    Esempio: se la famiglia è la seguente (MAIUSCOLA=donna,
    minuscola=uomo)
                        
                           a/B                    R/s
            ________________|___________________  |
            |         |            |            | |
            c         D            E            f/Q
       _____|___             ______|____   _____|__________
       |       |             |     |   |   |        |     |
       G       h             i     J   k   L        M     n

    avi('L', family) tornerà il dizionario
    {'L':0, 'f':1, 'Q':1, 'R':2, 's':2, 'a':2, 'B':2}
'''


## Ex3a
def avi(name, family):
    pass
    # scrivete qui il vostro codice

    
'''
Parte 2: 4 punti
    Realizzate la funzione ex3(family, name) che riceve come
    argomenti:

    - family: dizionario che descrive una famiglia, secondo il formato
      descritto prima
    - nome: il nome di uno dei familiari di cui vogliamo sapere gli
      eredi (viventi)

    NOTA: il dizionario family NON deve essere modificato

    Per individuare eredi seguite le seguenti regole, da applicare
    nell'ordine:
    - se ha compagno/a E/O ha figli viventi ereditano SOLO il/la
      compagno/a ed i figli
    - se non ha figli nè compagno/a, ereditano i congiunti più vicini
      fino al 6° grado

    La funzione deve tornare come risultato un insieme che contiene i
    nomi dei soli eredi del/la defunto/a

    Ad esempio se le persone (e la loro relazione genitore/figlio)
    sono le seguenti:

          Carlo + Lucia
                |              
             Aurora - Giovanni
            ________|_________
            |                |
           Ciro            Federica 
 
    gli eredi di Ciro sono solo Aurora e Giovanni visto che Ciro non
    ha nè figli nè moglie ed i suoi genitori sono vivi e sono più
    vicini (1 grado) della sorella Federica (2° grado).

    Nota: Il grado di parentela è il numero minimo di relazioni di
    parentela da attraversare per andare da una persona all'altra.

    Le relazioni da considarare sono esclusivamente quelle
    genitore-figlio (e non quelle date dal matrimonio).

    In pratica per calcolare la distanza tra due persone X,Y bisogna:
       - ricavare gli avi di X e di Y con le loro distanze da X e da Y
         usando la funzione avi(persona, famiglia)
       - trovare l'avo comune Z tale che il percorso X--Z--Y è minimo
       - (se non esiste avo comune X ed Y non sono imparentati)
 
    Esempio: se la famiglia è la seguente (MAIUSCOLA=donna,
    minuscola=uomo)
                           a/B                    R/s
            ________________|___________________  |
            |         |            |            | |
            c         D            E            f/Q
       _____|___             ______|____   _____|__________
       |       |             |     |   |   |        |     |
       G       h             i     J   k   L        M     n

     Il grado di parentela tra G e J è 4 (il percorso più breve che li
     unisce è G-c-a/B-E-J e contiene 4 archi) infatti G e J hanno in
     comune gli avi a, B
'''


## Ex3b
def ex3(family, name):
    pass
    # Inserire qui il proprio codice


# ----------------------------------- EX.4 ----------------------------------- #
'''Es4: 8 points [TRATTO DA UNA STORIA VERIA]

    Un ricercatore in IA ha testato dei tools per reasoning
    automatico.  Questi tools forniscono come output tre possibli
    risultati: 'sat', 'unsat', 'timeout' (in case il calcolo impieghi
    troppo tempo).
    Il ricercatore lascia eseguire i tools su un numero di benchmarks
    e colleziona i risultati in un modo particolare: data una
    directory root ("testbed/00") che contiene tutti i risultati
    collezionati durante la serie di esperimenti marcati "testbed/00",
    la prima sottodirectory della root indica il nome del tool
    ("fastsolver" e "powertool"). Poi, per ogni directory dei tool,
    ogni percorso ad un file di testo identifica il benchmark. Il file
    di testo contiene il risultato del task automatico di reasoning.
 
    Per esempio, sotto "testbed/00" abbiamo
    "fastsolver/alaska/demo-v2/demo-v-00.txt" e
    "powertool/alaska/demo-v2/demo-v-00.txt".  Entrambi i files
    contengono la stringa "sat", il che significa che entrambi i tools
    hanno fornito il solito risultato.
       
    Si nota che un solo filename non è sufficiente per identificare
    unicamente un test: infatti, sotto "testbed/00" abbiamo anche
    "fastsolver/alaska/demo-v3/demo-v-00.txt" e
    "powertool/alaska/demo-v3/demo-v-00.txt", che sono test diversi
    rispetto a quello elencato prima (si veda la dir "demo-v3" al
    posto di "demo-v2").
    
    Inoltre, potrebbe succedere che qualche tools non esegua su un
    particolare benchmark, e quindi qualche files o la sottodirectory
    completa potrebbero non essere presenti, mentre lo sono per quanto
    riguarda altri tools (in "testbed/00/powertool" abbiamo
    "alaska/demo-v2/demo-v-02.txt" anche se non si verifica in
    "testbed/00/fastsolver").
    
    Per aiutare il nostro ricercatore a fare una sintesi dei risultati
    degli esperimenti, progetta e implementa una funzione
    ex4(testbed_dir) tale che:
    - deve essere ricorsiva o usare funzioni ricorsive al suo interno
    - riceve come input la directory di root (testbed_dir)
      con i test annidati come spiegato sopra.
    - deve restituire la seguente struttura dati.
    
    La struttua dati di output è una coppia che contiene: 
    1) l'insieme (set) di tutti i tools usati per questo test 
     (for ""testbed/00" il set è {"fastsolver", "powertool"}) 
    2) un dizionario che ha come chiave, il nome del test
    ("alaska/demo-v3/demo-v-00.txt"), e come valore un altro
    dizionario che associa ad ogni tool il risultato su quel benchmark
    ({'powertool': 'unsat', 'fastsolver': 'sat'}).

    Il risultato di ex4("testbed/00") è:
    ( {'powertool', 'fastsolver'}, 
      {'alaska/demo-v3/demo-v-00.txt':
              {'powertool': 'unsat', 'fastsolver': 'sat'},
       'alaska/demo-v2/demo-v-00.txt': 
              {'powertool': 'sat', 'fastsolver': 'sat'},
       'alaska/demo-v2/demo-v-01.txt': 
              {'powertool': 'sat', 'fastsolver': 'sat'},
       'alaska/demo-v2/demo-v-02.txt':
              {'powertool': 'sat'}}
    ).
'''

import os

def ex4(testbed_dir):
    pass
    # Inserire qui il proprio codice
