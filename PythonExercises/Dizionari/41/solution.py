def es41(fname1):
    # visto che la sequenza contenuta nel file e' separata solo da virgole e spazi uso split sulle virgole
    # e poi converto ciascun frammento di testo in un numero
    with open(fname1, encoding='utf8') as f:
        sequenza = [int(x) for x in f.read().split(',')]

    # la sequenza derivata inizia col primo numero della sequenza originale
    derivata = [sequenza[0]]
    # gli altri si ottengono sommando il prossimo numero della sequenza originale all'ultimo inserito
    for el in sequenza[1:]:
        derivata.append(derivata[-1]+el)
    # ottenuta la sequenza derivata conto il numero di volte che i valori vi appaiono
    freq = {}
    for x in derivata:
        if x in freq:
            freq[x] += 1
        else:
            freq[x] = 1
    # per ottenere il valore che appare piu' volte, ed a pari merito e' il piu' grande
    # costruisco una lista di coppie (conteggio, valore) e ne cerco il massimo
    # (perche' nel confronto tra due tuple, i confronti vengono fatti nell'ordine da sinistra verso destra)
    coppie = [(v, k) for k, v in freq.items()]
    # il secondo valore della coppia massima e' il valore cercato
    return max(coppie)[1]
