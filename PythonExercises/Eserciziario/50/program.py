

def es50(s,k):
    '''
    progettare la funzione es50(s,k) che: 
    - riceve  in input una stringa s di caratteri che sono le cifre da  '0' a '9'  ed un intero k 
    - costruisce la lista con  le diverse sottostringhe  di s i cui caratteri sono in 
      ordine strattamente crescente.
    - restituisce la lista dopo averne ordinato gli elementi in ordine decrescente
   Nota che la lista non deve contenere duplicati. 
   Si ricorda che una sottostringa di s e' quello che si ottiene da s eliminando 0 o piu' 
    caratteri iniziali  e 0 o piu' caratteri finali.                                        
   ESEMPI: 
   con  s='9135918246556' e k=3 la funzione restituisce la lista ['359','246', 135']
   con  s='1234123412341234' e k=3 la funzione restituisce la lista ['234',123']
   con  s='987654321' e k=3 la funzione restituisce la lista []
    '''
    # inserisci qui il tuo codice
    sotto_stringhe = { s[i:i+k] for i in range(len(s)-k+1)}
    result = []
    for stringa in sotto_stringhe:
       a,b,c = stringa
       if (int(a)<int(b)<int(c)):
        result.append(stringa)
    return sorted(result, key=lambda x:-(int(x)))
print(es50('9135918246556',3))






