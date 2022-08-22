# do work here
pres_file = open("../data/presidents.txt")
dates = list()

# make each line into a list then extract names/dates
state_list = pres_file.readlines()
for i in state_list:
    line = i.split(":")
    dates.append((line[1], line[3],line[4]))

print("Enter a president's last name:")
name = input()
for n in dates:
    if name.lower() in n[0].lower():
        if "None".lower() in n[2].lower():
            print(f'{n[0]}, {n[1]}, ***')
        else:
            print(f'{n[0]}, {n[1]}, {n[2]}')

