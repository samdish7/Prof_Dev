#!/usr/bin/env python
import re
from functools import partial


def main():
    # create partial function that "preloads" range() with arguments 0 and 25
    count_by = partial(range, 0, 25)

    # call partial function with parameter, 0 and 25 automatically passed in
    print(list(count_by(1)), list(count_by(3)), list(count_by(5)), sep='\n')

    # create partial function that embeds pattern in re.search()
    has_a_number = partial(re.search, r'\d+')

    strings = ['abc', '123', 'abc123', 'turn it up to 11', 'blah blah']

    for s in strings:
        print("{}:".format(s), end=' ')
        if has_a_number(s):  # call re.search() with specified pattern
            print("YES")
        else:
            print("NO")


if __name__ == '__main__':
    main()
