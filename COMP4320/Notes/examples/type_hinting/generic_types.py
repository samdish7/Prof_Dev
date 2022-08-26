#!/usr/bin/env python
from typing import TypeVar, Sequence
Choice = TypeVar('Choice')


def third(coll: Sequence[Choice]) -> Choice:
    return coll[2]


print(third([1, 2, 3]), third(("A", "B", 5, "C")), third('Something'))
