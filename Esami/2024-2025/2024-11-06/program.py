#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
################################################################################
################################################################################

""" Operazioni da fare PRIMA DI TUTTO:
 1) Salvare il file come program.py
 2) Assegnare le variabili sottostanti con il tuo
    NOME, COGNOME, NUMERO DI MATRICOLA

Per superare l'esame è necessario:
    - risolvere almeno 3 esercizi di tipo func AND;
    - risolvere almeno 1 esercizio di tipo ex (problema ricorsivo) AND;
    - ottenere un punteggio maggiore o uguale a 18

Il voto finale è dato dalla somma dei punteggi degli esercizi risolti.

Attenzione! DEBUG=True nel grade.py per migliorare il debugging.
Per testare correttamente la ricorsione è, però, necessario DEBUG=False.

"""

nome       = "F"
cognome    = "L"
matricola  = "2097837"


# %% ----------------------------------- FUNC1 ------------------------- #
'''func1: 2 punti

Si definisca la funzione func1(int_list, keys) che prende in ingresso una
lista 'int_list' e un set 'keys' contenenti interi. La funzione restituisce
un dizionario in cui le chiavi sono gli interi in keys e i valori sono
liste con gli interi presenti in int_list divisibili per l'intero della
chiave corrispondente.
Le liste sono ordinate in ordine decrescente.


Esempio: se int_list=[4, 6, 10, 13] e keys={2, 3, 5}
  l'invocazione di func1(int_list, keys) deve restituire il dizionario
  {2:[10, 6, 4], 3:[6], 5:[10]}
'''
def func1(int_list, keys):
    dict = {k: sorted([v for v in int_list if v % k == 0], reverse=True) for k in keys}
    return dict

# int_list=[4, 6, 10, 13]
# keys={2, 3, 5}

# print(func1(int_list, keys))


# %% ----------------------------------- FUNC2 ------------------------- #
''' func2: 2 punti

Si definisca la funzione func2(L0, L1) che riceve 2 liste L0 e L1.
La prima lista L0 contiene stringhe S0, S1, ... Sn-1, la seconda lista
L1 contiene numeri interi positivi I0, I1, ... In-1.
La funzione restituisce una stringa ottenuta concatenando ogni stringa
Sj ripetuta Ij volte.

Ad esempio, se L0 = ['ab', 'o o'] e L1 = [2, 3] la funzione restituisce:
'ababo oo oo o'.
'''
def func2(L0, L1):
    ## Scrivi qui il tuo codice
    pass
# L0 = ['ab', 'o o']
# L1 = [2, 3]
# print(func2(L0, L1))
# L0 = ['quick', 'brow', 'fox']
# L1 = [2, 0, 2]
# print(func2(L0, L1))
# L0 = ['h', 'e', 'l', 'o']
# L1 = [1, 1, 2, 1]
# print(func2(L0, L1))
# L0 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
# L1 = [0, 1, 2, 3, 4, 5, 6, 7, 8]
# print(func2(L0, L1))



# %% ----------------------------------- FUNC3 ------------------------- #
'''  func3: 2 punti

Si definisca una funzione func3(string_list1, string_list2) che prende
in ingresso due liste di stringhe e restituisce una nuova lista di
stringhe.
La nuova lista è costituita da tutte quelle stringhe presenti in una
delle due liste in ingresso che contengono come una sottostringa
almeno una stringa o un inverso dell'altra lista.
La lista risultante deve essere ordinata per numero di caratteri
decrescente, in caso di parità, in ordine alfabetico.

Esempio: se string_list1=['shop', 'park', 'elichopter', 'cat', 'elephant'] e
            string_list2=['ark', 'contact', 'hop', 'mark']

         l'invocazione di func3(string_list1, string_list2) dovrà restituire
         la lista ['elichopter','contact','park', 'shop']
         Infatti:
             'elichopter' contiene 'hop',
             'contact' contiene l'inverso di 'cat'
             'park' contiene 'ark'
             'shop' contiene 'hop'

'''

def func3(string_list1, string_list2):
    result = {s for s in string_list1 for sub in string_list2 if sub in s or sub[::-1] in s}
    result |= {s for s in string_list2 for sub in string_list1 if sub in s or sub[::-1] in s}
    return sorted(result, key=lambda x: (-len(x), x))
    pass


# string_list1=['shop', 'park', 'elichopter', 'cat', 'elephant']
# string_list2=['ark', 'contact', 'hop', 'mark']
# print(func3(string_list1, string_list2))

# %% ----------------------------------- FUNC4 ------------------------- #
""" func4: 4 punti

Si definisca la funzione func4(D) che riceve in ingresso un
dizionario, in cui ogni chiave è una stringa e il valore
corrispondente è una collezione (un insieme, un dizionario, una lista,
...).
La funzione restituisce un elenco di liste, in cui ogni sottoelenco S
corrisponde a un elemento del dizionario in ingresso e contiene quanto
segue: - come primo elemento I0, la chiave dell'elemento del
dizionario corrispondente - come secondo elemento I1, il valore
dell'elemento del dizionario corrispondente.
Le liste interne sono ordinate in base alla lunghezza del secondo
elemento I1 in ogni lista interna, in ordine inverso (dalla più lunga
alla più corta).  Se le due liste interne hanno un secondo elemento
con la stessa lunghezza, vengono ordinati in base al valore del primo
elemento I0 (in ordine alfabetico o numerico).

Ad esempio, se D = {"f":(1, 2, 3), "a":["h", "w"], "c":{"f":3, "g":[1,2]}}
la funzione restituisce: [["f", (1, 2, 3)], ["a", ["h", "w"]], ["c", {"f":3, "g":[1,2]}]].
"""

def func4(D):
    ## Scrivi qui il tuo codice
    pass
# D = {"f":(1, 2, 3), "a":["h", "w"], "c":{"f":3, "g":[1,2]}}
# print(func4(D))
# D = {3: {'name': 'Steve', 'age': 25, 'marks': 60}, 2: {'name': 'Anil', 'age': 23, 'marks': 75}, 1: {'name': 'Asha', 'age': 20, 'marks': 70}}
# print(func4(D))
# D = {'hp': {'name': ' Folio Elitebook 9470M', 'brand': 'HewlettPackard Laptop', 'price':30000},
#             'lenovo': {'name': 'Camera 8989', 'brand': 'Lenovo Laptop', 'price':40000},
#             'dell': {'name': 'Dell Inspiron', 'brand': 'Dell Laptop', 'price':200}}
# print(func4(D))
# cities = ["Aberdeen", "Abilene", "Akron", "Albany", "Albuquerque", "Alexandria", "Allentown", "Amarillo", "Anaheim", "Anchorage", "Ann Arbor", "Antioch", "Apple Valley", "Appleton", "Arlington", "Arvada", "Asheville", "Athens", "Atlanta", "Atlantic City", "Augusta", "Aurora", "Austin", "Bakersfield", "Baltimore", "Barnstable", "Baton Rouge", "Beaumont", "Bel Air", "Bellevue", "Berkeley", "Bethlehem", "Billings", "Birmingham", "Bloomington", "Boise", "Boise City", "Bonita Springs", "Boston", "Boulder", "Bradenton", "Bremerton", "Bridgeport", "Brighton", "Brownsville", "Bryan", "Buffalo", "Burbank", "Burlington", "Cambridge", "Canton", "Cape Coral", "Carrollton", "Cary", "Cathedral City", "Cedar Rapids", "Champaign", "Chandler", "Charleston", "Charlotte", "Chattanooga", "Chesapeake", "Chicago", "Chula Vista", "Cincinnati", "Clarke County", "Clarksville", "Clearwater", "Cleveland", "College Station", "Colorado Springs", "Columbia", "Columbus", "Concord", "Coral Springs", "Corona", "Corpus Christi", "Costa Mesa", "Dallas", "Daly City", "Danbury", "Davenport", "Davidson County", "Dayton", "Daytona Beach", "Deltona", "Denton", "Denver", "Des Moines", "Detroit", "Downey", "Duluth", "Durham", "El Monte", "El Paso", "Elizabeth", "Elk Grove", "Elkhart", "Erie", "Escondido", "Eugene", "Evansville", "Fairfield", "Fargo", "Fayetteville", "Fitchburg", "Flint", "Fontana", "Fort Collins", "Fort Lauderdale", "Fort Smith", "Fort Walton Beach", "Fort Wayne", "Fort Worth", "Frederick", "Fremont", "Fresno", "Fullerton", "Gainesville", "Garden Grove", "Garland", "Gastonia", "Gilbert", "Glendale", "Grand Prairie", "Grand Rapids", "Grayslake", "Green Bay", "GreenBay", "Greensboro", "Greenville", "Gulfport-Biloxi", "Hagerstown", "Hampton", "Harlingen", "Harrisburg", "Hartford", "Havre de Grace", "Hayward", "Hemet", "Henderson", "Hesperia", "Hialeah", "Hickory", "High Point", "Hollywood", "Honolulu", "Houma", "Houston", "Howell", "Huntington", "Huntington Beach", "Huntsville", "Independence", "Indianapolis", "Inglewood", "Irvine", "Irving", "Jackson", "Jacksonville", "Jefferson", "Jersey City", "Johnson City", "Joliet", "Kailua", "Kalamazoo", "Kaneohe", "Kansas City", "Kennewick", "Kenosha", "Killeen", "Kissimmee", "Knoxville", "Lacey", "Lafayette", "Lake Charles", "Lakeland", "Lakewood", "Lancaster", "Lansing", "Laredo", "Las Cruces", "Las Vegas", "Layton", "Leominster", "Lewisville", "Lexington", "Lincoln", "Little Rock", "Long Beach", "Lorain", "Los Angeles", "Louisville", "Lowell", "Lubbock", "Macon", "Madison", "Manchester", "Marina", "Marysville", "McAllen", "McHenry", "Medford", "Melbourne", "Memphis", "Merced", "Mesa", "Mesquite", "Miami", "Milwaukee", "Minneapolis", "Miramar", "Mission Viejo", "Mobile", "Modesto", "Monroe", "Monterey", "Montgomery", "Moreno Valley", "Murfreesboro", "Murrieta", "Muskegon", "Myrtle Beach", "Naperville", "Naples", "Nashua", "Nashville", "New Bedford", "New Haven", "New London", "New Orleans", "New York", "New York City", "Newark", "Newburgh", "Newport News", "Norfolk", "Normal", "Norman", "North Charleston", "North Las Vegas", "North Port", "Norwalk", "Norwich", "Oakland", "Ocala", "Oceanside", "Odessa", "Ogden", "Oklahoma City", "Olathe", "Olympia", "Omaha", "Ontario", "Orange", "Orem", "Orlando", "Overland Park", "Oxnard", "Palm Bay", "Palm Springs", "Palmdale", "Panama City", "Pasadena", "Paterson", "Pembroke Pines", "Pensacola", "Peoria", "Philadelphia", "Phoenix", "Pittsburgh", "Plano", "Pomona", "Pompano Beach", "Port Arthur", "Port Orange", "Port Saint Lucie", "Port St. Lucie", "Portland", "Portsmouth", "Poughkeepsie", "Providence", "Provo", "Pueblo", "Punta Gorda", "Racine", "Raleigh", "Rancho Cucamonga", "Reading", "Redding", "Reno", "Richland", "Richmond", "Richmond County", "Riverside", "Roanoke", "Rochester", "Rockford", "Roseville", "Round Lake Beach", "Sacramento", "Saginaw", "Saint Louis", "Saint Paul", "Saint Petersburg", "Salem", "Salinas", "Salt Lake City", "San Antonio", "San Bernardino", "San Buenaventura", "San Diego", "San Francisco", "San Jose", "Santa Ana", "Santa Barbara", "Santa Clara", "Santa Clarita", "Santa Cruz", "Santa Maria", "Santa Rosa", "Sarasota", "Savannah", "Scottsdale", "Scranton", "Seaside", "Seattle", "Sebastian", "Shreveport", "Simi Valley", "Sioux City", "Sioux Falls", "South Bend", "South Lyon", "Spartanburg", "Spokane", "Springdale", "Springfield", "St. Louis", "St. Paul", "St. Petersburg", "Stamford", "Sterling Heights", "Stockton", "Sunnyvale", "Syracuse", "Tacoma", "Tallahassee", "Tampa", "Temecula", "Tempe", "Thornton", "Thousand Oaks", "Toledo", "Topeka", "Torrance", "Trenton", "Tucson", "Tulsa", "Tuscaloosa", "Tyler", "Utica", "Vallejo", "Vancouver", "Vero Beach", "Victorville", "Virginia Beach", "Visalia", "Waco", "Warren", "Washington", "Waterbury", "Waterloo", "West Covina", "West Valley City", "Westminster", "Wichita", "Wilmington", "Winston", "Winter Haven", "Worcester", "Yakima", "Yonkers", "York", "Youngstown"]
# D = {char: {city for city in cities if city.startswith(char)} for char in 'ABCDEFGHIJKLMNOPRSTUVWY'}
# print(func4(D))

# %% ----------------------------------- FUNC5 ------------------------- #
""" func5: 8 punti

Si definisca una funzione func5(input_pngfile) che prende in ingresso
una stringa che contiene il percorso ad un file con un'immagine in
formato PNG.
L'immagine indicata da 'input_pngfile' contiene dei segmenti
orizzontali di colore uniforme su uno sfondo nero. Su una riga ci
possono essere più segmenti di colore diverso, anche attaccati fra
loro.

La funzione deve individuare tutti i segmenti presenti nell'immagine e
ritornare un lista di triple rappresentanti i colori dei segmenti
individuati, ordinati dal più lungo al più corto. In caso di segmenti
di uguale lunghezza, i colori vanno ordinati (in ordine crescente)
considerando l'ordine prima della terza componente, poi della seconda
e infine della prima.  In caso di segmenti di uguale colore, si deve
considerare quello con la lunghezza maggiore.

Esempio: nell'immagine del file func5/image01.png sono presenti quattro segmenti
         uno di lunghezza 50 con colore (0, 128, 200)
         uno di lunghezza 30 con colore (200, 128, 200)
         uno di lunghezza 30 con colore (200, 200, 128)
         uno di lunghezza 29 con colore (0, 128, 200),
         per cui func5('func5/image01.png') deve restituire la lista
         [(0, 128, 200), (200, 200, 128), (200, 128, 200)]
"""
import images

def func5(input_pngfile):
    # INSERT HERE YOUR CODE
    pass

# print(func5('func5/image01.png'))
# print(func5('func5/image02.png'))
# print(func5('func5/image03.png'))
# print(func5('func5/image04.png'))


# %% ----------------------------------- EX.1 ------------------------- #
"""
Ex1: 8 punti

Si definisca la funzione ex1(L), ricorsiva o che utilizza funzioni o
metodi ricorsivi,che, data una lista di N liste di M caratteri
ciascuna, costruisce e restituisce la lista di tutte le possibili
stringhe di N caratteri ottenute concatenando un carattere della prima
lista, un altro della seconda, uno della terza e così via.

Ad esempio, se la lista di input è: [['c', 'q', 'a'], ['w', 'e', 'y']],
la funzione restituisce: ['ae', 'aw', 'ay', 'ce', 'cw', 'cy', 'qe', 'qw', 'qy'].
La lista ritornata deve essere ordinata in ordine alfabetico.

"""

def ex1(L):
    ## Scrivi qui il tuo codice
    pass

# L = [['c', 'q', 'a'], ['w', 'e', 'y']]
# print(ex1(L))
# L = [['0', '1'], ['0', '1'], ['0', '1'], ['0', '1']]
# print(ex1(L))
# L = [['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']]
# print(ex1(L))
# L = [['0', '1', '2'], ['a', 'b', 'c'], ['0', '1', '2'], ['x', 'y', 'z']]
# print(ex1(L))

# %% ----------------------------------- EX.2 ------------------------- #
"""
Ex2: 6 marks

Si definisca la funzione ex2(root), ricorsiva o che utilizza funzioni
o metodi ricorsivi, che prenda in input un albero binario e lo
modifichi (in-place) aggiungendo ricorsivamente a ogni nodo i valori
dei suoi nodi figli (se presenti).
La somma deve essere fatta dal basso verso l'alto, cioè le foglie
saranno aggiunte ai loro nodi genitori, e così via, fino a raggiungere
la radice.
La funzione restituisce una coppia che rappresenta il numero di valori
dispari e pari nell'albero originale.

Ad esempio, se l'albero di input è:

               1
              / \
             2   3
            /   / \
           4   5   6
              /
             7
L'albero modificato sarà:
               28
              /  \
             6    21
            /    / \
           4    12  6
               /
              7
e la funzione restituirà (4, 3).
"""

import tree

def ex2(root):
    ## Scrivi qui il tuo codice
    pass

if __name__ == '__main__':
    # Place your tests here
    print('*'*50)
    print('ITA\nDevi eseguire il grade.py se vuoi debuggare con il grader incorporato.')
    print('Altrimenti puoi inserire qui del codice per testare le tue funzioni ma devi scriverti i casi che vuoi testare')
    print('*'*50)
    print('ENG\nYou have to run grade.py if you want to debug with the automatic grader.')
    print('Otherwise you can insert here you code to test the functions but you have to write your own tests')
    print('*'*50)
