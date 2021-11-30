#
# person_name = 0
# people= 1
#
# while not person_name:
#     name = input("Insert your name")
#     if name = ('name'):
#
# print(name.count("b"))

#
# game = True
# while game:
#     name = input("Insert your name: ")
#     if name == "Cam":
#         print("You are great.")
#         game = False
#     else:
#         print("You are mad.")

name = (input("Insert your name: "))

i = 0
while i < len(name):
    print(f"{name[i]}: {name.count(name[i])}")
    i = i + 1

# for letter in name :
#     print(f"{letter}: {name.count(letter)}")
