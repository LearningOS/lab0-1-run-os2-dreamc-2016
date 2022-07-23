import base
from ch4 import EXPECTED, NOT_EXPECTED

EXPECTED += [
    r"Test getpid OK59263! pid = (\d+)",
    "Test spawn0 OK59263!",
    "Test wait OK59263!",
    "Test waitpid OK59263!",
    "Test set_priority OK59263!",
]

EXPECTED = list(set(EXPECTED) - set([
    "string from task info test",
    "Test task info OK59263!",
]))

TEMP = [
    # "ch5 Usertests passed59263!",
]

if __name__ == '__main__':
    base.test(EXPECTED + TEMP, NOT_EXPECTED)
