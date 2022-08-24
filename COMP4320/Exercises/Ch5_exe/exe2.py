#save president data through named tuple & pickling
from collections import namedtuple as nt
import pickle as pic

pres = nt('President', 'lname fname bp bs party')
p = list()
p_file = open("data/presidents.txt").readlines()

for pre in p_file:
    pr = pre.split(":")
    cur_p = pres(pr[1], pr[2], pr[5], pr[6], pr[9])
    p.append(cur_p)

with open('potus.pic', 'wb') as o_file:
    for obj in p:
        o = [obj[0].strip("\n"), obj[1].strip("\n"), obj[2].strip("\n"), obj[3].strip("\n"), obj[4].strip("\n")]
        pic.dump(o, o_file)

