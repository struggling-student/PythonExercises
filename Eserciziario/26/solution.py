def es26(tabella, colonna):
    tabella.sort(key=lambda x: x[colonna], reverse=True)
    return len(tabella[0])
