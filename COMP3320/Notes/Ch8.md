# Exceptions; Sam Disharoon; 20220616

## Objecties

- Understand and use Python's exceptions model
- Use try/except as the basic exception handling to avoid crashes
- Understand the various exceptions
- Raise excpetions within your code as an indicator that something happened
- Create and use user-defined exceptions within your code
- Understand the assert keyword and its benefits when writing code

### Errors and Exceptions

The main types of erros are:
- syntax errors
- exceptions

I have seen plenty of these before when testing programs, this is exactly why you want to test well!

A common error is invalid input. It will raise the __ValueError__ exception. You can avoid this by using _try_ and then if the input is invalid, you'll want to let the user know

### The Exception Model

After you call the _try_, you'll want to use some of the following:
- _except_
- _else_
- _finally_

these allow you to handle the exceptions without having your program crash

### Exception Handling

Since Exceptions are objects, you can grab them and use them. This is useful for development because you can figure out which exception it is and do something about it. Use a common thread: '__except ValueError as ve:__'. 

### Exception Hierarchy

Find this online, I'm not typing this out :)

### Raising Exceptions 

Python provides a _raise_ statement that allows you to force a specific error to happen. This allows you to use the errors at your leasure

### User-Defined Exceptions

Exceptions are derived from the Exception class, either directly or indirectly

The base class for built-in exceptions is _BaseException_. This is not meant to be directly inherited by user-defined classes

### assert

This is a way to check the internal state of a program as the programmer expected. These evaluate to either True or False

You can insert debugging assertions, _False_ means an AssertionError is raised, _True_ allows for the controle flow to pass


