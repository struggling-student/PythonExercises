import albero


def es7(tree,insieme,k,count=0):
    if tree.f==[]:
        return count
    a=0
    for el in tree.f:
        count=es7(el,insieme,k,count)
        if el.id in insieme:
            a+=1
    if a==k:
        return count+1
    else:
        return count