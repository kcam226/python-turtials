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

difficulty= input("choose a difficulty. Type easy or hard: ")

if difficulty == "easy":
    print("You have 15 attempts ")

if difficulty == "hard":
    print("You have 10 attempts ") 

game_over= True

# LTL -> Limit the Loop

while game_over:
    user_input = int(input("can you guess the winning number: "))
    if user_input == number:
        print("Congratulations,you win the guessing game")
        game_over = False

    if user_input > number:
        print("Its High")

    if user_input < number:
        print("Its Low")
        
