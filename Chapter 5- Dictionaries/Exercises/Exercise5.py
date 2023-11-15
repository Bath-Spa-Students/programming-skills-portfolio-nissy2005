#Create a list of dictionaries represnting different pets
my_pets = [
    {"kind": "Fish", "owner": "Alice"},
    {"kind": "Dog", "owner": "Bob"},
    {"kind": "Parrot", "owner": "Charlie"},
    {"kind": "Cat", "owner": "David"},
]

#Loop through the list and print information about each pet
for pet in my_pets:
    print(f"Kind of Animal: {pet['kind']}")
    print(f"Owner's Name: {pet['owner']}\n")