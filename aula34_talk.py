

#
# imutable typs: str, int, float, bool
#

string = "Filipe Tavares"

outra_variavel = f"{string[:3]} ABC{string[4:]}"

# this doesn't work! string[3] = "ABC"

print(string)
print(string.capitalize())
print(outra_variavel)