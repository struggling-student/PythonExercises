# ----------------------------------- EX.3 ----------------------------------- #

'''Es3: 9 punti
    Data la storia di una famiglia (che ne comprende nascite, matrimoni, divozi, decessi)
    vogliamo individuare, nel momento in cui una delle persone è deceduta,
    quali ne erano gli eredi e che percentuale della eredità spetta a ciascuno di loro.

    La storia è rappresentata in un file che contiene su righe separate i diversi eventi.
    Gli eventi sono di 4 tipi e sono rapprsentati dai seguenti template:
        - <data>    MATRIMONIO    spos1    spos2
        - <data>    NASCITA   nome del figlio  genitore1    genitore2
        - <data>    DECESSO   nome del defunto
        - <data>    DIVORZIO  nome di uno degli sposi
    tutte le informazioni sono separate da tab ('\t')

    Esempio
    se il file contiene le righe:
10/03/1900  MATRIMONIO  Carlo   Lucia
21/12/1900  NASCITA Aurora  Lucia   Carlo
27/08/1931  MATRIMONIO  Aurora   Giovanni
12/08/1932  NASCITA Ciro    Aurora   Giovanni
12/08/1933  NASCITA Federica   Giovanni    Aurora
15/08/1985  DECESSO Ciro
25/09/1960  DIVORZIO    Aurora

Che corrispondono alla foresta seguente
          Carlo + Lucia
                |
             Aurora - Giovanni
            ________|_________
            |                |
           Ciro            Federica

Gli eredi di Ciro sono solo Aurora e Giovanni visto che non aveva nè figli nè moglie
e sono più vicini della sorella Federica.

NOTA: non esistono persone con lo stesso nome.
NOTA: potete assumere che tutte le date siano diverse.
NOTA: potete assumere che le persone citate ma non "nate" erano già presenti all'inizio della storia.

    Realizzate la funzione es3(storia, nome) che riceve come argomenti:
    - storia:  il path di un file di testo contenente la storia di una famiglia
    - nome:    il nome di uno dei familiari deceduti (assumete che l'evento del suo decesso appaia sempre nella storia)
    La funzione es3 deve leggere il file e ricostruire la situazione dell'albero genealogico della famiglia
    al momento del decesso della persona 'nome'.
    Quindi deve individuare quali sono gli eredi del/la defunto/a e la loro percentuale di eredità.
    Per individuare eredi e percentuali seguite le seguenti regole, nell'ordine:
    - se il/la defunt/a ha compagno/a ma non ha figli il/la compagno/a eredita tutto
    - se ha figli ma non ha compagno/a i figli ereditano in parti uguali
    - se ha compagno/a E ha 1 figlio entrambi ereditano la metà
    - se ha compagno/a E ha più di 1 figlio
        il/la compagno/a eredita 1/3
        ed i figli ereditano 2/3 divisi in parti uguali tra tutti i figli
    - se non ha figli nè compagno/a
        - ereditano i congiunti più vicini fino al 6° grado, in parti uguali
    NOTA: la funzione es3 deve essere o fare uso di funzioni/metodi ricorsivi (ad esempio per individuare gli eredi).
    La funzione deve tornare come risultato un dizionario che contiene:
    - come chiavi i nomi dei soli eredi del/la defunto/a
    - come valore la percentuale di eredità spettante a quella persona (come float)

Per costruire l'albero genealogico usate la classe Persona definita sotto che rappresenta una persona
e le informazioni ad essa pertinenti:
    - viva/morta
    - compagno/a
    - figli
    - genitori
    - ...
Aggiungete a vostro piacimento i metodi necessari ad esplorare o modificare la geanalogia.

Nota: Il grado di parentela è il numero di relazioni di parentela da attraversare per andare da una persona all'altra.
Le relazioni da considarare sono esclusivamente quelle genitore-figlio.

Esempio: se l'albero in un certo momento è il seguente (MAIUSCOLA=donna, minuscola=uomo)

                           a/B
            ________________|___________________
            |         |            |            |
            c         D            E            f
       _____|___             ______|____   _____|__________
       |       |             |     |   |   |        |     |
       G       h             i     J   k   L        M     n

Il grado di parentela tra G e J è 4 (il percorso più breve che li unisce è G-c-a/B-E-J e contiene 4 archi)

'''


class Persona:
    ''' La classe che rappresenta le persone non ha nozione del tempo,
    perchè simuliamo la storia della famiglia solo fino al decesso della persona indicata
    ovvero la gestione dell'ordine di simulazione è fatta nella funzione principale'''
    persone = {}  # elenco di tutte le persone conosciute

    @classmethod
    def get(cls, nome):
        '''Ricava la persona che ha un certo nome oppure la crea se non esiste'''
        if nome not in cls.persone:
            cls.persone[nome] = Persona(nome)
        return cls.persone[nome]

    def __init__(self, nome):
        '''Questo metodo viene usato per creare una qualsiasi persona'''
        self.nome = nome  # nome della persona
        self.figli = []  # riferimenti ai figli
        self.genitori = []  # riferimenti ai genitori
        self.SO = None  # riferimento al/lla compagno/a
        self.alive = True  # per default la persona è viva

    def __repr__(self):
        return self.nome

    @classmethod
    def asJson(cls):
        return {n: p.as_json() for n, p in cls.persone.items()}

    def as_json(self):
        return {
            'name': self.nome,
            'sons': [s.nome for s in self.figli],
            'parents': [p.nome for p in self.genitori],
            'spouse': self.SO.nome if self.SO else None,
            'alive': self.alive,
        }

    @classmethod
    # <data>    NASCITA   nome del figlio  nome della madre    nome del padre
    def NASCITA(cls, nome, genitore1, genitore2):
        figlio = cls.get(nome)
        g1 = cls.get(genitore1)
        g2 = cls.get(genitore2)
        g1.figli.append(figlio)
        g2.figli.append(figlio)
        figlio.genitori = g1, g2

    @classmethod
    # <data>    DECESSO   nome del defunto
    def DECESSO(cls, nome):
        cls.get(nome).alive = False

    @classmethod
    # <data>    MATRIMONIO    nomi degli sposi
    def MATRIMONIO(cls, nome, SO):
        p1 = cls.get(nome)
        p2 = cls.get(SO)
        p1.SO, p2.SO = p2, p1

    @classmethod
    # <data>    DIVORZIO  nome di uno degli sposi
    def DIVORZIO(cls, nome):
        p = cls.get(nome)
        p.SO.SO = None  # p smette di essere SO del suo SO
        p.SO = None  # p non ha più SO

    def eredi(self):
        '''Calcola la lista degli eredi secondo le regole date'''
        # trova i parenti fino al 6° grado (parenti torna {nome: grado} )
        parentela = {p: g for p, g in self.parenti().items() if g <= 6}
        genitori = [g for g in self.genitori if g.alive]
        figli = [f for f in self.figli if f.alive]
        SO = self.SO
        # TODO: regole per stabilire gli eredi
        print(f'''
        {nome=}
            {parentela=}
            {genitori=}
            {figli=}
            {SO=}
        ''')

    def parenti(self):
        return {p: p.distanza(self) for p in self.persone.values() if p.distanza(self)}

    def avi(self, d=0):
        risultato = {self: d}
        risultato.update({a: D for g in self.genitori for a, D in g.avi(d + 1).items()})
        return risultato

    def distanza(self, other):
        avi1 = self.avi()
        avi2 = other.avi()
        # se hanno un avo in comune prendiamo il più vicino
        comuni = set(avi1) & set(avi2)
        if comuni:
            d1 = min(avi1[x] for x in comuni)
            d2 = min(avi2[x] for x in comuni)
            print(self, avi1, '\n\t', other, avi2, d1 + d2)
            return d1 + d2
        else:
            return 10 ** 4


def ex3(storia, nome):
    pass

    def date(evento):
        dd, mm, yy = evento[0].split('/')
        return yy, mm, dd

    # Inserire qui il proprio codice
    # leggo gli eventi
    with open(storia, encoding='utf8') as F:
        eventi = [line.split() for line in F]
    # li ordino per data crescente
    eventi.sort(key=date)
    # li eseguo nell'ordine
    for data, tipo, persona, *altri_parametri in eventi:
        print(f"{tipo} {persona} {altri_parametri}")
        getattr(Persona, tipo)(persona, *altri_parametri)
        # fermandomi al decesso della persona indicata
        if tipo == 'DECESSO' and nome == persona:
            break
    import json
    with open(storia + '.json', mode='w', encoding='utf8') as F:
        json.dump(Persona.asJson(), F, indent=4)
    # a questo punto la simulazione è ferma al decesso della persona indicata
    morto = Persona.get(nome)
    # TODO:
    # trovare gli eredi secondo le regole e la percentuale di eredità associata
    eredi = morto.eredi()
    # tornarli


print(ex3('families/example.txt', 'Ciro'))
