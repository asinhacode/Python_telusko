inStore = 5

x = int(input("How many candies do you want? "))

i = 1 # start distribution
while i <= x:
    if i > inStore:
        print("Ran out of all candies!")
        break # come out of the loop
    print("Here is " + str(i))
    i += 1

for i in range(1, 30):
    if i % 3 == 0:
        print("NO")
        continue # skip the remaining statements
    print(i)
