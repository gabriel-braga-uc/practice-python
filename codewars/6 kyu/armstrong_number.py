def narcissistic(value):
    digits = 1
    divisor = 10
    while(value / divisor > 0.9999999 and value > 10):
        digits = digits + 1
        divisor = divisor * 10
    sum = 0
    for x in str(value):
        sum = sum + (int(x))**digits
    return True if sum == value else False