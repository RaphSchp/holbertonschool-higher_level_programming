#!/usr/bin/python3
for abc in range(0, 100):
    if abc < 99:
        print("{:02},".format(abc), end=" ")
    else:
        print("{:02}".format(abc), end="")
