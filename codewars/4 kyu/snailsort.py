## !!! NOT FINISHED !!! ##
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
        sub.pop()
        if go == 'r':


            sub.pop
            go = 'd'
        elif go == 'd':


            go = 'l'
        elif go == 'l':



            go = 'u'
        elif go == 'u':



            go = 'r'
    return(path, steps, j, i)

print(snail(array))