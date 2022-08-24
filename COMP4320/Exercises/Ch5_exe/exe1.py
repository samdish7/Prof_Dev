# counting the extensions of the current directory. dir is passed in through CLI
from collections import Counter as C
import sys
import os

# get path and current dir
path = sys.argv[1]
d = os.listdir(path)
c = C()

# make counter go
for l in d:
    if l.find(".") == -1:
        continue
    item = l.split(".")
    c[item[1]] += 1

# print results
for i, c in sorted(c.items()):
    print(i,c)

