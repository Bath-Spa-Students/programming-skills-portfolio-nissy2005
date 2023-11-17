'''Write a Python program to iterate through both the keys and values of a dictionary and print them.'''

myself = {"Name": "Nissy Joji", "Age": 18, "Weight": "49kg", "Hobby": "Drawing"}
print(myself)

for key in myself:
  print(key, myself[key])