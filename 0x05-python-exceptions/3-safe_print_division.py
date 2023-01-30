#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a/b
    except ZeroDivivisionError:
        print("can'dive with zero")
        return None;
    else:
        print("{}".format(result)
    finally:
        return None

