'''
Si vuole calcolare la classifica finale di un campionato di calcio.
L'input è contenuto in un file di testo in cui su righe separate sono presenti, separate da spazi:
    - il nome della squadra "in casa"
    - il numero di goal da lei subiti
    - il nome della squadra "ospite"
    - il numero di goal da lei subiti

Si implementi la funzione ex1(file_partite, file_classifica) 
che riceve come argomenti:
    - file_partite: il nome del file txt che contiene i dati delle partite
    - file_classifica: il nome del file .txt in cui scrivere la classifica
alla fine la funzione deve ritornare il numero di squadre che hanno partecipato al torneo.

Il file di output deve contenere la classifica finale:
    - ordinata in ordine decrescente di punti finali
        - in caso di parità si considererà la classifica limitata ai soli scontri diretti tra le squadre a pari merito
        - in caso di ulteriore parità vince chi ha fatto più goal in trasferta negli scontri diretti
        - in caso di ulteriore parità vince chi ha subito meno goal in trasferta negli scontri diretti
        - in caso di ulteriore parità si usi l'ordine alfabetico crescente
    - ogni riga contiene, separate da spazi:
        - nome della squadra
        - numero di punti totali
        - numero di goal fatti
        - numero di goal subiti
'''

def ex1(file_partite, file_classifica):
    classifica = {}
    with open(file_partite) as F:
        for line in F:
            incasa, presi, ospite, dati = line.split()
            presi = int(presi)
            dati  = int(dati)
            if presi == dati:
                puntiin, puntiout = 1, 1
            elif presi > dati:
                puntiin, puntiout = 0, 3
            else: 
                puntiin, puntiout = 3, 0
            if incasa not in classifica:
                classifica[incasa] = { 'punti':0, 'dati':0, 'presi':0 }
            if ospite not in classifica:
                classifica[ospite] = { 'punti':0, 'dati':0, 'presi':0 }
            classifica[incasa]['punti'] += puntiin
            classifica[incasa]['dati']  += dati
            classifica[incasa]['presi'] += presi
            classifica[ospite]['punti'] += puntiout
            classifica[ospite]['dati']  += presi
            classifica[ospite]['presi'] += dati
    for k,v in sorted(classifica.items(), key=lambda kv: ( -kv[1]['punti'], kv[0])):
        print(k, v['punti'], v['dati'], v['presi'], sep='\t')

ex1('campionato.txt','')

