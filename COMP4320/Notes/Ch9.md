# Ch.9 Metaprogramming

## Objectives

- Learn what _metaprogramming_ means
- Access local and global variables by name
- Inspect the details of any object
- Use attribute functions to manipulate an object
- Design decorators for classes and functions
- Define classes with the type() function
- Create metaclasses
- Use descriptors to simplify repetitive code

_Metaprogramming_ is creating code that generates or modifies other code. This is done much easier in Python than other languages such as Java or C/C++.

You can easily overwrite any class/object instance with another one. It would take a lot of magic in other languages to do this.

The _globals()_ function returns a dict of all global objects. The _locals()_ function returns a dict of all local objects. 

The _inspect_ module provides user-friendly functions for accessing Python metadata. Some functions included are:
    - ismodule()
    - isclass()
    - getmemebers()
    - getfile()
    - stack()
    - trace()

## Working with Attributes

All python objcets are essentially dicts of attributes. There are four special functions that manage them:
    - getattr()
    - hasattr()
    - setattr()
    - delattr()

## Adding Instance Methods

Using _setattr()_, it is easy to add instance methods to classes. You can just add a function to a class, and it will automatically become bound to the instance. 

Once added, the method may be called from any existing or new instance of the class. 

Adding an instance method to an instance takes a little more effort. You need to specify which instance the method should be bound to in the format: __types.MethodType()__

## Decorators

In Python, many decorators are provided by the std. library, such as _property()_ or _classmethod()_. This is a component that modifies another component. Many of them register a component with another component.

The _@property_ method converts a class method into a _property_ object. The '@' symbol is used to declare a decorator.

### Trival Decorator

A decorator can be as basic as you want it to be. It can return anything, though typically decorators return the same type of object they are decorating. 

### Decorator Functions

A decorator function acts as a wrapper around some object. It allows you to add features to a function without changing the function itself. The only argument will be the function that the decorator itself will modify.

### Decorator Classes

A class can also be used to implement a decorator. The advantage of this is the class can keep state, so that the replacement function can update information stored at the class level.

If the decorator _does not_ have any parameters, the class must have both _(dunder) init()_ and _(dunder) call_. 

### Decorator parameters

You can pass a decorator as a parameter. Although requiring a little more ingenuity, it can be a very useful tool. There are 8 combos of possible decorators. 

### Creating classes at runtime

A class can be created programmatically, without the use of the _class_ statement. This is done by the syntax:

__type("name", (base_class, ...), {attributes})__

## Monkey Patching

This term refers to the technique of changing the behavior of an object by adding, replacing, or deleting attributes from outside the object's class definition. It can be used for:
    - Replacing methods, attributes, or functions
    - Modifying a third-party object for which you do not have access
    - Adding behavior to objects in memory

This can cause some hard-to-debug problems. So be careful with using it.

## Metaclasses

Are metaclasses needed? Kinda sorta. You could opt to replace them with _Decorators_ or _inheritence_, but there are a few special cases that can be useful:
    - modifying a class name
    - modifying the list of base classes.

__Django__ is a popular framework that uses Metaclasses. 

Metaclasses can be used to create a class. It provides extra functionality at __class creation time__, not __instance creation time__. The metaclasses can do many things a normal class can do, it is just different in how classes can access them. Metaclasses _share_ data with all other classes.

A classic use case for metaclasses is to create a _singleton_ class. These are often used for loggers, config data, and database connections. 

## Descriptors

These are the underlying foundation behind a lot of Python _magic_. A __descriptor__ is an attribute tha has custom methods for getting, setting, or deleting itself. They _MUST_ implement at least one of the following methods:
    - (dunder)get(self, instance, owner=None)
    - (dunder)set(self, instance, value)
    - (dunder)delete(self, instance)

These methods are invoked when they are attributes on an object. 
