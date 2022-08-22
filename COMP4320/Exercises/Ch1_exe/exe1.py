# do work here
pres_file = open("../data/presidents.txt")
state = dict()

# make each line into a list then create the dict
state_list = pres_file.readlines()
for i in state_list:
    line = i.split(":")
    curr = line[6]
    if state.get(curr):
        count = state.get(curr)
        state.update({curr : count + 1})
    else:
        state.update({curr : 1})

# print out the dict in order using sorted function
for x,y in sorted(state.items(), key=lambda p:p[1]):
    print(x,y)
                       
