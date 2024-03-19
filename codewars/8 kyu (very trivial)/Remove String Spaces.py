def no_space(x):
    spacephobicString = ''
    for char in x:
        if char != ' ':
            spacephobicString += char
    return spacephobicString