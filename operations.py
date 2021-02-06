var = input("Please enter a value:\n")
# var = input("Please enter a value: ")

print(var.upper())

print(var + " has " + str(len(var)) + " letters.")

print(var.isdecimal()) # isdecimal only returns True if all numbers
print(var.isalpha()) # isalpha only returns True if all letters
print(var.isalnum())

# difference between isdecimal, isdigit, isnumeric