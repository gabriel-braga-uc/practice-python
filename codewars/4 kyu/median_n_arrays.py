## !!! CODE TOO SLOW: WILL TRY USING BINARY SEARCH TREES TO FIND THE MIDDLE ELEMENT !!! ##

def median_from_n_arrays(arrays):
    biggy = []
    for x in arrays:
        if len(x) > 0:
            for n in x:
                biggy.append(n)
    biggy = sorted(biggy)
    if(len(biggy) % 2 == 0):
        return((biggy[(len(biggy)-1) // 2] + biggy[(len(biggy)) // 2])/2)
    else:
        return(biggy[(len(biggy)-1) // 2]) 
 
arr = [[5,7,9],[7,10,11,13]]
print(median_from_n_arrays(arr))