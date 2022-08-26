#!/usr/bin/env python
from multiple_inheritance import AnimalBase, CanBark, CanFly


class Dog(CanBark, AnimalBase):  # inherit from mixin and primary base class
    pass


class Sparrow(CanFly, AnimalBase):  # inherit from mixin and primary base class
    pass


def main():
    d = Dog('Dennis')
    print(d.get_id())  # Dog inherits get_id() from AnimalBase
    print(d.bark())    # Dog inherits bark() from CanBark mixin
    print()

    s = Sparrow('Steve')
    print(s.get_id())  # Sparrow inherits get_id() from AnimalBase
    print(s.fly())     # Sparrow inherits fly() from CanFly mixin
    print()

    print("Sparrow mro:", Sparrow.mro())
    print()
    print("Dog mro:", Dog.mro())


if __name__ == '__main__':
    main()
