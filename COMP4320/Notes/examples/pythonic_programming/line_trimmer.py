#!/usr/bin/env python


def trimmed(file_name):
    with open(file_name) as file_in:
        for line in file_in:
            # existence of a 'yield' causes function to return a generator
            yield line.rstrip()


# looping over the a generator object returned by trimmed()
for trimmed_line in trimmed('../data/mary.txt'):
    print(trimmed_line)
