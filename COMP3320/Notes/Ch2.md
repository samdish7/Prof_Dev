# Ch. 2, Basic Python Syntax; 20220613; Sam Disharoon

## Objectives

* Use correct python syntax in python programs
* Use basic python I/O functions properly
* Write python programs using the standard numeric datatypes and their operations
* Use strings and their methods in Python programs
* Convert between numeric and string datatypes

### Overview

Python is _case-sensitive_. These two examples are DIFFERENT:
- the-person = "Jim"
- The-person = "Bob"

All lines must begin in the first column. Indenting is huge with the langauge. It determines the control flow of functions and programs

Python can use multiple lines for the same function. An example of this will be given in the 'examples' folder as well as exercises.

### Simple Output

The most basic way to output something is the **print()** function. Can take zero or more arguments, zero arguments prints out a blank line. Seperate each argument by using comments

Automatically inputs a newline after each print

Several keywords:
- sep: argument seperators that is a single space
- end: appended at the end that is a newline if not specified
- file: throws into a file specified by the argument

### Simple Input

__input()__ allows us to get simple input from the user. This accepts information from the default input device. Automatically removes trailing newline character that plauges Java and C++

You'll want to save this to a variable, but this is ALWAYS returned as a string, so you'll need to convert it when applicable!

Comments are useful for explaing bits of code that make it easier to read. Although some code is _self-documented_. This means they can kinda know what they will be based off of the name given. An example of this may be *calcsalary()*. We know what this means based off the name. Use the '#' symbol to declare a comment

### Numbers

There are 3 types of numeric datatypes:
* Integers
* Floats
* Complex Numbers

Look for the datatypes documentation for more details

### Strings

Immutable (not changeable) sequence of zero or more characters. Can be enclosed in single or double quotes. These can span multiple lines in several ways:
* using the line continuation charcter
* matching triple-quotes: either _"""_ or _'''_. 

Literal strings are prefixed with the letter **r** or **R**

Use escape sequences to get the key words that strings house to work. Such as '\n' or '\t' or "\'"

### String Methods

String are represented using the class named _str_. Plenty of methods come with the _str_ class. Example in _string _ methods.py_

Other string methods include: 
* .find()
* .count()
* .replace()
* .rjust() & ljust()
* .split()
* .strip() .rstrip() & lstrip()
* .len()

All of these are self-explanatory. Use print(f"") to format output how you want it.

### Sequence operators

These perform operations on strings, such examples are:
* +
* *
* in
* can also automatically concatenate strings
 
### Indexing/Slicing

Strings are setup like arrays, and you can index/slice them similarly to how you do array/list operations in python. All indexes start at 0

### Conversion Fucntions

You can use these to convert eligible data types to other types:
* int()
* str()
* chr()
* oct()
* float()
* ord()
* hex()
* bin()

_int()_, _str()_, and _float()_ are constructors. This creates objects of those classes.


