
def es2(ls,ftesto):
   '''
   Si definisca la  funzione es4(ls,ftesto) che,
   - riceve una lista ls contenente stringhe di caratteri  e l'indirizzo di  un file di 
   testo 'ftesto' contenente almeno due stringhe di caratteri separate da spazi e/o  virgole e/o
   andate a capo.
   -  cancella in modo distruttivo da ls le stringhe che e' possibile ottenere concatenando due
      stringhe consecutive lette dal file
   - restituisce il numero di stringhe cancellate da ls.
   ESEMPIO: 
   se  ls=['b', 'abba', 'babc','ccc', 'bba', 'bb' ] e il  file di testo e' 
   "b, \n\n\n ab  ba, b \nc c cc" 
   la funzione restituisce il numero 2
   e la lista ls risultera' modificata come ['b',  'babc', 'bba', 'bb' ]
   Infatti il file contiene in sequenza le parole 
   'b', 'ab', 'ba', 'b', 'c' 'c' 'cc'
   e le parole di ls che possono ottenersi come concatenazione di due  parole che compaiono 
   una di seguito all'altra  nel file di testo 
   sono:
   'abba' = 'ab' +'ba'
   'ccc'= 'c' + 'cc'
   '''
   #inserisci qui il tuo codice
