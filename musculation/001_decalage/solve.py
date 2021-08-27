def is_shifted(s1, s2):
    """print("s1[0:-1]=",s1[0:-1])
    print(s2[1:len(s2)])
    print(s1[-1])
    print(s2[0])"""
    if (len(s1) >0 and len (s2)>0 and len(s1) == len(s2) #test sur les les longueurs
    and s1[0:-1] == s2[1:len(s2)]  and s1[-1]==s2[0]): #test sur les index
        return True
    else:
        return False
    
    