#even more list comprehension by tweaking the output and sorting by DOB
pres_file = open("data/presidents.txt")
pres = pres_file.readlines()
split_pres = [p.split(":") for p in pres]
dob_pres = [(p[1], p[2], p[3], p[9].replace("\n", "")) for p in split_pres]
[print(p) for p in sorted(dob_pres, key = lambda x : x[2])]

