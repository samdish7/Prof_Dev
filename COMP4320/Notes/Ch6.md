# Ch.6 Generators and Coroutines

## Objectives 

- Unpack iterables with wildcards
- Create generators in 3 different ways
- Create iterable Coroutines

## Extending iterable unpacking

Before we begin an indepth discussion of generators and coroutines, we will take a look at the topic of __extended iterable unpacking__.

When unpacking iterables, sometimes you want to grab parts of the iterable as a group. One (_and only one_) variable in the result of unpacking can have a star prepended.

## What exactly is an Iterable?

An object that provides an __iterator__ (the special dunder method _iter_). This responds to the builtin __next()__ funciton via another special dunder method _next()_.

All generators __ARE__ iterables.

## Generators

This is an object that provides values on demand (LAZY), rather than storing them (EAGER). These are usually based on some type of iterable for obvious reasons. Very good for saving memory space, but can only be used once, have no length, and cannot be indexed. 

There are three ways to create one in python:

1. Functions
2. Expressions
3. Classes

### Generator Functions

These maintain a state between calls, unlike normal functions. While each Unicode block may have many characters, the generator function does not need to hold all of them. 

Use _yield_ instead of return.

### Generator Expressions

Similar to comprehension, but provides a generator rather than a collection. They also use parenthesis rather than square brackets or curly braces.

There is an _implied_ yield statement at the beginning of the expression. If there is only the expression passed as an arg, the extra () are not needed. Very useful for functions such as:
- sum()
- min()
- max()

### Generator Classes

The most flexible way to create a generator is by defining a __generator class__. This _must_ implement a special method:
- dunder __init(self)__ must return an object that implements dunder __next(self)__
- dunder __next()__ returns the next value from the generator



## Coroutines

When writing generator functions, you can send a value __back__ to the generator. While similar to a generator:
- Generators tend to be _producers_
- Coroutines tend to be _consumers_

Assigning a variable to the _yield_ statement is what makes it a Coroutine, but they are __NOT__ designed for iteration.
