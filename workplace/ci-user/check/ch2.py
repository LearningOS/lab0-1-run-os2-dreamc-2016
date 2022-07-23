import base

EXPECTED = [
    "Hello, world from user mode program!",
    "Test power_3 OK59263!",
    "Test power_5 OK59263!",
    "Test power_7 OK59263!",
]

TEMP = []

NOT_EXPECTED = [
    "FAIL: T.T",
]

if __name__ == "__main__":
    base.test(EXPECTED + TEMP, NOT_EXPECTED)
