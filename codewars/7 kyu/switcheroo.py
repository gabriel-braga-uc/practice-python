# Swap a(s) for b(s) and keep c(s) in their original spot, all inputs consist of only combinations of a(s) b(s) and c(s)

def switcheroo(s):
    awns = ""
    eqv = {"a":"b", "b":"a", "c":"c"}
    for c in s:
        awns = awns + eqv[c]
    return awns
