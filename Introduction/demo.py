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
