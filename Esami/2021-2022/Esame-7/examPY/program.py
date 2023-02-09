#!/usr/bin/env python3
# -*- coding: utf-8 -*-
################################################################################
################################################################################
################################################################################

""" Operazioni da svolgere PRIMA DI TUTTO:
 1) Salvare questo file come program.py
 2) Indicare nelle variabili in basso il proprio
    NOME, COGNOME e NUMERO DI MATRICOLA
 3) Rinominare la directory examPY con il proprio numero di matricola
"""
nome        = "NOME"
cognome     = "COGNOME"
matricola   = "MATRICOLA"

################################################################################
################################################################################
################################################################################
# ---------------------------- SUGGERIMENTI PER IL DEBUG --------------------- #
# Per eseguire solo alcuni dei test, si possono commentare le voci con cui la
# lista 'test' è assegnata alla fine di grade.py
#
# Per controllare lo stack trace degli errori, si può decommentare la linea
# dedicata in testlib.py (vedere il commento nel corpo della funzione runOne)
################################################################################
# ----------------------------------- EX.1 ----------------------------------- #
''' Ex 1: 7 punti
    Si implementi una funzione che prende in ingresso tre nomi di file
    e restituisce una coppia di numeri interi.
    I parametri file1 e file2 sono stringhe contenenti i nomi di due file
    di testo. Questi file contengono, su ogni riga, una serie di stringhe
    separate da spazi, tabulazioni, virgole o punti e virgola.
    La funzione deve scrivere all'interno di un nuovo file indicato da
    file3 una riga per ogni riga di file1 la cui corrispondente riga in
    file2 ha almeno una stringa in comune. In particolare:
        - date le stringhe della riga i-esima di file1, se la riga i-esima
          di file2 contiene almeno una di tali stringhe, allora in file3
          sarà presente una riga con tutte le stringhe in comune.
        - Le stringhe in comune sono scritte nelle righe di file3 separate
          da uno spazio e ordinate per numero di caratteri crescente e, in
          caso di parità, in ordine alfabetico.
        - Le righe in file3 hanno lo stesso ordine delle righe di origine.
    La funzione ritorna una tupla in cui il primo e il secondo elemento
    sono, rispettivamente, il numero di stringhe e il numero di righe
    scritte in file3.
'''
def ex1(file1, file2, file3):
    # una riga per ogni riga di file1 la cui corrispondente riga in file2
    # ha almeno una stringa in comune.
    f1 = open(file1, "r")
    f2 = open(file2, "r")
    f3 = open(file3, "w")
    l1 = f1.readlines()
    l2 = f2.readlines()
    stringcount = 0
    rowcount = 0
    for i in range(len(l1)):
        L1 = l1[i]
        L2 = l2[i]
        L1 = L1.replace("\n", "")
        L1 = L1.replace("\t", " ")
        L1 = L1.replace(",", " ")
        L1 = L1.replace(";", " ")
        L2 = L2.replace("\n", "")
        L2 = L2.replace("\t", " ")
        L2 = L2.replace(",", " ")
        L2 = L2.replace(";", " ")
        ws1 = L1.split(" ")
        ws1 = [x for x in ws1 if x != ""]
        ws2 = L2.split(" ")
        ws2 = [x for x in ws2 if x != ""]
        ws3 = []
        for w1 in ws1:
            if w1 in ws2:
                ws3.append(w1)
        if ws3 != []:
            ws3 = sorted(ws3,key=lambda x: (len(x), x))
            f3.write(" ".join(ws3)  + '\n')
            stringcount += len(ws3)
            rowcount += 1
    #(numero di stringhe, numero di righe) in file 3.
    return (stringcount, rowcount)
# ----------------------------------- EX.2 ----------------------------------- #
''' Ex. 2: 7 punti
    Si scriva una funzione ex2(gridFilePath) che, data una griglia NxN
    contenuta in un file json come una lista di liste, restituisce un
    intero positivo. Nella griglia fornita come input, ogni cella può
    avere uno dei tre valori seguenti:
       - il valore 0 rappresenta una cella vuota;
       - il valore 1 rappresenta un'arancia matura;
       - il valore 2 rappresenta un'arancia marcita.
    Ogni minuto, una qualsiasi arancia matura che è adiacente
    orizzontalmente o verticalmente ad una arancia marcita diventa
    anch'essa marcia.

    La funzione deve restituire il minimo numero di minuti che
    possono trascorrere fino a quando nessuna cella contiene più
    un'arancia matura. Se questo è impossibile, deve restituire -1.

    Ad esempio, data la griglia:
    [[2,1,1],
     [1,1,0],
     [0,1,1]]
    la funzione deve restituire 4.

    Mentre, data la griglia:
    [[2,1,1],
     [0,1,1],
     [1,0,1]]
    la funzione rende -1.

    Nota: per caricare la griglia potete usare json.load()

'''
import json
def ex2(gridFilePath):
    ### INSERIRE QUI IL CODICE ###
    with open(gridFilePath, 'r') as f:
        matrice = json.load(f)
    minuto = 0
# ----------------------------------- EX.3 ----------------------------------- #
''' Ex 3: 9 punti
    Si implementi una funzione ricorsiva che prende in ingresso una
    coppia di stringhe a e b, e un intero k e ritorna una lista.
    Nella lista sono contenute tutte le possibili stringhe che si
    possono ottenere dalla concatenazione di una sottostringa di
    lunghezza k della prima stringa con una sottostringa di lunghezza
    k della seconda stringa.  La lista ritornata è ordinata in ordine
    rispetto alla posizione della sottostringa di a in a e, a
    parimerito, in ordine della sottostringa di b in b.

    esempio: ex3('casa', 'riccio', 3) ritorna la lista:

     ['casric', 'casicc', 'cascci', 'cascio', 'asaric', 'asaicc',
     'asacci', 'asacio']

    AVVISO: non inserite la vostra funzione ricorsiva dentro un'altra
    funzione, altrimenti il sistema di test non la rileverà la ricorsione
    e tutti i test falliranno.
'''
def ex3(a, b, k):
    res = []
    ex3_ric(a,b,k,res)
    return res
def ex3_ric(a,b,k,res):
    if len(a)<k:return res
    for s in range(0, len(b) - (k-1)):
        print(a[0:k]+b[s:s+k])
        res.append(a[0:k]+b[s:s+k])
    ex3_ric(a[1:],b,k,res)
# ----------------------------------- EX.4 ----------------------------------- #
'''Ex. 4: 9 punti
    Scrivere una funzione ex4(folderPath), ricorsiva o utilizzando
    funzioni/metodi ricorsivi che, dato il percorso di una cartella
    che è la radice di un albero di cartelle contenente solo file di
    testo, crea e restituisce un dizionario in cui:

     - c'è una coppia (chiave, valore) per ogni file di testo che è
       stato trovato nella cartella folderPath o, ricorsivamente, in
       una qualsiasi delle sue sottocartelle;
     - ogni chiave è il percorso di un file di testo, relativo alla
       cartella folderPath radice della prima chiamata a ex4;
     - il valore corrispondente è un intero, ottenuto come somma
       dei valori unicode di tutti i caratteri del file di testo,
       SENZA includere i caratteri di accapo.

    Per esempio, dato il seguente albero di cartelle:

    ex4/test01/
        |-f1
            |-f1-1

    e i seguenti file:

    ex4/t1.txt - contenuto del file: hello world
    ex4/f1/f1-1/t2.txt - contenuto del file: let's count to 3, 1-2-3

    ex4("ex4") restituirà il dizionario
    {'ex4/t1.txt': 1116, 'ex4/f1/f1-1/t2.txt': 1722}
    poiché la somma dei valori unicode di "hello world" è 1116,
    mentre quella di "let's count to 3, 1-2-3" è 1722.

    AVVISO: è vietato usare la funzione os.walk.
    AVVISO: non inserite la vostra funzione ricorsiva dentro un'altra
    funzione, altrimenti il sistema di test non la rileverà la ricorsione
    e tutti i test falliranno.
'''
import os
def ex4(folderPath):
    return ex4_ric(folderPath, {})
def ex4_ric(folderPath, result):
    for f in os.listdir(folderPath):
        path = folderPath + '/' + f
        if os.path.isdir(path):
            result = ex4_ric(path, result)
        elif os.path.isfile(path):
            with open(path, 'r') as f:
                for line in f:
                    valore = 0
                    for lettera in line:
                        if lettera != "\n":
                            valore += ord(lettera)
                    if path not in result:
                        result[path] = valore
                    else: result[path] += valore
    return result
# ----------------------------------- END ----------------------------------- #
if __name__ == '__main__':
    #print(ex4('/Users/lucian/Documents/GitHub/UniExercises/PythonExercises/Esami/2021-2022/Esame-7/examPY/ex4/test01'))
    #print(ex4('/Users/lucian/Documents/GitHub/UniExercises/PythonExercises/Esami/2021-2022/Esame-7/examPY/ex4/test02'))
    #print(ex2('/Users/lucian/Documents/GitHub/UniExercises/PythonExercises/Esami/2021-2022/Esame-7/examPY/ex2/grid01.json'))
    #print(ex3('casa', 'riccio', 3))
    print(ex1('/Users/lucian/Documents/GitHub/UniExercises/PythonExercises/Esami/2021-2022/Esame-7/examPY/ex1/f1.txt',
              '/Users/lucian/Documents/GitHub/UniExercises/PythonExercises/Esami/2021-2022/Esame-7/examPY/ex1/f2.txt',
              '/Users/lucian/Documents/GitHub/UniExercises/PythonExercises/Esami/2021-2022/Esame-7/examPY/ex1/test.txt'))
    pass
    ### INSERITE QUI IL CODICE PER I VOSTRI TEST ###
    #expected = {'ex4/test01/f1/f1-1/t2.txt': 1722, 'ex4/test01/t1.txt': 1116}
    #expected = {'ex4/test02/f1/f1-1/t1.txt': 42248, 'ex4/test02/f1/f1-2/t2.txt': 83019, 'ex4/test02/f2/f2-1/t1.txt': 1289763, 'ex4/test02/f2/f2-2/t2.txt': 3901830}