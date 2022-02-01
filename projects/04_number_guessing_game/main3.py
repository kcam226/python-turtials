from random import randint

logo = """
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|  
"""




print(logo)
print("Welcome to the Number Guessing Game! I'm thinking of a number between 1 and 100.")

number = randint(1,100)
EASY_ATTEMPTS = 15
EASY_LIVES = 0

HARD_ATTEMPTS = 10
HARD_LIVES = 0
difficulty = input("choose a difficulty. Type easy or hard: ")

if difficulty == "easy":
    print("You have 15 attempts ")
    while EASY_LIVES < EASY_ATTEMPTS:
        user_input = int(input("can you guess the winning number: "))
        if user_input == number:
            print("Congratulations,you win the guessing game")
            EASY_LIVES = EASY_ATTEMPTS

        if user_input > number:
            print("Its High")

        if user_input < number:
            print("Its Low")

        EASY_LIVES = EASY_LIVES + 1

if difficulty == "hard":
    print("You have 10 attempts ") 


        
