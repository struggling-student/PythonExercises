'''
    Es 9: 3 punti
    Si definisca la funzione es9(pathDir ) ricorsiva (o che fa uso di funzioni o 
    metodi ricorsive/i) che:
    - riceve come argomento l'indirizzo di una cartella.
    - restituisce una lista contenente i nomi delle sottocartelle in essa contenute a
      qualsiasi livello e per ogni sottocartella anche lo spazio  (in byte) occupato all'interno 
      della cartella da eventuali file di tipo .txt.
      La lista contiene dunque coppie, il primo elemento della coppia e' il nome di 
      una sottocartella ed il secondo e' lo spazio occupato dai file .txt presenti nella
      sottocartella.
      Le coppie devono comparire nella lista ordinate in modo decrescente rispetto 
      alla loro seconda componente e  a parita' vanno ordinate poi in modo lessicografico 
      crescente rispetto alla prima componente.
      File e cartelle il cui nome comincia  col carattere '.' non vanno considerati. 
      
      Ai fini dello svolgimento dell'esercizio possono risultare utili 
      le seguenti funzioni nel modulo os:
      os.listdir(), os.path.isfile(), os.path.isdir(), os.path.basename(), 
      os.path.getsize()

    Esempio: con es9('Informatica/Software') viene restituita la lista:
    [('SistemiOperativi', 287), ('Software', 10), ('BasiDati', 0)]

'''
import os

def es9(pathDir):
    valore = prova(pathDir)
    valore+=[pathDir]
    lista_finale=[]
    for el in valore:
      spazio=0
      for percorso in os.listdir(el):
        p=el+'/'+percorso
        if os.path.isfile(p):
          if p[-4:]=='.txt':
            spazio+=os.path.getsize(p)
      lista_finale.append((os.path.basename(el),spazio))
    lista_finale=sorted(lista_finale, key=lambda x: (-x[1],x[0]))
    return lista_finale

def prova(path):
  if os.path.isfile(path):
    return []
  lista=[]
  for elemento in os.listdir(path):
      p=path+'/'+elemento
      lista=lista+prova(p)
      if os.path.isdir(p):
        lista+=[p]
  return lista