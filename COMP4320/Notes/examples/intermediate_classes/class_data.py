#!/usr/bin/env python


class Rabbit:
    LOCATION = "the Cave of Caerbannog"  # class data

    def __init__(self, weapon):
        self.weapon = weapon

    def display(self):
        fmt = "This rabbit guarding {} uses {} as a weapon"

        # access class data Location from class Rabbit
        print(fmt.format(Rabbit.LOCATION, self.weapon))

        # access class data Location from class Rabbit
        # print(fmt.format(self.LOCATION, self.weapon))


r1 = Rabbit("a nice cup of tea")
r1.display()

r1 = Rabbit("big pointy teeth")
r1.display()
