# Gets time in seconds and returns it in a readable digital clock format "14:22:56" #

def make_readable(seconds):
    hh = seconds//3600
    seconds = seconds % 3600
    mm = seconds // 60
    seconds = seconds % 60
    ss = seconds
    if(hh < 10 and mm < 10 and ss < 10):
        return("0"+str(hh)+":0"+str(mm)+":0"+str(ss))
    elif(hh >= 10 and mm >= 10 and ss >= 10):
        return(str(hh)+":"+str(mm)+":"+str(ss))
    elif(hh >= 10 and mm >= 10 and ss < 10):
        return(str(hh)+":"+str(mm)+":0"+str(ss))
    elif(hh >= 10 and mm < 10 and ss >= 10):
        return(str(hh)+":0"+str(mm)+":"+str(ss))
    elif(hh < 10 and mm >= 10 and ss >= 10):
        return("0"+str(hh)+":"+str(mm)+":"+str(ss))
    elif(hh >= 10 and mm < 10 and ss < 10):
        return(str(hh)+":0"+str(mm)+":0"+str(ss))
    elif(hh < 10 and mm < 10 and ss >= 10):
        return("0"+str(hh)+":0"+str(mm)+":"+str(ss))
    elif(hh < 10 and mm >= 10 and ss < 10):
        return("0"+str(hh)+":"+str(mm)+":0"+str(ss))
    
