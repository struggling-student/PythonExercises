def es16(s, k):
    result = []
    temp_set = set()
    for i in range(0, len(s)+1):
        for y in range(i+k, len(s)+1):
            temp_set.add(s[i:y])
    for string in temp_set:
        n = k - 1
        last = string[0]
        for i in range(1, len(string)):
            if(last != string[i]):
                n -= 1
                last = string[i]
        if(n == 0):
            result.append(string)
    result.sort()
    result.sort(key=len, reverse=True)
    return result
