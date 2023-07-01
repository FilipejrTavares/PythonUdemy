

name = input("Insert the name:")

age = input("Insert age:")

if age and name:
    print(f"the name is: {name}")
    print(f"the name backwords is: {name[-1:-len(name)-1:-1]}")
    if " " in name:
        print("the name have sapaces!")
    else:
        print("the name don't have sapaces!")
    print(f"the lenght of the name is: {len(name)}")
    print(f"the first letter of the name is: {name[0]}")
    print(f"the last letter of the name is: {name[len(name)-1]}")
else:
    print("Sorry you have empty fields!")