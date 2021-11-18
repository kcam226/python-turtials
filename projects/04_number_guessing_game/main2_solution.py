import random

number = random.randint(1, 10)

print("Welcome to the Number Guessing Game")

game_over = True

while game_over:
    user_input = int(input("can you guess the winning number: "))
    if user_input == number:
        print("you win the guessing game")
        game_over = False

    if user_input > number:
        print("Its High")

    if user_input < number:
        print("Its Low")


# game_over = False
#
# while not game_over:
#     user_input = int(input("can you guess the winning number: "))
#     if user_input == number:
#         print("you win the guessing game")
#         game_over = True
#
#     if user_input > number:
#         print("Its High")
#
#     if user_input < number:
#         print("Its Low")