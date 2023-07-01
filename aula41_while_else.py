
""" While/Else """


string = input("Insira uma palavra!\n")

i = 0

while i < len(string):
    if string[i] == " ":
        print("Found a space!")
        break
    i += 1
else:
    print("Space not found!")