def solution(string, ending):
    n = 0
    for x in ending:
        n += 1
    if ending != '':
        if string[-n:] == ending:
            return True
        else:
            return False
    else:
        return True