""" Ici on part du principe que l'utilisateur ne se trompe jamais.
il répond bien les valeurs attendu et ne triche pas """

min = 1
max = 100

while True:
    proposition = (min + max) // 2 # division entière

    indication = input(f"{proposition}? ")

    if indication == "=":
        print("Super! J'ai gagné!")
        exit(0)

    if indication == "+":
        min = proposition + 1
    elif indication == "-":
        max = proposition - 1
