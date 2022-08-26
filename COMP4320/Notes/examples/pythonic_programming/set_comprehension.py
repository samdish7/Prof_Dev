#!/usr/bin/env python

with open("../data/mary.txt") as mary_in:
    # Get unique words from file
    # Only one line (ln) is in memory at any point
    # Skip "empty" words
    s = {w.lower() for ln in mary_in for w in ln.split() if w}

print(s)
