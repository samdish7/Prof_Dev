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

### 
