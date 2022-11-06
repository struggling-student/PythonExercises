
''' 
    Un modo comune di memorizzare tabelle e' come liste di dizionari. 
    Ogni riga della tabella corrisponde ad un dizionario le cui chiavi sono i nomi delle colonne della tabella.
    Questa collezione di dizionari e' poi memorizzata in una lista.
    Ad esempio la tabella
    
    nome  | anno | tel
  --------|------|---------
   Sofia  | 1973 | 5553546 
   Bruno  | 1981 | 5558432

puo' essere memorizzata come 
[{'nome': 'Sofia', 'anno': 1973 ,'tel': 5553546},{'nome': 'Bruno', 'anno': 1981 ,'tel': 5558432}]

'''


def es27(tabella, colonna, valore):
    ''' 
    Si implementi la funzione es27(tabella, colonna, valore) che presi in input
    - una tabella rappresentata tramite lista di dizionari
    - una stringa con il nome di una delle colonne della tabella
    - un valore
    modifica distruttivamente la tabella eliminando  la colonna indicata e 
    le righe che in quella colonna avevano valori diversi da valore.
    La funzione deve poi restituire il numero di righe eliminate.
    Ad esempio con  tabella = [{'nome': 'Sofia', 'anno': 1973 ,'tel': 5553546},
                                {'nome': 'Bruno', 'anno': 1981 ,'tel': 5558432}]
    al termine di es27(dati, 'anno', 1981)  verra' restituito il numero 1 e la tabella 
    risultera'  modificata  in [{'nome': 'Bruno','tel': 5558432}]

    '''
    # inserisci qui il tuo codice
