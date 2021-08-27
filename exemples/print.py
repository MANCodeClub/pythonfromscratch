print("Bonjour Charlotte")
# "Bonjour Charlotte"

print("Bonjour", "Charlotte")
# "Bonjour Charlotte"

print("Bonjour", "Charlotte", sep="[SEP]", end="[END]")
print("Bonjour", "Charlotte", sep="[SEP]")
# "Bonjour[SEP]Charlotte[END]Bonjour[SEP]Charlotte"

print("a", "b", "c", sep=";", end="\n\n\n")
print("a", "b", "c", sep=";", end="\n\n")
print("a", "b", "c", sep=";", end="\n")
"""
a;b;c


a;b;c

a;b;c
"""
