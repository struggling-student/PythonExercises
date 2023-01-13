

def es64(l):
    '''
    Scrivere la funzione es64 che prende come input una lista di
    interi non negativi e produce una stringa contenente i numeri della lista in verticale,
    una cifra per riga, allineando le cifre delle unita' alla riga piu' in basso.

    Es: es64([5,69,2090]) torna la stringa
        2
        0
      6 9
    5 9 0
    '''
    # inserite qui il vostro codice
    m = max(l)
    righe = len(str(m))
    lista = ["{:{r}}".format(valore, r=righe) for valore in l]
    risultato = "\n".join(" ".join)
    print(risultato)
print(es64([5,69,2090]))
