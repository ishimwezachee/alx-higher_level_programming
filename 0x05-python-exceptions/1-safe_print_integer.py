#!/usr/bin/python3
def safe_print_integer(value):
    try:
        if int(value):
            print("{:d}".format(value, end=''))
        else:
            print("{} is not an integer".format(value, end=''))
    except Exception as err:
            print(err)
