#!/usr/bin/python3
def uniq_add(my_list=[]):
    ul = set(my_list)
    n = 0

    for i in ul:
        n += i

    return (n)
