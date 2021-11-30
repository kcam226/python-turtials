game_over = False

while not game_over:
    number = int(input("Guess a number between 1, 10: "))
    if number == 8:
        print( "You Win")
        game_over = True
    if number > 8:
        print ("It' High")
    if number < 8:
        print ("It's low")

