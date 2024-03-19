def positive_sum(arr):
    posSum = 0
    for x in arr:
        if x > 0:
            posSum += x
    return posSum