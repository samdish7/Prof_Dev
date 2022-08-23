# Ch.3 Pythonic Programming; 20220823

## Objectives

- Learn what makes code "Pythonic" 
- Understand some Python-specific idioms
- Create Lambda functions
- Perform advanced slicing operations on sequences
- Distinguish between collections and generators
- Use __unittest__ to verify functionality

## Tuples

While a _tuple_ and a _list_ can be used to store a collection of any data:
- Use a __list__ when you have a collection of similar objects
    * Such as days of the week or grades on an exam
- Use a __tuple__ when you have a collection of related objects, which may or may not be similar:
    * First & last name & phone # of a person
    * Related but only to a particular person

## Iterable unpacking

An iterable such as a tuple or list provides access to individual elements by index.

__Iterables__ are useful for large amounts of data when creating a variable for each becomes cumbersome. 

## Custom Sort Keys

A reference to a function can be passed as a parameter to the _sorted()_ function with a named parameter of __key__. Any builtin or custom Python function that meets the requirements can be sorted.

The _sort()_ method of _list_ provides the same type of custom sorting, this modifies the list __in place__ as opposed to _sorted()_ which returns a __newly sorted list__. 

## Lambda Functions

A _one-lined_ function that allows for more condensed and faster code. You can reference them for later by "callbacks".

The basic syntax is: __lambda parameter_list: expression__

### Comprehensions

A _list comprehension_ consists of brackets containing an expression followed by a for clause, then zero or more for or if clauses.  This allows for very efficent data reading. 

### Set Comprehensions

Useful for turning any sequence into a set based on a given function. Very similar syntax to a list comprehension

### Dictionary Comprehensions

Similar to _Set_ and _List_ comprehensions

## Iterables

Python has many built in iterables. Some examples of these are:
- Collections
- Generators

Collections are subdivided into sequences and mappings:

### Sequences

- str
- byte
- list
- tuple
- collections.namedtuple
- sorted
- list comprehensions

### Mappings

- dict
- set
- frozenset
- collections.Counter

Generators do not keep values in memory, only creates what is needed
- open
- range
- enumerate
- zip
- dict.items
- generator expressions and functions

## Generator Functions

Like a normal function, but instead of a _return_, it has a __yield__ statement. Each time the __yield__ statement is reached, it provides the next value in the sequence.This will continue until the end of the sequence is reached and then the function will return.

## Generator Expressions

Similar to a comprehension, but it provides a generator instead of a _list_, _set_, or _dict_. The main difference in syntax is that the generator expression uses parentheses rather than brackets or curly braces. These are especially useful when functions like _sum()_, _min()_, and _max()_ that all reduce an iterable to a single value.

## String formatting

The traditional way to format strings in Python was using the __%__ operator. Now we just use the _format()_ method. This allows us to pass values to strings much easier and gives us more flexibility.

## f-strings

These strings were added in version 3.6. It allows for even more condensed functionality of string formatting. __This is my preferred method of formatting strings__

## __unittest__ and Unit Testing

There are an abundance of testing framework and libraries available to choose from in Python. The __unittest__ module is part of the Python std. library and will be the main framework of the module. This was inspired by the Java testing framework called __Junit__.

The basics of a unit test case is to create a test case using __unittest.TestCase__. There is an _automatic_ discovery of units within Python packages by the __unittest__ module. The process requires the use of the dunder __init.py__, even if the python interpretor no longer requires it.


