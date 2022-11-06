def es24(ifile, l):
    '''
    Scrivere la funzione es24(filename, listacar) che prende in input il nome di un file
    e una lista di caratteri e produce una lista di tuple. (carattere, stringa)
    Per ogni carattere nella lista di caratteri si calcola la
    sua percentuale di occorrenze nel contenuto del file ignorando le differenze 
    tra maiuscola e minuscola. 
    Ciascuna tupla del risultato ha come primo elemento un carattere della lista
    e come secondo elemento la stringa che si ottiene dalla percentuale 
    rispetto al numero totale di caratteri alfabetici (ovvero per cui isalpha() e' True)
    arrotondata alla seconda cifra decimale seguita dal carattere '%'.
    La lista di tuple deve essere ordinata in ordine decrescente di percentuale, 
    a parita' di stringa percentuale le tuple devono essere ordinate alfabeticamente.

    Es: se il file 'pippo' contiene la sequenza di caratteri "sono proprio cOntentO", 
    la chiamata es24('pippo',['o','i', 'S']) ritorna la lista
    [('o', '31.58%'), ('S', '5.26%'), ('i', '5.26%')]
    '''
    pass
