def es53(ftesto):
    with open(ftesto, encoding='utf8') as f:
        testo = f.read()
    lista = testo.split(':')
    for i in range(len(lista)):
        lista[i] = [int(x) for x in lista[i].split()]
    lista1 = [[lista[i-1][-1]]+lista[i][:-1] for i in range(1, len(lista)-1)]
    lista1 += [[lista[-2][-1]]+lista[-1]]
    return {elem[0]: elem[1:] for elem in lista1}
