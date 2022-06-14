# Exercise 1

print("Enter a lucky number")
num = input()

# Use a try/except to handle any errors
try:
    num = int(num)
except:
    print("This is not valid")

# Example 2

print("Enter a lucky number")
num = input()

# Use a try/except to handle any errors
try:
    num = int(num)
except:
    print("INVALID!")

# convert back into string to give the length of the number
print("The number of digits in", num, "are", len(str(num)))

# Exercise 3

print("Enter two integers:")
n1 = int(input())
n2 = int(input())

if n1 > n2:
    print(n1, ">", n2)
elif n2 > n1:
    print(n2, ">", n1)
else:
    print(n1, "=", n2)
# Exercise 4

print("Enter two integers:")
n1 = int(input())
n2 = int(input())
sum1 = 0

if n1 > n2:
    for u in range(n2, n1+1):
        sum1 += u
else:
    for u in range(n1, n2+1):
        sum1 += u
print("The sum of the range of ints provided is:", sum1)
print(sum)

# Exercise 5

print("Enter a list of numbers:")
values = input()

# use split to get the individual numbers and then convert them to an int to compare to 0
myList = values.split()
for i in myList:
    if int(i) > 0:
        print(i)
# Exercise 6

print("Enter a lower bound, and upper bound, and an incrementer:")
l = int(input())
f = int(input())
i = int(input())

for h in range(l, f+1, i):
    print(h)
# Exercise 7

# use the * to print all on the same line using range
print(*range(0,10))
print(*range(10,20))
print(*range(20,30))
print(*range(30,40))
print(*range(40,50))

