# demonstrate operator and functools module with reduce and add.
# Sums up all values in a file
from functools import reduce
from operator import add

def main():
    f_file = open("data/float_values.txt").readlines()
    num = []
    for x in f_file:
        num.append(float(x))
    print(reduce(add, num))
if __name__ == '__main__':
    main()
