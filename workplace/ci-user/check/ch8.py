import base
from ch5 import NOT_EXPECTED

EXPECTED = [
    # ch2b
    "Hello, world from user mode program!",
    "Test power_3 OK59263!",
    "Test power_5 OK59263!",
    "Test power_7 OK59263!",
    # ch3b
    r"get_time OK59263! (\d+)",
    "Test sleep OK59263!",
    r"current time_msec = (\d+)",
    r"time_msec = (\d+) after sleeping (\d+) ticks, delta = (\d+)ms!",
    "Test sleep1 passed59263!",
    "Test write A OK59263!",
    "Test write B OK59263!",
    "Test write C OK59263!",
    # ch5b
    "forktest2 test passed59263!",
    # ch6b
    "file_test passed59263!",
    # ch7b
    "pipetest passed59263!",
    # ch8b
    "mpsc_sem passed59263!",
    "philosopher dining problem with mutex test passed59263!",
    "race adder using spin mutex test passed59263!",
    "sync_sem passed59263!",
    "test_condvar passed59263!",
    "threads with arg test passed59263!",
    "threads test passed59263!",
    # ch8
    "deadlock test mutex 1 OK59263!",
    "deadlock test semaphore 1 OK59263!",
    "deadlock test semaphore 2 OK59263!",
    "ch8 Usertests passed59263!",
]


if __name__ == "__main__":
    base.test(EXPECTED, NOT_EXPECTED)
