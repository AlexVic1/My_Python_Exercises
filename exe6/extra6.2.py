### reate a program that, whenever executed, asks the user to enter a new member in the command line
member = input("Add a new member: ")

file = open("members.txt", 'r')
existing_members = file.readlines()
file.close()

existing_members.append(member + "\n")

file = open("members.txt", 'w')
existing_members = file.writelines(existing_members)
file.close()