#!/usr/bin/env python
from typing import Union


def apartment_info(apartment: Union[int, str]) -> None:
    prefix = "#" if isinstance(apartment, int) else ""
    return f'Apartment {prefix}{apartment}'


print(apartment_info(12), apartment_info("F"))
