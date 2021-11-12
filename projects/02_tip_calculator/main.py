print("welcome to the tip calculator!")
bill = int(input("what was the total bill? $"))
tip = int(input("How much tip would like to give? 10, 12 or 15? "))
tip_split = int(input("How many people to split the bill?"))
bill_tip = tip / 100 * bill
bill_and_tip = bill + bill_tip
people_split = round(bill_and_tip / tip_split, 2)
print("Each person should pay: $" + str(people_split))
