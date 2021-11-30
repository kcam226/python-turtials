name= input("Please enter your name: ")
letter = input("Please enter the Character : ")

count = 0
for i in range(len(name)):
    if(name[i] == letter):
        count = count + 1

print("The total Number of Times ", letter, " has occurred = " , count)