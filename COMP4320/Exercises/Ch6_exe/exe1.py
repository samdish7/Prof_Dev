#same as Ch3 exercise 1, but using generators instead of list comprehension
pres_file = open("data/presidents.txt")
pres = pres_file.readlines()
split_pres = (p.split(":") for p in pres)
upper_pres = ([p[1].upper(), p[2].upper()] for p in split_pres)
[print(f"{p[1]}, {p[0]}") for p in upper_pres]

