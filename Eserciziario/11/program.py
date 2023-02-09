'''
    Es 11: 3 punti
progettare la funzione es11(ftesto) che, preso in input 
l'indirizzo di un file di testo restituisce un dizionario avente per chiavi delle stringhe 
ed attributo liste di  stringhe.
Il file di testo contiene stringhe distinte di caratteri, si guardi 
ad esempio il file f9.txt. 
Le chiavi del dizionario si ottengono dalle stringhe presenti nel file dopo aver 
eliminato da queste le vocali ed aver riordinato lessicograficamente i caratteri rimanenti 
(ad esempio dalla stringa 'angelo' si ottine la chiave 'gln').
Attributo della chiave e' la lista contenente le stringhe del file che l'hanno generata. 
Nota che  stringhe diverse possono generare una stessa chiave come nel caso 
di  'casa', 'caso' e 'cose'
Le stringhe nella lista devono comparire  ordinate per lunghezza decrescente, a parita' 
di lunghezza, lessicograficamente.

Ad Esempio, per il file di testo f10.txt  la funzione restituisce  il dizionario:
{'prt': ['parto', 'porta'], 
'r': ['era', 'ora'], 
'pr': ['arpia', 'arpa'], 
'cs': ['casa', 'cosa'], 
'fll': ['follia', 'fallo', 'folla'], 
'rt': ['otre', 'tre'], 
'lp': ['piolo', 'polo']
}
'''

def es11(ftesto):
    with open(ftesto, 'r') as f:
        testo = f.read()
    testo = testo.split()
    dic = dict()
    for parola in testo:
        nuova_parola = []
        for lettera in parola:
            if lettera not in 'aeiou':
                nuova_parola.append(lettera)
        nuova_parola.sort()
        chiave = ''.join(nuova_parola)
        if chiave in dic:
            dic[chiave].append(parola)
        else: dic[chiave] = [parola]
    for chiave in dic:
        lista = dic[chiave]
        lista = sorted(lista, key=lambda x: (-len(x),x))
        dic[chiave]=lista
    return dic
    
#print(es11('/Users/lucian/Documents/GitHub/UniExercises/PythonExercises/Stringhe/11/ft10a.txt'))
