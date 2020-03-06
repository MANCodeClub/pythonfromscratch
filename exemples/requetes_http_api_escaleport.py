import requests

# module externe à installer dans la console avec la ligne de commande suivante:
# pip install --proxy http://pfrie-std.proxy.e2.rie.gouv.fr:8080 --user requests


# définition des proxies du MTES
proxies = {
    "http": "http://pfrie-std.proxy.e2.rie.gouv.fr:8080",
    "https": "https://pfrie-std.proxy.e2.rie.gouv.fr:8080",
}

# ?movementType=shifting&movementStatus=ongoing
params = {"movementType": "shifting", "movementStatus": "ongoing"}

# on souhaite avoir une réponse en json => on l'indique dans les entêtes
headers = {"Accept": "application/json"}

# API bouchon escaleport
url_api_escaleport = "https://virtserver.swaggerhub.com/nviel/escaleport/0.1.0"

# requête recherche de mouvements
response = requests.get(
    f"{url_api_escaleport}/port/FRCQF/movement",
    params=params,
    proxies=proxies,
    headers=headers,
)

# affichier le corps de la réponse sous forme de texte
print("Affichage de la réponse telle quelle:")
print(response.text)
# interpréter la réponse qu'on sait être du json
truc = response.json()
print("\nAffichage de la réponse interprétée en types python depuis le json:")
print(truc)

# contenu de la liste des membres d'équipage (dict et list python)
fal5 = [
    {
        "lastName": "Johnson",
        "firstName": "Boris",
        "dutyOfCrew": "captain",
        "nationality": "GB",
        "dateOfBirth": "2020-03-06",
        "placeOfBirth": "New York",
        "coountryOfBirth": "GB",
        "natureOfIdentityDocument": "MusterBook",
        "numberOfIdentityDocument": "string",
        "visaResidencePermitNumber": "string",
    },
    {
        "lastName": "Johnson",
        "firstName": "Boris",
        "dutyOfCrew": "captain",
        "nationality": "GB",
        "dateOfBirth": "2020-03-06",
        "placeOfBirth": "New York",
        "coountryOfBirth": "GB",
        "natureOfIdentityDocument": "MusterBook",
        "numberOfIdentityDocument": "string",
        "visaResidencePermitNumber": "string",
    },
]

# on indique (dans les entêtes) au serveur qu'on lui envoie du json
headers = {"Content-Type": "application/json"}
response = requests.post(
    f"{url_api_escaleport}/port/FRCQF/movement/2019001854/FAL5",
    proxies=proxies,
    json=fal5,
    headers=headers,
)

print("\nréponse du POST FAL5:", response.status_code, response.text)
