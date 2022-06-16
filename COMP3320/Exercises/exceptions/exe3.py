# Exercise 3; Similar to 1 and 2, but with a twist. Get the user to enter integers and sum them up at the end, but only allow them to exit using the Ctrl-D or entering 'end'. All else will get caught

# text various exceptions

def main():
    usrList = []
    while True:
        print("Enter some integers, Enter 'end' to quit")
# Add try/catch
        try:
            i = input()
            if i == 'end':
                break
            else:
                i = int(i)
                usrList.append(i)
# handle errors
        except ValueError:
            print("Invalid input")
        except KeyboardInterrupt:
            print("Nice try, enter 'end' if you want to quit")
        except EOFError:
            print("Fine, have it your way\n")
            break
    total = 0
    for i in usrList:
        total += i
    out = "The sum of all your integers is: {}".format(total)
    print(out)

if __name__ == '__main__':
    main()

