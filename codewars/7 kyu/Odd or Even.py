def odd_or_even(arr):
    sum = 0
    for x in arr:
        sum += x
    if sum / 2 == int(sum / 2):
        return 'even'
    else:
        return 'odd'