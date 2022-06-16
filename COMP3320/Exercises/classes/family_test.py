# Testing class for exercises 2 & 3; Create a Family class which has two parents and a list of children. Also add overloaded operators to compare the amount of children each family has

from family import Family
from person import Person

def main():
    parent1 = Person("Heather", 45, "F")
    parent2 = Person("Bill", 45, "M")
    kid1 = Person("Johnie", 2, "M")
    kid2 = Person("Janie", 3, "F")
    myFamily = Family(parent1, parent2, kid1, kid2)
    family2 = myFamily
    kid3 = Person("Paulie", 1, "M")
    myFamily.add(kid3)
    print(myFamily)

    print(myFamily > family2)
    print(myFamily < family2)
    print(myFamily == family2)


if __name__ == "__main__":
    main()

