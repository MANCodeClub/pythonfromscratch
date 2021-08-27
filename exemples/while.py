i = 0
print("--- while ---")
while i < 5:
    print(i)
    i += 1

"""
0
1
2
3
4
"""

""" Pour simuler une bouble "until" on peut utiliser break:"""
print("--- until ---")
i = 0
while True:
    print(i)
    i += 1
    if i >= 5:
        break

""" Ou bien comme ceci: """
print("--- until V2---")
i = 0
termine = False
while not termine:
    print(i)
    i += 1
    if i >= 5:
        termine = True
