# read the pickled data (did not finish)
import pickle as pic
from pprint import pprint

with open("potus.pic", "rb") as in_file:
    while True:
        try:
            pic_data = pic.load(in_file)
            pprint(pic_data)
        except (EOFError):
            break

