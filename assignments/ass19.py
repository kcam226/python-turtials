def func(l1):
    p1 = []
    p2 = []

    for i in l1:
        if type(i) == int:
            p1.append(i)
        else:
            p2.append(i)

    total = 0
    product = 1
    for i in p1:
        if i % 2 == 0:
            total = total + i
        if i % 2 != 0:
            product = product * i
    print(total + product)

    output = []
    for i in p2:
        if len(i) == 4:
            a = i[0].upper()  # first letter -> capitalizing # M
            b = i[1:4]  # ark
            c = a + b  # Mark
            output.append(c)  # ["Alan", "Mark"]
        else:
            uppercase = i.upper()  # KAU
            output.append(uppercase)  # ["Alan", "Mark", "HIM", "KAU"]
    print(output)


func([2, 3, 4, 6, 1, "alan", "mark", 7, 9, "him", "kau", "Steve", "Bamar"])
