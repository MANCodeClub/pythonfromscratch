from solve import is_shifted

test_cases = [
    ("","",0),
    ("","a", -1),
    ("a","a", 0),
    ("ab", "ba", 1),
    ("abcde", "deabc", 2),
    ("abcde", "abcde", 0),
    ("abcde", "eabcde", -1),
    ("abba", "baba", -1)
]

nb_failure = 0
for test in test_cases:
    if is_shifted(test[0], test[1]) != test[2]:
        nb_failure += 1
        print(f"Erreur: is_shifted('{test[0]}', '{test[1]}') doit retourner {test[2]}")

if nb_failure == 0:
    print("Bravo! Votre fonction semble fonctionner parfaitement")