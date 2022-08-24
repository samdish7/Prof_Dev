# uses an iterator function to determine which siblings are not friends
def sibling_rivalry(s, f):
    friend = set(s) ^ set(f)
    return iter(friend)
    
# main class defintion
def main():
    s = [("Sam", "Bob"), ("Martha", "Tyrone"), ("Keegan", "Will", "Jenna"), ("Joe", "Abby", "Mariah")]
    f = [s[0], s[2]]
    it = sibling_rivalry(s, f)
    print("Siblings whom are not friends:")
    for i in it:
        for x in range(0,len(i)):
            print(i[x], end = " ")
        print()

if __name__ == "__main__":
    main()
