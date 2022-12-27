###list replace

filenames = ["1.doc", "1.report", "1.presentation"]

filenames = [filename.replace('.', '-') + '.txt' for filename in filenames]

print(filenames)


###prints out the sum of the numbers.

user_entries = ['10', '19.1', '20']
user_numbers = [float(item) for item in user_entries]
print(sum(user_numbers))