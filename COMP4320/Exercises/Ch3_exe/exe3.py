# Demonstrating generator functions by redoing the first exercise
def pres_gen():
    with open("data/presidents.txt") as file_in:
        for l in file_in:
            l = l.split(":")
            l = [l[2], l[1]]
            yield l
for li in pres_gen():
    print(f"{li[0]} {li[1]}")

