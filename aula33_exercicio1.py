"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""


number = input("Insert a integer number!\n")

try:
    number_int = int(number)
    if number_int == 0:
        print("The number is 0!")
    elif number_int%2 == 0:
        print("The integer is even!")
    else:
        print("The integer is odd!")
except:
    print("The input isn't an integer!")