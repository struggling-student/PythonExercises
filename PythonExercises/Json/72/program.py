import os
import json
import os.path


def es72(dir, jsonFile):
    """
    Si definisca la funzione  ricorsiva (o che usa una vostra funzione ricorsiva) es72(dir, jsonfile) che, 
    data una directory, ne legge la struttura costruisce ricorsivamente un dizionario da salvare come Json.
    Tutti i file e directory che iniziano con '.' devono essere ignorati.
    Argomenti:
        dir:      percorso della directory da leggere
        jsonFile: percorso del file json da scrivere
    Il dizionario deve contenere come chiavi i nomi dei file/directories e come valori:
        - se si tratta di un file, la sua dimensione (intero)
        - se si tratta di una directory, il dizionario che ne descrive il contenuto
    Il dizionario piu' esterno contiene come chiave il solo nome della directory fornita come argomento.
    La funzione inoltre ritorna il massimo numero di files/dir contenuto in una delle directory/sottodirectory.
    """
    # inserite qui il vostro codice

