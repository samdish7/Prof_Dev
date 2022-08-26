#!/usr/bin/env python

from collections import defaultdict

dd = defaultdict(lambda: 0)  # create defaultdict with function that returns 0

dd['spam'] = 10  # assign some values to the dict
dd['eggs'] = 22

print(dd['spam'], dd['eggs'])
print(dd['foo'])  # missing key 'foo' invokes function and returns 0
