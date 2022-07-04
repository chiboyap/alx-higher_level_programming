#!/usr/bin/python3


def print_reversed_list_integer(my_list=None):
    """
    A function that prints all integers of a list, in reverse order
    """
    if my_list is None:
        my_list = []
    for i in my_list[::-1]:
        print("{:d}".format(i))
