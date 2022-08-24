# making a faux range function using a generator class

class FauxRange:
    def __init__(self, *args):
        self.start = 0
        self.step = 1
        arg_count = len(args)
        if arg_count == 1:
            self.stop = args[0]
        elif arg_count == 2:
            self.start, self.stop = args
        elif arg_count == 3:
            self.start, self.stop, self.step = args
        else:
            raise TypeError(f"FauxRange expected 1 to 3 args, got {arg_count}")
        self.current = self.start

    # iter returns the iterator (i.e., object that implements __next__)
    def __iter__(self):
        '''Returns self as iterator object'''
        return self

    # next returns next value
    def __next__(self):
        if self.current < self.stop:
            current = self.current
            self.current += self.step
            return current
        else:
            raise StopIteration()

def main():
    faux = FauxRange(10) 
    for value in faux:
        print(value)  
    

# testing
if __name__ == '__main__':
    main()
