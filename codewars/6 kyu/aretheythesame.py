#Given two arrays a and b write a function comp(a, b) (orcompSame(a, b)) that checks whether the two arrays have the "same" elements, with the same multiplicities (the multiplicity of a member is the number of times it appears). "Same" means, here, that the elements in b are the elements in a squared, regardless of the order.
import math
def comp(array1, array2):
    if(len(array1) == 0 and len(array2) == 0):
        return(False)
    else:
        i = 0
        for x in array1:
            a = array1[i]
            i += 1
            j = 0
            k = 0
            for y in array2:
                b = array2[j]
                j += 1
                exp = round((math.log(b))/(math.log(a)))
                print(exp)
                if exp % 1 == 0:
                    break
                else:
                    if k == len(array2) - 1:
                        return(False)
                    else:
                        k += 1
        return(True)

l1 = [5, -]
l2 = [125]
print(comp(l1, l2))