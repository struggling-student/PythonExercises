    
def es5(insieme,k):
    return recEs5(insieme, insieme, k)

def recEs5(insOrig, insResult, k):
    if(k == 1):
        return insResult
    else:
        nuovoInsieme = set()
        for el1 in insOrig:
            for el2 in insResult:
                nuovoInsieme.add(el1+el2) 
        return recEs5(insOrig, nuovoInsieme, k-1)
