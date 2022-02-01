# greatest
def greatest(num1, num2, num3, num4):
    if num1 > num2 and num1 > num3 and num1 > num4:
        print(num1)

    if num2 > num1 and num2 > num3 and num2 > num4:
        print(num2)

    if num3 > num1 and num3 > num2 and num3 > num4:
        print(num3)

    if num4 > num1 and num4 > num2 and num4 > num3:
        print(num4)


greatest(2,5,6,10)