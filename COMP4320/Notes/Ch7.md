# Ch.7 Type Hinting

## Objectives

- Learning how to annotate variables with their type
- Understand what the type hints do __NOT__ provide
- Employ the _typing_ module to annotate collections
- Use the _Union_ & _Optional_ types correctly
- Write the stub interfaces using type hints

## Type Hinting

Python supports optional _type hinting_ of variables, functions, and parameters. Types may be specified by following the variable name with a : and a datatype.

The mechanism behind how type hints are tracked is through a dictionary called __(dunder) annotations__. Although quite useful, it really just store the __key:value__ pairs of the variables.

### Static Analysis Tools

If these type hints are not used by the Python interpreter, how are they useful? This is where static analysis tools come into play. 

The most common tool is the __mypy__ module. This scans the code (the Abstract Syntax Tree of it at least) and determines at _compile time_ what type it likely is. 

### Type Hinting Functions

Functions use the __->__ symbol to indicate a return type.

Not all types may be available at the time that a given piece of code is compiled to bytecode, this is where __forward references__ come into play. This is here to let the interpreter what type is being referred _before_ it is created. This is handled automatically by the __(dunder)future__ import in 3.7+. This will be the __default__ behavior in Python 4.0.

Forward Referenecing are also how special dunder methods may need to be written, to refer to the current class.

## _typing_ Module

This module makes it easier to refer to contaienrs as a type in Python code. Makes numerous classes available to us, including but not limited to:

- ABCMeta
- Any
- BinaryIO
- DefaultDict
- Iterator
- Type
- Set
- Pattern

[Complete Documentation](https://docs.python.org/3/library/typing.html)

### Type Hinting of Parameters

_Tuple_ objects generally specifically exactly which type each positional value is, such as _Tuple[str, int, str]_ One of arbitrary length may be specified using the _Ellipsis_ object.

Most parameter types should not be of a specific container type such as an _Iterable_ or _Collection_. 

[PEP484](https://peps.python.org/pep-0484/#arbitrary-argument-lists-and-default-argument-values) discusses how to hint parameters that take a variable number of args.

### Type Hinting Generators

The _typing.Generator_ type takes exactly threes types for its template:
- the type _yielded_
- the type _sent_
- the type _returned_ by the generator

If any of these are not used, set them to _None_

## Creating Types

Creating a new type aliases in Python follows the same process as creating any other kind of variable. When working with generic types, make sure to signal that a given type is maintained throughout the function call. 

The _TypeVar_ can restrict itself to a specific set of types.

### Variance

When dealing with types and inheritence, certain interactions need to be made explicit.  

- __Covariance__ is a kind of relationship between an argument's type and its inheritance. The subtype of an arg can be used in the palce of the argument's type. A.K.A: __Lixkov Substitution Principle__.

- __Invariance__ is the problem that many mutable objects in Python such as:
    * list
    * set
    * dict

  which means although a subclass and a super class have _covariance_, but a __list__ of the subclass is not a subclass of a __list__ of the super class. For example:

   __Mammal__ super class
   __Cat__ subclass

   __Cat__ is a subclass of __Mammal__, but __list[Cat]__ is __NOT__ a subclass of __list[Mammal]__.

- __Contravariant__ is the kind of variance that can be notably expressed by Python's type-hinting system. For example:
   __Animal__ is a _supertype_ of __Mammal__ meaning that passing a __list[Animals]__ would not cause python to yell, but _mypy_ would.

### Specifying Variance

The default variance of the collections in the _typing_ module are __invariant__, which means that only the exact type specified is permitted.

### _Union_ Types

A _Union_ type is allowed to be one of a number of possible types

### _Optional_ Types

An important specific case of _Union_ types is the _Optional_ type. This is either _None_, or a specifed type. This works well for type-checking potentially absent-value cases. 

## functools.singledispatch 

This decorator allows multiple definitions of the same function, passing in different types for _first_ arguments. All additional registered functions must __not__ share the same function or method name as the orginally decorated function, unlike _@property_. 

## multimethod

Same thing as above, but it allows for multiple different arguments in each function. 

## Stub Type Hinting

While Type hinting can be a useful tool, it can be limiting when integrating with other source code. The _mypy_ utility can actually read a seperate file to find out the type interface of a different module. 

[Stub Docs](https://mypy.readthedocs.io/en/stable/stubs.html)
