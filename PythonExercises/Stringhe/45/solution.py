def es45(parola1,parola2):
    sotto1 = set()
    sotto2 = set()
    l1 = len(parola1)
    for i in range(l1):
        for j in range(i, l1):
            sotto1.add(parola1[i:j+1])
    l2 = len(parola2)
    for i in range(l2):
        for j in range(i, l2):
            sotto2.add(parola2[i:j+1])
    return sorted(sotto1.intersection(sotto2))