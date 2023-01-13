import albero

'''
    Es 1: 3 punti
    Si definisca la funzione es7(tree,insieme,k ) ricorsiva (o che fa uso 
    di funzioni o metodi ricorsive/i) che:
    - riceve come argomenti:
      - l'albero 'tree'  formato da nodi del tipo Nodo definito nella libreria 
        albero.py allegata, 
      - un insieme di caratteri 
      - un intero k
    - torna come risultato il numero di nodi dell'albero aventi 
      ESATTAMENTE  k figli i quali hanno  identificatori   
      presenti nell'insieme.
    
    Esempio: sia k=2 e ins={1,2,3,5,9}, allora la funzione es1
    - sull'albero a sinistra deve restituire 2 (per i figli dei nodi 4 e 2)
    - sull'albero a destra deve restituire 3 (per i figli dei nodi 7, 9 e 10).


              5                                     7              
      ________|_____________                _______|______         
     |          |           |              |              |        
     20         4           6              5              9        
     |     _____|______                 ___|___        ___|__      
     11   |   |  |  |  |               |       |      |      |     
          10  2  9  8  7               10      8      3      1     
            __|__                     _|_     _|_    _|_    _|_    
           |     |                   |   |   |   |  |   |  |   |   
           3     1                   1   2   12  13 15  6  4   0   
                                                                   
    '''


def es7(tree,insieme,k):
    pass
