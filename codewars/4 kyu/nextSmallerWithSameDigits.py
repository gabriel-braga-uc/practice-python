## !!! NOT FINISHED !!! ##

def next_smaller(n):
    possible = False
    nlist = [c for c in str(n)]
    aux = len(nlist)-1
    for x in reversed(nlist):
        if x != '0':
            templist = nlist
            templist[len(nlist)-1] = nlist[aux-1]
            templist[aux-1] = nlist[len(nlist)-1]
            print(templist)
            if(int(''.join(templist)) < n):
                possible = True
                break
        aux -= 1
    print(int(''.join(templist)))

n = 1042
next_smaller(n)