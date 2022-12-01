#!/usr/bin/python3

for i in range(0, 100):
    u = i % 10
    t = i // 10
    if u > t and u != t:
        print("{:02d}".format(i), end="")
        if i != 89:
            print(", ", end="")
        else:
            print("\n", end="")
