print("Lists")

# declaration
even = [0,2,4,6,8]
odd  =  [1,3,5,7,9]

print(even)
print(even[-2]) # same as string
print(even[3:])
print(odd[0:3])

added = even + odd # add 2 lists into 1
print(added)

# lists can contain any type of data type
letter = [1, 'A', 2, 'E', 3, 'I', 4, 'O', 5, 'U']
print(letter)

# zero is still zero
zero = [0, 0.00]
print(zero)

# reverse
added.reverse()
print(added)

# sort
added.sort()
print(added)

# max and sum
max = max(added)
sum = sum(added)
print(max)
print(sum)
