###Write a program that asks users to enter a password. Then, it checks if the password length is greater than 7 and returns "Great password there!".

password = input("Enter a new password: ")

if len(password) > 7:
    print("Great password there!")
elif len(password) == 7:
    print("Password is OK, but not too strong")
else:
    print("Your password is weak.")