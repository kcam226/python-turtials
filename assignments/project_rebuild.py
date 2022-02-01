print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 10.")
rerun_game = True

while rerun_game:
    level_selection = input("Which level do you opt for? [easy / hard]: ")

    if level_selection == "easy":
        i = 0
        attempts = 10
        while i < 10:
            print("You have", attempts, "attempts remaining to guess the number.")
            guess = int(input("Insert the number: "))
            if guess == 6:
                print("You Win the Game.")
                i = 10
            elif guess < 6:
                print("Its low.")
            elif guess > 6:
                print("Its high.")
            i = i + 1
            attempts = attempts - 1

    if level_selection == "hard":
        i = 0
        attempts = 5
        while i < 5:
            print("You have", attempts, "attempts remaining to guess the number.")
            guess = int(input("Insert the number: "))
            if guess == 6:
                print("You Win the Game.")
                i = 5
            elif guess < 6:
                print("Its low.")
            elif guess > 6:
                print("Its high.")
            i = i + 1
            attempts = attempts - 1

    play = input("Do you want to play again [yes/no]? ")
    if play == "yes":
        rerun_game = True
    else:
        rerun_game = False

