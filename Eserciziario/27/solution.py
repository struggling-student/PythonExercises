def es27(tabella, colonna, valore):
    tabella2 = [
        {
            c: v for c, v in riga.items() if c != colonna
        } for riga in tabella if riga[colonna] == valore
    ]
    diff = len(tabella) - len(tabella2)
    tabella[:] = tabella2
    return diff
