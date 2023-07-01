
print('Calculator strat!\nHello! to leave set "esq"')
while True:
    in_calc = input("")

    # vars
    operation_position = 0
    num_1 = 0
    num_2 = 0
    result = 0
    is_mult = False
    is_add = False
    is_sub = False
    is_div = False

    # check if is to leave
    if in_calc.lower() == "esq":
        break
    
    # check if have opperator
    count_operator = 0
    while count_operator < len(in_calc):
        is_mult = in_calc[count_operator] == "*"
        is_add = in_calc[count_operator] == "+"
        is_sub = in_calc[count_operator] == "-"
        is_div = in_calc[count_operator] == "/"
        if is_mult or is_add or is_sub or is_div: 
            operation_position = count_operator
            break
        count_operator += 1
    
    if not operation_position:
        print("Error set two numbers and an operation!")
        continue
    
    # Check if have two digits
    try:
        num_1 = float(in_calc[:operation_position].strip())
        num_2 = float(in_calc[operation_position+1:].strip())
    except Exception as error:
        print(error)
        continue
    
    # add
    if is_add:
        result = num_1 + num_2

    # sub
    if is_sub:
        result = num_1 - num_2

    # mult
    if is_mult:
        result = num_1 * num_2

    # div
    if is_div:
        result = num_1 / num_2

    print(f"{result:.2f}")
    print("______________________ // _______________________")

print("Goodbye!")