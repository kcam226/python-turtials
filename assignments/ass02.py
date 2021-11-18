print("We have to develop a fencing for plot. So please enter cost of per sq.m ; ")
lenght=int(input("insert the length: "))
breadth= int(input("insert the breadth: "))
cost= int(input("insert the cost: "))

fencing_size = 2*(lenght + breadth)

cost_of_fencing = fencing_size * cost

print("the amount of fencing: $", (cost_of_fencing))
print(f"The amount of the fencing is $ {cost_of_fencing}")

