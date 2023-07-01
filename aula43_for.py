

password = 123456
passwordInput = ""
repetitions = 0
text = "Python"
new_text = ""
for letra in text:
    new_text +=  f"*{letra}"
    print(letra)
print(new_text + "*")
#while password != passwordInput:
#    passwordInput = int(input(f"Insert the password! (Attempt {repetitions}x)\n"))
#    if password != passwordInput:
#        repetitions += 1
#
#print(f"{repetitions}x")

