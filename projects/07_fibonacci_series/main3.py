# initializing the first 2 numbers
a = 0
b = 1

number = int(input("How many numbers do you want from the fibonacci series: "))

# The main code starts here :
if number == 1:
    print(a)
elif number == 2:
    print(a, b)
else:
    print(a)
    print(b)
    for i in range(0, number - 2):  # range(0,3)
        c = a + b  # 0 + 1 = 1 # 1 + 1 = 2 # 1 + 2 = 3 # 2 + 3 = 5 # 3 + 5 = 8 # 5 + 8 = 13
        a = b  # 1 # 1 # 2 # 3 # 5
        b = c  # 1 # 2 # 3 # 5 # 8
        print(c)  # 1
