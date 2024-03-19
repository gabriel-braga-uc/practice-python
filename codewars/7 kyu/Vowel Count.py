def get_count(sentence):
    vowels = 0
    for char in sentence:
        if char.upper() == 'A' or char.upper() == 'E' or char.upper() == 'I' or char.upper() == 'O' or char.upper() == 'U':
            vowels += 1
    return vowels