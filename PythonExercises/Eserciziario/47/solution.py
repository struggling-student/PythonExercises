def es47(lista):
    return sorted(set(lista), key=lambda x: (-len(x), x), reverse=True)
