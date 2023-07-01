

first_value = int(input("Set first number:"))

second_value = int(input("Set second number:"))

if first_value == second_value:
    print("Os valores são iguais!")
elif first_value >= second_value:
    print(f"O valor {first_value} é maior que {second_value}!")
else:
    print(f"O valor {first_value} é menor que {second_value}!")