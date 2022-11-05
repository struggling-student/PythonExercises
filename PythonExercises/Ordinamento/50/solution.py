def es50(s,k):
    insieme={ s[i:i+k] for i in range(len(s)-k+1) if crescente(s[i:i+k])}
    return sorted(list(insieme),reverse=True)

def crescente(stringa):
    for i in range(len(stringa)-1):
        if stringa[i]>=stringa[i+1]:return False
    return True