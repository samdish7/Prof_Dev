# Exercise 1 main; Define a few functions and place them in a module, proceed to use them

# This is where I will perform operations from the functions I import
from exe1_mod import func1 as f1
from exe1_mod import func2 as f2

def main():
    f1()
    f2(10)

if __name__ == '__main__':
    main()

