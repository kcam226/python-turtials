print("Welcome to Treasure Island.")
print("Your mission is to find the treasure")
crossroad = input("Your at a cross road. Where do you want to go? Type left or Right : ")

if crossroad == "left":
    wait_swim = input("You've come to a lake. There is an island in the middle the of the lake. Type 'wait' to wait for the 'boat' and type 'swim' to swim across : ")
    if wait_swim == "swim":
        print("You were attacked by an angry trout. Game Over.")

    if wait_swim == "wait":
        island = input(
            "You arrive at the island unharmed. There is a house with 3 door. One red, One yellow or One green. Which color did you choose?: ")

        if island == "green":
            print("You enter a room of beasts. Game Over.")

        if island == "red":
            print("You enter a room full of fire. Game Over.")

        if island == "yellow":
            print("You found the treasure! You Win!")


if crossroad == "right":
         print("You fell into a hole. Game Over.")

