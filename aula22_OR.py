

user_input = input("[E]ntrada ou [S]air:\n")

if user_input == 'E' or user_input == 'S':
    print("Operação válida!")
else:
    print("Operação inválida!")


# Avaliação de curto circuito

password = input("Password:") or "Empty!" # começa da esquerda para a direita caso o imput seja vazio ele 
                                          # dá set de Empty na password.

print(password)