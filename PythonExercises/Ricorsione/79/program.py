
def es79(lista):
    '''
    Si definisca la funzione ricorsiva (o che usa una vostra funzione ricorsiva) es79(lista).
    La funzione prende in input una lista che puo' essere vuota, contenere interi e/o altre liste del suo stesso tipo.
    Al termine della funzione la lista deve risultare invertita e lo stesso deve accadere 
    a tutte le liste in essa contenute, ricorsivamente.
    Inoltre la funzione restituisce una tupla di tre elementi.
    Al primo posto della tupla deve comparire il numero totale di interi presenti nella lista e nelle sue sottoliste. 
    Al secondo posto della tupla deve comparire la somma di tutti gli interi presenti nella lista e nelle sue sottoliste.
    Al terzo posto della tupla deve comparire la lista, ordinata in modo crescente, contenente una sola volta i
    differenti interi presenti nella lista e nelle sue sottoliste.
    Ad esempio, se all'inizio la lista e'
     lista = [3, 3, 5, [[1, 8, [9, 3]], 3, [2, [9, [5, 6],[9]] ] ]]
    alla fine la lista dev'essere
     lista = [[[[[9], [6, 5], 9], 2], 3, [[3, 9], 8, 1]], 5, 3, 3]
    la funzione es79(lista) restituisce la tupla 
    (13, 66, [1, 2, 3, 5, 6, 8, 9])
     ''' 
    