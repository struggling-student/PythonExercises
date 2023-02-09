
def es57(griglia):
    N = []
    S = []
    E = []
    W = []
    if checkGriglia(griglia):
        N = countSky(griglia, 'c',  1)
        S = countSky(griglia, 'c', -1)
        E = countSky(griglia, 'r', -1)
        W = countSky(griglia, 'r',  1)
    return N, E, S, W


def countSky(griglia, scan, d):
    res = []
    l = len(griglia)
    if scan == 'r':
        for r in range(l):
            count = 0
            M = 0
            if d > 0:
                for c in range(l):
                    if griglia[r][c] > M:
                        count += 1
                        M = griglia[r][c]
            else:
                for c in range(l-1, -1, -1):
                    if griglia[r][c] > M:
                        count += 1
                        M = griglia[r][c]
            res.append(count)
    else:
        for c in range(l):
            count = 0
            M = 0
            if d > 0:
                for r in range(l):
                    if griglia[r][c] > M:
                        count += 1
                        M = griglia[r][c]
            else:
                for r in range(l - 1, -1, -1):
                    if griglia[r][c] > M:
                        count += 1
                        M = griglia[r][c]
            res.append(count)
    return res


def checkGriglia(griglia):
    l = len(griglia)
    allowed = range(1, l+1)
    for r in griglia:
        if len(set(r)) != l:
            return False
    for c in range(l):
        nums = set()
        for r in range(l):
            if not griglia[r][c] in allowed:
                return False
            nums.add(griglia[r][c])
        if len(nums) != l:
            return False
    return True
