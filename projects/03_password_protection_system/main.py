"""
Welcome to the Login System

Insert your username : cam
Insert your email : cam@allrich.com
Insert your password : 12345

Welcome to the System.
OR
Invalid Credentials.
"""

print("Welcome to the Login System")

username = input("Insert your username: ")
email = input("Insert your email: ")
password = input("Insert your password: ")

if username == "cam" and email == "cam@allrich.com" and password == "12345":
    print("You are Great Fool. Welcome to the System.")
else:
    print("You are Great Guy. Invalid Credentials.")

# if username == "cam":
#     print("Welcome to the System")
#
# if email == "cam@allrich.com":
#     print("Welcome to the System")
#
# if password == "12345":
#     print("Welcome to the System")
#
# else:
#     print("Invalid Credentials")