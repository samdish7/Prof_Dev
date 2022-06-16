# Exercise 1 main; Creating a Person class and testing it

# Test the class

from person import Person

def main():
    p1 = Person("Sam Disharoon", "24", "Male")
    p2 = Person("Jayson Tatum", "24", "Male")
    p3 = Person("Jaylen Brown", "25", "Male")
    print(p1)
    print(p2)
    print(p3)

    p3.name = "Mahcus Smaht"
    p3.age = 28
    print(p3)

if __name__ == "__main__":
    main()

