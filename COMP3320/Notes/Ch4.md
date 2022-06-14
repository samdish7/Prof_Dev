# Ch. 4: Collections; Sam Disharoon; 20220614

## Objectives

Different kinds of collections are as follows:
* Lists/Arrays
* Dictionaries
* Tuple
* Sets
* Maps

These are a good way to store large amounts of data without declaring variables for each one. Why write out 100 different ints when you can store them all in 1 data structure

Plenty of functions that go along with these structures, and plenty of documentation on them

Lists act similarly to vectors in c++

All of these structures are created using their respective _constructors_ such as:
* list()
* tuple()
* set()
* dict()

The above are all default constructors, you can utilize other constructors at will

### Lists

A list is an ordered data structure holding zero or more objects

Can be created in several ways:
* list()
* pair of square brakcets to denote an empty list
* pair of square brackets with values seperated by a comma

Indexing starts at 0

You can unpack lists, this means you can take each element and store them into seperate elements by accesses them through indexing.

### Tuples

This is an ordered, _immutable_ collection data structure.

This is similar to a list, but it cannot be changed, therefore it is more effiecent for static data. Such as ordered pairs, coordinates, etc...

Easier to use than a list, but is limited into what it can do since it doesn't change

### Sets

A set is an unordered collection without duplicates

Can be created using _set()_, {} to denote an empty set, or {} with values seperated by a comma. If a duplicate is entered, it will simply be ignored

Plenty of different methods for sets, including but not limited to:
* add()
* remove()
* update()
* discard()
* pop()
* clear()
* issuperset()/issubset() 

Key operators are: 
* | ~> union()
* & ~> intersect()
* - ~> difference()
* ^ ~> symmetric_difference()

Plenty of examples using these functions/operations in the _exercises_ directory

### Dictionaries

A dict is an unordered collection of entries

Each containts a key-value pair, which is often referred to as a hash or map in other langauges

This is good for storing large amounts of data with constant look-up time

You declare one by:
* dict()
* placing a comma-seperated list of key-value pairs within braces
* adding a key-value pair through assignment

The _get()_ method is useful because you are able to retrieve a value without throwing a __KeyError__ exception. Instead it just returns __None__

### Sorting Collections

You can use the _sort()_ method to sort the list in place, or the _sorted()_ method that takes an iterable object as its parameter and returns a new sorted list

A keyword parameter _reverse_ allows you to return the list in reverse order. You can also specify your own custom sort by giving the argument a certain _key_ value

You can use these functions on all of the data collections we have gone over today.



Examples of how to create and use one is also in exercises
