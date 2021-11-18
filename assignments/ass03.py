### Assignment 03

"""
Grade Calculator

The PC will ask you the marks you received in a few subjects in your class 10.

Algebra ( ... / 100 ) : 97
Geometry ( ... / 100 ) : 91
Physics ( ... / 100 ) : 99
Chemistry ( ... / 100 ) : 86
Biology ( ... / 100 ) : 65
English ( ... / 100 ) : 92
Spanish ( ... / 100 ) : 60
Social Studies ( ... / 100 ) : 88

Total Marks : 678 / 800
Total Percentage : 84.75
"""

print("Grade Calculator")

print("The PC will ask you the marks you received in a few subjects in your class 10.")

subject1=int(input("Algebra ( ... / 100 ) : "))

subject2=int(input("Geometry ( ... / 100 ) : "))

subject3=int(input("Physics ( ... / 100 ) : "))

subject4=int(input("Chemistry ( ... / 100 ) : "))

subject5=int(input("Biology ( ... / 100 ) : "))

subject6=int(input("English ( ... / 100 ) : "))

subject7=int(input("Spanish ( ... / 100 ) : "))

subject8=int(input("Social Studies ( ... / 100 ) : "))

total_grade= subject1 + subject2 + subject3 + subject4 + subject5 + subject6 + subject7 + subject8

total_percentage = 100*(total_grade / 800)

print(f"Total Marks : {total_grade} / 800")
print (f"Total Percentage:{total_percentage}")