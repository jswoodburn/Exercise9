
# created a list with an embedded set and list
cheeses =["cheddar", "brie", "philadelphia", "boirsin", {"chutney", "grapes", "grapes"},["bread", "crackers"]]

#print second item in list
print(cheeses[1])

# prints type of last element in the list
print(type(cheeses[-1]))

# practice how to print specific element of an embedded list
print(cheeses[2], cheeses[-1][0])

# taking slices of cheeses
print(cheeses[1:3])
print(cheeses[:3])
print(cheeses[1:])
print(cheeses[:])

# producing error [] not required- validate our understanding of syntax
# print(cheeses[])

# created a tuple
names ="eggs", "bacon", "spam", "tea"
print(names[2])

# unable to alter tuple, produces error
# names[1]=cheeses[0]

# created a dictionary
capital_cities = {"Ireland" : "Dublin",
                  "Italy" : "Rome",
                  "Argentina" : "Buenos Aires",
                    "Australia" :"Canberra"
}
print(capital_cities)
print(capital_cities["Italy"])

# add key pair to dictionary
country ="South Korea"
capital_cities[country] ="Seoul"
print(capital_cities)

# create a set
rugby_teams = {"Harlequins", "Wasps", "Saracens", "Sale Sharks"}
print(rugby_teams)

# confirm type
print(type(rugby_teams))

# attempt to select an element produces error
# print(rugby_teams[2])



