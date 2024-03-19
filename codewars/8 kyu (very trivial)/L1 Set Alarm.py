def set_alarm(employed, vacation):
    if employed:
        if vacation:
            return False
        else:
            return True
    else:
        return False