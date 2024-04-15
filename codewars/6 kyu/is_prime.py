def is_prime(num):
    if(num > 2):
        i = 2
        while(i*i <= num):
            if(num % i == 0):
                return False
            i = i + 1
        return True
    else:
        return True if num == 2 else False