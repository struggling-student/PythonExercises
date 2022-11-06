def es43(ftesto):
    somme = []
    with open(ftesto) as f:
        for line in f:
            interi = list(map(int, line.split()))
            for i, v in enumerate(interi):
                if i < len(somme):
                    somme[i] += v
                else:
                    for _ in range(i - len(somme)):
                        somme.append(0)
                    somme.append(v)
    return somme