# Data Types in Python

start = 5.6
print(type(start))

step2 = int(start)
print(type(step2))

listOfEven = [0, 2, 4, 6, 8, 10]
print(type(listOfEven))

# appends to a list but as a set!
setOfOdd = {1, 3, 5, 7, 9}
listOfEven.append(setOfOdd)
print(listOfEven)

print(listOfEven[6])

# list the range from 0 to 20
print(list(range(20)))

# range advanced
# From...To...Increments
print(list(range(-4, 16, 3)))
print(list(range(-4, 26, 2)))
print(list(range(-4, -16, -2)))

# INTERESTING!
print(list(range(-4, -16, 2)))

# Sets into dictionary
# !!! DICTIONARY !!!
set1 = {'Anupam': 'Sinha', 'Nabamita': 'Maiti', 'Sharmistha': 'Sinha'}
print(set1)
print(set1.keys())
print(set1.values())
print(set1['Sharmistha'])
print(set1['Sinha'])