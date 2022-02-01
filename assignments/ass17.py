def func(num):
    empty = []
    for i in range(len(num)):
        var = num.pop()
        print(var)
        empty.append(var)
        print(empty)
    return empty


print(func([1, 2, 3, 4]))
