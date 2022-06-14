# Ch. 2 Exercises; 20220613; Sam Disharoon

# Exercise 1; Prompt the user to input a string of text and number of characters given

print("Enter some text:")
word = input()
print(word, "is", len(word), "charcacters long.")

# Exercise 2; prompt the user twice for text, first and last name, and output initials

print("Enter your first and last name:")
word1 = input()
word2 = input()
print("Your full name is:", word1, word2)
print("Your initials are:", word1[0], word2[0])

# Exercise 3: Prompt user for text and do various operations on it:
print("Enter text:")
word = input()
print(word.endswith("."))
print(word.find("X"))
print(word.isalpha())
word = "hello everyone!"
sarcastic_word = word.replace("e", "E")
print(word, sarcastic_word)

# Exercise 4: Prompt user for a sentence and output how many times the first & last characters occur

print("Enter a sentence")
sent = input()
f = sent[0]
l = sent[len(sent)-1]
print(f, "is the first character in:", sent)
print(f, "occurs", sent.count(f), "times.")
print(l, "is the last character in:", sent)
print(l, "occurs", sent.count(l), "times.")

# Exercise 5: Prompt user for the radius of a circle, and output the area

print("You have a circle.Eenter the radius of your circle:")
r = input()
r = int(r)
area = 3.14159 * r * r
print("The area of your circle is:", area)

# Exercise 6: Prompt user for two integers and display the product. Determine what happens if you provide something other than an integer

print("Enter two integers:")
n1 = input()
n2 = input()
n1 = int(n1)
n2 = int(n2)
print(n1, "*", n2, "=", n1*n2)

# If you enter a decimal here, the program throws an error. If you enter a non-numeric character here, it also throws an error

# Exercise 7: Prompt user for a string and then an integer, and repeat that string the number of times that is provided using the repetition operator

print("Enter a string and then an integer:")
word = input()
num = input()
num = int(num)
rep_word = word * num
print(rep_word)

# Exercise 8: Prompt user for two numbers, and then perform the pow() function on them and display the answer

print("Enter two numbers, first will be just a number, second will be exponent:")
n1 = input()
n2 = input()
n1 = int(n1)
n2 = int(n2)
print(pow(n1,n2))


