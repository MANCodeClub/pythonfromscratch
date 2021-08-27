from solve import is_shifted

test_cases = [
    ("","",False),
    ("","a", False),
    ("a","a", True),
    ("ab", "ba", True),
    ("abcde", "eabcd", True),
    ("abcde", "abcde", False),
    ("abcde", "eabcde", False)
]

nb_failure = 0
for test in test_cases:
    if is_shifted(test[0], test[1]) != test[2]:
        nb_failure += 1
        print(f"Erreur: is_shifted('{test[0]}', '{test[1]}') doit retourner {test[2]}")

if nb_failure == 0:
    print("Bravo! Votre fonction semble fonctionner parfaitement")