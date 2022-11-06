def es28(tabella,colonna,valore):
    tabella2 = [
        {
            c: v for c, v in riga.items() if c != colonna
        } for riga in tabella if riga[colonna] == valore
    ]
    return tabella2