

user_input = input("[E]ntrada ou [S]air:\n")
password = input("Set password:\n")

if user_input == 'E' and password == str(12345):
    print("Você entrou na aplicação!")
elif user_input == 'S' and password == str(12345):
    print("Você saiu na aplicação!")
else:
    print("Operação ou password inválidos!")