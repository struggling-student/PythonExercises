def es51(ls, c):
    ls1=[ s for s in ls if not c.lower() in s.lower()]
    count=len(ls)-len(ls1)
    ls[:]=ls1
    return count