

def es55(sel, m, n, A):
    vm = vM = A[0][0]
    for r in A:
        for v in r:
            vm = min(vm, v)
            vM = max(vM, v)
    if m != n:
        if sel == 'r':
            A[m], A[n] = A[n], A[m]
        else:
            for r in range(len(A)):
                A[r][m], A[r][n] = A[r][n], A[r][m]
    return (vm, vM)
