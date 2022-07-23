import base
from ch5 import EXPECTED, NOT_EXPECTED

EXPECTED += [
    "Test file0 OK59263!",
    "Test fstat OK59263!",
    "Test link OK59263!",
    "Test mass open/unlink OK59263!"
]

EXPECTED = list(set(EXPECTED) - set([
    "Test set_priority OK59263!"
]))

TEMP = [
    # "ch6 Usertests passed59263!",
]

if __name__ == '__main__':
    base.test(EXPECTED + TEMP, NOT_EXPECTED)
