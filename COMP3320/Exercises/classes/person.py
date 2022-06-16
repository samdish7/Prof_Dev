# Person Class definition;

class Person:
    def __init__(self, n, a, g):
        self._name = n
        self._age = a
        self._gender = g

# getters

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age


    @property
    def gender(self):
        return self._gender

# setters

    @name.setter
    def name(self, name):
        self._name = name
    
    @age.setter
    def age(self, age):
        self._age = age
    
    @gender.setter
    def gender(self, gender):
        self._gender = gender

# print person

    def __str__(self):
        return "Name: {}|Age: {}|Gender: {}".format(self.name, self.age, self.gender)

