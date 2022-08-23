# Ch.4 Intermediate Classes; 20220823

## Objectives

- Defining a class and its constructor (ctor)
- Creating object methods
- Adding properties to a class
- Working with class data and methods
- Leveraging inheritence for code reuse
- Implementing special methods
- Knowing when __NOT__ to use classes (easier on memory usage)

## What is a Class?

A _class_ is a definition that represents and _object_. This describes both data and methods. It can be just about anything that you need it to be relative to coding ability.

## Defining Classes

The __class__ keyword is used to define a class with a given name. Classes should use the _Capwords Convention_. You can define variables and methods within the class itself. 

## Object Instances

An instance of a class is an object created from a class. Each instance of an object that is created has its own internal ID which uniquely defines that object among all others.  This allows each to be their own.

All _attributes_ of data are dynamically allocated. Unlike other languages, they _CANNOT_ be made private, thus allowing you to access them using the . operator. Although the data cannot be made private, people indicate a 'private' method by inserting a _ beside the attribute. Nothing actually stops people from accessing it, but that is the intended way to go about things.

If there is a double _ as a prefix, the interpreter rewrites the attribute name to avoid naming conflicts in subclasses.

A _method_ is just a function that is inside a class.

### Constructors (ctors)

If a class defines a method named (dunder)init(dunder), it will automatically be called when an object instance is created. This is a _constructor_. The first parameter is in all functions are always called __self__. This is equivalent to __this__ in other languages. It allows an instance to reference itself. 

### Getters/Setters

Like other languages, getters/setters are good programming practices to get used to. 

## Properties

While object attributes can be accessed directly, in many cases the class needs to exercise some control over the attributes. This is where _properties_ come into play. In order to make one, you can throw the __@property__ decorator over a method. 

### Class Data

Data can be attached to the class itself, and shared among all instances. Any class attribute not overwritten by an instance attribute is also available through the instance. 

### Class Methods

If a method only needs class attributes, it can be made a class method via the __@classmethod__ decorator. The parameter of a class method is named __cls__ by strong convention.

## Inheritence

Python also supports Inheritence. This means one class takes attributes from a base class, but has it's own twist. They are allowed to overwrite existing methods, implement their own, and access its parent class by using __super()__. 

Classes can also inherit from multiple classes, this is so originally called __multiple inheritence__.

## Abstract Base Classes

The _abc_ module provides __abstract base classes__. If a method in an abstract class is designated _abstract_, it must be implemented in any derived class.

To create one, import __ABCMeta__ and __abstractmethod__ from the _abc_ module. 

## Special Methods

Python has a set of _special methods_ that can be used to make user-defined classes emulate the behavior of builtin ones. These methods can be used to define the behavior of builtin functions such as:
- str()
- len()
- repr()

which are few among the rest of available options. 

They generally take in the __self__ parameter along with at least one other depending on your needs. Can be used to override current functions

## Static Methods

A _static method_ is a utility method that is related to the class, but does not need the instance or class object. Thus it has no automatic parameter. One use case for this is to factor some kind of logic out of several methods, when the logic doesn't require any of the data in the class.
