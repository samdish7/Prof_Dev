#!/usr/bin/env python

# A list of 4-element tuples
people = [
    ('Joe', 'Schmoe', 'Burbank', 'CA'),
    ('Mary', 'Rattburger', 'Madison', 'WI'),
    ('Jose', 'Ramirez', 'Ames', 'IA'),
]


# A function that takes 4 parameters
def person_record(first_name, last_name, city, state):
    print("{} {} lives in {}, {}".format(first_name, last_name, city, state))


for person in people:  # Each person is a 4-element tuple from people
    # *person unpacks the tuple into four individual parameters
    # This is also sometimes referred to as the "splat operator"
    person_record(*person)
