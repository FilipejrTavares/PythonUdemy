name = input("Set the name:\n")
name = name.strip()
count = 0 
new_name = ""

while count < len(name):
    if name[count] == " ":
        if name[count-1] != " ":
            new_name += "* "
        count +=1
        continue
    new_name = new_name + "*" + name[count]
    count +=1
    if count == len(name):
        new_name += "*"
print(new_name)