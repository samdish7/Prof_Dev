# Ch. 5 Exercises; Sam Disharoon; 20220615

# Exercise 1; Write a function to validate a postive integer

# determine if the input is a number, then look to see if it is positive
def valid():
    print("Enter a positive ingeter:", end=" ")
    num = input()
    if num.isnumeric():
        num = int(num)
        if num > 0:
            return num
    return 0

if valid() == 0:
    print("You did not enter a positive integer")

# Exercise 2; Write a function that takes a collection of strings an returns the length of the longest one, while also formatting the strings to be right-justified based off of the largest string

# Create a function to return the longest string length
def words(strs):
    max_len = 0
    for i in strs:
        if len(i) > max_len:
            max_len = len(i)
    return max_len

s = ["Hello", "World", "This is the longest", "I", "Love", "you"]

# Set variable equal to longest string length
longest = words(s)
print("The longest string in the list of strings given is:", longest)
print("The list of strings is:")

# Right justify the words in an output
for i in s:
    print(i.rjust(longest))

# Exercise 3; Create your own version of the 'sum' built-in function 

# Create the summing function then display
def my_sum(*nums):
    total = 0
    for i in nums:
        total += i
    return total
print("The sum of 4, 5, 6, 69, 100, 3, 4, and 75 is:", my_sum(4,5,6,69,100,3,4,75))

# Exercise 4; Rewrite 3 using a tuple instead of a sum. This tuple should be the sum and average of numbers passed

# Create my function with the same concepts as exe3, but add an average component
def my_sum(*nums):
    # Get values
    total = 0
    ave = 1
    total_nums = len(nums)
    for i in nums:
        total += i
    ave = total / total_nums
    # make and return a tuple
    vals = (total, ave)
    return vals

print("The sum/average of 4, 5, 6, 69, 100, 3, 4, and 75 is:", my_sum(4,5,6,69,100,3,4,75))

# Exercise 5; Build a simple calculator with functions for all the options: +, -, *, /

# make all calculator functions
def a(n1, n2):
    return n1 + n2
def s(n1, n2):
    return n1-n2
def m(n1, n2):
    return n1 * n2
def d(n1, n2):
    return n1/n2

# implement our calculator
while True:
    print("Welcome to a simple calculator. Which operation would you like?\n1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Quit")
    val = input()
    # determine if valid or not
    if val.isnumeric():
        val = int(val)
        if val == 5:
            break
        else:
            print("Great! Enter two numbers:")
            num1 = input()
            num2 = input()
            # determine if valid again
            if num1.isnumeric() and num2.isnumeric():
                num1 = int(num1)
                num2 = int(num2)
                if val == 1:
                    print(num1,"+",num2,"=",a(num1,num2))
                    continue
                elif val == 2:
                    print(num1,"-",num2,"=",s(num1,num2))
                    continue
                elif val == 3:
                    print(num1,"*",num2,"=",m(num1,num2))
                    continue
               	else:
                    # check for x/0!
                    if num2 == 0:
                        print("Divide by 0 error!")
                        continue
                    else:
                        print(num1,"/",num2,"=",d(num1,num2))
                        continue
            else:
                print("invalid numbers")
                continue
    else:
        print("Invalid")
        continue
print("Goodbye!")

# Exercise 6; Write a function that receieves a list as its only parameter and returns a new list of only the positive integers

# define function and only return a list of postive integers
def pos(l):
    l2 = list()
    for i in l:
        if i > 0:
            l2.append(i)
    return l2
# make a test list and display to user
x = [1, 2, -4, 5, 20, -9, 3, 234, 35423523, 5, -1]
print("The list of postive integers in the list:",x, "is:", pos(x))

# Exercise 7; Write a function that takes two parameters, a variable number of arguments, and then a named argument that counts the number of varaible arguments that are larger than the named argument

# return the number of numbers that are greater than num
def greater(*nums, num):
    big = 0
    for i in nums:
        if i > num:
            big += 1
    return big

# make a hard-coded list to test with num being 12
print("In the list: [6, 7, 8, 54, 35, 563, 3, 56, 9, 1],", greater(6,7,8,54,35,563,3,56,9,1, num=12), "were larger than 12")

# Exercise 8; Write a function that returns a nested function. The inner function should sum up two numbers by using the parameters of the outer function

# create outer function
def out(n1, n2):
    # create inner function
    def inn():
        return n1 + n2
    return inn()
print("2 + 2 =", out(2,2))
print("2 + 2 !=", out(3,3))

# Exercise 9; Same as 8, just flip which function gets the parameters

# create outer function
def out():
    n1 = n2 = 2
    # create inner function
    def inn(n1, n2):
        return n1 + n2
    return inn(n1, n2)
print("2 + 2 =", out())

# Exercise 10; Same objective as 8 and 9, but using lambda instead

# create function to house the lambda
def out (y):

    return lambda i: y + i

res = out(69)
print("69 + 12 =",res(12))

# Exercise 11; Write a function that takes two lists as parameters and returns a third list of elements that are common amongst them

# pass two lists in and return a list that has the shared elements

def shared(x1, x2):
    share = list()
    for i in x1:
        for h in x2:
            if i == h:
                share.append(i)
    return share

# create lists to test on

l1 = [1, "Hi", "Yeet", 350, "My guy", "Yes"]
l2 = [1, "Bye", "Yeet", 351, "My girl", "No"]
print(shared(l1, l2))

# Exercise 12; Write a function that takes a dictionary and a number, and modifies the dictionary's values by adding the number to them

# create a function that passes in a dictionary and a number
def num_manip(d, n):
    for i in d.keys():
        d[i] = d[i] + n
    return d

diction = {'first': 1, 'second': 4, 'third': 18}
print("Before:", diction)
print("After:", num_manip(diction, 20))

# Exercise 13; Wrtie a function that takes 3 parameters, a list, an object, and a number. You want to try to find the 2nd or 3rd occurance of the object passed. This will throw a 'ValueError' error if the value doesn't exist. This is fine

# pass in a list, item, and number
def f(l, item, n):
    for i in l:
        print(li.index(item))
# create test objects
li = [1, 2, 3, 5, 1, 3, 6]
f(li, 4, 2)

