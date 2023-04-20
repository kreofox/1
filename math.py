import math

a = input("Enter a number: ")

if int(a) == 5:
    print(math.factorial(int(a)))
elif int(a) > 5:
    x = int(a) / 2
    print(float(x))
elif int(a) < 5:
    print(pow(int(a), 2))
    print(divmod(int(a), 4))
