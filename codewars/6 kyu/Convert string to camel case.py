def to_camel_case(text):
    camelCase = ''
    nextIsUpper = False
    for char in text:
        if char == '-' or char == '_':
            nextIsUpper = True
        elif nextIsUpper == True:
            camelCase += char.upper()
            nextIsUpper = False
        else:
            camelCase += char
    return camelCase