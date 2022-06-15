# Ch.5: Functions; Sam Disharoon; 20220614

## Objectives

* Define and use custom functions in Python
* Define functions that allow positional and named arguments
* Acces different scopes in python programs
* Pass references to functions the same way references to other objects are used
* Use the map and filter datatypes to apply a function to an iterable object
* Understand nested uses and lambdas
* Define and use recursive functions

### Introduction

Large programs are much more easily understood using functions. This helps reduce size, redundancy, and makes the code easier to read and do stuff with

You can group these functions together using a library. You access these libraries by importing them. Usually called modules in python

### Defining your own Functions

You use the keyword _def_ to define a function of your own. Examples of how to create one will be under Exercises

### Parameters & Arguments

Generally, functions are more useful if you give them parameters or arguments. 
* A function declares parameters that it needs to work
* You pass arguments to it based on the set parameters

You can also return values using the _return_ statement. Otherwise it returns __None__

You can pass arguments by reference or by value. Reference means you pass the actual argument, value means a copy of the argument. Therefore, value will not change the orginal argument, whereas reference would

### Function Documentation

You can use the _ _ doc _ _ function to read the documentation provided by the user (assuming there is any lol). You can also access it by using Python's built in _help()_ function

### Named Arguments

These arguments are given a pre-determined name. This allows you to assign parameters without needing an order to go along with it. This is very useful for development purposes

### Optional Arguments

If a parameter is passed with a default value, this means passing it in is optional. Another quality of life perk that python offers.  If positional & named arguments are called in the same function call, the named arguments MUST be to the right of all other positional arguments 

### Passing Collectins to a Function

You are able to pass data structures into your functions. Very much like all other language. You just pass the name of it just like every other data type

### Variable Number of Arguments

You can pass more than one argument as a single parameter to python functions. It will be passed in as a _tuple_. Which in return can be used to do the task at hand. If you pass arguments AFTER the variable argument, it will need to be a _named_ argument otherwise it will crash 

### Scope

Just as other languages, the concept of scope is the same. Variables are only bound to the limits that are placed on them. A variable called in a function is only relative to that function. Calling it outside of the function will cause an error. A block of code is often called a __suite__

The types of scope are:
- __local__: refers to same suite of statements, these are local to the suite of code, this is always searched for first
- __global__: refers to the entire program. You can use/modify these variables throughout the entire program. Searched for after all local variables have been searched
- __built-in__: available to all statements in the application
- __nonlocal__: requires nested functions

### Functions - "First Class Citizens"

Two common practices when using functions are as follows:
- _fun()_ = invoking the function named __fun__
- _fun_ = referencing the function named __fun__

The second one allows us to pass an entire function into another function

### The map Data Type

This allows us to apply a function to each element of an iterable object. These iterables include:
- list
- str
- tuple
- dict

An example of this is in the _Exercises_ dicrectory

### The filter Data Type

This is an iterator that applies a function to every item of an iterable object, yeilding all the results that return True

### A Dictionary of Functions

You can create a dictionary that houses functions

### Nested Functions

You can call functions within other functions, this is the basics of _recursion_. The inner function can access the variables in outer function, but not the other way around

### lambda

This is an _anonymous_ function. Meaning they do not have a name and they are limited to only one line. Often used in conjunction with __filter__ and __map__

### Recursion

One of the most important topics, _recursion_ is the act of calling a function INSIDE of itself. A good example of this is the _fibonacci_ sequence. This is dangerous because if your base case is not good, it will cause a crash and run infinitely. Can be very costly, so may not use this often due to other, more robust solutions

