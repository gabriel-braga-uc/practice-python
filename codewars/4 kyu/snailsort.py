array = [[1,2,3],
         [4,5,6],
         [7,8,9]]

def snail(snail_map):
    path = []
    steps = len(snail_map) * len(snail_map)
    sub = snail_map
    subpath = []
    go = 'r'
    i = 0
    j = 0
    while steps > 0:
        if go == 'r':
            while i < len(sub) - 1:
                path.append(sub[j][i])
                i = i + 1
            steps = steps - 1
            go = 'd'
        elif go == 'd':
            while j < len(sub):
                path.append(sub[j][i])
                j = j + 1
            steps = steps - 1
            go = 'l'
        elif go == 'l':
            while i > 0:
                subpath.append(sub[j][len(sub)-i])
            steps = steps - 1
            go = 'u'
        if go == 'u':
            steps = steps - 1
            go = 'r'
    return(path, steps, j, i)

print(snail(array))