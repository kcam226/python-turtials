
number = int(input("Insert the number: "))


"""
Insert the number: 2
2x1 = 2
2x2 = 4
2x3 = 6
2x4 = 8
.
.
.
.
.
2x10 = 20
"""
sum = (2 * number)
print(f"{2} x {number} = {sum}")
for i in range(1, 11):
   print(sum, 'x', i, '=', sum*i)

