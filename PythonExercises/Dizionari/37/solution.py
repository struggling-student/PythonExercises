def es37(listaDizionari):
    # devo tenere solo le chiavi che appaiono in almeno N/2 dizionari
    # quindi per prima cosa le conto
    N = len(listaDizionari)
    conta = {}
    # per ciascun dizionario e per ciascuna chiave, conto quante volte la chiave appare
    for d in listaDizionari:
        for k in d:
            if k in conta:
                conta[k] += 1
            else:
                conta[k] = 1
    # una volta contate passo a raccogliere per ciascuna chiave che appare piu' di N/2 volte
    # tutti i valori comuni a tutti i dizionari (unione degli insiemi di valori)
    diz = {}
    for d in listaDizionari:
        for k, v in d.items():
            if conta[k] >= N/2:
                if k in diz:
                    diz[k] = diz[k].union(v)
                else:
                    diz[k] = set(v)
    return diz
