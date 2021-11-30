def check_if_18(person_age):
    if person_age >= 18:
        print("You are eligible for voting.")
    else:
        print("You are not eligible for voting.")


age = int(input("insert your age : "))
check_if_18(age)
