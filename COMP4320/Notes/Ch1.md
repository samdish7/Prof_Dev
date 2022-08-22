# Ch.1 Review of Python Basics; 20220822;

## Objectives

- Refresh the following, basic Python concepts
- Understand symbols and variables
- Use the basic Py data types
- Differentiate and use effectively the various sequence and mapping types
- Structure scripts and programs in a std. format
- Use File and console I/O
- Understand and use the various Py conditional and looping constructs

Every _symbol_ in Python is an alphanumeric string that does not start with a digit and is not a keyword. Symbols that start and end with two underscores are considered special. These are called __dunders__

_Variables_ are declared by assigning to them. It will automatically create it's type, so you don't have to. 

## Mapping Types

Python also supports mapping types - _dictionaries_ and _sets_. A dictionary __dict__ is a set of values indexed by an immutable keyword. Very useful type in Python. They need two special dunder methods:
- __hash__
- __eq__

## Program structure

Although you don't have to do it this way, this is the generally accepted method to do programming in python. __Modules__ must be imported before they can be used. These are called at the top.

Variables, functions, and classes must be declared before they can be used. 

## Files and Console I/O

### Screen output

Use the _print()_ function to show CLI output. These can be formatted in a number of different ways. 

## Reading files

To read a file, open it with _open()_ function as part of a _with_ statement. 

## User input

Use the _input()_ function to get input from the user. Like other languages, it will stay in a state until the user gives input. There is no timeout for this, so until the user puts something, it will pause execution. 

## Conditionals

The conditional statement is _if_. Used similarly to every other langauge, just nicer to read for us humans :grinning:. A shortcut to this is like the __A?B:C__ operator in C. An example of this is:

__result = value1 if condition else value2__

## Loops

Python has two kinds of looping constructs:
- __while__ loops are often used for reading data
- __for__ loops are used for iterating through sequenced data

## Builtins

These are built in utilitizes that make life much easier. 
