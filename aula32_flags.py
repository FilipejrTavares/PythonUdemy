

condition = True
if_is_true = None

if condition:
    if_is_true = True
    print("Do something!")
else:
    print("Don't do something!")

print(if_is_true, if_is_true is None)
print(if_is_true, if_is_true is not None)

if if_is_true is not None:
    print("If was true!")
else:
    print("If was false!")