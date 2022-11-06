def es25(n):
    if n == 0:
        return [1]
    t0 = [0] + es25(n-1) + [0]
    return [t0[i]+t0[i+1] for i in range(n+1)]
