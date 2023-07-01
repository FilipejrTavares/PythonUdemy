

in_out = input('Do you want to in or out?')


if in_out == "in":
    print('You are in')
elif in_out == "out":
    print('You are out')
else:
    print('Invalid input')


in_out_num = input('Do you want 1 or 2?')

in_out_num_int = int(in_out_num)

if in_out_num_int == 1:
    print('You have 1')
elif in_out_num_int == 2:
    print('You have 2')
else:
    print('Invalid input')
