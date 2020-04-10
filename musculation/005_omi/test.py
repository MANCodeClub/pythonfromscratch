from solve import check_IMO_nbr
from solve import check_IMO_field

test_cases = [
    (1111117, True),
    (8622983, True), # le Belem
#    (0111115, False), # interdit de commencer par un 0
    (111110, False), # doit faire 7 chiffres
    (11111117, False) # doit faire 7 chiffres
]

nb_failure = 0
for test in test_cases:
    if check_IMO_nbr(test[0]) != test[1]:
        nb_failure += 1
        print(f"Erreur: check_IMO_nbr({test[0]}) doit retourner {test[1]}")

if nb_failure == 0:
    print("Bravo! check_IMO_nbr() semble fonctionner parfaitement\n")

test_cases = [
    ("1111117", True),
    ("0111115", False), # interdit de commencer par un 0
    ("111110", False), # doit faire 7 chiffres
    ("", False), 
    ("Vraiment n'importe quoi", False), 
    ("1111A10", False), 
    ("111110", False) 
]

nb_failure = 0
for test in test_cases:
    if check_IMO_field(test[0]) != test[1]:
        nb_failure += 1
        print(f"Erreur: check_IMO_field({test[0]}) doit retourner {test[1]}")

if nb_failure == 0:
    print("Bravo! check_IMO_field() semble fonctionner parfaitement\n")
