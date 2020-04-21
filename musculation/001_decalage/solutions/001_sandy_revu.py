""" La version de Sandrine juste corrigée un poil pour qu'elle passe"""
def is_shifted(b, a):
    if len(a) != len (b) or len(a) == 0:           #comparer longueur
        #print('longueur differente') 
        return False
    elif a[0]!= b[len(b)-1] or a[1:(len(a)-1)] != b[0:(len(b)-2)]:
        return False
        #print('mauvaise position')
    else:
        return True

    return False

""" Le même algo dans une version plus épurée"""
def is_shifted2(s1, s2):
    if len(s1) != len(s2) or len(s1) == 0:           #comparer longueur
        return False
    if s2[0]!= s1[-1] or s2[1:] != s1[:-1]:
        return False
    return True