# Exercise 3; Write a program that will sort all of its command line arguments

import sys



def main():
    args = sys.argv
    print("Unsorted Args:", args)
    print("Sorted Args:", sorted(args))

# Exercise 4; Sam Disharoon

# This will sum up all the command line args and also give their average

    print("List of Args:", args)
    total = 0
    ave = 1
    for i in args:
        if i.isnumeric():
            i = int(i)
            total += i
    ave = total / len(args)
    print((total,ave))

if __name__ == '__main__':
    main()

