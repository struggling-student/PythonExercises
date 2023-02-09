

import os, sys, random

with open('words.txt') as F:
    words = F.read().lower().split()

exts = [ 'txt', 'pdf', 'png', 'doc', 'rtf', 'html' ]

def crea_file(path):
    size = random.randint(10, 200)
    parole = random.choices(words, k=size)
    sep = ',:@#!"£$%&/ \t\n'
    with open(path, mode='w', encoding='utf-8') as F:
        for w in parole:
            F.write(''.join(random.choices(sep, k=random.randint(1,100))))
            F.write(w)
    return len(parole), random.choice(parole)

def crea_dir(path, depth):
    found = {}
    files = random.choices(words, k=random.randint(0,5))
    for nome in files:
        ext = random.choice(exts)
        fullpath = f'{path}/{nome}.{ext}'
        N,p = crea_file(fullpath)
        found[fullpath] = p
    if depth:
        dirs = random.choices(words, k=random.randint(0,5))
        for nome in dirs:
            fullpath = f'{path}/{nome}'
            os.mkdir(fullpath)
            f2 = crea_dir(fullpath, depth-1)
            found.update(f2)
    return found

print(crea_dir('dirs/d3',4))
