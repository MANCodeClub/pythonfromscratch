""" 
Cette application trop super permet de réviser les tables de multiplicatio.
Bon, il y a encore du boulot mais c'est déjà un début.
"""

import random
import time
import json


def affiche_classement(scores):
    classement = 1
    for (user, score) in sorted(scores.items(), key=lambda s: s[1]):
        print(f"{classement:>3}. {user:<10}\t{score:.2f}")
        classement += 1


def load_scores():
    try:
        with open("scores.txt", "r") as scores_file:
            return json.load(scores_file)
    except:
        return {}


def save_scores(scores):
    try:
        with open("scores.txt", "w") as scores_file:
            scores_file.write(json.dumps(scores, sort_keys=True, indent=4))
    except Exception as e:
        print("Désolé vos score n'ont pas pu être enregistrés.")
        print(e)


NB_QUESTIONS = 3  # nombre de question posées par partie
# chargement des hi-scores enregistrés
scores = load_scores()

user = (input("Quel est votre nom? ")).upper()
play_again = True
while play_again:
    start_time = time.time()
    user_best_score = scores.get(user, 999.99)
    for i in range(NB_QUESTIONS):
        a = random.randint(2, 9)
        b = random.randint(2, 9)
        is_rep_ok = False
        # on pose la question jusqu'à ce qu'on ai la bonne réponse
        while not is_rep_ok:
            try:
                rep_str = input(f"{a} x {b} = ")
                rep = int(rep_str)
            except ValueError:
                print(f"[{rep_str}] n'est pas un entier.")
                continue
            if rep != a * b:
                print("ERREUR! :-(")
            else:
                is_rep_ok = True

    # vérification du score
    end_time = time.time()
    duration = end_time - start_time
    if duration < user_best_score:
        scores[user] = duration
        print(f"Vous avez batu votre meilleur score! {scores[user]:.2f}!")
        save_scores(scores)
    else:
        print(
            f"Vous avez fait {duration:.2f}s. Votre précédent score était {scores[user]:.2f}"
        )
    affiche_classement(scores)
    if (input("jouer encore? (oO/nN)")).upper() == "N":
        play_again = False
