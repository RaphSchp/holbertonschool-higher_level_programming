#!/usr/bin/python3
import sys
if __name__ == "__main__":
    counter = 1
    if len(sys.argv) == 1:
        print(f"{len(sys.argv) - 1} arguments.")
    else:
        if len(sys.argv) > 2:
            print(f"{len(sys.argv) - 1} arguments:")
        else:
            print(f"{len(sys.argv) - 1} argument:")
        for i in sys.argv[1:]:
            print(f"{counter}: {i}")
            counter += 1
