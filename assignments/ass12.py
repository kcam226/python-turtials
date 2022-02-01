"""
How many numbers you want to insert in the list: 5
Insert the number 1: 2
Insert the number 2: 4
Insert the number 3: 80
Insert the number 4: 43
Insert the number 5: 62

Here's your list: [2,4,80,43,62]
"""
numbers = int(input("How many numbers you want to insert in the list: "))
for i in range(1, numbers + 1):
 number = input(f"Insert the number {i}:")

# list.append(i)
