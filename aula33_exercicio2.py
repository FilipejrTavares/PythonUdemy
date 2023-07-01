"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

HOUR_MIN = 0
HOUR_1 = 11
HOUR_2 = 12
HOUR_3 = 17
HOUR_4 = 18
HOUR_MAX = 23


hour = input("Insert the hour!\n")

try:
    hour_int = int(hour)
    
    hour_is_valid = HOUR_MIN <= hour_int <= HOUR_MAX

    if hour_is_valid:

        hour_good_morning = HOUR_MIN <= hour_int <= HOUR_1
        hour_good_afternoon = HOUR_2 <= hour_int <= HOUR_3

        if hour_good_morning:
            print("Good morning!")
        elif hour_good_afternoon:
            print("Good afternoon!")
        else:
            print("Good night!")

    else:
        print("Hour not valid should be between 0 and 23!")


except:
    print("The input is not valid!")