

text = "O Python é uma linguagem dee programação " \
    "multiparadigma. " \
    "Python foi criado por Guido van Rossum."

i = 0
count = 0
letter = ""
while i < len(text):
    tempCount = text.count(text[i])
    if letter == text[i] or text[i] == " ":
        i += 1
        continue
    if tempCount > count:
        count = tempCount
        letter = text[i]
    i += 1

print(f"A letra é '{letter}' e apareceu {count} vezes!")