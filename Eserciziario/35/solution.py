import os


def es35(dir1, parole):
    # inizializzo il dizionario con le parole da cercare e i contatori a zero
    diz = {w: [0, 0] for w in parole}
    # scandisco la directory e prendo solo i file con estensione '.txt'
    for fn in os.listdir(dir1):
        if not os.path.isdir(fn) and fn[-4:] == '.txt':
            with open(dir1 + "/" + fn) as f:
                # estraggo le parole dal file, visto che sono separate da spazi/accapo/tab e' sufficiente usare split
                words = f.read().split()
                # per ogni parola nel file, se e' una di quelle cercate incremento il suo conteggio
                for w in words:
                    if w in parole:
                        diz[w][0] += 1
                # per ciascuna parola cercata, se e' nel file incremento il conteggio del numero di files che la contengono
                for p in parole:
                    if p in words:
                        diz[p][1] += 1
    # alla fine torno un dizionario con le sole parole cercate che sono state trovate in qualche file
    return {k: tuple(v) for k, v in diz.items() if v[0]}
