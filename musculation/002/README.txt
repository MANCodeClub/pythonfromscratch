Pour fêter le Brexit, le but est ici d'afficher un drapeau de la grande Bretagne suivant ce modèle:

| XXX XXX |
|X XX XX X|
|XX X X XX|
|XXX   XXX|
|         |
|XXX   XXX|
|XX X X XX|
|X XX XX X|
| XXX XXX |

 Le drapeau est carré et fait ici 9 caractères de coté.
 C'est une étoile noire (faite avec des espaces) sur un fond de X.

 La taille T du "demi coté" du drapeau sera passée en paramètre à notre script de sorte que le coté du drapeau sera 2*T+1.
 Voici quelques exemples:

> python solve.py 0
| |

> python solve.py 1
|   |
|   |
|   |

> python solve.py 2
| X X |
|     |
|     |
|     |
| X X |

> python solve.py 10
| XXXXXXXXX XXXXXXXXX |
|X XXXXXXXX XXXXXXXX X|
|XX XXXXXXX XXXXXXX XX|
|XXX XXXXXX XXXXXX XXX|
|XXXX XXXXX XXXXX XXXX|
|XXXXX XXXX XXXX XXXXX|
|XXXXXX XXX XXX XXXXXX|
|XXXXXXX XX XX XXXXXXX|
|XXXXXXXX X X XXXXXXXX|
|XXXXXXXXX   XXXXXXXXX|
|                     |
|XXXXXXXXX   XXXXXXXXX|
|XXXXXXXX X X XXXXXXXX|
|XXXXXXX XX XX XXXXXXX|
|XXXXXX XXX XXX XXXXXX|
|XXXXX XXXX XXXX XXXXX|
|XXXX XXXXX XXXXX XXXX|
|XXX XXXXXX XXXXXX XXX|
|XX XXXXXXX XXXXXXX XX|
|X XXXXXXXX XXXXXXXX X|
| XXXXXXXXX XXXXXXXXX |
