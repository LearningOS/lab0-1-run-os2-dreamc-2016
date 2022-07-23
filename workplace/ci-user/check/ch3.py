import base
from ch2 import EXPECTED, NOT_EXPECTED

EXPECTED += [
    r"get_time OK59263! (\d+)",
    "Test sleep OK59263!",
    r"current time_msec = (\d+)",
    r"time_msec = (\d+) after sleeping (\d+) ticks, delta = (\d+)ms!",
    "Test sleep1 passed59263!",
    "Test write A OK59263!",
    "Test write B OK59263!",
    "Test write C OK59263!",
]

EXPECTED += [
    "string from task info test",
    "Test task info OK59263!",
]

if __name__ == "__main__":
    base.test(EXPECTED, NOT_EXPECTED)
