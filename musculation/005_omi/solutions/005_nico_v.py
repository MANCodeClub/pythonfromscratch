def check_IMO_nbr(number):
    if number < 10 ** 6 or number >= 10 ** 7:
        # le nombre n'est pas de la bonne taille.
        return False
    key = number % 10
    check_sum = 0
    for i in range(2,8):
        number = number // 10
        check_sum += (number % 10) * i
    if check_sum % 10 == key:
        return True
    else:
        return False

def check_IMO_field(field):
    try :
        number = int(field)
    except  ValueError :
        return False
    return check_IMO_nbr(number)