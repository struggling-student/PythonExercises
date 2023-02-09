

import sys, os, random

try:
    _, N = sys.argv
    N = int(N)
except :
    print("Usage: genera-partite N")
    sys.exit()

alfabeto = "abcdefghijklmnopqrstuvwcyz"

squadre = [ ''.join(random.choices(alfabeto, k=20)) for _ in range(random.randint(N,2*N)) ]

print(squadre)

partite = []
for incasa in squadre:
    for ospite in squadre:
        if incasa == ospite: continue
        presi = random.randint(0,6)
        dati  = random.randint(0,6)
        game = incasa, presi, ospite, dati
        partite.append(game)

with open(f"games-{N}.txt", mode='w', encoding='utf8') as F:
    for game in random.sample(partite, k=len(partite)):
        print(*game, file=F)

