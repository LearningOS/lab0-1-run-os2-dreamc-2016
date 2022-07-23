import base
from ch3 import EXPECTED, NOT_EXPECTED


EXPECTED += [
    "Test 04_1 OK59263!",
    "Test 04_4 test OK59263!",
    "Test 04_5 ummap OK59263!",
    "Test 04_6 ummap2 OK59263!",
]

NOT_EXPECTED += [
    "Should cause error, Test 04_2 fail!",
    "Should cause error, Test 04_3 fail!",
]

if __name__ == "__main__":
    base.test(EXPECTED, NOT_EXPECTED)
