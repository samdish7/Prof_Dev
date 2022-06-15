# Ch.6 Modules; Sam Disharoon; 20220615

## Objectives

- Use modules to hold python defintions and statements
- Define and access modules from other modules
- Use the _dir_ function to list available symbols with a module's global scope.
- Check the index of Python std. library modules for modules that may be helpful
- Understand and use the various properties and functions of Python's _sys_ module
- Write programs that use various numeric and mathematical modules from python's std. library and that use the various data/time modules

### What is a Module?

Modules are files (or libraries) that house functions that we can use. Some are built-in, others you must import.

The main module is just the starting point of execution. You'll want to do this common term ~> 'if _ _ name _ _ == _ _ main _ _ : main()' This means find main and start there

### The _dir_ function

This can determine which symbols a module defines. You can find a full list of built-in symbols buy using __'dir( _ _ builtins _ _ )'__. 

### Python Std. Library Modules

These are the most commonly used functions in the language. These are not part of the core language, but they are built-in so the user has flexiblity as well as makes it easier to do things in python. This is why py is popular

There is plenty of documentation regarding these modules,

There are thousands of built-in modules and that number is alwasy growing based on the needs of developers. A bunch are imported from the _PyPi_ library

### The sys Module

This provides access to variables and functions to interact with the interpreter. Many ways to use this are:
- sys.path
- sys.argv
- sys.version_info
- sys.exit([arg])

These provide more flexibility of programs

### Numeric and Mathematical Modules

Python allows for many mathematical equations to be used. You can import these by adding __import math__ to grab these functions. One commo practice is only grabbing what you need. The _math_ library is massive, so you can do something like __from math import <insert what you need>__ so there is less overhead.

The _shuffle()_ function is a good way to implement randomly generated numbers. It updates the sequence passed to it in place as opposed to returning a new sequence. This is helpful if you don't want to have more than one copy of a sequence

### Time and Date Modules

Three of the modules from this section that we will be discussing are:
- datetime
- calender
- time

You can find documentation on these three everywhere


