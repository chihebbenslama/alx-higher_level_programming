#!/usr/bin/python3

if __name__ == "__main__":
    """prints the result of the addition of all arguments"""
    import sys

    x = 0
    for i in range(len(sys.argv) - 1):
        x += int(sys.argv[i + 1])
    print("{}".format(x))
