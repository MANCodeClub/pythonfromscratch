def is_shifted(s1, s2):
    """ Cette fonction retourne le nombre de caractère de décalage vers la droite de la seconde chaine par rapport à la première
        Elle retourne -1 si les chaines ne sont pas comparables.
        Ex: s1 = "azerty", s2="zertya" => 1
            s1 = "azerty", s2="azert" => -1 """
    if len(s1) != len(s2):
        return -1
    if len(s1) == 0:
        return 0
    for decalage in range(len(s1)):
        if s1[-decalage:]+s1[:-decalage] == s2:
            return decalage
    return -1