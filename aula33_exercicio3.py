"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

first_name = input("Insert the first name!\n")

name_valid = not (" " in first_name.strip())

if name_valid:

    short_name = 0 < len(first_name.strip()) <= 4
    normal_name = 4 < len(first_name.strip()) <= 6
    big_name = 6 < len(first_name.strip()) 

    if short_name:
        print(f"The name {first_name} is short!")
    elif normal_name:
        print(f"The name {first_name} is normal!")
    elif big_name:
        print(f"The name {first_name} is big!")
    else:
        print("Invalid name!")
else:
    print("The name contains sapaces!")