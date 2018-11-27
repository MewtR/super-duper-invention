
def purge_string(s):
    #Remove everything that isn't a letter
    s = ''.join(c for c in s if ((ord(c) > 96 and ord(c) < 123) or (ord(c) > 64 and ord(c) < 91)))
    
    #Make it lower case
    s = s.lower()
    return s

