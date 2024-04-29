def count_by(x, n):
    awns = []
    i = x
    while(i <= x*n):
        awns.append(i)
        i = i+x
    return(awns)
    