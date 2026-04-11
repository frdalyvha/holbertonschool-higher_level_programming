#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argc = len(sys.argv) - 1
    if argc == 0:
        print("0 arguments.")
    else:
        print("{} argument{}:".format(argc, "s" if argc > 1 else ""))
        for i in range(1, argc + 1):
            print("{}: {}".format(i, sys.argv[i]))
