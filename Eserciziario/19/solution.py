def es19(ftesto):
    matrix = []
    tot = 0
    file = open(ftesto, 'r')
    for line in file:
        if(line.isspace()):
            continue
        else:
            l = line.split()
            temp = []
            for i in l:
                temp.append(int(i))
            matrix.append(temp)
    file.close()
    for i in range(0, len(matrix)):
        for y in range(0, len(matrix[0])):
            if(i == 0):
                tot += matrix[i][y]
            elif(i == (len(matrix)-1)):
                tot += matrix[i][y]
            elif(y == 0):
                tot += matrix[i][y]
            elif(y == (len(matrix[0])-1)):
                tot += matrix[i][y]
    return (matrix, tot)
