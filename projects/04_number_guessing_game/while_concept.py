# While Loop

## 1. True and False

game = True
while game:
    name = input("Insert your name: ")
    if name == "Cam":
        print("You are great.")
        game = False
    else:
        print("You are mad.")

game = False
while not game:
    name = input("Insert your name: ")
    if name == "Cam":
        print("You are great.")
        game = True
    else:
        print("You are mad.")


## 2. Limiting the loop

counter = 1

while counter < 15:
    print("You are great")
    counter = counter + 1

