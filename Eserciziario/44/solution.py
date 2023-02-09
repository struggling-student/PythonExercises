def es44(a, b):
    interi = set()
    n = 2
    while len(interi) < a:
        ndiv = 0
        for i in range(1, n + 1):
            if n % i == 0:
                ndiv += 1
            if ndiv > b:
                break
        if ndiv != b:
            n += 1
            continue
        else:
            interi.add(n)
        n += 1
    return interi