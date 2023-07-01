
num = input("Set the number:\n")

try:
    num_int=float(num)
    print(f"The double of the number {num_int:.2f} is {num_int * 2:.2f}")
except:
    print("This is not a mumber!")