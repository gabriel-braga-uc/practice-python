def rot13(s):
    s_out = []
    for c in s:
        if(65 <= ord(c) <= 90):
            if(ord(c) + 13 > 90):
                s_out.append(chr(ord(c) - 13))
            else:  
                s_out.append(chr(ord(c) + 13))
        elif(97 <= ord(c)<= 122):
            if(ord(c) + 13 > 122):
                s_out.append(chr(ord(c) - 13))
            else:
                s_out.append(chr(ord(c) + 13))   
        else:
            s_out.append(c)
    return(''.join(s_out))


print(rot13('aA bB zZ 1234 *!?%'))
print('nN oO mM 1234 *!?%')