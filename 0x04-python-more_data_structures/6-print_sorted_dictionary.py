#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    lo = list(a_dictionary.keys())
    lo.sort()
    for i in lo:
        print("{}: {}".format(i, a_dictionary.get(i)))
