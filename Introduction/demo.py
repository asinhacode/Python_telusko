print("Hello")
placeHolder = 110
print(placeHolder)

array = "youtube"
print(array)
print(array[2:])

# list creation
nums = [1,2,3,4]
reverse = [9,8,7,6]

# add eleemnt from other lists
total = [nums[0] + reverse[0], nums[1] + reverse[1], nums[2] + reverse[2], nums[3] + reverse[3]]
print(total)

# print each element
for x in total:
    print(x)

# add at the end
total.append(9)
print(total)

total.pop()
# reverse the list
total.reverse()
print(total)

# remove from the end
total.pop()
print(total)

total.append(72)
print(total)

# add elements in a list
for i in range(10):
    total.append(i)

print(total)
total.reverse()
print(total)

for i in total:
    if i == 10:
        total.remove(i)

print(total)
print(max(total))
print(min(total))
total.remove(0)

print(total)
print(max(total) - min(total))

# DATA TYPE : INTEGER

print(type(4.3))  # float

print(type(4))  # int

print(type(4.3 + 3j))  # complex

# creating complex number
a = 32
b = -3
c = complex(a, b)
print(c)

# BOOLEAN
print(55 < 34)

# convert into int data type
print(int(bool(3 > 1)))


# convert range into a list
print(list(range(20)))

# modification to range
# increments by 5
print(list(range(0, 100, 5)))

import math

print(list(range(-10, 20, 2)))

print(math.sqrt(26))

print(math.floor(2.9))

print(math.ceil(2.9))

print(math.ceil(2.1))

print(math.factorial(4))

import math as m
print(m.sqrt(26))

x = 1
y = 2
print(x+y)

ch = input('enter a string, get a letter')[2]
print(ch)

