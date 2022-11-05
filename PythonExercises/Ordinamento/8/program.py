'''    
Es 3: 3 punti
due parole possono fondersi se la prima ha un suffisso di almeno due caratteri 
che coincide col prefisso di pari lunghezza della seconda. 
Il risultato della fusione e' la parola che si ottiene concatenando la prima parola 
con la seconda grazie alla parte comune.
Ad esempio:  
- le due parole 'candela' ed 'elastico' possono fondersi grazie al suffisso 
  'ela' di  3 caratteri, il risultato della fusione e' la parola  'candelastico' 
_ le parole 'Angelo' e 'gelo' possono fondersi grazie al suffisso 'gelo', la parola 
  risultante e''Angelo'. 
_ le parole 'aaaaa' e 'aaab' possono fondersi in diversi, modi: 
    _ grazie al suffisso 'aa' si ottiene la fusione 'aaaaaab' 
    _ grazie al suffisso 'aaa' si ottiene la fusione 'aaaaab'.
  Si definisca la  funzione es2(insieme) che, dato un insieme di parole, restituisce 
  la lista con tutte le possibili fusioni. 
  La lista deve risultare ordinata lessicograficamente e vanno eliminati eventuali 
  duplicati.
  
ESEMPIO: 
se  insieme={  'aaaa', 'acde', 'aacd', 'aaaade'} la funzione restituira' la lista: 
['aaaaaade', 'aaaaade', 'aaaacd', 'aaaade', 'aacde'] 
grazie alle seguenti fusioni:
'aaaa'  'aaaade' ---> 'aaaaaade' con suffisso 'aa'
'aaaa'  'aaaade' ---> 'aaaaade'  con suffisso 'aaa'
'aaaa'  'aaaade' ---> 'aaaade'   con suffisso 'aaaa'
'aaaa'  'aacd'   ---> 'aaaacd'   con suffisso 'aa'
'aacd'  'acde'   ---> 'aacde'    con suffisso 'acd'
'''
def es8(insieme):
  lista=[]
  for parola in insieme:
    for parola2 in insieme-{parola}:
      for i in range(2,len(parola)+1):
        if parola[-i:]==parola2[:i]:
            lista.append((parola+parola2[i:]))
        else: continue
  # se lo trasformo in un set non ci sono duplicati
  lista = set(lista)
  lista = list(lista)
  lista.sort()
  return lista

#insieme={  'aaaa', 'acde', 'aacd', 'aaaade'}
#print(es8(insieme))