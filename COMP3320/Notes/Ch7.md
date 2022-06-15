# Classes in Python

## Objectives

- Understand the basics of python classes
- Use the _class_ keyword to defind custom objects
- Use properties and decorators as a pythonic way of writing classes
- Use python's special methods within a class definition to accomplish standard tasks
- Use class variables as a way of providing shared access to instances of a class
- Understand inheritance and polymorphism to simplify class creation
- Use various built-in functions to obtain info about the relationship between datatypes

### Principals of Object Orientation

Object-oriented programs is a style of programming that lends itself to the principle that a software solution should closely model the problem domain. Allows you to house more than one variable type in a single data type

### Defining New Data Types

You can create your own data types using the _class_ keyword in python

Each instance of a data type is called an object

Good documentation is very helpful. Use the _help()_ function to determine what the data type is supposed to do.

The _pass_ keyword allows you to create a function without actally implementing it. Very good for a place holder

The _self_ keyword is always the first argument when referring to class specific functions. You'll also want an __' _ _ init _ _ '__ function to intialize the attributes of their function. 

### Properties as Decorators

A _decorator_ is a function that returns a function. Used mostly for getters and setters and in conjunction with the _property_ keyword.

Using these allows the application to be written in a way that allows us to think the objects of the class are being accessed directly, when they really aren't

### Special Methods

There are plenty of other special methods including _' _ _ init _ _ '_. Some others are:
- _' _ _ str _ _ '_ 
- _' _ _ del _ _ '_ 
- _' _ _ eq _ _ '_ 

There is documentation about each of these online

### Class Variables

Class data is part of the class but not part of an object. Instance variables are typically for data unique to each instance while class variables are for attributes and mthods shared by all instances of the class

### Inheritence & Polymorphism

These are the exact same concepts as other languages. Examples of the syntax are shown in the _Exercises_ directory


