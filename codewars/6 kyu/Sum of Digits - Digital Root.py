def digital_root(n):
    soma = 0
    lenght = 0

    while n > 9:
        for char in str(n):
            soma += int(char)
        n = soma
        soma = 0
    return n