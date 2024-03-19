def move_zeros(lst):
    sortedList = []
    zeroCount = 0
    
    for x in lst:
        if x == 0:
            zeroCount += 1
        else:
            sortedList.append(x)
            
    while zeroCount > 0:
        zeroCount -= 1
        sortedList.append(0)
            
            
    return sortedList