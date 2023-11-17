'''Write a Python program to merge two dictionaries into one.'''

names = {1: "Jisha", 2: "Joji", 3: "Neha1", 4: "Joji"}
friends = {5: "Neha2", 6: "Abhirami", 7: "Helen"}
people = names | friends
print(people)