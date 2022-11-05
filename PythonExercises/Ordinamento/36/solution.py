def es36(listaDizionari):
    # devo trovare l'insieme delle chiavi che appaiono in tutti i dizionari
    # lo inizializzo con le chiavi del primo dizionario
    keys = set(listaDizionari[0].keys())
    # e lo aggiorno facendo l'intersezione con l'insieme delle chiavi di ciascuno degli altri dizionari
    for d in listaDizionari[1:]:
        keys = keys.intersection(d.keys())
    # quindi ripeto sui valori lo stesso meccanismo solo per le chiavi ottenute
    # inizializzo tutti i valori delle chiavi con gli insiemi dei valori del primo dizionario
    diz = {k: set(v) for k, v in listaDizionari[0].items() if k in keys}
    # e poi per ciascun dizionario e per ciascuna chiave
    for d in listaDizionari[1:]:
        for k, v in d.items():
            if k in diz:
                # aggiorno i valori tenendo solo quelli comuni (intersezione)
                diz[k] = diz[k].intersection(v)
    # alla fine ordino i valori associati a ciascuna chiave (ottenendo liste ordinate)
    return {k: sorted(v) for k, v in diz.items()}
