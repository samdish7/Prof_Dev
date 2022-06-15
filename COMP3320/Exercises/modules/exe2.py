# Exercise 2 main file; Create a new file with the same name as a previous file, import them both and use them both

# This will demonstrate my exercise 2 module

import exe1_mod as m1
import my_mod as m2

def main():
    m1.func1()
    m1.func2(10)
    m2.func1()

if __name__ == '__main__':
    main()

