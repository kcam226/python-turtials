a = 0
b = 1

number = int(input("Insert a number: "))

if number == 1:
    print(a)
elif number == 2:
    print(a, b)
else:
    print(a)
    print(b)
    for i in range(0, number - 2):
        c = a+b
        a=b
        b=c
        print(c)
