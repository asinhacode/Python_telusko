print(id(10))

a = 10 # same address as 10
print(id(a))

b = a
print(id(b)) # same address as 10

b = 9
print(id(b)) # different address

