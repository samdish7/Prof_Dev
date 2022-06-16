# Python I/O; Sam Disharoon; 20220616

## Objectives

- Use Python's additional I/O capabilities beyond the _input_ and _print_ functions
- Create and use data streams to read/write to files
- read/write to text files
- Use _bytes_ and _bytearray_ to read/write to binary files
- Use the _seek_ and _tell_ methods to randomly access the contents of streams
- Use the _os_ and _os.path_ modules to work with files and directories

### Intro

You'll want to import the _sys_ module to take advantage of the more advanced I/O features. Some examples are:
- sys.stdin
- sys.stdout
- sys.stderr

These are all imported automatically, but you can directly access them through this method

### Creating your Own Data Streams

The _open()_ function opens a file and returns a data stream. If this fails, the __OSError__ is raised. The doctumentation on this function is online

Many different modes for opening are:
- r -> read
- w -> write
- x -> execute
- a -> append
- b -> binary mode
- t -> text mode
- + -> read/write

### Writing to a Text File

There are examples of writing to a file in the _Exercises/In-out_ directory

### Reading from a Text File

Use the _read()_ function to open a file to read from a file. _readline()_ allows for the reading of a single line into a string until the EOF is reached. _readlines()_ reads in an entire stream and adds each line to its own element in a list 

### bytes and bytearray Objects

If you want to write to binary files, you can use the _bytes_ and _bytearray_ objects. No encoding, decoding, or newline translation is performed. Bytes are immutable, bytearrays are mutable
