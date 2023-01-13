
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
def es29(tabella1,tabella2,col):
    ''' 
    Si implementi la funzione es29(tabella1, tabella2, col) che prese in input
    - due tabelle: tabella1 e tabella2,  rappresentate tramite lista di dizionari ed aventi le stesse colonne
    - una stringa con il nome di una delle colonne delle due tabelle rispetto alla quale le due tabelle sono 
      ordinate in modo crescente.
    modifica distruttivamente la tabella 1.
    Le righe della tabella 1 differiscono tutte nella colonna col  e lo stesso vale per le righe della tabella 2.
    Bisogna inserire nella tabella 1 righe della tabella 2. 
    Una riga della tabella 2 deve essere  inserita nella tabella 1 solo se nella sua colonna  col contiene un valore
    non presente tra quelli che compaiono nella corrispondente colonna della tabella1. 
    Al termine la tabella 1 deve ancora risultare ordinata rispetto ai valori della colonna col.  
    La funzione deve restituire il numero delle righe inserite nella tabella1.  
    Ad esempio con: 
    tabella1=[{'C1': 1, 'C2': 'x'},{'C1': 3, 'C2': 'a'},{'C1': 4, 'C2': 'a' },{'C1': 5, 'C2': 'a' },{'C1': 7, 'C2': 'b' }],
    tabella2=[{'C1': 2, 'C2': 'a'},{'C1': 3, 'C2': 'b'},{'C1': 5, 'C2': 'a' },{'C1': 6, 'C2': 'b' },{'C1': 7, 'C2': 'a' }] 
    al termine di es29(tabella1, tabella2, 'C1') verra' restituito il numero 2 e la tabella1 risultera'
    [{'C1': 1, 'C2': 'x'},{'C1': 2, 'C2': 'a'},{'C1': 3, 'C2': 'a' ,},{'C1': 4, 'C2': 'a' },{'C1': 5, 'C2': 'a' },\
    {'C1': 6, 'C2': 'b' },{'C1': 7, 'C2': 'b' }]
    '''
    # inserisci qui il tuo codice
















  
    
