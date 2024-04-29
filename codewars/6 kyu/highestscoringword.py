def high(x):
    x = x.split(" ")
    scores = []
    i = 0
    for word in x:
        scores.append(0)
        for letter in word:
            scores[i] = scores[i] + (ord(letter)-96)
        i = i + 1
    return(x[scores.index(max(scores))])