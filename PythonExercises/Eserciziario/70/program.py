import os
import os.path


def es70(dir, estensioni, parole):
    """
    Si definisca la funzione  ricorsiva (o che usa una vostra funzione ricorsiva) es70(dir, estensioni, parole),
    che deve contare quante volte le parole indicate sono presenti nei files che NON hanno le estensioni indicate,
    e che riceve come argomenti:
        dir: la directory in cui cercare
        estensioni: una lista di stringhe "estensioni" (le ultime lettere del nome dei files che evitiamo)
        parole: una lista di stringhe che non contengono spazi/tab/accapo, che vanno cercate nei files
                senza considerare la differenza tra maiuscole e minuscole.
    La funzione deve tornare un dizionario contenente come chiavi le parole cercate (in minuscolo)
    e come valori il numero di volte (>0) che queste parole appaiono (indipendentemente dalle maiuscole/minuscole)
    complessivamente nei files che NON hanno le estensioni indicate.
    Nota: una parola non deve apparire nel dizionario in output se nessun file con estensione diversa da quelle indicate la contiene.
    Nota: assumete che tutti i file presenti nelle directories siano file di testo indipendentemente dalla loro estensione.

    Test:   date alcune directory che contengono alcuni file con estensioni diverse a diverse profondita',
            contare alcune parole (in mixed-case) e controllare il dizionario risultante
    Test:   che la funzione sia ricorsiva
    """
    # inserite qui il vostro codice
