def disemvowel(string_):
    neutralizedString = ''
    for char in string_:
        if char != 'A' and char != 'E' and char != 'I' and char != 'O' and char != 'U' and char !='a' and char != 'e' and char != 'i' and char != 'o' and char != 'u':
            neutralizedString += char
    return neutralizedString