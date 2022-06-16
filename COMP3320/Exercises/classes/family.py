# Family class definition

from person import Person

# Class definition for the family class
class Family:

# initialize the parents and children
    def __init__(self, p1, p2, *c):
        self._parent1 = p1
        self._parent2 = p2
        self._children = []
        for i in c:
            self._children.append(i)
# create print statement
    def __str__(self):
        fmt ="Parent 1: {}|Age: {}|Gender: {}\nParent 2: {}|Age: {}|Gender: {}\n".format(
                                                                                    self.parent1.name, self.parent1.age, self.parent1.gender,
                                                                                    self.parent2.name, self.parent2.age, self.parent2.gender
                                                                                    )
        fmt = fmt + "\n"
        count = 1
        for i in self.children:
            fmt = fmt + ("Child {}: {}|Age {}|Gender {}\n".format(count, i.name, i.age, i.gender))
            count += 1
        return fmt

    @property
    def parent1(self):
        return self._parent1
     
    @property 
    def parent2(self):    
        return self._parent2
   
    @property
    def children(self):
        return self._children
       
# setters
    @parent1.setter
    def p1(self, p):
        self._parent1 = p

    @parent2.setter
    def parent2(self, p):
        self._parent2 = p
    
    @children.setter
    def children(self, c):
        self._children = c


# create add function
    def add(self, child):
        self._children.append(child)

# create overloaded methods

    def __gt__(self, other):
        return len(self._children) >len(other._children)


    def __lt__(self, other):
        return len(self._children) >len(other._children)

    def __eq__(self, other):
        return len(self._children) == len(other._children)

