# president class 
from datetime import date as d

# class definition
class President():
    # init method
    def __init__(self, index, p_file):
        # split indicated line and extract values
        p = p_file.readlines()
        tar_line = p[index-1].split(":")
        # normal variables
        self._term_number = index
        self._first_name = tar_line[2]
        self._last_name = tar_line[1]
        self._birth_place = tar_line[5]
        self._birth_state = tar_line[6]
        self._party = tar_line[9]

        # not so normal variables
        bd = tar_line[3].split("-")
        self._birth_date = d(int(bd[0]), int(bd[1]), int(bd[2]))
        dd = tar_line[4].split("-")
        self._death_date = d(int(dd[0]), int(dd[1]), int(dd[2]))
        tsd = tar_line[7].split("-")
        self._term_start_date = d(int(tsd[0]), int(tsd[1]), int(tsd[2]))
        ted = tar_line[8].split("-")
        self._term_end__date = d(int(ted[0]), int(ted[1]), int(ted[2]))
    # print data
    def print_p(self):
        print(f"President #{self._term_number}: {self._first_name} {self._last_name}")
        print(f"Born at {self._birth_place}, {self._birth_state} on {self._birth_date}")

