import immagini


def es74(filePng, centro, spessore, colori, pngFileOut):
    """
    Si definisca la funzione  es9(filePng, centro, spessore, colori, pngFileOut) che,
    data una immagine png, ci disegna sopra una serie di anelli colorati e salva l'immagine in un secondo file PNG.
    La funzione torna una lista contenente il numero di pixel colorati di ciascun colore, nell'ordine.
    Nota:   per evitare errori da arrotondamento non calcolate la distanza di un pixel dal centro con la radice quadrata
            ma confrontate la somma del quadrato dei cateti con il quadrato del raggio del cerchio corrente (insomma usate Pitagora)
    Nota:   per ciascun anello
            i pixel sul bordo interno devono essere compresi      ( usate il confronto >= )
            mentre quelli sul bordo esterno devono essere esclusi ( usate il confronto <  )
    :param filePng:     percorso del file PNG contenente l'immagine da modificare
    :param centro:      coppia (x, y) che indica le coordinate del centro del bersaglio
    :param spessore:    spessore degli anelli
    :param colori:      lista di colori da applicare in ordine dal centro fino all'anello piu' esterno
    :return:            lista col numero di pixel colorati di ciascun colore
    """
    # inserite qui il vostro codice
