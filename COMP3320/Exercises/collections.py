# Exercise 1; Concatenate the two list provided and output the third list on screen

# Create the 3 lists used
first = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
last = ["day", "day", "sday", "nesday", "rsday", "day", "urday"]
days = []

# Use a for loop to append the full words to new list and then print it out
for i in range(0, len(first)):
    days.append(first[i] + last[i])

print(days)

# Exercise 2; Ask the user to input numbers, store them in a list and then print the contents of the list as well as the sum of the elements

#prompt user for numbers and give end condition
print("Enter as many numbers as you want. Enter 'end' to stop")
numbers = list()
while True:
    data = input()
    if data == "end":
        break
    data = int(data)
    numbers.append(data)
total = 0

# perform calculations on list of numbers
for i in numbers:
    print(i, end=" ")
    total += i
print("\nSum ->", total)

# Exercise 3; Same as exercise 2, but keep track of the number of duplicate entries because this time store the numbers in a set. 

# Same as exe2.py, but using set and counting fails
print("Enter as many numbers as you want. Enter 'end' to stop")
fail = 0
numbers = set()
while True:
    data = input()
    if data == "end":
        break
    else:
        data = int(data)      
    if data not in numbers:
        numbers.add(data)
    else:
        fail += 1
# display to user
print("The set includes:", end=" ")
for i in numbers:
    print(i, end=" ")
print("\nThere were:", fail, "attempted duplicates")

# Exercise 4; Use a single set to determine the number of unique words in a user's input, sort it alphabetically and then display the number of unique words

# get input and loop through it
print("Enter a sentence:", end=" ")
data = input()
data = data.split(" ")
words = set()
for i in data:
    words.add(i)

# display stats to user
print("Your set of unique words:", words)
words = sorted(words)
print("Your set sorted alphabetically:", words)
print("There were:", len(words), "unique words in your sentence!")

# Exercise 5; Use a dictionary to create a mapping of the digits 0-9 to the words corresponding to them. Ask the user for a number and output the english version of each digit

# create the dictionary
numbers = {1:"one", 2:"two", 3:"three", 4:"four",
           5:"five", 6:"six", 7:"seven",
           8:"eight", 9:"nine",
           10:"ten"}

# ask user for input
print("Enter any number:")
num = input()

# split it up and print out based off of our dictionary
for i in range(0,len(num)):
    n = int(num[i])
    print(numbers.get(n), end=" ")

# Exercise 6; Rewrite exercise 4, but count the frequency of each word of the user's input. Print the sorted results and print by the sorted counts

# get input and loop through it
print("Enter a sentence:", end=" ")
data = input()
data = data.split(" ")
word_set = set()
#create a set of unique words
for i in data:
     word_set.add(i)

#loop through set to find counts of words then add to dictionary
word_count = {}
for i in word_set:
    count = 0
    for j in data:
        if i == j:
            count += 1
    word_count[i] = count
# display stats to user
word_set = sorted(word_set)
print("Your input sorted alphabetically:", word_set)
print("Your input sorted by count:", end=" ")
word_list = list(word_count.keys())
word_list.sort(key = word_count.get)
for y in word_list:
	print(y, word_count[y], end=" ")
print()

