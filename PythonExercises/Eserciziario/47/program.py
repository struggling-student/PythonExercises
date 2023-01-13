
def es47(lista):
    '''
    progettare la funzione es47(lista) che
    prende in input una lista di stringhe, e restituisce una lista di stringhe.
    La lista da restituire e' quella che si ottiene dalla lista di input dopo averne eliminato i duplicati,
    e in cui le stringhe sono state ordinate per lunghezza crescente ed a parita' di lunghezza  per ordine
    lessicografico decrescente.
    Al termine della funzione la lista passata in input non deve risultare modificata.

    Ad esempio: per lista=[ 'uuu','ccc','a','aa','d','z','zzz','uuu','z','z','uuu']:
    e la funzione restituira' la lista
    ['z','d','a','aa','zzz','uuu','ccc']
    mentre la lista di input non risultera' modificata.
    '''
    return sorted(set(lista), key=lambda x : (-len(x),x),reverse=True)
        
lista=[ 'uuu','ccc','a','aa','d','z','zzz','uuu','z','z','uuu']
print(es47(lista))

