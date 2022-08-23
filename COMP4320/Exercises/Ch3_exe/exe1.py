# using list comprehension to display first and last name in all upper case
pres = open("data/presidents.txt").readlines()
split_pres = [p.split(":") for p in pres]
upper_pres = [[p[1].upper(), p[2].upper()] for p in split_pres]
[print(f"{p[1]}, {p[0]}") for p in upper_pres]
