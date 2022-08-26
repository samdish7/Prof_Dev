from dataclasses import dataclass


@dataclass
class Fraction:
    num: int
    denom: int


f1 = Fraction(1, 2)
f2 = Fraction(3, 4)
