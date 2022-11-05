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


def es26(tabella, colonna):
    ''' 
    Si implementi la funzione es26(tabella,colonna) che presi in input
    - una tabella rappresentata tramite lista di dizionari
    - una stringa con il nome di una delle colonne della tabella
    modifica distruttivamente la tabella riordinandone le righe in ordine decrescente rispetto 
    ai valori contenuti nella  colonna indicata. La funzione deve restituire il numero di colonne della tabella.
        Ad esempio con  tabella = [{'nome': 'Bruno', 'anno': 1981 ,'tel': 5558432},
                        {'nome': 'Sofia', 'anno': 1973 ,'tel': 5553546}]
    al termine di es26(dati, 'anno')  la  tabella sara' stata modificata in 
    [{'nome': 'Bruno', 'anno': 1981 ,'tel': 5558432},{'nome': 'Sofia', 'anno': 1973 ,'tel': 5553546}]
    e restituisce il numero di colonne 3.
    '''
    # inserisci qui il tuo codice
