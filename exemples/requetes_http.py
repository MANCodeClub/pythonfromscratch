""" 
    Ce script montre un exemple d'utilisation du module request en 
    envoyant un sms à un client free mobile (ayant activé l'option adéquat).
"""

import requests

# pip install --proxy http://pfrie-std.proxy.e2.rie.gouv.fr:8080 --user requests

proxies = {
    "http": "http://pfrie-std.proxy.e2.rie.gouv.fr:8080",
    "https": "https://pfrie-std.proxy.e2.rie.gouv.fr:8080",
}

params = {
    "user": 12345678,
    "pass": "az3rTyui0p",
    "msg": "COUCOU! Ce message est envoyé depuis mon programme python!",
}

response = requests.get(
    "https://smsapi.free-mobile.fr/sendmsg", params=params, proxies=proxies
)

print(response.text)
