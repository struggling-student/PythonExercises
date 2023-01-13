COPYRIGHT
=========
Copyright (C) 2019- Andrea Sterbini <sterbini@di.uniroma1.it>, 
                    Angelo Monti <monti@di.uniroma1.it>, 
                    Matteo Neri <matteo2794@outlook.com>

Tutti i programmi ed i file contenuti in questo archivio/directory sono rilasciati sotto licenza GPL v.3 
(https://www.gnu.org/licenses/gpl-3.0.en.html)

ISTRUZIONI
==========
Per svolgere l'esercizio editate il file program.py usando un editor di testi, meglio ancora un IDE.
Vanno bene Notepad++, Atom, Spyder, PyCharm ed altri editor di testo. 
NON usate Notepad, Word, Wordpad o altri editor di documenti.

TEST
====
Questa directory contiene i file necessari a verificare, su almeno 3 esempi di input, che il vostro programma sia corretto.
Prima di eseguire i test se necessario installate Python e le librerie necessarie (vedi sotto).

Per controllare se il vostro programma funziona bene sui dati di esempio:
- aprite una finestra Anaconda Prompt e posizionatevi nella directory dell'esercizio (usando il comando cd)
- eseguite il comando:
	python test.py
- oppure
	pytest test.py

Per ottenere informazioni più dettagliate sull'esecuzione (con una analisi dei tempi spesi nelle diverse parti del programma)
- eseguite invece il comando
	pytest -v -rA --profile test.py

SOLUZIONE
=========
Nella directory è inclusa una nostra soluzione dell'esercizio.
Vi consigliamo di esaminarla SOLO DOPO AVER PROVATO A RISOLVERE L'ESERCIZIO DA SOLI.

INSTALLAZIONE
=============
Per poter eseguire questi test o quelli di un altro esercizio installate (va fatto una sola volta):
- la distribuzione Anaconda nella versione che contiene Python 3.x (da https://www.anaconda.com/distribution/)
- i moduli Python seguenti
   Aprite un Anaconda Prompt ed eseguite i comandi
	conda install -c conda-forge pytest
	conda install -c conda-forge ddt
	conda install -c conda-forge pytest-timeout
	conda install -c conda-forge pytest-profiling

