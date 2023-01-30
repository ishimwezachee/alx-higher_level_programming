#!/usr/bin/python3 
def safe_print_list_integers(my_list=[], x=0):
    index = 0
    for i in range(x):
        try:
            if isinstance(my_list[i],int):
                print(my_list[i], end="")
                index +=1
        except Exception as error:
            print(error)
    print()
    return index


