#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
################################################################################
################################################################################

""" PREREQUISITI:
 1) Salva il file come program.py
 2) Assegna le variabili sottostanti con il tuo
    NOME, COGNOME, NUMERO_MATRICOLA

Per superare l'esame, è necessario ottenere un punteggio maggiore o uguale a 18 (15 per studenti DSA)

Il voto finale è la somma dei punteggi dei problemi risolti.

Attenzione! DEBUG=True in grade.py per migliorare il debug.
Tuttavia, per testare correttamente la ricorsione, DEBUG=False è necessario.

"""
name       = "A"
surname    = "S"
student_id = "42"



################################################################################
# ---------------------------- SUGGERIMENTI PER IL DEBUG --------------------- #
# Per eseguire solo alcuni dei test, puoi commentare le voci
# corrispondenti ai test che non vuoi eseguire all'interno della lista `test`
# ALLA FINE di `grade.py`.
#
# Per il debug delle funzioni ricorsive, puoi disabilitare il test di ricorsione
# impostando `DEBUG=True` all'interno del file `grade.py`.
#
# L'impostazione di DEBUG=True attiva anche la stampa a terminale dello STACK
# TRACE degli errori, che ti permette di conoscere il numero di riga in `program.py`
# che ha generato un errore.
################################################################################


# %% -------------------------------- FUNC.1 -------------------------------- #
''' func1: 4 punti
Definisci la funzione func1(embedding_list1, embedding_list2) che prende come argomenti due liste di tuple. 
Ogni tupla rappresenta una parola e il suo embedding vettoriale: `(stringa_parola, [float1, float2, ...])`.
La funzione cerca la coppia di parole più simili. La somiglianza è calcolata usando la funzione di supporto
 `cosine_similarity` sugli embedding corrispondenti a due parole.
La funzione deve restituire una tupla `(parola1, parola2, punteggio_somiglianza)`, dove `parola1` proviene 
da `embedding_list1`, `parola2` proviene da `embedding_list2`, e `punteggio_somiglianza` è la somiglianza coseno.
Se più coppie hanno la stessa somiglianza, restituisci quella in cui `parola1` è alfabeticamente minore, ed in
 seconda istanza, `parola2` è alfabeticamente minore.

Esempio:
  embeddings1 = [('king', [0.1, 0.2]), ('queen', [0.3, 0.4])]
  embeddings2 = [('man', [0.05, 0.15]), ('woman', [0.25, 0.35])]
  # Per semplicità, se (queen, woman) ha la somiglianza più alta.
  func1(embeddings1, embeddings2) potrebbe restituire ('queen', 'woman', 0.9997)
  
  
FIXME: FUNC1 forse 4 punti sono troppi
'''
import math
def func1(embedding_list1, embedding_list2):
    # Funzione di supporto per la somiglianza coseno
    def cosine_similarity(vec1, vec2):
        dot_product = sum(a*b for a, b in zip(vec1, vec2))
        magnitude1 = math.sqrt(sum(a**2 for a in vec1))
        magnitude2 = math.sqrt(sum(b**2 for b in vec2))
        if magnitude1 == 0 or magnitude2 == 0:
            return 0.0
        return round(dot_product / (magnitude1 * magnitude2), 4)
    # Completa il codice qui
    def criterio(terna):
        x,y,sym = terna
        return -sym, x, y
    coppie = [ (x,y,cosine_similarity(xv, yv)) for x,xv in embedding_list1 for y,yv in embedding_list2 if x!=y ]
    return min(coppie,key=criterio)
    pass

'''
embeddings1 = [('king', [0.1, 0.2]), ('queen', [0.3, 0.4])]
embeddings2 = [('man', [0.05, 0.15]), ('woman', [0.25, 0.35])]
# Per semplicità, se (queen, woman) ha la somiglianza più alta.
print(func1(embeddings1, embeddings2)) # potrebbe restituire ('queen', 'woman', 0.9997)
'''

# %% -------------------------------- FUNC.2 -------------------------------- #
''' func2: 4 punti
Definisci la funzione func2(text_corpus, sentiment_lexicon, top_k_sentences) che prende:
  - `text_corpus`: una lista di stringhe, dove ogni stringa è una frase.
  - `sentiment_lexicon`: un dizionario, che mappa parole (stringhe, minuscole) ai loro punteggi di sentimento (float, es. da -1.0 a 1.0).
  - `top_k_sentences`: un intero, il numero delle frasi più positive da riportare.

Dividi ogni frase in `text_corpus` in parole (token minuscoli) usando la funzione di supporto `tokenize_alphabetic`.
Calcola il punteggio di sentimento della frase sommando i punteggi di tutte le sue parole trovate nel lessico.
Le parole non presenti nel lessico hanno sentimento 0. Arrotonda tutti i valori di sentimento a 2 cifre decimali.

La funzione deve restituire un dizionario con la seguente struttura:
  - `overall_sentiment`: float, il punteggio di sentimento medio di tutte le frasi.
  - `top_positive_sentences`: una lista di K tuple `(punteggio, stringa_frase)` di frasi con sentimento positivo,
    ordinate per punteggio decrescente. Se esistono meno di `top_k_sentences` con sentimento positivo, includi tutte quelle disponibili.
    In caso di parità, includi quelle con la frase maggiore in ordine lessicografico.
  - `total_sentences_analyzed`: intero, il numero totale di frasi elaborate.

Esempio:
  text_corpus = ["This is a great movie!", "It was terrible.", "What a lovely day."]
  sentiment_lexicon = {
      'great': 0.8,
      'terrible': -0.9,
      'lovely': 0.7
  }
  func2(text_corpus, sentiment_lexicon, 1) dovrebbe restituire (l'ordine delle frasi potrebbe variare per lo stesso punteggio):
  {
      'overall_sentiment': 0.20,
      'top_positive_sentences': [(0.80, 'This is a great movie!')],
      'total_sentences_analyzed': 3
  }
  
FIXME: FUNC2 se le frasi hanno sentiment 0 non appaiono nel grader? perchè?  va corretto il testo oppure il grader
  
'''
import re

def tokenize_alphabetic(text):
    """
    Tokenizza il testo di input in una lista di parole alfabetiche.
    Ignora la punteggiatura e i caratteri non alfabetici.

    Args:
        text (str): La stringa di input da tokenizzare.

    Returns:
        list: Una lista di parole alfabetiche.
    """
    return re.findall(r'[a-z]+', text.lower())


def func2(text_corpus, sentiment_lexicon, top_k_sentences):
    # Completa il codice qui
    def criterio(coppia):
        s,frase = coppia
        return -s, frase
    sentimenti = []
    somma = 0
    for frase in text_corpus:
        s = sentimento(frase, sentiment_lexicon)
        print(s, frase)
        if s > 0:
            sentimenti.append((s,frase))
        somma += s
    bestk = sorted(sentimenti, key=criterio)[:top_k_sentences]
    N = len(text_corpus)
    return { 
        'overall_sentiment': round(somma/N,2) if N else 0,
        "top_positive_sentences": bestk,
        'total_sentences_analyzed': N 
        }
    pass

def sentimento(frase, lexicon):
    parole = tokenize_alphabetic(frase)
    somma = 0
    for parola in parole:
        if parola in lexicon:
            somma += lexicon[parola]
    return somma

'''
text_corpus = ["This is a great movie!", "It was terrible.", "What a lovely day."]
sentiment_lexicon = {
    'great': 0.8,
    'terrible': -0.9,
    'lovely': 0.7
}
print(func2(text_corpus, sentiment_lexicon, 1) )
'''

# %% -------------------------------- FUNC.3 -------------------------------- #
''' func3: 4 punti
Definisci la funzione func3(sentence_list, forbidden_words) che prende come argomenti
una lista di stringhe `sentence_list` (che rappresentano frasi) e un set di `forbidden_words` (stringhe).
La funzione dovrebbe identificare e rimuovere qualsiasi frase da `sentence_list` (modificandola in-place)
che contiene almeno una parola dal set `forbidden_words` (case-insensitive).
Le parole nelle frasi sono definite come sequenze di caratteri alfabetici (puoi usare la funzione di supporto
`tokenize_alphabetic` per tokenizzare le frasi).
La funzione dovrebbe restituire il conteggio totale delle frasi rimosse.

Esempio:
    sentence_list = ["This is a test sentence.", "Bad words here.", "Another one for good measure."]
    forbidden_words = {"bad", "terrible", "forbidden"}
    dopo aver chiamato func3(sentence_list, forbidden_words),
    sentence_list dovrebbe essere ["This is a test sentence.", "Another one for good measure."]
    e la funzione dovrebbe restituire 1.

IMPORTANTE: la lista `sentence_list` deve essere modificata alla fine dell'esecuzione della funzione.

FIXME: FUNC3 forse 4 punti sono troppi

'''
def func3(sentence_list, forbidden_words):
    # Completa il codice qui
    giuste = [ frase for frase in sentence_list if not set(tokenize_alphabetic(frase)) & set(forbidden_words) ]
    N = len(sentence_list)-len(giuste)
    sentence_list[:] = giuste
    return N
    pass

# %% -------------------------------- FUNC.4 -------------------------------- #
''' func4: 4 punti
Definisci la funzione func4(text, n) che prende una stringa `text` e un intero `n`.
La funzione deve tokenizzare il testo in parole alfabetiche (usando `tokenize_alphabetic`),
contare la frequenza di ogni parola e restituire una lista delle `n` parole più frequenti
insieme ai loro conteggi. La lista deve essere ordinata per conteggio decrescente, dopodiché alfabeticamente
per parola in caso di parità.

Esempio:
  text = "The quick brown fox jumps over the lazy dog. The fox is quick."
  func4_a(text, 2) dovrebbe restituire [('the', 3), ('fox', 2)] (l'ordine per le parità dipende dalla logica di risoluzione delle parità)
  func4_a(text, 3) dovrebbe restituire [('the', 3), ('fox', 2), ('quick', 2)]
  
FIXME: FUNC4 cosa intendi con "ordine per parità"? forse 4 punti sono troppi
'''
def func4(text, n):
    # Completa il codice qui
    def criterio(coppia):
        parola,conteggio = coppia
        return -conteggio, parola
    parole = tokenize_alphabetic(text)
    D = {}
    for parola in parole:
        D[parola] = D.get(parola,0)+1
    return sorted(D.items(), key=criterio)[:n]
    pass

# %% -------------------------------- FUNC.5 -------------------------------- #
''' func5: 4 punti
Definisci la funzione func5(word_list) che prende una lista di stringhe `word_list`.
La funzione dovrebbe trovare tutti i gruppi di anagrammi all'interno di `word_list`.
Due parole sono anagrammi se contengono gli stessi caratteri, indipendentemente dall'ordine o dalla maiuscole/minuscole.
La funzione deve restituire un dizionario in cui le chiavi sono la "forma canonica" di un gruppo di anagrammi
(cioè, la parola in minuscolo con le sue lettere ordinate alfabeticamente), e i valori sono
set di parole uniche da `word_list` che appartengono a quel gruppo di anagrammi (preservando le maiuscole/minuscole originali).

Esempio:
  word_list = ["listen", "silent", "Enlist", "apple", "Banana", "apPLe"]
  func6(word_list) dovrebbe restituire (l'ordine delle chiavi potrebbe variare):
  {
      'eilnst': {'listen', 'silent', 'Enlist'},
      'aelpp': {'apple', 'apPLe'},
      'aaabnn': {'Banana'}
  }
  
FIXME: FUNC5 forse 4 punti sono troppi  

'''
def func5(word_list):
    # Completa il codice qui
    D = {}
    for parola in word_list:
        canonica = ''.join(sorted(parola.lower()))
        D[canonica] = D.get(canonica,set()) | {parola}
    return D


# %% --------------------------------- EX.1 --------------------------------- #
''' Ex1: 6 punti
**Questa funzione deve essere risolta usando un approccio ricorsivo.**
**La funzione ricorsiva deve essere top-level (cioè, non definita all'interno di un'altra funzione).**

Implementa la funzione ex1(root, result, target_value), che prende tre argomenti:
- root: La radice di un albero binario.
- result: Una lista vuota, deve essere popolata in-place con il percorso al nodo target.
- target_value: Il valore del nodo da trovare.

Registra il percorso dalla radice all'occorrenza più profonda di target_value nella lista `result`.
Se ci sono più occorrenze di target_value alla stessa profondità massima, scegli quella più a sinistra.
La funzione non deve restituire alcun valore. Invece, deve popolare la lista `result` in-place con la lista
dei valori dei nodi che rappresentano il percorso dalla radice al nodo target scelto. Se target_value non viene trovato nell'albero,
la lista `result` deve rimanere vuota.

Esempio:
  Albero:
       1
     /   \
    2     3
   / \   / \
  4   5 4   9
 / \
8   9
Se target_value è 5, result sarà [1, 2, 5].
Se target_value è 9, result sarà [1, 2, 4, 9] (più profonda).
Se target_value è 4, result sarà [1, 2, 4] (più a sinistra).

FIXME: EX1 facciamo ritornare un valore in modo da distinguere se non è implementata (ad esempio True/False per trovato)? 6 punti forse sono pochi

'''
def ex1(root, result, target_value):
    # Completa il codice qui
    percorso = _ex1(root, target_value, [])
    result[:] = percorso

def _ex1(root, target, path):
    "Torno il percorso massimo oppure []"
    if root is None:
        return []
    def criterio(percorso):
        return len(percorso)
    percorsoMy = path + [root.value] if root.value == target else []
    percorsoSX = _ex1(root.left,  target, path + [root.value])
    percorsoDX = _ex1(root.right, target, path + [root.value])
    return max([percorsoSX,percorsoDX,percorsoMy],key=criterio)


# %% --------------------------------- EX.2 --------------------------------- #
import images
''' Ex2: 6 punti
**Questa funzione deve essere risolta usando un approccio ricorsivo.**
**La funzione ricorsiva deve essere top-level (cioè, non definita all'interno di un'altra funzione).**

Implementa la funzione ex2(in_path, out_fpath, x, y, replacement_color), che prende i seguenti argomenti:
- in_path, out_fpath: i percorsi delle immagini PNG di input e output.
- x, y (int): La coordinata x e y di partenza.
- replacement_color (tupla di 3 interi): Il nuovo colore di riempimento.
Partendo dal pixel alle coordinate (x, y) di colore c, coloralo con `replacement_color`. Ricorsivamente, riempi la
regione di pixel vicini di colore c con il nuovo colore. Considera i pixel a sinistra, destra, sopra e sotto
rispetto al pixel corrente come vicini.
FIXME: EX2 OK

'''
def ex2(in_path, out_fpath, x, y, replacement_color):
    # Completa il codice qui
    pass
    img = images.load(in_path)
    W,H = len(img[0]), len(img)
    c = img[y][x]
    _fill(img,x,y,c,replacement_color,W,H)
    images.save(img, out_fpath)
    
def _fill(img,x,y,c,replacement_color,W,H):
    if 0 <= x < W and 0 <= y < H:
        if img[y][x] == c:
            img[y][x] = replacement_color
            _fill(img,x-1,y,c,replacement_color,W,H)
            _fill(img,x+1,y,c,replacement_color,W,H)
            _fill(img,x,y-1,c,replacement_color,W,H)
            _fill(img,x,y+1,c,replacement_color,W,H)

###################################################################################
if __name__ == '__main__':
    print('*' * 50)
    print('Eseguire grade.py per effettuare il debug con grader incorporato.')
    print('Altrimenti, inserire codice qui per verificare le funzioni con test propri')
    print('*' * 50)
