first = "Jacqueline"
last = "Phillips"

# These should do the same thing
print(first,last)
print(first + " " + last)

names = [first, last]
print(names)
print(f"{names}") # ask Victoria about what f-string does? (or google)

names_dict = {
    first : last
}
print(names_dict)
