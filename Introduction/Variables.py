# variable declaration
origin = 0
afterMuchWork = origin + 1

# convert int to string otherwise, cannot concatenate
print("Where we begin: " + str(origin))
print("Then I work hard and reach: " + str(afterMuchWork))

# string indexed :
#  0  1  2  3
#  y  o  u  t
# -4 -3 -2 -1

yout = "YOUT"
print(yout[2])
print(yout[-2])

# variable substring
print(yout[0:3])  # 0 1 2 or you

# getting the length of the string
print(len(yout))

# cannot make a string mutable
# must create a new variable
print(yout + "ube")

# still the length is 4 as it is the original string of yout
print(len(yout))
