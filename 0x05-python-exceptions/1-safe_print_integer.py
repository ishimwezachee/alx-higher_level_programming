#!/usr/bin/python3
def safe_print_integer(value):
    try:
        if value % 1 == 0:
            print("{:d}".format(value), end='')
        else:
            print("{} is not an integer".format(value, end='')
    except Exception as err:
            print(err)
