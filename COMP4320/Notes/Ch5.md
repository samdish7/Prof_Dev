# Ch.5 Idiomatic Data Handling

## Objectives

- Distinguish between deep and shallow copying
- Set default dictionary values
- Cout items with the __Counter__ object
- Enumerate possible allowed values with __Enum__
- Define named tuples
- Use Dataclasses
- Prettyprint data structures
- Create and extract from compressed archives
- Save Python structures to the hard drive

## Deep vs Shallow copy

A _Shallow_ copy just points to a current object. A deep copy creates an entirely new object, you can call the _deepcopy_ function in the _copy_ module to create one.

## Using _OrderedDict_

Prior to 3.6, dicts were unordered. Now we can maintain keys that allow for ordering. If you use an invalid key, it causes a _KeyError_ value to come up. The _defaultdict_ class in the collections module allows you to provide a default value. 

## Counting with Counter

The _collections_ module allows for us to use a __Counter__ class. This is essentially a _defaultdict_ whose value is zero.

### Arrays

Essentially lists, just python version. It runs faster than a list but can only house one type of value. So lists are generally used more.

## Enumerated Types

It is sometimes beneficial to have an enumerated set of vaules that cannot change. A bad way to do this is to assign each variable to each possibility. This is inefficent. Use the _enum_ module to create a declaration of each data type. This is an __iterable__ type.

## Dataclasses

Dataclasses drastically simplify the definition of classes. Rather than re-implementing the dunder init method, it is possible to have a __post-init function__ called (dunder)post_init(dunder). Rather than manually defining them, use the __@dataclass__ decoractor will generate them automatically. 

## Named Tuples

A named tuple is a tuple where each element has a name, and can be accessed via the name in addition to the normal access by index. Import the _namedtupe_ class in the collections module. 

## Printing data structures

When debugging data structures, the print command is not helpful at all. This is where two options come into play. You can implement your own or do _pprint()_. _pprint()_ analyzes the data structure to determine how it will print it out for you.

## Archives

You can do a few methods to compress your code in python:
- tar --> _tarfile_ module
- zip --> _zipfile_ module

This allows the code to become more portable and easier to move. You can make an archive using the _make_archive()_ function in the _shutil_ module. 

## Serializing Data

Serializing data means taking a data structure and transforming it so it can be written to a file or other destination, and later read back into the same data structure. Python uses the _pickle_ module for data serialization. To create pickled data, use the _pickle.dump()_ or _pickle.dumps()_ functions.

Both arguments take in a data structure as the first argument, and a file as the second argument.


