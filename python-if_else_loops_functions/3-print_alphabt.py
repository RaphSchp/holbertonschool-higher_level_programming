#!/usr/bin/python3
for abc in range(97, 123):
    if abc != ord('e') and abc != ord('q'):
        print("{}".format(chr(abc)), end="")
