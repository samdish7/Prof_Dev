# Exercise 2; Same thing as 1, but now dealing with negative numbers

# text various exceptions

def main():
    myList = [1,2,3,4,56,7,8,19,21,10]
    while True:
        print("Enter an index from 1-10, Enter 'end' to quit")
# Add try/catch
        try:
            i = input()
            if i == 'end':
                break
            else:
                i = int(i)
                if i < 1:
                    raise IndexError("Error! Index position cannot be less than 1!")
                out = "Number at position {}: {}".format(i, myList[i-1])
            print(out)
# handle errors
        except ValueError:
            print("Invalid input")
        except IndexError as ie:
            print("Illegal Value:", ie)
    print("Bye!")

if __name__ == '__main__':
    main()

