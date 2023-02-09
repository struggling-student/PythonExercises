import my_html
import os


def es73(dir, htmlFile):
    """
    Si definisca la funzione  ricorsiva (o che usa una vostra funzione ricorsiva) es73(dir, htmlfile) che, data una directory,
    ne legge la struttura e costruisce ricorsivamente l'albero dei nodi my_html.HTMLNode
	di un documento html da salvare in un file.
    Argomenti:
        dir:      percorso della directory radice da scandire
        htmlFile: percorso del file html da scrivere
    Tutte le directory o file che iniziano con '.' devono essere ignorate.
    L'albero da costruire deve contenere una serie di liste puntate che elencano i file e le directory trovate secondo la struttura:
    <ul>
        <li>dirRadice
            <ul>
                <li>nomeFile</li>
                <li>nomeDir
                    <ul>
                    <li>nomeFile</li>
                    <li>nomefile</li>
                    </ul>
                </li>
                <li>nomeFile</li>
                <li>nomeDir
                    <ul>
                    <li>nomeFile</li>
                    <li>nomefile</li>
                    </ul>
                </li>
            </ul>
        </li>
    </ul>
    (nota, ho indentato la struttura per farla capire, ma non va fatto altrimenti i file sono diversi)
    Per produrre il file HTML indicato dovete prima costruirne l'albero di my_html.HTMLNode e poi salvarlo su file.
    L'albero deve contenere un nodo con tag="ul" per ogni directory,
    All'interno del tag 'ul' ci devono essere tanti tag='li' quanti sono i file/dir contenuti (in ordina alfabetico).
    Ciascun tag 'li' ha come contenuto il nome del file/dir (sotto forma di un tag='_text_').
    Se si tratta di una directory, dopo il tag '_text_' si aggiunge un tag 'ul' che elenca il contenuto della directory.
    La funzione inoltre ritorna l'albero costruito.
    """
    # inserite qui il vostro codice
