def row_sum_odd_numbers(n):
    i = n
    to_n = 0
    while(i > 0):
        to_n = to_n + i
        i = i - 1
    to_n = to_n - n
    start = 1
    while(to_n > 0):
        start = start + 2
        to_n = to_n - 1
    sum = 0
    while(n > 0):
        el = start
        sum = sum + el
        start = start + 2
        n = n - 1
    return(sum)