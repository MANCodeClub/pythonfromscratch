print("True", end=" --> ")
if True:
    print("ok")
else:
    print("erreur")

print("not True", end=" --> ")
if not True:
    print("ok")
else:
    print("erreur")

print('"1" == 1', end=" --> ")
if "1" == 1:
    print("ok")
else:
    print("erreur")

print("1 == 3", end=" --> ")
if 1 == 3:
    print("ok")
else:
    print("erreur")

print("(1 == 3 or 1 == 1) and True", end=" --> ")
if (1 == 3 or 1 == 1) and True:
    print("ok")
else:
    print("erreur")

print("1 < 3 and 3 < 5", end=" --> ")
if 1 < 3 and 3 < 5:
    print("ok")
else:
    print("erreur")

print("1 < 3 < 5", end=" --> ")
if 1 < 3 < 5:
    print("ok")
else:
    print("erreur")

