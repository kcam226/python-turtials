
def count():
    number = int(input ("Enter the number of which the user wants to print the multiplication table: "))
    print ("The Multiplication Table of: ", number)
    for count in range(1, 11):
        print (number, 'x', count, '=', number * count)


count()
"""
2 x 1 = 2
2 x 2 = 4
..
.
.
.
.
.
.
2 x 10 = 20
"""