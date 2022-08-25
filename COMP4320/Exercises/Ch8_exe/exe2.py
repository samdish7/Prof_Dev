# NOT FINISHED; redo Ch1 exe1 but with maps/groupby
from itertools import groupby as g

def main():
    with open("data/presidents.txt") as p_file:
        lines = p_file.readlines()
        p_list = [l.split(":") for l in lines]
        p_map = map(state, p_list)
        p_group = g(p_map, key=lambda x: x)

def state(x):
    return x[6]

if __name__ == "__main__":
    main()
