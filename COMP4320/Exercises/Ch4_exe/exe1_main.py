# main for exercise 1
from president import President as P
p_file = open("data/presidents.txt")
p = P(16, p_file)
p.print_p()
