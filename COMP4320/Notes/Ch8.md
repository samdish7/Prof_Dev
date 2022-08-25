# Ch.8 Functional Tools

## Objectives

- Conceptualize higher-order functions
- Learn what's in functools and itertools
- Transform data with map/reduce
- Chain multiple iterables together
- Implement function overloading with single dispatch
- User iterative tools to work with iterators
- Chain multiple iterators together
- Compute combinations and permutations
- Zip multiple iterables with default values

## Higher-order functions

These operate on or return other functions. The most traditional higher-order functions in other languages are _map_ and _reduce_. These are used for functional programming, which prevents side effects. 

Can be nested to have multiple transformations on data.

## Lambda functions

An _inline anonymous_ function declaration. Very good for condensing code. Niether _blocks_ nor _return_ is allowed. Good for _callbacks_ in higher-order functions.

### _operator_ module

Provides functional versions of Python's std. operators. This saves the trouble of creating _trival_ lambda functions. 

### _functools_ module

Provides higher-order functions. These avoid explicit loops, and most of these functions can be implemented with list comprehensions or generator expressions. Two examples of these as stated above are:
    - map()
    - reduce() *Throw back to COSC420 with mpicc :)*

## Partial Functions

Wrappers that have some arguments already filled in for the 'real' function. This is useful when creating _callback_ functions. It is also nice for creating customized functions that rely on functions from the std. library. The _partial()_ function makes creating these a breeze. 

## Single dispatch

Added to the std library in 3.4, the _singledispatch_ module provides generic functions. These are defined by the _@singledispatch_ decorator, and then other functions can be registered to it. You register functions by providing the _@og_func_register(type)_ decorator.

This can be done manually by checking arg types, then calling other methods, but _singledispatch_ is less cumbersome. You cannot use them with class methods however, although there is a work around.

Use the _dispatch()_ method to check which function would be chosen for a given type. 

### The _itertools_ module

This provides many different iterators for us. Some work on existing iterators, while others are built from scratch. 

[itertools Docs](https://docs.python.org/3/library/itertools.html#itertools-recipes)

### Infinite Iterators

These return iterators that will iterate a specific number of times, or infinitely. Like generators, they do not keep all the values in memory. Some examples of these are:
    - count()
    - cycle()
    - repeat()
## Combinatoric generators

Several functions provide products, combinations, and permutations. The functions that do so are (so originally) called:
    - product()
    - combinations()
    - permutations()
