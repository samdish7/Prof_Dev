#!/usr/bin/env python


def main():
    name = "Guido"
    x = void(name)     # Calling void directly not actually passing a function
    print(x, type(x))  # but void() does not care it always returns 42

    print(hello, type(hello))  # hello is now the integer 42, not a function


def void(old_function):
    return 42                  # replace function with 42


@void                          # decorate hello() function
def hello():
    print("Hello, world")


if __name__ == '__main__':
    main()
