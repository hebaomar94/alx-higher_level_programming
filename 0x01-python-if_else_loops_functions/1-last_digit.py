#!/usr/bin/python3

import random
number = random.randint(-10000, 10000)
if number > 0:
    w = number % 10
else:
    w = (-1 * number % 10) * -1
    msg = "Last digit of {} is {}".format(number, w, w)
    if w > 5:
        print(msg, "and is greater than 5")
    elif w < 5 and w != 0:
        print(msg, "and is less than 6 and not 0")
    else:
        print(msg, "and is 0")
