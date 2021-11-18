import random

number = random.randint(1, 10)
tries = 0


print("Welcome to the Number Guessing Game")

player_name = input("Hello, What's your name?")

print('okay! '+ player_name+ ' I am Guessing a number between 1 and 10:')

number = int(input("can you guess the winning number: "))

while number != 5 and tries < 4:
    number = input("Try again: ")
    tries += 1


if number == 5:
    print("you win the guessing game")

if number > 5:
    print("You lose the guessing game")

if number < 5:
    print("You lose the guessing game")


#

#


# print("number is too low")
# number = number + 1

# number = 5
# while number > 5:
#     print("number is too high")
#     number = number + 1


