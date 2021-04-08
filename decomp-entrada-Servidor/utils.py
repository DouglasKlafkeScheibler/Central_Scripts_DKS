    
def tryGetFromString(string, start, end, mapfunc=str, default=''):
    if len(string) < end:
        return default
    newString = string[start:end].strip()

    return mapfunc(newString) if newString != '' else ''